param([string]$AccountId)

. (Join-Path $PSScriptRoot 'index-common.ps1')

foreach ($id in (Get-TargetAccountIds -AccountId $AccountId)) {
    $vault = Join-Path $script:RepoRoot "accounts\$id\内容库"
    $historyIndex = Join-Path $vault '01-历史内容\_history-index.jsonl'
    $ideaIndex = Join-Path $vault '03-选题规划\灵感库\_idea-index.jsonl'
    $candidateIndex = Join-Path $vault '03-选题规划\_candidate-index.jsonl'

    if (-not (Test-Path -LiteralPath $historyIndex)) { & (Join-Path $PSScriptRoot 'rebuild-history-index.ps1') -AccountId $id }
    if (-not (Test-Path -LiteralPath $ideaIndex)) { & (Join-Path $PSScriptRoot 'rebuild-idea-index.ps1') -AccountId $id }
    if (-not (Test-Path -LiteralPath $candidateIndex)) { & (Join-Path $PSScriptRoot 'rebuild-candidate-index.ps1') -AccountId $id }

    $history = @(Read-JsonLines -Path $historyIndex)
    $ideas = @(Read-JsonLines -Path $ideaIndex)
    $candidates = @(Read-JsonLines -Path $candidateIndex)
    $historyWithMonth = @($history | ForEach-Object {
        $month = if ([string]$_.publish_date -match '^(\d{4}-\d{2})') { $Matches[1] } else { '' }
        [pscustomobject]@{ publish_month = $month }
    })

    $summary = [pscustomobject][ordered]@{
        account_id = $id
        generated_from = @(
            Get-RepositoryRelativePath -Path $historyIndex
            Get-RepositoryRelativePath -Path $ideaIndex
            Get-RepositoryRelativePath -Path $candidateIndex
        )
        history_index_sha256 = (Get-FileHash -LiteralPath $historyIndex -Algorithm SHA256).Hash.ToLowerInvariant()
        history_count = $history.Count
        idea_count = $ideas.Count
        candidate_count = $candidates.Count
        history_by_month = Convert-GroupsToObject -Rows $historyWithMonth -Property 'publish_month'
        history_by_business_line = Convert-GroupsToObject -Rows $history -Property 'business_line'
        history_by_theme = Convert-GroupsToObject -Rows $history -Property 'theme'
        history_by_content_type = Convert-GroupsToObject -Rows $history -Property 'content_type'
        idea_by_status = Convert-GroupsToObject -Rows $ideas -Property 'status'
        candidate_by_status = Convert-GroupsToObject -Rows $candidates -Property 'status'
        note = '该 JSON 是可重复生成的机器派生摘要；原内容地图、缺口分析、重复检查和月度复盘 Markdown 保留为人工资产，不在本脚本中覆盖。'
    }

    $output = Join-Path $vault '04-内容复盘\_derived-assets-summary.json'
    $json = $summary | ConvertTo-Json -Depth 10
    [System.IO.File]::WriteAllText($output, $json + "`n", (New-Object System.Text.UTF8Encoding($false)))
    Write-Output "$id derived_summary=1 path=$(Get-RepositoryRelativePath -Path $output)"
}

