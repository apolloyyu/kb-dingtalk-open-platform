---
title: "三方业务审批分类集成：待办中心自定义业务分组"
source_url: "https://open.dingtalk.com/document/development/user-defined-approval-business-group-supports-custom-business-classification-in-the"
namespace: "development"
slug: "user-defined-approval-business-group-supports-custom-business-classification-in-the"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "OA 审批 > 集成方案 > 高级专享版 > 三方业务审批分类集成：待办中心自定义业务分组"
doc_id: "NHfanAGPFC"
updated_at: "2026-10-16 09:23:04"
---

> Source: https://open.dingtalk.com/document/development/user-defined-approval-business-group-supports-custom-business-classification-in-the
> Path: 应用开发 / 服务端 API / OA 审批 > 集成方案 > 高级专享版 > 三方业务审批分类集成：待办中心自定义业务分组
> Updated: 2026-10-16 09:23:04

# 三方业务审批分类集成：待办中心自定义业务分组

## **概述**

本方案面向企业多套业务系统审批任务来源混杂、管理层希望在钉钉待办中心按业务维度快速筛选三方审批的场景，通过钉钉OA审批流程中心提供的自定义审批业务分组API，支持三方业务系统将内部业务分组信息同步至钉钉审批中心，并在待办中心【OA审批】分类下生成对应的二级业务来源分组。审批人在查阅三方业务系统来源待办时可按分组精准筛选，提升审批事项繁多的管理层的查阅效率。

### 方案背景

企业规模扩大后审批类型激增（请假、报销、采购、合同、用印等），钉钉待办中心默认按时间排序展示所有待办，员工难以快速定位高优先级或特定业务类型的审批。通过自定义审批业务分组，可按业务域、紧急程度、所属系统等维度对审批进行分类聚合，提升处理效率。

企业在日常运营中常面临以下痛点：

- **待办列表混杂**： 数十种审批类型混排展示，员工需逐条辨认业务类型，重要审批容易被淹没在大量常规审批中。
- **跨系统审批难区分**： 来自OA、费控、HR等不同系统的审批外观一致，员工无法直观识别审批来源和处理 urgency。
- **批量处理效率低**： 同类审批（如批量报销单）无法分组筛选，员工需逐个点开处理，重复操作占比超60%。
- **管理视角缺失**： 部门负责人无法按业务类型查看团队待办分布，人力调配和资源分配缺乏数据依据。

### **核心价值**

本方案的核心价值体现在以下三个方面：

- **业务分组清晰：** 在钉钉待办中心【OA审批】分类下自动生成三方系统的二级业务分组，审批人可按分组快速筛选目标审批任务。
- **分类自动同步：** 三方系统调用API将业务分组信息同步至钉钉，新增/修改分组实时生效，无需手动维护钉钉侧分类结构。
- **灵活扩展：** 支持三方系统自定义分组名称、多语言标签、描述信息，根据业务架构灵活配置多级分组体系。

### **适用场景**

本方案适用于审批任务来源多样、业务线划分清晰的企业管理场景，典型包括：

- **多业务线审批聚合：** 集团型企业拥有多个独立业务单元，各单元使用不同审批系统，管理层希望在钉钉内按业务线维度快速定位待办。
- **高频跨部门审批：** 日常审批涉及采购/人事/财务等多个职能部门，审批人需频繁切换筛选条件查找特定类型审批。
- **待办中心精细化运营：** 企业希望提升钉钉待办中心的用户体验，通过自定义业务分组让审批人更快找到目标任务，减少无效浏览时间。

## **典型业务场景**

### **场景一：智慧农业园区多业态审批分类管理（农业科技行业）**

#### **痛点分析**

某大型智慧农业园区涵盖种植、养殖、农产品加工、农资销售四大业务板块，分别使用自研种植管理系统、养殖物联网平台、ERP加工系统和电商后台处理审批，四套系统审批任务分散运行。园区总经理和各板块负责人每天需处理大量审批，原有流程存在以下问题：

- **业务线混杂难筛选：** 日均审批量80+笔，来自四个业务系统的审批全部涌入钉钉待办中心，无业务维度分类，查找"种植灌溉设备采购"审批需在80+条混合任务中逐条翻看，平均耗时3分钟。
- **跨板块审批响应慢：** 总经理需同时关注四大板块审批进度，传统方式需分别登录四个系统查看，遗漏风险高，紧急事项（如养殖区温控故障维修）响应延迟影响生产安全。
- **待办中心体验差：** 审批人收到OA审批消息卡片后，点击进入待办中心看到的是扁平列表，无法按业务线快速过滤，新入职管理者适应周期长达2周。

#### **价值验证**

- **自动化流程**

  ![智慧农业园区多业态审批分类管理场景图](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3160491971/p1105443.png)
- **关键优势**

  - **分组清晰：** 四大业务线审批自动归类，查找目标审批从3分钟降至5秒，日均节省20分钟筛选时间。
  - **实时同步：** 新增业务分组（如"智慧温室"子分组）调用API即时生效，无需手动维护钉钉侧分类。
  - **多端一致：** PC端/手机端待办中心均显示自定义分组，移动办公时也能快速按业务线筛选审批。

### **场景二：文化传媒集团多频道内容审批分类集成（文化传媒行业）**

#### **痛点分析**

某省级文化传媒集团下设新闻、综艺、体育、纪录片四个内容频道，分别使用自研CMS系统处理稿件审批、版权管理系统处理授权审批、广告系统处理投放审批、财务系统处理预算审批，四套系统审批流程独立运行。总编室主任和各频道总监每天需处理大量审批，原有流程存在以下问题：

- **内容审批混杂：** 日均审批量100+笔，新闻稿/综艺脚本/体育赛事转播权/广告投放合同等审批全部混在钉钉待办中心，总编室主任需快速审核新闻稿但被其他类型审批淹没，重要稿件时效性受损。
- **版权审批易遗漏：** 版权授权审批具有强时效性（过期即失效），在传统扁平列表中容易被其他审批遮挡，曾发生3起版权到期未续导致节目下架事故。
- **频道总监视角缺失：** 各频道总监只关心本频道审批，但待办中心无频道维度过滤，需人工识别每条审批归属，每日浪费30分钟无效浏览。

#### **价值验证**

- **自动化流程**

  ![文化传媒集团多频道内容审批分类集成场景图](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3160491971/p1105444.png)
- **关键优势**

  - **精准筛选：** 四频道审批自动归类，总编室主任查找新闻稿审批从3分钟降至5秒，重要稿件零延误。
  - **版权保障：** 版权授权审批归入专属分组，醒目展示避免遗漏，版权到期事故率降为零。
  - **角色适配：** 各频道总监只看本频道分组，无效浏览时间从30分钟降至零，专注度显著提升。

## **实施指南**

### **技术架构**

本方案的技术架构包含以下核心组件：

- **身份鉴权层：** 负责应用凭证管理和访问令牌获取，确保所有API调用的身份合法性。
- **分组同步层：** 调用创建或更新业务分组接口，将三方业务系统的业务分组信息同步至钉钉审批中心，获取分组唯一编码`dirId`。
- **模板关联层：** 调用保存流程中心外部集成审批模板接口，通过`processFeatureConfig`中的`AFFILIATION_DIR`字段关联步骤返回的`dirId`，建立审批模板与业务分组的绑定关系。
- **任务创建层：** 调用创建/更新审批待办任务接口，将三方系统的审批任务同步至钉钉审批中心，任务自动归属对应业务分组。
- **事件回调层：** 监听审批任务状态变更回调事件，保持三方系统与钉钉审批中心数据一致性。

### **前置条件**

- **应用准备：** 完成[应用创建与配置](../01-XOnnmGCTbn-开发指南/0007-create-application.md)的流程。
- **权限要求：** 拥有钉钉企业管理员或子管理员权限，并申请以下接口权限：

  - `qyapi_aflow`(审批流数据管理权限)
  - `Workflow.Form.Write`（工作流模板写权限）
  - `Workflow.Form.Read`（工作流实例写权限）
  - `Premium.Workflow.ReadWrite.All`（OA审批工作流读写权限）
- **开发环境：** 已安装Java开发环境（JDK1.6及以上）及Maven构建工具。
- **SDK准备：** 下载钉钉服务端SDK，支持Java/Python/Go等多语言。

### **代码实现**

步骤一：进入应用详情页，获取应用 Client ID 和 Client Secret。

步骤二：申请接口权限，申请"OA审批"相应权限。

步骤三：获取应用访问凭证[获取企业内部应用的accessToken](0032-obtain-the-access-token-of-an-internal-app.md)。调用接口时，通过accessToken鉴权调用者身份。

步骤四：调用OA审批相关API：

1. 调用新版服务端API-[创建或更新业务分组](0539-api-premiuminsertorupdatedir.md)接口，获取分组`dirId`。
2. 调用新版服务端API-[保存流程中心外部集成审批模板](0541-api-premiumsaveintegratedprocess.md)接口，获取模板的唯一编码`processCode`。
3. 若未保存`processCode`，可以通过调用[获取模板code](0510-obtain-the-template-code.md)接口获取`processCode`。
4. 创建审批模板成功后，用户可以在钉钉OA审批管理后台，查看三方自有审批单模板、查看/搜索模板数据、导出/删除模板数据等。
5. 根据模板编码`processCode`，调用新版服务端API-[保存流程中心外部集成审批实例](0542-api-premiumexternalintegrationprocessinstance.md)接口发起审批实例，获取审批实例`processInstanceId`。
6. 创建实例成功后，可进入钉钉OA审批中心，查看审批四大列表（待处理、已处理、已发起、我收到的）、搜索审批实例数据、执行审批等操作。
7. 根据`processInstanceId`和`tasks`，调用[保存流程中心外部集成审批任务](0543-api-premiumsaveintegratedtask.md)接口，获取待办事项的taskId并生成对应的钉钉待办任务。
8. 创建待处理任务成功后，调用[查询通过流程中心集成的OA审批任务](0516-query-oa-approval-tasks-integrated-through-process-center.md)接口，可以查询到用户运行中的审批任务。
9. 根据`processInstanceId`和`taskId`，调用[更新流程中心任务状态](0517-update-process-center-task-status.md)接口，同步完成自有审批待办状态的更新。在或签等场景，可以调用[批量取消流程中心待处理任务](0518-cancel-multiple-oa-approval-tasks.md)接口，批量将审批实例下正在运行中的待办事项设置为CANCELED。
10. 根据审批实例`processInstanceId`和`status`、实例结果result等，通过[审批任务开始，结束，转交](../04-LFcRvVD08N-事件订阅/0038-event-bpms-task-change.md)或 [审批实例开始、结束、终止、删除](../04-LFcRvVD08N-事件订阅/0039-event-bpms-instance-change.md)事件，更新实例状态。
11. 若要删除业务分组，调用[删除业务分组](0540-api-premiumdeldir.md)接口，将三方系统同步到钉钉OA审批的分组信息进行删除，并同时删除对应的钉钉待办里OA审批分类下的二级分类。
12. 若需要对审批模板数据进行清理，调用[删除模板](0511-self-owned-approval-deletion-template.md)接口，删除为企业创建的审批模板，同时删除该模板下创建的实例和待办任务。

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

   - `qyapi_aflow`(审批流数据管理权限)：用于查询/更新流程中心任务状态。
   - `Workflow.Form.Write`（工作流模板写权限）：用于获取模板code。
   - `Workflow.Form.Read`（工作流模板读权限）：用于创建/更新审批实、删除模板。
   - `Premium.Workflow.ReadWrite.All`（OA审批工作流读写权限）：用于创建/更新业务分组。

> **[!NOTE]**
>
> 不同业务场景可能需要不同的权限组合，请根据实际需求申请。

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

### **步骤四：核心API调用**

1. **同步审批业务分组到钉钉**：调用新版服务端API-[创建或更新业务分组](0539-api-premiuminsertorupdatedir.md)接口，获取分组`dirId`。可以将三方系统内的业务分组信息同步到钉钉OA审批，并生成对应的钉钉待办里OA审批分类下的二级分类。

   > **[!NOTE]**
   >
   > 后续在同步待处理任务至钉钉时，可支持指定待办任务所属的业务分组信息，让审批人在查阅三方业务系统来源待办更清晰。

   ```
   请求示例：
   {
     "operateUserId":"manager9814",
     "bizGroup":"administeration",
     "name": "测试",
     "name18n": "{\"en_US\":\"test\",\"ja_JP\":\"test\",\"vi_VN\":\"test\",\"zh_CN\":\"测试\",\"zh_HK\":\"测试\",\"zh_TW\":\"测试\"}",
     "description": "自定义审批业务分组测试"
   }

   返回示例：
   {
     "result": {
       "bizGroup": "348925476_administeration20250210",
       "dirId": "194e436699fe71353fc1f3d498f80e66"
     },
     "success": true
   }
   ```

   **请求参数：**

   - `operateUserId`：操作人userid。
   - `bizGroup`：业务分组标识，用于区分不同分组。
   - `name`：分组中文名称。
   - `description`：分组描述信息。

   **返回字段：**

   - `bizGroup`：业务分组完整标识。
   - `dirId`：分组唯一编码，用于后续模板关联。
2. **同步审批模板数据到钉钉**：调用新版服务端API-[保存流程中心外部集成审批模板](0541-api-premiumsaveintegratedprocess.md)接口，获取模板的唯一编码`processCode`。**该场景下需通过processFeatureConfig流程中心集成配置中的****AFFILIATION\_DIR****进行配置步骤1返回的dirId分组信息。**

   ```
   {
     "name": "快捷审批",
     "description": "保存流程中心外部集成审批模板 (高级版专享接口)",
     "formComponents": [
       {
         "componentType": "TextField",
         "props": {
           "componentId": "TextField-1",
           "label": "单行输入框",
           "required": true,
           "bizAlias": "TextField-bizAlias",
           "disabled": false
         }
       }
     ],
     "processFeatureConfig": {
       "features": [
         {
           "name": "AFFILIATION_DIR",
           "runType": "OUTBIZ_CUSTOM",
           "config": "{\"dirId\":\"194e436699fe71353fc1f3d498f80e66\"}"
         }
       ]
     }
   }
   ```

   **请求参数：**

   - `name`：审批模板名称。
   - `description`：模板描述信息。
   - `formComponents`：表单组件配置数组。
   - `processFeatureConfig`：流程中心集成配置，`AFFILIATION_DIR`的`config`值为步骤1返回的`dirId`。

   **返回字段：**

   - `processCode`：审批表单模板唯一编码。
3. 若未保存`processCode`，可以通过调用[获取模板code](0510-obtain-the-template-code.md)接口获取`processCode`。

   ```
   public void getProcessCodeByName() throws Exception {
       Config config = new Config();
       config.protocol = "https";
       config.regionId = "central";

       com.aliyun.dingtalkworkflow_1_0.Client client = new com.aliyun.dingtalkworkflow_1_0.Client(config);

       GetProcessCodeByNameHeaders getProcessCodeByNameHeaders = new GetProcessCodeByNameHeaders();
       getProcessCodeByNameHeaders.xAcsDingtalkAccessToken = "accessToken";

       GetProcessCodeByNameRequest request = new GetProcessCodeByNameRequest()
               .setName("名称");

       try {
           GetProcessCodeByNameResponse getProcessCodeByNameResponse = client.getProcessCodeByNameWithOptions(
                   getProcessCodeByNameRequest,
                   getProcessCodeByNameHeaders,
                   new com.aliyun.teautil.models.RuntimeOptions()
           );
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

   - `name`：模板名称。

   **返回字段：**

   - `processCode`：审批表单模板唯一编码。
4. 创建审批模板成功后，用户可以在钉钉OA审批管理后台，查看三方自有审批单模板、查看/搜索模板数据、导出/删除模板数据等。
5. **同步审批实例数据到钉钉**：根据模板编码`processCode`，调用新版服务端API-[保存流程中心外部集成审批实例](0542-api-premiumexternalintegrationprocessinstance.md)接口发起审批实例，获取审批实例`processInstanceId`。**该场景也支持实例维度指定集成配置，通过featureConfig进行配置步骤1返回的dirId分组信息 。**

   ```
   {
     "formComponentValueList": [
       {
         "name": "单行输入框",
         "value": "[钉钉](https://www.dingtalk.com/)"
       }
     ],
     "title": "自定义分组快捷审批",
     "processCode": "PROC-3602AF75-58DE-4862-9946-321DE45BBAEE",
     "originatorUserId": "manager9814",
     "url": "http://www.dingtalk.com",
     "featureConfig": {
       "features": [
         {
           "name": "AFFILIATION_DIR",
           "runType": "OUTBIZ_CUSTOM",
           "config": "{\"dirId\":\"194e436699fe71353fc1f3d498f80e66\"}"
         }
       ]
     }
   }
   ```

   **请求参数：**

   - `formComponentValueList`：表单组件值列表。
   - `title`：审批实例标题。
   - `processCode`：审批模板唯一编码。
   - `originatorUserId`：发起人userid。
   - `url`：审批详情页跳转地址。
   - `featureConfig`：实例级集成配置，`AFFILIATION_DIR`的`config`值为步骤1返回的`dirId`。

   **返回字段：**

   - `processInstanceId`：审批实例唯一ID。
6. 创建审批实例成功后，用户也可以进入钉钉OA审批中心，查看审批四大列表（待处理、已处理、已发起、我收到的）、搜索审批实例数据、执行审批等操作。
7. **同步审批任务数据到钉钉**：根据`processInstanceId`和`tasks`，调用[保存流程中心外部集成审批任务](0543-api-premiumsaveintegratedtask.md)接口，将三方系统内的审批节点信息同步到钉钉OA审批，获取待办事项的taskId并生成对应的钉钉待办任务，**对应的待办任务将在步骤4指定的业务分组中出现。**

   > **[!NOTE]**
   >
   > 该场景下不指定自定义快捷审批按钮配置的话，同步的审批任务将会以打开业务系统详情页方式进行审批。

   ```
   {
       "processInstanceId": "skFv-tLeTTWObq_vWiezew09641738995784",
       "activityId": "0210-1",
       "tasks": [
           {
               "userId": "manager9814",
               "url": "https://www.dingtalk.com"
           }
       ]
   }
   ```

   **请求参数：**

   - `processInstanceId`：审批实例唯一ID。
   - `activityId`：审批节点活动ID。
   - `tasks`：待办事项列表，包含审批人userid和详情页URL。

   **返回字段：**

   - `taskId`：审批待办任务唯一ID。
8. 创建待处理任务成功后，调用[查询通过流程中心集成的OA审批任务](0516-query-oa-approval-tasks-integrated-through-process-center.md)接口，可以查询到用户运行中的审批任务。

   ```
       public void getPremiumRedirectTasksByManager() throws Exception {
           Config config = new Config();
           config.protocol = "https";
           config.regionId = "central";
           com.aliyun.dingtalkworkflow_1_0.Client client = new com.aliyun.dingtalkworkflow_1_0.Client(config);
           QueryIntegratedTodoTaskHeaders queryIntegratedTodoTaskHeaders = new QueryIntegratedTodoTaskHeaders();
           queryIntegratedTodoTaskHeaders.xAcsDingtalkAccessToken = "<your access token>";
           QueryIntegratedTodoTaskRequest queryIntegratedTodoTaskRequest = new QueryIntegratedTodoTaskRequest()
                   .setUserId("manager001")
                   .setPageSize(1)
                   .setPageNumber(1)
                   .setCreateBefore(1660036833411L);
           try {
               QueryIntegratedTodoTaskResponse queryIntegratedTodoTaskWithOptions = client.queryIntegratedTodoTaskWithOptions(queryIntegratedTodoTaskRequest, queryIntegratedTodoTaskHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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

   - `userId`：任务执行人的用户userId。
   - `pageSize`：分页大小，从1开始，最大值40。
   - `pageNumber`：页码，从1开始。
   - `createBefore`：查询的时间起点。

   **返回字段：**

   - `list`：任务列表，包含taskId（OA审批任务ID）、activityId（待办组ID）、processInstanceId（流程实例ID）等。
9. **同步审批任务状态到钉钉：**根据审批实例`processInstanceId`和审批待办任务taskId，可以调用[更新流程中心任务状态](0517-update-process-center-task-status.md)接口，同步完成自有审批待办状态的更新。

   ```
   public void getPremiumGetDoneTasks() throws Exception {
     Config config = new Config();
     config.protocol = "https";
     config.regionId = "central";
     com.aliyun.dingtalkworkflow_1_0.Client client = new com.aliyun.dingtalkworkflow_1_0.Client(config);
     UpdateIntegratedTaskHeaders updateIntegratedTaskHeaders = new UpdateIntegratedTaskHeaders();
     updateIntegratedTaskHeaders.xAcsDingtalkAccessToken = "<your access token>";
     UpdateIntegratedTaskRequest.UpdateIntegratedTaskRequestTasks tasks0 = new UpdateIntegratedTaskRequest.UpdateIntegratedTaskRequestTasks();
     tasks0.setTaskId(1234567L);
     tasks0.setStatus("COMPLETED");
     UpdateIntegratedTaskRequest updateIntegratedTaskRequest = new UpdateIntegratedTaskRequest()
       .setProcessInstanceId("S3j8rbiNT1CsXXXXXV3Q1Q04431661334483")
       .setTasks(java.util.Arrays.asList(
         tasks0
       ));
     try {
       UpdateIntegratedTaskResponse updateIntegratedTaskWithOptions = client.updateIntegratedTaskWithOptions(updateIntegratedTaskRequest, updateIntegratedTaskHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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

   - `processInstanceId`：OA审批流程实例ID。
   - `taskId`：OA审批任务ID。
   - `status`：更新为目标任务状态。

   **返回字段：**

   - `success`：更新结果。

   在或签等场景，可以调用[批量取消流程中心待处理任务](0518-cancel-multiple-oa-approval-tasks.md)接口，批量将审批实例下正在运行中的待办事项设置为CANCELED。

   ```
   public void getCancelIntegratedTask() throws Exception {
     Config config = new Config();
     config.protocol = "https";
     config.regionId = "central";
     com.aliyun.dingtalkworkflow_1_0.Client client = new com.aliyun.dingtalkworkflow_1_0.Client(config);
     CancelIntegratedTaskHeaders cancelIntegratedTaskHeaders = new CancelIntegratedTaskHeaders();
     cancelIntegratedTaskHeaders.xAcsDingtalkAccessToken = "<your access token>";
     CancelIntegratedTaskRequest cancelIntegratedTaskRequest = new CancelIntegratedTaskRequest()
       .setProcessInstanceId("S3j8rbiNT1CsXXXXXV3Q1Q04431661334483")
       .setActivityId("act_xxxx");
     try {
       CancelIntegratedTaskResponse cancelIntegratedTaskWithOptions = client.cancelIntegratedTaskWithOptions(cancelIntegratedTaskRequest, cancelIntegratedTaskHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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

   - `processInstanceId`：OA审批流程实例ID。
   - `activityId`：待办组ID。

   **返回字段：**

   - `success`：操作是否成功。
10. **同步审批实例状态到钉钉：**根据审批实例`processInstanceId`和实例状态status、实例结果result等，可以通过[审批任务开始，结束，转交](../04-LFcRvVD08N-事件订阅/0038-event-bpms-task-change.md)或 [审批实例开始、结束、终止、删除](../04-LFcRvVD08N-事件订阅/0039-event-bpms-instance-change.md)事件，更新实例状态。
11. **删除业务分组：**若需删除业务分组，调用[删除业务分组](0540-api-premiumdeldir.md)接口，将三方系统同步到钉钉OA审批的分组信息进行删除，并同时删除对应的钉钉待办里OA审批分类下的二级分类，对应分类下的钉钉待办数据将移动至OA审批分类下的【其他】分组。
12. 若需要对审批模板数据进行清理，可以调用[删除模板](0511-self-owned-approval-deletion-template.md)接口，删除为企业创建的审批模板，同时删除该模板下创建的实例和待办任务。

    ```
    public void deleteProcessHeaders() throws Exception {
      Config config = new Config();
      config.protocol = "https";
      config.regionId = "central";
      com.aliyun.dingtalkworkflow_1_0.Client client = new com.aliyun.dingtalkworkflow_1_0.Client(config);
      DeleteProcessHeaders deleteProcessHeaders = new DeleteProcessHeaders();
      deleteProcessHeaders.xAcsDingtalkAccessToken = "<your access token>";
      DeleteProcessRequest deleteProcessRequest = new DeleteProcessRequest()
        .setProcessCode("proc-abc")
        .setCleanRunningTask(false);
      try {
        DeleteProcessResponse deleteProcessResponse = client.deleteProcessWithOptions(deleteProcessRequest, deleteProcessHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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

    - `processCode`：模板code。
    - `cleanRunningTask`：是否清理正在运行的任务。

    **返回字段：**

    - `processCode`：模板code。

**实施完成检查清单**

- ✅ 应用已完成创建并获取Client ID和Client Secret。
- ✅ 已申请`qyapi_aflow`、`Workflow.Form.Write`、`Workflow.Form.Read`、`Premium.Workflow.ReadWrite.All`权限。
- ✅ accessToken获取成功且缓存策略已配置。
- ✅ 业务分组创建成功并获取dirId。
- ✅ 审批模板保存成功且AFFILIATION\_DIR正确关联dirId。
- ✅ 审批待办任务创建成功且自动归属对应业务分组。
- ✅ 审批实例回调事件注册并正常接收。
- ✅ 钉钉待办中心【OA审批】分类下显示自定义二级分组。
- ✅ 审批人可按分组精准筛选三方系统来源待办。
- ✅ 多语言分组名称在各语言环境下正确显示。
- ✅ 新增/修改分组实时同步至钉钉审批中心。
- ✅ 权限过滤生效，不同角色用户看到差异化审批任务。

## **常见问题（FAQ）**

- **Q：一个三方系统最多可以创建几个业务分组？**

  单个应用最多支持创建10个业务分组。建议根据实际业务线数量合理规划，避免过度细分导致审批人选择困惑。
- **Q：业务分组创建后是否可以修改名称？**

  可以。再次调用创建或更新业务分组接口，传入相同的`bizGroup`标识和新的`name`即可更新分组名称。
- **Q：删除业务分组后，已关联的审批任务如何处理？**

  删除业务分组不会删除已创建的审批任务和模板，但这些任务将失去分组归属，在待办中心显示为未分组状态。建议删除前先确认无活跃任务关联。
