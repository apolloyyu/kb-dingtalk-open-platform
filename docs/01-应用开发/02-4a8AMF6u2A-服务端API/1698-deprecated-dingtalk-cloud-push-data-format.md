---
title: "钉钉云推送数据格式"
source_url: "https://open.dingtalk.com/document/development/deprecated-dingtalk-cloud-push-data-format"
namespace: "development"
slug: "deprecated-dingtalk-cloud-push-data-format"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 钉钉云 > 钉钉云数据推送 > 钉钉云数据推送格式 > 钉钉云推送数据格式"
doc_id: "dV0tEKvY7X"
updated_at: "2025-12-09 12:04:34"
---

> Source: https://open.dingtalk.com/document/development/deprecated-dingtalk-cloud-push-data-format
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 钉钉云 > 钉钉云数据推送 > 钉钉云数据推送格式 > 钉钉云推送数据格式
> Updated: 2025-12-09 12:04:34

# 钉钉云推送数据格式

本文档详细说明钉钉云推送至开发者RDS实例的数据格式与处理逻辑，适用于ISV接收并解析钉钉侧推送的各类业务变更事件。

## 钉钉云推送数据表说明

钉钉云推送插入的数据库表创建请参考设置RDS实例接收钉钉推送。

| **主键（id）** | **订阅者ID（**subscribe\_id**）** | **企业ID（**corp\_id**）** | **业务ID（**biz\_id**）** | **业务类型（**biz\_type**）** | 说明 |
| --- | --- | --- | --- | --- | --- |
| 2 | xxxxx\_0 | corpxxxx | 716001 | 2 | 套件票据 |
| 4 | xxxxx\_0 | corpxxxx | 716001 | 4 | 企业授权变更，包含授权、解除授权、授权变更。 |
| 7 | xxxxx\_0 | corpxxxx | 1318 | 7 | 企业微应用变更，包含停用、启用、删除(删除保留授权) |
| 13 | xxxxx\_0 | corpxxxx | user123 | 13 | 企业用户变更，包含用户添加、修改、删除 |
| 14 | xxxxx\_0 | corpxxxx | dept123 | 14 | 企业部门变更，包含部门添加、修改、删除 |
| 15 | xxxxx\_0 | corpxxxx | role123 | 15 | 企业角色变更，包含角色添加、修改、删除 |
| 16 | xxxxx\_0 | corpxxxx | corpxxxx | 16 | 企业变更，包含企业修改、删除 |
| 17 | xxxxx\_0 | corpxxxx | orderidxx | 17 | 市场订单 |
| 20 | xxxxx\_0 | corpxxxx | user123 | 20 | 企业外部联系人变更，包含添加、修改、删除 |
| 22 | xxxxx\_0 | corpxxxx | ef-sss-sv | 22 | ISV自定义审批 |
| 25 | xxxxx\_0 | corpxxxx | userid或者deptid | 25 | 家校通讯录1.0(Deprecated)信息变更。家校通讯录升级，请查看[家校通讯录2.0数据推送](https://open.dingtalk.com/document/isvapp/home-school-address-book-2-0-data-push) |
| 32 | xxxxx\_0 | corpxxxx | 绑定： active+设备id  解绑： delete+设备id | 32 | 智能硬件绑定类型 |
| 37 | xxxxx\_0 | corpxxxx | orderidxx | 37 | 因订单到期或者用户退款等导致的服务关闭，目前仅推送因退款等导致的服务关闭 |
| 50 | xxxxx\_0 | corpxxxx | 无具体业务含义，只与其他属性构成唯一索引。  拼接规则：  人员关系事件： u\_r\_${id}\_${action}  监护人身份事件：g\_${id}\_${action}  学生身份事件： s\_${id}\_${action}  老师身份事件： t\_${id}\_${action}  示例：g\_1233\_insert | 50 | 家校通讯录2.0，部门信息变更 |
| 51 | xxxxx\_0 | corpxxxx | 无业务含义，只是与其他字段组成唯一索引。  拼接规则：d\_${id}\_${action} | 51 | 家校通讯录2.0，人员信息变更 |
| 63 | xxxxx\_0 | corpxxxx | 试用人的unionid | 63 | 应用试用记录回调信息 |

## 钉钉云数据推送插入表逻辑

推送数据采用“删除旧记录 + 插入新记录”的方式更新，保障数据最终一致性。

- 同一个订阅者（`subscribe\_id`）对某企业（`corp\_id`）下的某一类业务（`biz\_type`）中的特定对象（`biz\_id`），最多只存在一条有效记录。
- 当该对象发生变更时，系统会先删除原记录，再插入最新状态记录。
- 所有推送记录以 `(subscribe\_id, corp\_id, biz\_id, biz\_type)` 构成唯一索引。

## biz\_type=2

当 `biz\_type = 2` 时，表示推送最新的套件票据（suiteTicket），定时触发，插入表 `open\_sync\_biz\_data`。

| **字段** | **说明** |
| --- | --- |
| subscribe\_id | 套件suiteId + "\_0"，如 suite\_0。 |
| corp\_id | 套件所属企业的corpid。 |
| biz\_id | 套件suiteId。 |
| biz\_data | JSON格式数据。 |

biz\_data数据如下所示：

```
{
    "syncAction":"suite_ticket",
    "suiteTicket":"QsfJCEVF1h6E9fAaGwnAzbvYzxxxxxxxx"
}
```

## biz\_type=4

当 biz\_type = 4 时，表示企业对套件的授权的微应用状态发生变化（首次授权、授权变更、解除授权），插入表 open\_sync\_biz\_data。

| **字段** | **说明** |
| --- | --- |
| subscribe\_id | 套件suiteId + "\_0"。 |
| corp\_id | 开通套件微应用的企业corpid。 |
| biz\_id | 套件suiteId。 |
| biz\_data | JSON格式数据。 |

biz\_data数据如下：

```
{
    "syncAction": "org_suite_auth",
    "auth_corp_info": {
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

### **syncAction 字段取值说明**

| **syncAction字段值** | **含义** |
| --- | --- |
| org\_suite\_auth | 企业授权套件。 |
| org\_suite\_change | 企业变更授权范围。 |
| org\_suite\_relieve | 企业解除授权。 |

> **[!NOTE]**
>
> - auth\_corp\_info、auth\_info和auth\_user\_info 三段结构信息请参考[获取企业授权信息](https://open.dingtalk.com/document/isvapp/obtains-the-basic-information-of-an-enterprise)。
> - auth\_scope结构信息请参考[获取通讯录权限范围](https://open.dingtalk.com/document/isvapp/obtain-corpsecret-authorization-scope)。
> - permanent\_code和ch\_permanent\_code已废弃，请勿使用。

## biz\_type=7

当 `biz\_type = 7` 时，表示企业微应用状态变更（启用、停用、删除等），插入表 `open\_sync\_biz\_data`。

| **字段** | **说明** |
| --- | --- |
| subscribe\_id | 套件suiteId + "\_0"。 |
| corp\_id | 开通套件微应用的企业corpid。 |
| biz\_id | 微应用的appid。 |
| biz\_data | JSON格式数据。 |

### **biz\_data 示例**

biz\_data数据如下：

```
{
    "agentId":12345677,
    "syncAction":"org_micro_app_restore"
}
```

### **syncAction 字段取值说明**

| **syncAction字段值** | **含义** |
| --- | --- |
| org\_micro\_app\_restore | 微应用启用。 |
| org\_micro\_app\_stop | 微应用停用。 |
| org\_micro\_app\_remove | 微应用删除，保留企业对套件的授权。 |
| org\_micro\_app\_scope\_update | 微应用可见范围变更。 |

## biz\_type=13

当 `biz\_type = 13` 时，表示企业员工信息变更（增删改），插入表 `open\_sync\_biz\_data\_medium`。

| **字段** | **说明** |
| --- | --- |
| subscribe\_id | 套件suiteId + "\_0"。 |
| corp\_id | 开通套件微应用的企业corpid。 |
| biz\_id | 员工的userid。 |
| biz\_data | JSON格式数据。 |

### **biz\_data 示例**

数据为如下两种Json格式，企业增加或修改员工，字段值来自于[查询用户详情](https://open.dingtalk.com/document/isvapp/query-user-details)接口 。

#### **增加企业员工**

```
{
    "errcode": 0,
    "unionid": "m8axYHBIiSxxxx",
    "syncAction": "user_modify_org",
    "openId": "kiPw6f4Awmxxxx",
    "roles": [{
        "id": 289179322,
        "name": "角色01",
        "groupName": "职务01",
        "type": 0
    }],
    "userid": "1234567",
    "isCustomizedPortal": true,
    "isLeaderInDepts": "{1234567:false}",
    "isBoss": false,
    "isSenior": false,
    "department": [1234567],
    "email": "",
    "orderInDepts": "{1234567:23422}",
    "mobile": "186xxxxxxxx",
    "errmsg": "ok",
    "active": true,
    "avatar": "http://static.dingtalk.com/media/lADOD3zI380B080B0w_467_467.jpg",
    "isAdmin": false,
    "isHide": false,
    "jobnumber": "90010100999",
    "name": "暖心",
    "stateCode": "86",
    "position": "1111"
}
```

#### **企业删除员工**

> **[!NOTE]**
>
> 删除事件中不携带用户详情，`userid` 需从 `biz\_id` 中获取。

```
{
    "syncAction":"user_leave_org"
    // 删除员工userid从biz_id中获取
}
```

### **syncAction 字段取值说明**

| **syncAction字段值** | **含义** |
| --- | --- |
| user\_add\_org | 企业增加员工事件后的员工信息。 |
| user\_modify\_org | 企业修改员工事件后的员工信息。 |
| user\_dept\_change | 企业修改员工所在部门事件后的员工信息。 |
| user\_role\_change | 企业修改员工所在角色(包括管理员变更)事件后的员工信息。 |
| user\_active\_org | 用户加入企业后的激活信息，active字段为true时表示已激活。 |
| user\_leave\_org | 企业删除员工事件后的员工信息。 |

## biz\_type=14

当 `biz\_type = 14` 时，表示企业部门信息变更，在授权微应用的企业，发生部门的增加、删除、修改的时刻推送，插入表 `open\_sync\_biz\_data\_medium`。

当biz\_type=14时，数据为企业部门的最新状态。

| **字段** | **说明** |
| --- | --- |
| subscribe\_id | 套件suiteId + "\_0"。 |
| corp\_id | 开通套件微应用的企业corpid。 |
| biz\_id | 部门ID。 |
| biz\_data | JSON格式数据。 |

### **biz\_data 示例**

数据为如下两种Json格式，企业增加或修改部门和企业删除部门，字段值来自[获取部门详情](https://open.dingtalk.com/document/isvapp/query-department-details0-v2)接口 。

#### **企业增加/修改部门**

```
{
    "errcode": 0,
    "userPerimits": "",
    "syncAction": "org_dept_create/org_dept_modify",
    "orgDeptOwner": "0541092856786053",
    "outerDept": false,
    "errmsg": "ok",
    "deptManagerUseridList": "",
    "parentid": 60398183,
    "groupContainSubDept": false,
    "outerPermitUsers": "",
    "outerPermitDepts": "",
    "deptPerimits": "",
    "createDeptGroup": true,
    "name": "部门02",
    "id": 60397224,
    "autoAddUser": true,
    "deptHiding": false,
    "order": 60397224
}
```

#### **企业删除部门**

```
{
    "syncAction":"org_dept_remove"
}
```

### **syncAction 字段取值说明**

| **syncAction字段值** | **含义** |
| --- | --- |
| org\_dept\_create | 创建部门。 |
| org\_dept\_modify | 修改部门。 |
| org\_dept\_remove | 删除部门。 |

## biz\_type=15

当 `biz\_type = 15` 时，表示企业角色信息变更，授权微应用的企业中，发生角色的增加、删除、修改的时刻推送，插入表 `open\_sync\_biz\_data\_medium`。

| **字段** | **说明** |
| --- | --- |
| subscribe\_id | 套件suiteId + "\_0"。 |
| corp\_id | 开通套件微应用的企业corpid。 |
| biz\_id | 角色ID。 |
| biz\_data | JSON格式数据。 |

### **biz\_data 示例**

数据为如下两种Json格式：

#### **企业增加/修改角色**

```
{
    "role_name": "角色01",
    "role_id": 12345,
    "group_id": 1,
    "group_name": "默认角色组",
    "syncAction": "org_role_add"
}
```

#### **企业删除角色**

```
{
    "syncAction":"org_role_remove"
}
```

#### **syncAction 字段取值说明**

| **syncAction字段值** | **含义** |
| --- | --- |
| org\_role\_add | 企业增加角色事件之后的角色信息。 |
| org\_role\_remove | 企业修改角色事件之后的角色信息。 |

## biz\_type=16

当 `biz\_type = 16` 时，表示在授权微应用的企业中，企业自身信息发生变更或被删除，插入表 `open\_sync\_biz\_data\_medium`。

| **字段** | **说明** |
| --- | --- |
| subscribe\_id | 套件suiteId + "\_0"。 |
| corp\_id | 开通套件微应用的企业corpid。 |
| biz\_id | 企业的corpid。 |
| biz\_data | JSON格式数据。 |

### **biz\_data 示例**

数据为如下两种 Json格式：

### **企业变更**

```
{
    "errcode": 0,
    "corpid": "dingxxxxxxxxxxxxxx",
    "auth_level": 1,
    "syncAction": "org_update",
    "errmsg": "ok",
    "industry": "信息技术咨询",
    "is_authenticated": true,
    "corp_name": "XX企业",
    "corp_logo_url": "http://static.dingtalk.com/media/lALPBY0V4xtagzFgYA_96_96.png"
}
```

### **企业删除**

```
{
    "syncAction": "org_remove"
}
```

## biz\_type=17

当 `biz\_type = 17` 时，表示企业在服务市场购买商品产生订单时刻推送，插入表 `open\_sync\_biz\_data`。

| **字段** | **说明** |
| --- | --- |
| subscribe\_id | 套件suiteId + "\_0"。 |
| corp\_id | 开通套件微应用的企业corpid。 |
| biz\_id | 订单的orderid。 |
| biz\_data | JSON格式数据。 |

### **biz\_data 示例**

数据如下：

```
{
    "orderId": "312139204444444",
    "suiteId": 123123,
    "suiteKey": "xxxxxxxxx",
    "goodsName": "测试商品",
    "goodsCode": "xxxxxxxxxxx",
    "itemName": "测试规格",
    "itemCode": "xxxxxxx",
    "corpId": "dingxxxxxxxxxxxx",
    "maxOfPeople": 100,
    "minOfPeople": 0,
    "paidtime": 1524897069000,
    "serviceStopTime": 1524897069000,
    "payFee": 1000,
    "orderCreatSource": "xxxx",
    "distributorCorpName": "测试代理企业",
    "distributorCorpId": "dingxxxxxxxxxxxxx",
    "nominalPayFee": 1000,
    "discountFee": 0,
    "discount": 1,
    "subQuantity": 1,
    "serviceStartTime": 168000312000,
    "orderType": "RENEW",
    "unionId": "union1265341625"
}
```

字段说明：

| 字段 | 说明 |
| --- | --- |
| orderId | 订单ID。 |
| syncAction | 该订单对应的用户操作。  当syncAction为market\_order时，表示市场订单支付。 |
| suiteId | 用户购买套件的suiteId。 |
| suiteKey | 用户购买套件的suiteKey。 |
| goodsName | 商品名称。 |
| goodsCode | 商品码。 |
| itemName | 规格名称。 |
| itemCode | 规格码。 |
| subQuantity | 购买数量。 |
| maxOfPeople | 规格支持最大使用人数。 |
| minOfPeople | 规格支持最小使用人数。 |
| corpId | 购买企业的corpId。 |
| distributorCorpName | 分销商企业名称。 |
| distributorCorpId | 分销商企业corpId。 |
| paidtime | 支付时间（单位：毫秒）。 |
| serviceStopTime | 服务结束时间（单位：毫秒）。 |
| orderCreatSource | 订单来源：   - 默认订单来自应用中心。 - 若值为DRP，表示来自DRP分销平台。 |
| payFee | 实际支付价格（单位：分）。 |
| nominalPayFee | 名义票面费用（单位：分），现与payFee值相等 |
| discountFee | 折扣减免费用（单位：分），现值为0。 |
| discount | 折扣，现值为1.00。 |
| serviceStartTime | 服务开始时间（单位：毫秒）。 |
| orderType | 订单类型，取值：   - **BUY**：新购 - **RENEW**：续费 - **UPGRADE**：升级 - **RENEW\_UPGRADE**：续费升配 - **RENEW\_DEGRADE**：续费降配 |
| unionId | 下单人unionId。 |

## biz\_type=20

当 `biz\_type = 20` 时，表示在授权微应用的企业中，企业发生外部联系人的增加、删除、修改，插入表 `open\_sync\_biz\_data\_medium`。

| **字段** | **说明** |
| --- | --- |
| subscribe\_id | 套件suiteId + "\_0"。 |
| corp\_id | 开通套件微应用的企业corpid。 |
| biz\_id | 外部联系人的userId。 |
| biz\_data | JSON格式数据。 |

### **biz\_data示例**

数据为如下两种 Json格式：

#### **企业增加/修改外部联系人**

```
{
    "errcode": 0,
    "shareUserIds": [],
    "syncAction": "contact_modify_org",
    "mobile": "186xxx11111",
    "errmsg": "ok",
    "remark": "",
    "title": "",
    "userId": "2012130422-811754543",
    "shareDeptIds": [62039002],
    "labelIds": [83029],
    "followerUserId": "2000121002668",
    "name": "潜在客户小张",
    "stateCode": "86"
}
```

#### **企业删除外部联系人**

```
{"syncAction":"contact_leave_org"}
```

#### **syncAction 字段取值说明**

| **syncAction字段值** | **含义** |
| --- | --- |
| contact\_add\_org | 企业增加外部联系人事件之后的联系人信息。 |
| contact\_modify\_org | 企业修改外部联系人事件之后的联系人信息。 |
| contact\_leave\_org | 企业删除外部联系人事件之后的联系人信息。 |

## biz\_type=22

当 `biz\_type = 22` 时，表示在授权微应用的企业中，当由ISV通过接口发起的审批出现变更的，插入表 `open\_sync\_biz\_data\_medium`。

| **字段** | **说明** |
| --- | --- |
| subscribe\_id | 套件suiteId + "\_0"。 |
| corp\_id | 开通套件微应用的企业corpid。 |
| biz\_id | 审批实例ID。 |
| biz\_data | JSON格式数据。 |

### **biz\_data示例**

数据如下：

> **[!NOTE]**
>
> 字段说明，请参考[获取单个审批实例详情](https://open.dingtalk.com/document/isvapp/obtains-the-details-of-a-single-approval-instance)。

```
{
    "orderId": "312139204444444",
    "suiteId": 123123xxx,
    "suiteKey": "xxxxxxxxx",
    "goodsName": "测试商品",
    "goodsCode": "xxxxxxxxxxx",
    "itemName": "测试规格",
    "itemCode": "xxxxxxx",
    "corpId": "dingxxxxxxxxxxxx",
    "maxOfPeople": 100,
    "minOfPeople": 0,
    "paidtime": 1524897069000,
    "serviceStopTime": 1524897069000,
    "payFee": 1000,
    "orderCreatSource": "xxxx",
    "distributorCorpName": "测试代理企业",
    "distributorCorpId": "dingxxxxxxxxxxxxx",
    "nominalPayFee": 1000,
    "discountFee": 0,
    "discount": 1.00,
    "subQuantity": 1
}
```

#### **syncAction 字段取值说明**

| **syncAction字段值** | **含义** |
| --- | --- |
| isv\_bpms | 一条审批记录的创建或者流程更新。 |
| isv\_bpms\_cancel | 一条审批记录撤销（字段保留待开发） |

## biz\_type=32

当 `biz\_type = 32` 时，表示企业发生硬件设备绑定变更，插入表 `open\_sync\_biz\_data`。

| **字段** | **说明** |
| --- | --- |
| subscribe\_id | 套件suiteId + "\_0"。 |
| corp\_id | 开通套件微应用的企业corpid。 |
| biz\_id | 绑定： active + 设备id  解绑： delete + 设备id |
| biz\_type | 32，为固定值，标识是智能硬件绑定类型消息。 |
| biz\_data | JSON格式数据。 |

### **biz\_data示例**

#### **绑定事件**

```
{
  "actionType": "bind",
  "corpId": "yourcorpid",
  "syncAction": "device_bind_update",
  "sn": "设备sn",
  "pk": "产品编码",
  "nodeType": 0,
  "deviceId": 设备id
}
```

#### **解绑事件**

```
{
  "actionType": "unbind",
  "corpId": "yourcorpid",
  "syncAction": "device_bind_update",
  "sn": "设备sn",
  "pk": "产品编码",
  "nodeType": 0,
  "deviceId": 设备id
}
```

#### **字段说明**

| 参数 | 数据类型 | 说明 |
| --- | --- | --- |
| actionType | String | - bind：绑定 - unbind：解绑 |
| corpId | String | 企业的corpid。 |
| syncAction | String | 数据类型。 |
| sn | String | 设备序列号。 |
| pk | String | productKey，产品类型编码。 |
| nodeType | Integer | 节点类型：   - 0： 节点 - 1：网关 |
| deviceId | Long | 设备ID。 |
| eventTimestamp | Long | 设备变化的时间戳。 |
| outBindStatus | String | 外部的绑定状态， ok 表示成功，其他表示失败 |

## biz\_type=37

当 `biz\_type = 37` 时，表示企业在钉钉服务市场购买开通应用产生订单，插入表 `open\_sync\_biz\_data`。

| **字段** | **说明** |
| --- | --- |
| subscribe\_id | 套件suiteId + "\_0"。 |
| corp\_id | 开通套件微应用的企业corpid。 |
| biz\_id | 订单ID。 |
| biz\_data | JSON格式数据。 |

### **biz\_data示例**

数据如下：

```
 {
    "suiteId": 123,
    "corpId": "ding6121",
    "orderId": 500******005,
    "itemCode": "FW_GOODS-1***281-4",
    "eventType": "subscription_close",
    "mainGoodsName": "测试商品",
    "closeType": 3,
    "pushType": 0,
    "itemName": "3",
    "payFee": 121.0,
    "mainGoodsCode": "FW_GOODS-1***20281",
    "suiteKey": "suitew****bvi3euo",
    "goodsCode": "FW_GOODS-1***0281",
    "refundId": "2088",
    "serviceStartTime": 167000031311,
    "serviceStopTime": 168000031311,
    "openType":3
}
```

#### **字段说明**

| 字段 | 说明 |
| --- | --- |
| orderId | 订单ID。 |
| syncAction | 该订单对应的用户操作。  syncAction为market\_service\_close表示因订单到期或者用户退款等导致的服务关闭。  **[!IMPORTANT]**  目前仅推送因退款导致的服务关闭。 |
| suiteId | 用户购买套件的suiteId。 |
| suiteKey | 用户购买套件的suiteKey。 |
| goodsName | 商品名称。 |
| goodsCode | 商品码。 |
| itemName | 规格名称。 |
| itemCode | 规格码。 |
| subQuantity | 购买数量。 |
| corpId | 购买企业的corpId。 |
| payFee | 实际支付价格（单位：分）。 |
| refundId | 退款单id，退款唯一标识。 |
| closeType | 关闭类型：   - 1：升级关闭 - 2：到期关闭 - 3：退款关闭 - 4：其他关闭  **[!IMPORTANT]**  目前仅推送**3**退款关闭。 |
| serviceStartTime | 订购服务开始时间（单位：毫秒）。 |
| serviceStopTime | 订购服务结束时间（单位：毫秒）。 |
| openType | 开通类型。  **[!NOTE]**  目前针对订购开通的消息只推送开通类型为 “**续费变配开通**”，取值为：**3**。 |

## biz\_type=63

当 `biz\_type =63` 时，表示当组织或个人应用试用开通时推送，插入表 `open\_sync\_biz\_data`。

应用商品新增个人试用后，增加了应用的触达率，为了方便ISV对客户进行后续跟踪和推广，组织/个人在应用试用后，钉钉后台新增了应用试用记录的回调信息。

目前试用的回调信息有两种：

1. 试用开通的订单信息

   试用开通的订单信息，侧重于订单信息回调。
2. 试用开通记录信息

   试用开通记录回调信息中不一定会有试用订单。

> **[!IMPORTANT]**
>
> 当同组织的两个用户对同一商品的试用时间完全重合，或者同组织下已经开通该商品试用的有效期完全包含新开通试用的有效期的时候，不会产生订单。

| **字段** | **说明** |
| --- | --- |
| subscribe\_id | 套件suiteId + "\_0"。 |
| corp\_id | 开通套件微应用的企业corpid。 |
| biz\_id | 试用人的unionid。 |
| biz\_type | 63，为固定值，标识应用试用开通记录的回调信息。 |
| biz\_data | 开通记录数据，JSON格式。 |

### **biz\_data示例**

数据如下：

```
{
    "buyerUnionId":"mLyKVGiiwEXQ5mT0Nwxxxx",
    "suiteId":698002,
    "corpId":"dingd678857e4250521135c2f465xxxx",
    "fromDate":"2020-12-04 10:59:25",
    "endDate":"2020-12-19 10:59:25",
    "EventType":"goods_tryout",
    "appId":1948,
    "tryoutType":"enterprise_tryout",
    "goodsCode":"FW_GOODS-100030xxxx",
    "TimeStamp":"1607050765623"
}
```

#### **字段说明**

| **字段** | **说明** |
| --- | --- |
| buyerUnionId | 系统生成，固定值不会改变，可用来识别下单人。 |
| corp\_id | 开通套件微应用的企业corpid。 |
| suiteId | 套件ID。 |
| fromDate | 试用开始时间。 |
| endDate | 试用结束时间。 |
| appId | 应用ID。 |
| tryoutType | 试用类型   - personal\_tryout：个人试用 - enterprise\_tryout：企业试用（管理员） |
| goodsCode | 商品码。 |
| TimeStamp | 时间戳。 |
| EventType | 事件类型。 |

## biz\_type=67

当 `biz\_type =67` 时，表示企业发生假期相关的数据变更，插入表 `open\_sync\_biz\_data`。

| **字段** | **说明** |
| --- | --- |
| subscribe\_id | 套件suiteId + "\_0"。 |
| corp\_id | 开通套件微应用的企业corpId。 |
| biz\_id | 加班转调休事件：`${无业务含义的id}:${userId}:${workDate}`，workDate的格式为yyyyMMdd，如20210312。 |
| biz\_type | 67，为固定值，标识该消息为钉钉假期相关数据。 |
| biz\_data | JSON格式数据。 |

### **biz\_data示例**

数据格式如下：

#### **加班转调休假事件（新增、更新时会触发同步）**

> **[!NOTE]**
>
> 数据业务唯一性约束为 ${corpId}+${userId}+${workDate}，同一个员工一天内可能会触发多次数据同步，但是应以当天最后一次同步的数据为准（例如：重排班、修改加班申请、加班转调休规则修改等，均会触发重算逻辑，导致之前同一天已同步的数据失效）。
>
> **即**：一个员工一天只会有一条有效的加班转调休记录，不会存在2条。

```
{
    "syncAction": "overtime_to_vacation_data",
    "corpId": "ding33f33xxxx",
    "userId": "33506665005555",
    "workDate": "20210311",
    "overtimeDayType": "restDay",
    "overtimeDay": 0.262,
    "overtimeHour": 2.1,
    "workHoursPerDay": 8,
    "vacationRate": 2,
    "leaveCode": "c1f772d2-xxxx-407e-816a-55be5c245569",
    "startTime": 1615392000000,
    "endTime": 1640966399000,
    "delayEndTime": 1640966399000
}
```

#### **字段说明**

| 参数 | 数据类型 | 说明 |
| --- | --- | --- |
| syncAction | String | overtime\_to\_vacation\_data：加班转调休事件 |
| corpId | String | 企业的corpid。 |
| userId | String | 对应的员工id。 |
| workDate | String | 对应的工作日，格式yyyyMMdd，如：20210312。 |
| overtimeDayType | String | 加班类型：   - workDay：工作日加班转调休 - restDay：休息日加班转调休 - holiday：节假日加班转调休 |
| overtimeDay | Number | 加班转调休时长（以天为单位），例如：0.262。 |
| overtimeHour | Number | 加班转调休时长（以小时为单位），例如：2.1。  与overtimeDay的换算关系：overtimeDay=overtimeHour/workHoursPerDay |
| workHoursPerDay | Number | 一天的工作时长（单位：小时）。 |
| vacationRate | Number | 加班转调休的比例，即 实际工作时长\*vacationRate=调休时长。 |
| leaveCode | String | 转成的调休假，对应的假期code。 |
| startTime | Long | 该假期的开始生效时间（unix时间戳）。 |
| endTime | Long | 该假期的失效时间（unix时间戳）。 |
| delayEndTime | Long | 假期的延迟失效时间（unix时间戳）。  startTime < endTime <= delayEndTime |

## 钉钉推送数据处理伪代码

- 处理推送数据的逻辑

  ```
  /**
   * @param subscribeId 订阅者ID。格式为套件ID加下划线0。例如12345_0
   */
  processMsgInbox(subscribeId):
      //加锁。对每个订阅者加锁。保证每个订阅者的收件箱同一时刻是有一个线程在处理。
      //如果开发者有多台机器,并发处理数据造成数据被并发重复处理。
      lock = tryLock(subscribeId)

      //如果获取锁失败,表示有其他线程在处理收件箱。返回
      //加锁是为了有多台机器或者多个线程同时处理收件箱任务的时候,发生并发问题。
      if !lock
          return

      //拉取待处理的收件箱数据列表
      list msgList = getMsgList(subscribeId,subscribeCursor )

      //循环处理每条消息数据,处理完之后更新每条数据的处理状态
      //自己定义。0为未处理状态。1为处理完成状态。2为处理失败状态。
      //如果有重试策略,可定义status状态为2,3,4,5表示重试过得次数。当重试次数大于5次不再重试
      //此处要有监控报警。当发现处理失败或者未处理的数据堆积，要报警
      for msg: msgList
          processStatus = processMsg(msg)
          updateMsgStatus(msg.getId,processStatus);

      //休眠一段时间,防止msgList 为空的时候死循环执行,系统压力增大
      sleep(500)

      //继续执行本方法
      return processMsgInbox(subscribeId)
  ```
- 在项目启动的时候立即执行处理钉钉推送数据

  ```
  onProjectStart:
      processMsgInbox(subscribeId)
  ```
- 定时任务补偿执行处理钉钉推送数据（作为补偿机制存在）

  ```
  onTask:
      processMsgInbox(subscribeId)
  ```
