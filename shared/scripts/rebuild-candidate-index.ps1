param([string]$AccountId)

. (Join-Path $PSScriptRoot 'index-common.ps1')

$allowedStatuses = @('待核验', '可推荐', '已采用', '已发布', '已放弃')

function Convert-RecommendedFormat {
    param([string]$Value)

    switch ($Value.Trim()) {
        '短文字幕' { return 'text_broadcast' }
        '文字播报' { return 'text_broadcast' }
        '短文'     { return 'text_broadcast' }
        '口播'     { return 'spoken' }
        '真人口播' { return 'spoken' }
        '均可'     { return 'either' }
        default    { return '' }
    }
}

function Add-CandidateCard {
    param(
        [System.Collections.Generic.List[object]]$Target,
        [string]$Title,
        [System.Collections.IDictionary]$Fields,
        [string]$FilePath,
        [System.Collections.IDictionary]$FileMetadata
    )
    if ([string]::IsNullOrWhiteSpace($Title) -or $Title -eq '简短名称') { return }
    $status = if ($Fields.Contains('状态')) { [string]$Fields['状态'] } else { '' }
    if ($allowedStatuses -notcontains $status) { return }

    $scene = if ($Fields.Contains('经营场景')) { [string]$Fields['经营场景'] } else { '' }
    $pain = if ($Fields.Contains('核心痛点')) { [string]$Fields['核心痛点'] } else { '' }
    $painScene = @($scene, $pain) | Where-Object { -not [string]::IsNullOrWhiteSpace($_) }

    $cleanTitle = ($Title -replace '^选题[｜|：:]\s*', '').Trim()
    $relative = Get-RepositoryRelativePath -Path $FilePath
    $Target.Add([pscustomobject][ordered]@{
        path = "$relative#$cleanTitle"
        title = $cleanTitle
        status = $status
        business_line = if ($Fields.Contains('业务方向')) { [string]$Fields['业务方向'] } else { '' }
        theme = if ($Fields.Contains('主题')) { [string]$Fields['主题'] } else { '' }
        audience = if ($Fields.Contains('目标客户')) { [string]$Fields['目标客户'] } else { '' }
        pain_scene = ($painScene -join '；')
        content_goal = if ($Fields.Contains('内容目标')) { [string]$Fields['内容目标'] } elseif ($Fields.Contains('内容目的')) { [string]$Fields['内容目的'] } else { '' }
        service = if ($Fields.Contains('可承接服务')) { [string]$Fields['可承接服务'] } else { '' }
        recommended_format = if ($Fields.Contains('建议载体')) { Convert-RecommendedFormat ([string]$Fields['建议载体']) } else { '' }
        created = Get-MetadataValue -Metadata $FileMetadata -Names @('created', 'date')
    })
}

foreach ($id in (Get-TargetAccountIds -AccountId $AccountId)) {
    $planningRoot = Join-Path $script:RepoRoot "accounts\$id\内容库\03-选题规划"
    if (-not (Test-Path -LiteralPath $planningRoot)) {
        throw "Candidate root not found: $planningRoot"
    }

    $rows = [System.Collections.Generic.List[object]]::new()
    $files = Get-ChildItem -LiteralPath $planningRoot -Recurse -File -Filter '*.md' |
        Where-Object { $_.FullName -notlike "*\灵感库\*" } |
        Sort-Object FullName

    foreach ($file in $files) {
        $fileMeta = Get-Frontmatter -Path $file.FullName
        $currentTitle = ''
        $fields = [ordered]@{}
        $inFence = $false

        foreach ($line in (Get-Content -LiteralPath $file.FullName -Encoding UTF8)) {
            if ($line -match '^\s*(~~~|```)') {
                $inFence = -not $inFence
                continue
            }
            if ($inFence) { continue }

            $heading = [regex]::Match($line, '^###\s+(.+?)\s*$')
            if ($heading.Success) {
                Add-CandidateCard -Target $rows -Title $currentTitle -Fields $fields -FilePath $file.FullName -FileMetadata $fileMeta
                $currentTitle = $heading.Groups[1].Value.Trim()
                $fields = [ordered]@{}
                continue
            }
            if ($line -match '^#{1,2}\s+') {
                Add-CandidateCard -Target $rows -Title $currentTitle -Fields $fields -FilePath $file.FullName -FileMetadata $fileMeta
                $currentTitle = ''
                $fields = [ordered]@{}
                continue
            }
            if (-not [string]::IsNullOrWhiteSpace($currentTitle)) {
                $field = [regex]::Match($line, '^-\s*([^：:]+)[：:]\s*(.*)$')
                if ($field.Success) {
                    $fields[$field.Groups[1].Value.Trim()] = $field.Groups[2].Value.Trim()
                }
            }
        }
        Add-CandidateCard -Target $rows -Title $currentTitle -Fields $fields -FilePath $file.FullName -FileMetadata $fileMeta
    }

    $sortedRows = @($rows | Sort-Object path)
    $output = Join-Path $planningRoot '_candidate-index.jsonl'
    Write-JsonLines -Path $output -Rows $sortedRows
    Write-Output "$id candidate_index=$($sortedRows.Count) path=$(Get-RepositoryRelativePath -Path $output)"
}
