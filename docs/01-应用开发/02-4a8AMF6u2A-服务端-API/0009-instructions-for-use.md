---
title: "接入流程"
source_url: "https://open.dingtalk.com/document/development/instructions-for-use"
namespace: "development"
slug: "instructions-for-use"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "API 调用指南 > 授权套件 > 接入流程"
doc_id: "i6rm6w8C7F"
updated_at: "2026-08-03 09:13:56"
---

> Source: https://open.dingtalk.com/document/development/instructions-for-use
> Path: 应用开发 / 服务端 API / API 调用指南 > 授权套件 > 接入流程
> Updated: 2026-08-03 09:13:56

# 接入流程

本文介绍了如何通过钉钉统一授权套件完成第三方企业或个人授权和组织授权，帮助开发者安全、合规地获取用户或企业资源访问权限。

## **背景说明**

在钉钉开放平台中，三方应用需通过授权机制获取调用 OpenAPI 的权限。根据访问主体不同，授权方式分为：

- **个人授权（委托授权）**：由终端用户授权，应用代表该用户访问其个人数据（如通讯录信息、日程等）。适用于需要基于用户上下文的场景。
- **组织授权（应用授权）**：由企业管理员授权，应用以自身身份直接访问企业资源（如离职员工列表、考勤数据等），无需用户登录参与。

判断接口属于哪种授权类型的方法如下：

- 在开发者后台申请权限时，若该权限被标记为“个人权限”，则对应接口为**个人授权接口**；
- 其余权限（如组织、人事、审批等）均为**组织授权接口**。

开发者应先明确业务需求所涉及的接口类型，并在开发前完成相应权限申请。

## **版本说明**

| 客户端 | **Android** | **IOS** | **PC** |
| --- | --- | --- | --- |
| 版本说明 | 支持(钉钉版本≥6.3.35) | 支持(钉钉版本≥6.3.35) | 支持(钉钉版本≥6.3.35) |

## **组织授权（应用授权）**

### **效果示例图**

- 授权企业管理员授权

  ![管理员授权](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5079592871/p582160.png)
- 授权企业非管理员需要选择管理员授权

  ![非管理员](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2111968761/p582166.gif)

  选择管理员授权后，该管理员会收到消息卡片通知，样例如下：

  ![iShot_2023-04-27_10..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5079592871/p638726.png)

#### **授权流程图**

![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0509248471/p961801.png)

### **流程简介**

1. 确认使用场景，明确目标接口是否属于组织授权。
2. 在开发者后台申请对应的 OpenAPI 权限点，例如`qyapi_hrm_read_user`。
3. 集成统一授权 JS SDK，调用`openAuth`唤起授权弹窗，需企业管理员确认。
4. 授权完成后，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口，获取应用级`access_token`。
5. 使用`access_token`调用 [获取离职员工列表](0947-obtain-the-list-of-employees-who-have-left.md)接口，获取授权企业离职员工的 userId 列表。

### **接入步骤**

#### **步骤一：确认使用场景**

1. 明确你的应用希望调用的 OpenAPI。例如，若需获取离职员工列表，则应调用[获取离职员工列表](0947-obtain-the-list-of-employees-who-have-left.md)接口，该接口属于组织授权接口。
2. 在开发者后台权限管理页面搜索并申请权限`qyapi_hrm_read_user`。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9079592871/p961813.png)

#### **步骤二：****调用授权组件**

##### **安装 SDK**

执行以下命令，下载安装SDK（dingtalk-design-libs需要版本在0.1.0及以上）。

```
npm install dingtalk-design-libs --save
```

##### **导入** **openAuth**

下载完成后，直接在代码中导入即可。

```
import { openAuth } from 'dingtalk-design-libs/biz/openAuth';
```

##### **接入 openAuth 组件**

> 当用户同意授权后，需要缓存或持久化授权结果，避免用户每次进入应用都要唤起授权套件。

```
openAuth({
    clientId:'suitexxx', // 应用的 ClientID
    corpId:'dingxxx', // 授权组织的 CorpId
    rpcScope:'qyapi_hrm_read_user', // 权限点 Code
    fieldScope:'', // 特殊权限点 Code, 在应用访问场景为空
    type:1 // 0 标识授委托授权；1 标识应用授权
}).then((res)=>{
    // 处理返回数据
})
```

| **参数** | **类型** | **是否必填** | **示例** | **说明** |
| --- | --- | --- | --- | --- |
| clientId | string | 是 | suitexxx | 应用的 ClientID。 |
| corpId | string | 是 | dingxxxx | 授权组织的 CorpId。  **[!NOTE]**  填写授权企业的CorpId。 |
| rpcScope | string | 是 | qyapi\_hrm\_read\_user | 权限点 Code 列表，使用英文逗号分隔。你也可以填写.default，即默认填写所有应用申请的应用权限点 Code。 |
| fieldScope | string | 不填 |  | 字段 Code。 |
| type | string | 是 | 1 | - 0：申请委托（个人）授权 - 1：申请应用（组织）授权 |

##### **响应参数**

| **响应信息** | **说明** |
| --- | --- |
| 授权完成 | ``` {  status: 'ok',  result: {  authCode:'xxxxxxx' // 如果是组织授权（type=1），则不返回该值  } } ``` |
| 拒绝授权 | ``` {     status: 'cancel',     result: null } ``` |
| 授权异常 | ``` {     status: 'failed',     result: null } ``` |
| 向管理员发送了授权申请，等待授权（只在组织授权场景下出现） | ``` {     status: 'toAdmin',     result: null } ``` |

#### **步骤三：****授权码兑换用户委托的访问凭证**

授权组织管理员授权完成后，可直接调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口，获取应用访问凭证。

#### **步骤四：获取离职员工列表**

根据访问凭证 Access Token 调用[获取离职员工列表](0947-obtain-the-list-of-employees-who-have-left.md)接口，即可获取离职员工的 userId 列表信息。

## **个人授权（委托授权）**

### **效果示例图**

![iShot_2023-05-18_20..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9079592871/p672669.png)

### **授权流程图**

![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0509248471/p961756.png)

### **流程简介**

1. 确认使用场景，明确目标接口是否属于个人授权。
2. 在开发者后台申请对应的 OpenAPI 权限点，例如`Contact.User.Read`。
3. 集成统一授权 JS SDK，调用`openAuth`唤起授权弹窗，用户同意后获得`authCode`。
4. 使用`authCode`调用[获取用户token](0032-obtain-user-token.md)接口，换取用户级`access_token`。
5. 使用用户`access_token`调用 [获取用户通讯录个人信息](0054-dingtalk-retrieve-user-information.md)接口,获取用户昵称、unionId 等信息。

### **接入步骤**

#### **步骤一：确认使用场景**

1. 明确你的应用希望调用的 OpenAPI。例如，若需获取用户个人信息，则应调用 [获取用户通讯录个人信息](0054-dingtalk-retrieve-user-information.md)接口，该接口属于个人权限。
2. 登录开发者后台，为应用申请相关权限。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9079592871/p961760.png)

#### **步骤二：****调用授权组件**

##### **安装 SDK**

执行以下命令安装 SDK，要求 dingtalk-design-libs 版本为 0.1.0 及以上。

```
npm install dingtalk-design-libs --save
```

##### **导入** **openAuth**

下载完成后，在代码中导入组件：

```
import { openAuth } from 'dingtalk-design-libs/biz/openAuth';
```

##### **接入 openAuth 组件**

> 授权成功后，建议缓存或持久化授权结果，避免用户每次进入应用都重复唤起授权弹窗。

```
openAuth({
    clientId:'suitexxx', // 应用的 ClientID
    corpId:'dingxxx', // 授权组织的 CorpId
    rpcScope:'Contact.User.Read', // 权限点 Code
    fieldScope:'', // 特殊权限点 Code, 在应用访问场景为空
    type:0 // 0 标识授委托授权；1 标识应用授权
}).then((res)=>{
    // 处理返回数据
})
```

| **参数** | **类型** | **是否必填** | **示例** | **说明** |
| --- | --- | --- | --- | --- |
| clientId | string | 是 | suitexxx | 应用的 ClientID。 |
| corpId | string | 是 | dingxxxx | 授权企业的CorpId。 |
| rpcScope | string | 是 | Contact.User.Read | 权限点 Code 列表，使用英文逗号分隔。你也可以填写.default，即默认填写所有应用申请的应用权限点 Code。 |
| fieldScope | string | 否 |  | 字段 Code。 |
| type | string | 是 | 0 | - 0：申请委托（个人）授权 - 1：申请应用（组织）授权 |

##### **响应参数**

| **响应信息** | **说明** |
| --- | --- |
| 授权完成 | ``` {  status: 'ok',  result: {  authCode:'xxxxxxx' // 如果是组织授权（type=1），则不返回该值  } } ``` |
| 拒绝授权 | ``` {     status: 'cancel',     result: null } ``` |
| 授权异常 | ``` {     status: 'failed',     result: null } ``` |

#### **步骤三：****授权码兑换用户委托的访问凭证**

1. 委托（个人）授权完成后，会成功返回 authCode 授权码。
2. 根据授权码，调用[获取用户token](0032-obtain-user-token.md)接口，获取访问凭证。

#### **步骤四：获取用户个人信息**

根据访问凭证 Access Token 调用[获取用户通讯录个人信息](0054-dingtalk-retrieve-user-information.md)接口，即可获取用户昵称、用户unionId等信息。

> [获取用户通讯录个人信息](0054-dingtalk-retrieve-user-information.md)接口如需获取当前访问用户的个人信息，参数 unionId 参数传 me 即可。

## **快速体验（Demo）**

### **准备工作**

| **开发环境** | **说明** |
| --- | --- |
| Java | - 已安装 JDK 17 及以上，本示例使用 JDK 17。 - 已安装 Maven 3 |
| Node.js | - 已安装 Node.js。 |

### **操作步骤**

1. 确保应用为第三方企业应用，且已有授权组织。

   > 测试阶段可通过添加体验组织进行测试，详情参考[（可选）测试应用](../01-XOnnmGCTbn-开发指南/0016-test-dingtalk-app.md)。
2. 设置应用首页地址和 PC 端首页地址为：`http://localhost:3000/`。

   > 本示例运行在本地，采用 http://localhost:3000/。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9079592871/p961829.png)
3. 下载示例 Demo：[dingTalk-unified-authorization .zip](https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20250528/cilrjp/dingTalk-unified-authorization+.zip)。
4. 分别启动前端项目和后端项目：

   > 注意：确保 3000 和 8080 端口未被其他程序占用。

   | **启动项** | **说明** |
   | --- | --- |
   | 前端服务 | 在解压后的 dingTalk-unified-authorization 的目录下：  1. `cd frontend/`  2. `npm install`  3. `npm run dev -- --authCorpId=your authCorpId --clientId=your app clientId`  **[!NOTE]**  你需要替换 corpId 和 clientId：  - CorpId，需要传授权开通该三方应用的组织CorpId。 - Client ID，详情参考 [Client ID/Client Secret](../01-XOnnmGCTbn-开发指南/0001-basic-concepts-beta.md#7d9825efaadw7)。 |
   | 后端服务 | 在解压后的 dingTalk-unified-authorization 的目录下：  1. `cd backend/`  2.`./mvnw spring-boot:run -Dspring-boot.run.arguments="--dingtalk.clientId=your app clientId --dingtalk.clientSecret=your app clientSecret --dingtalk.authCorpId=your app authCorpId"`  **[!NOTE]**  你需要替换 clientId 和 client secret：  - Client ID，详情参考[Client ID/Client Secret](../01-XOnnmGCTbn-开发指南/0001-basic-concepts-beta.md#7d9825efaadw7)。 - Client Secret，详情参考[Client ID/Client Secret](../01-XOnnmGCTbn-开发指南/0001-basic-concepts-beta.md#7d9825efaadw7)。 - CorpId，需要传授权开通该三方应用的组织CorpId。 |
5. 项目启动后，可在授权组织的工作台中使用该应用。

   > **说明**：必须在钉钉客户端内访问应用页面。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9079592871/p961831.png)

## 注意事项

- **SDK 版本要求**：集成 `dingtalk-design-libs` 时，请确保版本不低于 0.1.0，否则可能导致功能异常。
- **缓存授权状态**：建议将授权成功状态进行本地存储或服务端记录，防止重复授权打扰用户体验。
- **权限申请时机**：必须在调用授权前完成权限申请，否则会导致授权失败或接口无权调用。
- **type 参数含义清晰**：`type=0`表示用户级授权，用于访问用户数据；`type=1`表示应用级授权，用于访问企业资源。

## 常见问题

**Q1：为什么调用接口返回“权限不足”？**

A：请检查以下几点：

- 是否已在开发者后台为应用申请对应权限；
- 是否已完成个人或组织授权流程；
- 授权的企业是否与当前调用接口的企业一致。

**Q2：组织授权为什么不返回 authCode？**

A：组织授权是应用级授权，授权完成后可直接获取应用`access_token`，无需通过`authCode`中转，因此不返回该字段。

**Q3：如何知道授权是否成功？**

A：可通过调用相关接口，测试是否能正常返回数据；

**Q4：Client ID 和 Client Secret 如何获取？**

A：登录[钉钉开放平台](https://open-dev.dingtalk.com/) → 进入应用详情页 → **基础信息 > 凭证与基础信息**，即可查看`Client ID`和`Client Secret`。

**Q5：能否同时支持个人授权和组织授权？**

A：可以。同一个第三方企业应用可根据不同业务场景分别实现两种授权模式，但需独立处理授权逻辑。

**Q6：授权后access\_token过期了怎么处理？**

A：建议实现定时刷新机制，定期调用获取接口刷新。
