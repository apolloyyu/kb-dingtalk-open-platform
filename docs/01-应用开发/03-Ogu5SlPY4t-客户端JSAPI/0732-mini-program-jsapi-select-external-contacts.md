---
title: "选择外部联系人"
source_url: "https://open.dingtalk.com/document/development/mini-program-jsapi-select-external-contacts"
namespace: "development"
slug: "mini-program-jsapi-select-external-contacts"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 开放接口 > 通讯录选人 > 选择外部联系人"
doc_id: "cFbbgd5rrn"
updated_at: "2025-09-17 21:01:11"
---

> Source: https://open.dingtalk.com/document/development/mini-program-jsapi-select-external-contacts
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 开放接口 > 通讯录选人 > 选择外部联系人
> Updated: 2025-09-17 21:01:11

# 选择外部联系人

调用**dd.chooseExternalUsers**选择外部联系人。

## 示例代码

```
dd.chooseExternalUsers({
     title:"测试标题",
     multiple:true, //是否多选  true多选，false单选，默认是单选
     limitTips:"超出了",
     maxUsers:1000, //默认不限制
     pickedUsers:[userId1,userId2,userId3],  //已选，但可取消，只针对多选生效
     disabledUsers:[userId4,userId5], //不可选，只针对多选生效
     requiredUsers:[userId6], //必选，只针对多选生效，不会在结果中返回
     success:function(res){
       /* res结构
       [
        {
            "userId":"123",//选人的员工id
            "name":"name",//员工姓名
            "avatar":"avatarURL",//头像url
            "orgName":"org"//公司名字
        },
        ...
       ]
        */           
     },
     fail:function(err){
     }
});
```

## 入参

| **参数** | **类型** | **说明** |
| --- | --- | --- |
| title | String | 选择联系人标题。 |
| multiple | Boolean | 是否多选。 |
| maxUsers | Int | 最多选择的人数。 |
| limitTips | String | 限制选择人数，0为不限制。 |
| pickedUsers | String[] | 默认选中的人，值为userId列表。  **[!IMPORTANT]**  已选中可以取消。 |
| disabledUsers | String[] | 不能选的人，值为userId列表。 |
| requiredUsers | String[] | 默认选中且不可取消选中状态的人，值为userId列表。 |

## 返回结果

| **参数** | **说明** |
| --- | --- |
| name | 姓名。 |
| avatar | 头像图片url，可能为空。 |
| userId | 用户id。 |
| orgName | 公司名字。 |
