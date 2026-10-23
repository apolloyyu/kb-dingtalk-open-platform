---
title: "智能人事花名册管理：员工信息获取与补全"
source_url: "https://open.dingtalk.com/document/development/realize-automatic-push-of-employee-birthday-wishes-information"
namespace: "development"
slug: "realize-automatic-push-of-employee-birthday-wishes-information"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "智能人事 > 集成方案 > 智能人事花名册管理：员工信息获取与补全"
doc_id: "jLES1yAEEK"
updated_at: "2026-10-16 09:23:15"
---

> Source: https://open.dingtalk.com/document/development/realize-automatic-push-of-employee-birthday-wishes-information
> Path: 应用开发 / 服务端 API / 智能人事 > 集成方案 > 智能人事花名册管理：员工信息获取与补全
> Updated: 2026-10-16 09:23:15

# 智能人事花名册管理：员工信息获取与补全

## **概述**

本方案基于钉钉开放平台智能人事API，介绍如何通过服务端接口实现员工花名册字段信息的获取、元数据查询及信息更新。企业通过调用智能人事相关API，可批量获取员工花名册中的指定字段（如民族、籍贯等），对缺失字段进行自动识别并通过元数据匹配完成补全，适用于环保科技企业、法律事务所等多种组织场景，确保员工档案信息的完整性和准确性。

### **方案背景**

企业在人力资源管理中常面临员工花名册信息不完整的问题：部分员工入职时未填写民族、籍贯等字段，后续补录依赖人工逐一核对效率低下；花名册字段的选项值（如民族编码）与实际显示值之间的映射关系不透明，手动更新容易出错；跨系统同步时因字段缺失导致数据不一致，影响报表统计和合规审计。钉钉智能人事API提供了花名册字段查询、元数据获取和信息更新的完整链路，使企业能够程序化地完成员工信息的获取与补全。

### **核心价值**

- **花名册信息一键获取：** 通过API批量查询指定员工的花名册字段信息，无需登录管理后台逐一查看，信息查询效率提升90%以上。
- **缺失字段智能识别：** 自动检测花名册中为空的目标字段，精准定位需要补全的员工记录，避免人工排查遗漏。
- **元数据动态匹配：** 获取花名册字段的选项元数据（如民族编码与名称的对应关系），确保更新时使用正确的value值，杜绝手动输入错误。
- **批量补全零遗漏：** 通过API批量更新缺失字段信息，一次调用即可完成多名员工的信息补全，确保花名册数据100%完整。

### **适用场景**

- **环保科技企业合规审计：** 环保工程公司需向监管部门提交员工花名册用于资质审核，通过API批量获取并补全所有员工的民族、籍贯等信息，确保审计材料完整合规。
- **律师事务所人员档案管理：** 律所按执业证申领要求需完善律师花名册中的民族、政治面貌等字段，通过API自动识别缺失项并批量补全，减少行政人员手工录入工作量。
- **会计师事务所年审准备：** 事务所在年度审计前需核实全体员工花名册信息完整性，通过API快速扫描缺失字段并一键补全，缩短审计准备周期。
- **政府机关人事统计上报：** 机关单位定期向上级报送人员编制花名册，通过API自动获取并校验字段完整性，对缺失信息进行标准化补全后再行上报。

## **典型业务场景**

### **场景一：环保科技企业员工花名册合规补全（环保科技行业）**

#### **痛点分析**

某环保工程公司拥有300+员工，每年需向生态环境部门提交完整的人员花名册用于企业资质年审。原有流程存在以下问题：

- **信息缺失难发现：** HR需在管理后台逐人打开花名册检查民族、籍贯等字段是否填写，300人逐一排查耗时3天，仍有约8%的缺失记录被遗漏。
- **补录易出错：** 民族字段为下拉选择型，HR手动输入时频繁出现"汉族"写成"汉"、编码与名称不对应等错误，年审时被退回修改2次。
- **跨系统不同步：** 花名册补全后需手动导出再导入OA系统，因格式差异导致15条记录丢失，二次核对又耗费1天。

#### **价值验证**

- **自动化流程**

  ![环保科技企业员工花名册合规补全场景图](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5973112971/p1105794.png)
- **关键优势**

  - **花名册信息一键获取：** 300人员工花名册字段信息通过API批量查询，排查时间从3天缩短至5分钟，效率提升99%。
  - **缺失字段智能识别：** 系统自动标记所有民族字段为空的员工记录，遗漏率从8%降为零。
  - **批量补全零遗漏：** 通过元数据匹配确保编码准确，批量更新后花名册完整率达100%，年审一次通过。

### **场景二：律师事务所执业人员档案标准化管理（法律服务行业）**

#### **痛点分析**

某中型律师事务所拥有80+执业律师及助理，司法局要求每季度上报完整的人员花名册用于执业证年检。原有流程存在以下问题：

- **字段标准不统一：** 不同时期入职的律师花名册中民族字段填写格式不一（有的填"汉族"、有的填"1"、有的留空），行政人员需逐条人工校对，季度上报前耗费2天整理。
- **新入职补录滞后：** 新律师入职后花名册信息未及时完善，等到季度上报时才发现缺失，紧急补录压力大且易出错。
- **历史数据纠错困难：** 已提交的错误数据无法追溯原始值，只能联系律师本人确认后再手动修改，沟通成本高且响应慢。

#### **价值验证**

- **自动化流程**

  ![律师事务所执业人员档案标准化管理场景图_20261014_104859](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5973112971/p1105815.png)
- **关键优势**

  - **员工档案实时查询：** 入职即触发花名册完整性检查，缺失字段当场识别并提示补全，季度上报前整理时间从2天缩短至30分钟。
  - **元数据动态匹配：** 所有字段更新均通过元数据API获取标准选项值，填写格式统一率达100%，杜绝人工输入错误。
  - **信息更新即时生效：** 补全操作通过API实时写入花名册，无需导出导入，数据同步延迟从1天降为零。

## **实施指南**

### **技术架构**

本方案的技术架构包含以下核心组件：

- **身份鉴权层：** 负责应用凭证管理和访问令牌获取，确保所有服务端调用的身份合法性。
- **花名册查询层：** 实现员工花名册字段信息的批量获取，支持按指定字段代码精确查询目标数据。
- **元数据管理层：** 提供花名册字段的选项元数据查询能力，返回字段类型、可选值列表及编码映射关系。
- **信息更新层：** 实现员工花名册信息的程序化更新，支持按字段代码和标准value值精确写入。

### **前置条件**

- **应用准备：** 完成[应用创建与配置](../01-XOnnmGCTbn-开发指南/0007-create-application.md)的流程。
- **权限要求：** 申请以下接口权限：

  - `qyapi_hrm_read_user`（智能人事花名册读权限）
  - `qyapi_hrm_manager`（智能人事花名册管理权限）
- **开发环境：** 已安装Java开发环境（JDK 8及以上版本）。
- **SDK准备：** [服务端SDK下载](0002-download-the-server-side-sdk.md)，版本建议最新稳定版。

### **代码实现**

步骤一：获取应用凭证信息，获取应用 Client ID 和 Client Secret。

步骤二：申请接口权限，申请智能人事相关接口的权限。

步骤三：获取应用访问凭证[获取企业内部应用的accessToken](0032-obtain-the-access-token-of-an-internal-app.md)，通过accessToken鉴权调用者身份。

步骤四：调用服务端智能人事和工作通知相关API：

1. 调用服务端API-[获取员工花名册字段信息](0940-api-getemployeerosterbyfield.md)接口，获取员工的民族。
2. 如果获取员工民族的字段为空，说明该员工的民族字段没有填写，调用服务端API-[获取花名册元数据](0938-intelligent-personnel-roster-metadata-query.md)接口，获取员工花名册字段元数据值。
3. 调用服务端API-[更新员工花名册信息](0941-intelligent-personnel-update-employee-file-information.md)接口，更新员工的民族信息。

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

   - `qyapi_hrm_read_user`（智能人事花名册读权限）— 用于获取员工花名册字段信息、获取花名册元数据。
   - `qyapi_hrm_manager`（智能人事花名册管理权限）— 用于更新员工花名册信息。

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

### **步骤四：核心API调用**

1. 调用服务端API-[获取员工花名册字段信息](0940-api-getemployeerosterbyfield.md)接口，获取员工信息。

   ```
   public void getEmployeeRosterByField() throws Exception {
       Config config = new Config();
       config.protocol = "https";
       config.regionId = "central";

       com.aliyun.dingtalkhrm_1_0.Client client = new com.aliyun.dingtalkhrm_1_0.Client(config);

       GetEmployeeRosterByFieldHeaders getEmployeeRosterByFieldHeaders = new GetEmployeeRosterByFieldHeaders();
       getEmployeeRosterByFieldHeaders.xAcsDingtalkAccessToken = "<your access token>";

       GetEmployeeRosterByFieldRequest getEmployeeRosterByFieldRequest = new GetEmployeeRosterByFieldRequest()
               .setUserIdList(java.util.Arrays.asList("userId123"))
               .setAppAgentId(1234L);

       try {
           GetEmployeeRosterByFieldResponse getEmployeeRosterByFieldResponse = client.getEmployeeRosterByFieldWithOptions(
                   getEmployeeRosterByFieldRequest,
                   getEmployeeRosterByFieldHeaders,
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

   解析返回值中的label值，可以拿到员工的民族信息。

   ```
   {
     "field_code": "sys02-nationType",
     "field_name": "民族",
     "field_value_list": [
       {
         "item_index": 0,
         "label": "阿昌族",
         "value": "40"
       }
     ],
     "group_id": "sys02"
   }
   ```

   **请求参数：**

   - `userid_list`：待查询的员工userId列表。
   - `appAgentId`：应用的AgentId。

   **返回字段：**

   - `fieldCode`：字段代码标识。
   - `fieldName`：字段中文名称。
   - `fieldValueList`：字段值列表，包含label（字段取值）和value（字段展示值）。
2. 如果未获取到民族字段信息，调用服务端API-[获取花名册元数据](0938-intelligent-personnel-roster-metadata-query.md)接口，获取的民族字段元数据信息。

   ```
   public void smartworkHrmRosterMetaGet() throws ApiException {
     DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/smartwork/hrm/roster/meta/get");
     OapiSmartworkHrmRosterMetaGetRequest req = new OapiSmartworkHrmRosterMetaGetRequest();
     req.setAgentid(123456L);
     OapiSmartworkHrmRosterMetaGetResponse rsp = client.execute(req, "access_token");
     System.out.println(rsp.getBody());
   }
   ```

   ```
   {
     "field_code":"sys02-nationType",
     "field_name":"民族",
     "field_type":"DDSelectField",
     "option_text":"[{\"label\":\"汉族\",\"value\":\"1\"},{\"label\":\"阿昌族\",\"value\":\"40\"},{\"label\":\"白族\",\"value\":\"15\"},{\"label\":\"保安族\",\"value\":\"49\"},{\"label\":\"布朗族\",\"value\":\"36\"},{\"label\":\"布依族\",\"value\":\"11\"},{\"label\":\"朝鲜族\",\"value\":\"14\"},{\"label\":\"穿青人\",\"value\":\"57\"},{\"label\":\"傣族\",\"value\":\"19\"},{\"label\":\"达斡尔族\",\"value\":\"33\"},{\"label\":\"德昂族\",\"value\":\"45\"},{\"label\":\"侗族\",\"value\":\"12\"},{\"label\":\"东乡族\",\"value\":\"24\"},{\"label\":\"独龙族\",\"value\":\"52\"},{\"label\":\"鄂伦春族\",\"value\":\"51\"},{\"label\":\"俄罗斯族\",\"value\":\"47\"},{\"label\":\"鄂温克族\",\"value\":\"42\"},{\"label\":\"高山族\",\"value\":\"56\"},{\"label\":\"亻革家人\",\"value\":\"58\"},{\"label\":\"仡佬族\",\"value\":\"22\"},{\"label\":\"哈尼族\",\"value\":\"16\"},{\"label\":\"哈萨克族\",\"value\":\"18\"},{\"label\":\"赫哲族\",\"value\":\"54\"},{\"label\":\"回族\",\"value\":\"4\"},{\"label\":\"景颇族\",\"value\":\"34\"},{\"label\":\"京族\",\"value\":\"43\"},{\"label\":\"基诺族\",\"value\":\"44\"},{\"label\":\"柯尔克孜族\",\"value\":\"32\"},{\"label\":\"拉祜族\",\"value\":\"23\"},{\"label\":\"黎族\",\"value\":\"17\"},{\"label\":\"傈僳族\",\"value\":\"21\"},{\"label\":\"珞巴族\",\"value\":\"55\"},{\"label\":\"满族\",\"value\":\"3\"},{\"label\":\"毛南族\",\"value\":\"37\"},{\"label\":\"蒙古族\",\"value\":\"9\"},{\"label\":\"门巴族\",\"value\":\"50\"},{\"label\":\"苗族\",\"value\":\"5\"},{\"label\":\"仫佬族\",\"value\":\"31\"},{\"label\":\"纳西族\",\"value\":\"27\"},{\"label\":\"怒族\",\"value\":\"41\"},{\"label\":\"普米族\",\"value\":\"39\"},{\"label\":\"羌族\",\"value\":\"28\"},{\"label\":\"撒拉族\",\"value\":\"35\"},{\"label\":\"畲族\",\"value\":\"20\"},{\"label\":\"水族\",\"value\":\"26\"},{\"label\":\"塔吉克族\",\"value\":\"38\"},{\"label\":\"塔塔尔族\",\"value\":\"53\"},{\"label\":\"土家族\",\"value\":\"8\"},{\"label\":\"土族\",\"value\":\"29\"},{\"label\":\"佤族\",\"value\":\"25\"},{\"label\":\"维吾尔族\",\"value\":\"6\"},{\"label\":\"乌孜别克族\",\"value\":\"46\"},{\"label\":\"锡伯族\",\"value\":\"30\"},{\"label\":\"瑶族\",\"value\":\"13\"},{\"label\":\"彝族\",\"value\":\"7\"},{\"label\":\"裕固族\",\"value\":\"48\"},{\"label\":\"藏族\",\"value\":\"10\"},{\"label\":\"壮族\",\"value\":\"2\"}]"
   }
   ```

   **请求参数：**

   - `agentid`：应用agentId。

   **返回字段：**

   - `field_code`：字段代码标识。
   - `field_type`：字段类型，`TextField`（文本）、`DDPhotoField`（附件）、`DDSelectField`（选项）
   - `option_text`：选项值JSON字符串，包含所有可选的label-value对。
3. 根据民族字段元数据信息的value值，调用服务端API-[更新员工花名册信息](0941-intelligent-personnel-update-employee-file-information.md)接口，更新员工的民族信息。

   > **[!NOTE]**
   >
   > [更新员工花名册信息](0941-intelligent-personnel-update-employee-file-information.md)接口，指定value值，员工的民族组队值会更新为对应的label值，例如更新张三的民族信息时，指定value值为1，张三的民族信息会显示为对应的汉族。

   ```
   public void smartworkHrmEmployeeV2Update() throws ApiException {
       DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/smartwork/hrm/employee/v2/update");
       OapiSmartworkHrmEmployeeV2UpdateRequest request = new OapiSmartworkHrmEmployeeV2UpdateRequest();
       request.setAgentid(23470561L);

       // 构建字段
       List<EmpFieldVo> fieldVos = new ArrayList<>();
       EmpFieldVo fieldVo = new EmpFieldVo();
       fieldVo.setFieldCode("test");
       fieldVo.setValue("测试");
       fieldVos.add(fieldVo);

       // 构建分区
       List<EmpListFieldVo> sections = new ArrayList<>();
       EmpListFieldVo section = new EmpListFieldVo();
       section.setSection(fieldVos);
       section.setOldIndex(0L);
       sections.add(section);

       // 构建分组
       List<EmpGroupFieldVo> groups = new ArrayList<>();
       EmpGroupFieldVo group = new EmpGroupFieldVo();
       group.setGroupId("asdsad");
       group.setSections(sections);
       groups.add(group);

       // 组装更新参数
       EmpUpdateByCustomParam param = new EmpUpdateByCustomParam();
       param.setUserid("user456");
       param.setGroups(groups);

       request.setParam(param);

       System.out.println(JSON.toJSONString(param, true));

       OapiSmartworkHrmEmployeeV2UpdateResponse rsp = client.execute(request, token);
       System.out.println(rsp.getBody());
   }
   ```

   **请求参数：**

   - `agentid`：应用的AgentId。
   - `userid`：待更新的员工userId。
   - `section`：花名册字段分组更新数据，包含field\_code和value。

   **返回字段：**

   - `success`：操作是否成功的布尔值。

**实施完成检查清单**

- ✅ 已完成应用创建并获取Client ID和Client Secret。
- ✅ 已申请`qyapi_hrm_read_user`和`qyapi_hrm_manager`接口权限。
- ✅ 已成功获取accessToken并能正常调用接口。
- ✅ 已成功获取员工花名册字段信息并正确解析返回值。
- ✅ 已成功获取花名册元数据并解析选项值映射关系。
- ✅ 已成功更新员工花名册信息并验证更新结果。

## **常见问题（FAQ）**

- **Q1：获取员工花名册字段信息时返回为空是什么原因？**

  返回为空说明该员工对应的花名册字段尚未填写。此时应调用获取花名册元数据接口获取该字段的标准选项值列表，再通过更新接口补全信息。
- **Q2：更新花名册信息时value值和label值有什么区别？**

  value值是系统内部编码（如"1"代表汉族），label值是前端显示文本（如"汉族"）。更新接口需传入value值，系统会自动将其转换为对应的label值显示。传入错误的value值会导致更新失败或显示异常。

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5973112971/p1105813.png)
- **Q3：如何获取花名册中所有可用的字段代码？**

  调用获取花名册元数据接口可返回当前企业花名册中所有字段的元数据信息，包括field\_code、field\_name和field\_type。
- **Q4：批量更新花名册信息有数量限制吗？**

  单次更新接口调用针对单个员工。批量更新时建议在业务层循环调用并合理控制调用频率，避免触发平台限流。具体频率限制请参考钉钉开放平台API调用指南。
- **Q5：花名册字段信息更新后多久生效？**

  更新接口调用成功后即时生效，再次调用获取员工花名册字段信息接口即可查到最新值。无需等待同步或刷新缓存。
