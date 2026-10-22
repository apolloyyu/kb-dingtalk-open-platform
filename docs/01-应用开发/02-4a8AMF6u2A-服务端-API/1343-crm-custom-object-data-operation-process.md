---
title: "自定义对象管理：个性化业务数据全生命周期管理"
source_url: "https://open.dingtalk.com/document/development/crm-custom-object-data-operation-process"
namespace: "development"
slug: "crm-custom-object-data-operation-process"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "更多开放 > 客户管理（官方CRM） > 集成方案 > 自定义对象管理：企业个性化业务数据全生命周期操作"
doc_id: "CtYgKI5kQ2"
updated_at: "2026-10-22 17:12:15"
---

> Source: https://open.dingtalk.com/document/development/crm-custom-object-data-operation-process
> Path: 应用开发 / 服务端 API / 更多开放 > 客户管理（官方CRM） > 集成方案 > 自定义对象管理：企业个性化业务数据全生命周期操作
> Updated: 2026-10-22 17:12:15

# 自定义对象管理：个性化业务数据全生命周期管理

## **概述**

本方案基于钉钉CRM自定义对象API，实现企业个性化业务数据的创建、更新、删除与条件查询，支持将非标准业务实体纳入钉钉CRM统一管理。

### **方案背景**

企业在数字化转型过程中，常需管理各类个性化业务数据（如项目台账、设备资产、供应商信息等），这些数据往往无法匹配钉钉CRM预置的标准对象模型。

企业在自定义业务数据管理中常面临以下痛点：

- **数据分散存储**：个性化业务数据散落在Excel、纸质文档或独立系统中，无法与钉钉生态打通。
- **缺乏统一规范**：不同部门自定义字段命名混乱，数据口径不一致导致协同困难。
- **操作效率低下**：手动录入、更新、删除数据耗时费力，且易出错遗漏。
- **查询检索困难**：缺少结构化索引和条件筛选能力，历史数据难以快速定位。

### **核心价值**

本方案通过调用钉钉CRM自定义对象接口，实现个性化业务数据的标准化操作与灵活管理：

- **元数据驱动建模**：动态获取自定义对象字段定义，适配企业个性化配置变化。
- **全生命周期管理**：支持创建、更新、删除、批量获取、条件查询等完整操作链路。
- **权限精细管控**：每条数据可设置负责人与协同人列表，确保数据安全可控。
- **高效批量操作**：单次最多获取200条记录，配合分页游标可完整拉取历史数据。

### **适用场景**

本方案适用于以下典型业务场景：

- **项目台账统一管理**：将分散的项目信息纳入钉钉CRM自定义对象，支持按阶段、负责人等维度检索。
- **设备资产数字化登记**：建立设备资产自定义对象，记录采购日期、维保状态、使用部门等信息。
- **供应商信息集中维护**：创建供应商自定义对象，统一管理资质、联系人、合作历史等关键数据。

## **典型业务场景**

### **场景一：项目台账统一管理与进度追踪**

#### **痛点分析**

某工程企业每年承接数十个项目，目前依赖Excel手工维护项目台账，存在以下问题：

- 项目经理各自维护项目表格，格式不统一导致汇总统计困难。
- 项目阶段变更、负责人调整等信息更新滞后，管理层无法实时掌握进展。
- 跨部门协作时，财务、采购等部门无法查阅项目侧的关键节点信息。
- 历史项目数据缺乏结构化归档，复盘分析时难以快速检索对比。

#### **价值验证**

- **自动化流程**

  ![项目台账统一管理场景图](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5330662971/p1107376.png)
- **核心优势**

  - **项目数据集中沉淀**：外部系统对接钉钉CRM API后，项目立项即自动创建自定义对象记录，无需人工二次录入。
  - **多维度精准检索**：支持按项目名称、阶段、负责人、时间范围等组合查询，秒级定位目标项目。
  - **批量数据高效获取**：单次接口最多返回200条记录，配合分页游标可完整拉取历史项目台账。

### **场景二：设备资产数字化登记与维保提醒**

#### **痛点分析**

某制造企业的设备管理部门在资产登记与维保管理中，面临以下挑战：

- 新购设备信息仅记录在纸质验收单上，未同步至数字化系统，后续维保计划无法关联。
- 设备维保到期依赖人工记忆，部分高价值设备的定期保养被遗忘，影响使用寿命。
- 设备调拨、报废等操作缺乏审批留痕，权责不清导致资产流失风险。
- 管理层无法实时掌握设备分布与使用状态，只能在年度盘点时才发现账实不符。

#### **价值验证**

- **自动化流程**

  ![设备资产数字化登记场景图](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5330662971/p1107377.png)
- **核心优势**

  - **资产信息完整可见**：按设备ID批量拉取所有历史记录，新管理员接手时可快速了解前情。
  - **协同人透明化管理**：每条资产记录包含负责人与协同人列表，权责清晰可追溯。
  - **分页游标连续获取**：支持通过next\_cursor逐页拉取全部历史记录，确保数据无遗漏。

## 实施指南

### **技术架构**

- **接口调用层**：调用CRM自定义对象服务端API实现元数据查询、创建、更新、删除、批量获取、条件检索等操作。
- **应用认证层**：通过Client ID和Client Secret获取accessToken，鉴权调用者身份。
- **自定义对象管理层**：调用CRM自定义对象相关API获取元数据、创建实例、更新/删除数据，获取instance\_id等关键标识符。
- **分页游标管理层**：调用分页游标机制连续拉取全部历史记录，查询has\_more状态判断是否还有下一页。
- **错误处理层**：完善的错误码体系，便于快速定位和解决问题。

### **前置条件**

在实施方案前，需满足以下条件：

- **应用准备**：完成创建[应用创建与配置](../01-XOnnmGCTbn-开发指南/0007-create-application.md)。
- **权限要求**：拥有钉钉企业管理员或子管理员权限，并申请以下接口权限：

  - `qyapi_crm_customdata_read`（CRM自定义对象数据读权限）
  - `qyapi_crm_customdata_write`（CRM自定义对象数据写权限）
  - `qyapi_crm_maindata_write`（CRM主数据写权限）
- **开发环境**：已安装Java开发环境（JDK1.6及以上）及Maven构建工具。
- **SDK准备**：下载钉钉服务端SDK，详情参见[服务端SDK下载](0002-download-the-server-side-sdk.md)，支持Java/Python/Go等多语言。

### **代码实现**

步骤一：获取应用凭证信息，获取应用 Client ID 和 Client Secret。

步骤二：申请接口权限，申请CRM自定义对象相关接口的权限。

步骤三：获取应用访问凭证[获取企业内部应用的accessToken](0032-obtain-the-access-token-of-an-internal-app.md)，调用接口时，通过accessToken鉴权调用者身份。

步骤四：调用服务端CRM自定义对象相关API。

1. 调用服务端API-[获取自定义对象的元数据](1373-get-metadata-description-of-crm-custom-object.md)接口，获取客户管理自定义对象的元数据信息。
2. 调用服务端API-[创建CRM自定义对象数据](1370-dingtalk-paas-master-create-custom-crm-object-data.md)接口，进行自定义对象数据的创建，获取自定义对象数据`instanceId`。
3. 根据自定义对象数据`instanceId`，调用服务端API-[更新自定义对象数据](1372-crm-master-data-opens-interface-for-updating-custom-object-data.md)接口，进行更新自定义对象数据。
4. 根据自定义对象数据`instanceId`，调用服务端API-[删除CRM自定义对象数据](1371-delete-crm-custom-object-data.md)接口，进行删除自定义对象数据。
5. 根据自定义对象数据`instanceId`，调用服务端API-[按照ID列表批量获取CRM自定义表单数据](1375-retrieves-custom-crm-forms-from-the-id-list.md)接口，进行批量获取自定义对象数据信息。
6. 调用服务端API-[根据指定条件查询自定义对象数据](1374-api-getobjectdata.md)接口，查询符合指定条件的自定义对象数据。

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

   - `qyapi_crm_customdata_read`（CRM自定义对象数据读权限）— 用于获取自定义对象元数据、查询及批量拉取自定义对象数据。
   - `qyapi_crm_customdata_write`（CRM自定义对象数据写权限）— 用于创建、更新自定义对象数据。
   - `qyapi_crm_maindata_write`（CRM主数据写权限）— 用于删除自定义对象数据。

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

### 步骤四：核心API调用

1. 获取自定义对象的元数据：调用服务端API-[获取自定义对象的元数据](1373-get-metadata-description-of-crm-custom-object.md)接口，获取客户管理自定义对象的元数据信息。

   ```
   public void getCustomizedObjectMeta() throws Exception {
     DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/crm/objectmeta/describe");
     OapiCrmObjectmetaDescribeRequest req = new OapiCrmObjectmetaDescribeRequest();
     req.setName("PROC-EF1xxxx");
     OapiCrmObjectmetaDescribeResponse rsp = client.execute(req, access_token);
     System.out.println(rsp.getBody());
   }
   ```

   **参数说明**

   - `name`：自定义表单code。

   **返回字段**

   - `name`：对象名称。
   - `fields`：字段列表，包含每个字段的名称、标签、类型、是否可空等信息。
2. **创建CRM自定义对象数据**：调用服务端API-[创建CRM自定义对象数据](1370-dingtalk-paas-master-create-custom-crm-object-data.md)接口，进行自定义对象数据的创建，获取自定义对象数据`instanceId`。

   ```
   public void createCustomizedData() throws Exception {
     DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/crm/objectdata/customobject/create");
     OapiCrmObjectdataCustomobjectCreateRequest req = new OapiCrmObjectdataCustomobjectCreateRequest();
     ObjectDataInstanceVo objectDataInstanceVo = new ObjectDataInstanceVo();
     objectDataInstanceVo.setCreatorUserid("user01");
     objectDataInstanceVo.setData("{\"TextField-xxxxxx\":\"李xx\"}");
     objectDataInstanceVo.setExtendData("{\"field_1\":\"CRM\"}");
     DataPermissionVo dataPermissionVo = new DataPermissionVo();
     dataPermissionVo.setParticipantUserids(Arrays.asList("user01", "user02"));
     objectDataInstanceVo.setPermission(dataPermissionVo);
     objectDataInstanceVo.setFormCode("PROC-A1xxxx");
     req.setInstance(objectDataInstanceVo);
     OapiCrmObjectdataCustomobjectCreateResponse rsp = client.execute(req, access_token);
     System.out.println(rsp.getBody());
   }
   ```

   **参数说明**

   - `creator_userid`：创建人的用户userId。
   - `data`：数据内容，JSON格式字符串。
   - `extend_data`：扩展数据内容。
   - `participant_userids`：协同人的用户userId。
   - `form_code`：自定义对象表单code。

   **返回字段**

   - `instance_id`：自定义对象数据ID。
3. **更新自定义对象数据**：根据自定义对象数据instanceId，调用服务端API-[更新自定义对象数据](1372-crm-master-data-opens-interface-for-updating-custom-object-data.md)接口，进行更新自定义对象数据。

   ```
   public void updateCustomizedData() throws Exception {
     DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/crm/objectdata/customobject/update");
     OapiCrmObjectdataCustomobjectUpdateRequest req = new OapiCrmObjectdataCustomobjectUpdateRequest();
     ObjectDataInstanceVo objectDataInstanceVo = new ObjectDataInstanceVo();
     DataPermissionVo dataPermissionVo = new DataPermissionVo();
     dataPermissionVo.setParticipantUserids(Arrays.asList("user01", "user02"));
     objectDataInstanceVo.setExtendData("{\"field_1\":\"CRM\"}");
     objectDataInstanceVo.setPermission(dataPermissionVo);
     objectDataInstanceVo.setInstanceId("INST_XX");
     objectDataInstanceVo.setFormCode("PROC-EFxxxx");
     objectDataInstanceVo.setModifierUserid("user01");
     objectDataInstanceVo.setModifierNick("张xx");
     req.setInstance(objectDataInstanceVo);
     OapiCrmObjectdataCustomobjectUpdateResponse rsp = client.execute(req, access_token);
     System.out.println(rsp.getBody());
   }
   ```

   **参数说明**

   - `extend_data`：扩展数据内容。
   - `participant_userids`：协同人的用户userId。
   - `instance_id`：自定义对象数据ID。
   - `form_code`：自定义对象表单code。
   - `modifier_userid`：钉钉用户userId。
   - `modifier_nick`：钉钉用户nick。

   **返回字段**

   - `instance_id`：自定义对象数据ID。
4. **删除CRM自定义对象数据**：根据自定义对象数据`instanceId`，调用服务端API-[删除CRM自定义对象数据](1371-delete-crm-custom-object-data.md)接口，进行删除自定义对象数据。

   ```
   public void deleteCustomizedData() throws Exception {
     Config config = new Config();
     config.protocol = "https";
     config.regionId = "central";
     com.aliyun.dingtalkcrm_1_0.Client client = new com.aliyun.dingtalkcrm_1_0.Client(config);
     com.aliyun.dingtalkcrm_1_0.models.DeleteCrmCustomObjectDataHeaders deleteCrmCustomObjectDataHeaders = new com.aliyun.dingtalkcrm_1_0.models.DeleteCrmCustomObjectDataHeaders();
     deleteCrmCustomObjectDataHeaders.xAcsDingtalkAccessToken = "<your access token>";
     com.aliyun.dingtalkcrm_1_0.models.DeleteCrmCustomObjectDataRequest deleteCrmCustomObjectDataRequest = new com.aliyun.dingtalkcrm_1_0.models.DeleteCrmCustomObjectDataRequest()
       .setFormCode("PROC-EFxxxx");
     try {
       DeleteCrmCustomObjectDataResponse deleteCrmCustomObjectDataResponse = client.deleteCrmCustomObjectDataWithOptions("INST_XX", deleteCrmCustomObjectDataRequest, deleteCrmCustomObjectDataHeaders, new RuntimeOptions());
       System.out.println(JSON.toJSONString(deleteCrmCustomObjectDataResponse.getBody()));
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

   - `instanceId`：CRM自定义对象数据ID（路径参数）。
   - `formCode`：自定义对象表单code。

   **返回字段**

   - `instanceId`：删除成功的CRM自定义对象数据ID。
5. **按照ID列表批量获取CRM自定义表单数据**：根据自定义对象数据`instanceId`，调用服务端API-[按照ID列表批量获取CRM自定义表单数据](1375-retrieves-custom-crm-forms-from-the-id-list.md)接口，进行批量获取自定义对象数据信息。

   ```
   public void getCustomizedDatasByInstanceIds() throws Exception {
     DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/crm/objectdata/list");
     OapiCrmObjectdataListRequest req = new OapiCrmObjectdataListRequest();
     req.setCurrentOperatorUserid("user01");
     req.setDataIdList("INST_XX1,INST_XX2");
     req.setName("PROC-EFxxxx");
     OapiCrmObjectdataListResponse rsp = client.execute(req, access_token);
     System.out.println(rsp.getBody());
   }
   ```

   **参数说明**

   - `current_operator_userid`：操作人用户userId。
   - `data_id_list`：数据ID列表，多个用英文逗号隔开。
   - `name`：表单code。

   **返回字段**

   - `instance_id`：数据ID。
   - `data`：数据内容。
   - `owner_userid_list`：负责人用户userId列表。
   - `participant_userid_list`：协同人用户userId列表。
6. **根据指定条件查询自定义对象数据**：调用服务端API-[根据指定条件查询自定义对象数据](1374-api-getobjectdata.md)接口，查询符合指定条件的自定义对象数据。

   ```
   public void queryCustomizedDatas() throws Exception {
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

   - `currentOperatorUserId`：用户userId。
   - `name`：表单code。
   - `queryDsl`：查询条件。

   **返回字段**

   - `values`：数据列表。
   - `instanceId`：数据ID。
   - `data`：数据内容。

**实施完成检查清单**

- ✅ 企业内部应用已创建并获取`Client ID` 和 `Client Secret`。
- ✅ 接口权限`qyapi_crm_customdata_read`、`qyapi_crm_customdata_write`和`qyapi_crm_maindata_write`已申请并通过审批。
- ✅ accessToken获取接口调用正常且缓存机制已实现。
- ✅ 自定义对象元数据接口返回正确的字段结构定义。
- ✅ 创建自定义对象数据接口调用成功并返回`instance_id`。
- ✅ 更新自定义对象数据接口调用成功。
- ✅ 删除自定义对象数据接口调用成功。
- ✅ 按ID列表批量获取自定义对象数据接口返回正确的记录列表。
- ✅ 条件查询自定义对象数据接口调用成功并返回分页数据。
- ✅ 分页游标机制已正确实现，可连续拉取全部数据。
- ✅ `data`字段JSON解析逻辑已就绪，可提取各字段实际值。
- ✅ `permission`权限信息可正确解析负责人与协同人列表。
- ✅ `TeaException`异常处理逻辑已实现，可正确解析`err.code`和`err.message`。

## **常见问题（FAQ）**

- **Q1：自定义对象的form\_code如何获取？**

  `form_code`对应自定义对象的表单编码，可通过"获取自定义对象的元数据"接口返回的`name`字段获取，或在钉钉开发者后台自定义对象管理页面查看。
- **Q2：创建自定义对象数据时data字段的JSON格式如何构造？**

  `data`字段以JSON字符串形式存储，键为字段名称（如TextField-xxxxxx），值为实际数据。字段名称需与元数据接口返回的fields[].name一致。示例：`{"TextField-xxxxxx":"李xx","Select-yyyyyy":"选项A"}`。
- **Q3：分页查询如何判断是否还有下一页？**

  条件查询接口返回结果中包含`hasMore`字段，true表示有下一页，false表示已是最后一页。同时`nextToken`字段提供下一页的游标值，将其作为下一次请求的`nextToken`参数即可继续拉取数据。当`hasMore`为false时停止分页。
- **Q4：删除自定义对象数据后能否恢复？**

  删除操作不可逆，数据删除后无法恢复。建议在删除前做好数据备份，或在业务层增加软删除标记而非直接调用删除接口。
- **Q5：为什么查询结果为空但确认存在自定义对象数据？**

  请检查以下几点：① `currentOperatorUserId`是否正确，该参数决定查询范围；② `name`是否与目标自定义对象表单code一致；③ 操作人是否具有对应数据的查看权限，`ownerUserIds`或`participantUserIds`中需包含当前用户。
