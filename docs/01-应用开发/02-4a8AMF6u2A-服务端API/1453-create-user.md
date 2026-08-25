---
title: "创建用户"
source_url: "https://open.dingtalk.com/document/development/create-user"
namespace: "development"
slug: "create-user"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 通讯录管理 > 用户管理1.0(不推荐) > 创建用户"
doc_id: "nQNBzcvPNZ"
updated_at: "2026-08-25 09:36:47"
---

> Source: https://open.dingtalk.com/document/development/create-user
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 通讯录管理 > 用户管理1.0(不推荐) > 创建用户
> Updated: 2026-08-25 09:36:47

# 创建用户

调用本接口创建新用户。

> **[!IMPORTANT]**
>
> - 本接口已完成升级，后续将维持现有功能且不再新增能力。
> - 未接入的开发者建议使用新版 [创建用户](0055-user-information-creation.md)接口，已接入用户不受影响。

## 权限

服务端API是以应用维度授权的，在调用接口前，确保已经为应用添加了接口权限。

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 是 | **[!NOTE]**  不支持申请 | — |
| 第三方企业应用 | 否 | — |
| 第三方个人应用 | 否 | — |

## 基本信息

**请求方式**：POST

**请求地址**：`https://oapi.dingtalk.com/user/create`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用服务端API授权凭证，通过[获取企业内部应用的access\_token](1444-obtain-orgapp-token.md)接口获取。 |

## Body参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| userid | String | 否 | 001 | 员工唯一标识ID（不可修改），企业内必须唯一。  长度为1~64个字符，如果不传，将自动生成一个userid。 |
| isSenior | Boolean | 否 | true | 是否开启高管模式：   - **true**：开启。  开启后，手机号码对所有员工隐藏。普通员工无法对其发DING、发起钉钉免费商务电话。高管之间不受影响。 - **false**：不开启。 |
| isHide | Boolean | 否 | true | 是否号码隐藏：   - **true**：隐藏。  隐藏手机号后，手机号在个人资料页隐藏，但仍可对其发DING、发起钉钉免费商务电话。 - **false**：不隐藏。 |
| jobnumber | String | 否 | 1001 | 员工工号，对应显示到OA后台和客户端个人资料的工号栏目。  长度为0~64个字符。 |
| email | String | 否 | 1@example.com | 员工邮箱。  长度为0~64个字符。企业内必须唯一，不可重复。 |
| managerUserid | String | 否 | manager240 | 员工直属主管的userid。 |
| remark | String | 否 | 测试用户 | 备注。  长度为0~1000个字符。 |
| workPlace | String | 否 | 杭州 | 办公地点。  长度为0~50个字符。 |
| tel | String | 否 | 8646xxxx | 分机号。  长度为0~50个字符，企业内必须唯一，不可重复。 |
| mobile | String | 是 | 138xxxx0000 | 手机号码，企业内必须唯一，不可重复。 |
| position | String | 否 | 技术支持 | 职位信息。  长度为0~64个字符。 |
| positionInDepts | JSONObject | 否 | {1:技术支持} | 设置用户在每个部门下的职位。  Key是deptId，表示部门；Value是职位，表示在这个部门下的职位。 |
| department | String | 是 | [389xxxx] | 成员所属部门ID列表，多个ID之间使用英文逗号分隔。 |
| name | String | 是 | 张x | 成员名称。  长度为1~64个字符。 |
| extattr | String | 否 | {\"爱好\":\"读书\"} | 扩展属性，可以设置多种属性。  手机上最多只能显示10个扩展属性，可登录[**OA管理后台**](https://oa.dingtalk.com/index.htm#/setting#setOrgInfo)**>设置>通讯录信息**进行设置。  **查看扩展属性：**   - 链接类型扩展属性，只支持在“移动端钉钉-点击该用户头像-个人资料页”查看，点击链接可以跳转。  **[!NOTE]**  链接类型支持变量通配符自动替换，目前支持通配符有：userid，corpid。例如： `[工位地址](http://www.dingtalk.com?userid=#userid#&corpid=#corpid#)`。 - 非链接类型扩展属性，支持在“移动端钉钉/PC端钉钉-点击该用户头像-个人资料页”查看。 |
| orgEmail | String | 否 | 1@dingtalk.com | 员工的企业邮箱，如果员工已经开通了企业邮箱，接口会返回，否则会报错。 |
| orderInDepts | JSONObject | 否 | {1:1} | 在对应的部门中的排序，Map结构的json字符串。Key是部门的ID，Value是人员在这个部门的排序值。 |
| hiredDate | Number | 否 | 1599735213000 | 入职时间，Unix时间戳。 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| userid | String | 111 | 员工ID。 |
| unionId | String | vpVCWxxx | 员工的unionId。 |

## 示例

**请求示例（HTTP）**

```
POST https://oapi.dingtalk.com/user/create?access_token=ACCESS_TOKEN
```

请求正文

```
{
    "orderInDepts": "{1995:1}",
    "mobile": "138xxxx0000",
    "remark": "测试用户",
    "userid": "user1",
    "managerUserid": "manager240",
    "isHide": "true",
    "orgEmail": "1@dingtalk.com",
    "jobnumber": "1001",
    "isSenior": "true",
    "hiredDate": 1599735213000,
    "name": "张x",
    "extattr": "{\"爱好\":\"读书\"}",
    "positionInDepts": "{\"1\":\"技术支持\"}",
    "tel": "8646xxxx",
    "position": "技术支持",
    "department": "[379661095,1]",
    "email": "1@example.com",
    "workPlace": "杭州"
}
```

**请求示例（JAVA SDK）**

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/user/create");
OapiUserCreateRequest req = new OapiUserCreateRequest();
req.setUserid("user1");
req.setManagerUserid("manager240");
req.setIsSenior(true);
req.setIsHide(true);
req.setJobnumber("1001");
req.setEmail("1@example.com");
req.setRemark("测试用户");
req.setWorkPlace("杭州");
req.setTel("138xxxx0000");
req.setMobile("138xxxx0000");
req.setPosition("技术支持");
req.setDepartment("[\"1995\",\"1\"]");
req.setName("张x");
req.setExtattr("{\"爱好\":\"读书\"}");
req.setOrgEmail("1@example.com");
req.setOrderInDepts("{\"1995\":\"1\"}");
req.setHiredDate(1599735213000L);
OapiUserCreateResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

**返回示例**

```
{
    "errcode": 0,
    "errmsg": "ok",
    "userid": "user1",
    "unionId": "vpVCWvmxxxxDAodyIgiEiE"
}
```
