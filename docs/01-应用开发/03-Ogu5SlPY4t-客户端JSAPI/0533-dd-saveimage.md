---
title: "保存图片到手机相册"
source_url: "https://open.dingtalk.com/document/development/dd-saveimage"
namespace: "development"
slug: "dd-saveimage"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 多媒体 > 图片 > 保存图片到手机相册"
doc_id: "o74rfE66qi"
updated_at: "2025-09-17 20:58:58"
---

> Source: https://open.dingtalk.com/document/development/dd-saveimage
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 多媒体 > 图片 > 保存图片到手机相册
> Updated: 2025-09-17 20:58:58

# 保存图片到手机相册

调用dd.saveImage保存在线、本地临时或者永久地址图片到手机相册。

## **扫码体验**

![image.png ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7254199951/p163546.png)

## **示例代码**

```
dd.saveImage({
    url:'https://img.alicdn.com/tps/TB1sXGYIFXXXXc5XpXXXXXXXXXX.jpg'
});
```

## **入参**

| 参数 | 类型 | 是否必填 | 说明 |
| --- | --- | --- | --- |
| url | String | 是 | 要保存的图片地址 |
| success | Function | 否 | 调用成功的回调函数。 |
| fail | Function | 否 | 调用失败的回调函数。 |
| complete | Function | 否 | 调用结束的回调函数。 |

## **错误码**

| **error** | **描述** |
| --- | --- |
| 2 | 参数无效，没有传 url 参数。 |
| 15 | 没有开启相册权限(ios only)。 |
| 16 | 手机相册存储空间不足(ios only)。 |
| 17 | 保存图片过程中的其他错误。 |
