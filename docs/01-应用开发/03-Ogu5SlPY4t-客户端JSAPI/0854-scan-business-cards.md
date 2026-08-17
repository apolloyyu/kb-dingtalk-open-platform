---
title: "扫名片"
source_url: "https://open.dingtalk.com/document/development/scan-business-cards"
namespace: "development"
slug: "scan-business-cards"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > H5微应用 > JSAPI参考 > 扫码 > 扫名片"
doc_id: "dSXaaz5ofu"
updated_at: "2025-09-17 20:57:13"
---

> Source: https://open.dingtalk.com/document/development/scan-business-cards
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > H5微应用 > JSAPI参考 > 扫码 > 扫名片
> Updated: 2025-09-17 20:57:13

# 扫名片

调用**biz.util.scanCard**扫名片。

## 调试

访问[JSAPI Explorer](https://open-dev.dingtalk.com/apiExplorer#/jsapi?api=biz.util.scanCard)在线调试该接口。

## 使用说明

| **客户端** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 支持 | 支持 | 不支持 |

```
dd.biz.util.scanCard({ // 无需传参数
    onSuccess: function(data) {
    //onSuccess将在扫码成功之后回调
      /* data结构
       {
         "ADDRESS": "深圳市南山区软件产业基地", 
         "COMPANY": "深圳市李乔科技有限公司", 
         "NAME": "李乔",
         "MPHONE": "861333567890",  
         "PHONE": "01087654321", 
         "POSITION": "CEO", 
         "IMAGE": "http://www.taobao.com/xxx.jpg", 
         "dt_tranfer": "BusinessCard", 
         "request_id": "20161206144554_efd40582d477a29df2e3bc62c260cdae"
      }
      */
    },
   onFail : function(err) {
   }
})
```

## 返回结果

| 参数 | 说明 |
| --- | --- |
| ADDRESS | 地址。 |
| COMPANY | 公司。 |
| NAME | 姓名。 |
| MPHONE | 手机号。 |
| PHONE | 电话。 |
| IMAGE | 名片图片地址，可供用户手动上传名片。 |
| POSITION | 职位。 |
