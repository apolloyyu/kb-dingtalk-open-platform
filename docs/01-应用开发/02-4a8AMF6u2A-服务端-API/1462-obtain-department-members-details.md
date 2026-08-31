---
title: "获取部门用户详情"
source_url: "https://open.dingtalk.com/document/development/obtain-department-members-details"
namespace: "development"
slug: "obtain-department-members-details"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "历史文档（不推荐） > 通讯录管理 > 用户管理1.0(不推荐) > 获取部门用户详情"
doc_id: "3STk4T7IgZ"
updated_at: "2026-08-25 09:36:53"
---

> Source: https://open.dingtalk.com/document/development/obtain-department-members-details
> Path: 应用开发 / 服务端 API / 历史文档（不推荐） > 通讯录管理 > 用户管理1.0(不推荐) > 获取部门用户详情
> Updated: 2026-08-25 09:36:53

# 获取部门用户详情

调用本接口获取部门用户详情。

> **[!IMPORTANT]**
>
> - 本接口已完成升级，后续将维持现有功能且不再新增能力。
> - 未接入的开发者建议使用新版[获取部门用户详情](0062-queries-the-complete-information-of-a-department-user.md)接口，已接入用户不受影响。

## 权限

服务端API是以应用维度授权的，在调用接口前，确保已经为应用添加了接口权限。

> **[!IMPORTANT]**
>
> 如果您想调用通讯录接口并同时获取员工手机号，添加通讯录手机号等敏感字段权限。

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 是 | **[!NOTE]**  不支持新增 | — |
| 第三方企业应用 | 是 | — |
| 第三方个人应用 | 否 | — |

## 基本信息

**请求方式**：GET

**请求地址**：`https://oapi.dingtalk.com/user/listbypage`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6ed1bxxx | 调用服务端API的应用凭证。   - 企业内部应用可通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 - 第三方企业应用可通过[服务商获取第三方应用授权企业的access\_token](1448-obtain-isvapp-token.md)接口获取。 |
| lang | String | 否 | zh\_CN | 通讯录语言，默认为zh\_CN。如果是英文，请输入en\_US。 |
| department\_id | Number | 是 | 1 | 获取的部门ID。1表示根部门，可调用[获取部门列表](1469-obtain-the-department-list.md)。  **[!NOTE]**  只获取当前部门下的员工信息，不包含子部门内的员工。 |
| offset | Number | 是 | 1 | 支持分页查询，与size参数同时设置时才生效，此参数代表偏移量，偏移量从0开始。 |
| size | Number | 是 | 1 | 支持分页查询，与offset参数同时设置时才生效，此参数代表分页大小，最大100。 |
| order | String | 否 | entry\_asc | 支持分页查询，部门成员的排序规则，默认不传是按自定义排序：   - **entry\_asc**：代表按照进入部门的时间升序 - **entry\_desc**：代表按照进入部门的时间降序 - **modify\_asc**：代表按照部门信息修改时间升序 - **modify\_desc**：代表按照部门信息修改时间降序 - **custom**：代表用户定义(未定义时按照拼音)排序 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| hasMore | Boolean | false | 在分页查询时返回，代表是否还有下一页更多数据。   - **false**：无下一页数据 - **true**：有下一页数据 |
| userlist | Userlist[] |  | 成员列表。 |
| userid | String | user123 | 员工在当前企业内的唯一标识，也称staffId。  可由企业在创建时指定，并代表一定含义比如工号，创建后不可修改。 |
| order | Number | 176318668975061512 | 表示员工在此部门中的排序，列表是按order的倒序排列输出的，即从大到小排列输出的。  **[!NOTE]**  管理员在管理后台里面调整了顺序后，order才有值。 |
| unionid | String | 3qsTvPlqZ98zcezgiPnRxxxx | 员工在当前开发者企业账号范围内的唯一标识，系统生成，固定值，不会改变。 |
| mobile | String | 138xxxx3264 | 手机号。  **[!NOTE]**  第三方企业应用不返回该参数。 |
| tel | String | 8643xxxx | 分机号。  **[!NOTE]**  第三方企业应用不返回该参数。 |
| workPlace | String | 杭州 | 办公地点。  **[!NOTE]**  第三方企业应用不返回该参数。 |
| remark | String | 测试用户 | 备注。  **[!NOTE]**  第三方企业应用不返回该参数。 |
| isAdmin | Boolean | false | 是否为企业的管理员：   - **true**：表示是 - **false**：表示不是 |
| isBoss | Boolean | false | 是否为企业的老板：   - **true**：表示是 - **false**：表示不是 |
| isHide | Boolean | false | 是否号码隐藏：   - **true**：表示隐藏 - **false**：表示不隐藏 |
| isLeader | Boolean | false | 是否是部门的主管：   - **true**：表示是 - **false**：表示不是 |
| name | String | 赵xx | 成员名称。 |
| active | Boolean | false | 是否激活了钉钉：   - **true**：已激活 - **false**：未激活 |
| department | Number[] | 1 | 部门信息。 |
| position | String | 技术支持 | 职位信息。 |
| email | String | 1@example.com | 员工邮箱。  **[!NOTE]**  第三方企业应用不返回该参数。 |
| orgEmail | String | 1@dingtalk.com | 员工的企业邮箱。  如果员工的企业邮箱没有开通，返回信息中不包含该数据。  **[!NOTE]**  第三方企业应用不返回该参数。 |
| avatar | String | http://xxxxx | 头像URL。 |
| jobnumber | String | 10001 | 员工工号，对应显示到OA后台和客户端个人资料的工号栏目。 |
| hiredDate | Date | 1599235200000 | 入职时间。 |
| extattr | String | {\"爱好\":\"读书\"} | 设置的扩展属性。  **[!NOTE]**  第三方企业应用不返回该参数。 |

## 示例

**请求示例（HTTP）**

```
GET https://oapi.dingtalk.com/user/listbypage?access_token=ACCESS_TOKEN&lang=zh_CN&department_id=1&offset=1&size=1&order=entry_asc
```

**请求示例（JAVA SDK）**

```
   DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/user/listbypage");
   OapiUserListbypageRequest req = new OapiUserListbypageRequest();
   req.setLang("zh_CN");
   req.setDepartmentId(1L);
   req.setOffset(1L);
   req.setSize(1L);
   req.setOrder("entry_asc");
   req.setHttpMethod("GET");
   OapiUserListbypageResponse rsp = client.execute(req, access_token);
   System.out.println(rsp.getBody());
```

**返回示例**

- 企业内部应用

  ```
  {
      "errcode": 0,
      "userlist": [{
          "unionid": "3qsTvPlqZ98zcezgiPnRxxxx",
          "isLeader": false,
          "mobile": "138xxxx3264",
          "active": false,
          "remark": "测试用户",
          "isAdmin": false,
          "avatar": "http://xxxxx",
          "userid": "user123",
          "isHide": false,
          "jobnumber": "10001",
          "isBoss": false,
          "hiredDate": 1598284800000,
          "name": "赵xx",
          "tel": "8643xxxx",
          "position": "技术支持",
          "orgEmail": "1@dingtalk.com""department": [1],
          "extattr": {
              "爱好": "读书"
          },

          "workPlace": "杭州",
          "email": "1@example.com",
          "order": 176318668975061512
      }],
      "hasMore": false,
      "errmsg": "ok"
  }
  ```
- 第三方企业应用

  ```
  {
          "errcode": 0, 
          "hasMore": false, 
          "errmsg": "ok", 
          "userlist": [
                  {
                          "unionid": "oOGjuVxVlsVceEWd2gpw0wiEiE", 
                          "userid": "manager3378", 
                          "isBoss": false, 
                          "department": [
                                  1
                          ], 
                          "order": 176313140324010500, 
                          "isLeader": false, 
                          "active": true, 
                          "isAdmin": true, 
                          "avatar": "", 
                          "isHide": false, 
                          "jobnumber": "", 
                          "name": "杨xxx", 
                          "position": ""
                  }
          ]
  }
  ```
