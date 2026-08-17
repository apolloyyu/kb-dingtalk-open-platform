---
title: "多语言配置"
source_url: "https://open.dingtalk.com/document/development/multi-language-configuration-1"
namespace: "development"
slug: "multi-language-configuration-1"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 小程序全局配置 > 多语言配置"
doc_id: "soFpKYk96q"
updated_at: "2025-09-17 20:57:52"
---

> Source: https://open.dingtalk.com/document/development/multi-language-configuration-1
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 小程序全局配置 > 多语言配置
> Updated: 2025-09-17 20:57:52

# 多语言配置

钉钉小程序可以配置 native 渲染的 tabBar 和 titleBar 部分的多语言文案。多语言配置通过小程序全局配置文件和页面配置文件进行注入。

> **[!NOTE]**
>
> 目前支持 zh\_CN（简体中文）、zh\_TW（繁体中文台湾）、zh\_HK（繁体中文香港）、en\_US（美式英文）、ja\_JP（日文）五种语言。

## 示例代码

```
// app.json 配置 tabBar 多语言文案
{
  "tabBar": {
    "items": [
      {
        "name": "首页",
        "name_locale": {
            "zh_CN": "首页",
          "en_US": "Home"
        }
      },
      {
        "name": "关于",
        "name_locale": {
            "zh_CN": "关于",
          "en_US": "About"
        }
      },
    ]
  }
}
```

```
// page.json 配置 titleBar 多语言文案
{
    "defaultTitle": "文件",
  "defaultTitle_locale": {
    "zh_CN": "文件",
    "en_US": "File",
    "ja_JP": "ファイル"
  }
}
```
