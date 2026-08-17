---
title: "设备管理"
source_url: "https://open.dingtalk.com/document/development/device-management"
namespace: "development"
slug: "device-management"
group: "硬件开发"
tab: "门禁Linux 接入"
breadcrumb: "SDK接入接口 > 设备管理"
doc_id: "YlS3T3BpQl"
updated_at: "2026-08-04 09:07:15"
---

> Source: https://open.dingtalk.com/document/development/device-management
> Path: 硬件开发 / 门禁Linux 接入 / SDK接入接口 > 设备管理
> Updated: 2026-08-04 09:07:15

# 设备管理

设备管理接口最主要的是设备初始化，必须首先调用进行设备的管理，包含头文件dtiot\_device\_service.h。

## 设置设备存储路径

**接口：**int (\*set\_storage\_path)(char\* path)

**请求参数：**

| 参数 | 是否必填 | 说明 |
| --- | --- | --- |
| path | 是 | 设置设备存储路径。  **[!NOTE]**  必须运行在init前面。 |

**返回结果：**

- **0**：成功
- **-1**或其他：失败

## 获取设备存储路径

**接口：**char\* (\*get\_storage\_path)(void)

**请求参数：**无

**返回结果：**char\*字符串类型存储路径。

## 初始化设备

**接口：**`int (*init)(dtiot_product_info_t *product_info`,

const char \*device\_sn, const char \*device\_mac, const char \*device\_name, const char \*device\_secret);

**请求参数：**

| 参数 | 是否必填 | 说明 |
| --- | --- | --- |
| product\_info | 是 | 产品信息，包含产品的PK、ID等信息。 |
| device\_sn | 是 | 设备SN号。 |
| device\_mac | 是 | 设备MAC地址。 |
| device\_name | 否 | IOT设备名。 |
| device\_secret | 否 | 设备安全信息。 |

**返回结果：**char\*字符串类型存储路径。

**示例**：

```
dtiot_product_info_t product_info;
memset(&product_info, 0, sizeof(product_info));
strncpy(product_info.product_key, DTIOT_PRODUCT_KEY, DTIOT_PRODUCT_KEY_LEN);
strncpy(product_info.product_secret, DTIOT_PRODUCT_SECRET, DTIOT_PRODUCT_SECRET_LEN);
strncpy(product_info.product_sign, DTIOT_PRODUCT_SIGN, DTIOT_PRODUCT_SIGN_LEN);
product_info.product_id = DTIOT_PRODUCT_ID;
product_info.platform = DTIOT_PLATFORM_DTIOT;
product_info.net_devices = DTIOT_NET_DEVICE_WIFI;
product_info.qr_type = DTIOT_QR_TYPE_PER_DEVICE;
product_info.bind_method = DTIOT_BIND_METHOD_STATICQR;
strncpy(product_info.product_manufacturer_version, DTIOT_MANU_VERSION, DTIOT_PRODUCT_MANUFACTURER_VERSION_LEN);

//产品初始化接口
dtiot_device_service_singleton()->init(&product_info, DTIOT_DEVICE_SN, DTIOT_DEVICE_MAC, NULL, NULL);
```

## 注册设备绑定解绑状态回调

**接口：**int (\*register\_bind\_listener)(void (\*bind\_status\_callback)(int status));

**请求参数：**

| 参数 | 是否必填 | 说明 |
| --- | --- | --- |
| bind\_status\_callback | 是 | 回调函数，status参考dtiot\_device\_bind\_state\_e定义。 |

**返回结果：**

- **0**：成功
- **其他**：失败

## 获取绑定状态

**接口：**int (\*get\_bind\_status)(void);

**请求参数：**

| 参数 | 是否必填 | 说明 |
| --- | --- | --- |
| bind\_status\_callback | 是 | 回调函数，status参考dtiot\_device\_bind\_state\_e枚举类型。 |

**返回结果：**

- **0**：成功
- **其他**：失败

## 解绑

**接口：**int (\*unbind)(void);

> **[!NOTE]**
>
> 解绑之后，一定要自己删除存储路径下的所有文件。

**请求参数：**无

**返回结果：**

- **0**：成功
- **其他**：失败

## 输出到标准输出

**接口：**int (\*set\_stdout)(int enable);

**请求参数：**

| 参数 | 是否必填 | 说明 |
| --- | --- | --- |
| enable | 否 | 该功能默认开启，即默认输出到标准输出。 |

**返回结果：**

- **0**：成功
- **其他**：失败

## 输出到文件

**接口：**int (\*set\_logfile)(int enable, unsigned int maxline, const char\* filepath);

**请求参数：**

| 参数 | 是否必填 | 说明 |
| --- | --- | --- |
| enable | 否 | 是否输出到文件。 |
| maxline | 否 | 最大行数。 |
| filepath | 否 | 提供路径和文件名，例如/tmp/xxxx.log。  如果不传值，日志输出到set\_storage\_path路径，名称为`dtiot.log`。 |

关于日志的控制：

通常输出到文件，需要指定输出路径。当开启日志输出后，SDK除了会输出到当前所指定文件之后，还会自动开启备份日志功能，目前不可关闭备份。

备份原理是：当前日志文件的大小达到设定的maxline之后，自动压缩后备份到存储目录的log子目录 。如果log子目录的压缩文件数已经达到10个，则自动清掉最老的那个，以保证最多存放10个备份日志。

**返回结果：**

- **0**：成功
- **其他**：失败

## 注册消息通知

**使用场景：**第三方注册了本函数，在拉取特征的长时间过程中，会得到回调，且消息类型为`DTIOT_DEV_NOTIFY_FACE_SYNCING`，里面给出了建议转圈UI显示的时间，一般是20秒，不一定很准。

UI根据这个建议在设备上显示“同步中”的动画，时长约20秒。但在未到20秒之前，有可能重复得到本消息，那么，计时应该重新开始，以保证转圈动画停止之时，同步中的业务是肯定完成了的。

**接口：**int (\*register\_dev\_notify)(int (\*dev\_notify\_callback)(dtiot\_dev\_notify\_t \*notify));

**请求参数：**

| 参数 | 是否必填 | 说明 |
| --- | --- | --- |
| dev\_notify\_callback | 否 | 注册消息通知(例如同步中)回调函数。 |

**返回结果：**

- **0**：成功
- **其他**：失败

**通知类型：**关于通知的类型，参考如下两个数据结构。

```
//第一个数据结构
typedef enum {
    DTIOT_DEV_NOTIFY_FACE_SYNCING = 1,              /*人脸信息，请使用联合体中的face结构*/
    DTIOT_DEV_NOTIFY_ATTENDANCE_RECORD_SYNCING,     /*考勤记录信息，请使用联合体中的attendance结构*/
    DTIOT_DEV_NOTIFY_REBOOT_APP,                    /*重启应用, 注意不是系统, 当SDK出现严重异常时需要重新启动会调用此接口*/   
    DTIOT_DEV_NOTIFY_MAX,
    } dtiot_device_dev_notify_e;
//第二个数据结构
typedef struct dtiot_dev_nofity {
  dtiot_device_dev_notify_e type;
  union {
    struct {
      unsigned int notify_keep_ms;    /*通告的建议有效时间(比如UI显示本消息)*/
    } face;
    struct {
      int status;                     /*当前网络状态, 1 or 0 */
      unsigned int count;             /*通告还有多少考勤记录未上传*/
    } attendance;
  } data;
} dtiot_dev_notify_t;
```

## 注册系统时间设置回调函数

**使用场景：**第三方注册了本函数，可以在设备登录之后得到SDK从云端得到的同步时间，建议用来设置一下系统的时间。如果系统有NTP等保障时间准确性的机制，可以不接这个接口。

**接口：**int (\*register\_set\_dev\_time)(int (\*set\_dev\_time\_callback)(unsigned long long timestamp));

**请求参数：**

| 参数 | 是否必填 | 说明 |
| --- | --- | --- |
| set\_dev\_time\_callback | 否 | 回调函数。 |

**返回结果：**

- **0**：成功
- **其他**：失败

## 获取SDK信息

**使用场景：**第三方注册了本函数，可以在设备登录之后得到SDK从云端得到的同步时间，建议用来设置一下系统的时间。如果系统有NTP等保障时间准确性的机制，可以不接这个接口。

**接口：**dtiot\_sdk\_info\_t\* (\*get\_sdk\_info)();

**请求参数：**无

**返回结果：**版本信息，例如1.0.0-R-20200426.1042
