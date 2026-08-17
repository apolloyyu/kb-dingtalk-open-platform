---
title: 认证与凭证(auth / PAT / profile / 密钥存储)
source_refs: internal/app/auth_command.go, internal/auth/oauth_provider.go, internal/auth/device_flow.go, internal/auth/token.go, internal/auth/refresh_failure.go, internal/auth/filelock.go, internal/auth/keychain_store.go, internal/auth/profiles.go, internal/keychain/keychain.go, internal/keychain/file_dek.go, internal/keychain/keychain_linux.go, internal/keychain/keychain_windows.go, internal/pat/chmod.go, internal/pat/browser_policy.go, internal/profilectx/profile.go, internal/app/profile_command.go, internal/app/access_token_resolve.go, internal/transport/client.go, pkg/config/constants.go
---

# 认证与凭证(auth / PAT / profile / 密钥存储)

本文介绍登录方式、Token 结构与刷新、PAT、keychain 存储、profile 体系与凭证注入。

## 登录方式

登录命令为 `internal/app/auth_command.go` 的 `newAuthLoginCommand`:

- **默认 OAuth Loopback**:127.0.0.1 回调,`internal/auth/oauth_provider.go` 的 `OAuthProvider.Login` 先静默刷新,再打开浏览器;
- **`--device`**:使用 `DeviceFlowProvider`(`device_flow.go`),通过 user_code + 短 URL 轮询;
- **`--token`**:手动导入,有效期为 `config.ManualTokenExpiry` = 24h;
- **`--intl`**:走 `.io`(`LoginRegionInternational`)。

## Token 结构

`internal/auth/token.go` 定义 `TokenData`,字段包括 `AccessToken`、`RefreshToken`、`PersistentCode`、`ExpiresAt`、`RefreshExpAt`、`CorpID`/`UserID`、`ClientID`、`Source`、`LoginRegion`。

- `IsAccessTokenValid` 带 5 分钟提前量;
- 默认 access token 寿命 7200s(`pkg/config/constants.go`)。

## Token 刷新

`oauth_provider.go` 的 `GetTokenSnapshot` 提供快路径;过期且 refresh 有效时走 `lockedRefresh`:`AcquireDualLock`(进程锁 + 文件锁,`filelock.go`)双重检查后执行 `refreshWithRefreshToken`。

`refresh_failure.go` 的 `ClassifyRefreshFailure` 区分 transient / terminal;仅非瞬时失败才 `MarkProfileStatus(ProfileStatusExpired)`。

## auth status

`newAuthStatusCommand` 读取 token,必要时刷新;失败时标记 expired 或清除(`AutoPurgeToken`)。诊断 reason 包括:`ciphertext_key_mismatch`、`dek_missing`、`keychain_unavailable`、`token_refresh_failed`。

## PAT(注意命名)

PAT 是 **Personal Action Token(行为授权)**,不是 Personal Access Token:

- `dws pat chmod <scope>...` 经服务端 MCP 工具批量授权,scope 不落本地(`chmod.go`);
- `dws pat browser-policy` 本地策略存 `<configDir>/pat_policy.json`(`browser_policy.go`);
- host-owned 模式(设置 `DINGTALK_DWS_AGENTCODE`)下,PAT 错误以 stderr JSON + exit=4 返回(`internal/errors/pat.go` `ExitCodePermission=4`)。

## keychain 存储

`internal/keychain/keychain.go`:`Service`=`"dws-cli"`,AES-256-GCM 加密。

| 平台 | 实现 |
|---|---|
| macOS | DEK 存系统 Keychain(go-keyring),密文在 `~/Library/Application Support/dws-cli`;`DWS_DISABLE_KEYCHAIN` 可回退 file-DEK |
| Linux | file-DEK(`file_dek.go`,`~/.local/share/dws-cli/dek`)+ `.enc` 文件(`keychain_linux.go`) |
| Windows | DPAPI + HKCU 注册表(`keychain_windows.go`) |

keychain 槽位(`internal/auth/keychain_store.go`):

- 全局:`auth-token`
- 组织:`auth-token:<corpId>`
- 身份:`auth-token:id:<sha256>`

`token.json` 仅为标记(`TokenMarker`:`updated_at` / `revision`),不含凭证。

## profile 体系

元数据存 `<configDir>/profiles.json`(`internal/auth/profiles.go` 的 `ProfilesConfig`:`currentProfile` / `primaryProfile` / `orgCurrentProfiles`;`Profile` 含 `corpId` / `userId` / `status`),token 本体在 keychain。

- 切换命令:`internal/app/profile_command.go` 的 `list` / `use` / `switch`;
- 运行时覆盖用进程内变量 `profilectx.Set` / `Get`(`internal/profilectx/profile.go`,`SetRuntimeProfile`);
- selector 形如 `corpId:userId`(`ParseIdentitySelector`);
- 配置目录默认 `~/.dws`,可被 `DWS_CONFIG_DIR` 覆盖(`pkg/config/constants.go` `DefaultConfigDir`)。

## 凭证注入

- 无 token 环境变量注入;
- 显式 token 走 `--token`,`internal/app/access_token_resolve.go` 的 `TokenManager.Get`(`source="explicit"`);
- 请求注入 `Authorization: Bearer`(`internal/transport/client.go`)。

## 过期表现

- `ErrTokenDataNotFound` 提示 `no credentials found, run: dws auth login`;
- 刷新失败提示重新登录;refresh_token 过期有单独提示;
- profile 状态置 expired 后,`dws auth status` 显示未登录 + 原因。
