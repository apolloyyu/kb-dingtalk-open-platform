---
title: "联系人管理：个人与企业的联系人全生命周期管理"
source_url: "https://open.dingtalk.com/document/development/crm-contact-data-operation-process"
namespace: "development"
slug: "crm-contact-data-operation-process"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "更多开放 > 客户管理（官方CRM） > 集成方案 > 联系人管理：个人与企业的联系人全生命周期管理"
doc_id: "qd944mJZCf"
updated_at: "2026-10-22 17:12:12"
---

> Source: https://open.dingtalk.com/document/development/crm-contact-data-operation-process
> Path: 应用开发 / 服务端 API / 更多开放 > 客户管理（官方CRM） > 集成方案 > 联系人管理：个人与企业的联系人全生命周期管理
> Updated: 2026-10-22 17:12:12

# 联系人管理：个人与企业的联系人全生命周期管理

## **概述**

通过钉钉开放平台CRM联系人数据操作API，实现联系人数据的创建、批量导入、更新、删除、查询和元数据获取等全生命周期管理，帮助企业构建高效、标准化的联系人数据操作体系。

### **方案背景**

零售电商企业在日常运营中需要频繁管理大量联系人数据，包括线上渠道引流的新客户、线下门店积累的会员信息、合作供应商的联系人资料等。这些联系人数据来源多样、格式不一，人工手动录入不仅效率低下，还容易出现重复、遗漏和格式错误等问题。

企业在日常运营中常面临以下痛点：

- **数据录入效率低**：市场活动获取的批量联系人数据需逐条手动录入CRM，一个百人名单的录入往往耗时数小时，影响后续跟进时效。
- **数据重复率高**：多渠道来源的联系人信息缺乏统一去重机制，同一客户可能被不同渠道多次录入，导致数据冗余和跟进混乱。
- **信息更新滞后**：联系人电话号码、职位、所在企业等信息变更后，CRM中旧数据未及时更新，导致营销触达失败率高。
- **数据查询不便**：缺乏按条件精准筛选联系人的能力，运营人员难以快速定位特定标签或跟进阶段的联系人群体进行定向营销。

### **核心价值**

本方案通过钉钉开放平台CRM联系人数据操作API，为零售电商企业提供联系人数据的标准化操作能力，覆盖从创建、批量导入、更新、删除到查询的完整生命周期。

- **批量导入提效**：通过批量新增接口一次性导入大量联系人数据，将百人名单的录入时间从数小时缩短至分钟级。
- **自动查重去重**：创建联系人时设置查重校验参数，自动拦截重复数据，确保CRM联系人库的干净整洁。
- **灵活条件查询**：支持按标签、跟进阶段、创建时间等维度精准筛选联系人，助力运营团队高效开展分群营销。
- **元数据动态适配**：通过元数据接口获取联系人对象字段定义，自动适配不同企业的自定义字段结构，无需硬编码字段映射。

### **适用场景**

本方案适用于以下典型业务场景：

- **市场活动线索批量入库**：将线上活动、展会等渠道收集的联系人数据批量导入CRM，快速建立跟进流程。
- **会员信息维护与更新**：会员手机号、地址等信息变更后，通过更新接口同步至CRM，确保营销触达准确率。
- **供应商联系人统一管理**：将合作供应商的联系人信息统一录入CRM，按标签分类管理，便于采购团队快速查找。
- **无效联系人定期清理**：通过条件查询筛选长期未互动的联系人，批量删除无效数据，保持CRM联系人库的精简有效。

## **典型业务场景**

### **场景一：市场活动线索批量入库与智能去重（零售电商行业）**

#### **痛点分析**

零售电商企业每月举办多场线上直播和线下展会活动，每场活动可收集数百条潜在客户联系方式。运营团队需要将这些联系人数据录入CRM系统并分配给销售团队跟进。当前做法是运营人员手动逐条录入，一场活动下来的录入工作往往耗费半天时间。更棘手的是，部分联系人可能已在往期活动中录入过CRM，重复录入不仅浪费时间，还导致同一客户被多个销售重复跟进，引起客户反感。

- 百人名单逐条录入耗时3～4小时，严重影响活动后的黄金跟进窗口。
- 缺乏自动去重机制，跨活动重复联系人占比常达15%～20%。
- 手动录入过程中容易出现手机号缺位、姓名错字等格式错误。
- 录入完成后无法快速按活动来源筛选分配，需额外导出Excel手工标记。

#### **价值验证**

- **自动化流程**

  ![场景一-市场活动线索批量入库与智能去重_20261020_111906](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2330662971/p1107153.png)
- **核心优势**

  - **批量导入提效**：通过批量新增接口一次性导入活动收集的数百条联系人数据，将录入时间从半天缩短至5分钟以内，确保销售团队在活动当天即可启动跟进。
  - **自动查重去重**：创建时设置查重校验参数，系统自动拦截已存在的联系人记录，重复联系人零入库，消除多头跟进问题。
  - **来源标签可追溯**：创建时标记活动来源标签，后续可按活动维度一键筛选联系人列表，精准评估各渠道转化效果。

### **场景二：会员信息动态更新与无效数据清理（零售电商行业）**

#### **痛点分析**

零售电商企业的会员信息库维护是一个持续性难题。会员更换手机号后未及时更新，导致促销短信发送失败；会员升职后所在企业信息变更，CRM中仍记录旧职位影响B端客户画像准确性；长期未互动的沉睡会员占据CRM容量，影响系统响应速度和营销精准度。运营团队通常需要每月手动逐条核对和清理，工作量巨大且容易遗漏。

- 会员联系方式变更后未及时更新，营销短信触达失败率高达20%～30%。
- 沉睡会员（超过12个月无互动）占比达30%以上，影响系统性能和营销精准度。
- 手动逐条核对更新效率低，一个运营人员一天最多处理200条记录。
- 批量删除操作缺乏安全校验，曾出现误删活跃会员的事故。

#### **价值验证**

- **自动化流程**

  ![场景二-会员信息动态更新与无效数据清理_20261020_112014](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2330662971/p1107154.png)
- **核心优势**

  - **变更即时同步**：通过更新接口将会员最新联系方式同步至CRM，确保营销触达准确率提升至95%以上。
  - **批量操作安全可控**：更新和删除操作均以联系人实例ID为唯一标识，操作前可先查询确认，避免误操作。
  - **精准筛选清理**：通过条件查询接口按最后互动时间筛选沉睡会员，精准批量删除，保持联系人库精简高效。

## **实施指南**

### **技术架构**

本方案基于钉钉开放平台CRM联系人数据操作API实现，整体架构分为三层：

- **应用接入层**：创建企业内部应用，获取AppKey和AppSecret作为API调用凭证。
- **接口调用层**：调用钉钉开放平台服务端API实现联系人数据的创建、批量导入、更新、删除、查询和元数据获取等操作。
- **数据管理层**：调用钉钉CRM联系人管理相关API完成联系人实例的增删改查，获取instanceId作为联系人唯一标识。

### **前置条件**

- **应用准备**：完成[应用创建与配置](../01-XOnnmGCTbn-开发指南/0007-create-application.md)。
- **权限要求**：拥有钉钉企业管理员或子管理员权限，并申请以下接口权限：

  - `qyapi_crm_maindata_read`（CRM主数据读权限）
  - `qyapi_crm_maindata_write`（CRM主数据写权限）
- **开发环境**：已安装Java开发环境（JDK1.6及以上）及Maven构建工具。
- **SDK准备**：下载钉钉服务端SDK，详情参见[服务端SDK下载](0002-download-the-server-side-sdk.md)，支持Java/Python/Go等多语言。

### **代码实现**

步骤一：获取应用凭证信息，获取应用 Client ID 和 Client Secret。

步骤二：申请接口权限，申请会议相关接口的权限。

步骤三：获取应用访问凭证[获取企业内部应用的accessToken](0032-obtain-the-access-token-of-an-internal-app.md)，调用接口时，通过accessToken鉴权调用者身份。

步骤四：调用核心API：

1. 调用服务端API-[获取联系人的元数据](1361-gets-the-metadata-description-of-a-crm-contact-object.md)接口，获取客户管理联系人元数据信息。
2. 调用服务端API-[批量新增联系人数据](1358-add-contact-data-in-batches.md)接口，进行联系人数据的创建，获取联系人数据`instanceId`（部分接口可能定义为relationId或data\_id，含义相同）。
3. 根据联系人数据`instanceId`进行联系人数据管理操作。

   - 根据联系人数据`instanceId`，调用服务端API-[批量修改联系人数据](1360-modify-contact-data-in-batches.md)接口，进行更新联系人数据。
   - 根据联系人数据`instanceId`，调用服务端API-[删除联系人数据](1359-delete-crm-contact.md)接口，进行删除联系人数据。
   - 根据联系人数据`instanceId`，调用服务端API-[按照ID列表批量获取联系人数据](1363-retrieves-contact-data-in-batches-based-on-the-id-list.md)接口，进行批量获取联系人数据信息。
4. 调用服务端API-[根据指定条件查询联系人数据](1362-api-getcontacts.md)接口，查询符合指定条件的联系人数据。

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

   - `qyapi_crm_maindata_read`（CRM主数据读权限）— 用于获取联系人元数据和查询联系人数据。
   - `qyapi_crm_maindata_write`（CRM主数据写权限）— 用于创建、更新、删除联系人数据。

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

### **步骤四：调用核心API**

1. **获取联系人对象的元数据：**调用服务端API-[获取联系人的元数据](1361-gets-the-metadata-description-of-a-crm-contact-object.md)接口，获取客户管理联系人元数据信息。

   ```
   public void getContactObjectMeta() throws Exception {
     DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/crm/objectmeta/contact/describe");
     OapiCrmObjectmetaContactDescribeRequest req = new OapiCrmObjectmetaContactDescribeRequest();
     OapiCrmObjectmetaContactDescribeResponse rsp = client.execute(req, accessToken);
     System.out.println(rsp.getBody());
   }
   ```

   **参数说明**

   - `access_token`：调用该接口的应用凭证。

   **返回字段**

   - `result`：返回结果，包含对象名称、是否自定义对象、字段列表等信息。
   - `result.fields`：字段列表，每项包含字段名称、字段展示名、字段类型、是否可空、是否引用关联等属性。
2. **批量新增联系人数据**：调用服务端API-[批量新增联系人数据](1358-add-contact-data-in-batches.md)接口，进行联系人数据的创建，获取联系人数据`instanceId`（部分接口可能定义为relationId或data\_id，含义相同）。

   ```
   public void batchAddContacts() throws Exception {
           Config config = new Config();
           config.protocol = "https";
           config.regionId = "central";
           com.aliyun.dingtalkcrm_1_0.Client client = new com.aliyun.dingtalkcrm_1_0.Client(config);
           BatchAddContactsHeaders batchAddContactsHeaders = new BatchAddContactsHeaders();
           batchAddContactsHeaders.xAcsDingtalkAccessToken = "<your access token>";
           java.util.Map<String, String> relationList0BizExtMap = TeaConverter.buildMap(
                   new TeaPair("key", "{}")
           );
           BatchAddContactsRequest.BatchAddContactsRequestRelationListBizDataList relationList0BizDataList0 = new BatchAddContactsRequest.BatchAddContactsRequestRelationListBizDataList()
                   .setKey("contact_name")
                   .setValue("XX有限公司");
           BatchAddContactsRequest.BatchAddContactsRequestRelationListBizDataList relationList0BizDataList1 = new BatchAddContactsRequest.BatchAddContactsRequestRelationListBizDataList()
                   .setKey("contact_related_customer")
                   .setValue("[\"XX公司\"]")
                   .setExtendValue("{\"list\":[{\"instanceId\":\"customerInstanceId\"}]}");
           BatchAddContactsRequest.BatchAddContactsRequestRelationListBizDataList relationList0BizDataList2 = new BatchAddContactsRequest.BatchAddContactsRequestRelationListBizDataList()
                   .setKey("contact_phone")
                   .setValue("185xxxxxxxx");
           BatchAddContactsRequest.BatchAddContactsRequestRelationList relationList0 = new BatchAddContactsRequest.BatchAddContactsRequestRelationList()
                   .setBizDataList(java.util.Arrays.asList(
                           relationList0BizDataList0,
                           relationList0BizDataList1,
                           relationList0BizDataList2
                   ))
                   .setBizExtMap(relationList0BizExtMap);
           BatchAddContactsRequest batchAddContactsRequest = new BatchAddContactsRequest()
                   .setOperatorUserId("manager021a")
                   .setRelationList(java.util.Arrays.asList(
                           relationList0
                   ));
           try {
               BatchAddContactsResponse batchAddContactsResponse = client.batchAddContactsWithOptions(batchAddContactsRequest, batchAddContactsHeaders, new RuntimeOptions());
               System.out.println(JSON.toJSONString(batchAddContactsResponse.getBody()));
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

   - `operatorUserId`：操作人userId。
   - `relationList`：联系人数据列表，最大值10。

   **返回字段**

   - `relationId`：保存成功时返回的联系人relationId。
3. **批量修改联系人数据**：根据联系人数据instanceId，调用服务端API-[批量修改联系人数据](1360-modify-contact-data-in-batches.md)接口，进行更新联系人数据。

   ```
    public void  batchUpdateContacts() throws Exception {
           Config config = new Config();
           config.protocol = "https";
           config.regionId = "central";
           com.aliyun.dingtalkcrm_1_0.Client client = new com.aliyun.dingtalkcrm_1_0.Client(config);
           BatchUpdateContactsHeaders batchUpdateContactsHeaders = new BatchUpdateContactsHeaders();
           batchUpdateContactsHeaders.xAcsDingtalkAccessToken = "<your access token>";
           java.util.Map<String, String> relationList0BizExtMap = TeaConverter.buildMap(
                   new TeaPair("key", "{}")
           );
           BatchUpdateContactsRequest.BatchUpdateContactsRequestRelationListBizDataList relationList0BizDataList0 = new BatchUpdateContactsRequest.BatchUpdateContactsRequestRelationListBizDataList()
                   .setKey("TextField_71U51A")
                   .setValue("XX有限公司")
                   .setExtendValue("{}");
           BatchUpdateContactsRequest.BatchUpdateContactsRequestRelationList relationList0 = new BatchUpdateContactsRequest.BatchUpdateContactsRequestRelationList()
                   .setBizDataList(java.util.Arrays.asList(
                           relationList0BizDataList0
                   ))
                   .setBizExtMap(relationList0BizExtMap)
                   .setRelationId("fasdg8i814-0afsd");
           BatchUpdateContactsRequest batchUpdateContactsRequest = new BatchUpdateContactsRequest()
                   .setOperatorUserId("manager021a")
                   .setRelationList(java.util.Arrays.asList(
                           relationList0
                   ));
           try {
               BatchUpdateContactsResponse batchUpdateContactsResponse = client.batchUpdateContactsWithOptions(batchUpdateContactsRequest, batchUpdateContactsHeaders, new RuntimeOptions());
               System.out.println(JSON.toJSONString(batchUpdateContactsResponse.getBody()));
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

   - `operatorUserId`：操作人userId。
   - `relationList`：联系人数据列表，最大值10。

   **返回字段**

   - `relationId`：更新成功时返回的联系人ID。
4. **删除联系人数据**：根据联系人数据`instanceId`，调用服务端API-[删除联系人数据](1359-delete-crm-contact.md)接口，进行删除联系人数据。

   ```
   public void deleteContact() throws Exception {
     DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/crm/objectdata/contact/delete");
     OapiCrmObjectdataContactDeleteRequest req = new OapiCrmObjectdataContactDeleteRequest();
     req.setOperatorUserid("user01");
     req.setDataId("INST_XX");
     OapiCrmObjectdataContactDeleteResponse rsp = client.execute(req, access_token);
     System.out.println(rsp.getBody());
   }
   ```

   **参数说明**

   - `operator_userid`：操作人用户userId。
   - `data_id`：联系人实例ID，可通过条件查询接口获取。

   **返回字段**

   - `instance_id`：删除的联系人实例ID。
5. **按照ID列表批量获取联系人数据**：根据联系人数据`instanceId`，调用服务端API-[按照ID列表批量获取联系人数据](1363-retrieves-contact-data-in-batches-based-on-the-id-list.md)接口，进行批量获取联系人数据信息。

   ```
   public void getContactsByInstanceIds() throws Exception {
     DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/crm/objectdata/contact/list");
     OapiCrmObjectdataContactListRequest req = new OapiCrmObjectdataContactListRequest();
     req.setCurrentOperatorUserid("manager1");
     req.setDataIdList("nst_Id1, inst_Id2");
     OapiCrmObjectdataContactListResponse rsp = client.execute(req, access_token);
     System.out.println(rsp.getBody());
   }
   ```

   **参数说明**

   - `current_operator_userid`：操作人用户userId。
   - `data_id_list`：数据ID列表，通过条件查询接口获取instance\_id参数值，多个用英文逗号隔开。

   **返回字段**

   - `instance_id`：数据ID。
   - `data`：数据内容。
6. **根据指定条件查询联系人数据**：调用服务端API-[根据指定条件查询联系人数据](1362-api-getcontacts.md)接口，查询符合指定条件的联系人数据。

   ```
   public void queryContacts() throws Exception {
     DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/crm/objectdata/contact/query");
     OapiCrmObjectdataContactQueryRequest req = new OapiCrmObjectdataContactQueryRequest();
     req.setCurrentOperatorUserid("user01");
     req.setCursor("0");
     req.setPageSize(100L);
     req.setProviderCorpid("dingxxx");
     req.setQueryDsl("{\"queryGroupList\":[{\"logicType\":\"AND\",\"queryObjectList\":[{\"fieldId\":\"contact_phone\",\"filterType\":\"EQ\",\"value\":\"18000****000\"},{\"fieldId\":\"contact_related_customer\",\"filterType\":\"EQ\",\"value\":\"INST-XXX\"}]}]}");
     OapiCrmObjectdataContactQueryResponse rsp = client.execute(req, access_token);
     System.out.println(rsp.getBody());
   }
   ```

   **参数说明**

   - `currentOperatorUserId`：用户userId。
   - `objectType`：对象类型，固定值`crm_contact`。
   - `maxResults`：分页大小，最多可一次获取200条数据。
   - `nextToken`：分页游标，用于翻页获取后续数据。
   - `queryDsl`：查询条件，支持按字段ID和值组合过滤。

   **返回字段**

   - `values`：数据列表。
   - `instanceId`：数据ID。
   - `data`：数据内容。

**实施完成检查清单**

- ✅ 企业内部应用已创建并获取AppKey和AppSecret。
- ✅ 接口权限已申请并通过审批。
- ✅ accessToken获取接口调用正常。
- ✅ 联系人元数据获取接口返回正确字段结构。
- ✅ 批量新增联系人接口调用成功并返回relationId。
- ✅ 批量修改联系人接口调用成功。
- ✅ 删除联系人接口调用成功。
- ✅ 按ID列表批量获取联系人接口返回正确的联系人数据。
- ✅ 条件查询联系人接口返回正确的分页数据。
- ✅ 批量操作异常处理机制已就绪。

## **常见问题（FAQ）**

- **Q1：accessToken过期后如何处理？**

  accessToken有效期为7200秒（2小时）。建议在服务端实现Token缓存和自动刷新机制，在Token过期前5分钟主动刷新，避免API调用中断。
- **Q2：批量创建联系人时部分记录失败如何处理？**

  批量创建接口返回的results中会逐条标注成功或失败状态。建议解析results，对失败项提取错误原因后修正数据重新提交，而非整体重试。
- **Q3：如何判断联系人是否已存在以实现去重？**

  创建联系人时设置查重校验参数，系统会自动进行查重校验。若联系人已存在，接口将返回错误提示，不会创建重复记录。
- **Q4：更新联系人时是否需要传入全部字段？**

  不需要。更新接口仅需传入变更的字段，未传入的字段保持不变。但需确保传入的字段键名与元数据接口返回的字段定义一致。
- **Q5：联系人数据删除后能否恢复？**

  钉钉CRM联系人数据删除为物理删除，不可恢复。建议在删除前调用按ID列表批量获取接口备份数据，或在业务系统中保留软删除标记作为兜底方案。
- **Q6：条件查询接口支持哪些筛选维度？**

  条件查询接口支持按手机号、关联客户、跟进状态等字段进行条件筛选，具体支持的筛选字段请参考元数据接口返回的字段定义。查询DSL格式详见钉钉开放平台查询DSL说明文档。
