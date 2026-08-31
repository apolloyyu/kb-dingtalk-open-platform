---
title: "常见问题"
source_url: "https://open.dingtalk.com/document/development/common-errors"
namespace: "development"
slug: "common-errors"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "通讯录管理 > 常见问题"
doc_id: "Kv55fVtVUr"
updated_at: "2026-07-02 10:35:57"
---

> Source: https://open.dingtalk.com/document/development/common-errors
> Path: 应用开发 / 服务端 API / 通讯录管理 > 常见问题
> Updated: 2026-07-02 10:35:57

# 常见问题

本文介绍了调用钉钉服务端通讯录接口时的常见错误。

- **userId和unionId的具体场景区别**

  答：userId和unionId的具体场景区别如下：

  - 用户的userid在同一企业下是全局唯一的，不会出现重复现象；
  - 用户的unionId在同一个应用服务内是全局唯一的。例如，小钉同时在三个企业内，共用了同一个第三方企业应用，通过该第三方企业应用获取小钉的信息，unionId是相同的。
  - 通过userId可以查询对应unionId，请参见[查询用户详情](0056-query-user-details.md)。反之通过unionId也查询对应的userId，请参见[根据unionid获取用户userid](0064-query-a-user-by-the-union-id.md)。
- **调用获取用户Token接口未返回corpId**

  答：调用[获取用户token](0032-obtain-user-token.md)接口出现上述问题可能原因是：在[获取登录用户的访问凭证](0029-obtain-identity-credentials.md)进行构造登录授权页面时需传上scope=openid%20corpid 授权后取到authcode再获取用户Token即可返回corpid。
- **如何获取企业全部员工信息**

  答：钉钉尚未提供获取企业全部员工信息接口，开发者可以通过以下方式获取企业全部员工信息，详细流程可参考[创建、获取、更新和删除企业员工](0048-address-book-employee-operations.md)使用案例。

  - 可以先调用[获取部门列表](0082-user-management-acquires-the-list-departments.md)接口，获取到该企业下所有部门ID。
  - 遍历调用[获取部门用户userid列表](0065-query-the-list-of-department-userids.md)接口。

    确保通讯录接口权限为**全部员工**。

    ![全部员工](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4293842061/p172140.png)
- **调用获取用户个人通讯录信息接口未返回邮箱**

  答：调用[获取用户通讯录个人信息](0054-dingtalk-retrieve-user-information.md)接口出现上述问题可能原因如下：

  在钉钉客户端-邮箱里有设置的邮箱才会返回邮箱数据（如下图所示）

  > **[!IMPORTANT]**
  >
  > 钉钉提供的邮箱（例如:xxx@dingtalk.com）不返回邮箱数据。

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7579592871/p1084673.png)
- **如何清除用户信息中部门主管**

  答：调用[更新用户信息](0057-user-information-update.md)接口清除部门主管的方式：清空部门主管传参force\_update\_fields（强制更新字段）设置dept\_manager\_userid\_list（部门主管），不要传dept\_manager\_userid\_list为空，否则会出现异常。
- **调用查询用户详情接口，无法获取用户手机号**

  答：调用[查询用户详情](0056-query-user-details.md)接口出现上述错误原因可能为：接口权限不足。

  解决方案：在[钉钉开发者后台](https://open-dev.dingtalk.com/#/)，打开该应用详情，找到接口权限入口，申请开通里面获取手机号信息的权限。

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6523897661/p513618.png)
- **关于报错“请求的用户userid/部门id不在授权范围内”的说明**

  答：调用通讯录管理相关接口出现上述错误时，请先确认当前应用是第三方企业应用还是企业内部应用。

  - 若为企业内部应用：请在开发者后台进入对应应用的权限管理界面，确认是否已经将对应的部门或人员添加到授权权限范围中。

    ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6523897661/p495834.png)
  - 若为第三方企业应用：则需要授权企业（即开通使用该应用的企业）在[钉钉管理后台](https://oa.dingtalk.com/) **> 工作台 > 应用管理**，选择对应三方应用，并点击设置按钮。在弹出的界面中，确认是否已经将对应的人员添加到可见范围中。

    ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6523897661/p510121.png)
- **调用通讯录接口报错{"errcode":50002，"errmsg": "请求的员工userid不在授权范围内"}**

  答：请求接口accessToken对应的应用，在开发者后台**权限管理**页面的授权范围内不包含该员工。

  解决方案：单击权限管理的**添加**按钮，将该用户添加到**授权人员**中。![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6523897661/p513163.png)
- **调用通讯录接口报错{"errcode":50004，"errmsg": "请求的部门id不在授权范围内"}**

  答：请求接口accessToken对应的应用，在开发者后台**权限管理**页面的授权范围内不包含该部门。

  解决方案：单击权限管理的**添加**按钮，将需要变更的部门添加到**授权人员**中。

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6523897661/p513163.png)
- **调用更新用户信息报错{"errcode":40022，"errmsg": "企业中的手机号码和登录钉钉的手机号码不一致，暂时不支持修改用户信息，可以删除后重新添加"}**

  答：调用[更新用户信息](0057-user-information-update.md)接口出现上述错误原因为：接口暂时不支持修改用户手机号，可以删除后重新添加。
- **调用根据手机号查询用户报错{"errmsg": "无权限调用"}**

  答：调用[根据手机号查询用户](0063-query-users-by-phone-number.md)接口出现上述错误原因可能为：应用版本过老（使用corpId和Corpsecret获取accessToken的应用）。

  解决方案：需要创建新应用获取。
- **调用创建用户报错{"errmsg": "系统繁忙"}**

  答：调用[创建用户](0055-user-information-creation.md)接口出现上述错误原因可能如下：

  可能是企业添加员工超出每周添加人数上限，或者是超出企业添加人数上限。
- **调用创建用户报错{"errcode": 60103，"errmsg": "手机号码不合法，如果是国际号码，请使用+xx-xxxxxx的格式"}**

  答：调用[创建用户](0055-user-information-creation.md)接口出现上述报错时，其可能原因包括但不限于以下几点：

  - 在钉钉中设置的公司地区是非中国大陆地区，若手机号为中国大陆地区，请使用+86-xxxxxx。
  - 在钉钉中设置的公司地区是中国大陆地区，若手机号为非中国大陆地区，请使用+86-xxxxxx。
- **调用创建用户返回"errcode: 40103， errmsg: 已发出邀请，对方同意后即可加入组织"**

  答：在调用[创建用户](0055-user-information-creation.md)接口邀请用户加入组织时，若出现上述返回信息，可能原因包括但不限于以下情况:

  - 命中安全规则：如果一个员工已经在认证企业A，此时B企业再添加该员工时就会有上述提示。请在客户端搜索团队邀请或者在通讯录界面查看对应的邀请信息并进行相应处理。
  - 被邀请的用户在钉钉手机客户端-我的-设置-隐私-团队与成员中启用了“团队添加我时需要验证”，开启后请在客户端搜索团队邀请或者在通讯录界面查看对应的邀请信息并进行相应处理。
  > **[!IMPORTANT]**
  >
  > 用户同意并成功加入企业后，若当天企业删除该用户，则删除后24小时内再次调用接口邀请该用户时，也会返回上述错误信息。
- **调用添加外部联系人报错{"errmsg":"系统繁忙"，"errcode":40001}**

  答：调用[添加外部联系人](0097-add-enterprise-external-contacts.md)报上述错误可能原因是企业在外部联系人里面添加了自定义字段，并且设置为必填。可以修改这个自定义字段的必填选项为“否”，或者添加外部联系人时添加此字段信息。

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7579592871/p1084676.png)
- **调用获取用户个人通讯录信息接口报"{code: Forbidden.AccessDenied.AccessTokenPermissionDenied，message: 没有调用该接口的权限}"**

  答：调用[获取用户通讯录个人信息](0054-dingtalk-retrieve-user-information.md)接口出现上述错误时，其可能原因包括但不限于以下几点：

  - 权限问题：需要检查“通讯录个人信息读权限”和“个人手机号信息”是否已申请。

    ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6523897661/p495849.png)
  - 接口凭证accessToken有误：该接口的授权凭证为个人用户的accessToken，若传入的accessToken不对也会产生上述报错。获取个人用户的accessToken步骤如下：

    **第1步**：获取authCode。浏览器访问构造出的登录授权页面地址：https://login.dingtalk.com/oauth2/auth?redirect\_uri=https%3A%2F%2Fwww.aaaaa.com%2Fa%2Fb（示例并非固定uri） //授权通过/拒绝后回调地址，确保已经添加至开发者后台对应应用中登录与分享-回调域名中。&response\_type=code //固定值为code，授权通过后返回authCode。

    &client\_id=dingbbbbbbb //应用appkey

    &scope=openid%2Bcorpid

    &state=dddd

    &prompt=consent

    用户点击进行授权后，会跳转到https://www.aaaaa.com/a/b?authCode=xxxx&state=dddd 通过该地址即可获取authCode。

    **第2步**：获取到的authCode后，通过调用[获取用户token](0032-obtain-user-token.md)获取个人用户的accessToken。详情可以查看[获取登录用户的访问凭证](0029-obtain-identity-credentials.md)。
- 调用更新/删除/查询用户报错{"errcode":60121，"errmsg":"找不到该用户"}

  答：出现上述错误时可能原因包括但不限于以下情况：

  - 传参userId（用户在企业中唯一标识）与传参access\_token（服务端API访问凭证）所对应的应用不在同一个企业。
  - 传参userId（用户在企业中唯一标识）的用户为已离职状态或待入职状态。
  - 企业邀请该用户后，用户暂未同意加入企业导致。
- **调用获取部门详情报错{ errcode:40009， success:false， errmsg:不合法的部门id}**

  答：调用[获取部门详情](0081-query-department-details0-v2.md)接口出现上述错误可能原因如下：

  传参dept\_id为-7（-7是家校通讯录部门ID），家校通讯录dept\_id=-7不支持调用通讯录管理场景文档。
- 调用更新用户信息报错{'errmsg': '修改失败，已开启智能人事职位管理，请前往「智能人事」中修改或使用「智能人事员工调岗」（https://open.dingtalk.com/document/development/intelligent-personnel-staff-transfer）'， 'errcode': 12150}

  答：调用[更新用户信息](0057-user-information-update.md)接口出现上述错误可能原因如下：

  已开启智能人事职位管理的场景，若需更新用户信息中职位（title）或部门（deptid）就需要根据[智能人事员工调岗](0954-intelligent-personnel-staff-transfer.md)来更新。
