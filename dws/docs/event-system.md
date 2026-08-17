---
title: 事件系统(event bus / consume / 订阅)
source_refs: internal/event/types.go, internal/event/bus/hub.go, internal/event/bus/daemon.go, internal/event/bus/lockfile.go, internal/event/busctl/spawn.go, internal/event/busctl/discover.go, internal/event/source/dingtalk.go, internal/event/source/portal_ticket.go, internal/event/source/personal.go, internal/event/transport/protocol.go, internal/event/endpoint.go, internal/event/consume/run.go, internal/event/consume/pipeline.go, internal/event/dedup/lru.go, internal/event/registry/catchall.go, internal/app/event_command.go, internal/app/event_listen_im.go
---

# 事件系统(event bus / consume / 订阅)

事件系统由本地 event bus、云端长连接源、bus→consumer 帧协议与消费端组成。

## 核心类型

`internal/event/types.go`:

- `SourceKind`:`app_stream` / `personal_stream`;
- `RawEvent`:`event_id` / `event_type` / `data` / `headers` / `subscribe_id` 等;
- `EmitFn`;
- `DedupKey()`;
- `ClientIDHash()` / `IdentityHash()`:sha256 前 8 字节,用于路径与 IPC 命名。

## 本地 event bus

`internal/event/bus/hub.go`:`Hub` / `Consumer`,`consumerMatcher` 支持 event_type 通配符 + 正则 filter + subscribe_id 精确匹配。提供 `NewHub`、`Register`、`Deliver`(满缓冲 drop-oldest,`DefaultSendBuffer`=100)、`Broadcast`、`Snapshot`、`StopConsumers`。

同目录相关文件:`daemon.go`(IPC wire 读写)、`lockfile.go`(单实例锁)、`meta.go`(bus.meta)、`metrics.go`、`tuning.go`(env 调参)。

`busctl/spawn.go` 负责 fork 隐藏的 `dws event _bus` 守护进程;配套 `discover.go`、`status.go`、`stop.go`。

## 云端 → bus:长连接

云端到 bus 的传输是长连接,不是轮询:

- `internal/event/source/dingtalk.go` 的 `DingtalkSource` 封装 `dingtalk-stream-sdk-go`(`client.NewStreamClient`),即 DingTalk Stream WebSocket;
- `portal_ticket.go` 通过 portal 取票建联;
- `source/personal.go` 为个人 Stream 源;
- `state.go` 为连接状态机。

## bus → consumer:帧协议与端点

- `internal/event/transport/protocol.go`:JSON 帧,包括 `hello` / `hello_ack` / `event` / `heartbeat` / `source_state` / `bye` / `status_req` / `credential_update` 等;
- `internal/event/endpoint.go` 的 `IPCEndpoint()`:Windows 使用命名管道 `\\.\pipe\dws-event-...`,其余平台使用 Unix socket。

## 消费端

`internal/event/consume/run.go` 的 `Run`:发现/fork bus 并 dial。相关文件:`pipeline.go`、`router.go`、`sink.go`、`formatter.go`(默认 NDJSON 输出到 stdout)、`run_many.go`、`validate.go`。

去重:`dedup/lru.go`;`registry/catchall.go` 提供 `CatchAllEventTypes()`。

## 命令与配置

命令入口:`internal/app/event_command.go` 的 `newEventCommand`(`Use` 为 `event`,基于 DingTalk Stream 长连接)。子命令包括:

- `event listen-im`(`internal/app/event_listen_im.go`):按 at-me / sender / group / all-direct / all-group 意图编译为个人 EventKey;
- `consume`:NDJSON 输出,支持 `--flatten`、`--max-events` / `--duration`;
- `list`、`schema`、`status`、`stop`、隐藏的 `_bus`。

`--as` 仅支持 `user`(app/bot 未开放)。相关环境变量:`DWS_STREAM_TICKET_MODE` / `SOURCE_ID` / `URL`。
