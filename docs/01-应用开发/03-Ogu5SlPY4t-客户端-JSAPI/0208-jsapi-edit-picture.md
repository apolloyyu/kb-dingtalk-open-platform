---
title: "editPicture"
source_url: "https://open.dingtalk.com/document/development/jsapi-edit-picture"
namespace: "development"
slug: "jsapi-edit-picture"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "多媒体 > 图片 > editPicture"
doc_id: "0U90mvOn2j"
updated_at: "2025-08-27 18:06:33"
---

> Source: https://open.dingtalk.com/document/development/jsapi-edit-picture
> Path: 应用开发 / 客户端 JSAPI / 多媒体 > 图片 > editPicture
> Updated: 2025-08-27 18:06:33

# editPicture

调用editPicture，编辑图片。

> 支持远程 https 图片地址和本地虚拟路径，提供涂鸦、裁剪、马赛克等功能。

## 支持说明

| 应用能力 | Android | iOS | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 6.0.0 | 6.0.0 | 7.0.10 | 7.0.10 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10199) |

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

- `url`（string，必填）：图片的远端路径或者本地路径。

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性描述：

### 出参

- `path`（string，必填）：编辑后的本地文件路径。

## **错误码**

| **错误码** | **描述** |
| --- | --- |
| 2 | 参数无效 |
| 3 | 系统异常 |
| -1 | 用户取消 |
| 1 | 当前端不支持此API |

## **示例****代码**

### 默认出入参

```
dd.editPicture({
  url: 'https://gw.alicdn.com/imgextra/i3/O1CN01Eg6xCm1nnsXZCnkP4_!!6000000005135-2-tps-200-200.png',
  success: (res) => {
    const { path } = res;
  },
  fail: () => {},
  complete: () => {},
});
```

`success`返回对象示例：

```
{ "path": "https://resource/427842e730ca5187d9275681e4968f99.image" }
```
