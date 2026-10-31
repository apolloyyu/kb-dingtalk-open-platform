---
title: "应用全生命周期管控：自动化创建、查询与权限配置"
source_url: "https://open.dingtalk.com/document/development/application-management-workflow"
namespace: "development"
slug: "application-management-workflow"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "钉钉应用 > 集成方案 > 应用全生命周期管控：自动化创建、查询与权限配置"
doc_id: "izYdSmy8KD"
updated_at: "2026-10-16 09:23:13"
---

> Source: https://open.dingtalk.com/document/development/application-management-workflow
> Path: 应用开发 / 服务端 API / 钉钉应用 > 集成方案 > 应用全生命周期管控：自动化创建、查询与权限配置
> Updated: 2026-10-16 09:23:13

# 应用全生命周期管控：自动化创建、查询与权限配置

## **概述**

本方案基于钉钉开放平台应用管理API，介绍如何通过服务端接口实现企业内部应用的创建、查询、更新、使用范围管理及删除等全生命周期管理。企业通过调用应用管理相关API，可将应用的创建部署、权限配置、范围调整等操作集成到自有管理系统中，实现从应用创建到下线的全流程程序化管控，适用于房地产物业管理、汽车后市场服务等多种企业场景。

### 方案背景

随着企业数字化转型深入，内部应用数量快速增长，但依赖开发者后台手动创建、配置和管理应用效率低下且易出错；应用使用范围的调整需逐一操作，跨部门协作时权限变更响应滞后；废弃应用缺乏统一清理机制，长期残留增加安全风险和管理成本。钉钉应用管理API提供了从应用创建、信息查询、使用范围配置到应用删除的完整链路，使企业能够实现应用全生命周期的程序化管理。

企业在日常运营中常面临以下痛点：

- **应用创建耗时**： 每个新应用需在开发者后台手动填写名称、图标、首页链接等参数并逐一配置，单个应用部署周期长达半天，影响业务及时上线。
- **权限配置粗放**： 应用使用范围只能手动勾选部门，无法按岗位或角色精细分配，曾发生多起非授权人员误操作敏感应用导致数据混乱的事件。
- **应用状态不透明**： 无法一键获取企业所有应用列表及指定用户的可见应用，应用资产盘点依赖人工逐页翻查，年度盘点耗时数周。
- **废弃应用堆积**： 退出使用的应用未及时清理，累计残留大量废弃应用占用配额且存在安全隐患，管理员难以区分有效和无效应用。

### **核心价值**

- **应用批量创建部署：** 通过API批量创建企业内部H5微应用，自动配置应用名称、图标、首页链接等参数，获取agentid用于后续管理，应用上线效率提升80%以上。
- **使用范围精准管控：** 支持按用户维度动态设置应用可见范围，实现按部门、角色或个人的精细化权限分配，确保敏感应用仅对授权人员可见。
- **应用状态实时查询：** 一键获取企业所有应用列表及指定用户的可见应用列表，为应用资产盘点和权限审计提供实时数据支撑。
- **废弃应用安全清理：** 通过API删除不再使用的内部应用，避免废弃应用长期残留带来的安全隐患和管理负担。

### **适用场景**

- **房地产物业管理系统部署：** 物业公司为新接管小区批量创建业主服务、设备巡检、费用缴纳等专属应用，按楼栋和岗位精准配置使用范围，项目交接时一键清理旧应用。
- **汽车4S店售后服务应用管理：** 集团总部为各门店统一创建维保预约、配件查询、客户回访等应用，根据门店类型和员工角色动态调整应用可见范围，闭店时批量删除对应应用。
- **环保科技企业项目管理：** 为每个环保工程项目创建独立的数据采集和分析应用，按项目组配置使用范围，项目结项后自动清理相关应用释放资源。

## **典型业务场景**

### **场景一：房地产物业小区服务应用批量部署（房地产行业）**

#### **痛点分析**

某大型物业管理公司管理200+住宅小区，每个小区需在钉钉工作台部署业主报修、费用查询、访客登记、设备巡检等6-8个专属应用。原有流程存在以下问题：

- **应用创建耗时：** 每个新接管小区需在开发者后台手动创建6-8个应用并逐一配置参数，单个小区的应用部署周期长达3天，影响物业服务及时上线。
- **权限配置粗放：** 应用使用范围只能手动勾选部门，无法按楼栋管家、维修工等岗位精细分配，曾发生15起非授权人员误操作设备巡检应用导致数据混乱的事件。
- **废弃应用堆积：** 退出管理的小区应用未及时清理，累计残留120+废弃应用，管理员难以区分有效和无效应用，年度应用资产盘点耗时2周。

#### **价值验证**

- **自动化流程**

  ![房地产物业小区服务应用批量部署场景图](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3260491971/p1105663.png)
- **关键优势**

  - **应用批量秒级创建：** 新小区6-8个应用通过API批量创建并自动配置参数，部署周期从3天缩短至10分钟，服务上线提速99%。
  - **岗位级权限精准分配：** 按楼栋管家、维修工、客服等岗位动态设置应用可见范围，非授权误操作事件降为零。
  - **废弃应用一键清理：** 退出小区时自动删除所有关联应用，残留应用从120+清零，年度盘点耗时从2周缩短至1天。

### **场景二：汽车4S店集团门店应用统一管理（汽车后市场行业）**

#### **痛点分析**

某全国性汽车经销商集团拥有300+4S店门店，总部IT部门需为各门店统一部署维保预约、配件库存查询、客户满意度回访、培训考核等应用。原有流程存在以下问题：

- **门店差异难适配：** 不同品牌门店（豪华/合资/自主）需要的应用组合不同，总部需逐店手动创建和配置，300家门店的年度应用部署工作量耗费3名专职IT人员。
- **人员变动响应慢：** 门店员工调岗或离职后应用权限未及时更新，离职员工仍可访问客户信息应用，季度内发生6起数据安全合规告警。
- **闭店清理遗漏：** 关闭的门店应用未从系统中删除，废弃应用占用应用配额且存在数据泄露风险，安全审计时被通报整改。

#### **价值验证**

- **自动化流程**

  ![汽车4S店集团门店应用统一管理场景图](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3260491971/p1105664.png)
- **关键优势**

  - **门店应用模板化上线：** 新店应用按品牌模板批量创建，300家门店年度部署工作量从3人降至0.5人，IT人力成本降低83%。
  - **权限随人员动态同步：** 员工调岗或离职时系统自动更新应用可见范围，数据安全合规告警从季度6起降为零。
  - **闭店应用零残留：** 闭店时自动触发应用批量删除，废弃应用占用配额归零，安全审计通过率提升至100%。

## **实施指南**

### **技术架构**

本方案的技术架构包含以下核心组件：

- **身份鉴权层：** 负责应用凭证管理和访问令牌获取，确保所有服务端调用的身份合法性。
- **应用查询层：** 实现企业应用列表和用户可见应用列表的查询功能，为应用资产盘点和权限审计提供数据基础。
- **应用创建与维护层：** 实现内部应用的创建、信息更新和删除操作，支持应用全生命周期的程序化管理。
- **使用范围管理层：** 实现应用可见范围的查询和动态调整，保障应用权限的精细化管控。

### **前置条件**

- **应用准备：** 完成[应用创建与配置](../01-XOnnmGCTbn-开发指南/0007-create-application.md)的流程。
- **权限要求：** 操作者为企业管理员，具备在开发者后台进行配置的权限，并申请以下接口权限：

  - `qyapi_get_microapp_list`（获取应用列表权限）
  - `qyapi_microapp_manage`（应用管理权限）
- **开发环境：** 已安装Java开发环境（JDK 8及以上版本）。
- **SDK准备：** 下载钉钉[服务端SDK](0002-download-the-server-side-sdk.md)，版本建议最新稳定版。

### **代码实现**

步骤一：获取应用凭证信息，获取应用 Client ID 和 Client Secret。

步骤二：申请接口权限，申请应用管理相关接口的权限。

步骤三：获取应用访问凭证[获取企业内部应用的accessToken](0032-obtain-the-access-token-of-an-internal-app.md)，通过accessToken鉴权调用者身份。

步骤四：应用查询操作：

1. 调用服务端API-[获取企业所有应用列表](0865-obtains-a-list-of-all-enterprise-applications.md)接口，获取企业应用信息。
2. 调用服务端API-[获取用户可见的企业应用列表](0868-obtains-the-list-of-enterprise-applications-visible-to-a-user.md)接口，获取当前用户可使用的应用信息。

步骤五：应用管理操作：

1. 调用服务端API-[创建企业内部应用](0862-create-an-h5-application-for-your-enterprise.md)接口，创建一个企业内部应用-H5微应用，获取应用的agentid。
2. 根据应用agentid，调用服务端API-[更新企业内部应用](0863-update-internal-h5-applications.md)接口，更新企业内部应用-H5微应用信息。
3. 根据应用agentid，调用服务端API-[获取企业应用的可使用范围](0874-obtains-the-application-visible-range.md)接口，获取当前应用的可使用范围。
4. 根据应用agentid，调用服务端API-[更新企业内部应用的可使用范围](0873-update-the-visible-range-of-micro-applications.md)接口，更新当前应用的可使用范围。
5. 根据应用agentid，调用服务端API-[删除企业内部应用](0864-delete-an-internal-h5-application.md)接口，删除对应的企业内部应用。

## **实施步骤**

### **步骤一：****获取应用凭证**

1. 登录[钉钉开发者后台](https://open-dev.dingtalk.com/)。
2. 选择目标应用，进入应用详情页。
3. 单击**基础信息** > **凭证与基础信息**。
4. 记录应用的`Client ID`和`Client Secret`。

   > **[!NOTE]**
   >
   > 请妥善保管 `Client Secret`，不要泄露给第三方。建议将其存储在环境变量或密钥管理系统中，避免硬编码在代码里。

### **步骤二：添加接口权限**

1. 在应用详情页，单击**权限管理**。
2. 在权限搜索框中输入以下权限标识并申请：

   - `qyapi_get_microapp_list`（获取应用列表权限）— 用于获取企业所有应用列表、获取用户可见的企业应用列表。
   - `qyapi_microapp_manage`（应用管理权限）— 用于创建企业内部应用、更新企业内部应用、获取应用可使用范围、更新应用可使用范围、删除企业内部应用。

> **[!NOTE]**
>
> 不同业务场景可能需要不同的权限组合，请根据实际需求申请。例如批量导入场景还需申请批量操作用户的相关权限。

### 步骤三：获取访问凭证（accessToken）

根据步骤一中 的 Client ID 和 Client Secret，获取应用访问凭证[获取企业内部应用的accessToken](0032-obtain-the-access-token-of-an-internal-app.md)。

```
public void getAccessToken() throws Exception {
  Config config = new Config();
  config.protocol = "https";
  config.regionId = "central";
  com.aliyun.dingtalkoauth2_1_0.Client client = new com.aliyun.dingtalkoauth2_1_0.Client(config);
  GetAccessTokenRequest accessTokenRequest = new GetAccessTokenRequest()
    .setAppKey("din*********hgn")
    .setAppSecret("9G_O************mBkhgGIO");
  GetAccessTokenResponse accessToken = client.getAccessToken(accessTokenRequest);
  System.out.println(JSON.toJSONString(accessToken.getBody()));
}
```

**最佳实践**：

- **缓存策略**：`accessToken`有效期为2小时，建议在内存或Redis中缓存，过期前5分钟主动刷新。
- **并发控制**：避免多个线程同时刷新token导致冲突，可使用分布式锁机制。
- **异常重试**：网络波动时自动重试，最多3次，间隔递增（1s → 2s → 4s）。

### **步骤四：应用查询操作**

1. 调用服务端API-[获取企业所有应用列表](0865-obtains-a-list-of-all-enterprise-applications.md)接口，获取企业应用信息。

   ```
   public void allApps() throws Exception {
       Config config = new Config();
       config.protocol = "https";
       config.regionId = "central";

       com.aliyun.dingtalkmicro_app_1_0.Client client = new com.aliyun.dingtalkmicro_app_1_0.Client(config);

       ListAllAppHeaders listAllAppHeaders = new ListAllAppHeaders();
       listAllAppHeaders.xAcsDingtalkAccessToken = "accessToken";

       try {
           ListAllAppResponse listAllAppResponse = client.listAllAppWithOptions(
                   listAllAppHeaders,
                   new RuntimeOptions()
           );
           System.out.println(JSON.toJSONString(listAllAppResponse.getBody()));
       } catch (TeaException err) {
           if (!com.aliyun.teautil.Common.empty(err.code) && !com.aliyun.teautil.Common.empty(err.message)) {
               // err 中含有 code 和 message 属性，可帮助开发定位问题
               System.out.println(err.code);
               System.out.println(err.message);
           }
       } catch (Exception _err) {
           TeaException err = new TeaException(_err.getMessage(), _err);
           if (!com.aliyun.teautil.Common.empty(err.code) && !com.aliyun.teautil.Common.empty(err.message)) {
               // err 中含有 code 和 message 属性，可帮助开发定位问题
               System.out.println(err.code);
               System.out.println(err.message);
           }
       }
   }
   ```

   **请求参数：**

   - 无需传入业务参数，通过accessToken鉴权即可获取当前企业所有应用列表。

   **返回字段：**

   - `appList`：企业所有应用的信息列表，包含应用名称、agentid、应用类型、应用状态等。
2. 调用服务端API-[获取用户可见的企业应用列表](0868-obtains-the-list-of-enterprise-applications-visible-to-a-user.md)接口，获取当前用户可使用的应用信息。

   ```
   public void usersApps() throws Exception {
           Config config = new Config();
           config.protocol = "https";
           config.regionId = "central";
           com.aliyun.dingtalkmicro_app_1_0.Client client = new com.aliyun.dingtalkmicro_app_1_0.Client(config);
           ListUserVilebleAppHeaders listUserVilebleAppHeaders = new ListUserVilebleAppHeaders();
           listUserVilebleAppHeaders.xAcsDingtalkAccessToken = "accessToken";
           try {
               ListUserVilebleAppResponse userAppsList = client.listUserVilebleAppWithOptions("manager7675", listUserVilebleAppHeaders, new RuntimeOptions());
               System.out.println(JSON.toJSONString(userAppsList.getBody()));
           } catch (TeaException err) {
               if (!com.aliyun.teautil.Common.empty(err.code) && !com.aliyun.teautil.Common.empty(err.message)) {
                   // err 中含有 code 和 message 属性，可帮助开发定位问题
                   System.out.println(err.code);
                   System.out.println(err.message);
               }
           } catch (Exception _err) {
               TeaException err = new TeaException(_err.getMessage(), _err);
               if (!com.aliyun.teautil.Common.empty(err.code) && !com.aliyun.teautil.Common.empty(err.message)) {
                   // err 中含有 code 和 message 属性，可帮助开发定位问题
                   System.out.println(err.code);
                   System.out.println(err.message);
               }
           }
       }
   ```

   **请求参数：**

   - `userId`：目标用户的userId，作为路径参数传入。

   **返回字段：**

   - `appList`：该用户可见的应用信息列表。

### **步骤五：应用管理操作**

1. 调用服务端API-[创建企业内部应用](0862-create-an-h5-application-for-your-enterprise.md)接口，创建一个企业内部应用，获取应用的agentid。

   ```
    public void appsCreate() throws Exception {
           Config config = new Config();
           config.protocol = "https";
           config.regionId = "central";
           com.aliyun.dingtalkmicro_app_1_0.Client client = new com.aliyun.dingtalkmicro_app_1_0.Client(config);
           CreateInnerAppHeaders createInnerAppHeaders = new CreateInnerAppHeaders();
           createInnerAppHeaders.xAcsDingtalkAccessToken = "accessToken";
           CreateInnerAppRequest createInnerAppRequest = new CreateInnerAppRequest()
                   .setOpUnionId("E9CS6Xu5*****N7QiEiE")
                   .setName("20221104应用")
                   .setDesc("20221104应用")
                   .setIcon("@lADOd*****0CbA")
                   .setHomepageLink("https://www.dingtalk.com")
                   .setPcHomepageLink("https://www.dingtalk.com")
                   .setOmpLink("https://www.dingtalk.com")
                   .setIpWhiteList(java.util.Arrays.asList(
                           "1.1.1.1","127.0.0.1"
                   ))
                   .setScopeType("BASE");
           try {
               CreateInnerAppResponse innerAppWithOptions = client.createInnerAppWithOptions(createInnerAppRequest, createInnerAppHeaders, new RuntimeOptions());
               System.out.println(JSON.toJSONString(innerAppWithOptions.getBody()));
           } catch (TeaException err) {
               if (!com.aliyun.teautil.Common.empty(err.code) && !com.aliyun.teautil.Common.empty(err.message)) {
                   // err 中含有 code 和 message 属性，可帮助开发定位问题
                   System.out.println(err.code);
                   System.out.println(err.message);
               }
           } catch (Exception _err) {
               TeaException err = new TeaException(_err.getMessage(), _err);
               if (!com.aliyun.teautil.Common.empty(err.code) && !com.aliyun.teautil.Common.empty(err.message)) {
                   // err 中含有 code 和 message 属性，可帮助开发定位问题
                   System.out.println(err.code);
                   System.out.println(err.message);
               }
           }
       }
   ```

   **请求参数：**

   - `name`：应用名称。
   - `desc`：应用描述信息。
   - `homepageLink`：移动端首页链接。
   - `pcHomepageLink`：PC端首页链接。
   - `scopeType`：权限类型，目前只支持BASE。

   **返回字段：**

   - `agentId`：应用唯一标识，后续所有应用管理操作的必传参数。
   - `appKey`：应用的AppKey。
   - `appSecret`：应用的AppSecret。
2. 根据应用agentid，调用服务端API-[更新企业内部应用](0863-update-internal-h5-applications.md)接口，更新企业内部应用信息。

   ```
   public void appsUpdate() throws Exception {
           Config config = new Config();
           config.protocol = "https";
           config.regionId = "central";
           com.aliyun.dingtalkmicro_app_1_0.Client client = new com.aliyun.dingtalkmicro_app_1_0.Client(config);
           UpdateInnerAppHeaders updateInnerAppHeaders = new UpdateInnerAppHeaders();
           updateInnerAppHeaders.xAcsDingtalkAccessToken = "accessToken";
           UpdateInnerAppRequest updateInnerAppRequest = new UpdateInnerAppRequest()
                   .setOpUnionId("E9CS6Xu5*****N7QiEiE")
                   .setName("20221104应用测试")
                   .setDesc("20221104应用测试")
                   .setIcon("@lADOd*****bM0CbA")
                   .setHomepageLink("https://www.dingtalk.com")
                   .setPcHomepageLink("https://www.dingtalk.com")
                   .setOmpLink("https://www.dingtalk.com")
                   .setIpWhiteList(java.util.Arrays.asList(
                          "1.1.1.1","127.0.0.1"
                   ));
           try {
               UpdateInnerAppResponse updateInnerAppResponse = client.updateInnerAppWithOptions("2021****82", updateInnerAppRequest, updateInnerAppHeaders, new RuntimeOptions());
               System.out.println(JSON.toJSONString(updateInnerAppResponse.getBody()));
           } catch (TeaException err) {
               if (!com.aliyun.teautil.Common.empty(err.code) && !com.aliyun.teautil.Common.empty(err.message)) {
                   // err 中含有 code 和 message 属性，可帮助开发定位问题
                   System.out.println(err.code);
                   System.out.println(err.message);
               }
           } catch (Exception _err) {
               TeaException err = new TeaException(_err.getMessage(), _err);
               if (!com.aliyun.teautil.Common.empty(err.code) && !com.aliyun.teautil.Common.empty(err.message)) {
                   // err 中含有 code 和 message 属性，可帮助开发定位问题
                   System.out.println(err.code);
                   System.out.println(err.message);
               }
           }
       }
   ```

   **请求参数：**

   - `agentId`：应用唯一标识，作为路径参数传入。
   - `opUnionId`：操作更新的员工unionId。
   - `name`：新的应用名称，可选参数。
   - `desc`：新的应用描述，可选参数。
   - `homepageLink`：新的移动端首页链接，可选参数。

   **返回字段：**

   - `result`：操作是否成功的布尔值。
3. 根据应用agentid，调用服务端API-[获取企业应用的可使用范围](0874-obtains-the-application-visible-range.md)接口，获取当前应用的可使用范围。

   ```
   public void  appsScopes() throws Exception {
           Config config = new Config();
           config.protocol = "https";
           config.regionId = "central";
           com.aliyun.dingtalkmicro_app_1_0.Client client = new com.aliyun.dingtalkmicro_app_1_0.Client(config);
           GetMicroAppScopeHeaders getMicroAppScopeHeaders = new GetMicroAppScopeHeaders();
           getMicroAppScopeHeaders.xAcsDingtalkAccessToken = "accessToken";
           try {
               GetMicroAppScopeResponse microAppScopeWithOptions = client.getMicroAppScopeWithOptions("2021****82", getMicroAppScopeHeaders, new RuntimeOptions());
               System.out.println(JSON.toJSONString(microAppScopeWithOptions.getBody()));
           } catch (TeaException err) {
               if (!com.aliyun.teautil.Common.empty(err.code) && !com.aliyun.teautil.Common.empty(err.message)) {
                   // err 中含有 code 和 message 属性，可帮助开发定位问题
                   System.out.println(err.code);
                   System.out.println(err.message);
               }

           } catch (Exception _err) {
               TeaException err = new TeaException(_err.getMessage(), _err);
               if (!com.aliyun.teautil.Common.empty(err.code) && !com.aliyun.teautil.Common.empty(err.message)) {
                   // err 中含有 code 和 message 属性，可帮助开发定位问题
                   System.out.println(err.code);
                   System.out.println(err.message);
               }
           }
       }
   ```

   **请求参数：**

   - `agentId`：应用唯一标识，作为路径参数传入。

   **返回字段：**

   - `userIds`：可见用户userId列表。
   - `deptIds`：可见部门ID列表。
   - `roleIds`可见角色ID列表。
   - `onlyAdminVisible`：是否仅管理员可使用。
4. 根据应用agentid，调用服务端API-[更新企业内部应用的可使用范围](0873-update-the-visible-range-of-micro-applications.md)接口，更新当前应用的可使用范围。

   ```
    public void appsScopesUpdate() throws Exception {
           Config config = new Config();
           config.protocol = "https";
           config.regionId = "central";
           com.aliyun.dingtalkmicro_app_1_0.Client client = new com.aliyun.dingtalkmicro_app_1_0.Client(config);
           SetMicroAppScopeHeaders setMicroAppScopeHeaders = new SetMicroAppScopeHeaders();
           setMicroAppScopeHeaders.xAcsDingtalkAccessToken = "accessToken";
           SetMicroAppScopeRequest setMicroAppScopeRequest = new SetMicroAppScopeRequest()
                   .setAddUserIds(java.util.Arrays.asList(
                           "01296106445126923197"
                   ))
                   .setOnlyAdminVisible(false);
           try {
               SetMicroAppScopeResponse setMicroAppScopeResponse = client.setMicroAppScopeWithOptions("2021****82", setMicroAppScopeRequest, setMicroAppScopeHeaders, new RuntimeOptions());
               System.out.println(JSON.toJSONString(setMicroAppScopeResponse.getBody()));
           } catch (TeaException err) {
               if (!com.aliyun.teautil.Common.empty(err.code) && !com.aliyun.teautil.Common.empty(err.message)) {
                   // err 中含有 code 和 message 属性，可帮助开发定位问题
                   System.out.println(err.code);
                   System.out.println(err.message);
               }
           } catch (Exception _err) {
               TeaException err = new TeaException(_err.getMessage(), _err);
               if (!com.aliyun.teautil.Common.empty(err.code) && !com.aliyun.teautil.Common.empty(err.message)) {
                   // err 中含有 code 和 message 属性，可帮助开发定位问题
                   System.out.println(err.code);
                   System.out.println(err.message);
               }
           }
       }
   ```

   **请求参数：**

   - `agentId`：应用唯一标识，作为路径参数传入。
   - `addUserIds`：待添加的用户userId列表。
   - `onlyAdminVisible`：是否仅管理员可使用。

   **返回字段：**

   - `result`：操作是否成功的布尔值。
5. 根据应用agentid，调用服务端API-[删除企业内部应用](0864-delete-an-internal-h5-application.md)接口，删除对应的企业内部应用。

   ```
    public void appsDelete() throws Exception {
           Config config = new Config();
           config.protocol = "https";
           config.regionId = "central";
           com.aliyun.dingtalkmicro_app_1_0.Client client = new com.aliyun.dingtalkmicro_app_1_0.Client(config);
           DeleteInnerAppHeaders deleteInnerAppHeaders = new DeleteInnerAppHeaders();
           deleteInnerAppHeaders.xAcsDingtalkAccessToken = "accessToken";
           DeleteInnerAppRequest deleteInnerAppRequest = new DeleteInnerAppRequest()
                   .setOpUnionId("E9CS6Xu5*****N7QiEiE");
           try {
               DeleteInnerAppResponse deleteInnerAppResponse = client.deleteInnerAppWithOptions("2021****82", deleteInnerAppRequest, deleteInnerAppHeaders, new RuntimeOptions());
               System.out.println(JSON.toJSONString(deleteInnerAppResponse.getBody()));
           } catch (TeaException err) {
               if (!com.aliyun.teautil.Common.empty(err.code) && !com.aliyun.teautil.Common.empty(err.message)) {
                   // err 中含有 code 和 message 属性，可帮助开发定位问题
                   System.out.println(err.code);
                   System.out.println(err.message);
               }
           } catch (Exception _err) {
               TeaException err = new TeaException(_err.getMessage(), _err);
               if (!com.aliyun.teautil.Common.empty(err.code) && !com.aliyun.teautil.Common.empty(err.message)) {
                   // err 中含有 code 和 message 属性，可帮助开发定位问题
                   System.out.println(err.code);
                   System.out.println(err.message);
               }
           }
       }
   ```

   **请求参数：**

   - `agentId`：应用唯一标识，作为路径参数传入。
   - `opUnionId`：操作人的unionId。

   **返回字段：**

   - `result`：操作是否成功的布尔值。

**实施完成检查清单**

- ✅ 已完成应用创建并获取Client ID和Client Secret。
- ✅ 已申请`qyapi_get_microapp_list`和`qyapi_microapp_manage`接口权限。
- ✅ 已成功获取accessToken并能正常调用接口。
- ✅ 已成功获取企业所有应用列表和用户可见应用列表。
- ✅ 已成功创建企业内部应用并获取agentid。
- ✅ 已成功更新应用信息和可使用范围。
- ✅ 已成功删除测试应用。
- ✅ 已在生产环境中完成端到端联调验证。

## **常见问题（FAQ）**

- **Q1：创建应用时需要哪些必填参数？**

  必填参数包括应用名称（name）、应用描述（desc）和操作人unionId（opUnionId）。首页链接、图标、IP白名单等为可选参数，建议在生产环境中配置完整的首页链接以确保应用可正常访问。
- **Q2：应用删除后可以恢复吗？**

  不可以。删除操作不可逆，建议在删除前先调用获取应用信息接口确认目标应用，并在测试环境验证删除逻辑后再在生产环境执行。
- **Q3：更新使用范围时如何移除已有用户？**

  更新使用范围接口支持通过`addUserIds`添加用户和`removeUserIds`移除用户。如需完全重置范围，可先调用获取范围接口获取当前列表，再按需构造添加和移除列表。
- **Q4：获取用户可见应用列表时userId从哪里获取？**

  userId可通过通讯录管理API获取，也可在钉钉管理后台的员工详情中查看。注意`userId`与`unionId`是不同的标识符，此接口使用的是`userId`。
- **Q5：应用管理API有调用频率限制吗？**

  有。应用管理相关接口遵循钉钉开放平台统一的频率限制策略，建议批量操作时合理控制调用间隔，避免触发限流。具体限制请参考钉钉开放平台API调用指南。
