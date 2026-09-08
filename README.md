# 微信视频号多账号内容运营系统

这是一个统一维护六个微信视频号账号的内容运营 Monorepo。公共运营逻辑只保留一套，账号配置和内容数据库彼此隔离。

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
| `qycslc` | 备用 | 原 `gzlxcs` 备用库 | `accounts/qycslc/内容库` |
| `gzcktxpp` | 广州出口退税-翩翩 | `linqh92/gzcktxpp_wxvideos_contens` | `accounts/gzcktxpp/内容库` |
| `tsxbj` | 退税小笔记 | 本项目新建 | `accounts/tsxbj/内容库` |
| `gzlxcs` | 广州老徐聊企业财税合规 | `linqh92/qycslc_wxvideos_contens`（内容继承） | `accounts/gzlxcs/内容库` |

旧仓库只作为迁移对照、数据核验和回滚来源；本项目是后续统一维护入口。

## 使用方式

开始内容任务时先指定账号，例如“为 `gzminge` 给 5 个选题”。Agent 会锁定该账号，仅加载公共层和对应内容库。切换账号时必须明确给出新账号。

内容生产阶段分别由以下公共 Skill 处理：

- `idea-intake`：保存原始灵感并增量更新 Idea Index。
- `topic-planning`：由资深财税获客选题主编主导，围绕客户问题、业务重点和用户反馈调用材料；Index First 检索、按需读取正文，默认推荐 5 个合格选题及载体，不足不凑数；也支持灵感分析模式。
- `text-broadcast-copywriting`：读取公共文案规则，生成短文字幕与文字播报文案。
- `spoken-copywriting`：读取公共文案规则和专用的中式真人口语规则，生成可直接真人口播的文案。
- `spoken-visual-planning`：在口播文案确认后，规划搜索封面、推荐流/PPT封面与可独立阅读的完整PPT资料，并交付逐页设计执行方案。
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

`spoken-visual-planning` 是口播文案完成后的可选视觉设计 Skill。口播负责现场交流中的重点讲解，PPT依据相同事实形成能够独立阅读和分享的完整资料。PPT可以重新组织标题、字段、条件、过程与结论，同时保持确认事实和专业判断一致。

视觉规划包含三类页面职责：3:4搜索封面服务搜索结果、账号主页和内容列表中的关注吸引；16:9推荐流/PPT封面服务视频开场停留；16:9内容页服务视频理解和课后资料阅读。两个封面由主题文字、字体层级、编辑构图和视觉气质建立吸引力，内容页由信息编辑与信息设计组织完整关系。

设计师根据每页内容选择完整页面生图、生成视觉素材后排版，或使用原生文字、表格和图形构建页面。完整PPT文案作为内容依据，生图提示词只描述当前执行方式需要生成的画面和文字。确认完整分页内容、页面用途和设计方向后，交付PPT设计执行指南与剪辑分段表；剪辑表只包含视频实际使用的页面。

## 数据层级

选题记忆采用“有效偏好摘要＋近期 5 批＋旧推荐按需检索”。规则见 `shared/rules/topic-memory-reading.md`；工具 `shared/scripts/topic-memory.py` 提供本账号增量缓存、近期批次、反馈分页和关键词检索。首次实际使用建立缓存，正常追加只处理新增事件。原始月度日志保留，缓存和摘要可重建；关键词命中由主编进一步判断语义重复。

选题流程：账号锁定 → 主编理解业务重点与反馈 → 寻找客户问题并调用材料 → 判断选题价值 → 查重与必要核验 → 推荐并记录 → 下一轮根据反馈调整。

候选池是备查材料。已推荐题不会因仍为“可推荐”而自动再次入选；上轮未选题默认退出下一轮，明确否定按用户表达的题目或方向范围执行。旧题回归需要用户主动指定或新的材料、条件、判断价值。

`03-选题规划/推荐记录/YYYY-MM.jsonl` 是独立的推荐与反馈事实记录，按 `shared/schemas/topic-recommendation-log-schema.md` 增量保存，不属于可重建索引，也不改变候选状态。旧记录不猜测回填；首次实际推荐时开始记录。发布效果须经用户明确要求记录或复盘，缺失效果不等于零效果。

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
   ├─ tsxbj/
   └─ gzlxcs/
```
