---
title: "创建、获取、更新和删除企业员工"
source_url: "https://open.dingtalk.com/document/development/address-book-employee-operations"
namespace: "development"
slug: "address-book-employee-operations"
group: "应用开发"
tab: "服务端API"
breadcrumb: "通讯录管理 > 使用教程 > 创建、获取、更新和删除企业员工"
doc_id: "58Wi4Lt3sV"
updated_at: "2026-07-02 10:35:46"
---

> Source: https://open.dingtalk.com/document/development/address-book-employee-operations
> Path: 应用开发 / 服务端API / 通讯录管理 > 使用教程 > 创建、获取、更新和删除企业员工
> Updated: 2026-07-02 10:35:46

# 创建、获取、更新和删除企业员工

本文介绍了创建一个企业内部应用，使用通讯录管理提供的用户管理相关API，实现创建、获取、更新和删除企业员工等。

## **预期效果**

用户信息界面如下图所示：

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1378516661/p505603.png)

## **接入流程简介**

本文介绍了创建一个企业内部应用，使用**通讯录管理**提供的**用户管理**相关API，实现创建、获取、更新和删除企业员工等。

步骤一：获取应用凭证信息，获取应用 Client ID 和 Client Secret。

步骤二：申请接口权限，申请通讯录管理相关接口权限。

步骤三：获取应用访问凭证[获取企业内部应用的access\_token](1444-obtain-orgapp-token.md)。调用接口时，通过accessToken鉴权调用者身份。

步骤四：调用通讯录相关API：

1. 调用服务端API-[创建用户](0055-user-information-creation.md)接口，实现用户创建。获取用户`userid`。

   - 如果员工添加到根部门，接口参数传1即可。本示例采用添加员工至根部门。
   - 如果员工添加到某个部门下，先调用[获取子部门ID列表](0083-obtain-the-list-of-sub-department-ids.md)接口获取部门ID，作为创建用户接口的部门参数。
2. 根据用户`userid`信息，调用服务端API-[查询用户详情](0056-query-user-details.md)接口，获取用户详细信息。
3. 根据用户`userid`信息，调用服务端API-[更新用户信息](0057-user-information-update.md)接口，实现更新用户信息。
4. 根据用户`userid`信息，调用服务端API-[删除用户](0058-delete-a-user.md)接口，实现删除用户信息。

## **前提条件**

完成[应用创建与配置](../01-XOnnmGCTbn-开发指南/0007-create-application.md)的流程。

## **步骤一：获取应用凭证**

1. 选择目标应用，进入应用详情页，单击**基础信息** > **凭证与基础信息**。
2. 获取应用 Client ID 和 Client Secret。

## 步骤二：添加接口权限

单击**开发配置** > **权限管理**，在权限搜索框中输入`qyapi_manage_addresslist`和`qyapi_get_department_list`，并申请权限。

## 步骤三：获取应用访问凭证accessToken

> **[!IMPORTANT]**
>
> - 服务端API差异详情参见[新版API VS 旧版API](0002-download-the-server-side-sdk.md#section-8lr-id4-rbz)。
> - 服务端API接口SDK下载，详情参见[服务端SDK下载](0002-download-the-server-side-sdk.md)。

根据步骤一中的 Client ID 和 Client Secret，获取应用访问凭证[获取企业内部应用的access\_token](1444-obtain-orgapp-token.md)。

```
public void getAccessToken() throws ApiException {
        DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/gettoken");
        OapiGettokenRequest req = new OapiGettokenRequest();
        req.setAppkey("dingxxxxxxxxxhgn");
        req.setAppsecret("9G_xxxxxxxxxxxxxxx1JDf0Qq3nexxxxxxxxGIO");
        req.setHttpMethod("GET");
        OapiGettokenResponse rsp = client.execute(req);
        System.out.println(rsp.getBody());
    }
```

## **步骤四：调用通讯录相关API**

1. 调用服务端API-[创建用户](0055-user-information-creation.md)接口，实现用户创建。获取用户`userid`。

   ```
   public void createUser() throws ApiException {
           DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/v2/user/create");
           OapiV2UserCreateRequest req = new OapiV2UserCreateRequest();
           req.setUserid("manger7676");
           req.setName("1009测试用户");
           req.setSeniorMode(false);
           req.setMobile("152****3025");
           req.setTitle("技术总监");
           req.setEmail("test*****@xx.com");
           req.setOrgEmail("test***@xxx.com");
           req.setOrgEmailType("profession");
           ArrayList<OapiV2UserCreateRequest.DeptTitle> deptTitles = new ArrayList<>();
           OapiV2UserCreateRequest.DeptTitle deptTitle = new OapiV2UserCreateRequest.DeptTitle();
           deptTitle.setDeptId(724960197L);
           deptTitle.setTitle("资深技术总监");
           deptTitles.add(deptTitle);
           req.setDeptTitleList(deptTitles);
           req.setHideMobile(false);
           req.setTelephone("010-8xxxxx6-2345");
           req.setJobNumber("202210190001");
           req.setHiredDate(1666143772000L);
           req.setWorkPlace("阿里中心******");
           req.setRemark("备注信息");
           req.setDeptIdList("724960197");
           List<OapiV2UserCreateRequest.DeptOrder> deptOrderList = new ArrayList<OapiV2UserCreateRequest.DeptOrder>();
           OapiV2UserCreateRequest.DeptOrder deptOrder = new OapiV2UserCreateRequest.DeptOrder();
           deptOrder.setDeptId(724960197L);
           deptOrder.setOrder(1L);
           deptOrderList.add(deptOrder);
           req.setDeptOrderList(deptOrderList);
           req.setExtension("{\"爱好\":\"[爱好](http://test.com?userid=#userid#&corpid=#corpid#)\"}");
           req.setManagerUserid("manager7676");
           req.setLoginEmail("test****@xxx.com");
           OapiV2UserCreateResponse rsp = client.execute(req, "access_token");
           System.out.println(rsp.getBody());
       }
   ```

   - 如果员工添加到根部门，接口参数传1即可。本示例采用添加员工至根部门。
   - 如果员工添加到某个部门下，先调用[获取子部门ID列表](0083-obtain-the-list-of-sub-department-ids.md)接口获取部门ID，作为创建用户接口的部门参数。

   ```
   public void departmentListSubId() throws ApiException {
           DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/v2/department/listsubid");
           OapiV2DepartmentListsubidRequest req = new OapiV2DepartmentListsubidRequest();
           req.setDeptId(1L);
           OapiV2DepartmentListsubidResponse rsp = client.execute(req, "access_token");
           System.out.println(rsp.getBody());
       }
   ```
2. 根据用户`userid`信息，调用服务端API-[查询用户详情](0056-query-user-details.md)接口，获取用户详细信息。

   > **[!NOTE]**
   >
   > 获取用户详情返回的部分字段有一定要求，请参考[查询用户详情](0056-query-user-details.md)接口文档返回字段的描述。

   ```
    public void userInfo() throws ApiException {
           DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/v2/user/get");
           OapiV2UserGetRequest req = new OapiV2UserGetRequest();
           req.setUserid("manger7676");
           req.setLanguage("zh_CN");
           OapiV2UserGetResponse rsp = client.execute(req, "access_token");
           System.out.println(rsp.getBody());
       }
   ```
3. 根据用户`userid`信息，调用服务端API-[更新用户信息](0057-user-information-update.md)接口，实现更新用户信息。

   > **[!NOTE]**
   >
   > 更新用户信息接口，暂时不支持更新手机号。

   ```
   public void userModify() throws ApiException {
           DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/v2/user/update");
           OapiV2UserUpdateRequest req = new OapiV2UserUpdateRequest();
           req.setUserid("manger7676");
           req.setName("小钉");
           req.setHideMobile(false);
           req.setTelephone("010-86*****6-2345");
           req.setJobNumber("202210190002");
           req.setTitle("技术总监");
           req.setEmail("test*****@xxx.com");
           req.setWorkPlace("未来park");
           req.setRemark("备注备注");
           req.setDeptIdList("1");
           List<OapiV2UserUpdateRequest.DeptOrder> list2 = new ArrayList<OapiV2UserUpdateRequest.DeptOrder>();
           OapiV2UserUpdateRequest.DeptOrder obj3 = new OapiV2UserUpdateRequest.DeptOrder();
           list2.add(obj3);
           obj3.setDeptId(1L);
           obj3.setOrder(1L);
           req.setDeptOrderList(list2);
           req.setExtension("{\"爱好\":\"旅游\",\"年龄\":\"24\"}");
           req.setSeniorMode(false);
           req.setHiredDate(1633017600000L);
           req.setLanguage("zh_CN");
           OapiV2UserUpdateResponse rsp = client.execute(req, "access_token");
           System.out.println(rsp.getBody());
       }
   ```
4. 根据用户`userid`信息，调用服务端API-[删除用户](0058-delete-a-user.md)接口，实现删除用户信息。

   ```
   public void userDelete() throws ApiException {
           DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/v2/user/delete");
           OapiV2UserDeleteRequest req = new OapiV2UserDeleteRequest();
           req.setUserid("manager7676");
           OapiV2UserDeleteResponse rsp = client.execute(req, "access_token");
           System.out.println(rsp.getBody());
       }
   ```
