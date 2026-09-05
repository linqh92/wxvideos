# 微信视频号多账号内容运营系统

这是一个统一维护五个微信视频号账号的内容运营 Monorepo。公共运营逻辑只保留一套，账号配置和内容数据库彼此隔离。

```text
Agent 路由与阶段控制
        ↓
Shared Skills / Schemas / Scripts
        ↓
当前 Account Content Vault
```

## 账号

| Account ID | 账号名称 | 迁移来源 | 内容库路径 |
| --- | --- | --- | --- |
| `gzminge` | 广州敏哥聊财税 | `linqh92/gzminge_wxvideos_contens` | `accounts/gzminge/内容库` |
| `gzxzcs` | 广州小张说财税 | `linqh92/gzxzcs_wxvideos_contens` | `accounts/gzxzcs/内容库` |
| `qycslc` | 企业财税-老陈 | `linqh92/qycslc_wxvideos_contens` | `accounts/qycslc/内容库` |
| `gzcktxpp` | 广州出口退税-翩翩 | `linqh92/gzcktxpp_wxvideos_contens` | `accounts/gzcktxpp/内容库` |
| `tsxbj` | 退税小笔记 | 本项目新建 | `accounts/tsxbj/内容库` |

旧仓库只作为迁移对照、数据核验和回滚来源；本项目是后续统一维护入口。

## 使用方式

开始内容任务时先指定账号，例如“为 `gzminge` 给 5 个选题”。Agent 会锁定该账号，仅加载公共层和对应内容库。切换账号时必须明确给出新账号。

内容生产阶段分别由以下公共 Skill 处理：

- `idea-intake`：保存原始灵感并增量更新 Idea Index。
- `topic-planning`：Index First 检索、按需读取少量相关正文，输出选题与建议载体；也支持灵感分析模式。
- `text-broadcast-copywriting`：读取公共文案规则，生成短文字幕与文字播报文案。
- `spoken-copywriting`：读取公共文案规则和专用的中式真人口语规则，生成可直接真人口播的文案。
- `spoken-visual-planning`：在口播文案确认后，根据语义段规划少量稳定的理解强化型示意图，并输出 AI 生图正向/反向提示词。
- `publish-archive`：仅在“实际发布 + 明确归档”同时成立时写历史并增量更新索引。

正式内容生成按载体路由：

```text
确认选题
    ↓
CONTENT_FORMAT
├─ text_broadcast
│  └─ text-broadcast-copywriting
│
└─ spoken
   └─ spoken-copywriting
        ↓
   [用户明确要求视觉辅助]
        ↓
   spoken-visual-planning

用户实际发布 + 用户明确要求归档
    ↓
publish-archive
```

用户明确指定载体优先，其次使用候选的 `recommended_format`；旧候选或 `either` 默认短文字幕，以兼容原流程。两个文案 Skill 的公共规则统一位于 `shared/rules/copywriting-common-rules.md`。口播专用的真人中文语感规则位于 `.codex/skills/spoken-copywriting/references/chinese-spoken-naturalness.md`，不得继承到文字播报流程。

`spoken-visual-planning` 是口播文案完成后的可选视觉设计 Skill，负责获客封面、完整 PPT 页面设计、生图提示词和口播分段映射。口播改写、图片生成与发布归档分别由对应阶段处理。

`spoken-visual-planning` 采用“设计师主导”模式：当前账号的定位与人设负责说明角色、受众和业务语境，`账号视觉风格.md` 只补充已确认品牌资产与视觉禁用项；设计师先确定视觉基调、视觉基础与连续性语言，再逐页分配主要信息、辅助解释、环境与连续性的表达职责。背景在前景信息关系明确后回应页面需要，具体媒介由设计师按页面职责选择。

视觉工作流为理解传播任务、选定方向、规划封面与分页、确认、完成构图、提炼提示词和交付。统一视觉基础保留跨页稳定的外观关系，各页对象与布局依据内容选择。提示词只携带本图需要的具体画面、确切文字和生成要求；设计理由留在规划中。确认后交付独立生图指南与剪辑分段表，成图效果依据实际图像反馈判断。

## 数据层级

```text
历史 Markdown        = 已发布内容最终事实源
_history-index.jsonl = 历史机器检索层
_idea-index.jsonl    = 灵感机器检索层
_candidate-index.jsonl = 候选机器检索层
内容地图 / 缺口 / 复盘 = 人工查看与周期性重建的派生资产
```

索引可随时从 Markdown 重建：

```powershell
./shared/scripts/rebuild-history-index.ps1
./shared/scripts/rebuild-idea-index.ps1
./shared/scripts/rebuild-candidate-index.ps1
./shared/scripts/rebuild-derived-assets.ps1
```

传入 `-AccountId gzminge` 可只处理一个账号；不传时处理全部账号。

## 目录

```text
.
├─ AGENTS.md
├─ README.md
├─ GitHub-Sync-Rules.md
├─ .codex/
│  ├─ agents/
│  └─ skills/
├─ shared/
│  ├─ rules/
│  ├─ schemas/
│  └─ scripts/
└─ accounts/
   ├─ gzminge/
   ├─ gzxzcs/
   ├─ qycslc/
   ├─ gzcktxpp/
   └─ tsxbj/
```
