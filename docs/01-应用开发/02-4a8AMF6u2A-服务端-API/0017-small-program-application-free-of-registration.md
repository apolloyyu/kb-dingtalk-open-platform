---
title: "企业内部小程序免登"
source_url: "https://open.dingtalk.com/document/development/small-program-application-free-of-registration"
namespace: "development"
slug: "small-program-application-free-of-registration"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "认证与授权 > 身份验证（免登） > 使用教程 > 企业内部应用 > 企业内部小程序免登"
doc_id: "0btNjCav6Z"
updated_at: "2026-09-10 14:32:56"
---

> Source: https://open.dingtalk.com/document/development/small-program-application-free-of-registration
> Path: 应用开发 / 服务端 API / 认证与授权 > 身份验证（免登） > 使用教程 > 企业内部应用 > 企业内部小程序免登
> Updated: 2026-09-10 14:32:56

# 企业内部小程序免登

基于钉钉统一身份认证体系，实现“一次登录、处处通行”的无缝企业级体验。零感知登录、企业级安全、快速集成。

## **概述**

### 业务背景

在企业数字化办公场景中，员工需要频繁访问各类内部业务系统（如OA审批、CRM、HR系统等）。传统账号密码登录方式存在显著弊端：

- **用户体验差：**每次访问需输入凭证，操作繁琐。
- **安全风险高：**密码易泄露或被暴力破解。
- **维护成本高：**忘记密码重置、账号同步增加IT负担。
- **效率低下：**登录流程打断工作流，影响业务连续性。

### 核心价值

- **零感知登录：**打开应用自动认证，无需输入任何凭证；
- **企业级安全：**依托OAuth2.0协议，确保验证可靠；
- **快速集成：**标准化API接口，降低开发门槛；
- **统一管理：**与通讯录深度打通，权限自动配置；

### **适用场景**

本文档适用于具备服务端开发能力的钉钉开发者，用于实现企业内部应用在钉钉小程序环境下的免登功能。需熟悉前端小程序开发及后端接口调用流程。

## **使用场景**

### **零售行业**

- **门店管理：**店员快速进入库存查询、销售录入。
- **会员平台：**导购一键查看客户画像。
- **巡店检查：**区域经理实时提交巡检报告。

### **制造业**

- **生产报工：**工人扫码记录工序进度。
- **设备巡检：**维修人员现场填写保养记录。
- **质量追溯：**质检员快速录入检验结果。

### **金融行业**

- **客户经理：**查看资产配置，生成建议书。
- **合规审查：**在线审核业务流程，电子签名。
- **培训考核：**完成合规课程及在线考试。

### 典型业务流程：OA审批优化

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6791209871/p1100873.png)

## 实施指南

### **前置条件**

1. 成为[钉钉开发者](../01-XOnnmGCTbn-开发指南/0006-get-developer-permissions.md)。
2. 创建[钉钉企业应用](../01-XOnnmGCTbn-开发指南/0007-create-application.md)，获取应用凭证信息 Client ID 和 Client Secret。
3. 完成[添加小程序应用](../01-XOnnmGCTbn-开发指南/0007-create-application.md)能力。

### **代码实现**

1. 调用`dd.getAuthCode`接口获取免登授权码，小程序免登可参考[小程序免登](../03-Ogu5SlPY4t-客户端-JSAPI/0006-jsapi-get-auth-code.md)。

   若在小程序中使用`dd.httpRequest`API，需将请求域名添加至【小程序开发设置 > 安全设置】中的 HTTP 可信域名列表，否则线上发布后请求将被拦截。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5179592871/p963889.png)

   ```
   dd.getAuthCode({
     success: (res) => {
       const { authCode } = res;
     },
     fail: () => {},
     complete: () => {},
   });
   ```
2. 调用[获取应用的 Access Token](0037-api-gettoken.md)接口，获取应用级别的访问凭证。
3. 根据免登授权码`code`和应用级`access_token`，调用[通过免登码获取用户信息](0024-obtain-the-userid-of-a-user-by-using-the-log-free.md)接口，获取当前用户的`userId`和`unionId`等身份信息。

> **[!NOTE]**
>
> 开发完成后必须发布应用，免登功能仅支持在钉钉客户端内运行，外部浏览器或非钉钉环境无法正常调用免登组件。

## **体验示例（Demo）**

### **前置条件**

- 已安装 Maven 3。
- 已安装 JDK 17 及以上，本示例使用 JDK 17。
- 已经下载[小程序开发工具](../06-JDICnQyZLF-开发工具/0001-miniapp-tool.md)和服务端开发工具，服务端工具可根据实际开发环境自由下载。
- 已经获取了应用的 **Client ID** 和 **Client Secret**基本凭证信息，获取方式参见[Client ID/Client Secret](../01-XOnnmGCTbn-开发指南/0001-basic-concepts-beta.md#7d9825efaadw7)说明。
- 若需在本地 PC 端调试，需开启小程序 PC 端使用能力，参见[添加小程序地址](../01-XOnnmGCTbn-开发指南/0028-add-miniapp-address.md)说明。
- 参见[配置安全域名](../01-XOnnmGCTbn-开发指南/0029-configure-secure-domain-name.md)说明，配置**重定向 URL**（本示例填写`http://127.0.0.1:8080`）及**HTTP 可信域名**（本示例填写`0.0.0.0,127.0.0.1`）。

> **[!NOTE]**
>
> 配置完成后，确保应用完成发布，否则工作台不可见，无法使用应用。

### **操作步骤**

1. 确保完成上述准备工作，满足 Demo 运行条件。
2. 你可以下载示例 [mini-app-sso.zip](https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20250604/sjjrjm/mini-app-sso.zip) Demo。

   > 解压包含两个目录：`backend`（服务端代码）和`mini-app-front`（小程序前端代码）。
3. 打开服务端开发工具，导入`backend`目录中的服务端项目。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3255361671/p1018972.png)
4. 打开`application.properties`文件，填写应用的`clientId`和`clientSecret`。

   > **注意**：请删除原字段值末尾可能存在的空格，确保配置格式正确。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3255361671/p1018974.png)
5. 启动小程序免登后端服务即可。

   > **注意**：启动前请确认 8080 端口未被其他进程占用，否则会导致服务启动失败。
6. 打开钉钉小程序开发工具，单击右上角【打开项目】，选择解压后的`mini-app-front`目录。项目类型应选择 **钉钉** 的 **企业内部应用**。
7. 单击左上角【登录以选择关联应用】，并选择已在前述步骤中完成配置的小程序应用。
8. 登录成功且应用绑定完成后，可在 IDE 模拟器中点击【免登登录】按钮进行测试。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5179592871/p963927.png)
9. 成功调用后，将在页面展示当前用户的`userId`和`unionId`等信息。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5179592871/p963934.png)
10. 测试无误后，单击右上角【上传版本】，将小程序代码上传至钉钉平台。
11. 进入对应应用详情页，依次单击**应用发布** > **版本管理与发布**。

    ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5179592871/p963945.png)
12. 单击【创建新版本】，填写版本信息，选择已上传的小程序版本，提交发布。
13. 发布完成后，你需要在钉钉工作台打开应用。

    ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5179592871/p963974.png)
14. 单击【免登登录】按钮，查看是否能正常获取用户信息。

    ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5179592871/p963975.png)

## **常见问题**

**Q：在钉钉客户端访问如果出现“网络请求失败：4”，如何解决？**

A：通常由缓存导致。请清理钉钉客户端缓存（**设置 -> 存储空间 -> 缓存数据** **->** **前往清理**，进入缓存数据页面，勾选小程序**清理小程序缓存**）。

若仍存在，检查HTTP可信域名配置及后端服务状态。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5179592871/p964661.png)
