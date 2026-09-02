---
title: "chooseExternalUsers"
source_url: "https://open.dingtalk.com/document/development/jsapi-choose-external-users"
namespace: "development"
slug: "jsapi-choose-external-users"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "通讯录 > chooseExternalUsers"
doc_id: "33PPoot2WX"
updated_at: "2025-08-27 18:08:45"
---

> Source: https://open.dingtalk.com/document/development/jsapi-choose-external-users
> Path: 应用开发 / 客户端 JSAPI / 通讯录 > chooseExternalUsers
> Updated: 2025-08-27 18:08:45

# chooseExternalUsers

调用chooseExternalUsers，选择外部联系人。

## 支持说明

| 应用能力 | Android | iOS | Harmony | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 6.0.0 | 6.0.0 | 7.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10311) |
| 小程序 | 6.0.0 | 6.0.0 | 7.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10311) |

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

- `title`（string）：选择页面的标题。
- `multiple`（boolean）：是否可多选：  
    
  \* true: 可多选  
  \* false：仅单选  
    
  > 默认仅单选。
- `limitTips`（string）：超过限定人数返回的提示内容。
- `maxUsers`（number）：最大可选人数，最大值为10000。
- `pickedUsers`（array）：已选用户的userId列表。
- `disabledUsers`（array）：不可选用户的userId列表。
- `requiredUsers`（array）：必选用户。  
    
  > 不可取消选中状态。
- `corpId`（string）：企业corpId。  
    
  > H5应用必填。

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性描述：

### 出参

（array）

## **示例****代码**

### 默认出入参

```
dd.chooseExternalUsers({
  title: '选择员工',
  corpId: 'ding12345',
  maxUsers: 100,
  multiple: true,
  limitTips: '选择人数不能超过20个',
  pickedUsers: ['userId0', 'userId2'],
  disabledUsers: ['userId0', 'userId2'],
  requiredUsers: ['userId0', 'userId2'],
  success: (res) => {
    // res: [{name: '钉小二',avatar: 'https://static.dingtalk.com/media/lADPDiCpu12oVqvNApTNApQ_660_660.jpg',userId: '22055215283702319x',orgName: '钉钉',}]
  },
  fail: () => {},
  complete: () => {},
});
```

`success`返回对象示例：

```
[
  {
    "name": "钉小二",
    "avatar": "https://static.dingtalk.com/media/lADPDiCpu12oVqvNApTNApQ_660_660.jpg",
    "userId": "22055215283702319x",
    "orgName": "钉钉"
  }
]
```
