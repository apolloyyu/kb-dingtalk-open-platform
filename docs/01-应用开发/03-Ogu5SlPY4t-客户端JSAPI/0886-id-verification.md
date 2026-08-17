---
title: "专属实人认证"
source_url: "https://open.dingtalk.com/document/development/id-verification"
namespace: "development"
slug: "id-verification"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > H5微应用 > JSAPI参考 > 专属钉钉 > 专属实人认证"
doc_id: "GbChFxaga0"
updated_at: "2025-09-17 20:57:38"
---

> Source: https://open.dingtalk.com/document/development/id-verification
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > H5微应用 > JSAPI参考 > 专属钉钉 > 专属实人认证
> Updated: 2025-09-17 20:57:38

# 专属实人认证

调用**biz.ATMBle.exclusiveLiveCheck**，实现实人人脸对比。

## **JSAPI使用步骤**

1. 专属钉钉组织管理员登录[企业管理后台](https://oa.dingtalk.com)，依次选择**专属钉钉 > 专属开放 > 实人认证**，开通实人认证服务。

   ![iShot2022-09-06 11](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8475442661/p486759.png)
2. 开通实人认证服务后，添加**场景注册**。

   ![iShot2022-09-06 13](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9475442661/p486763.png)

## **使用说明**

| **客户端** | **Android** | **IOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 支持(钉钉版本≥6.5.40) | 支持(钉钉版本≥6.5.40) | 不支持 |

```
 dd.biz.ATMBle.exclusiveLiveCheck({
           agentId:"2748xxxx",
           corpId:"ding027xxxxx",
           onSuccess:(res)=>{
                  console.log(JSON.stringify(res))
                },
           onFail:(err) =>{
                  console.log(JSON.stringify(err))
                }
 })
```

## **参数说明**

| **参数** | **类型** | **是否必填** | **描述** |
| --- | --- | --- | --- |
| agentId | String | 是 | 钉钉应用agentId，参考[基础概念-AgentId念](https://open.dingtalk.com/document/orgapp/basic-concepts)。 |
| corpId | Sting | 是 | 钉钉组织corpId，参考[基础概念-CorpId念](https://open.dingtalk.com/document/orgapp/basic-concepts)。 |
| onSuccess | Function | 否 | 调用成功的回调函数。 |
| onFail | Function | 否 | 调用失败的回调函数。 |

## **返回结果**

### **成功**

| **字段** | **类型** | **描述** |
| --- | --- | --- |
| photoStatus | Number | 是否对比成功。   - **1**：对比验证成功 - **2**：对比验证失败 |

### **失败**

| **errorCode** | **errorMessage** | **说明** |
| --- | --- | --- |
| 2 | 应用未授权场景 | 开通实人认证服务后，未添加场景注册，参考本文档**JSAPI使用步骤**。 |
