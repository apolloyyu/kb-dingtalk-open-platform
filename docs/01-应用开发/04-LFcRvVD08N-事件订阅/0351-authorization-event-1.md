---
title: "授权事件"
source_url: "https://open.dingtalk.com/document/development/authorization-event-1"
namespace: "development"
slug: "authorization-event-1"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "历史文档（不推荐） > RDS推送/SyncHTTP推送 > 授权事件"
doc_id: "nY3mjKF65T"
updated_at: "2025-10-16 15:06:30"
---

> Source: https://open.dingtalk.com/document/development/authorization-event-1
> Path: 应用开发 / 事件订阅 / 历史文档（不推荐） > RDS推送/SyncHTTP推送 > 授权事件
> Updated: 2025-10-16 15:06:30

# 授权事件

本文介绍了授权的RDS和SyncHTTP推送的数据格式。

## 配置事件回调

第三方企业应用配置事件订阅流程，请参见[第三方企业应用事件与回调流程](https://open.dingtalk.com/document/isvapp/third-party-enterprise-application-address-book-change-event-subscription-process)。

## 授权数据表

| **主键（id）** | **订阅者ID（**subscribe\_id**）** | **企业ID（**corp\_id**）** | **业务ID（**biz\_id**）** | **业务类型（**biz\_type**）** | 说明 |
| --- | --- | --- | --- | --- | --- |
| 2 | xxxxx\_0 | corpxxxx | 716001 | 2 | 第三方企业应用的票据 |
| 4 | xxxxx\_0 | corpxxxx | 716001 | 4 | 企业授权变更，包含授权、解除授权、授权变更 |
| 7 | xxxxx\_0 | corpxxxx | 1318 | 7 | 第三方企业应用变更，包含停用、启用、删除（删除保留授权） |

## biz\_type=2

当biz\_type=2时，数据为第三方企业应用票据suiteTicket最新状态。

该数据为定时推送，插入表open\_sync\_biz\_data中。

| **字段** | **说明** |
| --- | --- |
| subscribe\_id | 第三方企业应用的suiteid加下划线0。 |
| corp\_id | 第三方企业应用的corpid。 |
| biz\_id | 第三方企业应用的suiteid。 |
| biz\_data | 数据为Json格式。 |

biz\_data数据如下所示：

```
{
    "syncAction":"suite_ticket",
    "suiteTicket":"QsfJCEVF1h6E9fAaGwnAzbvYzxxxxxxxx"
}
```

## biz\_type=4

当biz\_type=4时，数据为企业授权应用的最新状态。

该数据为企业授权第三方企业应用、解除第三方企业应用授权、变更第三方企业应用的授权范围时刻推送，插入表open\_sync\_biz\_data中。

| **字段** | **说明** |
| --- | --- |
| subscribe\_id | 第三方企业应用的suiteid加下划线0。 |
| corp\_id | 开通第三方企业应用的企业corpid。 |
| biz\_id | 第三方企业应用的suiteid。 |
| biz\_data | 数据为Json格式。 |

biz\_data数据如下：

```
{
    "syncAction": "org_suite_auth",
    "auth_corp_info": {
      	"corp_type_v2":0,    //0是普通组织；1是项目；2是圈子；3没有业务表现形式；4是自建班级群；10是敏捷组织；11是培训群敏捷组织
        "is_ecological_corp": "false",  //是否为上下游组织  true是； false否
        "auth_channel": "",
        "auth_channel_type": "",
        "auth_level": 1,
        "corp_logo_url": "http://url.com",
        "corp_name": "浩倡测试企业申请认证",
        "corpid": "dingxxxxxxxxxxxxxx",
        "industry": "信息技术咨询",
        "invite_code": "000000",
        "invite_url": "http://url.com",
        "is_authenticated": true,
        "license_code": "xxx"
    },
    "auth_info": {
        "agent": [{
            "admin_list": ["aaaa", "bbbb"],
            "agent_name": "Demo",
            "agentid": 16000,
            "appid": 1234,
            "logo_url": "http://url.png"
        }]
    },
    "auth_user_info": {
        "userId": "xxxx"
    },
    "auth_scope": {
        "errcode": 0,
        "condition_field": [],
        "auth_user_field": ["position", "jobnumber", "avatar", "deviceId"],
        "auth_org_scopes": {
            "authed_user": [],
            "authed_dept": [1]
        },
        "errmsg": "ok"
    },
    "permanent_code": "xxxxxxxxxxxxx",
    "ch_permanent_code": "xxxxxxxxxxxxxx"
}
```

其中：

- syncAction字段的取值如下：

  - org\_suite\_auth：表示企业授权的第三方企业应用
  - org\_suite\_change：表示企业变更授权范围
  - org\_suite\_relieve：表示企业解除授权
  > **[!NOTE]**
  >
  > **org\_suite\_auth**，**org\_suite\_change**两个事件都表示企业对于第三方企业应用的授权信息，需要等同处理，在很短时间内发生的两个事件，有可能会覆盖，保证只给出最新的授权信息
- auth\_corp\_info, auth\_info和auth\_user\_info 三段结构信息请参考[获取企业授权信息](https://open.dingtalk.com/document/isvapp/obtains-the-basic-information-of-an-enterprise)。
- auth\_scope结构信息请参考[获取通讯录权限范围](https://open.dingtalk.com/document/isvapp/obtain-corpsecret-authorization-scope)。
- permanent\_code已废弃。兼容老接口[获取第三方应用授权企业的accessToken](https://open.dingtalk.com/document/isvapp/obtain-the-access_token-of-the-authorized-enterprise)。
- ch\_permanent\_code已废弃。兼容老接口service/get\_channel\_corp\_token。

## biz\_type=7

当biz\_type=7时，数据为第三方企业应用的最新状态。

该数据为企业停用、启动第三方企业应用的时刻推送，插入表open\_sync\_biz\_data中。

| **字段** | **说明** |
| --- | --- |
| subscribe\_id | 第三方企业应用的suiteid加下划线0。 |
| corp\_id | 开通第三方企业应用的企业corpid。 |
| biz\_id | 第三方企业应用的appid。 |
| biz\_data | 数据为Json格式。 |

biz\_data数据如下：

其中，syncAction字段的取值如下：

- org\_micro\_app\_restore：第三方企业应用启用

  ```
  {
      "agentId":12345677,
      "syncAction":"org_micro_app_restore"
  }
  ```
- org\_micro\_app\_stop：第三方企业应用停用

  ```
  {
      "agentId":12345677,
      "syncAction":"org_micro_app_stop"
  }
  ```
- org\_micro\_app\_remove：第三方企业应用删除，保留企业对第三方企业应用的授权

  ```
  {
      "agentId":12345677,
      "syncAction":"org_micro_app_remove"
  }
  ```
- org\_micro\_app\_scope\_update： 第三方企业应用可见范围变更

  ```
  {
      "agentId":12345677,
      "syncAction":"org_micro_app_scope_update"
  }
  ```
