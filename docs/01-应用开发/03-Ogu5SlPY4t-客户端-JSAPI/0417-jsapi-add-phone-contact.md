---
title: "addPhoneContact"
source_url: "https://open.dingtalk.com/document/development/jsapi-add-phone-contact"
namespace: "development"
slug: "jsapi-add-phone-contact"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "设备能力 > 拨打电话 > addPhoneContact"
doc_id: "8WgOnPD1e6"
updated_at: "2025-08-27 18:08:10"
---

> Source: https://open.dingtalk.com/document/development/jsapi-add-phone-contact
> Path: 应用开发 / 客户端 JSAPI / 设备能力 > 拨打电话 > addPhoneContact
> Updated: 2025-08-27 18:08:10

# addPhoneContact

调用addPhoneContact，添加手机联系人。

用户可以选择将表单以“创建新联系人”或“添加到现有联系人”的方式，写入联系人资料到手机系统的通讯录。

## 支持说明

| 应用能力 | Android | iOS | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 7.0.0 | 7.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11626) |
| 小程序 | 7.0.10 | 7.0.10 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11626) |

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

- `name`（string，必填）：姓名。
- `email`（string）：电子邮件。
- `remark`（string）：备注。
- `address`（string）：联系地址。
- `phoneNumber`（string，必填）：手机号。
- `photoFilePath`（string）：头像本地文件路径。

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性描述：

### 入参

- `success`（boolean，必填）：是否添加成功。

## **示例****代码**

### 默认出入参

```
dd.addPhoneContact({
  name: `name示例值`,
  email: `email示例值`,
  remark: `remark示例值`,
  address: `address示例值`,
  phoneNumber: `phoneNumber示例值`,
  photoFilePath: `photoFilePath示例值`,
  success: (res) => {
    const { success } = res;
  },
  fail: () => {},
  complete: () => {},
});
```

`success`返回对象示例：

```
{ "success": true }
```
