---
title: "企业OA系统与钉钉通讯录实现同步"
source_url: "https://open.dingtalk.com/document/development/synchronization-between-enterprise-oa-system-and-dingtalk-address-book"
namespace: "development"
slug: "synchronization-between-enterprise-oa-system-and-dingtalk-address-book"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "通讯录管理 > 使用教程 > 企业OA系统与钉钉通讯录实现同步"
doc_id: "uYLZbIXHIn"
updated_at: "2026-07-02 10:35:50"
---

> Source: https://open.dingtalk.com/document/development/synchronization-between-enterprise-oa-system-and-dingtalk-address-book
> Path: 应用开发 / 服务端 API / 通讯录管理 > 使用教程 > 企业OA系统与钉钉通讯录实现同步
> Updated: 2026-07-02 10:35:50

# 企业OA系统与钉钉通讯录实现同步

本文档介绍说明如何实现企业自有OA系统通讯录与钉钉通讯录同步。

## **前提条件**

完成[应用创建与配置](../01-XOnnmGCTbn-开发指南/0007-create-application.md)的流程。

## **步骤一：获取应用凭证**

1. 选择目标应用，进入应用详情页，单击**基础信息** > **凭证与基础信息**。
2. 获取应用 Client ID 和 Client Secret。

## **步骤二：添加接口权限**

单击**开发配置** > **权限管理**，在权限搜索框中输入`qyapi_manage_addresslist`，并申请权限。

## 步骤三：获取应用访问凭证accessToken

> **[!IMPORTANT]**
>
> - 服务端API差异详情参见[新版API VS 旧版API](0002-download-the-server-side-sdk.md#section-8lr-id4-rbz)。
> - 服务端API接口SDK下载，详情参见[服务端SDK下载](0002-download-the-server-side-sdk.md)。

根据步骤一中 的 Client ID 和 Client Secret，获取应用访问凭证[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)。

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

## 步骤四：通讯录同步相关流程

1. 钉钉通讯录信息同步到企业OA系统通讯录：

   实现同步的关键在于钉钉通讯录内的信息有相关变动，要同时保证企业OA系统通讯录也有响应的操作。

   1. 先参考[创建、获取、更新和删除企业员工](0048-address-book-employee-operations.md)文档，把当前钉钉组织架构信息全部获取到企业OA系统通讯录内。
   2. 使用钉钉提供的[事件订阅](0014-event-subscription-overview.md)功能，并订阅通讯录事件，钉钉通讯录内的变动会对应推送相关的回调事件信息。通讯录事件推送信息格式参考[通讯录](../04-LFcRvVD08N-事件订阅/0002-org-event-overview.md#ab90dc1084bai)。![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8875958071/p769119.png)
   3. 企业OA系统，接收并处理钉钉推送的通讯录事件，同步更新企业OA系统的通讯录信息。
2. 企业OA系统通讯录信息更新到钉钉通讯录：

   当企业OA系统通讯录的信息发生变动，需要同步更新钉钉通讯录信息，确保通讯录信息一致。

   1. 企业OA系统通讯录内创建了部门，调用[创建部门](0077-address-book-creation-department-established-department.md)接口，根据企业自有OA系统内该部门层级和部门名称，在钉钉客户端内创建同样的部门层级和部门名称。

      ```
       public void deptCreate() throws ApiException {
              DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/v2/department/create");
              OapiV2DepartmentCreateRequest req = new OapiV2DepartmentCreateRequest();
              req.setParentId(1L);
              req.setOuterDept(true);
              req.setHideDept(false);
              req.setCreateDeptGroup(true);
              req.setOrder(1L);
              req.setName("1019部门测试");
              req.setSourceIdentifier("1019部门测试");
              req.setOuterPermitUsers("manager7675,01472825524039877041");
              req.setOuterDeptOnlySelf(true);
              OapiV2DepartmentCreateResponse rsp = client.execute(req, getAccessToken());
              System.out.println(rsp.getBody());
          }
      ```

      > **[!NOTE]**
      >
      > 钉钉通讯录的部门ID是自动生成的，不支持设置。在进行通讯录更新时，建议以部门名称作为标识同步到钉钉，并同时保存对应的钉钉通讯录的部门ID值，便于后续操作使用。
   2. 企业OA系统通讯录添加角色，根据企业OA系统内的角色信息。

      1. 调用服务端API-[创建角色组](0091-add-a-role-group.md)接口，创建角色组信息。

         ```
         public void addRoleGroup() throws ApiException {
                 DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/role/add_role_group");
                 OapiRoleAddrolegroupRequest req = new OapiRoleAddrolegroupRequest();
                 req.setName("1019测试角色组");
                 OapiRoleAddrolegroupResponse rsp = client.execute(req, getAccessToken());
                 System.out.println(rsp.getBody());
             }
         ```
      2. 调用服务端API-[创建角色](0086-address-book-add-role.md)接口，创建企业角色信息。

         ```
           public void addRole() throws ApiException {
                 DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/role/add_role");
                 OapiRoleAddRoleRequest req = new OapiRoleAddRoleRequest();
                 req.setRoleName("1019测试角色");
                 req.setGroupId(3168010875L);
                 OapiRoleAddRoleResponse rsp = client.execute(req, getAccessToken());
                 System.out.println(rsp.getBody());
             }
         ```
   3. 调用[创建用户](0055-user-information-creation.md)接口，把企业OA系统内各个部门内的员工创建添加到钉钉对应的部门内，本步骤添加用户的同时，可以同时添加该员工的角色信息。

      ```
      public void createUser() throws ApiException {
              DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/v2/user/create");
              OapiV2UserCreateRequest req = new OapiV2UserCreateRequest();
              req.setUserid("manger7666");
              req.setName("1009测试用户");
              req.setSeniorMode(false);
              req.setMobile("152****3025");
              req.setTitle("技术总监");
              req.setEmail("test***@xx.com");
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
              req.setWorkPlace("阿里中心****");
              req.setRemark("备注信息");
              req.setDeptIdList("724960197");
              List<OapiV2UserCreateRequest.DeptOrder> deptOrderList = new ArrayList<OapiV2UserCreateRequest.DeptOrder>();
              OapiV2UserCreateRequest.DeptOrder deptOrder = new OapiV2UserCreateRequest.DeptOrder();
              deptOrder.setDeptId(724960197L);
              deptOrder.setOrder(1L);
              deptOrderList.add(deptOrder);
              req.setDeptOrderList(deptOrderList);
              req.setExtension("{\"爱好\":\"[爱好](http://test.com?userid=#userid#&corpid=#corpid#)\"}");
              req.setManagerUserid("manager7675");
              req.setLoginEmail("test****@xxx.com");
              OapiV2UserCreateResponse rsp = client.execute(req, getAccessToken());
              System.out.println(rsp.getBody());
          }
      ```
