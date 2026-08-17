---
title: "获取员工信息"
source_url: "https://open.dingtalk.com/document/development/get-employee-information"
namespace: "development"
slug: "get-employee-information"
group: "专属版客户端插件"
tab: "功能介绍"
breadcrumb: "使用开放API > 获取员工信息"
doc_id: "PQaYt5lm09"
updated_at: "2025-10-15 17:02:29"
---

> Source: https://open.dingtalk.com/document/development/get-employee-information
> Path: 专属版客户端插件 / 功能介绍 / 使用开放API > 获取员工信息
> Updated: 2025-10-15 17:02:29

# 获取员工信息

## **基础信息**

获取当前登录账号的所在的专属组织相关信息。

| **API名称** | **调用方式** | **支持的平台** |
| --- | --- | --- |
| dd.user.getMainRealmOrgInfo | 异步调用 | Android、iOS、HarmonyOS |

## **入参**

无

## **返回结果**

返回Map数据。

| **参数** | **描述** |
| --- | --- |
| corpId | 账号所在的专属组织ID |
| staffId | 账号所在的专属组织中的员工UserID |

> **[!IMPORTANT]**
>
> 异常处理：
>
> - Android：如果当前账号的组织列表中没有专属钉钉组织，则回调onException。
> - iOS：通用错误返回会包含两个key：（1） errCode：错误码；（2）errMsg：错误描述。

## **示例代码**

Android-Java

```
ApiRequest request = new ApiRequest();
request.api = "dd.user.getMainRealmOrgInfo";

bundleContext.invokeApi(request, new ApiCallback<ApiResponse>() {
    @Override
    public void onSuccess(ApiResponse apiResponse) {
        if (apiResponse != null && apiResponse.isSuccess()) {
            String corpId = apiResponse.getString("corpId");
            String staffId = apiResponse.getString("staffId");
        }

     @Override
     public void onException(String code, String info) {
          // 异常处理
     }
```

Object C

```
id<DTKExternalNativeAPIServiceProtocol> handler = DTKExternalGetImpl(@"your_bundle_id", DTKExternalNativeAPIServiceProtocol);
NSString *apiName = @"dd.user.getMainRealmOrgInfo";
[handler invokeNativeAPI:apiName
            requestParam:^(id<DTKExternalAPIRequest>  _Nonnull param, id<DTKExternalAPIContext>  _Nonnull context) { }
                callback:^(NSDictionary * _Nonnull response) {
    //专属钉钉客户组织ID
    NSString *corpId = response[@"corpId"];
    //专属钉钉客户员工ID
    NSString *staffId = response[@"staffId"];
}];
```

arkts

```
myBundle.invokeApi({ api: 'dd.user.getMainRealmOrgInfo'})
.then((data) => { 
  data.getString('staffId')
  data.getString('corpId')
})
.catch((e: Error) => { 
  myBundle.toast(`用例失败：${e.message}`) 
})
```
