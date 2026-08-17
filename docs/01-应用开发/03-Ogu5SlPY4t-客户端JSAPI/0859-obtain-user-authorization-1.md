---
title: "授权获取审批实例数据"
source_url: "https://open.dingtalk.com/document/development/obtain-user-authorization-1"
namespace: "development"
slug: "obtain-user-authorization-1"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > H5微应用 > JSAPI参考 > 授权 > 授权获取审批实例数据"
doc_id: "kjn20FjWdm"
updated_at: "2025-10-16 18:48:09"
---

> Source: https://open.dingtalk.com/document/development/obtain-user-authorization-1
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > H5微应用 > JSAPI参考 > 授权 > 授权获取审批实例数据
> Updated: 2025-10-16 18:48:09

# 授权获取审批实例数据

调用**biz.auth.requestAuthInfo**唤起授权弹窗，提示用户授权，当用户点击**确认**按钮后，就可以有权限获取企业审批模板的审批数据。

> **[!NOTE]**
>
> 本接口只支持第三方企业应用调用，不支持企业内部应用、第三方个人应用调用。

## 使用说明

| **客户端** | Android | iOS | PC |
| --- | --- | --- | --- |
| 支持说明 | 支持（钉钉版本≥5.1.21） | 支持（钉钉版本≥5.1.21） | 不支持 |

```
requestAuthInfo({
    authorizeType: 1,
    ext:'{"modelKey":"dd.oa|bpms","bizScene":"processCode","content":["#这里填processCode(审批模板的唯一码)，仅支持1个#"]}',
        onSuccess:(res) => {
            console.log(res)
      },
      onFail:(err) => {
            console.log(err)
    }
})
```

## 参数说明

| 参数 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| authorizeType | String | 是 | 固定传**1**。 |
| ext | String | 是 | ``` {     "modelKey": "dd.oa|bpms",     "bizScene": "processCode",     "content": [         "#这里填processCode(审批模板的唯一码)，仅支持1个#"     ] } ```   只有**content**字段的`processCode`是可变的，其他字段都是常量。 |
| onSuccess | Function | 否 | 调用成功的回调函数。 |
| onFail | Function | 否 | 调用失败的回调函数。 |

## 返回结果

| 参数 | 说明 |
| --- | --- |
| 2 | 参数错误。 |
| 3 | 未知错误。 |
| -1 | 用户取消。 |
| 15001 | 当前用户无可授权项。 |
| 其他 | 服务端接口返回的错误。 |
