---
title: "配置宽屏卡片"
source_url: "https://open.dingtalk.com/document/development/configure-widescreen-cards"
namespace: "development"
slug: "configure-widescreen-cards"
group: "互动卡片"
tab: "卡片规范设计"
breadcrumb: "配置宽屏卡片"
doc_id: "3FTtkyDwmw"
updated_at: "2026-05-19 15:23:41"
---

> Source: https://open.dingtalk.com/document/development/configure-widescreen-cards
> Path: 互动卡片 / 卡片规范设计 / 配置宽屏卡片
> Updated: 2026-05-19 15:23:41

# 配置宽屏卡片

本文介绍了如何配置宽屏卡片。

## **卡片模板添加普通变量 config**

设置对象类型的普通变量 config，然后添加布尔值的子属性 autoLayout。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6947852271/p828865.png)

## **投放卡片时传参示例**

调用接口[创建并投放卡片](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0783-create-and-deliver-cards.md)，传参 cardData：

Java

```
import com.alibaba.fastjson.JSONObject;

// 创建 cardParamMap
JSONObject cardParamMap = new JSONObject();
cardParamMap.put("autoLayout", "true"); 

// 创建 cardData，将 cardParamMap 放入其中
JSONObject cardData = new JSONObject();
cardData.put("cardParamMap", cardParamMap);
```

Python

```
import json

# 创建 cardParamMap - 所有卡片模板参数都放在这里
card_param_map = {
    "autoLayout": "true", 
}

# 创建 cardData，将 cardParamMap 放入其中
card_data = {
    "cardParamMap": card_param_map
}
```

## **宽屏卡片效果**

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6947852271/p828880.png)
