---
title: "获取手机基础信息"
source_url: "https://open.dingtalk.com/document/development/obtain-basic-mobile-phone-information"
namespace: "development"
slug: "obtain-basic-mobile-phone-information"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > H5微应用 > JSAPI参考 > 设备 > 获取手机基础信息"
doc_id: "y55yyM31V3"
updated_at: "2025-09-17 20:56:03"
---

> Source: https://open.dingtalk.com/document/development/obtain-basic-mobile-phone-information
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > H5微应用 > JSAPI参考 > 设备 > 获取手机基础信息
> Updated: 2025-09-17 20:56:03

# 获取手机基础信息

调用**device.base.getPhoneInfo**获取手机基础信息。

## 调试

访问[JSAPI Explorer](https://open-dev.dingtalk.com/apiExplorer#/jsapi?api=device.base.getPhoneInfo)在线调试该接口。

## 使用说明

调用本接口前，请先引入钉钉js，参考[准备工作](https://open.dingtalk.com/document/orgapp/read-before-development)。

| **客户端** | **是否需要鉴权** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- | --- |
| 支持说明 | 不需要 | 支持 | 支持 | 不支持 |

```
dd.device.base.getPhoneInfo({
    onSuccess : function(data) {
        /*
        {
            screenWidth: 1080, // 手机屏幕宽度
            screenHeight: 1920, // 手机屏幕高度
            brand:'Mi', // 手机品牌
            model:'Note4', // 手机型号
            version:'7.0', // 版本
            netInfo:'wifi', // 网络类型 wifi／4g／3g 
            operatorType:'xx' // 运营商信息
        }
        */
    },
    onFail : function(err) {}
});
```

## 返回结果

| 参数 | 说明 |
| --- | --- |
| screenWidth | 手机屏幕宽度。 |
| screenHeight | 手机屏幕高度。 |
| brand | 手机品牌。 |
| model | 手机型号。 |
| version | 版本。 |
| netInfo | 网络类型: wifi、2g、3g、4g、unknown、none。  none表示离线。 |
| operatorType | 运营商信息。 |
