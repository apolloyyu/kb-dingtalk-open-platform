---
title: "loadFontFace"
source_url: "https://open.dingtalk.com/document/development/jsapi-load-font-face"
namespace: "development"
slug: "jsapi-load-font-face"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "基础交互 > 界面 > 字体 > loadFontFace"
doc_id: "fkIC2FW9yn"
updated_at: "2025-08-27 18:05:51"
---

> Source: https://open.dingtalk.com/document/development/jsapi-load-font-face
> Path: 应用开发 / 客户端 JSAPI / 基础交互 > 界面 > 字体 > loadFontFace
> Updated: 2025-08-27 18:05:51

# loadFontFace

调用loadFontFace，动态的加载网络字体。

调用时请注意以下事项：

\* 仅支持 HTTPS 格式文件地址。

\* 钉钉小程序目前只支持 woff，otf，ttf，sfnt 字体。

\* 钉钉小程序不支持woff2字体，原因是：

 \* 相对其他格式字体，对内存占用较高。

 \* 此字体支持对于内核so size有较大负担，目前钉钉使用的u4内核3.0将woff2格式支持给裁剪了，导致无法正常显示，建议使用其他格式。

## 支持说明

| 应用能力 | Android | iOS | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 6.0.0 | 6.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10138) |

## 支持应用类型

| 应用类型 | 是否支持调用 |
| --- | --- |
| 企业内部应用 | 是 |
| 第三方企业应用 | 是 |
| 第三方个人应用 | 是 |

## 鉴权规则

无需鉴权即可直接调用

## **参数说明**

继承[通用输入对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性描述：

### Object

- `family`（string，必填）：字体名称。
- `source`（string，必填）：字体资源地址。

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性为空

## **示例****代码**

### 默认出入参

```
dd.loadFontFace({
  family: 'Bitstream Vera Serif Bold',
  source: 'url("https://sungd.github.io/Pacifico.ttf")',
  success: () => {},
  fail: () => {},
  complete: () => {},
});
```
