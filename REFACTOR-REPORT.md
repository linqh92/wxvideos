# Monorepo 重构报告

## 结果

四个独立账号仓库已经合并为一个本地 Git Monorepo。公共 Agent、Skills、Schema 和脚本只保留一套；四个账号的配置、历史、灵感、候选、地图、复盘和素材继续独立保存。

## 最终目录结构

```text
wxvideos/
├─ .git/
├─ .codex/
│  ├─ agents/video-account-operator.toml
│  └─ skills/
│     ├─ idea-intake/
│     ├─ topic-planning/
│     │  └─ references/history-vault-rules.md
│     ├─ text-broadcast-copywriting/
│     ├─ spoken-copywriting/
│     └─ publish-archive/
├─ shared/
│  ├─ rules/
│  │  └─ copywriting-common-rules.md
│  ├─ schemas/
│  │  ├─ content-state-machine.md
│  │  ├─ history-index-schema.md
│  │  ├─ idea-index-schema.md
│  │  └─ candidate-index-schema.md
│  └─ scripts/
│     ├─ index-common.ps1
│     ├─ rebuild-history-index.ps1
│     ├─ rebuild-idea-index.ps1
│     ├─ rebuild-candidate-index.ps1
│     ├─ rebuild-derived-assets.ps1
│     └─ validate-monorepo.ps1
├─ accounts/
│  ├─ gzminge/
│  │  ├─ account.yaml
│  │  └─ 内容库/
│  ├─ gzxzcs/
│  │  ├─ account.yaml
│  │  └─ 内容库/
│  ├─ qycslc/
│  │  ├─ account.yaml
│  │  └─ 内容库/
│  └─ gzcktxpp/
│     ├─ account.yaml
│     └─ 内容库/
├─ AGENTS.md
├─ README.md
├─ GitHub-Sync-Rules.md
└─ migration-notes.md
```

## 账号迁移结果

| Account | 源内容库文件 | 源文件缺失 | History Index | Idea Index | Candidate Index |
| --- | ---: | ---: | ---: | ---: | ---: |
| `gzminge` | 150 | 0 | 85 | 28 | 0 |
| `gzxzcs` | 74 | 0 | 26 | 14 | 6 |
| `qycslc` | 142 | 0 | 40 | 73 | 34 |
| `gzcktxpp` | 67 | 0 | 13 | 19 | 4 |

`gzminge` 的 Candidate Index 为 0 是源数据结果：现有 `待发布选题.md` 只有模板，没有含明确公共状态的实际候选卡。Topic Planning 已规定此时不打开空模板。

## 状态机修复

唯一公共定义位于 `shared/schemas/content-state-machine.md`。

```text
灵感：待分析 → 可入池 → 已转选题
      待分析/可入池 → 已放弃

候选：待核验 → 可推荐 → 已采用 → 已发布
      待核验/可推荐/已采用 → 已放弃
```

`已采用` 不等于 `已发布`；只有 `publish-archive` 能在“实际发布 + 明确归档”同时成立时改为 `已发布`。

## 正式内容载体路由

```text
topic-planning
→ 用户确认选题
→ CONTENT_FORMAT
   ├─ text_broadcast → text-broadcast-copywriting
   └─ spoken         → spoken-copywriting
→ 用户实际发布 + 用户明确要求归档
→ publish-archive
```

候选的 `recommended_format` 仅是推荐，实际历史使用 `content_format`。用户明确载体永远覆盖推荐；旧候选或 `either` 保持 `text_broadcast` 默认。两个生成 Skill 共同引用 `shared/rules/copywriting-common-rules.md`，载体层分别负责视觉阅读与听觉口播。

## Token 优化

旧流程：每次重新列全部历史、解析全部 frontmatter、固定读取最新 10 篇正文和最多 10 篇相关正文，并默认加载内容地图、缺口与重复检查。

新流程：

```text
精简账号定位
→ History / Candidate / Idea 三个 Index
→ metadata 初筛 8～10 个方向
→ 正常只读约 5～8 篇高度相关正文
→ 实质去重与排序
→ 只核验最终政策型候选
```

选题阶段不读长人设文件；内容地图、缺口、重复检查和复盘退出默认上下文。同一会话数据不变时复用快照。

## Index 与派生资产

- 三类 Index 均已成功从 Markdown 生成，所有 JSONL 均可解析且路径只指向所属账号。
- 全量重建脚本重复运行后，16 个生成文件的 SHA256 变化数为 0。
- 将 `gzcktxpp` 的 History Index 临时移走后，脚本从 Markdown 重建出的 SHA256 与原文件完全相同。
- `rebuild-derived-assets.ps1` 生成确定性的机器摘要，不覆盖迁移来的人工内容地图、缺口分析、重复检查和月度复盘，避免丢失人工判断。

## 验证结果

| 测试 | 结果 |
| --- | --- |
| Account Isolation | 通过；每个 Index 的全部路径均以自身 `accounts/<id>/` 开头，公共规则默认禁止其他账号 |
| Account Switch | 通过；四账号定位哈希、显示名和三类数据计数独立，切换规则会使旧快照失效 |
| Idea Intake | 通过；测试笔记以 `待分析` 入 Idea Index，History/Candidate 未变化，测试资产已清理 |
| Idea State | 通过；测试状态 `待分析 → 可入池` 可写回并由 Index 读取，测试资产已清理 |
| Topic Planning | 通过；契约只默认读取精简定位与三个 Index，不读全部地图或固定最新 10 篇 |
| Historical Dedupe | 通过；相似方向先由 metadata 命中 2 篇历史，再只打开这 2 篇正文 |
| 再换 5 个 | 通过；Same Session Snapshot 规则已纳入 Skill 和验证脚本 |
| Copywriting | 通过；两个载体 Skill 共享账号、事实与合规规则，并分别保留短文视觉阅读和真人口播逻辑 |
| Archive | 通过；双触发条件、History Index 更新、候选发布终态与派生资产按需规则均通过契约校验 |
| Index Rebuild | 通过；缺失 Index 可从 Markdown 确定性恢复 |

最终验证：`shared/scripts/validate-monorepo.ps1` 通过 565 项检查。

## 遗留与边界

- 未配置新 GitHub remote，也未创建提交或推送；指南要求这些操作只能在用户以后明确要求并确认同步范围后执行。
- 原内容地图、缺口、重复检查和月度复盘包含人工判断，已完整保留且不自动覆盖；当前统一 rebuild 生成机器摘要。若未来要自动重写每一类 Markdown 地图，需要先为各地图明确无损生成规则。
- 本次验证覆盖文件、状态、索引、隔离与流程契约；没有代表账号实际发布内容，也没有触发任何真实政策核验或外部平台操作。
