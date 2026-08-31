. (Join-Path $PSScriptRoot 'index-common.ps1')

$script:Checks = 0
function Assert-True {
    param([bool]$Condition, [string]$Message)
    if (-not $Condition) { throw "VALIDATION FAILED: $Message" }
    $script:Checks++
}

$rootAgent = [System.IO.File]::ReadAllText((Join-Path $script:RepoRoot 'AGENTS.md'))
$topicSkill = [System.IO.File]::ReadAllText((Join-Path $script:RepoRoot '.codex\skills\topic-planning\SKILL.md'))
$historyRules = [System.IO.File]::ReadAllText((Join-Path $script:RepoRoot '.codex\skills\topic-planning\references\history-vault-rules.md'))
$ideaSkill = [System.IO.File]::ReadAllText((Join-Path $script:RepoRoot '.codex\skills\idea-intake\SKILL.md'))
$textBroadcastSkill = [System.IO.File]::ReadAllText((Join-Path $script:RepoRoot '.codex\skills\text-broadcast-copywriting\SKILL.md'))
$spokenSkill = [System.IO.File]::ReadAllText((Join-Path $script:RepoRoot '.codex\skills\spoken-copywriting\SKILL.md'))
$spokenNaturalness = [System.IO.File]::ReadAllText((Join-Path $script:RepoRoot '.codex\skills\spoken-copywriting\references\chinese-spoken-naturalness.md'))
$spokenVisualSkill = [System.IO.File]::ReadAllText((Join-Path $script:RepoRoot '.codex\skills\spoken-visual-planning\SKILL.md'))
$spokenVisualRules = [System.IO.File]::ReadAllText((Join-Path $script:RepoRoot '.codex\skills\spoken-visual-planning\references\visual-aid-generation-rules.md'))
$copyCommonRules = [System.IO.File]::ReadAllText((Join-Path $script:RepoRoot 'shared\rules\copywriting-common-rules.md'))
$archiveSkill = [System.IO.File]::ReadAllText((Join-Path $script:RepoRoot '.codex\skills\publish-archive\SKILL.md'))
$stateSchema = [System.IO.File]::ReadAllText((Join-Path $script:RepoRoot 'shared\schemas\content-state-machine.md'))
$historySchema = [System.IO.File]::ReadAllText((Join-Path $script:RepoRoot 'shared\schemas\history-index-schema.md'))
$historyRebuild = [System.IO.File]::ReadAllText((Join-Path $script:RepoRoot 'shared\scripts\rebuild-history-index.ps1'))

$requiredContentFormatPaths = @(
    'shared\rules\copywriting-common-rules.md',
    '.codex\skills\text-broadcast-copywriting\SKILL.md',
    '.codex\skills\text-broadcast-copywriting\agents\openai.yaml',
    '.codex\skills\spoken-copywriting\SKILL.md',
    '.codex\skills\spoken-copywriting\references\chinese-spoken-naturalness.md',
    '.codex\skills\spoken-copywriting\agents\openai.yaml'
)
foreach ($relativePath in $requiredContentFormatPaths) {
    Assert-True (Test-Path -LiteralPath (Join-Path $script:RepoRoot $relativePath)) "missing content-format asset: $relativePath"
}

$requiredSpokenVisualPaths = @(
    '.codex\skills\spoken-visual-planning\SKILL.md',
    '.codex\skills\spoken-visual-planning\references\visual-aid-generation-rules.md',
    '.codex\skills\spoken-visual-planning\agents\openai.yaml'
)
foreach ($relativePath in $requiredSpokenVisualPaths) {
    Assert-True (Test-Path -LiteralPath (Join-Path $script:RepoRoot $relativePath)) "missing spoken-visual-planning asset: $relativePath"
}

Assert-True ($rootAgent.Contains('CURRENT_ACCOUNT') -and $rootAgent.Contains('Account Context Lock')) 'root AGENTS must define CURRENT_ACCOUNT and Account Context Lock'
Assert-True ($rootAgent.Contains('默认禁止读取其他 `accounts/*`')) 'root AGENTS must forbid other accounts by default'

$hardcoded = @('广州敏哥', '广州小张', '企业财税-老陈', '广州出口退税', '补充业务不得脱离', '成熟企业经营不得', '电商合规')
$publicText = $topicSkill + $historyRules + $ideaSkill + $textBroadcastSkill + $spokenSkill + $spokenVisualSkill + $spokenVisualRules + $copyCommonRules + $archiveSkill
foreach ($term in $hardcoded) {
    Assert-True (-not $publicText.Contains($term)) "public Skills must not hardcode account rule: $term"
}

Assert-True ($topicSkill.Contains('_history-index.jsonl') -and $topicSkill.Contains('_candidate-index.jsonl') -and $topicSkill.Contains('_idea-index.jsonl')) 'topic planning must read all three indexes'
Assert-True ($topicSkill.Contains('5～8') -and $historyRules -match '(?i)metadata') 'topic planning must use Metadata First and bounded body reads'
Assert-True (-not $historyRules.Contains('full body of the 10 most recent')) 'old latest-10 body rule must be removed'
Assert-True ($historyRules.Contains('Same Session Snapshot')) 'same-session snapshot rule must exist'
Assert-True ($historyRules.Contains('不是普通选题的默认数据源')) 'derived assets must be outside default topic context'

Assert-True ($textBroadcastSkill.Contains('shared/rules/copywriting-common-rules.md') -and $spokenSkill.Contains('shared/rules/copywriting-common-rules.md')) 'both copywriting Skills must use the shared common rules'
Assert-True ($spokenSkill.Contains('references/chinese-spoken-naturalness.md')) 'spoken Skill must load the spoken-naturalness reference'
Assert-True ($spokenNaturalness.Contains('applies ONLY to `spoken-copywriting`') -and $spokenNaturalness.Contains('MUST NOT be inherited by `text-broadcast-copywriting`')) 'spoken-naturalness reference must remain isolated from text-broadcast copywriting'
Assert-True ($rootAgent.Contains('spoken-visual-planning') -and $rootAgent.Contains('不得自动进入 `spoken-visual-planning`')) 'root AGENTS must route spoken visual planning as an explicit-only stage'
Assert-True ($rootAgent.Contains('账号视觉风格.md') -and $rootAgent.Contains('不得从账号人设与文风推断视觉风格') -and $rootAgent.Contains('不得借用其他账号视觉风格')) 'root AGENTS must define account visual style as an isolated source'
Assert-True ($spokenVisualSkill.Contains('Do NOT automatically invoke this Skill after `spoken-copywriting`.') -and $spokenVisualSkill.Contains('After delivering the requested visual-planning materials, STOP.')) 'spoken visual planning must be explicit-only and stop after delivery'
Assert-True ($spokenVisualSkill.Contains('Do not automatically:') -and $spokenVisualSkill.Contains('call image generation') -and $spokenVisualSkill.Contains('archive the content')) 'spoken visual planning must not generate images or archive automatically'
Assert-True ($spokenVisualSkill.Contains('2. accounts/{CURRENT_ACCOUNT}/内容库/00-首页与维护规则/账号视觉风格.md') -and $spokenVisualSkill.Contains('Do NOT read other accounts.')) 'spoken visual planning must require only the current account visual style'
$doNotReadOffset = $spokenVisualSkill.IndexOf('### Do NOT automatically read')
$personaPathOffset = $spokenVisualSkill.IndexOf('账号人设与文风.md')
Assert-True ($doNotReadOffset -ge 0 -and $personaPathOffset -gt $doNotReadOffset) 'spoken visual planning must place persona under the do-not-read contract'
Assert-True ($spokenVisualRules.Contains('Universal Quality Negatives') -and $spokenVisualRules.Contains('Account-Specific Style Negatives') -and $spokenVisualRules.Contains('Scene-Specific Negatives')) 'spoken visual prompts must contain universal, account, and scene negative layers'
Assert-True ($spokenVisualRules.Contains('CURRENT_ACCOUNT visual-style injection') -and $spokenVisualSkill.Contains('Account Visual DNA')) 'spoken visual prompts must inject CURRENT_ACCOUNT visual DNA'
$fixedGlobalVisualStyle = @(
    '- semi-realistic or realistic business explanatory visual;',
    '- blue-gray-white base;',
    '- small red accents only for risk;',
    '- light neutral background;',
    '- restrained financial / compliance feel;',
    '整体采用半写实或真实商业视觉风格',
    '蓝灰白主色调',
    '少量红色仅用于风险提示'
)
foreach ($term in $fixedGlobalVisualStyle) {
    Assert-True (-not $spokenVisualRules.Contains($term)) "shared visual rules must not fix account style: $term"
}
Assert-True ($rootAgent.Contains('CONTENT_FORMAT') -and $rootAgent.Contains('text_broadcast') -and $rootAgent.Contains('spoken')) 'root AGENTS must route both content formats'
Assert-True (-not $rootAgent.Contains('`video-copywriting`')) 'root AGENTS must not route formal copy to video-copywriting'
$runtimeFiles = @(
    Get-Item -LiteralPath (Join-Path $script:RepoRoot 'AGENTS.md'), (Join-Path $script:RepoRoot 'README.md')
    Get-ChildItem -LiteralPath (Join-Path $script:RepoRoot '.codex') -Recurse -File
)
foreach ($runtimeFile in $runtimeFiles) {
    $runtimeText = [System.IO.File]::ReadAllText($runtimeFile.FullName)
    Assert-True (-not $runtimeText.Contains('$video-copywriting')) "stale runtime invocation in $(Get-RepositoryRelativePath -Path $runtimeFile.FullName)"
}
Assert-True ($ideaSkill.Contains('_idea-index.jsonl') -and $ideaSkill.Contains('不得自动执行选题')) 'idea intake must update Idea Index and stop'
Assert-True ($archiveSkill.Contains('_history-index.jsonl') -and $archiveSkill.Contains('_candidate-index.jsonl')) 'archive must update history and candidate indexes'
Assert-True ($archiveSkill.Contains('以下两项必须同时成立')) 'archive must require publication and explicit archive instruction'
Assert-True ($archiveSkill.Contains('content_format') -and $archiveSkill.Contains('recommended_format')) 'archive must record actual content format instead of the recommendation'
Assert-True ($historySchema.Contains('content_type') -and $historySchema.Contains('content_format')) 'history schema must keep content type and add content format'
Assert-True ($historyRebuild.Contains('content_type =') -and $historyRebuild.Contains('content_format =')) 'history rebuild must emit content type and content format separately'
Assert-True ($stateSchema.Contains('待分析 → 可入池 → 已转选题') -and $stateSchema.Contains('待核验 → 可推荐 → 已采用 → 已发布')) 'state schema must contain both repaired state machines'

$validIdea = @('待分析', '可入池', '已转选题', '已放弃')
$validCandidate = @('待核验', '可推荐', '已采用', '已发布', '已放弃')
$validRecommendedFormats = @('text_broadcast', 'spoken', 'either')
$validContentFormats = @('text_broadcast', 'spoken')

foreach ($id in $script:KnownAccountIds) {
    $accountRoot = Join-Path $script:RepoRoot "accounts\$id"
    $vault = Join-Path $accountRoot '内容库'
    $yaml = [System.IO.File]::ReadAllText((Join-Path $accountRoot 'account.yaml'))
    Assert-True ($yaml -match "(?m)^id:\s*$id\s*$") "$id account.yaml id mismatch"
    Assert-True ((Test-Path -LiteralPath (Join-Path $vault '00-首页与维护规则\账号基本定位.md')) -and
                 (Test-Path -LiteralPath (Join-Path $vault '00-首页与维护规则\账号人设与文风.md'))) "$id positioning split missing"

    $visualStylePath = Join-Path $vault '00-首页与维护规则\账号视觉风格.md'
    Assert-True (Test-Path -LiteralPath $visualStylePath) "$id account visual style missing"
    $visualStyle = [System.IO.File]::ReadAllText($visualStylePath)
    Assert-True ($visualStyle.Contains('# Account Visual Style') -and
                 -not $visualStyle.Contains(': ""') -and
                 -not $visualStyle.Contains(': []') -and
                 -not $visualStyle.Contains('- ""')) "$id account visual style contains unresolved blank fields"

    $basic = [System.IO.File]::ReadAllText((Join-Path $vault '00-首页与维护规则\账号基本定位.md'))
    $voice = [System.IO.File]::ReadAllText((Join-Path $vault '00-首页与维护规则\账号人设与文风.md'))
    Assert-True (-not $basic.Contains('# Persona')) "$id topic positioning still contains persona block"
    Assert-True ($voice.Contains('# Persona')) "$id voice file lost persona block"

    $historyPath = Join-Path $vault '01-历史内容\_history-index.jsonl'
    $ideaPath = Join-Path $vault '03-选题规划\灵感库\_idea-index.jsonl'
    $candidatePath = Join-Path $vault '03-选题规划\_candidate-index.jsonl'
    $derivedPath = Join-Path $vault '04-内容复盘\_derived-assets-summary.json'
    foreach ($path in @($historyPath, $ideaPath, $candidatePath, $derivedPath)) {
        Assert-True (Test-Path -LiteralPath $path) "$id missing generated asset: $path"
    }

    $history = @(Read-JsonLines -Path $historyPath)
    $ideas = @(Read-JsonLines -Path $ideaPath)
    $candidates = @(Read-JsonLines -Path $candidatePath)
    $historyFiles = @(Get-ChildItem -LiteralPath (Join-Path $vault '01-历史内容') -Recurse -File -Filter '*.md')
    $ideaFiles = @(Get-ChildItem -LiteralPath (Join-Path $vault '03-选题规划\灵感库') -Recurse -File -Filter '*.md' | Where-Object { $_.Name -notlike '00-*' })

    Assert-True ($history.Count -eq $historyFiles.Count) "$id history index count mismatch"
    Assert-True ($ideas.Count -eq $ideaFiles.Count) "$id idea index count mismatch"
    foreach ($row in $history) {
        Assert-True ($row.path -like "accounts/$id/*") "$id history index leaked another account"
        Assert-True (-not [string]::IsNullOrWhiteSpace([string]$row.title) -and -not [string]::IsNullOrWhiteSpace([string]$row.publish_date)) "$id history metadata incomplete"
        if ($row.PSObject.Properties.Name -contains 'content_format' -and -not [string]::IsNullOrWhiteSpace([string]$row.content_format)) {
            Assert-True ($validContentFormats -contains [string]$row.content_format) "$id history content_format invalid"
        }
    }
    foreach ($row in $ideas) {
        Assert-True ($row.path -like "accounts/$id/*" -and $validIdea -contains $row.status) "$id idea index path/status invalid"
    }
    foreach ($row in $candidates) {
        Assert-True ($row.path -like "accounts/$id/*" -and $validCandidate -contains $row.status) "$id candidate index path/status invalid"
        if ($row.PSObject.Properties.Name -contains 'recommended_format' -and -not [string]::IsNullOrWhiteSpace([string]$row.recommended_format)) {
            Assert-True ($validRecommendedFormats -contains [string]$row.recommended_format) "$id candidate recommended_format invalid"
        }
    }
}

Write-Output "VALIDATION PASSED checks=$script:Checks accounts=$($script:KnownAccountIds.Count)"
