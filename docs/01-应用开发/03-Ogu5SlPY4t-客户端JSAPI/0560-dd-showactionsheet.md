---
title: "显示操作菜单"
source_url: "https://open.dingtalk.com/document/development/dd-showactionsheet"
namespace: "development"
slug: "dd-showactionsheet"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 界面 > 交互反馈 > 显示操作菜单"
doc_id: "l2sVSquwnR"
updated_at: "2025-09-17 20:59:16"
---

> Source: https://open.dingtalk.com/document/development/dd-showactionsheet
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 界面 > 交互反馈 > 显示操作菜单
> Updated: 2025-09-17 20:59:16

# 显示操作菜单

调用**dd.showActionSheet**显示操作菜单。

## 扫码体验

![image.png ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7354199951/p163560.png)

## **示例****代码**

```
dd.showActionSheet({
  title: '钉钉-ActionSheet',
  items: ['菜单一', '菜单二', '菜单三'],
  cancelButtonText: '取消好了',
  success: (res) => {
     const btn = res.index === -1 ? '取消' : '第' + (res.index+1) + '个';
      dd.alert({
      title: `你点了${btn}按钮`
    });
  },
});
```

## **入参**

| **参数** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| title | String | 否 | 菜单标题。 |
| items | String Array | 是 | 菜单按钮文字数组。 |
| cancelButtonText | String | 否 | 取消按钮文案。  **[!IMPORTANT]**  Android平台此字段无效，不会显示取消按钮。 |
| success | Function | 否 | 调用成功的回调函数。 |
| fail | Function | 否 | 调用失败的回调函数。 |
| complete | Function | 否 | 调用结束的回调函数（调用成功、失败都会执行）。 |

**success 返回值**

| **名称** | **类型** | **描述** |
| --- | --- | --- |
| index | Number | 被点击的按钮的索引，从0开始。点击取消或蒙层时返回 -1。 |
