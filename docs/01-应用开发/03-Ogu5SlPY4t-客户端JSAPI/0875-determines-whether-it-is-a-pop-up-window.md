---
title: "判断是否为弹窗窗口"
source_url: "https://open.dingtalk.com/document/development/determines-whether-it-is-a-pop-up-window"
namespace: "development"
slug: "determines-whether-it-is-a-pop-up-window"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > H5微应用 > JSAPI参考 > 打开新页面 > 判断是否为弹窗窗口"
doc_id: "j053r0XDrT"
updated_at: "2025-09-17 20:57:29"
---

> Source: https://open.dingtalk.com/document/development/determines-whether-it-is-a-pop-up-window
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > H5微应用 > JSAPI参考 > 打开新页面 > 判断是否为弹窗窗口
> Updated: 2025-09-17 20:57:29

# 判断是否为弹窗窗口

调用**biz.tabwindow.isTab**，判断当前页面是否为弹窗页面。

## 效果示例

- **打开的页面不是弹窗页面：**调用本jsapi方法，判断页面是否为弹窗窗口，判断结果为**false**。例如，在钉钉PC端工作台打开应用内页面，如下图所示。![iShot2022-05-31 14](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4441893561/p444735.png)
- **打开的页面是弹窗页面：**在打开的页面内调用本jsapi方法，判断页面是否为弹窗窗口，判断结果为**true**。

  > **[!IMPORTANT]**
  >
  > 目前只有使用[PC端打开新弹窗页面](https://open.dingtalk.com/document/orgapp/open-new-tab)方法才可以打开弹窗页面。

  ![lQLPJxZb6ecgiKzNAizNCEiwKtfKiXYQySYCl6hd2oAZAA_2120_556](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4877793561/p444666.png)

## 调试

本jsapi暂不支持调试。

## 使用说明

| **客户端** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 不支持 | 不支持 | 支持(钉钉版本≥6.5.10) |

```
dd.biz.tabwindow.isTab({
     onSuccess:function (result) {
        console.log(JSON.stringify(result))
     },
     onFail:function (err) {
     }
})
```

## 返回结果

### 成功

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| result | Boolean | 是否为弹窗。   - true：是 - false：否 |
