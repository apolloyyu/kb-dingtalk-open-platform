---
title: 富媒体与文件
source_refs: internal/helpers/drive.go, internal/helpers/drive_transfer.go, internal/helpers/doc_media_upload.go, internal/helpers/chat_media_upload.go, internal/helpers/doc.go, internal/helpers/sheet.go, internal/localio/download.go, internal/localio/upload.go, internal/localio/publish.go, internal/localio/input.go
---

# 富媒体与文件

本篇覆盖云盘上传/下载、文档与群聊媒体上传、doc/sheet 命令组织，以及产品共享的安全本地 I/O（`internal/localio`）。

## 云盘命令（internal/helpers/drive.go）

`newDriveCommand()`（约 L363）构建 `dws drive` 命令组，主要子命令：

| 子命令 | 入口 | 说明 |
|---|---|---|
| `upload` | 约 L1284，RunE=`runDriveUpload` | 上传本地文件到云盘 |
| `download` | 约 L684 | 从云盘下载文件 |
| `upload-info` / `commit` | 上传流程的独立步骤命令 | 获取上传凭证 / 提交上传 |
| `pull` / `push` / `sync` | 约 L3328 起 | 云盘与本地的同步 |

语义目录与快捷方式位于 `internal/shortcut/drive/`，配套目录数据见 `semantic_catalog_drive.json`。

## 上传机制：三步凭证化 PUT（非 multipart）

云盘上传不使用 multipart，而是纯 HTTP PUT + 凭证化，共三步：

1. `get_upload_info` —— 获取上传凭证；响应由 `parseDriveUploadInfo`（drive.go 约 L227）解析；
2. `httpPutFile` —— 携带凭证 PUT 上传文件体，见 `driveUploadPut`（drive_transfer.go）；
3. `commit_upload` —— 提交完成上传。

要点：

- 中心协议为 `uploadType=httpToCenterWithToken`；
- PUT 遇到 401/403 时重取凭证重试一次；
- `decorateUploadSizeError` 为超限错误补充友好提示；
- `httpPutFile` 是可注入变量（helpers/doc.go 约 L29），便于测试替换。

## 下载机制：两步 + 分片并发 + 断点续传

下载同样两步：先 `download_file` 取下载 URL 与 headers，再 GET 文件体。传输实现为 `driveTransferDownload`（drive_transfer.go）：

- 文件 ≥ 2×partSize 时先用 `probeRangeSupport` 探测 Range 支持，随后并发分片下载（`downloadRangedParts` / `fetchRangeInto`），默认分片 16MB、并发 4；
- 支持断点续传：中间文件 `<dest>.dwspart` 与元数据 `.dwspart.meta`，状态由 `driveDownloadCheckpoint` 维护；
- 下载中遇到 401/403 经 `driveCredentialState.refresh` single-flight 刷新凭证后重试，避免并发分片重复取凭证。

## 媒体上传（文档附件 / 群文件）

- 文档媒体上传：`internal/helpers/doc_media_upload.go` 的 `runDocMediaUpload`，流程为 `get_doc_attachment_upload_info` → PUT；doc media 命令组在 doc.go 约 L2826。
- 群聊文件上传：`internal/helpers/chat_media_upload.go`，命令挂在 chat.go 约 L2130。

## doc / sheet 命令组织

- 文档：`newDocCommand()`（internal/helpers/doc.go 约 L1153）；快捷层在 `internal/shortcut/doc/`。
- 电子表格：`newSheetCommand()`（internal/helpers/sheet.go 约 L23），按能力细分为 `sheet_dimension` / `sheet_chart` / `sheet_comment` / `sheet_float_image` / `sheet_filter_view` / `sheet_batch.go` 等文件；快捷层在 `internal/shortcut/sheet/`。

## internal/localio：产品共享的安全本地 I/O

`internal/localio` 提供所有产品共用的安全文件操作：

- **download.go `Download`**：`ValidateDownloadURL` 仅信任 `dingtalk.com` / 阿里云 OSS 的 HTTPS 地址；解析目标 IP 排除公网 IP 防 SSRF；用 `os.Root` 打开目录防符号链接逃逸；写临时文件 + fsync 后原子 rename 发布；单文件上限 512MB。
- **upload.go `PutFile`**：向预签名 URL PUT 上传；拒绝 HTTP 重定向；上限 5GiB。
- **publish.go `PublishBytes`**：字节内容的安全落盘发布。
- **input.go `ReadTextInput`**：解析文本输入字面量 / `-`（stdin）/ `@file` 三种形式，上限 8MB。
