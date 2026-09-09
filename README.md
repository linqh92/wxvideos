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

在 ChatGPT 项目中，每个生产阶段使用一个独立对话。项目指令负责让每个新对话先读取最新 `AGENTS.md`；确定账号和阶段后，只加载当前 Skill 与最少必要文件。仓库提供长期规则和事实，不代表每个对话都要读取完整仓库。

只有“选题 → 文案”通过 ChatGPT 项目共享的 Handoff 文件交接：

```text
选题对话
→ 用户采用选题并指定短文或口播
→ 生成 `选题交接｜账号｜题目短名｜确认时间.md`
→ 在项目中新建文案对话
→ 输入 `@选题交接` 或题目短名快速引用
→ 只读取文案阶段最小上下文并创作
```

文案确认后不生成 Handoff。短文生成一份 `Repo内容文档` 后结束；口播必须先确认最终正文和三个主标题方案中的唯一最终标题，再同时生成一份 `Repo内容文档` 和一份 `视觉规划输入` 文档。标题没有明确选择时，文案对话会主动提醒，不会默认采用第一个标题或提前生成最终文件。

`Repo内容文档` 供用户切换到 Codex 后通过 `@` 引用并执行允许的仓库动作。它会继承选题 Handoff 中的推荐批次、用户 `selected` 反馈和尚未写入的完整事件，使反馈不会在文案阶段丢失；直接给题或参考重写则明确标记为“不适用”。该文档本身不表示已经写入、发布或归档。

`视觉规划输入` 供新的视觉对话通过 `@` 引用，只包含最终标题、最终口播和视觉阶段必要的确认信息；选题反馈、推荐批次、其余标题、草稿、检索过程和 Repo 操作均不带入。格式见 `shared/schemas/confirmed-copy-delivery-schema.md`。

Handoff 不是仓库文件，格式见 `shared/schemas/handoff-packet-schema.md`。新文件固定以 `选题交接` 开头，账号与题目短名排在时间前，便于在项目文件较多时通过 `@` 快速缩小结果；旧版 Handoff 仍可继续使用。

同一轮采用多个独立选题时，仍按“一条内容一份交接”处理。例如同时采用第 2、4 题，当前选题对话分别生成两份 `选题交接`，用户再为两份文件各建一个文案对话。两个选题可以共享原推荐批次，但必须分别拥有 `topic_id`、`content_id`、selected 反馈事件和最终交付文件；只有用户明确要求合并成一篇并确认合并后的唯一选题时，才使用一份 Handoff。

选题被正式采用后建立一个稳定 `content_id`，后续文案、可选视觉、发布和归档始终复用。规则见 `shared/schemas/content-identity-schema.md`。

具备本地执行能力时，可用 `shared/scripts/content-handoff.py` 生成内容 ID 或校验下载后的选题 Handoff；脚本只做身份与格式检查，不会把 Handoff 写入 Repo。

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
        ├─ Repo内容文档 → Codex
        └─ 视觉规划输入
             ↓ 用户明确要求视觉辅助
           新视觉对话 → spoken-visual-planning

用户实际发布 + 用户明确要求归档
    ↓
publish-archive
```

用户明确指定载体优先，其次使用候选的 `recommended_format`；旧候选或 `either` 默认短文字幕，以兼容原流程。两个文案 Skill 的公共规则统一位于 `shared/rules/copywriting-common-rules.md`。口播专用的真人中文语感规则位于 `.codex/skills/spoken-copywriting/references/chinese-spoken-naturalness.md`，不得继承到文字播报流程。

`spoken-visual-planning` 是口播文案完成后的可选视觉设计 Skill。口播负责现场交流中的重点讲解，PPT依据相同事实形成能够独立阅读和分享的完整资料。PPT可以重新组织标题、字段、条件、过程与结论，同时保持确认事实和专业判断一致。

视觉规划包含三类页面职责：3:4搜索封面服务搜索结果、账号主页和内容列表中的关注吸引；16:9推荐流/PPT封面服务视频开场停留；16:9内容页服务视频理解和课后资料阅读。两个封面由主题文字、字体层级、编辑构图和视觉气质建立吸引力，内容页由信息编辑与信息设计组织完整关系。

设计师根据每页内容选择完整页面生图、生成视觉素材后排版，或使用原生文字、表格和图形构建页面。完整 PPT 文案作为内容依据，生图提示词只描述当前执行方式需要生成的画面和文字。确认完整分页内容、页面用途和设计方向后，交付 PPT 设计执行指南与剪辑分段表；剪辑表只包含视频实际使用的页面。这些视觉阶段文件保留在 ChatGPT 项目中，不写入账号内容库，也不进入 GitHub 同步范围。

Repo 始终保存一套长期正式事实，不按阶段保存多份 Handoff、视觉规划输入或 Chat 中间 revision。推荐与明确反馈按现有规则持久化；Repo 内容文档只是 Codex 的确认输入，最终文案仍只有在用户明确要求且存在对应写入规则时才保存；实际发布内容仍通过 `publish-archive` 进入历史事实源。ChatGPT“对话”模式通过 GitHub 集成读取项目时直接按只读处理，不尝试写入，也不会再触发 `403`；尚未执行的推荐与反馈事件通过 Handoff 和后续 Repo 内容文档交给 Codex。其他只读环境同样只输出待执行动作，不得声称已经写入、更新索引或同步。

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

## 跨平台同步 GitHub

安装 Python 3.9+ 和 Git 后，可在 Windows、macOS 或 Linux 的项目目录运行：

```text
python shared/scripts/sync_github.py
```

脚本会先获取并比较 `origin/main`，展示完整文件清单和提交信息；只有手动输入“同步”后才会提交和推送。只想查看同步计划时使用：

```text
python shared/scripts/sync_github.py --dry-run
```

脚本不依赖第三方 Python 包，也不会自动解决远端领先或文件冲突。复制到其他 Git 仓库后，可通过 `--repo`、`--remote` 和 `--branch` 调整目标。

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
