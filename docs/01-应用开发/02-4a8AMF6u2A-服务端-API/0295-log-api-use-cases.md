---
title: "日志数据自动化集成：从业务系统到钉钉日志的无缝流转"
source_url: "https://open.dingtalk.com/document/development/log-api-use-cases"
namespace: "development"
slug: "log-api-use-cases"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "日志 > 使用教程 > 日志数据自动化集成：从业务系统到钉钉日志的无缝流转"
doc_id: "N0slg35yJ3"
updated_at: "2026-09-23 12:04:39"
---

> Source: https://open.dingtalk.com/document/development/log-api-use-cases
> Path: 应用开发 / 服务端 API / 日志 > 使用教程 > 日志数据自动化集成：从业务系统到钉钉日志的无缝流转
> Updated: 2026-09-23 12:04:39

# 日志数据自动化集成：从业务系统到钉钉日志的无缝流转

本文档介绍企业使用自有系统或第三方应用如何通过钉钉开放平台API实现日志的自动创建、发送及阅读情况查询，支持将业务系统中的周报、日报等数据自动同步至钉钉日志模块，实现统一工作汇报管理。

## 概述

本方案提供一套完整的钉钉日志集成解决方案，通过调用钉钉开放平台的日志相关API，实现在第三方系统中直接发起钉钉日志、查看日志阅读情况等功能，支持两种日志创建模式（编辑后发送/直接发送）及回调通知机制。

> **[!NOTE]**
>
> 本案例实现仅支持钉钉PC客户端内实现，手机端暂不支持。

### 方案背景

企业在日常运营中常面临以下痛点：

- **日志手动创建耗时**：业务系统中已生成的周报、日报数据，仍需人工在钉钉日志中重新填写，重复操作效率极低。
- **数据孤岛阻碍协同**：业务系统数据与钉钉日志未打通，无法基于已有数据自动生成日志内容。
- **阅读状态难追踪**：日志发送后无法实时掌握接收人的阅读情况（已读人数、评论数、点赞数等）。
- **流程断点影响体验**：从业务系统跳转到钉钉填写日志时，需手动复制粘贴内容，用户体验割裂。

### 核心价值

本方案提供一套完整的钉钉日志集成解决方案，通过调用钉钉开放平台的日志相关API，实现在第三方系统中直接发起钉钉日志、查看日志阅读情况等功能。

- **日志自动创建**：业务系统确定日志内容后一键同步至钉钉日志，无需人工重新填写，大幅提升汇报效率。
- **双模式灵活选择**：支持"编辑后发送"和"直接发送"两种模式，满足不同业务场景需求。
- **阅读状态实时追踪**：支持查询日志的已读人数、评论条数、点赞人数等数据，形成完整的汇报闭环。
- **回调通知机制**：日志提交成功后自动回调业务系统，实现日志ID关联和数据同步。

### 适用场景

本方案适用于以下典型业务场景：

- **CRM系统销售周报自动生成**：销售人员完成客户拜访后，CRM系统自动汇总本周工作数据生成周报草稿并跳转至钉钉日志完善后发送。
- **项目管理系统日报自动同步**：项目管理工具中的任务完成情况自动组装为日报内容，直接发送至钉钉日志供团队成员查看。
- **HR系统绩效日志集成**：员工绩效考核数据自动填充至钉钉日志模板，简化绩效汇报流程。
- **日志阅读数据分析**：管理层通过API批量获取团队日志的阅读情况，评估信息传达效果。

## 典型业务场景

### 场景一：CRM系统销售周报自动生成并跳转编辑

#### 痛点分析

销售团队每周需在CRM系统中整理客户拜访记录，但仍需在钉钉日志中手动填写周报：

- CRM系统中的拜访数据无法自动带入钉钉日志，需人工复制粘贴
- 周报格式不统一，难以进行跨部门数据统计和分析
- 管理者无法实时掌握团队成员周报提交情况和阅读反馈
- 缺乏统一的日志阅读状态视图，难以评估信息传达效果

#### 价值验证

- **自动化流程**

  ![CRM销售周报生成流程图](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9726310971/p1103457.png)
- **关键优势**

  - **数据自动填充**：CRM系统自动汇总本周拜访记录生成周报草稿，减少80%的手动录入工作量。
  - **灵活编辑完善**：跳转至钉钉日志页面后可继续补充细节，兼顾自动化与灵活性。
  - **提交后自动关联**：日志提交成功通过回调URL通知CRM系统，自动关联日志ID便于后续追溯。

### 场景二：项目管理系统日报直接发送

#### 痛点分析

项目团队成员每日需在项目管理工具中更新任务进度，但仍需在钉钉日志中单独汇报：

- 任务进度数据分散在多个系统中，日报编写需多次切换应用
- 日报内容重复率高，大量时间浪费在复制粘贴上
- 缺乏统一的日报阅读反馈机制，难以了解团队成员的关注度
- 历史日报数据难以统计分析，无法发现工作效率趋势

#### 价值验证

- **自动化流程**

  ![项目管理日报发送流程图](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9726310971/p1103458.png)
- **关键优势**

  - **一键直接发送**：后端自动组装日报内容并调用API创建日志，用户无需任何手动操作。
  - **图片自动上传**：支持上传图片至钉钉获取mediaId，确保日报中的截图正常显示。
  - **阅读数据实时查看**：支持查询日志的已读人数、评论数、点赞数，形成完整的数据闭环。

## 实施指南

### 技术架构

- **接口调用层**：调用日志服务端API实现日志内容的保存、创建及阅读情况查询操作。
- **模板管理层**：调用日志模板相关API获取模板详情，确保日志内容符合企业规范。
- **文件上传层**：调用文件上传API处理日志中的图片等资源，获取mediaId用于内容组装。
- **URL拼接层**：根据业务需求拼接钉钉日志填写页面的跳转URL，支持自定义回调地址。
- **回调通知层**：实现回调URL接口接收日志提交成功的通知，完成日志ID关联。
- **错误处理层**：完善的错误码体系，便于快速定位和解决问题。

### 前置条件

在实施方案前，需满足以下条件：

- 应用准备：完成企业内部应用的创建与配置，参考[应用创建与配置](../01-XOnnmGCTbn-开发指南/0007-create-application.md)。
- 权限要求：拥有钉钉企业管理员或子管理员权限，并申请以下接口权限：

  - `qyapi_report_query`（日志查询权限）
  - `qyapi_report_manage`（日志管理权限）
- 开发环境：已安装Java开发环境（JDK1.6及以上）及Maven构建工具。
- SDK准备：下载钉钉服务端SDK，详情参见[服务端SDK下载](0002-download-the-server-side-sdk.md)，支持Java/Python/Go等多语言。
- 模板准备：手动在钉钉的日志中创建一个日志模板，用于后续API调用。

### 代码实现

步骤一：获取应用凭证信息，获取应用 Client ID 和 Client Secret。

步骤二：申请接口权限，查找"日志"相关权限并申请。

步骤三：获取应用访问凭证[获取企业内部应用的access\_token](1444-obtain-orgapp-token.md)。调用接口时，通过accessToken鉴权调用者身份。

步骤四：手动在钉钉的日志中创建一个日志模板。

步骤五：调用日志相关API：

a. 调用[保存日志内容](0297-save-custom-log-content.md)接口，获取contentId（编辑后发送模式）。

b. 拼接URL，在三方系统页面内访问该URL，跳转进入日志发起页面。

c. 或直接调用[创建日志](0296-create-a-log.md)接口，实现日志的直接发送。

d. 调用获取日志阅读情况接口，查看日志的已读人数、评论数等数据。

## 实施步骤

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

   - `qyapi_report_query`（日志查询权限）— 用于查询日志阅读情况。
   - `qyapi_report_manage`（日志管理权限）— 用于创建和管理日志。

> **[!NOTE]**
>
> 不同业务场景可能需要不同的权限组合，请根据实际需求申请。例如批量导入场景还需申请批量操作用户的相关权限。

### 步骤三：获取访问凭证（accessToken）

根据步骤一中 的 Client ID 和 Client Secret，获取应用访问凭证[获取企业内部应用的accessToken](0032-obtain-the-access-token-of-an-internal-app.md)。

```
public String getAccessToken() {
    com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
    config.protocol = "https";
    config.regionId = "central";
    try {
        com.aliyun.dingtalkoauth2_1_0.Client client = new com.aliyun.dingtalkoauth2_1_0.Client(config);
        GetAccessTokenRequest getAccessTokenRequest = new GetAccessTokenRequest()
                .setAppKey("dingeqqpkv3xxxxxx")
                .setAppSecret("GT-lsu-taDAxxxsTsxxxx");
        GetAccessTokenResponse response = client.getAccessToken(getAccessTokenRequest);
        System.out.println(response.getBody());
        return response.getBody().getAccessToken();
    } catch (Exception e) {
        throw new RuntimeException(e);
    }
}
```

**最佳实践**：

- **缓存策略**：`accessToken`有效期为2小时，建议在内存或Redis中缓存，过期前5分钟主动刷新。
- **并发控制**：避免多个线程同时刷新token导致冲突，可使用分布式锁机制。
- **异常重试**：网络波动时自动重试，最多3次，间隔递增（1s → 2s → 4s）。

### **步骤四：创建日志模板**

手动在钉钉的日志中创建一个日志模板。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5600089071/p776197.png)

### **步骤五：核心API调用**

#### **模式一：编辑后发送**

主体流程是在企业内部系统中，点击“生成周报”的时候：

1. 获取要生成的模板的详情，根据模板和周报内容组装对应的内容，并调用开放平台的接口上传内容，开放平台会返回对应的contentId。
2. 拼接写日志页面的url，跳转到钉钉日志的写日志页面。
3. 在写日志页面进行编辑（可选），选择接收人后进行发送。
4. 发送完，触发对应企业的回调url，通知已发出的日志id。

调用流程图如下：![编辑后在发送流程](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8221943871/p162641.png)

> **[!NOTE]**
>
> 开放平台已开通上传图片接口。

1. **保存日志内容获取contentId**：调用[保存日志内容](0297-save-custom-log-content.md)接口，获取contentId。

   ```
   public void reportSavecontent() throws ApiException {
     DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/report/savecontent");
     OapiReportSavecontentRequest req = new OapiReportSavecontentRequest();
     OapiCreateReportParam obj1 = new OapiCreateReportParam();
     List<OapiReportContentVo> list3 = new ArrayList<OapiReportContentVo>();
     OapiReportContentVo obj4 = new OapiReportContentVo();
     list3.add(obj4);
     obj4.setSort(0L);
     obj4.setType(1L);
     obj4.setContentType("markdown");
     obj4.setContent("### 序号1");
     obj4.setKey("字段1");
     obj1.setContents(list3);
     obj1.setTemplateId("12345abcde");
     obj1.setDdFrom("report");
     obj1.setUserid("12345");
     req.setCreateReportParam(obj1);
     OapiReportSavecontentResponse rsp = client.execute(req, access_token);
     System.out.println(rsp.getBody());
   }
   ```
2. **拼接跳转URL**：拼接URL，在三方系统页面内访问该URL，可以跳转进入日志发起页面，拼接的URL如下：

   ```
   dingtalk://dingtalkclient/action/openapp?corpid={corpid}&container_type=work_platform&app_id=2&redirect_type=jump&redirect_url="+encodeURIComponent("https://landray.dingtalkapps.com/alid/app/reportpc/createreport.html?corpid={corpid}&templateid={templateid}&contentid={contentid}&callbackUrl={callback_url}&dd_from=ThirdParty")
   ```

   **URL参数说明**：

   - `corpId`：该日志模板所在企业的CorpId，登录[钉钉开发者后台](https://open-dev.dingtalk.com/)获取。
   - `container_type`：固定值`work_platform`。
   - `app_id`：固定值`2`。
   - `templateid`：日志模板Id，调用[获取模板详情](0298-query-template-details.md)接口获取。
   - `contentid`：调用[保存日志内容](0297-save-custom-log-content.md)接口返回的contentId。
   - `redirect_url`：跳转的日志提交页面地址，**必须encodeURL处理**。
   - `callbackUrl`：第三方自己提供的回调URL，用于用户提交日志成功之后通知第三方生成的日志ID。
   - `dd_from`：固定为`ThirdParty`。

   **callbackUrl的说明：**提交日志成功时，钉钉服务器会以GET请求的方式请求构造的回调URL。

   例如，开发者构造的回调URL为`http://www.dingtalk.com/callback`，提交日志时，钉钉服务器的请求为：

   ```
   GET  http://www.dingtalk.com/callback?reportId=17d6xxxxxx
   ```

   开发者构造回调URL的示例如下

   ```
   @RestController
   public class reportCallBack {
     @RequestMapping(value = "/callback",method = RequestMethod.GET)
     public void report(@RequestParam(value = "reportId")String reportId){
       System.out.println(reportId);
     }
   }
   ```
3. 拼接好的URL，在企业自有系统内访问跳转，即可打开钉钉填写日志页面，如下图所示。

   ![同步日志](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3244199951/p162640.png)

#### **模式二：直接发送**

在企业内部系统中点击"生成周报"时，后端直接调用API创建并发送日志，用户无需任何手动操作：

1. 后端先调用开放平台接口获取模板详情。
2. 调用开放平台接口上传周报中的图片，获取上传图片后的mediaId。
3. 根据模板字段组装日志内容(包括上传图片后的mediaId)，再调用开放平台接口创建日志。
4. 钉钉日志创建并发送完日志后，会返回对应的日志id。

调用流程图如下：

![直接发送流程](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8221943871/p162647.png)

1. **获取模板详情**：调用[获取模板详情](0298-query-template-details.md)接口，获取日志模板的结构和字段定义。

   ```
   public void reportTemplateGetbyname() throws ApiException {
     DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/report/template/getbyname");
     OapiReportTemplateGetbynameRequest req = new OapiReportTemplateGetbynameRequest();
     req.setUserid("12345");
     req.setTemplateName("日报");
     OapiReportTemplateGetbynameResponse rsp = client.execute(req, access_token);
     System.out.println(rsp.getBody());
   }
   ```
2. **上传图片获取mediaId**：调用开放平台接口上传周报中的图片，获取上传图片后的`mediaId`。
3. **组装日志内容并创建日志**：根据模板字段组装日志内容（包括上传图片后的mediaId），再调用开放平台接口[创建日志](0296-create-a-log.md)并发送完日志后，会返回对应的日志id。

   ```
   public void reportTemplateGetbyname() throws ApiException {
     DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/report/create");
     OapiReportCreateRequest req = new OapiReportCreateRequest();
     OapiCreateReportParam obj1 = new OapiCreateReportParam();
     List<OapiReportContentVo> list3 = new ArrayList<OapiReportContentVo>();
     OapiReportContentVo obj4 = new OapiReportContentVo();
     list3.add(obj4);
     obj4.setSort(0L);
     obj4.setType(1L);
     obj4.setContentType("markdown");
     obj4.setContent("### 序号1");
     obj4.setKey("字段1");
     obj1.setContents(list3);
     obj1.setToUserids(""123","456"");
     obj1.setTemplateId("12345abcde");
     obj1.setToChat(true);
     obj1.setDdFrom("report");
     obj1.setUserid("12345");
     obj1.setToCids(""123","456"");
     req.setCreateReportParam(obj1);
     OapiReportCreateResponse rsp = client.execute(req, access_token);
     System.out.println(rsp.getBody());
   }
   ```

#### 查看日志阅读情况

获取日志的阅读情况，包含已读人数、评论条数、评论人数和点赞人数等，并供企业员工查看。

1. 企业开通日志，员工使用日志并提交周报、日报等。
2. 各部门日志填报完成后，企业内部可以通过[数据资产平台](../../07-数据资产/01-fIz0pQ6X4y-平台介绍/0001-dataopen-overview.md)获取日志相关数据。

**实施完成检查清单**：

- ✅ 应用凭证获取成功（Client ID / Client Secret）。
- ✅ 日志读写权限申请成功。
- ✅ access\_token获取成功。
- ✅ 日志模板创建成功。
- ✅ 编辑后发送模式测试成功，能正确跳转至钉钉日志页面。
- ✅ 直接发送模式测试成功，日志已正确创建并发送。
- ✅ 回调URL配置正确，能正确接收日志ID通知。
- ✅ 日志阅读情况查询成功，返回正确的统计数据。

## 常见问题（FAQ）

- **Q1：为什么手机端暂不支持本流程？**

  A：本流程的案例实现仅支持钉钉PC客户端内实现，手机端暂不支持。这是当前API的技术限制，建议引导用户在PC端完成日志相关操作。
- **Q2：如何获取日志模板ID？**

  A：调用[获取模板详情](0298-query-template-details.md)接口可获取日志模板ID。也可在钉钉日志管理后台查看已创建的模板列表获取模板ID。
- **Q3：callbackUrl的作用是什么？**

  A：callbackUrl是第三方自己提供的回调URL，用于用户提交日志成功之后，通知第三方生成的日志ID。第三方可以基于此ID拼接成日志详情页的URL，关联到钉钉里面的日志详情。钉钉服务器会在提交日志成功之后以GET请求触发回调。
- **Q4：两种日志创建模式如何选择？**

  A：

  - **编辑后发送模式**：适合需要用户在钉钉日志页面进行二次编辑完善的场景，灵活性高但需用户手动操作。
  - **直接发送模式**：适合完全自动化的场景，后端组装好内容后直接发送，用户体验最好但灵活性较低。

    > **[!NOTE]**
    >
    > 建议根据业务需求选择合适的模式，也可同时支持两种模式供用户选择。
