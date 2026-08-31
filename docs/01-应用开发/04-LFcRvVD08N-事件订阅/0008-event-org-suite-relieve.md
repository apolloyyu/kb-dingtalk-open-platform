---
title: "企业授权变更事件"
source_url: "https://open.dingtalk.com/document/development/event-org-suite-relieve"
namespace: "development"
slug: "event-org-suite-relieve"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "身份与免登 > 企业授权变更事件"
doc_id: "Jp8IHYvfwx"
updated_at: "2026-07-22 16:25:28"
---

> Source: https://open.dingtalk.com/document/development/event-org-suite-relieve
> Path: 应用开发 / 事件订阅 / 身份与免登 > 企业授权变更事件
> Updated: 2026-07-22 16:25:28

# 企业授权变更事件

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 企业授权变更事件 |
| 英文名称 | org\_suite\_change |

## 功能描述

数据为企业授权应用的最新状态，企业授权变更事件表示企业变更第三方企业应用的授权范围。其中auth\_corp\_info， auth\_info和auth\_user\_info三段结构信息请参考[获取企业授权信息](../02-4a8AMF6u2A-服务端-API/0042-obtains-the-basic-information-of-an-enterprise.md)。auth\_scope结构信息请参考[获取通讯录权限范围](../02-4a8AMF6u2A-服务端-API/0053-obtain-corpsecret-authorization-scope.md)。

## 支持应用类型

| 应用类型 | Stream模式推送 | HTTP推送 | SyncHTTP/RDS推送 |
| --- | --- | --- | --- |
| 第三方企业应用 | 支持 | 不支持 | 支持 |

## 事件体描述

Stream模式推送

### 字段说明

- `eventUnifiedAppId`（String，必填）：统一应用身份Id。
- `eventCorpId`（String）：事件所属的corpId。
- `eventType`（String）：事件类型。
- `eventId`（String）：事件的唯一Id。
- `eventBornTime`（Long）：事件生成时间。
- `data`（object）：事件体data。
- `data.authCorpInfo`（object）：授权方企业信息。
- `data.authCorpInfo.corpType`（integer）：企业类型。
- `data.authCorpInfo.corpTypeV2`（integer）：- 0 是普通组织  
  - 1 是项目  
  - 2 是圈子  
  - 3 没有业务表现形式  
  - 4 是自建班级群  
  - 10 是敏捷组织  
  - 11 是培训群敏捷组织
- `data.authCorpInfo.isAuthenticated`（boolean）：是否为上下游组织：  
  - true：是  
  - false：否
- `data.authCorpInfo.isEcologicalCorp`（boolean）：是否为上下游组织：  
  - true：是  
  - false： 否
- `data.authCorpInfo.authLevel`（integer）：企业认证等级：  
  - 0：未认证  
  - 1：高级认证  
  - 2：中级认证  
  - 3：初级认证
- `data.authCorpInfo.corpid`（string）：授权企业的corpid。
- `data.authCorpInfo.authChannel`（string）：渠道码。
- `data.authCorpInfo.industry`（string）：行业类型。
- `data.authCorpInfo.fullCorpName`（string）：授权方企业名称。
- `data.authCorpInfo.corpName`（string）：组织名称。
- `data.authCorpInfo.inviteUrl`（string）：企业邀请链接。
- `data.authCorpInfo.authChannelType`（string）：渠道类型。为了避免渠道码重复，可与渠道码共同确认渠道。可能为空，非空时当前只有满天星类型，值为STAR\_ACTIVITY。
- `data.authCorpInfo.inviteCode`（string）：邀请码，只有自己邀请的企业才会返回邀请码，可用该邀请码统计不同渠道的拉新，否则值为空字符串。
- `data.authCorpInfo.licenseCode`（string）：序列号。
- `data.authCorpInfo.corpLogoUrl`（string）：企业logo。
- `data.authScope`（object）
- `data.authScope.errcode`（integer，必填）：返回码。
- `data.authScope.authUserField`（array）：授权auth\_user\_field。
- `data.authScope.authOrgScopes`（object）：授权范围信息。
- `data.authScope.authOrgScopes.errmsg`（string，必填）：返回码说明。
- `data.authScope.authOrgScopes.authedDept`（array）：授权的部门。
- `data.permanentCode`（string）：permanent\_code已经废弃。
- `data.authUserInfo`（object）：授权方管理员信息。
- `data.authUserInfo.userId`（string）：管理员的userId。
- `data.authInfo`（object）：授权的应用信息。
- `data.authInfo.agent`（array）
- `data.authInfo.agent[].agentid`（long）：授权方应用ID。
- `data.authInfo.agent[].agentName`（string）：授权方应用名字。
- `data.authInfo.agent[].logoUrl`（string）：授权方应用头像。
- `data.authInfo.agent[].appid`（number）：应用appid。
- `data.authInfo.agent[].adminList`（array）：对此微应用有管理权限的管理员userid。

### **事件体示例**

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
      "corpTypeV2": 2,
      "industry": "互联网",
      "corpName": "测试组织",
      "isAuthenticated": true,
      "licenseCode": "xxx",
      "corpLogoUrl": "https://static-legacy.dingtalk.com/xxx",
      "inviteUrl": "https://wx.dingtalk.com/invite-page/xxx",
      "inviteCode": "dada2xdaflgf",
      "isEcologicalCorp": false,
      "authLevel": 2,
      "authChannelType": "STAR_ACTIVITY"
    },
    "permanentCode": "68QKuTAkgHRSMOyCxoYZyNXXXX",
    "authUserInfo": {
      "userId": "managerxxx92"
    },
    "authScope": {
      "errcode": 0,
      "authUserField": [
        "jobnumber"
      ],
      "authOrgScopes": {
        "errmsg": "ok",
        "authedDept": [
          1
        ]
      }
    },
    "authInfo": {
      "agent": [
        {
          "agentid": 2574805120,
          "adminList": [
            "182937xxx"
          ],
          "appid": "1000",
          "agentName": "测试应用",
          "logoUrl": "https://staticXXX.jpg"
        }
      ]
    }
  }
}
```

SyncHTTP/RDS推送

为RDS推送方式时，数据插入表open\_sync\_biz\_data中。

### root

- `corp_id`（String）：企业corp\_id。
- `biz_id`（String）：biz\_id无业务意义，幂等。
- `biz_type`（Integer）：事件bizType。
- `biz_data`（object）：事件bizData介绍。
- `biz_data.syncAction`（String）：事件英文名。
- `biz_data.eventId`（String）：事件的唯一Id。
- `biz_data.auth_corp_info`（object）：授权方企业信息。
- `biz_data.auth_corp_info.corp_type`（integer）：企业类型。
- `biz_data.auth_corp_info.auth_level`（integer）：企业认证等级：  
  - 0：未认证  
  - 1：高级认证  
  - 2：中级认证  
  - 3：初级认证
- `biz_data.auth_corp_info.is_ecological_corp`（boolean）：是否为上下游组织：  
  - true：是  
  - false： 否
- `biz_data.auth_corp_info.corp_type_v2`（integer）：- 0 是普通组织  
  - 1 是项目  
  - 2 是圈子  
  - 3 没有业务表现形式  
  - 4 是自建班级群  
  - 10 是敏捷组织  
  - 11 是培训群敏捷组织
- `biz_data.auth_corp_info.is_authenticated`（boolean）：是否为上下游组织：  
  - true：是  
  - false：否
- `biz_data.auth_corp_info.corpid`（string）：授权企业的corpid。
- `biz_data.auth_corp_info.auth_channel`（string）：渠道码。
- `biz_data.auth_corp_info.industry`（string）：行业类型。
- `biz_data.auth_corp_info.full_corp_name`（string）：授权方企业名称。
- `biz_data.auth_corp_info.corp_name`（string）：组织名称。
- `biz_data.auth_corp_info.invite_url`（string）：企业邀请链接。
- `biz_data.auth_corp_info.auth_channel_type`（string）：渠道类型。为了避免渠道码重复，可与渠道码共同确认渠道。可能为空，非空时当前只有满天星类型，值为STAR\_ACTIVITY。
- `biz_data.auth_corp_info.invite_code`（string）：邀请码，只有自己邀请的企业才会返回邀请码，可用该邀请码统计不同渠道的拉新，否则值为空字符串。
- `biz_data.auth_corp_info.license_code`（string）：序列号。
- `biz_data.auth_corp_info.corp_logo_url`（string）：企业logo。
- `biz_data.auth_scope`（object）
- `biz_data.auth_scope.errcode`（integer，必填）：返回码。
- `biz_data.auth_scope.auth_user_field`（array，必填）：授权auth\_user\_field。
- `biz_data.auth_scope.auth_org_scopes`（object，必填）：授权范围信息。
- `biz_data.auth_scope.auth_org_scopes.authed_dept`（array，必填）：授权的部门。
- `biz_data.auth_scope.auth_org_scopes.errmsg`（string，必填）：返回码说明。
- `biz_data.permanent_code`（string）：permanent\_code已经废弃。
- `biz_data.auth_user_info`（object）：授权方管理员信息。
- `biz_data.auth_user_info.userId`（string）：管理员的userId。
- `biz_data.auth_info`（object）：授权的应用信息。
- `biz_data.auth_info.agent`（array）
- `biz_data.auth_info.agent[].agentid`（long）：授权方应用ID。
- `biz_data.auth_info.agent[].agent_name`（string）：授权方应用名字。
- `biz_data.auth_info.agent[].logo_url`（string）：授权方应用头像。
- `biz_data.auth_info.agent[].appid`（number）：应用appid。
- `biz_data.auth_info.agent[].admin_list`（array）：对此微应用有管理权限的管理员userid。

### **biz\_data数据示例(biz\_type=4)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 4,
  "biz_data": {
    "auth_user_info": {
      "userId": "managerxxx92"
    },
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "auth_corp_info": {
      "corp_type": 0,
      "corpid": "dingb2b068b57xxxxxx288",
      "auth_level": 2,
      "auth_channel": "4",
      "industry": "互联网",
      "full_corp_name": "测试组织",
      "corp_name": "测试组织",
      "is_ecological_corp": false,
      "invite_url": "https://wx.dingtalk.com/invite-page/xxx",
      "auth_channel_type": "STAR_ACTIVITY",
      "invite_code": "dada2xdaflgf",
      "corp_type_v2": 2,
      "is_authenticated": true,
      "license_code": "xxx",
      "corp_logo_url": "https://static-legacy.dingtalk.com/xxx"
    },
    "syncAction": "org_suite_change",
    "auth_scope": {
      "errcode": 0,
      "auth_user_field": [
        "jobnumber"
      ],
      "auth_org_scopes": {
        "authed_dept": [
          1
        ],
        "errmsg": "ok"
      }
    },
    "auth_info": {
      "agent": [
        {
          "agentid": 2574805120,
          "agent_name": "测试应用",
          "logo_url": "https://staticXXX.jpg",
          "appid": "1000",
          "admin_list": [
            "182937xxx"
          ]
        }
      ]
    },
    "permanent_code": "68QKuTAkgHRSMOyCxoYZyNXXXX"
  }
}
```
