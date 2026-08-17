---
title: "设备初始化及管理"
source_url: "https://open.dingtalk.com/document/development/device-initialize"
namespace: "development"
slug: "device-initialize"
group: "硬件开发"
tab: "门禁/考勤机接入"
breadcrumb: "设备初始化及管理"
doc_id: "uTgQxi6fs7"
updated_at: "2026-08-04 09:07:10"
---

> Source: https://open.dingtalk.com/document/development/device-initialize
> Path: 硬件开发 / 门禁/考勤机接入 / 设备初始化及管理
> Updated: 2026-08-04 09:07:10

# 设备初始化及管理

## 头文件

```
#include "dtiot_device_service.h"
```

## 设备初始化

**场景：**本函数用于初始化sdk，需要传入产品的信息和设备的信息。

产品的主要信息由钉钉颁发给三方，设备的信息由三方自己提供。

**函数：**

```
int (*init)(dtiot_product_info_t *product_info, 
            const char *device_sn,  //设备sn
      const char *device_mac, //设备mac
      const char *device_name,  //设备dn, 接入iot场景下使用
      const char *device_secret); //设备ds, 接入iot场景下使用
```

**参数：**

```
产品信息参数如下:
/**
 * @Description: 产品信息结构体
 * @Param: int32_t platform 设备接入的平台信息，包括阿里IoT、钉钉IoT平台等
 *         char *product_key, 产品KEY，在钉钉开放平台创建
 *         char *product_secret，产品secret，在钉钉开放平台创建
 *         int32_t net_device 设备使用的联网硬件信息
 *         int32_t bind_method 设备绑定的方式
 *         int32_t qr_type 静态二维码类型，是一型一码还是一机一码
 */
 
typedef struct dtiot_product_info
{
    int32_t platform;
    int32_t product_id;
    char product_key[PRODUCT_KEY_LEN + 1];
    char product_secret[PRODUCT_SECRET_LEN + 1];
    char product_sign_secret[PRODUCT_SIGN_LEN + 1];
    int32_t net_devices;
    int32_t bind_method;
    int32_t qr_type;
} dtiot_product_info_t;

其余为设备的信息
```

**示例**：

```
    char device_sn[DEVICE_NAME_LEN] = XXXXXX;
    char device_mac[DEVICE_NAME_LEN] = XXXXXX;
    
    dtiot_product_info_t product_info;
    memset(&product_info, 0, sizeof(product_info));
    strncpy(product_info.product_key, XXXXXX, PRODUCT_KEY_LEN);
    strncpy(product_info.product_secret, XXXXXX, PRODUCT_SECRET_LEN);
    strncpy(product_info.product_sign_secret, XXXXXX, PRODUCT_SIGN_LEN);
    product_info.product_id = XXXXXX;
    product_info.platform = PLATFORM_DTIOT;
    product_info.net_devices = NET_DEVICE_WIFI;
    product_info.qr_type = QR_TYPE_PER_DEVICE;
    product_info.bind_method = BIND_METHOD_STATICQR;
    
    dtiot_device_service_singleton()->init(&product_info,
                                    device_sn, 
                                    device_mac, 
                                    NULL,
                                    NULL);
```

## 设备绑定解绑回调

**场景：**注册设备绑定/解绑状态回调，绑定状态发生改变时会通知注册方

**函数:：**

```
int (*register_bind_callback)(void (*bind_status_callback)(int status));
```

## 设备查询绑定状态

**场景：**

```
主动获取绑定/解绑状态
```

**函数：**

```
int (*get_bind_status)(void);
```

## 设备解绑

**场景：**第三方主动解绑设备

**函数：**

```
int (*unbind_device)(void);
```
