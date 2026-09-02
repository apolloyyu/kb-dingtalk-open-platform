---
title: "requestAuthInfo"
source_url: "https://open.dingtalk.com/document/development/jsapi-request-auth-info"
namespace: "development"
slug: "jsapi-request-auth-info"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "获取凭证 > requestAuthInfo"
doc_id: "8at5dVSMt7"
updated_at: "2025-10-21 16:39:08"
---

> Source: https://open.dingtalk.com/document/development/jsapi-request-auth-info
> Path: 应用开发 / 客户端 JSAPI / 获取凭证 > requestAuthInfo
> Updated: 2025-10-21 16:39:08

# requestAuthInfo

调用 dd.requestAuthInfo 唤起授权弹窗，获取用户授权。

第三方企业应用在获取部分企业用户数据时候需要得到用户的授权，即可调用该 jsapi。

> 本接口只支持第三方企业应用调用，不支持企业内部应用、第三方个人应用调用。

> **重要**
>
> 2023年2月13日：为提升接口使用体验，针对获取用户授权接口规范进行升级，本文接口文档已不再推荐使用，且本接口仅保持现有功能，不再新增支持其他能力。
>
> - 如果未使用本接口，推荐使用统一授权套件。
> - 如果已使用本接口，建议您根据自身实际情况评估是否切换至推荐接口。

## 支持说明

| 应用能力 | Android | iOS | Harmony | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 6.0.0 | 6.0.0 | 不支持 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10296) |
| 小程序 | 6.0.0 | 6.0.0 | 不支持 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10296) |

## 支持应用类型

| 应用类型 | 是否支持调用 |
| --- | --- |
| 企业内部应用 | 否 |
| 第三方企业应用 | 是 |
| 第三方个人应用 | 否 |

## 鉴权规则

在H5应用中，调用[dd.config](https://open.dingtalk.com/document/orgapp/jsapi-authentication)完成鉴权后使用

在小程序应用中，无需鉴权即可直接调用

## **参数说明**

继承[通用输入对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性描述：

### 入参

- `authorizeType`（number，必填）：固定传1。
- `ext`（string，必填）：授权内容参数，根据授权场景不同有较大差异：  
    
  \* 审批 — 授权获取审批实例数据   
     
  ```  
    
  {  
   "modelKey": "dd.oa|bpms", // 常量  
   "bizScene": "processCode", // 常量  
   "content": [  
   "#这里填processCode(审批模板的唯一码)，仅支持1个#"  
   ]  
  }  
  ```  
    
  \* 服务窗 — 获取服务窗用户授权  
     
  ```  
  {  
   "dataType": 1, // 固定值  
   "fieldScope": [ // 固定值  
   "mobile",  
   "mainOrgName"  
   ]  
  }  
  ```  
    
  \* 服务窗 — 获取服务窗发送单聊消息授权  
     
  ```  
  {  
   "dataType": 1, // 固定值  
   "rpcScope": [ // 固定值  
   "send\_dingmi\_message"  
   ]  
  }  
  ```

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性为空

## **示例****代码**

### 审批-授权获取审批实例数据

```
dd.requestAuthInfo({
  ext: '{"modelKey":"dd.oa|bpms","bizScene":"processCode","content":["#这里填processCode(审批模板的唯一码)，仅支持1个#"]}',
  authorizeType: 1,
  success: () => {},
  fail: () => {},
  complete: () => {},
});
```

### 服务窗-获取服务窗用户授权

```
dd.requestAuthInfo({
  ext: '{"dataType":1,"fieldScope":["mobile","mainOrgName"]}',
  authorizeType: 1,
  success: () => {},
  fail: () => {},
  complete: () => {},
});
```

### 服务窗-获取服务窗发单聊消息授权

```
dd.requestAuthInfo({
  ext: '{"dataType":1,"rpcScope":["send_dingmi_message"]}',
  authorizeType: 1,
  success: () => {},
  fail: () => {},
  complete: () => {},
});
```
