---
title: "PC端打开新弹窗页面"
source_url: "https://open.dingtalk.com/document/development/open-new-tab"
namespace: "development"
slug: "open-new-tab"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > H5微应用 > JSAPI参考 > 打开新页面 > PC端打开新弹窗页面"
doc_id: "VhcsYMpkB5"
updated_at: "2025-09-17 20:57:28"
---

> Source: https://open.dingtalk.com/document/development/open-new-tab
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > H5微应用 > JSAPI参考 > 打开新页面 > PC端打开新弹窗页面
> Updated: 2025-09-17 20:57:28

# PC端打开新弹窗页面

调用**biz.util.invokeWorkbench**，在PC端打开新弹窗页面。

## 效果示例

在钉钉电脑客户端工作台的微应用页面内调用本接口，调用效果如下图所示，钉钉客户端会弹出一个弹窗页面，弹窗页面内打开指定的页面地址。![iShot2022-04-01 17](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1575492561/p425990.png)

## 使用说明

| **客户端** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 不支持 | 不支持 | 支持 |

```
 dd.biz.util.invokeWorkbench({
    app_url:"https://www.dingtalk.com",
    app_info:{
         app_tab_key:"123",
         app_refresh_if_exist:true,
         app_active_if_exist:true
    },
    onSuccess:function (result) {
    },
    onFail:function (err) {
    }
})
```

## 参数说明

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| url | String | 弹窗页面的链接地址。  **[!NOTE]**  请输入http或https开头的链接，例如：https://www.dingtalk.com |
| app\_info | Object | 弹窗页面的配置信息。 |
| app\_tab\_key | String | 弹窗页面的Id。 |
| app\_refresh\_if\_exist | Boolean | 如果弹窗页面存在，是否刷新该页面。   - **true**：是。 - **false**：否。 |
| app\_active\_if\_exist | Boolean | 如果弹窗页面存在，是否切换到该页面。   - **true**：是。 - **false**：否。 |
| onSuccess | Function | 调用成功的回调函数。 |
| onFail | Function | 调用失败的回调函数。 |

## 返回结果

### 成功

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| result | JSONObject | 调用成功时，返回结果为`{"body":true}`。 |

### 失败

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| error | JSONObject | 错误信息。 |

## 错误码

| 参数 | 说明 |
| --- | --- |
| -1 | 参数url不正确。  **[!NOTE]**  请输入正确的url，且以http或https开头的链接，例如：https://www.dingtalk.com |
