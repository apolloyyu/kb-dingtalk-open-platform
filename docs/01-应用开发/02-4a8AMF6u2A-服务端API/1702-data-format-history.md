---
title: "数据格式"
source_url: "https://open.dingtalk.com/document/development/data-format-history"
namespace: "development"
slug: "data-format-history"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 钉钉云 > 钉钉云数据推送 > 钉钉云数据推送格式 > 数据格式"
doc_id: "rnruMo6OBX"
updated_at: "2025-10-16 14:31:23"
---

> Source: https://open.dingtalk.com/document/development/data-format-history
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 钉钉云 > 钉钉云数据推送 > 钉钉云数据推送格式 > 数据格式
> Updated: 2025-10-16 14:31:23

# 数据格式

通过本文了解RDS和SyncHTTP推送的数据格式。

## RDS和SyncHTTP推送数据表说明

在推送数据表中，subscribe\_id、corp\_id、biz\_id、biz\_type四个字段构成唯一索引。

当同一个订阅者(subscribe\_id)订阅了某企业(corp\_id)下的一个业务类目(biz\_type)的一条数据(biz\_id)：

- 一个订阅者订阅一个企业下的相同业务类目下的同一条数据只存在一条
- 当数据发生重复变更时，收件箱会删除老数据再插入新数据，收件箱的自增主键会发生变化

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
| 25 | xxxxx\_0 | corpxxxx | userid或者deptid | 25 | 家校通讯录1.0(Deprecated)信息变更。家校通讯录升级，请查看家校通讯录2.0数据推送 |
| 32 | xxxxx\_0 | corpxxxx | 绑定： active+设备id  解绑： delete+设备id | 32 | 智能硬件绑定类型 |
| 37 | xxxxx\_0 | corpxxxx | orderidxx | 37 | 应用市场商业化服务关闭或服务开通事件 |
| 50 | xxxxx\_0 | corpxxxx | 无具体业务含义，只与其他属性构成唯一索引。  拼接规则：  人员关系事件： u\_r\_${id}\_${action}  监护人身份事件：g\_${id}\_${action}  学生身份事件： s\_${id}\_${action}  老师身份事件： t\_${id}\_${action}  示例：g\_1233\_insert | 50 | 家校通讯录2.0，部门信息变更 |
| 51 | xxxxx\_0 | corpxxxx | 无业务含义，只是与其他字段组成唯一索引。  拼接规则：d\_${id}\_${action} | 51 | 家校通讯录2.0，人员信息变更 |
| 63 | xxxxx\_0 | corpxxxx | 试用人的unionid | 63 | 应用试用记录回调信息 |
| 66 | xxxxx\_0 | corpxxxx | 无业务意义，幂等。  详见下方biz\_type=66的数据格式解释 | 66 | 工作台组件变更回调事件 |
| 67 | xxxxx\_0 | corpxxxx | 详见下方biz\_type=67的数据格式解释 | 67 | 钉钉假期相关回调事件 |
| 133 | xxxxx\_0 | corpxxxx | 详见下方biz\_type=133的数据格式解释 | 133 | CRM客户动态相关数据回调事件 |
| 137 | xxxxx\_0 | corpxxxx | 无业务意义，幂等。  详见下方biz\_type=137的数据格式解释 | 137 | 人事平台员工异动V2相关数据回调事件。 |
| 175 | xxxxx\_0 | corpxxxx | 无业务意义，幂等。  详见下方biz\_type=175的数据格式解释 | 175 | 人事解决方案变更事件。 |

## biz\_type=2

当biz\_type=2时，数据为套件票据suiteTicket最新状态。

该数据为定时推送，插入表open\_sync\_biz\_data中。

| **字段** | **说明** |
| --- | --- |
| subscribe\_id | 套件suiteid加下划线0。 |
| corp\_id | 套件所属企业的corpid。 |
| biz\_id | 套件suiteid。 |
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

该数据为企业授权微应用、解除微应用授权、变更微应用的授权范围时刻推送，插入表open\_sync\_biz\_data中。

| **字段** | **说明** |
| --- | --- |
| subscribe\_id | 套件suiteid加下划线0。 |
| corp\_id | 开通套件微应用的企业corpid。 |
| biz\_id | 套件suiteid。 |
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

  - org\_suite\_auth：表示企业授权套件
  - org\_suite\_change：表示企业变更授权范围
  - org\_suite\_relieve：表示企业解除授权
  > **[!NOTE]**
  >
  > **org\_suite\_auth**，**org\_suite\_change**两个事件都表示企业对于套件的授权信息，需要等同处理，在很短时间内发生的两个事件，有可能会覆盖，保证只给出最新的授权信息
- auth\_corp\_info, auth\_info和auth\_user\_info 三段结构信息请参考[获取企业开通应用后的授权信息](https://open.dingtalk.com/document/isvapp/obtains-the-authorization-information-after-the-enterprise-activates-the-application)。
- auth\_scope结构信息请参考[获取通讯录权限范围](https://open.dingtalk.com/document/isvapp/obtain-corpsecret-authorization-scope)。
- permanent\_code已废弃。
- ch\_permanent\_code已废弃。

## biz\_type=7

当biz\_type=7时，数据为企业微应用的最新状态。

该数据为企业停用、启动微应用的时刻推送，插入表open\_sync\_biz\_data中。

| **字段** | **说明** |
| --- | --- |
| subscribe\_id | 套件suiteid加下划线0。 |
| corp\_id | 开通套件微应用的企业corpid。 |
| biz\_id | 微应用的appid。 |
| biz\_data | 数据为Json格式。 |

biz\_data数据如下：

其中，syncAction字段的取值如下：

- org\_micro\_app\_restore：微应用启用

  ```
  {
      "agentId":12345677,
      "syncAction":"org_micro_app_restore"
  }
  ```
- org\_micro\_app\_stop：微应用停用

  ```
  {
      "agentId":12345677,
      "syncAction":"org_micro_app_stop"
  }
  ```
- org\_micro\_app\_remove：微应用删除，保留企业对套件的授权

  ```
  {
      "agentId":12345677,
      "syncAction":"org_micro_app_remove"
  }
  ```
- org\_micro\_app\_scope\_update：微应用可见范围变更

  ```
  {
      "agentId":12345677,
      "syncAction":"org_micro_app_scope_update"
  }
  ```

## biz\_type=13

当biz\_type=13时，数据为企业员工的最新状态。

该数据为在授权微应用的企业中，发生员工的增加、删除、修改的时刻推送，插入表open\_sync\_biz\_data\_medium中。

| **字段** | **说明** |
| --- | --- |
| subscribe\_id | 套件suiteid加下划线0。 |
| corp\_id | 开通套件微应用的企业corpid。 |
| biz\_id | 员工的userid。 |
| biz\_data | 数据为Json格式。 |

biz\_data数据为如下两种Json格式，企业增加或修改员工，字段值来自于[根据userId获取用户详情](https://open.dingtalk.com/document/isvapp-server/query-user-details#topic-1960047)接口 。

- 增加企业员工：

  其中**syncAction**字段取值含义如下：

  - user\_add\_org：企业增加员工事件之后的员工信息
  - user\_modify\_org：企业修改员工事件之后的员工信息
  - user\_dept\_change：企业修改员工所在部门事件之后的员工信息
  - user\_role\_change：企业修改员工所在角色(包括管理员变更)事件之后的员工信息
  - user\_active\_org：用户加入企业后的激活信息，active字段为true时表示已激活

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
- 企业删除员工

  ```
  {
      "syncAction":"user_leave_org"
      // 删除员工userid从biz_id中获取
  }
  ```

## biz\_type=14

当biz\_type=14时，数据为企业部门的最新状态。

该数据为在授权微应用的企业，发生部门的增加、删除、修改的时刻推送，插入表open\_sync\_biz\_data\_medium。

| **字段** | **说明** |
| --- | --- |
| subscribe\_id | 套件suiteid加下划线0。 |
| corp\_id | 开通套件微应用的企业corpid。 |
| biz\_id | 部门ID。 |
| biz\_data | 数据为Json格式。 |

biz\_data数据为如下两种Json格式，企业增加或修改部门，字段值来自于[获取部门详情](https://open.dingtalk.com/document/isvapp/query-department-details0-v2)接口 。

- 企业增加部门：

  其中**syncAction**字段取值含义如下：

  - org\_dept\_create：创建部门
  - org\_dept\_modify：修改部门

  ```
  {
      "errcode": 0,
      "userPerimits": "",
      "syncAction": "org_dept_create",
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
- 企业删除部门

  ```
  {
      "syncAction":"org_dept_remove"
  }
  ```

## biz\_type=15

当biz\_type=15时，数据为企业角色的最新状态。

该数据为在授权微应用的企业中，发生角色的增加、删除、修改的时刻推送，插入表open\_sync\_biz\_data\_medium中。

| **字段** | **说明** |
| --- | --- |
| subscribe\_id | 套件suiteid加下划线0。 |
| corp\_id | 开通套件微应用的企业corpid。 |
| biz\_id | 角色ID。 |
| biz\_data | 数据为Json格式。 |

biz\_data数据为如下两种Json格式：

- 企业增加/修改角色：企业增加角色事件之后的角色信息

  ```
  {
      "role_name": "角色01",
      "role_id": 12345,
      "group_id": 1,
      "group_name": "默认角色组",
      "syncAction": "org_role_add"
  }
  ```
- 企业删除角色：企业修改角色事件之后的角色信息

  ```
  {
      "syncAction":"org_role_remove"
  }
  ```

## biz\_type=16

当biz\_type=16时，数据为企业的最新状态。

该数据为在授权微应用的企业中，企业信息发生变更的时刻推送，插入表open\_sync\_biz\_data\_medium中。

| **字段** | **说明** |
| --- | --- |
| subscribe\_id | 套件suiteid加下划线0。 |
| corp\_id | 开通套件微应用的企业corpid。 |
| biz\_id | 企业的corpid。 |
| biz\_data | 数据为Json格式。 |

biz\_data数据为如下两种 Json格式：

- 企业变更

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
- 企业删除

  ```
  {
      "syncAction": "org_remove"
  }
  ```

## biz\_type=17

当biz\_type=17时，数据为订单信息。

该数据为企业在钉钉服务市场购买开通应用产生订单时刻推送，插入表open\_sync\_biz\_data中。

| **字段** | **说明** |
| --- | --- |
| subscribe\_id | 套件suiteid加下划线0。 |
| corp\_id | 开通套件微应用的企业corpid。 |
| biz\_id | 订单的orderid。 |
| biz\_data | 数据为Json格式。 |

biz\_data数据如下：

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
    "unionId": "union1265341625",
    "outTradeNo": "30990011123",
    "mainArticleCode": "DT_GOODS_1233",
    "mainArticleName": "测试商品001",
    "openId": "2343242412",
    "orderChannelCode": "all_star_isv_channel_code",
    "isvOperationCode": "***",
    "orderChargeType": "FREE",
    "articleType": "normal",
    "originalArticleCode": "DT_GOODS_23311",
    "originalItemCode": "DT_GOODS_23311_123",
    "appId": 299011,
    "extendParam": {
        "name": "***"
    },
    "buyUserId": "staff2313",
    "solutionPackageKey": "SOLUTION313-31231",
    "solutionPackageName": "中小企业财务解决方案",
    "mainCorpId": "ding23093214311",
    "saleModelType": "CYC_UPGRADE",
    "orderLabel": 1,
    "presentRelMainOrderId": 209130000311,
    "autoChangeFreeItem": false,
    "leadsFrom": "广场-搜索",
    "purchaserType":1
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
| buyCorpId | 购买企业的corpId。  **[!IMPORTANT]**  使用HTTP推送方式时返回此参数，且此参数即将废弃，**建议使用corpId作为购买企业的唯一标识。** |
| distributorCorpName | 分销商企业名称。  **[!NOTE]**  当商品类型**articleType**为**image**时不返回此字段。 |
| distributorCorpId | 分销商企业corpId。  **[!NOTE]**  当商品类型**articleType**为**image**时不返回此字段。 |
| paidtime | 支付时间（单位：毫秒）。 |
| serviceStopTime | 服务结束时间（单位：毫秒）。 |
| orderCreatSource | 订单来源：   - 默认订单来自应用中心。 - 若值为**TIANYUAN**，表示来自天元系统平台。 |
| payFee | 实际支付价格（单位：分）。  **[!NOTE]**  当商品类型**articleType**为**image**时不返回此字段。 |
| nominalPayFee | 名义票面费用（单位：分），现与payFee值相等。  **[!NOTE]**  当商品类型**articleType**为**image**时不返回此字段。 |
| discountFee | 折扣减免费用（单位：分），现值为0。  **[!NOTE]**  当商品类型**articleType**为**image**时不返回此字段。 |
| discount | 折扣，现值为1.00。  **[!NOTE]**  当商品类型**articleType**为**image**时不返回此字段。 |
| serviceStartTime | 服务开始时间（单位：毫秒）。 |
| orderType | 订单类型，取值：   - **BUY**：新购 - **RENEW**：续费 - **UPGRADE**：升级 - **RENEW\_UPGRADE**：续费升配 - **RENEW\_DEGRADE**：续费降配 |
| unionId | 下单人unionId。 |
| outTradeNo | 外部订单号。 |
| mainGoodsCode | 内购商品关联的主应用商品code。  **[!NOTE]**  当订单为内购商品订单时该字段有值。 |
| mainGoodsName | 内购商品关联的主应用商品名称。  **[!NOTE]**  当订单为内购商品订单时该字段有值。 |
| openId | 用户在当前开放应用内的唯一标识。 |
| purchaserType | 购买类型。   - **1**：组织购买 - **2**：个人购买   **[!NOTE]**  当订单为内购商品订单时该字段有值。 |
| orderChannelCode | 订单来源渠道码。 |
| isvOperationCode | 开发者后台商品管理生成商品二维码时ISV填入的渠道码。 |
| orderChargeType | 订单收费类型（仅针对试用规格）   - **FREE**：免费开通 - **TRYOUT**：试用开通 |
| articleType | 商品类型，取值：   - **normal**：普通商品 - **image**：OXM镜像商品。   **[!NOTE]**  OXM商品：非官方商品纳入钉钉一方售卖的机制，需要确定对接方式，并经过必要的立项和评审环节，可融入付费钉钉或独立售卖，支持进入钉钉甄选市场的商品。 |
| originalArticleCode | 镜像商品对应的原生商品Code。  **[!NOTE]**  非OXM商品可不用关注该字段。 |
| originalItemCode | 镜像商品规格Code对应的原生商品的规格Code。  **[!NOTE]**  非OXM商品可不用关注该字段。 |
| appId | 应用ID。  **[!NOTE]**  内购订单时该字段有值。 |
| extendParam | 订单扩展参数。 |
| buyUserId | 下单人在企业内的工号。 |
| solutionPackageKey | 解决方案KEY值。  **[!NOTE]**  当订单为解决方案时该字段有值。 |
| solutionPackageName | 解决方案名称。  **[!NOTE]**  当订单为解决方案时该字段有值。 |
| mainCorpId | 个人体验版虚拟组织对应的主组织ID。 |
| autoChangeFreeItem | 自动转免费规格。  **[!NOTE]**  付费商品如果有免费规格，试用到期后会系统自动下单转免费规格，包含此订单标记。 |
| orderLabel | 订单标记，取值   - **0**: 普通订单 - **1**：满赠订单 |
| presentRelMainOrderId | 满赠订单关联的付费主订单ID。 |
| leadsFrom | 商机来源，取值包含：   - 工作台-底部推荐 - 工作台-分组推荐 - 工作台-分组更多-顶部推荐位 - 工作台-应用图标推荐 - 广场-搜索 - 广场-banner - 广场-专题 - 广场-商品推荐 - 应用中心-新企业管理员推荐 - 应用中心-搜索 - 应用中心-banner - 应用中心-专题 - 应用中心-全部应用(安卓) - 应用中心-解决方案 - 人事专区 - 开发者后台-推广码 - PC应用中心 |
| saleModelType | 售卖模式，取值：   - **CYC\_UPGRADE\_MEMBER**： 按周期 + 数量（人数）售卖 - **CYC\_UPGRADE**： 按周期售卖 - **QUANTITY**： 按数量（人数）售卖 |

## biz\_type=20

当biz\_type=20时，数据为企业外部联系人的最新状态。

该数据为在授权微应用的企业中，发生外部联系人的增加、删除、修改的时刻推送，插入表open\_sync\_biz\_data\_medium中。

| **字段** | **说明** |
| --- | --- |
| subscribe\_id | 套件suiteid加下划线0。 |
| corp\_id | 开通套件微应用的企业corpid。 |
| biz\_id | 外部联系人的userId。 |
| biz\_data | 数据为Json格式。 |

biz\_data数据为如下两种 Json格式：

- 企业增加/修改外部联系人：

  - 当syncAction为contact\_add\_org时表示企业增加外部联系人事件之后的联系人信息。
  - 当syncAction为contact\_modify\_org时表示企业修改外部联系人事件之后的联系人信息。

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
- 企业删除外部联系人

  ```
  {"syncAction":"contact_leave_org"}
  ```

## biz\_type=22

当biz\_type=22时，数据为由ISV通过接口发起的审批实例数据。

该数据为在授权微应用的企业中，当由ISV通过接口发起的审批出现变更的时刻产生数据推送，插入表open\_sync\_biz\_data\_medium中。

> **[!NOTE]**
>
> 当表单内容大于64KB时，为防止推送失败，推送数据中会省略掉formValueVOS字段，并同时添加formValuesOmitted为true的标识字段。若需要获取表单完整数据，可调用服务端API-[获取单个审批实例详情](https://open.dingtalk.com/document/isvapp/obtains-the-details-of-a-single-approval-instance-pop)接口。

| **字段** | **说明** |
| --- | --- |
| subscribe\_id | 套件suiteid加下划线0。 |
| corp\_id | 开通套件微应用的企业corpid。 |
| biz\_id | 审批实例ID。 |
| biz\_data | 数据为Json格式。 |

biz\_data数据如下。

其中"syncAction" 字段取值含义如下：

- isv\_bpms：一条审批记录的创建或者流程更新。
- isv\_bpms\_cancel：一条审批记录撤销（字段保留待开发）

```
{
  "processInstanceId": "bbdf6db4-8786-4cd7-afce-xxx955094716",
  "attachedProcessInstanceIds": [],
  "syncAction": "isv_bpms",
  "businessId": "201808201943000524542",
  "title": "13567666099的test_1534743715441",
  "originatorDeptId": "-1",
  "url": "https://aflow.dingtalk.com/dingtalk/mobile/homepage.htm?corpid=ding6e51bbd3049d542f35c2f4657eb6378f&dd_share=false&showmenu=true&dd_progress=false&back=native&procInstId=bbdf6db4-8786-4cd7-afce-1ee955094716c&taskId=&dinghash=approval&dd_from=isv#approval",
  "operationRecords": [{
    "date": 1534765433000,
    "result": "NONE",
    "type": "START_PROCESS_INSTANCE",
    "userId": "0805174458-2101290130"
  }],
  "result": "",
  "bizAction": "NONE",
  "ccUserids": ["0805174458-xxxx290130"],
  "createTime": 1534765433000,
  "originatorUserid": "0805174458-210129xxxx",
  "processCode": "PROC-0D214F00-1817-490F-xxxx-541FEF589574",
  "formValueVOS": [{
    "name": "文本1",
    "id": "TextField-JL1PLEE3",
    "value": "测试"
  }],
  "tasks": [{
    "result": "NONE",
    "createTime": 1534765434000,
    "userId": "0805174458-2101290130",
    "taskId": 39260212292,
    "status": "RUNNING"
  }],
  "approverUserids": ["0805174458-2101290130"],
  "originatorDeptName": "XX的体验组织",
  "status": "RUNNING"
}
```

字段说明，请参考[获取单个审批实例详情](https://open.dingtalk.com/document/isvapp/obtains-the-details-of-a-single-approval-instance-pop)。

## biz\_type=32

当biz\_type=32时，数据为智能硬件设备管理。

该数据为企业发生硬件设备绑定变更时推送，插入表open\_sync\_biz\_data中。

| **字段** | **说明** |
| --- | --- |
| subscribe\_id | 套件suiteid加下划线0。 |
| corp\_id | 开通套件微应用的企业corpid。 |
| biz\_id | 绑定： active + 设备id  解绑： delete + 设备id |
| biz\_type | 32，为固定值，标识是智能硬件绑定类型消息。 |
| biz\_data | 数据为Json格式。 |

biz\_data数据如下。

- 绑定事件

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
- 解绑事件

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

**字段说明：**

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

当biz\_type=37时，数据为应用市场商业化服务关闭数据或服务开通数据。

该数据在退款导致服务关闭或续费变配生效时推送，插入表open\_sync\_biz\_data中。

| **字段** | **说明** |
| --- | --- |
| subscribe\_id | 第三方企业应用的suiteid加下划线0。 |
| corp\_id | 开通第三方企业应用的企业corpid。 |
| biz\_id | 订单orderId。 |
| biz\_data | 数据为Json格式。 |

#### **服务关闭的biz\_data数据如下（目前仅退款导致服务关闭时推送）：**

```
{
    "eventType": "subscription_close",
    "syncAction": "market_service_close",
    "orderId": "312139204444444",
    "corpId": "dingxxxxxxxxxxxx",
    "goodsName": "测试商品",
    "goodsCode": "xxxxxxxxxxx",
    "itemName": "测试规格",
    "itemCode": "xxxxxxx",
    "suiteId": 123123,
    "suiteKey": "xxxxxxxxx",
    "payFee": 1000,
    "subQuantity": 1,
    "closeType": 3,
    "refundId": "2088"
}
```

**字段说明：**

| 字段 | 说明 |
| --- | --- |
| eventType | 事件类型：   - **subscription\_close**：服务关闭事件 |
| syncAction | 操作类型：   - **market\_service\_close**：服务关闭事件 |
| orderId | 订单id。 |
| corpId | 购买企业的corpId。 |
| suiteId | 用户购买第三方企业应用的suiteId。 |
| suiteKey | 用户购买第三方企业应用的suiteKey。 |
| goodsName | 商品名称。 |
| goodsCode | 商品码。 |
| itemName | 规格名称。 |
| itemCode | 规格码。 |
| subQuantity | 购买数量。 |
| payFee | 实际支付价格（单位：分）。 |
| refundId | 退款id，退款唯一标识。 |
| closeType | 服务关闭类型：   - **3**：退款导致的服务关闭 |

#### 服务开通的biz\_data数据如下（目前仅续费变配服务开通时推送）：

```
{
    "eventType": "subscription_open",
    "syncAction": "market_service_open",
    "orderId": "312139204444444",
    "corpId": "dingxxxxxxxxxxxx",
    "goodsName": "测试商品",
    "goodsCode": "xxxxxxxxxxx",
    "itemName": "测试规格",
    "itemCode": "xxxxxxx",
    "suiteId": 123123,
    "suiteKey": "xxxxxxxxx",
    "payFee": 1000,
    "subQuantity": 1,
    "serviceStartTime": 167000031311,
    "serviceStopTime": 168000031311,
    "openType": 3
}
```

**字段说明：**

| 字段 | 说明 |
| --- | --- |
| eventType | 事件类型：   - **subscription\_open**：服务开通事件 |
| syncAction | 操作类型：   - **market\_service\_open**：服务开通事件 |
| orderId | 订单id。 |
| corpId | 购买企业的corpId。 |
| suiteId | 用户购买第三方企业应用的suiteId。 |
| suiteKey | 用户购买第三方企业应用的suiteKey。 |
| goodsName | 商品名称。 |
| goodsCode | 商品码。 |
| itemName | 规格名称。 |
| itemCode | 规格码。 |
| subQuantity | 购买数量。 |
| payFee | 实际支付价格（单位：分）。 |
| serviceStartTime | 订购服务开始时间（单位：毫秒）。 |
| serviceStopTime | 订购服务结束时间（单位：毫秒）。 |
| openType | 服务开通类型：   - **3**：续费变配开通 |

## biz\_type=50

家校通讯录2.0，部门变更推送。subscribe\_id, corp\_id, biz\_id, biz\_type组成唯一索引。

| 字段 | 说明 |
| --- | --- |
| subscribe\_id | 套件suiteid加下划线0。 |
| corp\_id | 开通套件微应用的企业corpid。 |
| biz\_id | 无业务含义，只是与其他字段组成唯一索引。  拼接规则：d\_${id}\_${action} |
| biz\_type | 业务类型。家校通讯录部门变更的值为50。 |
| biz\_data | 数据为Json格式。 |

biz\_data主要包括家校通讯录架构中各个部门发生变更时的信息。主要包括新增，更新，删除(毕业)：

- **edu\_dept\_insert：部门节点新增**

  | 名称 | 类型 | 示例 | 说明 |
  | --- | --- | --- | --- |
  | dept\_id | String | 12345 | 部门ID。 |
  | contact\_type | String | classic | 家校通讯录类型。  - classic: 传统经典4层结构。校区/学段/年级/班级。 - custom：自定义结构，但是叶子节点仍旧是班级。 |
  | name | String | 一年级2班(苹果班) | 部门名称。 |
  | nick | String | 苹果班 | 部门别名。 |
  | dept\_type | String | grade | 部门类型：  - **campus：**校区/学院 - **period**：学段 - **grade**：年级 - **class**：班级 - **dept**：没有业务含义，只是一个部门节点。 |
  | chain | string | [123,456] | 从顶层部门到当前节点部门的部门链，其内容不包含当前节点。  如classic类型下的班级：[校区id,学段id,年级id]；如classic类型下的校区: []。 |
  | feature | String |  | 部门feature，JSON格式。  各种节点部门存在不同的属性。 |
  | syncAction | String | edu\_dept\_insert | 事件类型。  syncAction为edu\_dept\_insert表示新增部门节点。 |
  | errcode | Number | 0 | 返回码。 |
  | errmsg | String | ok | 返回码描述。 |
- **edu\_dept\_update：被更新的部门节点以及其当前最新相关信息**

  | 名称 | 类型 | 示例 | 说明 |
  | --- | --- | --- | --- |
  | dept\_id | String | 12345 | 部门ID。 |
  | contact\_type | String | classic | 家校通讯录类型。  - classic: 传统经典4层结构。校区/学段/年级/班级。 - custom：自定义结构，但是叶子节点仍旧是班级。 |
  | name | String | 一年级2班(苹果班) | 部门名称。 |
  | nick | String | 苹果班 | 部门别名。 |
  | dept\_type | String | grade | 部门类型：  - **campus：**校区/学院 - **period**：学段 - **grade**：年级 - **class**：班级 - **dept**：没有业务含义，只是一个部门节点。 |
  | chain | string | [123,456] | 从顶层部门到当前节点部门的部门链，其内容不包含当前节点。  如classic类型下的班级：[校区id,学段id,年级id]；如classic类型下的校区: []。 |
  | feature | String |  | 部门feature，JSON格式。  各种节点部门存在不同的属性。 |
  | syncAction | String | edu\_dept\_update | 事件类型。 |
  | errcode | Number | 0 | 返回码。 |
  | errmsg | String | ok | 返回码描述。 |
- **edu\_dept\_delete：被删除的部门节点**

  | 名称 | 类型 | 示例 | 说明 |
  | --- | --- | --- | --- |
  | dept\_id | Number | 12345 | 部门节点ID。 |
  | is\_graduate | Number | 0 | **0**：表示正常的删除。  **1**：表示毕业。 |
  | syncAction | String | edu\_dept\_delete | 事件类型。 |
  | errcode | Number | 0 | 返回码。 |
  | errmsg | String | ok | 返回码描述。 |

## biz\_type=51

家校通讯录2.0，人员变更推送。

subscribe\_id, corp\_id, biz\_id, biz\_type组成唯一索引。

| 字段 | 说明 |
| --- | --- |
| subscribe\_id | 套件suiteid加下划线0。 |
| corp\_id | 开通套件微应用的企业corpid。 |
| biz\_id | 无具体业务含义，只与其他属性构成唯一索引。  拼接规则：   - 人员关系事件：u\_r\_${id}\_${action} - 监护人身份事件：g\_${id}\_${action} - 学生身份事件：s\_${id}\_${action} - 老师身份事件：t\_${id}\_${action}   示例：g\_1233\_insert |
| biz\_type | 业务类型，家校通讯录人员变更的值为51。 |
| biz\_data | 数据为Json格式。 |

家校通讯录人员变更，主要包括两部分：人员在家校业务场景下的身份以及用户关系。

> **[!NOTE]**
>
> 关系目前只有监护人与学生的关系。

- **人员身份biz\_data说明**

  - **edu\_user\_insert：在某个班级中新增人员身份**

    | 名称 | 类型 | 示例 | 说明 |
    | --- | --- | --- | --- |
    | userid | String | 123344 | 用户的userid。 |
    | unionid | String | FzyqbxFafVOEEEE5kGv93wiEiE | unionid, 无手机号的学生为""。 |
    | role | String | teacher | 此人在家校的角色类型：  - **teacher**：老师角色 - **guardian**：监护人角色 - **student**：学生角色 |
    | name | String | 小明爸爸 | 此人在此班级的项目。 |
    | class\_id | Number | 12345 | 班级ID。 |
    | feature | String |  | 各个角色下存在不同属性，JSON格式。 |
    | └ is\_adviser |  |  | 是否班主任，老师角色下有效。 |
    | └ student\_no |  |  | 学号，学生角色下有效。  此值如果班级中设置了学号则有值，否则无值。 |
    | syncAction | String | edu\_user\_insert | 事件类型。 |
    | errcode | Number | 0 | 返回码。 |
    | errmsg | String | ok | 返回码描述。 |
  - **edu\_user\_update：在某个班级中人员相关身份的变更**

    | 名称 | 类型 | 示例 | 说明 |
    | --- | --- | --- | --- |
    | userid | String | 123344 | 用户的userid。 |
    | role | String | teacher | 此人在家校的角色类型：  - **teacher**：老师角色 - **guardian**：监护人角色 - **student**：学生角色 |
    | name | String | 小明爸爸 | 此人在此班级的项目。 |
    | class\_id | Number | 12345 | 班级ID。 |
    | feature | String |  | 各个角色下存在不同属性，JSON格式。 |
    | └ is\_adviser |  |  | 是否班主任，老师角色下有效。 |
    | └ student\_no |  |  | 学号，学生角色下有效。 |
    | syncAction | String | edu\_user\_update | 事件类型。 |
    | errcode | Number | 0 | 返回码。 |
    | errmsg | String | ok | 返回码描述。 |
  - **edu\_user\_delete：在某个班级中人员身份的删除**

    | **名称** | **类型** | **示例** | **说明** |
    | --- | --- | --- | --- |
    | userid | String | 123456 | 用户的userid。 |
    | role | String | teacher | 此人在家校的角色类型。  - **teacher：**老师角色 - **guardian：**监护人。 - **student：**学生 |
    | class\_id | Number | 12345 | 班级ID。 |
    | is\_graduate | Number | 0 | - **0**：表示正常的删除。 - **1**：表示由于毕业业务导致的人员删除。 |
    | feature | String |  | 扩展属性，老师身份提前下有效。 |
    | |\_ is\_adviser | Integer | 0 | 是否是班主任。只有在teacher的角色下有效。  - **0**: 非班主任身份 - **1**：班主任身份 |
    | syncAction | String | edu\_user\_delete | 事件类型。 |
    | errcode | Number | 0 | 返回码。 |
    | errmsg | String | ok | 返回码描述。 |
- **人员关系biz\_data说明**

  - **edu\_user\_relation\_insert**

    此事件中各个字段的理解，可以总结为如下一句表达式：在班级${classId}中，${from}是${to}的 ${relationName}。

    示例：在班级12345中，"123457896"是"34567890"的"爸爸"。在家校场景下，from为监护人，to为学生。

    | 名称 | **类型** | **示例** | **说明** |
    | --- | --- | --- | --- |
    | from\_userid | String | 123457896 | 用户的userid。 |
    | to\_userid | String | 34567890 | 用户的userid。 |
    | class\_id | Number | 12345 | 班级ID。 |
    | relation\_code | String | F | 关系code。 |
    | relation\_name | String | 爸爸 | 关系名。 |
    | syncAction | String | edu\_user\_relation\_insert | 事件类型。 |
    | errcode | Number | 0 | 返回码。 |
    | errmsg | String | ok | 返回码描述。 |
  - **edu\_user\_relation\_update**

    此事件中各个字段的理解，可以总结为如下一句表达式：在班级${classId}中，将${from}与${to}的关系更新为 ${relationName}。

    示例：在班级12345中，将"123457896"的"34567890"关系更新为"妈妈"。在家校场景下，from为监护人，to为学生。

    | 名称 | **类型** | **示例** | **说明** |
    | --- | --- | --- | --- |
    | from\_userid | String | 123457896 | 用户的userid。 |
    | to\_userid | String | 34567890 | 用户的userid。 |
    | class\_id | Number | 12345 | 班级ID。 |
    | relation\_code | String | M | 关系code。 |
    | relation\_name | String | 妈妈 | 关系名。 |
    | syncAction | String | edu\_user\_relation\_update | 事件类型。 |
    | errcode | Number | 0 | 返回码。 |
    | errmsg | String | ok | 返回码描述。 |
  - **edu\_user\_relation\_delete**

    此事件中各个字段的理解，可以总结为如下一句表达式：在班级${classId}中，将${from}是${to}的 ${relationName}的关系删除。

    示例：在班级12345中，删除"123457896"是"34567890"的"爸爸"这样一层关系。在家校场景下，from为监护人，to为学生。

    | 名称 | **类型** | **示例** | **说明** |
    | --- | --- | --- | --- |
    | from\_userid | String | 123457896 | 用户的userid。 |
    | to\_userid | String | 34567890 | 用户的userid。 |
    | class\_id | Number | 12345 | 班级ID。 |
    | relation\_code | String | M | 关系code。 |
    | relation\_name | String | 妈妈 | 关系名。 |
    | syncAction | String | edu\_user\_relation\_delete | 事件类型。 |
    | errcode | Number | 0 | 返回码。 |
    | errmsg | String | ok | 返回码描述。 |

## biz\_type=63

应用商品新增个人试用后，增加了应用的触达率，为了方便ISV对客户进行后续跟踪和推广，组织/个人在应用试用后，钉钉后台新增了应用试用记录的回调信息。

目前试用的回调信息有两种：

1. 试用开通的订单信息

   试用开通的订单信息，侧重于订单信息回调。
2. 试用开通记录信息

   试用开通记录回调信息中不一定会有试用订单。

> **[!IMPORTANT]**
>
> 当同组织的两个用户对同一商品的试用时间完全重合，或者同组织下已经开通该商品试用的有效期完全包含新开通试用的有效期的时候，不会产生订单。

当biz\_type=63时，为应用试用开通记录的回调信息。

当组织或个人应用试用开通时推送，插入表open\_sync\_biz\_data中。

| **字段** | **说明** |
| --- | --- |
| subscribe\_id | 套件suiteid加下划线0。 |
| corp\_id | 开通套件微应用的企业corpid。 |
| biz\_id | 试用人的unionid。 |
| biz\_type | 63，为固定值，标识应用试用开通记录的回调信息。 |
| biz\_data | 开通记录数据，JSON格式。 |

示例：

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
    "itemType":"charge_goods_free_item",
    "TimeStamp":"1607050765623"
}
```

字段说明：

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
| itemType | 开通的规格类型：   - **charge\_goods\_free\_item**：付费商品的免费规格   **[!NOTE]**  当开通付费商品的免费规格时会返回该字段。 |
| TimeStamp | 时间戳。 |
| EventType | 事件类型。 |

## biz\_type=66

当biz\_type=66时，数据为工作台组件发生变更。

该数据为企业在工作台操作组件时推送，插入表open\_sync\_biz\_data中。

> **[!NOTE]**
>
> 当组件发生启用、停用、可见范围变化等事件时，会向ISV发出组件变更消息，当前仅支持可见范围变化的事件类型。

| **字段** | **说明** |
| --- | --- |
| subscribe\_id | 套件suiteid加下划线0。 |
| corp\_id | 操作组件的管理员企业corpid。 |
| biz\_id | 无业务意义，幂等。 |
| biz\_type | 66，为固定值，标识该消息为工作台组件相关数据。 |
| biz\_data | 数据为Json格式。 |

biz\_data数据如下：

```
{
    "componentEventType": "component_auth_scope_update",
    "suiteId": "1673xxx",
    "componentId": "microApp_xxxxx",
    "corpId": "ding13dbb8xxxx",
    "componentName": "500000xxxx",
    "eventType": "workbench_component_event",
    "requestNo": "microApp_429xxx"
}
```

字段说明：

| 字段 | 说明 |
| --- | --- |
| eventType | 推送事件类型，工作台组件事件。 |
| componentEventType | 组件事件类型，目前仅支持可见范围变更。 |
| suiteId | 套件ID。 |
| componentId | 组件ID。 |
| corpId | 组织corpId |
| componentName | 组件名称 |
| requestNo | 请求幂等号。 |

## biz\_type=67

当biz\_type=67时，数据为钉钉假期相关数据

该数据为企业发生假期相关的数据变更时推送，插入表open\_sync\_biz\_data中。

| **字段** | **说明** |
| --- | --- |
| subscribe\_id | 套件suiteid加下划线0。 |
| corp\_id | 开通套件微应用的企业corpId。 |
| biz\_id | 加班转调休事件：`${无业务含义的id}:${userId}:${workDate}`，workDate的格式为yyyyMMdd，如20210312。 |
| biz\_type | 67，为固定值，标识该消息为钉钉假期相关数据。 |
| biz\_data | 数据为Json格式。 |

biz\_data各数据格式如下。

- 加班转调休假事件（新增、更新时会触发同步）

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

> **[!NOTE]**
>
> 数据业务唯一性约束为 ${corpId}+${userId}+${workDate}，同一个员工一天内可能会触发多次数据同步，但是应以当天最后一次同步的数据为准（例如：重排班、修改加班申请、加班转调休规则修改等，均会触发重算逻辑，导致之前同一天已同步的数据失效）。
>
> **即**：一个员工一天只会有一条有效的加班转调休记录，不会存在2条。

**字段说明：**

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

## biz\_type=133

当biz\_type=133时，数据为CRM客户动态相关数据。

该数据为企业在客户动态相关的数据变更时推送，插入表open\_sync\_biz\_data中。

| **字段** | **说明** |
| --- | --- |
| corp\_id | 操作组件的管理员企业corpid。 |
| biz\_id | 无业务意义，幂等。 |
| biz\_type | 固定值133，表示该消息为CRM客户动态相关数据。 |
| biz\_data | 数据为Json格式。 |

biz\_data数据如下：

```
{
    "syncAction": "crm_customer_track",
    "tracks": [
        {
            "corpId": "ding9axxx",
            "customerId": "84c75568-xxx-xxx",
            "subType": 0,
            "gmtCreate": 1630474492814,
            "type": 107,
            "creator": "manager1234"
        }
    ],
    "syncSeq": "7C0F83xxx"
}
```

字段说明

| 参数 | 数据类型 | 说明 |
| --- | --- | --- |
| syncAction | String | 取值为`crm_customer_track`时，表示客户动态相关的数据变更。 |
| corpId | String | 客户所在组织的corpId。 |
| customerId | String | 客户ID。 |
| subType | Number | 客户动态子类型。 |
| gmtCreate | Number | 动态创建时间。 |
| type | Number | 客户动态类型。 |
| creator | String | 动态创建者的userid。 |

## biz\_type=137

当biz\_type=137时，数据为人事平台员工异动V2相关数据。

该数据为人事平台员工异动V2相关的数据变更时推送，插入表open\_sync\_biz\_data\_medium中。

| **字段** | **说明** |
| --- | --- |
| corp\_id | 企业corpId。 |
| biz\_id | 无业务意义，幂等。 |
| biz\_type | 固定值137，表示人事平台员工异动V2相关数据。 |
| biz\_data | 数据为Json格式。 |

biz\_data数据如下：

```
{
    "syncAction": "hrm_mdm_user_change",
    "changeType": 4,
    "staffId": "01142240209xxxxx",
    "bizTime": 1559836800000,
    "syncSeq": "335BF2BEE1351DC0241DDE"
}
```

字段说明：

| 参数 | 数据类型 | 说明 |
| --- | --- | --- |
| syncAction | String | 事件类型。 |
| changeType | Number | 人事平台员工异动类型：   - 1：入职 - 2：转正 - 3：调岗 - 4：离职 - 8：晋升 |
| staffId | String | 用户userId。 |
| bizTime | Long | 业务时间。 |
| syncSeq | String | 无业务意义。 |

## biz\_type=175

当biz\_type=175时，数据为人事解决方案变更事件的相关数据。

该数据为人事解决方案变更事件相关的数据推送，插入表open\_sync\_biz\_data\_medium中。

| **字段** | **说明** |
| --- | --- |
| corp\_id | 企业corpId。 |
| biz\_id | 无业务意义，幂等。 |
| biz\_type | 固定值175，表示人事解决方案变更相关数据。 |
| biz\_data | 数据为Json格式。 |

biz\_data数据如下：

```
{
  "corpId" : "ding57935b18bfd13e9735cxxxxxxxxxx",
  "staffIds" : [ "157087xxxxxxxx" ],
  "syncAction" : "hrm_solution_manage",
  "solutionType" : "onboarding",
  "solutionStatus" : "start"
}
```

字段说明：

| 参数 | 数据类型 | 说明 |
| --- | --- | --- |
| corpId | String | 企业corpId。 |
| staffIds | Array of String | 用户userId。 |
| syncAction | String | 事件类型。 |
| solutionType | String | 人事解决方案类型：   - onboarding：新人流程 |
| solutionStatus | String | 人事解决方案状态：   - init：初始化解决方案 - start：发起解决方案 |

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
