---
title: "设置导航栏"
source_url: "https://open.dingtalk.com/document/development/dd-setnavigationbar"
namespace: "development"
slug: "dd-setnavigationbar"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 界面 > 导航栏 > 设置导航栏"
doc_id: "4ccoX06Hbe"
updated_at: "2025-09-17 20:59:07"
---

> Source: https://open.dingtalk.com/document/development/dd-setnavigationbar
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 界面 > 导航栏 > 设置导航栏
> Updated: 2025-09-17 20:59:07

# 设置导航栏

调用**dd.setNavigationBar**设置导航栏文字及样式。

## 扫码体验

![image.png ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4354199951/p163554.png)

## 示例代码

```
dd.setNavigationBar({
  title: '你好',
  backgroundColor: '#108ee9',
  success() {
    dd.alert({
      content: '设置成功', 
    });
  },
  fail() {
    dd.alert({
      content: '设置失败',
    });
  },
});
```

## 入参

| **名称** | **类型** | **是否必填** | **描述** |
| --- | --- | --- | --- |
| title | String | 否 | 导航栏标题。 |
| backgroundColor | String | 否 | 导航栏背景色，支持十六进制颜色值。 |
| reset | Boolean | 否 | 是否重置导航栏为钉钉默认配色。  **默认值**： false。 |
| success | Function | 否 | 调用成功的回调函数。 |
| fail | Function | 否 | 调用失败的回调函数。 |
| complete | Function | 否 | 调用结束的回调函数（调用成功、失败都会执行）。 |
