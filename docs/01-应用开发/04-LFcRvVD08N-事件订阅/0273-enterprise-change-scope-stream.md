---
title: "企业变更第三方企业应用的授权范围"
source_url: "https://open.dingtalk.com/document/development/enterprise-change-scope-stream"
namespace: "development"
slug: "enterprise-change-scope-stream"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "历史文档（不推荐） > Stream推送 > 授权事件 > 企业变更第三方企业应用的授权范围"
doc_id: "w1zCx4tQEc"
updated_at: "2025-10-30 21:55:04"
---

> Source: https://open.dingtalk.com/document/development/enterprise-change-scope-stream
> Path: 应用开发 / 事件订阅 / 历史文档（不推荐） > Stream推送 > 授权事件 > 企业变更第三方企业应用的授权范围
> Updated: 2025-10-30 21:55:04

# 企业变更第三方企业应用的授权范围

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 企业变更第三方企业应用的授权范围 |
| 英文名称 | org\_suite\_change |

## 功能描述

eventType为org\_suite\_change，表示企业变更第三方企业应用的授权范围。其中authCorpInfo, authInfo和authUserInfo三段结构信息请参考[获取企业授权信息](https://open.dingtalk.com/document/isvapp/obtains-the-basic-information-of-an-enterprise)。authScope结构信息清参考[获取通讯录权限范围](https://open.dingtalk.com/document/isvapp/obtain-corpsecret-authorization-scope)。

## 支持应用类型

| 应用类型 | 是否支持 |
| --- | --- |
| 企业内部应用 | 不支持 |
| 第三方企业应用 | 支持 |

## **事件体描述**

### header部分

### 字段说明

- `eventUnifiedAppId`（String，必填）：统一应用身份Id。
- `eventCorpId`（String）：事件所属的corpId。
- `eventType`（String）：事件类型。
- `eventId`（String）：事件的唯一Id。
- `eventBornTime`（Long）：事件生成时间。

### data部分(事件业务信息)

### 字段说明

- `authCorpInfo`（object）：授权方企业信息。
- `authCorpInfo.authChannel`（string）：渠道码。
- `authCorpInfo.corpid`（string）：授权企业的CorpId。
- `authCorpInfo.corpType`（integer）：企业类型。
- `authCorpInfo.fullCorpName`（string）：授权方企业名称。
- `authCorpInfo.corpTypeV2`（integer）：- 0 是普通组织  
  - 1 是项目  
  - 2 是圈子  
  - 3 没有业务表现形式  
  - 4 是自建班级群  
  - 10 是敏捷组织  
  - 11 是培训群敏捷组织
- `authCorpInfo.corpName`（string）：组织名称。
- `authCorpInfo.industry`（string）：行业类型。
- `authCorpInfo.isAuthenticated`（boolean）：企业是否认证：  
  - true：已经认证  
  - false：未认证
- `authCorpInfo.licenseCode`（string）：序列号。
- `authCorpInfo.corpLogoUrl`（string）：企业logo。
- `authCorpInfo.inviteUrl`（string）：企业邀请链接。
- `authCorpInfo.inviteCode`（string）：邀请码，只有自己邀请的企业才会返回邀请码，可用该邀请码统计不同渠道的拉新，否则值为空字符串。
- `authCorpInfo.isEcologicalCorp`（boolean）：是否为上下游组织  
  - true：是  
  - false： 否
- `authCorpInfo.authLevel`（integer）：企业认证等级：  
  - 0：未认证  
  - 1：高级认证  
  - 2：中级认证  
  - 3：初级认证
- `authCorpInfo.authChannelType`（string）：渠道类型。为了避免渠道码重复，可与渠道码共同确认渠道。可能为空，非空时当前只有满天星类型，值为STAR\_ACTIVITY。
- `permanentCode`（string）：permanentCode已经废弃。
- `authUserInfo`（object）：授权方管理员信息。
- `authUserInfo.userId`（string）：管理员的userId。
- `authScope`（object）：授权范围。
- `authScope.errcode`（integer）：返回码。
- `authScope.authUserField`（array，必填）：授权userfield。
- `authScope.authOrgScopes`（object）：授权范围信息。
- `authScope.authOrgScopes.authedDept`（array）：授权的部门。
- `authScope.errmsg`（string）：返回码说明。
- `authInfo`（object）：授权信息。
- `authInfo.agent`（array）：授权的应用信息。
- `authInfo.agent[].agentid`（long）：授权方应用ID。
- `authInfo.agent[].adminList`（array）：对此微应用有管理权限的管理员userid。
- `authInfo.agent[].appid`（long）：应用appid。
- `authInfo.agent[].agentName`（string）：授权方应用名字。
- `authInfo.agent[].logoUrl`（string）：授权方应用头像。

### **事件体数据示例如下:**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "org_suite_change",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "authCorpInfo": {
      "authChannel": "4",
      "corpid": "dingb2b068b57xxxxxx288",
      "corpType": 0,
      "fullCorpName": "测试组织",
      "corpTypeV2": 0,
      "corpName": "测试组织",
      "industry": "互联网",
      "isAuthenticated": false,
      "licenseCode": "",
      "corpLogoUrl": "https://static-legacy.dingtalk.com/xxx",
      "inviteUrl": "https://wx.dingtalk.com/invite-page/xxx",
      "inviteCode": "dada2xdaflgf",
      "isEcologicalCorp": false,
      "authLevel": 0,
      "authChannelType": "68QKuTAkgHRSMOyCxoYZyNXXXX"
    },
    "permanentCode": "68QKuTAkgHRSMOyCxoYZyNXXXX",
    "authUserInfo": {
      "userId": "managerxxx92"
    },
    "authScope": {
      "errcode": 0,
      "authUserField": [
        "jobnumber",
        "isLeader",
        "name",
        "position"
      ],
      "authOrgScopes": {
        "authedDept": [
          1
        ]
      },
      "errmsg": "ok"
    },
    "authInfo": {
      "agent": [
        {
          "agentid": 2574805120,
          "adminList": [
            "182937xxx",
            "0148564xxx93182"
          ],
          "appid": 131191,
          "agentName": "测试应用",
          "useAppRole": false,
          "logoUrl": "https://static-legacy.dingtalk.com/media/lADPDfmVQafoVxrMyMzI_200_200.jpg"
        }
      ]
    }
  }
}
```
