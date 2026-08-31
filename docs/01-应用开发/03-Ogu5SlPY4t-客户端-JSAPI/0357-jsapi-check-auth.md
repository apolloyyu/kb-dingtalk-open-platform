---
title: "checkAuth"
source_url: "https://open.dingtalk.com/document/development/jsapi-check-auth"
namespace: "development"
slug: "jsapi-check-auth"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "设备能力 > 系统信息 > checkAuth"
doc_id: "Ef4368Hmf3"
updated_at: "2025-08-27 18:07:29"
---

> Source: https://open.dingtalk.com/document/development/jsapi-check-auth
> Path: 应用开发 / 客户端 JSAPI / 设备能力 > 系统信息 > checkAuth
> Updated: 2025-08-27 18:07:29

# checkAuth

调用checkAuth，检查手机权限授权状态。

检查钉钉是否获得某个权限的系统授权，如果没有获得，可以通过showAuthGuide引导用户授权。

| 枚举值 | 描述 |
| --- | --- |
| CAMERA | 相机 |
| PHOTO | 相册 |
| LBS | 地理位置 |
| BLUETOOTH | 蓝牙 |
| MICROPHONE | 麦克风 |
| ADDRESSBOOK | 通讯录 |
| NOTIFICATION | 通知栏权限 |
| SHORTCUT | 创建桌面快捷方式（仅Android） |

注意：

蓝牙权限 仅在iOS13.1及以上系统支持。

## 支持说明

| 应用能力 | Android | iOS | Harmony | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 7.0.0 | 7.0.0 | 7.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11621) |
| 小程序 | 7.0.10 | 7.0.10 | 7.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11621) |

## 支持应用类型

| 应用类型 | 是否支持调用 |
| --- | --- |
| 企业内部应用 | 是 |
| 第三方企业应用 | 是 |
| 第三方个人应用 | 是 |

## 鉴权规则

无需鉴权即可直接调用

## **参数说明**

继承[通用输入对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性描述：

### 入参

- `authType`（string，必填）：权限类型

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性描述：

### 出参

- `granted`（boolean，必填）：是否获得授权

## **示例****代码**

### 默认出入参

```
dd.checkAuth({
  authType: 'PHOTO',
  success: (res) => {
    const { granted } = res;
  },
  fail: () => {},
  complete: () => {},
});
```

`success`返回对象示例：

```
{ "granted": true }
```
