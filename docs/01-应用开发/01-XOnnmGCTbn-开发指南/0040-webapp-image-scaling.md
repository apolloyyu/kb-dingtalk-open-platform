---
title: "图片缩放"
source_url: "https://open.dingtalk.com/document/dingstart/webapp-image-scaling"
namespace: "dingstart"
slug: "webapp-image-scaling"
group: "应用开发"
tab: "开发指南"
breadcrumb: "开发网页应用 > 开发参考 > 图片缩放"
doc_id: "KRZXdJjBXS"
updated_at: "2026-01-22 20:01:16"
---

> Source: https://open.dingtalk.com/document/dingstart/webapp-image-scaling
> Path: 应用开发 / 开发指南 / 开发网页应用 > 开发参考 > 图片缩放
> Updated: 2026-01-22 20:01:16

# 图片缩放

为了适应移动端加载速度和屏幕尺寸，系统支持对JSAPI获取的图片进行动态缩放。通过在原始图片URL后拼接特定参数，可实现按需裁剪与压缩，提升页面性能并优化用户体验。开发者可根据不同展示场景选择合适的缩放尺寸，避免因图片过大导致加载缓慢或过小引发模糊问题。

## **说明**

为了适应移动端的加载速度和屏幕尺寸，系统支持对通过JSAPI获取的图片进行动态缩放。该功能适用于H5微应用的开发。

在使用图片缩放功能前，请确保：

1. 图片原始URL需可公网访问；
2. 图片URL无时效性签名限制，或签名有效期足够长，避免因链接过期导致缩放失败；
3. 管理员与普通成员均可正常使用此功能，无角色权限限制。

合理选择缩放尺寸有助于提升页面性能并优化用户体验。建议根据展示场景选择合适尺寸：避免因图片过大导致加载缓慢，或因过小引发模糊问题。

## 图片缩放规则

- 原始图片URL格式：`https://example.com/image.jpg`。
- 缩放参数拼接方式：根据文件名+拼接规则，在URL末尾添加`@{width}_{height}`，表示目标宽高。
- 示例：将图片缩放为 200x150，URL应为`https://example.com/image.jpg_200_150.jpg`。
- 系统会自动按比例裁剪并缩放图像以匹配指定尺寸。

> **[!NOTE]**
>
> 建议宽度和高度均不超过2048px以保证处理效率与图像质量。

## **示例**

通过JSAPI获取的图片都支持缩放，比如图片：

```
http://gtms02.alicdn.com/tps/i2/TB1SlYwGFXXXXXrXVXX9vKJ2XXX-2880-1560.jpg
```

通过文件名拼接的方法缩放为最大宽高为250x250的尺寸。

```
http://gtms02.alicdn.com/tps/i2/TB1SlYwGFXXXXXrXVXX9vKJ2XXX-2880-1560.jpg_250x250.jpg
```

## **使用建议**

- 头像显示推荐使用`80x80`，兼顾清晰度与加载效率。
- 列表项配图建议设置为`250x250`，适配多数移动设备屏幕。
- 详情页主图可采用`800x600`，保证视觉质量的同时控制文件体积。
- 避免请求小于`40x40`的尺寸，可能导致图片严重模糊影响体验。

推荐使用以下拼接规则：

```
80x80 => _80x80.jpg
120x120 => _120x120.jpg
250x250 => _250x250.jpg
310x310 => _310x310.jpg
```

## 常见问题

**Q：拼接参数后图片未生效，仍返回原图？**

A：请检查URL拼接格式是否正确（必须为`_{width}x{height}.jpg`）。

**Q：缩放是否会拉伸图片？**

A：不会。系统默认保持原图比例，进行等比缩放+居中裁剪，避免变形。
