---
title: "跟进记录管理：销售拜访数据自动归档与智能查询"
source_url: "https://open.dingtalk.com/document/development/crm-follow-up-record-data-operation-process"
namespace: "development"
slug: "crm-follow-up-record-data-operation-process"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "更多开放 > 客户管理（官方CRM） > 集成方案 > 跟进记录管理：销售拜访数据自动归档与智能查询"
doc_id: "d3t5nVXO1X"
updated_at: "2026-10-22 17:12:13"
---

> Source: https://open.dingtalk.com/document/development/crm-follow-up-record-data-operation-process
> Path: 应用开发 / 服务端 API / 更多开放 > 客户管理（官方CRM） > 集成方案 > 跟进记录管理：销售拜访数据自动归档与智能查询
> Updated: 2026-10-22 17:12:13

# 跟进记录管理：销售拜访数据自动归档与智能查询

## **概述**

本方案基于钉钉CRM跟进记录API，实现销售拜访数据的自动化获取、条件查询与批量检索，帮助企业将分散的线下跟进记录统一沉淀到钉钉CRM系统中。

### **方案背景**

销售团队在日常客户拜访过程中产生的大量跟进记录，是衡量客户关系维护质量与销售转化效率的关键数据资产。然而在实际业务中，这些宝贵的跟进信息往往散落在个人笔记、聊天记录或零散的Excel表格中，未能形成统一、可检索、可分析的结构化数据体系。

企业在客户跟进管理中常面临以下痛点：

- **跟进记录分散**：销售人员通过微信、邮件、纸质笔记等多种方式记录拜访信息，数据难以集中管理和追溯。
- **查询效率低下**：历史跟进记录缺乏结构化索引，按客户、时间、拜访方式等维度筛选耗时费力。
- **协同信息断层**：团队成员无法实时查看同一客户的跟进历史，重复沟通或遗漏关键节点频发。
- **数据分析缺失**：非结构化的跟进记录无法支撑拜访频次、转化漏斗等量化分析，管理层决策缺乏数据依据。

### **核心价值**

本方案通过调用钉钉CRM跟进记录接口，实现跟进数据的标准化采集与灵活查询：

- **数据集中沉淀**：所有拜访记录统一存储于钉钉CRM系统，支持多维度检索与历史追溯。
- **条件精准查询**：支持按客户、联系人、拜访方式等字段组合筛选，快速定位目标记录。
- **批量高效获取**：单次最多获取200条跟进记录，大幅降低接口调用次数与等待时间。
- **元数据驱动扩展**：动态获取跟进记录对象字段定义，适配企业自定义字段配置变化。

### **适用场景**

本方案适用于以下典型业务场景：

- **销售拜访记录自动归档**：外部CRM或OA系统定时同步拜访记录至钉钉CRM，形成统一数据资产。
- **客户服务跟进全链路留痕**：客服团队按客户ID批量拉取历史跟进记录，确保服务连续性。
- **管理层拜访数据分析**：定期导出指定时间段内的跟进记录，支撑拜访频次、转化率等经营分析。

## **典型业务场景**

### **场景一：销售拜访记录自动归档与智能查询**

#### **痛点分析**

某制造企业销售团队每月产生超过500条客户拜访记录，目前依赖Excel手工汇总，存在以下问题：

- 销售人员在拜访结束后需手动填写Excel表格，格式不统一导致后续统计困难。
- 新入职销售无法快速获取老客户的完整跟进历史，重复询问客户已提供过的信息。
- 销售经理每周花费数小时人工核对拜访记录的完整性与准确性。
- 跨部门协作时，生产、采购等部门无法查阅销售侧的客户沟通记录，信息传递延迟。

#### **价值验证**

- **自动化流程**

  ![销售拜访记录自动归档场景图](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3330662971/p1107363.png)
- **核心优势**

  - **拜访记录自动沉淀**：外部系统对接钉钉CRM API后，拜访结束即自动创建跟进记录，无需人工二次录入。
  - **多条件精准检索**：支持按客户、联系人、拜访方式、时间范围等组合查询，秒级定位目标记录。
  - **批量数据高效获取**：单次接口最多返回200条记录，配合分页游标可完整拉取历史数据。

### **场景二：客户服务跟进全链路留痕与协同提醒**

#### **痛点分析**

某零售电商企业的客服团队在处理客户投诉与售后问题时，面临以下挑战：

- 同一客户多次来电投诉，不同客服无法查看之前的处理记录，导致重复询问客户问题细节。
- 复杂问题需要跨部门协同处理，但协同人列表仅存在于个人笔记中，交接时容易遗漏。
- 客户满意度回访依赖人工记忆，部分高价值客户的回访被遗忘，影响客户关系维护。
- 客服主管无法实时掌握团队跟进进度，只能在月度复盘时才发现积压工单。

#### **价值验证**

- **自动化流程**

  ![客户服务跟进全链路留痕场景图](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3330662971/p1107359.png)
- **核心优势**

  - **跟进历史完整可见**：按客户ID批量拉取所有历史跟进记录，新客服接手时可快速了解前情。
  - **协同人透明化管理**：每条跟进记录包含负责人与协同人列表，权责清晰可追溯。
  - **分页游标连续获取**：支持通过next\_cursor逐页拉取全部历史记录，确保数据无遗漏。

## **实施指南**

### **技术架构**

- **接口调用层**：调用CRM跟进记录服务端API实现元数据查询、条件检索、批量获取等操作。
- **应用认证层**：通过Client ID和Client Secret获取accessToken，鉴权调用者身份。
- **跟进记录管理层**：调用CRM跟进记录相关API获取元数据、按条件查询及按ID批量拉取，获取instance\_id等关键标识符。
- **分页游标管理层**：调用分页游标机制连续拉取全部历史记录，查询has\_more状态判断是否还有下一页。
- **错误处理层**：完善的错误码体系，便于快速定位和解决问题。

### **前置条件**

在实施方案前，需满足以下条件：

- **应用准备**：完成企业内部应用的创建与配置，参考[应用创建与配置](../01-XOnnmGCTbn-开发指南/0007-create-application.md)。
- **权限要求**：拥有钉钉企业管理员或子管理员权限，并申请以下接口权限：

  - `qyapi_crm_maindata_read` （CRM主数据读权限）
- **开发环境**：已安装Java开发环境（JDK1.6及以上）及Maven构建工具。
- **SDK准备**：下载钉钉服务端SDK，详情参见[服务端SDK下载](0002-download-the-server-side-sdk.md)，支持Java/Python/Go等多语言。

### **代码实现**

步骤一：获取应用凭证信息，获取应用 Client ID 和 Client Secret。

步骤二：申请接口权限，申请CRM跟进记录相关接口的权限。

步骤三：调用[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口，通过accessToken鉴权调用者身份。

步骤四：调用服务端CRM跟进记录相关API。

1. 调用服务端API-[获取跟进记录对象的元数据](1367-obtains-the-metadata-description-of-the-crm-follow-up-record-object.md)接口，获取客户管理跟进记录元数据信息。
2. 调用服务端API-[根据指定条件查询跟进记录数据](1371-query-and-dingtalk-data-of-track-records-in-apsara-stack.md)接口，查询符合指定条件的跟进记录数据。
3. 调用服务端API-[根据ID列表批量获取跟进记录数据](1372-dingtalk-the-primary-data-of-apsara-stack-agility-paas-allows-you.md)接口，查询多个跟进记录数据。

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

   - `qyapi_crm_maindata_read` （CRM主数据读权限）— 用于获取跟进记录元数据、查询及批量拉取跟进记录数据。

> **[!NOTE]**
>
> 不同业务场景可能需要不同的权限组合，请根据实际需求申请。例如批量导入场景还需申请批量操作用户的相关权限。

### 步骤三：获取访问凭证（accessToken）

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

**最佳实践**：

- **缓存策略**：`accessToken`有效期为2小时，建议在内存或Redis中缓存，过期前5分钟主动刷新。
- **并发控制**：避免多个线程同时刷新token导致冲突，可使用分布式锁机制。
- **异常重试**：网络波动时自动重试，最多3次，间隔递增（1s → 2s → 4s）。

### **步骤四：核心API调用**

1. **获取跟进记录对象的元数据**：调用服务端API-[获取跟进记录对象的元数据](1367-obtains-the-metadata-description-of-the-crm-follow-up-record-object.md)接口，获取客户管理跟进记录元数据信息。

   ```
   public void customerFollowRecordObjectMeta() throws Exception {
     DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/crm/objectmeta/followrecord/describe");
     OapiCrmObjectmetaFollowrecordDescribeRequest req = new OapiCrmObjectmetaFollowrecordDescribeRequest();
     OapiCrmObjectmetaFollowrecordDescribeResponse rsp = client.execute(req, access_token);
     System.out.println(rsp.getBody());
   }
   ```

   **参数说明**

   - `access_token`：调用该API的应用凭证，通过获取企业内部应用的access\_token接口获取。

   **返回字段**

   - `name`：对象名称，固定为`crm_follow_record`。
   - `customized`：是否为自定义对象，`true`表示是，`false`表示否。
   - `fields`：字段列表，包含每个字段的名称、标签、类型、是否可空等信息。
2. **根据指定条件查询跟进记录数据**：调用服务端API-[根据指定条件查询跟进记录数据](1371-query-and-dingtalk-data-of-track-records-in-apsara-stack.md)接口，查询符合指定条件的跟进记录数据。

   ```
   public void queryCustomerFollowRecord() throws Exception {
     DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/crm/objectdata/followrecord/query");
     OapiCrmObjectdataFollowrecordQueryRequest req = new OapiCrmObjectdataFollowrecordQueryRequest();
     req.setCurrentOperatorUserid("user01");
     req.setCursor("0");
     req.setPageSize(100L);
     OapiCrmObjectdataFollowrecordQueryResponse rsp = client.execute(req, access_token);
     System.out.println(rsp.getBody());
   }
   ```

   **参数说明**

   - `current_operator_userid`：用户userId，标识当前操作人。
   - `cursor`：分页游标，首次查询传"0"，后续使用返回的next\_cursor值。
   - `page_size`：分页大小，单次最多200条。
   - `query_dsl`：查询条件，格式参考钉钉开放平台查询DSL说明文档。

   **返回字段**

   - `values`：数据列表，包含多条跟进记录详情。
   - `instance_id`：数据ID，唯一标识一条跟进记录。
   - `creator_userid`：创建记录的用户userId。
   - `creator_nick`：创建记录的用户昵称。
   - `data`：数据内容，JSON字符串格式，包含各字段实际值。
   - `extend_data`：扩展数据内容，JSON字符串格式。
   - `object_type`：数据类型，固定为crm\_follow\_record。
3. **根据ID列表批量获取跟进记录数据**：调用服务端API-[根据ID列表批量获取跟进记录数据](1372-dingtalk-the-primary-data-of-apsara-stack-agility-paas-allows-you.md)接口，查询多个跟进记录数据。

   ```
   public void getCustomerFollowRecordByInstanceIds() throws Exception {
     DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/crm/objectdata/followrecord/list");
     OapiCrmObjectdataFollowrecordListRequest req = new OapiCrmObjectdataFollowrecordListRequest();
     req.setCurrentOperatorUserid("user01");
     req.setDataIdList("INST_XX1,INST_XX2");
     OapiCrmObjectdataFollowrecordListResponse rsp = client.execute(req, access_token);
     System.out.println(rsp.getBody());
   }
   ```

   **参数说明**

   - `current_operator_userid`：操作人用户userId。
   - `data_id_list`：数据ID列表，多个ID用英文逗号隔开，可通过条件查询接口获取`instance_id`参数值。

   **返回字段**

   - `result_list`：实例数据列表，包含多条跟进记录详情。
   - `instance_id`：数据ID，唯一标识一条跟进记录。
   - `creator_userid`：记录创建人的用户ID。
   - `creator_nick`：记录创建人的昵称。
   - `data`：数据内容，JSON字符串格式，包含各字段实际值。
   - `extend_data`：扩展数据内容，JSON字符串格式。
   - `object_type`：数据类型，固定为`crm_follow_record`。

**实施完成检查清单**

- ✅ 企业内部应用已创建并获取`AppKey`和`AppSecret`。
- ✅ 接口权限`qyapi_crm_maindata_read`已申请并通过审批。
- ✅ accessToken获取接口调用正常且缓存机制已实现。
- ✅ 跟进记录元数据接口返回正确的字段结构定义。
- ✅ 条件查询跟进记录接口调用成功并返回分页数据。
- ✅ 按ID列表批量获取跟进记录接口返回正确的记录列表。
- ✅ 分页游标机制已正确实现，可连续拉取全部数据。
- ✅ `data`字段JSON解析逻辑已就绪，可提取各字段实际值。
- ✅ `permission`权限信息可正确解析负责人与协同人列表。
- ✅ `TeaException`异常处理逻辑已实现，可正确解析`err.code`和`err.message`。

## **常见问题（FAQ）**

- **Q1：条件查询接口的query\_dsl参数如何构造？**

  `query_dsl`参数遵循钉钉开放平台查询DSL规范，基本结构为`{"filterGroupJSONType":"AND","needCount":"true","groupLogicType":"AND"}`。如需按具体字段过滤，需在`queryGroupList`中添加`queryObjectList`，每个对象包含`fieldId`和`value`。详细语法请参考钉钉开放平台查询DSL说明文档。
- **Q2：分页查询如何判断是否还有下一页？**

  条件查询接口返回结果中包含`has_more`字段，true表示有下一页，false表示已是最后一页。同时`next_cursor`字段提供下一页的游标值，将其作为下一次请求的`cursor`参数即可继续拉取数据。当`has_more`为false时停止分页。
- **Q3：跟进记录的data字段为何是JSON字符串而非对象？**

  `data`字段以JSON字符串形式存储，是因为跟进记录对象可能包含企业自定义字段，字段数量和类型不固定。调用方需自行解析该JSON字符串，根据元数据接口返回的fields定义来识别各字段含义。
- **Q4：为什么查询结果为空但确认存在跟进记录？**

  请检查以下几点：① `current_operator_userid`是否正确，该参数决定查询范围；② `query_dsl`中的`fieldId`是否与元数据接口返回的字段名称一致；③ 操作人是否具有对应数据的查看权限，`permission.owner_userid_list`或`participant_userid_list`中需包含当前用户。
