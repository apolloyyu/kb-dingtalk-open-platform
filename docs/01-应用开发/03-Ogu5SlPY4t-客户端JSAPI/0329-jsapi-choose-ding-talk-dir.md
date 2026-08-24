---
title: "chooseDingTalkDir"
source_url: "https://open.dingtalk.com/document/development/jsapi-choose-ding-talk-dir"
namespace: "development"
slug: "jsapi-choose-ding-talk-dir"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "文件存储 > 钉盘 > chooseDingTalkDir"
doc_id: "LfxJLrdrUN"
updated_at: "2025-08-27 18:08:19"
---

> Source: https://open.dingtalk.com/document/development/jsapi-choose-ding-talk-dir
> Path: 应用开发 / 客户端JSAPI / 文件存储 > 钉盘 > chooseDingTalkDir
> Updated: 2025-08-27 18:08:19

# chooseDingTalkDir

调用chooseDingTalkDir，唤起钉盘选择器， 从用户当前的企业空间或个人空间选择一个目录， 用以保存文件等操作。

## 支持说明

| 应用能力 | Android | iOS | Harmony | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 6.0.0 | 6.0.0 | 7.0.0 | 6.0.0 | 6.0.0 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10319) |
| 小程序 | 6.0.0 | 6.0.0 | 7.0.0 | 6.0.0 | 6.0.0 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10319) |

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

- `corpId`（string）：企业corpId。  
    
  > H5应用中必填。

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性描述：

### 出参

- `data`（array，必填）：文件信息。
- `data[].spaceId`（string，必填）：被选中的空间id。
- `data[].path`（string，必填）：被选中的文件夹路径。
- `data[].dirId`（string，必填）：被选中的文件夹id。

## **示例****代码**

### 默认出入参

```
dd.chooseDingTalkDir({
  corpId: 'ding',
  success: (res) => {
    const { data } = res;
  },
  fail: () => {},
  complete: () => {},
});
```

`success`返回对象示例：

```
{ "data": [{ "path": "/path/to", "dirId": "dddd", "spaceId": "xxxx" }] }
```
