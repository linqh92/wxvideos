Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

$script:RepoRoot = (Resolve-Path (Join-Path $PSScriptRoot '..\..')).Path
$script:KnownAccountIds = @('gzminge', 'gzxzcs', 'qycslc', 'gzcktxpp')

function Get-TargetAccountIds {
    param([string]$AccountId)

    if ([string]::IsNullOrWhiteSpace($AccountId)) {
        return $script:KnownAccountIds
    }
    if ($script:KnownAccountIds -notcontains $AccountId) {
        throw "Unknown AccountId '$AccountId'. Allowed: $($script:KnownAccountIds -join ', ')"
    }
    return @($AccountId)
}

function Get-Frontmatter {
    param([Parameter(Mandatory)][string]$Path)

    $text = [System.IO.File]::ReadAllText($Path, [System.Text.Encoding]::UTF8)
    $match = [regex]::Match(
        $text,
        '\A(?:\uFEFF)?---\s*\r?\n(?<yaml>.*?)\r?\n---\s*(?:\r?\n|$)',
        [System.Text.RegularExpressions.RegexOptions]::Singleline
    )
    $data = [ordered]@{}
    if (-not $match.Success) {
        return $data
    }

    foreach ($line in ($match.Groups['yaml'].Value -split '\r?\n')) {
        $item = [regex]::Match($line, '^([A-Za-z_][A-Za-z0-9_-]*):\s*(.*)$')
        if (-not $item.Success) { continue }
        $key = $item.Groups[1].Value
        $value = $item.Groups[2].Value.Trim()
        if (($value.StartsWith('"') -and $value.EndsWith('"')) -or
            ($value.StartsWith("'") -and $value.EndsWith("'"))) {
            $value = $value.Substring(1, $value.Length - 2)
        }
        $data[$key] = $value
    }
    return $data
}

function Get-MetadataValue {
    param(
        [Parameter(Mandatory)][System.Collections.IDictionary]$Metadata,
        [Parameter(Mandatory)][string[]]$Names
    )
    foreach ($name in $Names) {
        if ($Metadata.Contains($name) -and -not [string]::IsNullOrWhiteSpace([string]$Metadata[$name])) {
            return [string]$Metadata[$name]
        }
    }
    return ''
}

function Get-RepositoryRelativePath {
    param([Parameter(Mandatory)][string]$Path)
    return [System.IO.Path]::GetRelativePath($script:RepoRoot, $Path).Replace('\', '/')
}

function Get-TitleFromFilename {
    param([Parameter(Mandatory)][string]$Path)
    $name = [System.IO.Path]::GetFileNameWithoutExtension($Path)
    return ($name -replace '^\d{4}-\d{2}-\d{2}｜', '')
}

function Write-JsonLines {
    param(
        [Parameter(Mandatory)][string]$Path,
        [Parameter(Mandatory)][AllowEmptyCollection()][object[]]$Rows
    )
    $parent = Split-Path -Parent $Path
    [System.IO.Directory]::CreateDirectory($parent) | Out-Null
    $lines = @($Rows | ForEach-Object { $_ | ConvertTo-Json -Compress -Depth 8 })
    $content = if ($lines.Count -gt 0) { ($lines -join "`n") + "`n" } else { '' }
    [System.IO.File]::WriteAllText($Path, $content, (New-Object System.Text.UTF8Encoding($false)))
}

function Read-JsonLines {
    param([Parameter(Mandatory)][string]$Path)
    if (-not (Test-Path -LiteralPath $Path)) { return @() }
    return @(
        Get-Content -LiteralPath $Path -Encoding UTF8 |
            Where-Object { -not [string]::IsNullOrWhiteSpace($_) } |
            ForEach-Object { $_ | ConvertFrom-Json }
    )
}

function Convert-GroupsToObject {
    param(
        [Parameter(Mandatory)][AllowEmptyCollection()][object[]]$Rows,
        [Parameter(Mandatory)][string]$Property
    )
    $result = [ordered]@{}
    foreach ($group in @($Rows | Where-Object {
        $_.PSObject.Properties.Name -contains $Property -and
        -not [string]::IsNullOrWhiteSpace([string]$_.$Property)
    } | Group-Object -Property $Property | Sort-Object Name)) {
        $result[$group.Name] = $group.Count
    }
    return [pscustomobject]$result
}

