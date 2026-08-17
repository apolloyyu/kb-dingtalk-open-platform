---
title: 构建发布与版本
source_refs: Makefile, scripts/dev/build.sh, scripts/dev/build-all.sh, internal/app/version.go, pkg/cli/cli.go, internal/app/upgrade.go, internal/upgrade/github.go, internal/upgrade/version.go, internal/upgrade/downloader.go, internal/upgrade/verify.go, internal/upgrade/replacer.go, internal/upgrade/rollback.go, Formula/dingtalk-workspace-cli.rb
---

# 构建发布与版本

本篇覆盖 Makefile 目标、构建脚本、版本注入、`dws upgrade` 自升级与发布物。

## Makefile 主要目标

| 目标 | 说明 |
|---|---|
| `build` / `rebuild` | 调 `scripts/dev/build.sh` |
| `test` | `go test ./...` |
| `policy` | 跑 `scripts/policy/` 下检查：`check-open-source-assets.sh`、`check-schema-catalog.sh`、`check-schema-binary.sh` 等 |
| `generate-schema` | `go generate ./internal/cli` + `check-schema-assembly.sh`；仅刷新 `param_aliases_generated.go` 并验证装配确定性 |
| `package` | `build-all.sh` + `scripts/release/post-goreleaser.sh` |
| `release-pre` / `release-stable` | `scripts/release/release.sh` |
| `publish-homebrew-formula` | 发布 Homebrew 配方 |

## 构建脚本

- `scripts/dev/build.sh`：`go build -buildmode=pie -trimpath -ldflags="-s -w"`。**注意**：裸 `go build ./cmd` 会失败（输出名与目录冲突），必须 `-o dws`。
- `scripts/dev/build-all.sh`：ldflags `-X internal/app.version/gitCommit/buildTime` 注入版本信息，6 平台交叉构建，产出 `checksums.txt`（SHA256）。

## 版本变量

- `internal/app/version.go`：`var version = "dev"`，提供 `SetVersion()` / `RawVersion()`；
- `pkg/cli/cli.go`：`SetVersion` 供 overlay 注入。

## 自升级（dws upgrade）

命令入口 `internal/app/upgrade.go`，支持 `--check` / `--list` / `--version` / `--rollback` / `--force` / `--beta` / `--dry-run`；嵌入模式（embedded）下禁用自升级。`internal/upgrade` 各模块：

| 模块 | 职责 |
|---|---|
| `github.go` | `Client` / `ReleaseTrack`（release / beta），默认 `api.github.com`，仓库 `DingTalk-Real-AI/dingtalk-workspace-cli` |
| `version.go` | `CompareVersions` / `NeedsUpgrade` |
| `downloader.go` | 下载发布包 |
| `verify.go` | SHA256 校验 |
| `replacer.go` | `ReplaceSelf` 原子替换二进制 |
| `rollback.go` | `RollbackManager`，备份存放于 `~/.dws/data/backups` |

## 发布物

- `Formula/dingtalk-workspace-cli.rb`（及 `-beta.rb`）：Homebrew 配方，下载 URL 指向 GitHub Releases；
- 根目录 `CHANGELOG.md`：记录版本历史。

## 测试与策略门

```bash
DWS_PACKAGE_VERSION=0.0.0-test go test ./...
./scripts/policy/check-generated-drift.sh   # 生成物漂移检查
./scripts/policy/check-schema-catalog.sh    # Schema 契约检查
```
