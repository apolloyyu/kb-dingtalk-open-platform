---
title: "editExternalUser"
source_url: "https://open.dingtalk.com/document/development/jsapi-edit-external-user"
namespace: "development"
slug: "jsapi-edit-external-user"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "通讯录 > editExternalUser"
doc_id: "ERs7pY9hM1"
updated_at: "2025-08-27 18:08:46"
---

> Source: https://open.dingtalk.com/document/development/jsapi-edit-external-user
> Path: 应用开发 / 客户端 JSAPI / 通讯录 > editExternalUser
> Updated: 2025-08-27 18:08:46

# editExternalUser

调用editExternalUser，编辑外部联系人。

## 支持说明

| 应用能力 | Android | iOS | Harmony | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 6.0.0 | 6.0.0 | 7.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10312) |
| 小程序 | 6.0.0 | 6.0.0 | 7.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10312) |

## 支持应用类型

| 应用类型 | 是否支持调用 |
| --- | --- |
| 企业内部应用 | 是 |
| 第三方企业应用 | 是 |
| 第三方个人应用 | 是 |

## 鉴权规则

在H5应用中，调用[dd.config](https://open.dingtalk.com/document/orgapp/jsapi-authentication)完成鉴权后使用

在小程序应用中，无需鉴权即可直接调用

## **参数说明**

继承[通用输入对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性描述：

### 入参

- `title`（string）：编辑页面的标题。
- `emplId`（string）：需要编辑的外部联系人的userId；不填，则为新增外部联系人。
- `name`（string）：需要新增的外部联系人的名字。
- `mobile`（string）：需要预填的手机号。
- `companyName`（string）：需要预填的公司名。
- `deptName`（string）：预填部门名字。
- `job`（string）：预填职位。
- `remark`（string）：备注信息。
- `corpId`（string）：企业corpId。  
    
  > H5应用必填。

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性描述：

### 出参

- `userId`（string）：外部联系人的userId。
- `name`（string）：外部联系人的姓名。
- `mobile`（string）：外部联系人的电话。
- `companyName`（string）：外部联系人的的公司名。
- `deptName`（string）：外部联系人的部门。
- `job`（string）：外部联系人的职位。
- `remark`（string）：外部联系人的备注信息。

## **示例****代码**

### 默认出入参

```
dd.editExternalUser({
  job: '总监',
  name: '钉小二',
  title: '添加外部联系人',
  corpId: 'ding12345',
  emplId: '09888',
  mobile: '13800000000',
  remark: '人事部一号位',
  deptName: '人事部',
  companyName: '钉钉',
  success: (res) => {
    const { job, name, mobile, remark, userId, deptName, companyName } = res;
  },
  fail: () => {},
  complete: () => {},
});
```

`success`返回对象示例：

```
{
  "job": "总监",
  "name": "钉小二",
  "mobile": "13800000000",
  "remark": "人事部一号位",
  "userId": "09888",
  "deptName": "人事部",
  "companyName": "钉钉"
}
```
