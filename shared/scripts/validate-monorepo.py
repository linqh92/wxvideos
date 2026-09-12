"""Validate repository rules, generated indexes, and account isolation."""

from __future__ import annotations

import argparse
import re
from pathlib import Path

from index_common import KNOWN_ACCOUNT_IDS, REPO_ROOT, configure_console, read_json_lines


CHECKS = 0


def assert_true(condition: bool, message: str) -> None:
    global CHECKS
    if not condition:
        raise RuntimeError(f"VALIDATION FAILED: {message}")
    CHECKS += 1


def read_repo_text(relative_path: str) -> str:
    return (REPO_ROOT / Path(relative_path)).read_text(encoding="utf-8-sig")


def repository_relative_path(path: Path) -> str:
    return path.resolve().relative_to(REPO_ROOT).as_posix()


def validate_rules() -> None:
    root_agent = read_repo_text("AGENTS.md")
    readme = read_repo_text("README.md")
    topic_skill = read_repo_text(".codex/skills/topic-planning/SKILL.md")
    history_rules = read_repo_text(
        ".codex/skills/topic-planning/references/history-vault-rules.md"
    )
    idea_skill = read_repo_text(".codex/skills/idea-intake/SKILL.md")
    text_broadcast_skill = read_repo_text(
        ".codex/skills/text-broadcast-copywriting/SKILL.md"
    )
    spoken_skill = read_repo_text(".codex/skills/spoken-copywriting/SKILL.md")
    spoken_naturalness = read_repo_text(
        ".codex/skills/spoken-copywriting/references/chinese-spoken-naturalness.md"
    )
    spoken_visual_skill = read_repo_text(
        ".codex/skills/spoken-visual-planning/SKILL.md"
    )
    spoken_visual_rules = read_repo_text(
        ".codex/skills/spoken-visual-planning/references/visual-aid-generation-rules.md"
    )
    spoken_visual_agent = read_repo_text(
        ".codex/skills/spoken-visual-planning/agents/openai.yaml"
    )
    copy_common_rules = read_repo_text("shared/rules/copywriting-common-rules.md")
    archive_skill = read_repo_text(".codex/skills/publish-archive/SKILL.md")
    archive_manual = read_repo_text(
        ".codex/skills/publish-archive/references/manual-archive.md"
    )
    state_schema = read_repo_text("shared/schemas/content-state-machine.md")
    content_identity_schema = read_repo_text(
        "shared/schemas/content-identity-schema.md"
    )
    handoff_schema = read_repo_text("shared/schemas/handoff-packet-schema.md")
    confirmed_copy_delivery_schema = read_repo_text(
        "shared/schemas/confirmed-copy-delivery-schema.md"
    )
    repo_operation_schema = read_repo_text("shared/schemas/repo-operation-schema.md")
    topic_recommendation_schema = read_repo_text(
        "shared/schemas/topic-recommendation-log-schema.md"
    )
    candidate_schema = read_repo_text("shared/schemas/candidate-index-schema.md")
    history_schema = read_repo_text("shared/schemas/history-index-schema.md")
    history_rebuild = read_repo_text("shared/scripts/rebuild-history-index.py")
    candidate_rebuild = read_repo_text("shared/scripts/rebuild-candidate-index.py")
    repo_ops = read_repo_text("shared/scripts/wxv-ops.py")

    required_content_format_paths = (
        "shared/rules/copywriting-common-rules.md",
        ".codex/skills/text-broadcast-copywriting/SKILL.md",
        ".codex/skills/text-broadcast-copywriting/agents/openai.yaml",
        ".codex/skills/spoken-copywriting/SKILL.md",
        ".codex/skills/spoken-copywriting/references/chinese-spoken-naturalness.md",
        ".codex/skills/spoken-copywriting/agents/openai.yaml",
    )
    for relative_path in required_content_format_paths:
        assert_true(
            (REPO_ROOT / Path(relative_path)).exists(),
            f"missing content-format asset: {relative_path}",
        )

    required_spoken_visual_paths = (
        ".codex/skills/spoken-visual-planning/SKILL.md",
        ".codex/skills/spoken-visual-planning/references/visual-aid-generation-rules.md",
        ".codex/skills/spoken-visual-planning/agents/openai.yaml",
    )
    for relative_path in required_spoken_visual_paths:
        assert_true(
            (REPO_ROOT / Path(relative_path)).exists(),
            f"missing spoken-visual-planning asset: {relative_path}",
        )

    required_handoff_paths = (
        "shared/schemas/content-identity-schema.md",
        "shared/schemas/handoff-packet-schema.md",
        "shared/schemas/confirmed-copy-delivery-schema.md",
        "shared/schemas/repo-operation-schema.md",
        "shared/scripts/content-handoff.py",
        "shared/scripts/test-content-handoff.py",
        "shared/scripts/wxv-ops.py",
        "shared/scripts/test-wxv-ops.py",
        ".codex/skills/publish-archive/references/manual-archive.md",
    )
    for relative_path in required_handoff_paths:
        assert_true(
            (REPO_ROOT / Path(relative_path)).exists(),
            f"missing content-handoff asset: {relative_path}",
        )

    assert_true(
        "CURRENT_ACCOUNT" in root_agent and "Account Context Lock" in root_agent,
        "root AGENTS must define CURRENT_ACCOUNT and Account Context Lock",
    )
    assert_true(
        "默认禁止读取其他 `accounts/*`" in root_agent,
        "root AGENTS must forbid other accounts by default",
    )
    assert_true(
        all(
            term in root_agent
            for term in (
                "Context Loading 与阶段交接",
                "每个生产阶段使用独立对话",
                "上一阶段唯一工作成果",
                "视觉规划输入",
                "视觉规划通过新对话 `@视觉规划输入` 执行",
            )
        ),
        "root AGENTS must enforce stage-isolated chats and explicit document transitions",
    )
    assert_true(
        all(
            term in root_agent
            for term in (
                "Handoff 和视觉规划输入都是 ChatGPT 项目中的临时共享文件",
                "不写入 Repo",
                "content-identity-schema.md",
            )
        ),
        "root AGENTS must keep Handoff outside Repo and preserve stable content identity",
    )
    assert_true(
        all(
            term in root_agent
            for term in (
                "通过 GitHub 集成读取仓库时，一律把该集成视为只读",
                "不得先尝试写入再根据 `403` 回退",
                "直接写入 `pending_repo_actions`",
            )
        ),
        "root AGENTS must prevent GitHub write attempts in Chat projects",
    )
    assert_true(
        all(
            term in root_agent
            for term in (
                "一条独立内容对应一个 `topic_id`、一个 `content_id`、一份 Handoff 和一个下游文案对话",
                "同一轮选定多个彼此独立的选题",
                "它们只共享原 `recommendation_batch_id`",
            )
        ),
        "root AGENTS must split multiple selected topics into isolated content workflows",
    )
    assert_true(
        all(term in root_agent for term in ("视觉规划", "不属于仓库同步范围"))
        and "项目规则不规定用户选择 Chat、Work、Codex" in root_agent,
        "root AGENTS must exclude visual files from sync and remain model-neutral",
    )

    allocation_terms = ("GPT-5.6 Sol", "Sol 高", "Sol 中", "高能力模型", "低成本模型", "额度分配")
    project_control_text = (
        root_agent
        + readme
        + content_identity_schema
        + handoff_schema
        + confirmed_copy_delivery_schema
    )
    for term in allocation_terms:
        assert_true(
            term not in project_control_text,
            f"project rules must not prescribe user model or quota allocation: {term}",
        )

    assert_true(
        all(
            term in content_identity_schema
            for term in (
                "wxv-{account_id}-{YYYYMMDD}-{8hex}",
                "已有有效 `content_id` 时必须复用",
                "同一 Repo 内不得存在两个不同内容共用同一 `content_id`",
                "每个选题分别创建不同的 `content_id`",
            )
        ),
        "content identity schema must define stable reusable IDs for multi-select flows",
    )
    assert_true(
        all(
            term in handoff_schema
            for term in (
                "confirmed_by_user",
                "pending_repo_actions",
                "不得写入仓库",
                "只用于",
                "topic_planning",
                "recommendation_batch_id",
                "feedback_event_id",
                "完整事件 payload",
                "选题交接｜{account_id}｜{topic_short_name}｜{YYYYMMDD-HHmmss}.md",
                "旧版 `Handoff｜{content_id}",
                "一份 Handoff 只交接一条独立内容",
                "每份 Handoff 只能再携带本选题自己的 selected feedback action",
            )
        ),
        "Handoff schema must preserve feedback, searchable filenames, and one-content packets",
    )
    assert_true(
        all(
            term in confirmed_copy_delivery_schema
            for term in (
                "Repo内容文档",
                "视觉规划输入",
                "三个主标题方案",
                "不得把沉默视为选择",
                "spoken_visual_input",
                "topic_feedback_status",
                'publication_status: "published_by_user"',
                'requested_repo_action: "archive_published_content"',
                "必须原样继承",
                "direct_user_input",
                "不能只写一个引用不存在批次的反馈",
                'delivery_version: "1.1"',
                "Repo 操作载荷",
                "repo-operation-schema.md",
                "仅生成可下载文件或当前对话临时附件不视为完成",
                "尚未加入项目来源",
            )
        ),
        "confirmed copy delivery must preserve feedback continuity, provide scripted Repo operations, and require project-source delivery",
    )
    assert_true(
        all(
            term in repo_operation_schema
            for term in ("sync-published", "already_synced", "不执行 Git 提交或推送")
        )
        and all(
            term in repo_ops
            for term in ("def apply_sync", "def verify_sync", "semantic_enrichment", "--apply")
        ),
        "Repo operation schema and script must provide deterministic checked execution",
    )
    assert_true(
        all(
            term in topic_skill
            for term in (
                "content-identity-schema.md",
                "交付“选题 → 对应文案阶段”的 Handoff",
                "selected` feedback 分配稳定 `event_id`",
                "完整、可幂等执行事件",
                "必须预判为只读",
                "通过 `@选题交接`",
                "### 同一轮选定多个选题",
                "每份 Handoff 分别新建一个文案对话",
                "不得在本对话加载或执行文案 Skill",
            )
        ),
        "topic planning must create identity and preserve executable feedback events",
    )
    assert_true(
        all(
            term in topic_recommendation_schema
            for term in (
                "每个题目分别 append 一条 `selected` feedback",
                "`topic_ids` 只包含当前一个题目",
                "不得改成 `scope: batch`",
            )
        ),
        "topic feedback schema must split multi-select feedback per topic",
    )
    assert_true(
        all(
            term in text_broadcast_skill
            for term in (
                "sole prior-stage working result",
                "stable `content_id`",
                "generate one `Repo内容文档`",
                "without changing IDs or reducing payloads",
                "not_applicable",
                "Do not ask for or generate a Handoff",
            )
        ),
        "text copywriting must end with one Repo content document",
    )
    assert_true(
        all(
            term in spoken_skill
            for term in (
                "唯一的上一阶段工作成果",
                "稳定 `content_id`",
                "口播正文已确认，标题待确认",
                "Repo内容文档",
                "视觉规划输入",
                "不得改变事件 ID 或缩减 payload",
                "not_applicable",
                "不询问或生成 Handoff",
                "项目文件交付",
                "尚未加入项目来源",
                "本对话只交付两份文件，不加载或执行视觉 Skill，不执行仓库写入",
            )
        ),
        "spoken copywriting must enforce title selection and dual-document output",
    )
    assert_true(
        all(
            term in spoken_visual_skill
            for term in (
                "sole prior-stage working result",
                "视觉规划输入",
                "shared files in the ChatGPT project",
                "remain outside the Repo",
            )
        )
        and "incoming Handoff" not in spoken_visual_skill
        and "suitable attachment directory inside the current account" not in spoken_visual_skill,
        "visual planning must use the dedicated visual input and keep outputs outside Repo",
    )
    archive_text = archive_skill + archive_manual
    assert_true(
        "content-identity-schema.md" in archive_manual
        and all(
            term in archive_skill
            for term in (
                "publication_status: published_by_user",
                "该指令授权当前 Repo 文档指定的动作",
                "shared/scripts/wxv-ops.py sync-published",
                "灵感回流只在用户明确要求",
                "manual-archive.md",
            )
        )
        and "没有对应候选时不创建候选卡" in archive_manual,
        "publish archive must route structured documents to deterministic execution",
    )
    assert_true(
        "content_id" in history_schema and '"content_id":' in history_rebuild,
        "history schema and rebuild must preserve content_id",
    )
    assert_true(
        "content_id" in candidate_schema and '"content_id":' in candidate_rebuild,
        "candidate schema and rebuild must preserve content_id when present",
    )

    accounts_root = REPO_ROOT / "accounts"
    repo_handoff_files = [
        path
        for path in accounts_root.rglob("*.md")
        if path.name.casefold().startswith("handoff｜")
        or path.name.startswith("选题交接｜")
    ]
    assert_true(not repo_handoff_files, "Handoff files must not be stored under accounts")
    repo_visual_input_files = [
        path for path in accounts_root.rglob("视觉规划输入｜*.md") if path.is_file()
    ]
    assert_true(
        not repo_visual_input_files,
        "visual planning input files must not be stored under accounts",
    )

    hardcoded = (
        "广州敏哥",
        "广州小张",
        "广州老徐聊企业财税合规",
        "广州出口退税",
        "补充业务不得脱离",
        "成熟企业经营不得",
        "电商合规",
    )
    public_text = (
        topic_skill
        + history_rules
        + idea_skill
        + text_broadcast_skill
        + spoken_skill
        + spoken_visual_skill
        + spoken_visual_rules
        + copy_common_rules
        + archive_text
    )
    for term in hardcoded:
        assert_true(
            term not in public_text,
            f"public Skills must not hardcode account rule: {term}",
        )

    assert_true(
        all(
            term in topic_skill
            for term in ("_history-index.jsonl", "_candidate-index.jsonl", "_idea-index.jsonl")
        ),
        "topic planning must retain account-scoped indexes for support and final screening",
    )
    assert_true(
        "初步候选形成后" in topic_skill and "候选形成前不读取历史正文" in topic_skill,
        "topic planning must form acquisition-led candidates before history review",
    )
    assert_true(
        "不得在候选形成前" in history_rules
        and "默认不读取历史正文" in history_rules
        and re.search("metadata", history_rules, flags=re.IGNORECASE) is not None,
        "history must be a metadata-first dedupe check after shortlisting",
    )
    assert_true(
        "full body of the 10 most recent" not in history_rules,
        "old latest-10 body rule must be removed",
    )
    assert_true(
        "Same Session Snapshot" in history_rules,
        "same-session snapshot rule must exist",
    )
    assert_true(
        "不是普通选题的默认数据源" in history_rules,
        "derived assets must be outside default topic context",
    )

    assert_true(
        "shared/rules/copywriting-common-rules.md" in text_broadcast_skill
        and "shared/rules/copywriting-common-rules.md" in spoken_skill,
        "both copywriting Skills must use the shared common rules",
    )
    assert_true(
        "references/chinese-spoken-naturalness.md" in spoken_skill,
        "spoken Skill must load the spoken-naturalness reference",
    )
    assert_true(
        "applies ONLY to `spoken-copywriting`" in spoken_naturalness
        and "MUST NOT be inherited by `text-broadcast-copywriting`" in spoken_naturalness,
        "spoken-naturalness reference must remain isolated from text-broadcast copywriting",
    )
    assert_true(
        "spoken-visual-planning" in root_agent
        and "不得自动进入 `spoken-visual-planning`" in root_agent,
        "root AGENTS must route spoken visual planning as an explicit-only stage",
    )
    assert_true(
        "创作角色、媒介方法、页面职责和阶段内验收只在对应 Skill" in root_agent
        and "`spoken-visual-planning` 使用三类页面职责" not in root_agent,
        "root AGENTS must remain control context and leave stage detail in Skills",
    )
    assert_true(
        all(
            term in readme
            for term in (
                "口播负责现场交流中的重点讲解",
                "能够独立阅读和分享的完整资料",
                "两个封面由主题文字",
            )
        ),
        "README must explain the dual-expression model and entry-cover responsibility",
    )
    assert_true(
        all(
            term in spoken_visual_skill
            for term in ("Use this Skill only when", "wait for explicit user confirmation", "## Stop")
        ),
        "spoken visual planning must be explicit-only, confirm the deck, and stop after delivery",
    )
    assert_true(
        all(
            term in spoken_visual_skill
            for term in (
                "senior designer and information editor",
                "账号基本定位.md",
                "账号人设与文风.md",
                "账号视觉风格.md",
            )
        ),
        "spoken visual Skill must define designer authority and account-context sources",
    )
    assert_true(
        all(
            term in spoken_visual_skill
            for term in (
                "native 3:4 search cover",
                "native 16:9 recommendation-feed opening cover",
                "Information architecture",
            )
        ),
        "spoken visual Skill must distinguish entry covers from content-page information design",
    )
    assert_true(
        "Image generation, editable PPT production, video editing, publishing and archiving are separate stages."
        in spoken_visual_skill,
        "spoken visual planning must preserve downstream stage boundaries",
    )
    assert_true(
        all(
            term in spoken_visual_skill
            for term in (
                "accounts/{CURRENT_ACCOUNT}/内容库/00-首页与维护规则/账号基本定位.md",
                "accounts/{CURRENT_ACCOUNT}/内容库/00-首页与维护规则/账号人设与文风.md",
                "accounts/{CURRENT_ACCOUNT}/内容库/00-首页与维护规则/账号视觉风格.md",
            )
        ),
        "spoken visual planning must load current-account positioning, persona, and visual context",
    )
    assert_true(
        all(
            term in spoken_visual_skill
            for term in ("Phase 1", "Phase 2", "standalone deck narrative", "complete visible PPT copy")
        ),
        "visual planning must confirm the complete standalone deck before execution",
    )
    assert_true(
        "等待我确认" in spoken_visual_agent and "PPT设计执行指南和剪辑分段表" in spoken_visual_agent,
        "visual entry must preserve confirmation and two-document delivery",
    )
    assert_true(
        all(
            term in spoken_visual_skill
            for term in (
                "COVER-01",
                "IMG-01",
                "3:4",
                "16:9",
                "PPT设计执行指南.md",
                "剪辑分段表.md",
            )
        ),
        "visual planning must retain both covers and segmentation output",
    )
    assert_true(
        all(
            term in spoken_visual_skill
            for term in ("video_and_share", "share_only", "source material already approved")
        ),
        "visual planning must distinguish video pages, reference pages, and approved source material",
    )
    assert_true(
        all(
            term in spoken_visual_skill
            for term in (
                "Rebuild both final documents from the latest fully confirmed state",
                "revision history",
                "final-state purity pass",
            )
        ),
        "visual planning must rebuild clean execution documents from final confirmed state",
    )
    assert_true(
        all(
            term in spoken_visual_rules
            for term in (
                "Dual-Expression Model",
                "Entry-Cover Design",
                "Page Copy and Typesetting",
                "Production-Method Selection",
                "Prompt Distillation",
                "Video Segmentation",
                "Review with Generated Evidence",
            )
        ),
        "visual reference must cover the complete document and role-led execution model",
    )
    assert_true(
        all(
            term in spoken_visual_rules
            for term in (
                "Never use conversation-relative or revision-relative instructions",
                "Final Delivery Purity Check",
                "operational specification, not a record of the confirmation conversation",
            )
        ),
        "visual execution prompts and guides must contain final operational state only",
    )
    fixed_global_visual_style = (
        "- semi-realistic or realistic business explanatory visual;",
        "- blue-gray-white base;",
        "- small red accents only for risk;",
        "- light neutral background;",
        "- restrained financial / compliance feel;",
        "整体采用半写实或真实商业视觉风格",
        "蓝灰白主色调",
        "少量红色仅用于风险提示",
    )
    for term in fixed_global_visual_style:
        assert_true(
            term not in spoken_visual_rules,
            f"shared visual rules must not fix account style: {term}",
        )
    assert_true(
        all(term in root_agent for term in ("CONTENT_FORMAT", "text_broadcast", "spoken")),
        "root AGENTS must route both content formats",
    )
    assert_true(
        "`video-copywriting`" not in root_agent,
        "root AGENTS must not route formal copy to video-copywriting",
    )
    runtime_files = [REPO_ROOT / "AGENTS.md", REPO_ROOT / "README.md"] + [
        path for path in (REPO_ROOT / ".codex").rglob("*") if path.is_file()
    ]
    for runtime_file in runtime_files:
        runtime_text = runtime_file.read_text(encoding="utf-8-sig")
        assert_true(
            "$video-copywriting" not in runtime_text,
            f"stale runtime invocation in {repository_relative_path(runtime_file)}",
        )
    assert_true(
        all(term in idea_skill for term in ("_idea-index.jsonl", "不做选题分析", "## Stop")),
        "idea intake must update Idea Index and stop",
    )
    assert_true(
        "_history-index.jsonl" in archive_text and "_candidate-index.jsonl" in archive_text,
        "archive must update history and candidate indexes",
    )
    assert_true(
        all(
            term in archive_skill
            for term in ("以下任一入口成立时使用", "明确引用有效 Repo 内容文档", "要求“同步”或“录入”")
        ),
        "archive must accept the personal Repo-document sync workflow",
    )
    assert_true(
        "content_format" in archive_text and "recommended_format" in archive_text,
        "archive must record actual content format instead of the recommendation",
    )
    assert_true(
        "content_type" in history_schema and "content_format" in history_schema,
        "history schema must keep content type and add content format",
    )
    assert_true(
        '"content_type":' in history_rebuild and '"content_format":' in history_rebuild,
        "history rebuild must emit content type and content format separately",
    )
    assert_true(
        "待分析 → 可入池 → 已转选题" in state_schema
        and "待核验 → 可推荐 → 已发布" in state_schema
        and "已采用" not in state_schema
        and "已采用" not in candidate_schema
        and "已采用" not in candidate_rebuild,
        "candidate workflow must use selected feedback and direct publication without an adopted state",
    )


def validate_account_data() -> None:
    valid_idea = ("待分析", "可入池", "已转选题", "已放弃")
    valid_candidate = ("待核验", "可推荐", "已发布", "已放弃")
    valid_recommended_formats = ("text_broadcast", "spoken", "either")
    valid_content_formats = ("text_broadcast", "spoken")
    history_content_id_paths: dict[str, str] = {}
    candidate_content_id_paths: dict[str, str] = {}

    for account_id in KNOWN_ACCOUNT_IDS:
        account_root = REPO_ROOT / "accounts" / account_id
        vault = account_root / "内容库"
        yaml_text = (account_root / "account.yaml").read_text(encoding="utf-8-sig")
        assert_true(
            re.search(
                rf"^id:\s*{re.escape(account_id)}\s*$",
                yaml_text,
                flags=re.MULTILINE | re.IGNORECASE,
            )
            is not None,
            f"{account_id} account.yaml id mismatch",
        )
        archive_rules = (vault / "00-首页与维护规则" / "历史内容归档规范.md").read_text(
            encoding="utf-8-sig"
        )
        assert_true(
            all(
                term in archive_rules
                for term in (
                    "content_id",
                    "content-identity-schema.md",
                    "publication_status: published_by_user",
                    "requested_repo_action: archive_published_content",
                )
            ),
            f"{account_id} archive rules must preserve stable content_id and Repo-document sync semantics",
        )
        basic_path = vault / "00-首页与维护规则" / "账号基本定位.md"
        voice_path = vault / "00-首页与维护规则" / "账号人设与文风.md"
        assert_true(
            basic_path.exists() and voice_path.exists(),
            f"{account_id} positioning split missing",
        )

        visual_style_path = vault / "00-首页与维护规则" / "账号视觉风格.md"
        assert_true(
            visual_style_path.exists(), f"{account_id} account visual context missing"
        )
        visual_style = visual_style_path.read_text(encoding="utf-8-sig")
        assert_true(
            all(
                term in visual_style
                for term in (
                    "# Account Visual Context",
                    "## Explicit Brand Assets",
                    "## Designer Authority",
                    "## Visual Fact Boundaries",
                )
            )
            and all(term not in visual_style for term in (': ""', ": []", '- ""')),
            f"{account_id} account visual context contains unresolved blank fields",
        )
        assert_true(
            all(
                term not in visual_style
                for term in ("background_preference", "primary_colors", "fixed_layout", "rendering:")
            ),
            f"{account_id} account visual context must not prescribe a visual treatment",
        )
        assert_true(
            all(
                term in visual_style
                for term in (
                    "主要信息、辅助解释、环境与连续性",
                    "当前内容需要什么视觉证据",
                    "背景是否回应当前页面的实际需要",
                )
            )
            and "背景语义层" not in visual_style,
            f"{account_id} account visual context must support designer-led carrier assignment without background obligation",
        )

        basic = basic_path.read_text(encoding="utf-8-sig")
        voice = voice_path.read_text(encoding="utf-8-sig")
        assert_true(
            "# Persona" not in basic,
            f"{account_id} topic positioning still contains persona block",
        )
        assert_true(
            "# Persona" in voice, f"{account_id} voice file lost persona block"
        )

        history_path = vault / "01-历史内容" / "_history-index.jsonl"
        idea_path = vault / "03-选题规划" / "灵感库" / "_idea-index.jsonl"
        candidate_path = vault / "03-选题规划" / "_candidate-index.jsonl"
        derived_path = vault / "04-内容复盘" / "_derived-assets-summary.json"
        for path in (history_path, idea_path, candidate_path, derived_path):
            assert_true(path.exists(), f"{account_id} missing generated asset: {path}")

        history = read_json_lines(history_path)
        ideas = read_json_lines(idea_path)
        candidates = read_json_lines(candidate_path)
        history_files = [
            path for path in (vault / "01-历史内容").rglob("*.md") if path.is_file()
        ]
        idea_files = [
            path
            for path in (vault / "03-选题规划" / "灵感库").rglob("*.md")
            if path.is_file() and not path.name.casefold().startswith("00-")
        ]

        assert_true(
            len(history) == len(history_files),
            f"{account_id} history index count mismatch",
        )
        assert_true(
            len(ideas) == len(idea_files), f"{account_id} idea index count mismatch"
        )
        for row in history:
            row_path = str(row["path"])
            assert_true(
                row_path.casefold().startswith(f"accounts/{account_id}/".casefold()),
                f"{account_id} history index leaked another account",
            )
            assert_true(
                bool(str(row.get("title", "")).strip())
                and bool(str(row.get("publish_date", "")).strip()),
                f"{account_id} history metadata incomplete",
            )
            content_format = str(row.get("content_format", ""))
            if content_format.strip():
                assert_true(
                    content_format in valid_content_formats,
                    f"{account_id} history content_format invalid",
                )
            content_id = str(row.get("content_id", ""))
            if content_id.strip():
                assert_true(
                    re.fullmatch(
                        rf"wxv-{re.escape(account_id)}-\d{{8}}-[0-9a-f]{{8}}",
                        content_id,
                        flags=re.IGNORECASE,
                    )
                    is not None,
                    f"{account_id} history content_id invalid",
                )
                assert_true(
                    content_id not in history_content_id_paths,
                    f"duplicate history content_id: {content_id}",
                )
                history_content_id_paths[content_id] = row_path

        for row in ideas:
            row_path = str(row["path"])
            assert_true(
                row_path.casefold().startswith(f"accounts/{account_id}/".casefold())
                and row.get("status") in valid_idea,
                f"{account_id} idea index path/status invalid",
            )

        for row in candidates:
            row_path = str(row["path"])
            assert_true(
                row_path.casefold().startswith(f"accounts/{account_id}/".casefold())
                and row.get("status") in valid_candidate,
                f"{account_id} candidate index path/status invalid",
            )
            recommended_format = str(row.get("recommended_format", ""))
            if recommended_format.strip():
                assert_true(
                    recommended_format in valid_recommended_formats,
                    f"{account_id} candidate recommended_format invalid",
                )
            content_id = str(row.get("content_id", ""))
            if content_id.strip():
                assert_true(
                    re.fullmatch(
                        rf"wxv-{re.escape(account_id)}-\d{{8}}-[0-9a-f]{{8}}",
                        content_id,
                        flags=re.IGNORECASE,
                    )
                    is not None,
                    f"{account_id} candidate content_id invalid",
                )
                assert_true(
                    content_id not in candidate_content_id_paths,
                    f"duplicate candidate content_id: {content_id}",
                )
                candidate_content_id_paths[content_id] = row_path
                if row.get("status") == "已发布":
                    assert_true(
                        content_id in history_content_id_paths,
                        f"{account_id} published candidate content_id has no matching history",
                    )


def main() -> int:
    configure_console()
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--rules-only", action="store_true")
    args = parser.parse_args()

    validate_rules()
    if args.rules_only:
        print(f"RULE VALIDATION PASSED checks={CHECKS}")
        return 0

    validate_account_data()
    print(f"VALIDATION PASSED checks={CHECKS} accounts={len(KNOWN_ACCOUNT_IDS)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
