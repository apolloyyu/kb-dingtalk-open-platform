---
title: "企业授权第三方企业应用"
source_url: "https://open.dingtalk.com/document/development/enterprise-authorized-application-stream"
namespace: "development"
slug: "enterprise-authorized-application-stream"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "历史文档（不推荐） > Stream推送 > 授权事件 > 企业授权第三方企业应用"
doc_id: "A08OUOzFyM"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/enterprise-authorized-application-stream
> Path: 应用开发 / 事件订阅 / 历史文档（不推荐） > Stream推送 > 授权事件 > 企业授权第三方企业应用
> Updated: 2022-01-19 19:29:22

# 企业授权第三方企业应用

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 企业授权第三方企业应用 |
| 英文名称 | org\_suite\_auth |

## 功能描述

eventType为org\_suite\_auth，表示企业授权第三方企业应用。其中authCorpInfo, authInfo和authUserInfo三段结构信息请参考[获取企业授权信息](https://open.dingtalk.com/document/isvapp/obtains-the-basic-information-of-an-enterprise)。authScope结构信息清参考[获取通讯录权限范围](https://open.dingtalk.com/document/isvapp/obtain-corpsecret-authorization-scope)。

## 支持应用类型

| 应用类型 | 是否支持 |
| --- | --- |
| 企业内部应用 | 不支持 |
| 第三方企业应用 | 支持 |

## **事件体描述**

### header部分

### data部分(事件业务信息)

### **事件体数据示例如下:**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "org_suite_auth",
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
