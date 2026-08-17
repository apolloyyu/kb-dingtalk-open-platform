---
title: "创建企业群聊天"
source_url: "https://open.dingtalk.com/document/development/create-enterprise-group-chat"
namespace: "development"
slug: "create-enterprise-group-chat"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 开放接口 > 通讯录选人 > 创建企业群聊天"
doc_id: "b2qvtWFsXk"
updated_at: "2025-09-17 21:01:10"
---

> Source: https://open.dingtalk.com/document/development/create-enterprise-group-chat
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 开放接口 > 通讯录选人 > 创建企业群聊天
> Updated: 2025-09-17 21:01:10

# 创建企业群聊天

调用**dd.createGroupChat**创建企业群聊天。

## 示例代码

```
dd.createGroupChat({
    users: ['100','101'], //默认选中的userId列表
    success:function(res){
        /*{
            "id": 123   //企业群id
        }*/            
    },
    fail:function(err){
    }
});
```

## 入参

| **参数** | **类型** | **说明** |
| --- | --- | --- |
| users | String[] | 默认选中的用户列表。 |

## 返回结果

| **参数** | **说明** |
| --- | --- |
| id | 企业群id。 |
