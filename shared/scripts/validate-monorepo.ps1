[CmdletBinding()]
param(
    [switch]$RulesOnly
)

. (Join-Path $PSScriptRoot 'index-common.ps1')

$script:Checks = 0
function Assert-True {
    param([bool]$Condition, [string]$Message)
    if (-not $Condition) { throw "VALIDATION FAILED: $Message" }
    $script:Checks++
}

$rootAgent = [System.IO.File]::ReadAllText((Join-Path $script:RepoRoot 'AGENTS.md'))
$readme = [System.IO.File]::ReadAllText((Join-Path $script:RepoRoot 'README.md'))
$topicSkill = [System.IO.File]::ReadAllText((Join-Path $script:RepoRoot '.codex\skills\topic-planning\SKILL.md'))
$historyRules = [System.IO.File]::ReadAllText((Join-Path $script:RepoRoot '.codex\skills\topic-planning\references\history-vault-rules.md'))
$ideaSkill = [System.IO.File]::ReadAllText((Join-Path $script:RepoRoot '.codex\skills\idea-intake\SKILL.md'))
$textBroadcastSkill = [System.IO.File]::ReadAllText((Join-Path $script:RepoRoot '.codex\skills\text-broadcast-copywriting\SKILL.md'))
$spokenSkill = [System.IO.File]::ReadAllText((Join-Path $script:RepoRoot '.codex\skills\spoken-copywriting\SKILL.md'))
$spokenNaturalness = [System.IO.File]::ReadAllText((Join-Path $script:RepoRoot '.codex\skills\spoken-copywriting\references\chinese-spoken-naturalness.md'))
$spokenVisualSkill = [System.IO.File]::ReadAllText((Join-Path $script:RepoRoot '.codex\skills\spoken-visual-planning\SKILL.md'))
$spokenVisualRules = [System.IO.File]::ReadAllText((Join-Path $script:RepoRoot '.codex\skills\spoken-visual-planning\references\visual-aid-generation-rules.md'))
$spokenVisualAgent = [System.IO.File]::ReadAllText((Join-Path $script:RepoRoot '.codex\skills\spoken-visual-planning\agents\openai.yaml'))
$copyCommonRules = [System.IO.File]::ReadAllText((Join-Path $script:RepoRoot 'shared\rules\copywriting-common-rules.md'))
$archiveSkill = [System.IO.File]::ReadAllText((Join-Path $script:RepoRoot '.codex\skills\publish-archive\SKILL.md'))
$archiveManual = [System.IO.File]::ReadAllText((Join-Path $script:RepoRoot '.codex\skills\publish-archive\references\manual-archive.md'))
$stateSchema = [System.IO.File]::ReadAllText((Join-Path $script:RepoRoot 'shared\schemas\content-state-machine.md'))
$contentIdentitySchema = [System.IO.File]::ReadAllText((Join-Path $script:RepoRoot 'shared\schemas\content-identity-schema.md'))
$handoffSchema = [System.IO.File]::ReadAllText((Join-Path $script:RepoRoot 'shared\schemas\handoff-packet-schema.md'))
$confirmedCopyDeliverySchema = [System.IO.File]::ReadAllText((Join-Path $script:RepoRoot 'shared\schemas\confirmed-copy-delivery-schema.md'))
$repoOperationSchema = [System.IO.File]::ReadAllText((Join-Path $script:RepoRoot 'shared\schemas\repo-operation-schema.md'))
$topicRecommendationSchema = [System.IO.File]::ReadAllText((Join-Path $script:RepoRoot 'shared\schemas\topic-recommendation-log-schema.md'))
$candidateSchema = [System.IO.File]::ReadAllText((Join-Path $script:RepoRoot 'shared\schemas\candidate-index-schema.md'))
$historySchema = [System.IO.File]::ReadAllText((Join-Path $script:RepoRoot 'shared\schemas\history-index-schema.md'))
$historyRebuild = [System.IO.File]::ReadAllText((Join-Path $script:RepoRoot 'shared\scripts\rebuild-history-index.ps1'))
$candidateRebuild = [System.IO.File]::ReadAllText((Join-Path $script:RepoRoot 'shared\scripts\rebuild-candidate-index.ps1'))
$repoOps = [System.IO.File]::ReadAllText((Join-Path $script:RepoRoot 'shared\scripts\wxv-ops.py'))

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

$requiredHandoffPaths = @(
    'shared\schemas\content-identity-schema.md',
    'shared\schemas\handoff-packet-schema.md',
    'shared\schemas\confirmed-copy-delivery-schema.md',
    'shared\schemas\repo-operation-schema.md',
    'shared\scripts\content-handoff.py',
    'shared\scripts\test-content-handoff.py',
    'shared\scripts\wxv-ops.py',
    'shared\scripts\test-wxv-ops.py',
    '.codex\skills\publish-archive\references\manual-archive.md'
)
foreach ($relativePath in $requiredHandoffPaths) {
    Assert-True (Test-Path -LiteralPath (Join-Path $script:RepoRoot $relativePath)) "missing content-handoff asset: $relativePath"
}

Assert-True ($rootAgent.Contains('CURRENT_ACCOUNT') -and $rootAgent.Contains('Account Context Lock')) 'root AGENTS must define CURRENT_ACCOUNT and Account Context Lock'
Assert-True ($rootAgent.Contains('默认禁止读取其他 `accounts/*`')) 'root AGENTS must forbid other accounts by default'
Assert-True ($rootAgent.Contains('Context Loading 与阶段交接') -and
             $rootAgent.Contains('每个生产阶段使用独立对话') -and
             $rootAgent.Contains('上一阶段唯一工作成果') -and
             $rootAgent.Contains('视觉规划输入') -and
             $rootAgent.Contains('视觉规划通过新对话 `@视觉规划输入` 执行')) 'root AGENTS must enforce stage-isolated chats and explicit document transitions'
Assert-True ($rootAgent.Contains('Handoff 和视觉规划输入都是 ChatGPT 项目中的临时共享文件') -and
             $rootAgent.Contains('不写入 Repo') -and
             $rootAgent.Contains('content-identity-schema.md')) 'root AGENTS must keep Handoff outside Repo and preserve stable content identity'
Assert-True ($rootAgent.Contains('通过 GitHub 集成读取仓库时，一律把该集成视为只读') -and
             $rootAgent.Contains('不得先尝试写入再根据 `403` 回退') -and
             $rootAgent.Contains('直接写入 `pending_repo_actions`')) 'root AGENTS must prevent GitHub write attempts in Chat projects'
Assert-True ($rootAgent.Contains('一条独立内容对应一个 `topic_id`、一个 `content_id`、一份 Handoff 和一个下游文案对话') -and
             $rootAgent.Contains('同一轮选定多个彼此独立的选题') -and
             $rootAgent.Contains('它们只共享原 `recommendation_batch_id`')) 'root AGENTS must split multiple selected topics into isolated content workflows'
Assert-True ($rootAgent.Contains('视觉规划') -and
             $rootAgent.Contains('不属于仓库同步范围') -and
             $rootAgent.Contains('项目规则不规定用户选择 Chat、Work、Codex')) 'root AGENTS must exclude visual files from sync and remain model-neutral'

$allocationTerms = @('GPT-5.6 Sol', 'Sol 高', 'Sol 中', '高能力模型', '低成本模型', '额度分配')
$projectControlText = $rootAgent + $readme + $contentIdentitySchema + $handoffSchema + $confirmedCopyDeliverySchema
foreach ($term in $allocationTerms) {
    Assert-True (-not $projectControlText.Contains($term)) "project rules must not prescribe user model or quota allocation: $term"
}

Assert-True ($contentIdentitySchema.Contains('wxv-{account_id}-{YYYYMMDD}-{8hex}') -and
             $contentIdentitySchema.Contains('已有有效 `content_id` 时必须复用') -and
             $contentIdentitySchema.Contains('同一 Repo 内不得存在两个不同内容共用同一 `content_id`') -and
             $contentIdentitySchema.Contains('每个选题分别创建不同的 `content_id`')) 'content identity schema must define stable reusable IDs for multi-select flows'
Assert-True ($handoffSchema.Contains('confirmed_by_user') -and
             $handoffSchema.Contains('pending_repo_actions') -and
             $handoffSchema.Contains('不得写入仓库') -and
             $handoffSchema.Contains('只用于') -and
             $handoffSchema.Contains('topic_planning') -and
             $handoffSchema.Contains('recommendation_batch_id') -and
             $handoffSchema.Contains('feedback_event_id') -and
             $handoffSchema.Contains('完整事件 payload') -and
             $handoffSchema.Contains('选题交接｜{account_id}｜{topic_short_name}｜{YYYYMMDD-HHmmss}.md') -and
             $handoffSchema.Contains('旧版 `Handoff｜{content_id}') -and
             $handoffSchema.Contains('一份 Handoff 只交接一条独立内容') -and
             $handoffSchema.Contains('每份 Handoff 只能再携带本选题自己的 selected feedback action')) 'Handoff schema must preserve feedback, searchable filenames, and one-content packets'
Assert-True ($confirmedCopyDeliverySchema.Contains('Repo内容文档') -and
             $confirmedCopyDeliverySchema.Contains('视觉规划输入') -and
             $confirmedCopyDeliverySchema.Contains('三个主标题方案') -and
             $confirmedCopyDeliverySchema.Contains('不得把沉默视为选择') -and
             $confirmedCopyDeliverySchema.Contains('spoken_visual_input') -and
             $confirmedCopyDeliverySchema.Contains('topic_feedback_status') -and
             $confirmedCopyDeliverySchema.Contains('publication_status: "published_by_user"') -and
             $confirmedCopyDeliverySchema.Contains('requested_repo_action: "archive_published_content"') -and
             $confirmedCopyDeliverySchema.Contains('必须原样继承') -and
             $confirmedCopyDeliverySchema.Contains('direct_user_input') -and
             $confirmedCopyDeliverySchema.Contains('不能只写一个引用不存在批次的反馈') -and
             $confirmedCopyDeliverySchema.Contains('delivery_version: "1.1"') -and
             $confirmedCopyDeliverySchema.Contains('Repo 操作载荷') -and
             $confirmedCopyDeliverySchema.Contains('repo-operation-schema.md') -and
             $confirmedCopyDeliverySchema.Contains('仅生成可下载文件或当前对话临时附件不视为完成') -and
             $confirmedCopyDeliverySchema.Contains('尚未加入项目来源')) 'confirmed copy delivery must preserve feedback continuity, provide scripted Repo operations, and require project-source delivery'
Assert-True ($repoOperationSchema.Contains('sync-published') -and
             $repoOperationSchema.Contains('already_synced') -and
             $repoOperationSchema.Contains('不执行 Git 提交或推送') -and
             $repoOps.Contains('def apply_sync') -and
             $repoOps.Contains('def verify_sync') -and
             $repoOps.Contains('semantic_enrichment') -and
             $repoOps.Contains('--apply')) 'Repo operation schema and script must provide deterministic checked execution'
Assert-True ($topicSkill.Contains('content-identity-schema.md') -and
             $topicSkill.Contains('交付“选题 → 对应文案阶段”的 Handoff') -and
             $topicSkill.Contains('selected` feedback 分配稳定 `event_id`') -and
             $topicSkill.Contains('完整、可幂等执行事件') -and
             $topicSkill.Contains('必须预判为只读') -and
             $topicSkill.Contains('通过 `@选题交接`') -and
             $topicSkill.Contains('### 同一轮选定多个选题') -and
             $topicSkill.Contains('每份 Handoff 分别新建一个文案对话') -and
             $topicSkill.Contains('不得在本对话加载或执行文案 Skill')) 'topic planning must create identity and preserve executable feedback events'
Assert-True ($topicRecommendationSchema.Contains('每个题目分别 append 一条 `selected` feedback') -and
             $topicRecommendationSchema.Contains('`topic_ids` 只包含当前一个题目') -and
             $topicRecommendationSchema.Contains('不得改成 `scope: batch`')) 'topic feedback schema must split multi-select feedback per topic'
Assert-True ($textBroadcastSkill.Contains('sole prior-stage working result') -and
             $textBroadcastSkill.Contains('stable `content_id`') -and
             $textBroadcastSkill.Contains('generate one `Repo内容文档`') -and
             $textBroadcastSkill.Contains('without changing IDs or reducing payloads') -and
             $textBroadcastSkill.Contains('not_applicable') -and
             $textBroadcastSkill.Contains('Do not ask for or generate a Handoff')) 'text copywriting must end with one Repo content document'
Assert-True ($spokenSkill.Contains('唯一的上一阶段工作成果') -and
             $spokenSkill.Contains('稳定 `content_id`') -and
             $spokenSkill.Contains('口播正文已确认，标题待确认') -and
             $spokenSkill.Contains('Repo内容文档') -and
             $spokenSkill.Contains('视觉规划输入') -and
             $spokenSkill.Contains('不得改变事件 ID 或缩减 payload') -and
             $spokenSkill.Contains('not_applicable') -and
             $spokenSkill.Contains('不询问或生成 Handoff') -and
             $spokenSkill.Contains('项目文件交付') -and
             $spokenSkill.Contains('尚未加入项目来源') -and
             $spokenSkill.Contains('本对话只交付两份文件，不加载或执行视觉 Skill，不执行仓库写入')) 'spoken copywriting must enforce title selection and dual-document output'
Assert-True ($spokenVisualSkill.Contains('sole prior-stage working result') -and
             $spokenVisualSkill.Contains('视觉规划输入') -and
             $spokenVisualSkill.Contains('shared files in the ChatGPT project') -and
             $spokenVisualSkill.Contains('remain outside the Repo') -and
             -not $spokenVisualSkill.Contains('incoming Handoff') -and
             -not $spokenVisualSkill.Contains('suitable attachment directory inside the current account')) 'visual planning must use the dedicated visual input and keep outputs outside Repo'
$archiveText = $archiveSkill + $archiveManual
Assert-True ($archiveManual.Contains('content-identity-schema.md') -and
             $archiveSkill.Contains('publication_status: published_by_user') -and
             $archiveSkill.Contains('该指令授权当前 Repo 文档指定的动作') -and
             $archiveManual.Contains('没有对应候选时不创建候选卡') -and
             $archiveSkill.Contains('shared/scripts/wxv-ops.py sync-published') -and
             $archiveSkill.Contains('灵感回流只在用户明确要求') -and
             $archiveSkill.Contains('manual-archive.md')) 'publish archive must route structured documents to deterministic execution'
Assert-True ($historySchema.Contains('content_id') -and $historyRebuild.Contains('content_id =')) 'history schema and rebuild must preserve content_id'
Assert-True ($candidateSchema.Contains('content_id') -and $candidateRebuild.Contains('content_id =')) 'candidate schema and rebuild must preserve content_id when present'

$repoHandoffFiles = @(Get-ChildItem -LiteralPath (Join-Path $script:RepoRoot 'accounts') -Recurse -File | Where-Object { $_.Name -like 'Handoff｜*.md' -or $_.Name -like '选题交接｜*.md' })
Assert-True ($repoHandoffFiles.Count -eq 0) 'Handoff files must not be stored under accounts'
$repoVisualInputFiles = @(Get-ChildItem -LiteralPath (Join-Path $script:RepoRoot 'accounts') -Recurse -File -Filter '视觉规划输入｜*.md')
Assert-True ($repoVisualInputFiles.Count -eq 0) 'visual planning input files must not be stored under accounts'

$hardcoded = @('广州敏哥', '广州小张', '广州老徐聊企业财税合规', '广州出口退税', '补充业务不得脱离', '成熟企业经营不得', '电商合规')
$publicText = $topicSkill + $historyRules + $ideaSkill + $textBroadcastSkill + $spokenSkill + $spokenVisualSkill + $spokenVisualRules + $copyCommonRules + $archiveText
foreach ($term in $hardcoded) {
    Assert-True (-not $publicText.Contains($term)) "public Skills must not hardcode account rule: $term"
}

Assert-True ($topicSkill.Contains('_history-index.jsonl') -and $topicSkill.Contains('_candidate-index.jsonl') -and $topicSkill.Contains('_idea-index.jsonl')) 'topic planning must retain account-scoped indexes for support and final screening'
Assert-True ($topicSkill.Contains('初步候选形成后') -and $topicSkill.Contains('候选形成前不读取历史正文')) 'topic planning must form acquisition-led candidates before history review'
Assert-True ($historyRules.Contains('不得在候选形成前') -and $historyRules.Contains('默认不读取历史正文') -and $historyRules -match '(?i)metadata') 'history must be a metadata-first dedupe check after shortlisting'
Assert-True (-not $historyRules.Contains('full body of the 10 most recent')) 'old latest-10 body rule must be removed'
Assert-True ($historyRules.Contains('Same Session Snapshot')) 'same-session snapshot rule must exist'
Assert-True ($historyRules.Contains('不是普通选题的默认数据源')) 'derived assets must be outside default topic context'

Assert-True ($textBroadcastSkill.Contains('shared/rules/copywriting-common-rules.md') -and $spokenSkill.Contains('shared/rules/copywriting-common-rules.md')) 'both copywriting Skills must use the shared common rules'
Assert-True ($spokenSkill.Contains('references/chinese-spoken-naturalness.md')) 'spoken Skill must load the spoken-naturalness reference'
Assert-True ($spokenNaturalness.Contains('applies ONLY to `spoken-copywriting`') -and $spokenNaturalness.Contains('MUST NOT be inherited by `text-broadcast-copywriting`')) 'spoken-naturalness reference must remain isolated from text-broadcast copywriting'
Assert-True ($rootAgent.Contains('spoken-visual-planning') -and $rootAgent.Contains('不得自动进入 `spoken-visual-planning`')) 'root AGENTS must route spoken visual planning as an explicit-only stage'
Assert-True ($rootAgent.Contains('创作角色、媒介方法、页面职责和阶段内验收只在对应 Skill') -and
             -not $rootAgent.Contains('`spoken-visual-planning` 使用三类页面职责')) 'root AGENTS must remain control context and leave stage detail in Skills'
Assert-True ($readme.Contains('口播负责现场交流中的重点讲解') -and
             $readme.Contains('能够独立阅读和分享的完整资料') -and
             $readme.Contains('两个封面由主题文字')) 'README must explain the dual-expression model and entry-cover responsibility'
Assert-True ($spokenVisualSkill.Contains('Use this Skill only when') -and
             $spokenVisualSkill.Contains('wait for explicit user confirmation') -and
             $spokenVisualSkill.Contains('## Stop')) 'spoken visual planning must be explicit-only, confirm the deck, and stop after delivery'
Assert-True ($spokenVisualSkill.Contains('senior designer and information editor') -and
             $spokenVisualSkill.Contains('账号基本定位.md') -and
             $spokenVisualSkill.Contains('账号人设与文风.md') -and
             $spokenVisualSkill.Contains('账号视觉风格.md')) 'spoken visual Skill must define designer authority and account-context sources'
Assert-True ($spokenVisualSkill.Contains('native 3:4 search cover') -and
             $spokenVisualSkill.Contains('native 16:9 recommendation-feed opening cover') -and
             $spokenVisualSkill.Contains('Information architecture')) 'spoken visual Skill must distinguish entry covers from content-page information design'
Assert-True ($spokenVisualSkill.Contains('Image generation, editable PPT production, video editing, publishing and archiving are separate stages.')) 'spoken visual planning must preserve downstream stage boundaries'
Assert-True ($spokenVisualSkill.Contains('accounts/{CURRENT_ACCOUNT}/内容库/00-首页与维护规则/账号基本定位.md') -and
             $spokenVisualSkill.Contains('accounts/{CURRENT_ACCOUNT}/内容库/00-首页与维护规则/账号人设与文风.md') -and
             $spokenVisualSkill.Contains('accounts/{CURRENT_ACCOUNT}/内容库/00-首页与维护规则/账号视觉风格.md')) 'spoken visual planning must load current-account positioning, persona, and visual context'
Assert-True ($spokenVisualSkill.Contains('Phase 1') -and
             $spokenVisualSkill.Contains('Phase 2') -and
             $spokenVisualSkill.Contains('standalone deck narrative') -and
             $spokenVisualSkill.Contains('complete visible PPT copy')) 'visual planning must confirm the complete standalone deck before execution'
Assert-True ($spokenVisualAgent.Contains('等待我确认') -and
             $spokenVisualAgent.Contains('PPT设计执行指南和剪辑分段表')) 'visual entry must preserve confirmation and two-document delivery'
Assert-True ($spokenVisualSkill.Contains('COVER-01') -and
             $spokenVisualSkill.Contains('IMG-01') -and
             $spokenVisualSkill.Contains('3:4') -and
             $spokenVisualSkill.Contains('16:9') -and
             $spokenVisualSkill.Contains('PPT设计执行指南.md') -and
             $spokenVisualSkill.Contains('剪辑分段表.md')) 'visual planning must retain both covers and segmentation output'
Assert-True ($spokenVisualSkill.Contains('video_and_share') -and
             $spokenVisualSkill.Contains('share_only') -and
             $spokenVisualSkill.Contains('source material already approved')) 'visual planning must distinguish video pages, reference pages, and approved source material'
Assert-True ($spokenVisualSkill.Contains('Rebuild both final documents from the latest fully confirmed state') -and
             $spokenVisualSkill.Contains('revision history') -and
             $spokenVisualSkill.Contains('final-state purity pass')) 'visual planning must rebuild clean execution documents from final confirmed state'
Assert-True ($spokenVisualRules.Contains('Dual-Expression Model') -and
             $spokenVisualRules.Contains('Entry-Cover Design') -and
             $spokenVisualRules.Contains('Page Copy and Typesetting') -and
             $spokenVisualRules.Contains('Production-Method Selection') -and
             $spokenVisualRules.Contains('Prompt Distillation') -and
             $spokenVisualRules.Contains('Video Segmentation') -and
             $spokenVisualRules.Contains('Review with Generated Evidence')) 'visual reference must cover the complete document and role-led execution model'
Assert-True ($spokenVisualRules.Contains('Never use conversation-relative or revision-relative instructions') -and
             $spokenVisualRules.Contains('Final Delivery Purity Check') -and
             $spokenVisualRules.Contains('operational specification, not a record of the confirmation conversation')) 'visual execution prompts and guides must contain final operational state only'
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
Assert-True ($ideaSkill.Contains('_idea-index.jsonl') -and $ideaSkill.Contains('不做选题分析') -and $ideaSkill.Contains('## Stop')) 'idea intake must update Idea Index and stop'
Assert-True ($archiveText.Contains('_history-index.jsonl') -and $archiveText.Contains('_candidate-index.jsonl')) 'archive must update history and candidate indexes'
Assert-True ($archiveSkill.Contains('以下任一入口成立时使用') -and
             $archiveSkill.Contains('明确引用有效 Repo 内容文档') -and
             $archiveSkill.Contains('要求“同步”或“录入”')) 'archive must accept the personal Repo-document sync workflow'
Assert-True ($archiveText.Contains('content_format') -and $archiveText.Contains('recommended_format')) 'archive must record actual content format instead of the recommendation'
Assert-True ($historySchema.Contains('content_type') -and $historySchema.Contains('content_format')) 'history schema must keep content type and add content format'
Assert-True ($historyRebuild.Contains('content_type =') -and $historyRebuild.Contains('content_format =')) 'history rebuild must emit content type and content format separately'
Assert-True ($stateSchema.Contains('待分析 → 可入池 → 已转选题') -and
             $stateSchema.Contains('待核验 → 可推荐 → 已发布') -and
             -not $stateSchema.Contains('已采用') -and
             -not $candidateSchema.Contains('已采用') -and
             -not $candidateRebuild.Contains('已采用')) 'candidate workflow must use selected feedback and direct publication without an adopted state'

if ($RulesOnly) {
    Write-Output "RULE VALIDATION PASSED checks=$script:Checks"
    return
}

$validIdea = @('待分析', '可入池', '已转选题', '已放弃')
$validCandidate = @('待核验', '可推荐', '已发布', '已放弃')
$validRecommendedFormats = @('text_broadcast', 'spoken', 'either')
$validContentFormats = @('text_broadcast', 'spoken')
$historyContentIdPaths = @{}
$candidateContentIdPaths = @{}

foreach ($id in $script:KnownAccountIds) {
    $accountRoot = Join-Path $script:RepoRoot "accounts\$id"
    $vault = Join-Path $accountRoot '内容库'
    $yaml = [System.IO.File]::ReadAllText((Join-Path $accountRoot 'account.yaml'))
    Assert-True ($yaml -match "(?m)^id:\s*$id\s*$") "$id account.yaml id mismatch"
    $archiveRules = [System.IO.File]::ReadAllText((Join-Path $vault '00-首页与维护规则\历史内容归档规范.md'))
    Assert-True ($archiveRules.Contains('content_id') -and
                 $archiveRules.Contains('content-identity-schema.md') -and
                 $archiveRules.Contains('publication_status: published_by_user') -and
                 $archiveRules.Contains('requested_repo_action: archive_published_content')) "$id archive rules must preserve stable content_id and Repo-document sync semantics"
    Assert-True ((Test-Path -LiteralPath (Join-Path $vault '00-首页与维护规则\账号基本定位.md')) -and
                 (Test-Path -LiteralPath (Join-Path $vault '00-首页与维护规则\账号人设与文风.md'))) "$id positioning split missing"

    $visualStylePath = Join-Path $vault '00-首页与维护规则\账号视觉风格.md'
    Assert-True (Test-Path -LiteralPath $visualStylePath) "$id account visual context missing"
    $visualStyle = [System.IO.File]::ReadAllText($visualStylePath)
    Assert-True ($visualStyle.Contains('# Account Visual Context') -and
                 $visualStyle.Contains('## Explicit Brand Assets') -and
                 $visualStyle.Contains('## Designer Authority') -and
                 $visualStyle.Contains('## Visual Fact Boundaries') -and
                 -not $visualStyle.Contains(': ""') -and
                 -not $visualStyle.Contains(': []') -and
                 -not $visualStyle.Contains('- ""')) "$id account visual context contains unresolved blank fields"
    Assert-True (-not $visualStyle.Contains('background_preference') -and
                 -not $visualStyle.Contains('primary_colors') -and
                 -not $visualStyle.Contains('fixed_layout') -and
                 -not $visualStyle.Contains('rendering:')) "$id account visual context must not prescribe a visual treatment"
    Assert-True ($visualStyle.Contains('主要信息、辅助解释、环境与连续性') -and
                 $visualStyle.Contains('当前内容需要什么视觉证据') -and
                 $visualStyle.Contains('背景是否回应当前页面的实际需要') -and
                 -not $visualStyle.Contains('背景语义层')) "$id account visual context must support designer-led carrier assignment without background obligation"

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
        if ($row.PSObject.Properties.Name -contains 'content_id' -and -not [string]::IsNullOrWhiteSpace([string]$row.content_id)) {
            $historyContentId = [string]$row.content_id
            Assert-True ($historyContentId -match "^wxv-$id-\d{8}-[0-9a-f]{8}$") "$id history content_id invalid"
            Assert-True (-not $historyContentIdPaths.ContainsKey($historyContentId)) "duplicate history content_id: $historyContentId"
            $historyContentIdPaths[$historyContentId] = [string]$row.path
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
        if ($row.PSObject.Properties.Name -contains 'content_id' -and -not [string]::IsNullOrWhiteSpace([string]$row.content_id)) {
            $candidateContentId = [string]$row.content_id
            Assert-True ($candidateContentId -match "^wxv-$id-\d{8}-[0-9a-f]{8}$") "$id candidate content_id invalid"
            Assert-True (-not $candidateContentIdPaths.ContainsKey($candidateContentId)) "duplicate candidate content_id: $candidateContentId"
            $candidateContentIdPaths[$candidateContentId] = [string]$row.path
            if ([string]$row.status -eq '已发布') {
                Assert-True ($historyContentIdPaths.ContainsKey($candidateContentId)) "$id published candidate content_id has no matching history"
            }
        }
    }
}

Write-Output "VALIDATION PASSED checks=$script:Checks accounts=$($script:KnownAccountIds.Count)"
