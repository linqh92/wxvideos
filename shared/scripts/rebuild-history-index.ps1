param([string]$AccountId)

. (Join-Path $PSScriptRoot 'index-common.ps1')

foreach ($id in (Get-TargetAccountIds -AccountId $AccountId)) {
    $historyRoot = Join-Path $script:RepoRoot "accounts\$id\内容库\01-历史内容"
    if (-not (Test-Path -LiteralPath $historyRoot)) {
        throw "History root not found: $historyRoot"
    }

    $rows = @(
        Get-ChildItem -LiteralPath $historyRoot -Recurse -File -Filter '*.md' |
            Sort-Object FullName |
            ForEach-Object {
                $meta = Get-Frontmatter -Path $_.FullName
                $title = Get-MetadataValue -Metadata $meta -Names @('title')
                if ([string]::IsNullOrWhiteSpace($title)) { $title = Get-TitleFromFilename -Path $_.FullName }
                $publishDate = Get-MetadataValue -Metadata $meta -Names @('publish_date', 'published', 'date')
                if ([string]::IsNullOrWhiteSpace($publishDate) -and $_.BaseName -match '^(\d{4}-\d{2}-\d{2})') {
                    $publishDate = $Matches[1]
                }

                [pscustomobject][ordered]@{
                    path = Get-RepositoryRelativePath -Path $_.FullName
                    title = $title
                    publish_date = $publishDate
                    business_line = Get-MetadataValue -Metadata $meta -Names @('business_line')
                    theme = Get-MetadataValue -Metadata $meta -Names @('theme')
                    content_type = Get-MetadataValue -Metadata $meta -Names @('content_type')
                    content_format = Get-MetadataValue -Metadata $meta -Names @('content_format')
                    audience = Get-MetadataValue -Metadata $meta -Names @('audience')
                    pain_scene = Get-MetadataValue -Metadata $meta -Names @('pain_scene')
                    content_goal = Get-MetadataValue -Metadata $meta -Names @('content_goal')
                    status = 'published'
                    series = Get-MetadataValue -Metadata $meta -Names @('series')
                    region = Get-MetadataValue -Metadata $meta -Names @('region')
                }
            }
    )

    $output = Join-Path $historyRoot '_history-index.jsonl'
    Write-JsonLines -Path $output -Rows $rows
    Write-Output "$id history_index=$($rows.Count) path=$(Get-RepositoryRelativePath -Path $output)"
}
