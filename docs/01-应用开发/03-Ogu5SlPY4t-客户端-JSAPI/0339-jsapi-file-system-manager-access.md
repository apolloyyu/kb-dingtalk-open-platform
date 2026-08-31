---
title: "FileSystemManager.access"
source_url: "https://open.dingtalk.com/document/development/jsapi-file-system-manager-access"
namespace: "development"
slug: "jsapi-file-system-manager-access"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "文件存储 > 文件 > FileSystemManager.access"
doc_id: "hh26qZNzzI"
updated_at: "2025-08-27 18:08:24"
---

> Source: https://open.dingtalk.com/document/development/jsapi-file-system-manager-access
> Path: 应用开发 / 客户端 JSAPI / 文件存储 > 文件 > FileSystemManager.access
> Updated: 2025-08-27 18:08:24

# FileSystemManager.access

调用FileSystemManager.access，判断文件或者目录是否存在。

## 支持说明

| 应用能力 | Android | iOS | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 6.5.26 | 6.5.26 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10265) |

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

- `path`（string，必填）：文件夹路径或者文件路径。

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性描述：

### success

（boolean）文件或目录存在时，返回true。 示例：`true`

## **示例****代码**

### 默认出入参

```
const fileSystemManager = dd.FileSystemManager();

fileSystemManager.access({
  path: '${dd.env.USER_DATA_PATH}/newDir',
  success: (res) => {
    // res: true
  },
  fail: () => {},
  complete: () => {},
});
```

`success`返回对象示例：

```
true
```
