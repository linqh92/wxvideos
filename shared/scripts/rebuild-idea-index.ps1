param([string]$AccountId)

. (Join-Path $PSScriptRoot 'index-common.ps1')

foreach ($id in (Get-TargetAccountIds -AccountId $AccountId)) {
    $ideaRoot = Join-Path $script:RepoRoot "accounts\$id\内容库\03-选题规划\灵感库"
    if (-not (Test-Path -LiteralPath $ideaRoot)) {
        throw "Idea root not found: $ideaRoot"
    }

    $rows = @(
        Get-ChildItem -LiteralPath $ideaRoot -Recurse -File -Filter '*.md' |
            Where-Object { $_.Name -notlike '00-*' } |
            Sort-Object FullName |
            ForEach-Object {
                $meta = Get-Frontmatter -Path $_.FullName
                $title = Get-MetadataValue -Metadata $meta -Names @('title')
                if ([string]::IsNullOrWhiteSpace($title)) { $title = Get-TitleFromFilename -Path $_.FullName }

                [pscustomobject][ordered]@{
                    path = Get-RepositoryRelativePath -Path $_.FullName
                    title = $title
                    created = Get-MetadataValue -Metadata $meta -Names @('created', 'date')
                    status = Get-MetadataValue -Metadata $meta -Names @('status')
                    business_line = Get-MetadataValue -Metadata $meta -Names @('business_line')
                    audience = Get-MetadataValue -Metadata $meta -Names @('audience')
                    pain_scene = Get-MetadataValue -Metadata $meta -Names @('pain_scene')
                    source = Get-MetadataValue -Metadata $meta -Names @('source', 'source_type')
                }
            }
    )

    $output = Join-Path $ideaRoot '_idea-index.jsonl'
    Write-JsonLines -Path $output -Rows $rows
    Write-Output "$id idea_index=$($rows.Count) path=$(Get-RepositoryRelativePath -Path $output)"
}

