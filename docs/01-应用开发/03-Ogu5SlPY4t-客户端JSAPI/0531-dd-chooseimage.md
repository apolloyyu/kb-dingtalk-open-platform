---
title: "选择图片"
source_url: "https://open.dingtalk.com/document/development/dd-chooseimage"
namespace: "development"
slug: "dd-chooseimage"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 多媒体 > 图片 > 选择图片"
doc_id: "8PI3UsAeul"
updated_at: "2025-09-17 20:58:56"
---

> Source: https://open.dingtalk.com/document/development/dd-chooseimage
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 多媒体 > 图片 > 选择图片
> Updated: 2025-09-17 20:58:56

# 选择图片

调用**dd.chooseImage**从本地相册选择图片。

## 扫码体验

![1595557841088-1 ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1479903061/p171722.png)

## **示例****代码**

```
dd.chooseImage({
  count: 2,
  success: (res) => {
      dd.alert({ 
          title: '选中的图片',
          content: JSON.stringify(res.filePaths)
      })
  },
});
```

## **入参**

| **参数** | 类型 | **是否必填** | **说明** |
| --- | --- | --- | --- |
| count | Number | 否 | 最大可选照片数。  **默认值**：1。 |
| sourceType | String[] | 否 | 相册选取或者拍照。  **默认****值：**['camera','album']。 |
| success | Function | 否 | 调用成功的回调函数。 |
| fail | Function | 否 | 调用失败的回调函数。 |
| complete | Function | 否 | 调用结束的回调函数。 |

**success 返回值**

| **名称** | 类型 | **描述** |
| --- | --- | --- |
| filePaths | String[] | 图片文件描述。 |

## **错误码**

| **error** | **描述** |
| --- | --- |
| 11 | 用户取消操作。 |
