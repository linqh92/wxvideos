# 微信视频号多账号内容运营系统

这是一个统一维护四个微信视频号账号的内容运营 Monorepo。公共运营逻辑只保留一套，账号配置和内容数据库彼此隔离。

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

旧仓库只作为迁移对照、数据核验和回滚来源；本项目是后续统一维护入口。

## 使用方式

开始内容任务时先指定账号，例如“为 `gzminge` 给 5 个选题”。Agent 会锁定该账号，仅加载公共层和对应内容库。切换账号时必须明确给出新账号。

四个阶段分别由以下公共 Skill 处理：

- `idea-intake`：保存原始灵感并增量更新 Idea Index。
- `topic-planning`：Index First 检索、按需读取少量相关正文并输出选题；也支持灵感分析模式。
- `video-copywriting`：读取当前账号的业务定位和人设文风后生成文案。
- `publish-archive`：仅在“实际发布 + 明确归档”同时成立时写历史并增量更新索引。

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
│  ├─ schemas/
│  └─ scripts/
└─ accounts/
   ├─ gzminge/
   ├─ gzxzcs/
   ├─ qycslc/
   └─ gzcktxpp/
```

