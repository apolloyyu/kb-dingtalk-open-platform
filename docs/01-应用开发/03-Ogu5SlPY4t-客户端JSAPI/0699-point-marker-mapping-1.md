---
title: "点标记（Marker）图鉴"
source_url: "https://open.dingtalk.com/document/development/point-marker-mapping-1"
namespace: "development"
slug: "point-marker-mapping-1"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 地图 > MapContext > 点标记（Marker）图鉴"
doc_id: "lDDPWuOZVV"
updated_at: "2025-09-17 21:00:46"
---

> Source: https://open.dingtalk.com/document/development/point-marker-mapping-1
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 地图 > MapContext > 点标记（Marker）图鉴
> Updated: 2025-09-17 21:00:46

# 点标记（Marker）图鉴

## **支持版本**

钉钉客户端版本号为5.1.2及以后的版本。

## **Marker 样式优先级说明**

- **customcallout、callout 与 label 互斥**优先级： label > customcallout > callout。
- **style 与 icon 互斥**优先级：style > iconAppendStr、style > icon。

## style

**图鉴列表**

| **结构** | **图鉴** |
| --- | --- |
| { type:1, text1:"Style1", icon1:'xxx', icon2:'xxx'} |  |
| { type:2, text1:"Style2", icon1:'xxx', icon2:'xxx'} |  |
| { type:3, icon:xxx, //选填 text:xxx, //必填 color:xxx, //默认#33B276 bgColor:xxx, //默认#FFFFFF gravity:"left/center/right", //默认 center fontType:"small/standard/large" //默认standard} |  |

## customcallout

**图鉴列表**

| **结构** | **图鉴** |
| --- | --- |
| { "type": 0, "time": "3", "descList": [{ "desc": "点击立即打车", "descColor": "#ffffff" }], "isShow": 1} |  |
| { "type": 1, "time": "3", "descList": [{ "desc": "点击立即打车", "descColor": "#333333" }], "isShow": 1} |  |
| { "type": 2, "descList": [{ "desc": "预计", "descColor": "#333333" }, { "desc": "5分钟", "descColor": "#108EE9" }, { "desc": "到达", "descColor": "#333333" }], "isShow": 1} |  |

## label

**参数列表**

| **参数** | **是否必填** | **说明** |
| --- | --- | --- |
| content | 是 | 内容。 |
| color | 否 | 颜色。  **默认值**：#000000。 |
| fontsize | 否 | 字号。  **默认值**：14。 |
| borderRadius | 否 | 绘图边角的弧度设置。  **默认值**：20。 |
| bgColor | 否 | 背景颜色。  **默认值**：#FFFFFF。 |
| padding | 否 | 填充。  **默认值**：10。 |

**图鉴列表**

| **结构** | **图鉴** |
| --- | --- |
| {content:"Hello Label",color:"#000000",fontSize:16,borderRadius:5,bgColor:"#ffffff",padding:12,} |  |
