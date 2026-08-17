---
title: "唤起拨打电话菜单"
source_url: "https://open.dingtalk.com/document/development/call-menu"
namespace: "development"
slug: "call-menu"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 开放接口 > 电话 > 唤起拨打电话菜单"
doc_id: "3IEh7Im1fl"
updated_at: "2025-09-17 21:01:14"
---

> Source: https://open.dingtalk.com/document/development/call-menu
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 开放接口 > 电话 > 唤起拨打电话菜单
> Updated: 2025-09-17 21:01:14

# 唤起拨打电话菜单

调用**dd.showCallMenu**唤起拨打电话菜单。

## 示例代码

```
dd.showCallMenu({
    phoneNumber: ‘1xxxxxxxxxx’, // 期望拨打的电话号码
    code: '+86', // 国家代号，中国是+86
    showDingCall: true, // 是否显示钉钉电话
    success:function(res){   
    },
    fail:function(err){
    }
});
```

## 入参

| **参数** | **类型** | **说明** |
| --- | --- | --- |
| phoneNumber | String | 期望拨打的电话号码。 |
| code | String | 国家代号，中国是+86。 |
| showDingCall | Boolean | 是否显示钉钉电话。 |

![1522328074789-b3b2b41e-33ee-4f3b-9e6d-4ce1f47564e1.png ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1200805061/p163590.png)
