---
title: "创建企业聊天"
source_url: "https://open.dingtalk.com/document/development/create-enterprise-chat"
namespace: "development"
slug: "create-enterprise-chat"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > H5微应用 > JSAPI参考 > 通讯录选人 > 创建企业聊天"
doc_id: "yH8MEJQTQM"
updated_at: "2025-09-17 20:56:16"
---

> Source: https://open.dingtalk.com/document/development/create-enterprise-chat
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > H5微应用 > JSAPI参考 > 通讯录选人 > 创建企业聊天
> Updated: 2025-09-17 20:56:16

# 创建企业聊天

调用**biz.contact.createGroup**创建企业聊天。

## 调试

访问[JSAPI Explorer](https://open-dev.dingtalk.com/apiExplorer#/jsapi?api=biz.contact.createGroup)在线调试该接口。

## 使用说明

| **客户端** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 支持 | 支持 | 不支持 |

```
dd.biz.contact.createGroup({
    corpId: '', //企业id，可选，若配置必须是用户所属企业的corpId，即实现在指定企业创建群聊天；
    users: ['100','101'], //默认选中的用户工号列表，可选；使用此参数必须指定corpId
    onSuccess: function(result) {
        /*{
            id: 123   //企业群id
        }*/
    },
    onFail: function(err) {
    }
});
```

## 参数说明

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| corpId | String | 企业的corpId。 |
| users | Array[String] | 默认选中的用户列表，可选；  使用此参数必须指定corpId。 |

## 返回结果

| 参数 | 说明 |
| --- | --- |
| id | 企业群id。 |

展示效果如下图所示：

> **[!IMPORTANT]**
>
>  Android端和iOS端不同系统展示结果可能会出现差别，请以最终的展示效果为准。

![创建企业群](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7505834061/p177802.png)
