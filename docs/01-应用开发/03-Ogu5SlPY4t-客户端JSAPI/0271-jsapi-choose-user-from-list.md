---
title: "chooseUserFromList"
source_url: "https://open.dingtalk.com/document/development/jsapi-choose-user-from-list"
namespace: "development"
slug: "jsapi-choose-user-from-list"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "通讯录 > chooseUserFromList"
doc_id: "hTQWGLKeUw"
updated_at: "2025-08-27 18:08:45"
---

> Source: https://open.dingtalk.com/document/development/jsapi-choose-user-from-list
> Path: 应用开发 / 客户端JSAPI / 通讯录 > chooseUserFromList
> Updated: 2025-08-27 18:08:45

# chooseUserFromList

调用chooseUserFromList，选取单个自定义联系人。

## 支持说明

| 应用能力 | Android | iOS | Harmony | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 6.0.0 | 6.0.0 | 7.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11505) |
| 小程序 | 6.0.0 | 6.0.0 | 7.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11505) |

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
- `users`（array，必填）：自定义可以选择对的用户的userId列表。
- `isShowCompanyName`（boolean）：是否显示公司名称。
- `disabledUsers`（array）：不可选用户的userId列表。
- `corpId`（string）：企业corpId。  
    
  > 在H5应用中必填。

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性为空

## **示例****代码**

### 默认出入参

```
dd.chooseUserFromList({
  title: '标题',
  users: ['userId0', 'userId2'],
  corpId: `corpId示例值`,
  disabledUsers: ['userId0', 'userId2'],
  isShowCompanyName: true,
  success: (res) => {
    const { name, avatar, userId } = res;
  },
  fail: () => {},
  complete: () => {},
});
```

`success`返回对象示例：

```
{
  "name": "钉小二",
  "avatar": "https://static.dingtalk.com/media/lADPDiCpu12oVqvNApTNApQ_660_660.jpg",
  "userId": "22055215283702319x"
}
```
