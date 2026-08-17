---
title: "编辑图片"
source_url: "https://open.dingtalk.com/document/development/dd-editpicture"
namespace: "development"
slug: "dd-editpicture"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 多媒体 > 图片 > 编辑图片"
doc_id: "PgpqCv4QHc"
updated_at: "2025-09-17 20:58:59"
---

> Source: https://open.dingtalk.com/document/development/dd-editpicture
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 多媒体 > 图片 > 编辑图片
> Updated: 2025-09-17 20:58:59

# 编辑图片

调用**dd.editPicture**编辑图片。支持远程 https 图片地址和本地虚拟路径，提供涂鸦、裁剪、马赛克等功能。

> **[!IMPORTANT]**
>
> 调用前请使用[dd.canIUse](https://open.dingtalk.com/document/orgapp/dd-caniuse)('editPicture')判断是否可用**。**

## **示例代码**

```
dd.editPicture({
      url: 'xxxx',
      success: function(res) {
        console.log(res.path)
      },
      fail: function(e){
        console.log(e)
      }
});
```

## **入参**

| **参数** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| url | String | 是 | 图片的远端路径或者本地路径。 |
| success | Function | 否 | 调用成功的回调函数。 |
| fail | Function | 否 | 调用失败的回调函数。 |

## **返回值**

**成功**

| **名称** | **类型** | **描述** |
| --- | --- | --- |
| path | string | 本地文件路径。 |

**失败**

| **errorCode** | **描述** |
| --- | --- |
| -1 | 用户取消。 |
| 1 | 参数为空。 |
| 2 | 参数异常。 |
| 3 | 内部异常。 |
