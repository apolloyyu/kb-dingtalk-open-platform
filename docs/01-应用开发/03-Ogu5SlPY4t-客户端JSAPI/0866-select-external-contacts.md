---
title: "选择外部联系人"
source_url: "https://open.dingtalk.com/document/development/select-external-contacts"
namespace: "development"
slug: "select-external-contacts"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > H5微应用 > JSAPI参考 > 外部联系人 > 选择外部联系人"
doc_id: "PyPrwtYCSd"
updated_at: "2025-09-17 20:57:22"
---

> Source: https://open.dingtalk.com/document/development/select-external-contacts
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > H5微应用 > JSAPI参考 > 外部联系人 > 选择外部联系人
> Updated: 2025-09-17 20:57:22

# 选择外部联系人

调用**biz.contact.externalComplexPicker**选择外部联系人。

## 使用说明

| **客户端** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 支持 | 支持 | 不支持 |

```
dd.biz.contact.externalComplexPicker({
     "title":"测试标题",
     "corpId":"xxx",
     "multiple":false, //默认只有单选
     "limitTips":"超出了",
     "maxUsers":1000, //默认不限制
     "pickedUsers":[staffId1,staffId2,staffId3],  //已选，但可取消，只针对多选生效
     "disabledUsers":[staffId4,staffId5], //不可选，，只针对多选生效
     "requiredUsers":[staffId6], //必选，只针对多选生效
     onSuccess: function(data) {
    /* data结构
      [
        {
            "emplId":"123",//选人的员工id
            "name":"name",//员工姓名
            "avatar":"avatarURL",//头像url
            "orgName":"org"//公司名字
        },
       ...
      ]
    */
    },
    onFail : function(err) {}
});
```

## 参数说明

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| title | String | 选择联系人标题。 |
| corpId | String | 企业corpid。 |
| multiple | Boolean | 是否多选。 |
| maxUsers | int | 最多选择的人数。 |
| limitTips | String | 限制选择人数，0为不限制。 |
| pickedUsers | Array[String] | 默认选中的人。  **[!IMPORTANT]**  已选中可以取消。 |
| disabledUsers | Array[String] | 不能选的人。 |
| requiredUsers | Array[String] | 默认选中且不可取消选中状态的人。 |

## 返回结果

| 参数 | 说明 |
| --- | --- |
| name | 姓名。 |
| avatar | 头像图片url，可能为空。 |
| emplId | 用户的staffId。 |
| orgName | 公司名字。 |
