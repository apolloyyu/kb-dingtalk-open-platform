---
title: "更新用户信息"
source_url: "https://open.dingtalk.com/document/development/update-user-details"
namespace: "development"
slug: "update-user-details"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "历史文档（不推荐） > 通讯录管理 > 用户管理1.0(不推荐) > 更新用户信息"
doc_id: "zP8p6VMbMO"
updated_at: "2026-08-25 09:36:49"
---

> Source: https://open.dingtalk.com/document/development/update-user-details
> Path: 应用开发 / 服务端 API / 历史文档（不推荐） > 通讯录管理 > 用户管理1.0(不推荐) > 更新用户信息
> Updated: 2026-08-25 09:36:49

# 更新用户信息

调用本接口更新用户详情。

> **[!IMPORTANT]**
>
> - 本接口已完成升级，后续将维持现有功能且不再新增能力。
> - 未接入的开发者建议使用新版 [更新用户信息](0057-user-information-update.md)接口，已接入用户不受影响。

## 权限

服务端API是以应用维度授权的，在调用接口前，确保已经为应用添加了接口权限。

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 是 | **[!NOTE]**  不支持新增 | — |
| 第三方企业应用 | 否 | — |
| 第三方个人应用 | 否 | — |

## 基本信息

**请求方式**：POST

**请求地址**：`https://oapi.dingtalk.com/user/update`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用服务端API授权凭证，通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 |

## Body参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| userid | String | 是 | 1001 | 员工userid，不可修改，长度为1~64个字符，可通过[根据手机号查询用户](1465-retrieve-userid-from-mobile-phone-number.md)接口获取。 |
| name | String | 否 | 赵xx | 员工姓名，长度为1~64个字符。 |
| managerUserid | String | 否 | user01 | 员工直属主管的userid。 |
| workPlace | String | 否 | 杭州 | 办公地点，长度为0~50个字符。 |
| remark | String | 否 | 测试用户 | 备注，长度为0~1000个字符。 |
| isSenior | Boolean | 否 | true | 是否开启高管模式：   - **true**：开启  开启后，手机号码对所有员工隐藏。普通员工无法对其发DING、发起钉钉免费商务电话。高管之间不受影响。 - **false**：不开启 |
| orgEmail | String | 否 | 1@dingtalk.com | 员工的企业邮箱。 |
| tel | String | 否 | 8646xxxx | 分机号，长度为0~50个字符。 |
| orderInDepts | JSONObject | 否 | {1:1} | 在对应的部门中的排序，Map结构的json字符串。Key是部门的ID，Value是人员在这个部门的排序值。 |
| department | List[] | 否 | [1] | 成员所属部门ID列表。 |
| email | String | 否 | 1@example.com | 员工邮箱。  长度为0~64个字符。企业内必须唯一，不可重复。 |
| managerUserid | String | 否 | manager240 | 员工直属主管的userid。 |
| position | String | 否 | 技术支持 | 职位信息。  长度为0~64个字符。 |
| positionInDepts | JSONObject | 否 | {\"1\":\"技术支持\"} | 设置用户在每个部门下的职位。  Key是deptId，表示部门ID；Value是职位，表示在这个部门下的职位。 |
| extattr | String | 否 | {\"爱好\":\"读书\"} | 扩展属性。  **[!IMPORTANT]**   - 手机上最多只能显示10个扩展属性，可登录[**OA管理后台**](https://oa.dingtalk.com/index.htm#/setting#setOrgInfo)**>设置>通讯录信息**进行设置。 - 如果给员工设置有10个扩展属性字段，更新时即使扩展属性字段值没变，也必须要将10个扩展属性字段都传进去。如果只传其中1个，那么剩下9个字段都会被清空。  **查看扩展属性：**   - 链接类型扩展属性，只支持在“移动端钉钉-点击该用户头像-个人资料页”查看，点击链接可以跳转。  **[!NOTE]**  链接类型支持变量通配符自动替换，目前支持通配符有：userid，corpid。例如： `[工位地址](http://www.dingtalk.com?userid=#userid#&corpid=#corpid#)`。 - 非链接类型扩展属性，支持在“移动端钉钉/PC端钉钉-点击该用户头像-个人资料页”查看 |
| jobnumber | String | 否 | 1001 | 员工工号，对应显示到OA后台和客户端个人资料的工号栏目。  长度为0~64个字符。 |
| isHide | Boolean | 否 | true | 是否号码隐藏：   - **true**：隐藏  隐藏手机号后，手机号在个人资料页隐藏，但仍可对其发DING、发起钉钉免费商务电话。 - **false**：不隐藏 |
|  |  |  |  |  |
| lang | String | 否 | zh\_CN | 通讯录语言，默认zh\_CN。如果是英文，请输入en\_US。 |
| hiredDate | Number | 否 | 1599735213000 | 入职时间，Unix时间戳。 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |

## 示例

**请求示例（HTTP）**

```
POST https://oapi.dingtalk.com/user/update?access_token=ACCESS_TOKEN
```

请求正文

```
{
    "orderInDepts": "{\"1995\":\"1\"}",
    "isSenior": "true",
    "hiredDate": 1599735213000,
    "name": "测试回调",
    "extattr": "{\"爱好\":\"读书\"}",
    "positionInDepts": "{\"1995\":\"技术支持\"}",
    "remark": "测试用户",
    "tel": "8646xxxx",
    "position": "技术支持",
    "department": [
        1995
    ],
    "userid": "2022",
    "managerUserid": "user01"
}
```

**请求示例（JAVA SDK）**

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/user/update");
OapiUserUpdateRequest req = new OapiUserUpdateRequest();
req.setUserid("user12331");
req.setManagerUserid("10203029011219896");
req.setName("测试回调");
req.setRemark("测试用户");
req.setIsSenior(true);
req.setTel("15023229144");
req.setOrderInDepts("{\"1995\":\"1\"}");
req.setDepartment(Arrays.asList(1995L));
req.setPosition("技术支持");
req.setExtattr("{\"爱好\":\"读书\"}");
req.setHiredDate(1599735213000L);
req.setPositionInDepts("{\"1995\":\"技术支持\"}");
OapiUserUpdateResponse rsp = client.execute(req, access_token);
 System.out.println(rsp.getBody());
```

**返回示例**

```
{
    "errcode": 0,
    "errmsg": "ok"
}
```
