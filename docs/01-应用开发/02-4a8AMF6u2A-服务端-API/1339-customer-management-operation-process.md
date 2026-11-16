---
title: "客户数据管理：构建客户数据创建与查重全流程"
source_url: "https://open.dingtalk.com/document/development/customer-management-operation-process"
namespace: "development"
slug: "customer-management-operation-process"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "更多开放 > 客户管理（官方CRM） > 集成方案 > 客户数据管理：构建客户数据创建与查重全流程"
doc_id: "nKJO0CMQxq"
updated_at: "2026-10-20 09:09:21"
---

> Source: https://open.dingtalk.com/document/development/customer-management-operation-process
> Path: 应用开发 / 服务端 API / 更多开放 > 客户管理（官方CRM） > 集成方案 > 客户数据管理：构建客户数据创建与查重全流程
> Updated: 2026-10-20 09:09:21

# 客户数据管理：构建客户数据创建与查重全流程

## **概述**

本方案基于钉钉开放平台CRM客户管理API，实现客户数据的全生命周期自动化管理。通过调用服务端接口，完成客户数据的创建、更新、删除、查询及查重等核心操作，打通企业内部业务系统与钉钉CRM的数据链路，消除手动录入带来的效率瓶颈与数据风险。

### **方案背景**

企业在客户管理过程中普遍面临以下挑战：销售线索分散在多个渠道（网站表单、展会名片、电话沟通），需要人工逐条录入CRM系统；客户信息变更频繁（联系方式、地址、跟进状态），依赖人工维护易遗漏或出错；海量客户数据中重复录入难以识别，导致资源浪费与管理混乱。传统手动流程不仅耗时费力，还容易因人为疏忽造成数据不一致，影响销售决策与客户体验。

企业在日常运营中常面临以下痛点：

- **线索录入效率低**：市场活动产生的大量线索需人工逐条复制粘贴至CRM系统，单人单日处理上限约50条，高峰期积压严重。
- **数据质量难保障**：姓名、手机号、公司名等字段拼写错误频发，后续还需二次核对修正，增加额外工作量。
- **重复记录难识别**：同一客户被多人重复创建，公海池与私海池数据割裂，管理层无法获得全局视图。
- **变更维护易遗漏**：客户联系方式、跟进阶段、负责人调整等操作依赖手动修改，常出现"改了A没改B"的局部更新问题。

### **核心价值**

本方案通过钉钉开放平台CRM客户管理API，为企业提供从线索导入、数据查重到动态更新的全链路自动化能力，彻底解决手动维护带来的效率瓶颈与数据风险。

- **数据录入自动化**：通过API批量创建客户，将原本需要数小时的手工录入压缩至分钟级完成，释放销售团队精力聚焦高价值跟进工作。
- **数据质量可控化**：内置查重校验机制，在创建/更新环节自动拦截重复记录，确保客户库唯一性与准确性。
- **数据流转实时化**：业务系统触发即同步至钉钉CRM，无需等待人工中转，保证各端数据始终一致。
- **运维成本最小化**：标准化接口调用替代定制化对接脚本，降低后续维护复杂度与技术债务。

### **适用场景**

本方案适用于以下典型业务场景：

- **企业自研CRM/ERP系统双向同步**：企业内部业务系统需与钉钉客户管理模块实现数据实时双向同步，避免信息孤岛。
- **营销活动线索批量导入去重**：市场活动产生的大量线索需批量导入钉钉CRM并自动去重，提升线索转化效率。
- **客户数据动态更新与精准查重**：客户联系方式、跟进阶段、负责人调整等操作自动触发钉钉CRM更新，结合服务端查重校验确保数据唯一性，避免手动维护遗漏与重复记录。
- **合规审计全程可追溯**：满足合规审计要求，客户数据变更全程留痕可追溯，支持多维度数据分析与历史回溯。

## **典型业务场景**

### **场景一：招聘候选人批量导入与人才库去重（人力资源）**

#### **痛点分析**

人力资源部门每日从多个渠道（招聘网站、内推、猎头推荐、校园招聘）接收数百份候选人简历，传统做法由HR专员手动逐条录入钉钉CRM系统，单人单日处理上限约30条，且姓名/手机号/邮箱拼写错误频发，后续还需二次核对修正。招聘高峰期候选人积压严重，黄金跟进窗口期被白白浪费，优质人才流失风险加剧。

#### **价值验证**

- **自动化流程**

  ![场景一-销售线索批量导入与客户数据创建](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1658542971/p1106994.png)
- **核心优势**

  - **批量导入提效**：单次API请求支持多条线索批量导入，替代人工逐条复制粘贴，处理效率提升数十倍。
  - **自动查重去重**：通过`skipDuplicateCheck=false`开启服务端查重校验，自动跳过已存在记录，避免重复推送导致脏数据。
  - **异常实时告警**：失败条目自动写入日志表并触发钉钉消息通知，确保问题可追溯、可复核。

### **场景二：员工客户关系动态更新与权限管控（人力资源）**

#### **痛点分析**

员工联系方式变更、入职状态推进、所属部门调整等操作依赖HR手动修改CRM记录，常出现"改了A没改B"的局部更新问题；跨部门协作时同一员工被多人重复创建，公海池与私海池数据割裂，管理层无法获得全局视图；负责人变更后未及时同步权限组，导致越权访问与数据泄露风险。

#### **价值验证**

- **自动化流程**

  ![场景二-客户数据动态更新与精准查重_20261019_141533](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1658542971/p1106995.png)
- **核心优势**

  - **事件驱动更新**：审批流通过后自动触发Webhook回调，确保数据变更与业务流程强绑定，避免人工遗漏。
  - **权限同步管控**：负责人变更时同步更新`permission.ownerStaffIds`权限组，防止越权访问与数据泄露。
  - **查重规则适配**：定期调用`getRelationUkSetting`获取最新查重配置，结合条件查询做交叉验证，适应不同业务线差异化需求。

## **实施指南**

### **技术架构**

- **接口调用层**：调用钉钉开放平台服务端API实现客户数据的创建、查询、更新、删除等操作。
- **应用认证层**：通过AppKey和AppSecret获取accessToken，鉴权调用者身份。
- **数据管理层**：调用钉钉CRM客户管理相关API完成客户实例的增删改查，获取instanceId。
- **查重校验层**：调用`getRelationUkSetting`获取查重字段配置，结合`skipDuplicateCheck`参数实现服务端去重。

### **前置条件**

- **应用准备**：完成企业内部应用的创建与配置，参考[应用创建与配置](../01-XOnnmGCTbn-开发指南/0007-create-application.md)。
- **权限要求**：拥有钉钉企业管理员或子管理员权限，并申请以下接口权限：

  - `qyapi_crm_maindata_read`（CRM主数据读权限）
  - `qyapi_crm_maindata_write`（CRM主数据写权限）
- **开发环境**：已安装Java开发环境（JDK1.6及以上）及Maven构建工具。
- **SDK准备**：下载钉钉服务端SDK，详情参见[服务端SDK下载](0002-download-the-server-side-sdk.md)，支持Java/Python/Go等多语言。

### **代码实现**

步骤一：获取应用凭证信息，获取应用 Client ID 和 Client Secret。

步骤二：申请接口权限，申请会议相关接口的权限。

步骤三：获取应用访问凭证[获取企业内部应用的accessToken](0032-obtain-the-access-token-of-an-internal-app.md)，调用接口时，通过accessToken鉴权调用者身份。

步骤四：核心API调用。

1. 调用服务端API-[获取个人或企业客户的元数据](1344-obtain-the-metadata-of-individual-enterprise-customers.md)接口，获取客户管理客户元数据信息。
2. 调用服务端API-[创建个人或企业客户数据](1345-add-crm-personal-customers.md)接口，进行客户数据的创建，获取客户数据`instanceId`。
3. 调用服务端API-[批量新增个人或企业客户数据](1348-add-multiple-relationship-data-in-batches.md)接口，进行客户数据的批量创建，获取多个客户数据`instanceId`。
4. 根据客户数据`instanceId`进行客户数据管理操作：
5. 根据客户数据`instanceId`，调用服务端API-[更新个人或企业客户数据](1346-update-crm-personal-customers.md)接口，进行更新客户数据。
6. 根据客户数据`instanceId`，调用服务端API-[批量更新个人或企业客户数据](1349-update-multiple-relational-data-tables-at-a-time.md)接口，进行更新客户数据。
7. 根据客户数据`instanceId`，调用服务端API-[删除个人或企业客户数据](1347-delete-crm-personal-customer.md)接口，进行删除客户数据。
8. 根据客户数据`instanceId`，调用服务端API-[批量获取个人或企业客户数据](1350-acquire-crm-individual-customers-in-batches.md)接口，进行批量获取客户数据信息。
9. 调用服务端API-[获取全量个人或企业客户数据](1351-crm-obtains-all-private-sea-customer-data.md)接口，获取全部客户数据。
10. 调用服务端API-[根据指定条件查询个人或企业客户数据](1352-obtains-crm-individual-customers-in-batches-based-on-specified-query.md)接口，查询符合指定条件的客户数据。
11. 调用服务端API-[获取个人或企业客户查重字段](1353-obtain-duplicate-check-fields.md)接口，获取查重字段数据。

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

   - `VideoConference.Conference.Write`（视频会议信息管理写权限）—— 用于创建、关闭会议，开启/停止录制。
   - `VideoConference.Conference.Read`（视频会议信息管理读权限）—— 用于查询会议信息、录制信息。

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

## 步骤四：核心API调用

1. **获取个人或企业客户的元数据**：调用服务端API-[获取个人或企业客户的元数据](1344-obtain-the-metadata-of-individual-enterprise-customers.md)接口，获取个人或企业客户的元数据信息。

   ```
   public void getCustomerObjectMeta() throws Exception {
           Config config = new Config();
           config.protocol = "https";
           config.regionId = "central";
           com.aliyun.dingtalkcrm_1_0.Client client = new com.aliyun.dingtalkcrm_1_0.Client(config);
           DescribeCrmPersonalCustomerObjectMetaHeaders describeCrmPersonalCustomerObjectMetaHeaders = new DescribeCrmPersonalCustomerObjectMetaHeaders();
           describeCrmPersonalCustomerObjectMetaHeaders.xAcsDingtalkAccessToken = "accessToken";
           DescribeCrmPersonalCustomerObjectMetaRequest describeCrmPersonalCustomerObjectMetaRequest = new DescribeCrmPersonalCustomerObjectMetaRequest()
                   .setRelationType("crm_customer");
           try {
               DescribeCrmPersonalCustomerObjectMetaResponse describeCrmPersonalCustomerObjectMetaResponse = client.describeCrmPersonalCustomerObjectMetaWithOptions(describeCrmPersonalCustomerObjectMetaRequest, describeCrmPersonalCustomerObjectMetaHeaders, new RuntimeOptions());
               System.out.println(JSON.toJSONString(describeCrmPersonalCustomerObjectMetaResponse.getBody()));
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

   **参数说明**

   - `relationType`：关系类型，固定传"crm\_customer"。

   **返回字段**

   - `objectMeta`：客户对象元数据信息，包含字段定义、类型、约束等。
2. **创建个人或企业客户数据**：调用服务端API-[创建个人或企业客户数据](1345-add-crm-personal-customers.md)接口，进行客户数据的创建，获取客户数据`instanceId`。

   ```
    public void createCustomers() throws Exception {
           Config config = new Config();
           config.protocol = "https";
           config.regionId = "central";
           com.aliyun.dingtalkcrm_1_0.Client client = new com.aliyun.dingtalkcrm_1_0.Client(config);
           AddCrmPersonalCustomerHeaders addCrmPersonalCustomerHeaders = new AddCrmPersonalCustomerHeaders();
           addCrmPersonalCustomerHeaders.xAcsDingtalkAccessToken = "accessToken";
           AddCrmPersonalCustomerRequest.AddCrmPersonalCustomerRequestPermission permission = new AddCrmPersonalCustomerRequest.AddCrmPersonalCustomerRequestPermission()
                   .setOwnerStaffIds(java.util.Arrays.asList(
                           "ma*******75"

                   ))
                   .setParticipantStaffIds(java.util.Arrays.asList(
                           "0147*********041"
                   ));
           Map<String,String> data = new HashMap<>();
           //客户名称字段必须填写
           data.put("customer_name","小钉");
           data.put("customer_follow_up_status","新获取");
           data.put("address","浙江省,杭州市,西湖区");
           data.put("TextField-714256","三墩镇,XX路XX号XX大厦XX室");
           data.put("MultiTagField-1437d010","客户");
           data.put("MultiTagField-e63401a9","重要");
           data.put("MultiTagField-5c48fb1d","洽谈");
           AddCrmPersonalCustomerRequest addCrmPersonalCustomerRequest = new AddCrmPersonalCustomerRequest()
                   .setCreatorUserId("ma*******75")
                   .setCreatorNick("小七")
                   .setData(data)
                   .setPermission(permission)
                   .setRelationType("crm_customer")
                   .setSkipDuplicateCheck(false);
   //                .setAction("publicDraw");
           try {
               AddCrmPersonalCustomerResponse addCrmPersonalCustomerResponse = client.addCrmPersonalCustomerWithOptions(addCrmPersonalCustomerRequest, addCrmPersonalCustomerHeaders, new RuntimeOptions());
               System.out.println(JSON.toJSONString(addCrmPersonalCustomerResponse.getBody()));
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

   **参数说明**

   - `creatorUserId`：创建者用户ID。
   - `creatorNick`：创建者昵称。
   - `data`：客户字段键值对Map。
   - `permission`：权限配置，包含负责人与参与人列表。
   - `relationType`：关系类型，固定传"crm\_customer"。
   - `skipDuplicateCheck`：是否跳过查重。

   **返回字段**

   - `instanceId`：新创建客户的唯一实例ID。
3. **批量新增个人或企业客户数据**：调用服务端API-[批量新增个人或企业客户数据](1348-add-multiple-relationship-data-in-batches.md)接口，进行客户数据的批量创建，获取多个客户数据`instanceId`。

   ```
   public void batchAddCustomers() throws Exception {
           Config config = new Config();
           config.protocol = "https";
           config.regionId = "central";
           com.aliyun.dingtalkcrm_1_0.Client client = new com.aliyun.dingtalkcrm_1_0.Client(config);
           BatchAddRelationDatasHeaders batchAddRelationDatasHeaders = new BatchAddRelationDatasHeaders();
           batchAddRelationDatasHeaders.xAcsDingtalkAccessToken = "<your access token>";
           BatchAddRelationDatasRequest.BatchAddRelationDatasRequestRelationListRelationPermissionDTO relationList0RelationPermissionDTO = new BatchAddRelationDatasRequest.BatchAddRelationDatasRequestRelationListRelationPermissionDTO()
                   .setPrincipalUserIds(java.util.Arrays.asList(
                           "manager0123"
                   ))
                   .setParticipantUserIds(java.util.Arrays.asList(
                           "manager0123"
                   ));
           java.util.Map<String, String> relationList0BizExtMap = TeaConverter.buildMap(
                   new TeaPair("key", "1")
           );
           BatchAddRelationDatasRequest.BatchAddRelationDatasRequestRelationListBizDataList relationList0BizDataList0 = new BatchAddRelationDatasRequest.BatchAddRelationDatasRequestRelationListBizDataList()
                   .setKey("customer_name")
                   .setValue("XX有限公司");
           BatchAddRelationDatasRequest.BatchAddRelationDatasRequestRelationList relationList0 = new BatchAddRelationDatasRequest.BatchAddRelationDatasRequestRelationList()
                   .setBizDataList(java.util.Arrays.asList(
                           relationList0BizDataList0
                   ))
                   .setBizExtMap(relationList0BizExtMap)
                   .setRelationPermissionDTO(relationList0RelationPermissionDTO);
           BatchAddRelationDatasRequest batchAddRelationDatasRequest = new BatchAddRelationDatasRequest()
                   .setRelationType("crm_customer")
                   .setOperatorUserId("manager021a")
                   .setSkipDuplicateCheck(false)
                   .setRelationList(java.util.Arrays.asList(
                           relationList0
                   ));
           try {
               BatchAddRelationDatasResponse batchAddRelationDatasResponse = client.batchAddRelationDatasWithOptions(batchAddRelationDatasRequest, batchAddRelationDatasHeaders, new RuntimeOptions());
               System.out.println(JSON.toJSONString(batchAddRelationDatasResponse.getBody()));
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

   **参数说明**

   - `relationType`：关系类型，固定传"crm\_customer"。
   - `operatorUserId`：操作者用户ID。
   - `skipDuplicateCheck`：是否跳过查重。
   - `relationList`：待创建客户列表，每项包含bizDataList、bizExtMap、relationPermissionDTO。

   **返回字段**

   - `resultList`：批量创建结果列表，含每条记录的instanceId与成功状态。
4. **更新个人或企业客户数据**：根据客户数据`instanceId`，调用服务端API-[更新个人或企业客户数据](1346-update-crm-personal-customers.md)接口，进行更新单个客户数据。

   ```
     public void updateCustomer() throws Exception {
           Config config = new Config();
           config.protocol = "https";
           config.regionId = "central";
           com.aliyun.dingtalkcrm_1_0.Client client = new com.aliyun.dingtalkcrm_1_0.Client(config);
           UpdateCrmPersonalCustomerHeaders updateCrmPersonalCustomerHeaders = new UpdateCrmPersonalCustomerHeaders();
           updateCrmPersonalCustomerHeaders.xAcsDingtalkAccessToken = "accessToken";
           UpdateCrmPersonalCustomerRequest.UpdateCrmPersonalCustomerRequestPermission permission = new UpdateCrmPersonalCustomerRequest.UpdateCrmPersonalCustomerRequestPermission()
                   .setOwnerStaffIds(java.util.Arrays.asList(
                           "ma*******75"
                   ))
                   .setParticipantStaffIds(java.util.Arrays.asList(
                           "014****************41"
                   ));
           Map<String,String> data = new HashMap<>();
           data.put("customer_name","小钉");
           data.put("customer_follow_up_status","新获取");
           data.put("address","北京市,朝阳区,望京东");
           data.put("TextField-714256","阿******座");
           data.put("MultiTagField-1437d010","客户");
           data.put("MultiTagField-e63401a9","重要");
           data.put("MultiTagField-5c48fb1d","洽谈");
           UpdateCrmPersonalCustomerRequest updateCrmPersonalCustomerRequest = new UpdateCrmPersonalCustomerRequest()
                   .setInstanceId("22GX******************2641")
                   .setModifierUserId("ma******75")
                   .setData(data)
                   .setModifierNick("小七")
                   .setPermission(permission)
                   .setRelationType("crm_customer")
                   .setSkipDuplicateCheck(false);
   //                .setAction("publicDraw");
           try {
               UpdateCrmPersonalCustomerResponse updateCrmPersonalCustomerResponse = client.updateCrmPersonalCustomerWithOptions(updateCrmPersonalCustomerRequest, updateCrmPersonalCustomerHeaders, new RuntimeOptions());
               System.out.println(JSON.toJSONString(updateCrmPersonalCustomerResponse.getBody()));
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

   **参数说明**

   - `instanceId`：待更新客户的唯一实例ID。
   - `modifierUserId`：修改者用户ID。
   - `data`：需更新的字段键值对Map。
   - `modifierNick`：修改者昵称。
   - `permission`：更新后的权限配置。
   - `relationType`：关系类型，固定传"crm\_customer"。
   - `skipDuplicateCheck`：更新时是否执行查重。

   **返回字段**

   - `instanceId`：被更新客户的实例ID。
5. **批量更新个人或企业客户数据**：根据客户数据`instanceId`，调用服务端API-[批量更新个人或企业客户数据](1349-update-multiple-relational-data-tables-at-a-time.md)接口，进行批量更新多个客户数据。

   ```
     public void batchUpdateCustomers() throws Exception {
           Config config = new Config();
           config.protocol = "https";
           config.regionId = "central";
           com.aliyun.dingtalkcrm_1_0.Client client = new com.aliyun.dingtalkcrm_1_0.Client(config);
           BatchUpdateRelationDatasHeaders batchUpdateRelationDatasHeaders = new BatchUpdateRelationDatasHeaders();
           batchUpdateRelationDatasHeaders.xAcsDingtalkAccessToken = "<your access token>";
           java.util.Map<String, String> relationList0BizExtMap = TeaConverter.buildMap(
                   new TeaPair("key", "1")
           );
           BatchUpdateRelationDatasRequest.BatchUpdateRelationDatasRequestRelationListBizDataList relationList0BizDataList0 = new BatchUpdateRelationDatasRequest.BatchUpdateRelationDatasRequestRelationListBizDataList()
                   .setKey("customer_name")
                   .setValue("XX有限公司");
           BatchUpdateRelationDatasRequest.BatchUpdateRelationDatasRequestRelationList relationList0 = new BatchUpdateRelationDatasRequest.BatchUpdateRelationDatasRequestRelationList()
                   .setBizDataList(java.util.Arrays.asList(
                           relationList0BizDataList0
                   ))
                   .setBizExtMap(relationList0BizExtMap)
                   .setRelationId("fasdg8i814-0afsd");
           BatchUpdateRelationDatasRequest batchUpdateRelationDatasRequest = new BatchUpdateRelationDatasRequest()
                   .setRelationType("crm_customer")
                   .setOperatorUserId("manager021a")
                   .setSkipDuplicateCheck(false)
                   .setRelationList(java.util.Arrays.asList(
                           relationList0
                   ));
           try {
               BatchUpdateRelationDatasResponse batchUpdateRelationDatasResponse = client.batchUpdateRelationDatasWithOptions(batchUpdateRelationDatasRequest, batchUpdateRelationDatasHeaders, new RuntimeOptions());
               System.out.println(JSON.toJSONString(batchUpdateRelationDatasResponse.getBody()));
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

   **参数说明**

   - `relationType`：关系类型，固定传"crm\_customer"。
   - `operatorUserId`：操作者用户ID。
   - `skipDuplicateCheck`：是否跳过查重。
   - `relationList`：待更新客户列表，每项需指定relationId。

   **返回字段**

   - `resultList`：批量更新结果列表。
6. **删除个人或企业客户数据**：根据客户数据`instanceId`，调用服务端API-[删除个人或企业客户数据](1347-delete-crm-personal-customer.md)接口，进行删除客户数据。

   ```
   public void deleteCustomerData() throws Exception {
       Config config = new Config();
       config.protocol = "https";
       config.regionId = "central";

       com.aliyun.dingtalkcrm_1_0.Client client = new com.aliyun.dingtalkcrm_1_0.Client(config);

       DeleteCrmPersonalCustomerHeaders deleteCrmPersonalCustomerHeaders = new DeleteCrmPersonalCustomerHeaders();
       deleteCrmPersonalCustomerHeaders.xAcsDingtalkAccessToken = "accessToken";

       DeleteCrmPersonalCustomerRequest deleteCrmPersonalCustomerRequest = new DeleteCrmPersonalCustomerRequest()
               .setRelationType("crm_customer")
               .setCurrentOperatorUserId("m********5");

       try {
           DeleteCrmPersonalCustomerResponse deleteCrmPersonalCustomerResponse = client.deleteCrmPersonalCustomerWithOptions(
                   "22GXvbkITYCMkIKBDo9YJA08811665212641",
                   deleteCrmPersonalCustomerRequest,
                   deleteCrmPersonalCustomerHeaders,
                   new RuntimeOptions()
           );
           System.out.println(JSON.toJSONString(deleteCrmPersonalCustomerResponse.getBody()));
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

   **参数说明**

   - `dataId`：待删除客户的唯一实例ID。
   - `relationType`：关系类型，固定传"crm\_customer"。
   - `currentOperatorUserId`：当前操作者用户ID。

   **返回字段**

   - `instanceId`：被删除的客户数据ID。
7. **批量获取个人或企业客户数据**：根据客户数据`instanceId`，调用服务端API-[批量获取个人或企业客户数据](1350-acquire-crm-individual-customers-in-batches.md)接口，进行批量获取客户数据信息。

   ```
   public void  getCustomersByInstanceIds() throws Exception {
           Config config = new Config();
           config.protocol = "https";
           config.regionId = "central";
           com.aliyun.dingtalkcrm_1_0.Client client = new com.aliyun.dingtalkcrm_1_0.Client(config);
           ListCrmPersonalCustomersHeaders listCrmPersonalCustomersHeaders = new ListCrmPersonalCustomersHeaders();
           listCrmPersonalCustomersHeaders.xAcsDingtalkAccessToken = "accessToken";
           ListCrmPersonalCustomersRequest listCrmPersonalCustomersRequest = new ListCrmPersonalCustomersRequest()
                   .setCurrentOperatorUserId("m*******5")
                   .setBody(java.util.Arrays.asList(
                           "FPG*****************4161"
                   ));
           try {
               ListCrmPersonalCustomersResponse listCrmPersonalCustomersResponse = client.listCrmPersonalCustomersWithOptions(listCrmPersonalCustomersRequest, listCrmPersonalCustomersHeaders, new RuntimeOptions());
               System.out.println(JSON.toJSONString(listCrmPersonalCustomersResponse.getBody()));
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

   **参数说明**

   - `currentOperatorUserId`：当前操作者用户ID。
   - `body`：待查询客户instanceId列表。

   **返回字段**

   - `result`：客户数据详情列表。
8. **获取全量个人或企业客户数据**：调用服务端API-[获取全量个人或企业客户数据](1351-crm-obtains-all-private-sea-customer-data.md)接口，获取全部客户数据。

   ```
    public void queryAllCustomers() throws Exception {
           Config config = new Config();
           config.protocol = "https";
           config.regionId = "central";
           com.aliyun.dingtalkcrm_1_0.Client client = new com.aliyun.dingtalkcrm_1_0.Client(config);
           QueryAllCustomerHeaders queryAllCustomerHeaders = new QueryAllCustomerHeaders();
           queryAllCustomerHeaders.xAcsDingtalkAccessToken = "<your access token>";
           QueryAllCustomerRequest queryAllCustomerRequest = new QueryAllCustomerRequest()
                   .setOperatorUserId("ding_userid")
                   .setMaxResults(100L)
                   .setNextToken("")
                   .setObjectType("crm_customer");
           try {
               QueryAllCustomerResponse queryAllCustomerResponse = client.queryAllCustomerWithOptions(queryAllCustomerRequest, queryAllCustomerHeaders, new RuntimeOptions());
               System.out.println(JSON.toJSONString(queryAllCustomerResponse.getBody()));
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

   **参数说明**

   - `operatorUserId`：操作者用户ID。
   - `maxResults`：单次查询最大返回条数。
   - `nextToken`：分页游标。
   - `objectType`：对象类型，固定传"crm\_customer"。

   **返回字段**

   - `values`：客户数据详情列表。
   - `nextToken`：下一页分页游标。
   - `maxResults`：每页条目数量。
9. **根据指定条件查询个人或企业客户数据**：调用服务端API-[根据指定条件查询个人或企业客户数据](1352-obtains-crm-individual-customers-in-batches-based-on-specified-query.md)接口，查询符合指定条件的客户数据。

   ```
   public void queryCustomers() throws Exception {
           Config config = new Config();
           config.protocol = "https";
           config.regionId = "central";
           com.aliyun.dingtalkcrm_1_0.Client client = new com.aliyun.dingtalkcrm_1_0.Client(config);
           QueryCrmPersonalCustomerHeaders queryCrmPersonalCustomerHeaders = new QueryCrmPersonalCustomerHeaders();
           queryCrmPersonalCustomerHeaders.xAcsDingtalkAccessToken = "<your access token>";
           QueryCrmPersonalCustomerRequest queryCrmPersonalCustomerRequest = new QueryCrmPersonalCustomerRequest()
                   .setCurrentOperatorUserId("2665246xxx")
                   .setRelationType("crm_customer_personal")
                   .setNextToken("0")
                   .setMaxResults(10)
                   .setQueryDsl("{\"queryGroupList\":[{\"logicType\":\"AND\",\"queryObjectList\":[{\"fieldId\":\"customer_name\",\"filterType\":\"EQ\",\"value\":\"xx有限公司\"}]}]}");
           try {
               QueryCrmPersonalCustomerResponse queryCrmPersonalCustomerResponse = client.queryCrmPersonalCustomerWithOptions(queryCrmPersonalCustomerRequest, queryCrmPersonalCustomerHeaders, new RuntimeOptions());
               System.out.println(JSON.toJSONString(queryCrmPersonalCustomerResponse.getBody()));
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

   **参数说明**

   - `currentOperatorUserId`：当前操作者用户ID。
   - `relationType`：关系类型，如"crm\_customer\_personal"。
   - `nextToken`：分页游标。
   - `maxResults`：单次查询最大返回条数。
   - `queryDsl`：查询条件DSL表达式，JSON格式。

   **返回字段**

   - `values`：符合条件的客户数据详情列表。
   - `nextToken`：下一页分页游标。
   - `hasMore`：是否还有更多数据。
10. **获取个人或企业客户查重字段**：调用服务端API-[获取个人或企业客户查重字段](1353-obtain-duplicate-check-fields.md)接口，获取查重字段数据。

    ```
    public void getRelationUkSetting() throws Exception {
            Config config = new Config();
            config.protocol = "https";
            config.regionId = "central";
            com.aliyun.dingtalkcrm_1_0.Client client = new com.aliyun.dingtalkcrm_1_0.Client(config);
            GetRelationUkSettingHeaders getRelationUkSettingHeaders = new GetRelationUkSettingHeaders();
            getRelationUkSettingHeaders.xAcsDingtalkAccessToken = "<your access token>";
            GetRelationUkSettingRequest getRelationUkSettingRequest = new GetRelationUkSettingRequest()
                    .setRelationType("crm_customer");
            try {
                GetRelationUkSettingResponse relationUkSettingWithOptions = client.getRelationUkSettingWithOptions(getRelationUkSettingRequest, getRelationUkSettingHeaders, new RuntimeOptions());
                System.out.println(JSON.toJSONString(relationUkSettingWithOptions.getBody()));
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

    **参数说明**

    - `relationType`：关系类型，固定传"crm\_customer"。

    **返回字段**

    - `fieldId`：查重字段的字段Id。
    - `bizAlias`：查重字段的别名。

**实施完成检查清单**

- ✅ 企业内部应用创建成功（网页应用）。
- ✅ AppKey和AppSecret获取成功。
- ✅ CRM客户管理接口权限申请成功。
- ✅ accessToken获取成功。
- ✅ 获取客户元数据接口调用成功。
- ✅ 创建单个客户接口调用成功，返回instanceId。
- ✅ 批量新增客户接口调用成功，返回多条instanceId。
- ✅ 更新单个客户接口调用成功。
- ✅ 批量更新客户接口调用成功。
- ✅ 删除客户接口调用成功。
- ✅ 批量获取客户接口调用成功，返回客户详情列表。
- ✅ 全量查询客户接口调用成功，支持分页。
- ✅ 条件查询客户接口调用成功，DSL查询生效。
- ✅ 获取查重字段接口调用成功，返回查重规则配置。

## **常见问题（FAQ）**

- **Q：如何通过钉钉开放平台API创建CRM客户？**

  调用[创建个人或企业客户数据](1345-add-crm-personal-customers.md)接口，传入客户名称、跟进状态、负责人等字段，设置`relationType="crm_customer"`，返回结果中包含新创建客户的`instanceId`。
- **Q：instanceId在钉钉开放平台API中有什么作用？**

  `instanceId`是客户数据的唯一标识符，用于后续的更新、删除、查询等操作。创建客户后需保存该值，作为后续所有客户管理操作的入参。
- **Q：如何通过钉钉开放平台API获取CRM自定义对象的查重字段配置？**

  调用[获取个人或企业客户查重字段](1353-obtain-duplicate-check-fields.md)接口，传入`relationType="crm_customer"`，返回结果中的`result`字段包含当前配置的查重规则，可用于判断哪些字段组合构成重复记录。
- **Q：使用钉钉开放平台API进行批量操作（如批量创建/更新客户）时有哪些关键注意事项？**

  ①必须设置`skipDuplicateCheck=false`才能启用服务端查重校验；②每条记录的`bizDataList`中必须包含`customer_name`字段；③批量操作返回的`resultList`需逐条检查成功状态，失败条目应记录日志并告警。
