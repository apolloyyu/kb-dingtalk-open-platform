---
title: "创建、获取、更新和删除企业部门"
source_url: "https://open.dingtalk.com/document/development/operations-related-to-address-book-departments"
namespace: "development"
slug: "operations-related-to-address-book-departments"
group: "应用开发"
tab: "服务端API"
breadcrumb: "通讯录管理 > 使用教程 > 创建、获取、更新和删除企业部门"
doc_id: "Rqv5HvWlb3"
updated_at: "2026-07-30 10:03:06"
---

> Source: https://open.dingtalk.com/document/development/operations-related-to-address-book-departments
> Path: 应用开发 / 服务端API / 通讯录管理 > 使用教程 > 创建、获取、更新和删除企业部门
> Updated: 2026-07-30 10:03:06

# 创建、获取、更新和删除企业部门

本文介绍了创建一个企业内部应用，使用通讯录管理提供的部门管理相关API，实现创建、获取、更新和删除企业部门等。

## **预期效果**

部门信息展示如下图所示：

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6177616661/p505647.png)

## **接入流程简介**

1. 获取应用凭证信息，获取应用 Client ID 和 Client Secret。
2. 申请接口权限，申请通讯录管理相关接口权限。
3. 获取应用访问凭证[获取企业内部应用的access\_token](1444-obtain-orgapp-token.md)。调用接口时，通过accessToken鉴权调用者身份。
4. 调用通讯录相关API：

   1. 调用服务端API-[创建部门](0077-address-book-creation-department-established-department.md)接口，实现创建部门，获取部门`dept_id`**。**

      - 如果创建根部门的子部门，参数parent\_id传1。本示例采用创建根部门下的子部门。
      - 如果创建的是其他部门的子部门，需要先调用[获取部门列表](0082-user-management-acquires-the-list-departments.md)接口，获取的部门ID作为parent\_id的值。
   2. 根据部门`dept_id`，调用服务端API-[获取部门详情](0081-query-department-details0-v2.md)接口，获取部门详情信息。
   3. 根据部门`dept_id`，调用服务端API-[更新部门](0078-address-book-update-department.md)接口，实现更新部门信息。
   4. 根据部门`dept_id`，调用服务端API-[删除部门](0079-address-book-deletion-department.md)接口，实现删除部门信息。

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

1. 调用服务端API-[创建部门](0077-address-book-creation-department-established-department.md)接口，实现创建部门，获取部门`dept_id`**。**

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
           OapiV2DepartmentCreateResponse rsp = client.execute(req, "access_token");
           System.out.println(rsp.getBody());
       }
   ```

   - 如果创建根部门的子部门，参数parent\_id传1。本示例采用创建根部门下的子部门。
   - 如果创建的是其他部门的子部门，需要先调用[获取部门列表](0082-user-management-acquires-the-list-departments.md)接口，获取的部门ID作为parent\_id的值。

     ```
     public void departmentList() throws ApiException {
             DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/v2/department/listsub");
             OapiV2DepartmentListsubRequest req = new OapiV2DepartmentListsubRequest();
             req.setDeptId(1L);
             req.setLanguage("zh_CN");
             OapiV2DepartmentListsubResponse rsp = client.execute(req, "access_token");
             System.out.println(rsp.getBody());
         }
     ```
2. 根据部门`dept_id`，调用服务端API-[获取部门详情](0081-query-department-details0-v2.md)接口，获取部门详情信息。

   ```
   public void deptInfo() throws ApiException {
           DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/v2/department/get");
           OapiV2DepartmentGetRequest req = new OapiV2DepartmentGetRequest();
           req.setDeptId(724960197L);
           req.setLanguage("zh_CN");
           OapiV2DepartmentGetResponse rsp = client.execute(req, "access_token");
           System.out.println(rsp.getBody());
       }
   ```
3. 根据部门`dept_id`，调用服务端API-[更新部门](0078-address-book-update-department.md)接口，实现更新部门信息。

   ```
   public void deptModify() throws ApiException {
           DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/v2/department/update");
           OapiV2DepartmentUpdateRequest req = new OapiV2DepartmentUpdateRequest();
           req.setDeptId(724960197L);
           req.setParentId(1L);
           req.setOuterDept(true);
           req.setHideDept(false);
           req.setCreateDeptGroup(true);
           req.setOrder(1L);
           req.setName("1019部门测试");
           req.setSourceIdentifier("1019部门测试");
           req.setOuterPermitUsers("manager7675,01472825524039877041");
           req.setOuterDeptOnlySelf(true);
           req.setLanguage("zh_CN");
           req.setAutoAddUser(true);
           req.setAutoApproveApply(true);
           req.setOrgDeptOwner("manager7675");
           OapiV2DepartmentUpdateResponse rsp = client.execute(req, "access_token");
           System.out.println(rsp.getBody());
       }
   ```
4. 根据部门`dept_id`，调用服务端API-[删除部门](0079-address-book-deletion-department.md)接口，实现删除部门信息。

   ```
    public void deptDelete() throws ApiException {
           DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/v2/department/delete");
           OapiV2DepartmentDeleteRequest req = new OapiV2DepartmentDeleteRequest();
           req.setDeptId(724960197L);
           OapiV2DepartmentDeleteResponse rsp = client.execute(req, "access_token");
           System.out.println(rsp.getBody());
       }
   ```

   > **[!NOTE]**
   >
   > - 当前部门内有成员或者该部门的子部门内有成员，不允许删除的。
   > - 当前部门及其所有子部门都会被删除。
   > - 部门删除后，对应的部门群会自动解散。
