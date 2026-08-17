---
title: "显示确认框"
source_url: "https://open.dingtalk.com/document/development/dd-confirm"
namespace: "development"
slug: "dd-confirm"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 界面 > 交互反馈 > 显示确认框"
doc_id: "0nYjtpp5M7"
updated_at: "2025-09-17 20:59:13"
---

> Source: https://open.dingtalk.com/document/development/dd-confirm
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 界面 > 交互反馈 > 显示确认框
> Updated: 2025-09-17 20:59:13

# 显示确认框

调用**dd.confirm**显示确认框，可以配置确认框的标题、内容、确认或取消按钮的文字等。

## 扫码体验

![image.png ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6354199951/p163557.png)

## **示例****代码**

```
dd.confirm({
  title: '温馨提示',
  content: '您是否想查询快递单号：1234567890',
  confirmButtonText: '马上查询',
  cancelButtonText: '暂不需要',
  success: (result) => {
    dd.alert({
      title: `${result.confirm}`,
    });
  },
});
```

## **入参**

| **参数** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| title | String | 是 | confirm框的标题。 |
| content | String | 是 | confirm框的内容。 |
| confirmButtonText | String | 否 | 确认按钮文字。 |
| cancelButtonText | String | 否 | 取消按钮文字。 |
| success | Function | 否 | 调用成功的回调函数。 |
| fail | Function | 否 | 调用失败的回调函数。 |
| complete | Function | 否 | 调用结束的回调函数（调用成功、失败都会执行）。 |

**success 返回值**

| **名称** | **类型** | **描述** |
| --- | --- | --- |
| confirm | Boolean | 点击 confirm 返回 true，点击 cancel 返回false。 |
