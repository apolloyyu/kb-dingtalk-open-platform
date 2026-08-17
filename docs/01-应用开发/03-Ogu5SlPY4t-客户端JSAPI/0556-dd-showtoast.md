---
title: "显示弱提示"
source_url: "https://open.dingtalk.com/document/development/dd-showtoast"
namespace: "development"
slug: "dd-showtoast"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 界面 > 交互反馈 > 显示弱提示"
doc_id: "de9YrZal4K"
updated_at: "2025-09-17 20:59:14"
---

> Source: https://open.dingtalk.com/document/development/dd-showtoast
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 界面 > 交互反馈 > 显示弱提示
> Updated: 2025-09-17 20:59:14

# 显示弱提示

调用**dd.showToast**显示一个弱提示，在到达设定的显示时间后自动消失弱提示。

## 扫码体验

![1595556977173-3 ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7724572061/p172094.png)

## **示例****代码**

```
dd.showToast({
  type: 'success',
  content: '操作成功',
  duration: 3000,
  success: () => {
    dd.alert({
      title: 'toast 消失了',
    });
  },
});
```

## 入参

| **参数** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| content | String | 是 | 文字内容。 |
| type | String | 是 | toast 类型，展示相应图标，支持：   - success - fail - exception：exception 类型必须传文字信息。 - none（**默认值**） |
| duration | Number | 否 | 显示时长，单位为毫秒，默认 2000。  按系统规范，Android只有两种(<=2s和>2s)。 |
| success | Function | 否 | 调用成功的回调函数。 |
| fail | Function | 否 | 调用失败的回调函数。 |
| complete | Function | 否 | 调用结束的回调函数（调用成功、失败都会执行）。 |
