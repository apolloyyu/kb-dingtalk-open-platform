---
title: "chooseDistrict"
source_url: "https://open.dingtalk.com/document/development/jsapi-choose-district"
namespace: "development"
slug: "jsapi-choose-district"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "基础交互 > 界面 > 地图 > chooseDistrict"
doc_id: "R4Z5apvcxZ"
updated_at: "2025-08-27 18:05:52"
---

> Source: https://open.dingtalk.com/document/development/jsapi-choose-district
> Path: 应用开发 / 客户端 JSAPI / 基础交互 > 界面 > 地图 > chooseDistrict
> Updated: 2025-08-27 18:05:52

# chooseDistrict

调用chooseDistrict，选择地区。

地区选择器内置数据境内外及港澳台城市数据。

## 支持说明

| 应用能力 | Android | iOS | Harmony | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 7.0.10 | 7.0.10 | 7.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11618) |
| 小程序 | 7.0.10 | 7.0.10 | 7.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11618) |

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

### 入参

- `selectedCode`（string）：选择地区。

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性描述：

### 出参

- `region`（string）：选择地区。
- `regionCode`（string，必填）：地区编码。
- `regionName`（string，必填）：地区的名称
- `regionFullName`（string，必填）：地区的全名

## **示例****代码**

### 默认出入参

```
dd.chooseDistrict({
  selectedCode: '110000',
  success: (res) => {
    const { region, regionCode, regionName, regionFullName } = res;
  },
  fail: () => {},
  complete: () => {},
});
```

`success`返回对象示例：

```
{
  "region": "chooseDistrict",
  "regionCode": "chooseDistrict",
  "regionName": "chooseDistrict",
  "regionFullName": "中国_浙江_杭州"
}
```
