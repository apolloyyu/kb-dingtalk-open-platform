---
title: "softap配网接入"
source_url: "https://open.dingtalk.com/document/development/odyrxi"
namespace: "development"
slug: "odyrxi"
group: "硬件开发"
tab: "门禁/考勤机接入"
breadcrumb: "softap配网接入"
doc_id: "jdzkjCjuW3"
updated_at: "2026-08-04 09:07:11"
---

> Source: https://open.dingtalk.com/document/development/odyrxi
> Path: 硬件开发 / 门禁/考勤机接入 / softap配网接入
> Updated: 2026-08-04 09:07:11

# softap配网接入

## 头文件

```
#include "dtiot_netconfig_bind_service.h"
```

## softap配网接入

### 启动softap配网

**场景：**启动softap配网。

**函数:**

```
int (*softap_bind_start)(dtiot_wifi_ap_mode_cb ap_mode_cb, dtiot_wifi_sta_mode_cb sta_mode_cb);
```

**参数:**

```
//切换成ap模式的回调
typedef int (*dtiot_wifi_ap_mode_cb)(dtiot_wifi_info_t *wifi_info);

//切换成station模式的回调
typedef int (*dtiot_wifi_sta_mode_cb)(dtiot_wifi_info_t *wifi_info, dtiot_net_info_t *net_info);

详细请参考头文件。
```

### 停止softap配网

**场景：**停止softap配网。

**函数:**

```
int (*softap_bind_stop)(void);
```

## 设备配网成功

**场景：**待wifi连接成功后，设置网络状态**。**

**函数：**

```
int (*set_net_status)(int net_status);
```
