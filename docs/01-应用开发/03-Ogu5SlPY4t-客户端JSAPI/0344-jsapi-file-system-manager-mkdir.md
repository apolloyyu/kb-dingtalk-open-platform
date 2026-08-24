---
title: "FileSystemManager.mkdir"
source_url: "https://open.dingtalk.com/document/development/jsapi-file-system-manager-mkdir"
namespace: "development"
slug: "jsapi-file-system-manager-mkdir"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "文件存储 > 文件 > FileSystemManager.mkdir"
doc_id: "lVxmIDUIoi"
updated_at: "2025-08-27 18:08:27"
---

> Source: https://open.dingtalk.com/document/development/jsapi-file-system-manager-mkdir
> Path: 应用开发 / 客户端JSAPI / 文件存储 > 文件 > FileSystemManager.mkdir
> Updated: 2025-08-27 18:08:27

# FileSystemManager.mkdir

调用FileSystemManager.mkdir，创建本地用户目录。

## 支持说明

| 应用能力 | Android | iOS | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 6.5.26 | 6.5.26 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10270) |

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

- `dirPath`（string，必填）：创建的目录路径。
- `recursive`（boolean）：例如，dirPath值为：/a/b/c。 如果recursive传true，创建目录时会先创建a，再创建b，最后再创建c。 如果recursive传false，a、b、c只要有一个目录不存在，接口会提示父级目录不存在。

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性描述：

### success

（boolean）目录创建成功时，返回true。 示例：`true`

## **示例****代码**

### 默认出入参

```
const fileSystemManager = dd.FileSystemManager();

fileSystemManager.mkdir({
  dirPath: '${dd.env.USER_DATA_PATH}/newDir',
  recursive: /a/b / c,
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
