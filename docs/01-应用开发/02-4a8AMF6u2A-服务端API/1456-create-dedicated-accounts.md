---
title: "创建专属帐号用户"
source_url: "https://open.dingtalk.com/document/development/create-dedicated-accounts"
namespace: "development"
slug: "create-dedicated-accounts"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 通讯录管理 > 用户管理1.0(不推荐) > 创建专属帐号用户"
doc_id: "4GyKRTViVq"
updated_at: "2026-08-25 09:36:48"
---

> Source: https://open.dingtalk.com/document/development/create-dedicated-accounts
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 通讯录管理 > 用户管理1.0(不推荐) > 创建专属帐号用户
> Updated: 2026-08-25 09:36:48

# 创建专属帐号用户

调用本接口创建专属账号新用户。

> **[!IMPORTANT]**
>
> - 本接口已完成升级，后续将维持现有功能且不再新增能力。
> - 未接入的开发者推荐根据帐号类型选择使用[创建SSO企业账号](0104-create-an-sso-account.md)或者[创建钉钉自建企业账号](0106-create-dingtalk-user-created-dedicated-account.md)或者[邀请其他组织企业账号加入](0115-invite-other-organization-specific-accounts-to-join.md)接口，已接入用户不受影响。

## 使用说明

创建专属帐号用户接口，仅支持购买开通的组织使用。

## 权限

服务端API是以应用维度授权的，在调用接口前，确保已经为应用添加了接口权限。

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 是 | **[!NOTE]**  不支持新增 | — |
| 第三方企业应用 | 否 | — |
| 第三方个人应用 | 否 | — |

## 基本信息

**请求方式**：POST

**请求地址**：`https://oapi.dingtalk.com/topapi/v2/user/create`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | BE3xxxx | 调用该接口的访问凭证，通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 |

## Body参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| userid | String | 否 | zhangsan | 员工唯一标识ID（不可修改），企业内必须唯一。  长度为1~64个字符，如果不传，将自动生成一个userid。 |
| name | String | 是 | 张三 | 员工名称，长度最大80个字符。 |
| dept\_id\_list | String | 是 | "2,3,4" | 所属部门ID列表，多个部门ID使用`英文,`隔开，每次调用最多传100个部门ID。 |
| telephone | String | 否 | 010-86123456-2345 | 分机号，长度最大50个字符。  **[!NOTE]**  分机号是唯一的，企业内不能重复。 |
| job\_number | String | 否 | 4 | 员工工号，长度最大为50个字符。 |
| title | String | 否 | 技术总监 | 职位，长度最大为200个字符。 |
| email | String | 否 | test@xxx.com | 员工个人邮箱，长度最大50个字符。  **[!NOTE]**  员工邮箱是唯一的，企业内不能重复。 |
| org\_email | String | 否 | test@xxx.com | 员工的企业邮箱，长度最大100个字符。  **[!NOTE]**  需满足以下条件，此字段才生效：员工已开通企业邮箱。 |
| org\_email\_type | String | 否 | profession | 员工的企业邮箱类型。   - **profession:** 标准版 - **base：**基础版 |
| work\_place | String | 否 | 未来park | 办公地点，长度最大100个字符。 |
| remark | String | 否 | 备注备注 | 备注，长度最大2000个字符。 |
| dept\_order\_list | Object[] | 否 |  | 员工在对应的部门中的排序。 |
| dept\_id | Number | 否 | 2 | 部门ID。 |
| order | Number | 否 | 1 | 员工在部门中的排序，数值越小，排序越靠前。 |
| dept\_title\_list | Object[] | 否 |  | 员工在对应的部门中的职位。 |
| dept\_id | Number | 否 | 2 | 部门ID。 |
| title | String | 否 | 资深产品经理 | 员工在部门中的职位。 |
| extension | String | 否 | {"爱好":"旅游","年龄":"24"} | 扩展属性，可以设置多种属性，最大长度2000个字符。  **[!NOTE]**     - 手机上最多只能显示10个扩展属性。 - 在使用该参数前，需要先在[OA管理后台](https://oa.dingtalk.com/index_new.htm#/setting/contactInfo)增加该属性，然后再调用接口进行赋值。 - 该字段的值支持链接类型填写，同时链接支持变量通配符自动替换，目前支持通配符有：userid，corpid。例如： {"爱好":"[爱好](http://www.dingtalk.com?userid=#userid#&corpid=#corpid#)"} |
| senior\_mode | Boolean | 否 | false | 是否开启高管模式，默认值false。   - **true**：开启。  **[!NOTE]**      - 开启后，手机号码对所有员工隐藏。   - 普通员工无法对其发DING、发起钉钉商务电话。   - 高管之间可以发DING、发起钉钉商务电话。 - **false**：不开启。 |
| hired\_date | Number | 否 | 1597573616828 | 入职时间，Unix时间戳，单位毫秒。 |
| manager\_userid | String | 否 | 001 | 直属主管的userId。 |
| exclusive\_account | Boolean | 是 | false | 是否专属帐号。   - **true**：不能指定**loginEmail**或**mobile**。 - **false**：是否创建专属帐号   **[!NOTE]**  仅适用于专属帐号。 |
| exclusive\_account\_type | String | 否 | dingtalk | 专属帐号类型。   - **sso**：企业自建专属帐号， - **dingtalk**：钉钉自建专属帐号   **[!NOTE]**     - 仅适用于专属帐号。 - 如果不传，默认为sso。 |
| login\_id | String | 否 | login\_id3 | 钉钉自建专属帐号的登录名。  **[!NOTE]**     - 仅适用于自建专属账号。 - 当入参账号类型exclusive\_account\_type传dingtalk时，该参数必填。 |
| init\_password | String | 否 | init\_password220 | 钉钉自建专属帐号的初始密码。  **[!NOTE]**     - 初始密码至少8个字符 - 不能全是字母或者数字 - 当入参账号类型exclusive\_account\_type传dingtalk时，该参数必填。 |
| exclusive\_mobile | String | 否 | +86-13412341234 | 专属帐号手机号。  **[!NOTE]**  仅适用于专属帐号。 |
| outer\_exclusive\_corpid | String | 否 | ding12345 | 需要添加的专属帐号所属corpId。  **[!NOTE]**  仅适用于邀请其他组织创建的专属账号加入本组织。 |
| outer\_exclusive\_userid | String | 否 | user01 | 需要添加的专属帐号所属userId。  **[!NOTE]**  仅适用于邀请其他组织创建的专属账号加入本组织。 |
| avatarMediaId | String | 否 | @lALPDfmVUw19YdrNA-jNA-g | 创建本组织专属帐号时可指定头像MediaId，只支持jpg/png。  可调用[上传媒体文件](https://open.dingtalk.com/document/app/upload-media-files#topic-1936786)接口获取。  **[!NOTE]**  仅适用于专属帐号。 |
| nickname | String | 否 | 昵称 | 创建本组织专属帐号时可指定昵称。  **[!NOTE]**  仅适用于专属帐号。 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| errcode | Number | 0 | 错误码。0代表成功。 |
| errmsg | String | ok | 错误信息。 |
| result | Object |  | 返回结果。 |
| userid | String | zhangsan | 员工id。 |
| unionId | String | xxxx | 员工唯一id。 |

## 示例

**请求示例（HTTP）**

```
POST https://oapi.dingtalk.com/topapi/v2/user/create?access_token=ACCESS_TOKEN
```

请求正文

```
{
        "exclusive_account_type":"dingtalk",
        "extension":"{\"爱好\":\"旅游\",\"年龄\":\"24\"}",
        "exclusive_account":"false",
        "manager_userid":"001",
        "outer_exclusive_userid":"需要添加的专属帐号所属userid",
        "outer_exclusive_corpid":"需要添加的专属帐号所属corpid",
        "remark":"备注备注",
        "title":"技术总监",
        "hired_date":"1597573616828",
        "userid":"zhangsan",
        "org_email_type":"profession",
        "work_place":"未来park",
        "dept_order_list":{
                "dept_id":"2",
                "order":"1"
        },
        "senior_mode":"false",
        "dept_id_list":"\"2,3,4\"",
        "job_number":"4",
        "email":"test@xxx.com",
        "login_id":"login_id3",
        "telephone":"010-86123456-2345",
        "dept_title_list":{
                "dept_id":"2",
                "title":"资深产品经理"
        },
        "org_email":"test@xxx.com",
        "name":"张三",
        "exclusive_mobile":"+86-13412341234",
        "init_password":"init_password220"
}
```

**请求示例（JAVA SDK）**

```
public class Main {
    public static void main(String[] args) {
        try {
            DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/v2/user/create");
                        OapiV2UserCreateRequest req = new OapiV2UserCreateRequest();
                        OapiV2UserCreateResponse rsp = client.execute(req, "");
                        System.out.println(rsp.getBody());
        } catch (ApiException e) {
            e.printStackTrace();
        }
    }
}
```

**返回示例**

```
{
        "errcode":"0",
        "result":{
                "unionId":"xxxx",
                "userid":"zhangsan"
        },
        "errmsg":"ok"
}
```

## 关于extension参数的使用

如果想要展示扩展字段**extension**中设置的用户属性，您还需要完成以下操作。

1. 登录[企业管理后台](https://login.dingtalk.com/)**。**
2. 单击内部通讯录设置，然后单击**通讯录信息**，单击新增字段。![extension](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0807377361/p358455.png)
