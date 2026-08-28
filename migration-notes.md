# Monorepo 迁移记录

## 源仓库快照

四个源仓库在迁移时均为 `main` 且工作区干净；迁移过程中未修改源仓库。

| Account ID | 本地源目录 | Origin | HEAD | 源仓文件数（不含 `.git`） | 内容库文件数 |
| --- | --- | --- | --- | ---: | ---: |
| `gzminge` | `C:\Users\lqh\Desktop\广州敏哥聊财税-微信视频号` | `linqh92/gzminge_wxvideos_contens` | `9bcaca66e0e603875311f643c09a1a244753d3dd` | 164 | 150 |
| `gzxzcs` | `C:\Users\lqh\Desktop\广州小张说财税` | `linqh92/gzxzcs_wxvideos_contens` | `dba836f0d367a1b6b16e2fe757b833f724e75b00` | 88 | 74 |
| `qycslc` | `C:\Users\lqh\Desktop\企业财税-老陈` | `linqh92/qycslc_wxvideos_contens` | `c3143601c682d31b4c60e5e66940d51a6b2f98d3` | 156 | 142 |
| `gzcktxpp` | `C:\Users\lqh\Desktop\广州出口退税-翩翩` | `linqh92/gzcktxpp_wxvideos_contens` | `22b47cc845fbb17e1d8b2ce301a307ae216d4445` | 81 | 67 |

## Inventory 分类

### 完全相同

- `video-copywriting/SKILL.md`：四仓 SHA256 完全一致，公共层直接复制一份。
- `topic-planning/references/history-vault-rules.md`：`gzxzcs`、`qycslc`、`gzcktxpp` 完全一致，差异仓仅是旧内容库根路径。
- `publish-archive/SKILL.md`：`gzxzcs`、`qycslc`、`gzcktxpp` 完全一致，差异仓仅是旧内容库根路径。
- `GitHub-Sync-Rules.md`：`gzxzcs`、`qycslc`、`gzcktxpp` 完全一致。

### 高度相似

- 根 `AGENTS.md`、`video-account-operator.toml`、四个 Skill 的代理界面 YAML。
- `idea-intake`：流程一致，少量字段与旧路径不同。
- `topic-planning`：评分权重、候选来源、去重和事实核验一致，但混有不同账号业务硬编码。
- 账号内容库的目录骨架、维护说明、归档规范、候选模板和灵感模板。

### 账号专属

- 每个账号的定位、人设、固定选项、历史内容、灵感、候选池、内容地图、复盘、素材库、附件和 Obsidian 配置。
- 同名业务文件仍按账号分别保留，没有跨账号合并。

### 仅单仓存在

- 各账号独有的历史月份、业务选题池、灵感、复盘与素材文件均原样保留。
- `gzxzcs` 的 `视频内容模板.md` 等单仓文件保留在对应账号内容库。
- 无法归类的账号内容未删除或移入公共层。

## 公共文件来源

| 新文件 | 复制基准 | 后续修改 |
| --- | --- | --- |
| `.codex/skills/video-copywriting/SKILL.md` | `gzminge`；四仓完全一致 | 仅改为读取 `CURRENT_ACCOUNT` 的定位与人设两个文件 |
| `.codex/skills/topic-planning/references/history-vault-rules.md` | `gzxzcs`；与另两仓完全一致 | 改为 Index First、Body On Demand、派生资产按需读取 |
| `.codex/skills/publish-archive/SKILL.md` | `gzxzcs`；与另两仓完全一致 | 动态账号路径、增量索引、统一状态机、取消每篇全量地图重建 |
| `.codex/skills/topic-planning/SKILL.md` | `gzminge` 的完整版本 | 保留候选优先级、评分、去重和核验；删除账号硬编码并增加两种模式 |
| `.codex/skills/idea-intake/SKILL.md` | `qycslc` 的完整字段版本 | 动态账号路径、Account Lock、Idea Index 增量更新 |
| `.codex/agents/video-account-operator.toml` | `gzminge` 的职责结构 | 参数化为四账号运营 Agent |
| `GitHub-Sync-Rules.md` | `gzxzcs` | 未改写 |

## 账号数据迁移与修改

所有源内容库文件都能在新账号目录找到，源文件缺失数均为 0。首次复制完成时，四个目标内容库与源内容库逐文件 SHA256 不一致数均为 0。

后续只做指南要求的局部修改：

- 四账号 `账号基本定位.md`：原段落拆分；业务、受众、事实边界与内容目标保留。
- 四账号新增 `账号人设与文风.md`：由原定位文件的人设、文风、标题、幽默、禁用表达和反 AI 段落直接移动形成。
- 四账号维护说明、首页、候选模板、灵感说明和归档检查：改为引用公共状态机、三个 Index 与派生资产按需机制。
- `qycslc/04-内容复盘/重复选题检查.md`：将“每次扫描历史”改为 Index First；原复盘数据未重写。
- `gzminge` 四篇灵感：旧状态 `已采用并发布` 映射为灵感状态机终态 `已转选题`；正文未改。

定位拆分按非空原文行多重集校验，四账号均为 `multiset_diff=0`，没有丢失或改写原人设规则。

## 新增机器资产

每个账号新增：

- `account.yaml`
- `01-历史内容/_history-index.jsonl`
- `03-选题规划/灵感库/_idea-index.jsonl`
- `03-选题规划/_candidate-index.jsonl`
- `04-内容复盘/_derived-assets-summary.json`

Index 由 Markdown 自动生成，不人工录入历史事实。

