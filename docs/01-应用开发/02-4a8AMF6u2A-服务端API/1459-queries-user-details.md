---
title: "查询用户详情"
source_url: "https://open.dingtalk.com/document/development/queries-user-details"
namespace: "development"
slug: "queries-user-details"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 通讯录管理 > 用户管理1.0(不推荐) > 查询用户详情"
doc_id: "ssqZ01qVNz"
updated_at: "2026-08-25 09:36:51"
---

> Source: https://open.dingtalk.com/document/development/queries-user-details
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 通讯录管理 > 用户管理1.0(不推荐) > 查询用户详情
> Updated: 2026-08-25 09:36:51

# 查询用户详情

调用本接口根据userid获取用户详情。

> **[!IMPORTANT]**
>
> - 本接口已完成升级，后续将维持现有功能且不再新增能力。
> - 未接入的开发者建议使用新版[查询用户详情](0056-query-user-details.md)接口，已接入用户不受影响。

## 权限

服务端API是以应用维度授权的，在调用接口前，确保已经为应用添加了接口权限。

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 是 | **[!NOTE]**  不支持新增 | — |
| 第三方企业应用 | 是 | — |
| 第三方个人应用 | 否 | — |

## 基本信息

**请求方式**：GET

**请求地址**：`https://oapi.dingtalk.com/user/get`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6ed1bxxx | 调用服务端API的应用凭证。   - 企业内部应用可通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 - 第三方企业应用可通过[服务商获取第三方应用授权企业的access\_token](1448-obtain-isvapp-token.md)接口获取。 |
| userid | String | 是 | userid1 | 员工唯一标识userid。   - 企业内部应用可通过[根据手机号查询用户](1465-retrieve-userid-from-mobile-phone-number.md)接口获取。 - 第三方企业应用可通过[获取部门用户userid列表](1461-obtain-the-list-of-employee-ids-by-department-id.md)接口获取。 |
| lang | String | 否 | zh\_CN | 通讯录语言，默认zh\_CN。 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| userid | String | user123 | 员工在当前企业内的唯一标识，也称staffId。 |
| unionid | String | 3qsTvPlqZ98zcezgiPnRxxxxx | 员工在当前开发者企业账号范围内的唯一标识，系统生成，固定值，不会改变。 |
| managerUserid | String | manager240 | 员工直属主管的userid。 |
| hiredDate | Date | 1599235200000 | 入职时间，Unix时间戳 。  在OA后台通讯录中的员工基础信息中维护过入职时间才会返回。  **[!NOTE]**  第三方企业应用不返回该参数。 |
| tel | String | 8643xxxxx | 分机号。  **[!NOTE]**  第三方企业应用不返回该参数。 |
| remark | String | 测试用户 | 备注。  **[!NOTE]**  第三方企业应用不返回该参数。 |
| workPlace | String | 杭州 | 办公地点。  **[!NOTE]**  第三方企业应用不返回该参数。 |
| name | String | 张三 | 成员名称。 |
| position | String | 技术支持 | 职位信息。 |
| mobile | String | 138xxxx0000 | 手机号。  **[!NOTE]**  第三方企业应用不返回该参数。 |
| stateCode | String | 86 | 国家地区码。  **[!NOTE]**  第三方企业应用不返回该参数。 |
| email | String | 1@example.com | 员工的邮箱。  **[!NOTE]**  第三方企业应用不返回该参数。 |
| orgEmail | String | 1@dingtalk.com | 员工的企业邮箱。  如果员工的企业邮箱没有开通，返回信息中不包含该数据。  **[!NOTE]**  第三方企业应用不返回该参数。 |
| isSenior | Boolean | true | 是否开启高管模式:   - **true**：开启  开启后，手机号码对所有员工隐藏。普通员工无法对其发DING、发起钉钉免费商务电话。高管之间不受影响。 - **false**：不开启 |
| jobnumber | String | 1 | 员工工号，对应显示到OA后台和客户端个人资料的工号栏目。  长度为0~64个字符。 |
| active | Boolean | true | 是否已经激活：   - **true**：表示已激活 - **false**：表示未激活 |
| avatar | String | http://xxxxx | 头像URL。 |
| extattr | String | {\"爱好\"\:"读书\"} | 扩展属性，可以设置多种属性。  **[!NOTE]**  第三方企业应用不返回该参数。  手机上最多只能显示10个扩展属性，可登录[**OA管理后台**](https://oa.dingtalk.com/index.htm#/setting#setOrgInfo) **> 设置 > 通讯录信息**进行设置。  **查看扩展属性：**   - 链接类型扩展属性，只支持在“移动端钉钉-点击该用户头像-个人资料页”查看，点击链接可以跳转。  **[!NOTE]**  链接类型支持变量通配符自动替换，目前支持通配符有：userid，corpid。示例： `[工位地址](http://www.dingtalk.com?userid=#userid#&corpid=#corpid#)`。 - 非链接类型扩展属性，支持在“移动端钉钉/PC端钉钉-点击该用户头像-个人资料页”查看。 |
| roles | Roles[] |  | 用户所在角色列表。 |
| id | Number | 149xxxxx | 角色ID。 |
| name | String | 总监 | 角色名称。 |
| type | Number | 101 | 标签组。  type返回值如下：   - **type is null**：自建 - **0**（可以删除）：系统生成 - **1**：默认员工标签组 - **101**：主管理员 - **102**：子管理员 - **103**：负责人 - **104**：部门主管 - **201**：项目角色标签组 |
| groupName | String | 职务 | 角色组名称。 |
| department | String | [1,2] | 数组类型，数组里面值为整型，成员所属部门ID列表。 |
| orderInDepts | JSONObject | {1:1} | 在对应的部门中的排序，Map结构的json字符串。Key是部门的ID，Value是人员在这个部门的排序值。 |
| isAdmin | Boolean | true | 是否为企业的管理员：   - **true**：是 - **false**：不是 |
| isLeaderInDepts | String | {1:false} | 在对应的部门中是否为主管。  key是部门的ID，value是人员在这个部门中是否为主管，true表示是，false表示不是。 |
| isHide | Boolean | true | 是否号码隐藏：   - **true**：隐藏  隐藏手机号后，手机号在个人资料页隐藏，但仍可对其发DING、发起钉钉免费商务电话。 - **false**：不隐藏 |
| isBoss | Boolean | true | 是否为企业的老板：   - **true**：表示是 - **false**：表示不是 |
| realAuthed | Boolean | true | 是否实名认证：   - **true**：是 - **false**：否 |

## 示例

**请求示例（HTTP）**

```
GET https://oapi.dingtalk.com/user/get?access_token=ACCESS_TOKEN&userid=userid1
```

**请求示例（JAVA SDK）**

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/user/get");
OapiUserGetRequest req = new OapiUserGetRequest();
req.setUserid("userid1");
req.setHttpMethod("GET");
OapiUserGetResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

**返回示例**

- 企业内部应用

  ```
  {
      "errcode": 0,
      "errmsg": "ok",
      "unionid": "3qsTvPlqZ98zcezgiPnRxxxxx",
      "roles": [
          {
              "id": 149,
              "name": "总监",
              "groupName": "职务",
              "type": 102
          }
      ],
      "remark": "测试用户",
      "userid": "manager3378",
      "isLeaderInDepts": "{1:false}",
      "isBoss": true,
      "hiredDate": 1600099200000,
      "isSenior": true,
      "tel": "8643xxxxx",
      "department": [
          1,
          2
      ],
      "extattr": {
          "爱好": "读书"
      },
      "workPlace": "杭州",
      "orgEmail": "1@dingtalk.com",
      "email": "1@example.com",
      "orderInDepts": "{1:1}",
      "mobile": "138xxxx0000",
      "managerUserid": "manager240",
      "active": true,
      "avatar": "http://xxxxx",
      "isAdmin": true,
      "tags": {},
      "isHide": true,
      "jobnumber": "1",
      "name": "张三",
      "stateCode": "86",
      "position": "技术支持",
      "realAuthed": true
  }
  ```
- 第三方企业应用

  ```
  {
      "errcode": 0,
      "exclusiveAccount": false,
      "unionid": "BUMQk4CwjV2LNww06rRtoQiEiE",
      "userid": "01255030530821552072",
      "managerUserid": "manager8988",
      "isLeaderInDepts": "{1:false}",
      "isBoss": false,
      "isSenior": false,
      "department": [
          1
      ],
      "orderInDepts": "{1:1762990}",
      "errmsg": "ok",
      "active": false,
      "avatar": "",
      "managerUserid": "manager240",
      "isAdmin": false,
      "tags": {},
      "isHide": false,
      "jobnumber": "",
      "name": "杨XX",
      "position": "",
      "realAuthed": false
  }
  ```
