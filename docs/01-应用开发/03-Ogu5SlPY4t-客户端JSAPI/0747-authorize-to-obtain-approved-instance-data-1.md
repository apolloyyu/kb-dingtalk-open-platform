---
title: "授权获取审批实例数据"
source_url: "https://open.dingtalk.com/document/development/authorize-to-obtain-approved-instance-data-1"
namespace: "development"
slug: "authorize-to-obtain-approved-instance-data-1"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 开放接口 > 授权 > 授权获取审批实例数据"
doc_id: "aHyFEk67ou"
updated_at: "2025-09-17 21:01:22"
---

> Source: https://open.dingtalk.com/document/development/authorize-to-obtain-approved-instance-data-1
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 开放接口 > 授权 > 授权获取审批实例数据
> Updated: 2025-09-17 21:01:22

# 授权获取审批实例数据

调用**dd.requestAuthInfo**唤起授权弹窗，提示用户授权，当用户点击**确认**按钮后，就可以有权限获取企业审批模板的审批数据。

> **[!NOTE]**
>
> 本接口只支持第三方企业应用调用，不支持企业内部应用、第三方个人应用调用。

## 示例代码

> **[!NOTE]**
>
> 此接口仅支持钉钉客户端**5.1.21**及以上版本。在调用本接口前，你可以先使用[dd.canIUse](https://open.dingtalk.com/document/orgapp-client/dd-caniuse#topic-2024690)判断用户客户端版本是否支持调用。

```
dd.requestAuthInfo({
    authorizeType:1,
    ext:'{"modelKey":"dd.oa|bpms","bizScene":"processCode","content":["#这里填processCode，仅支持1个#"]}',
    success: (res) => {
        console.log(res)
    },
    fail: (err) => {
        console.error(err)
    }
})
```

## 入参

| 参数 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| authorizeType | String | 是 | 固定传**1**。 |
| ext | String | 是 | ``` {     "modelKey": "dd.oa|bpms",     "bizScene": "processCode",     "content": [         "#这里填processCode，仅支持1个#"     ] } ```   只有**content**字段的`processCode`是可变的，其他字段都是常量。 |
| success | Function | 否 | 调用成功的回调函数。 |
| fail | Function | 否 | 调用失败的回调函数。 |

## 错误码

| 参数 | 说明 |
| --- | --- |
| 2 | 参数错误。 |
| 3 | 未知错误。 |
| -1 | 用户取消。 |
| 15001 | 当前用户无可授权项。 |
| 其他 | 服务端接口返回的错误。 |
