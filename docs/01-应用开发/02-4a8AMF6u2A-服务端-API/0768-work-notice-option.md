---
title: "工作通知消息管理：发送、查询与撤回开发实践"
source_url: "https://open.dingtalk.com/document/development/work-notice-option"
namespace: "development"
slug: "work-notice-option"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "即时通信 > 消息通知 > 集成方案 > 工作通知消息管理：发送、查询与撤回开发实践"
doc_id: "uykrgz2Wnq"
updated_at: "2026-10-16 09:23:11"
---

> Source: https://open.dingtalk.com/document/development/work-notice-option
> Path: 应用开发 / 服务端 API / 即时通信 > 消息通知 > 集成方案 > 工作通知消息管理：发送、查询与撤回开发实践
> Updated: 2026-10-16 09:23:11

# 工作通知消息管理：发送、查询与撤回开发实践

## **概述**

本方案基于钉钉即时通信IM工作通知API，介绍如何通过服务端接口实现工作通知消息的发送、进度查询、结果查询、状态栏更新及撤回全流程。企业通过创建内部应用并调用工作通知相关API，可将业务系统中的审批结果、任务提醒、系统告警等消息精准推送至员工钉钉端，并实时追踪消息送达状态，支持对已发送消息进行状态更新或撤回操作，适用于人力资源、餐饮连锁、政务服务等多种企业场景。

### 方案背景

企业需向员工推送各类工作通知（如会议提醒、政策发布、任务分配），但传统邮件或短信触达率低、无法追踪阅读状态。通过钉钉工作通知API，可实现消息的程序化发送、阅读状态查询和误发撤回，确保重要通知精准送达并可追溯。

企业在日常运营中常面临以下痛点：

- **通知触达不可靠**： 邮件打开率不足30%，短信被拦截率高，重要通知发出后无法确认员工是否收到，反复电话确认耗费大量时间。
- **阅读状态黑盒**： 无法得知哪些员工已读、哪些未读，催办只能盲目群发提醒，已读员工被重复打扰产生反感情绪。
- **误发无法补救**： 通知内容有误或发送对象错误时无法撤回，错误信息持续传播造成误解，事后澄清成本远高于预防成本。
- **通知数据难分析**： 各类通知的送达率、阅读率、点击率等指标无法量化，运营团队无法评估通知效果和优化策略。

### **核心价值**

- **工作通知精准触达：** 通过服务端API向指定员工或全员发送工作通知，支持OA、文本、链接、Markdown等多种消息类型，消息直达钉钉工作台通知中心，到达率接近100%。
- **发送状态实时追踪：** 通过task\_id实时查询消息发送进度和送达结果，精确掌握每位接收人的阅读状态，为消息触达效果提供数据支撑。
- **消息生命周期管控：** 支持更新已发送工作通知的状态栏展示（如审批状态变更），以及撤回误发或过期消息，确保员工接收到的信息始终准确有效。
- **跨系统集成无缝衔接：** 工作通知API与企业内部系统深度对接，实现从业务事件触发到消息推送、状态同步、消息撤回的端到端闭环，消除信息传递断层。

### **适用场景**

- **人力资源服务入职流程通知：** HR系统在候选人offer审批通过后自动发送入职须知工作通知，实时追踪新员工阅读状态，未读人员自动触发二次提醒，确保入职材料准备零遗漏。
- **餐饮连锁门店运营指令下发：** 总部运营系统向各门店店长批量发送促销活动执行通知，通过状态栏实时更新活动进度（待执行/执行中/已完成），过期活动通知一键撤回避免误导。
- **政务服务机构办事进度告知：** 政务审批系统在受理、审核、办结等关键节点自动向申请人发送进度通知，审批状态变更时同步更新通知状态栏，让群众实时掌握办事进展。
- **汽车后市场维保提醒推送：** 4S店售后系统根据车辆保养周期自动向车主发送维保提醒工作通知，预约成功后更新通知状态为"已预约"，过期提醒自动撤回保持消息列表整洁。

## **典型业务场景**

### **场景一：人力资源服务企业入职流程通知自动化（人力资源行业）**

#### **痛点分析**

某大型人力资源服务公司年服务3000+新入职员工，HR系统需在offer审批、入职材料提交、培训安排等多个节点向新员工发送通知。原有流程存在以下问题：

- **通知触达率低：** 依赖邮件发送入职须知，平均打开率仅42%，大量新员工未及时查阅导致入职当天材料不全，首日办理效率降低60%。
- **状态无法追踪：** 邮件发送后无法确认员工是否阅读，HR需逐一电话确认，3000人/年的确认工作量耗费2名专职人力。
- **信息更新滞后：** 入职时间或地点变更后需重新发送邮件，旧邮件仍留在员工邮箱中造成混淆，曾发生12起因信息不一致导致的入职延误事件。

#### **价值验证**

- **自动化流程**

  ![人力资源入职流程通知自动化场景图](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1260491971/p1105598.png)
- **关键优势**

  - **入职通知零遗漏：** 入职须知通过钉钉工作通知直达员工手机端，到达率从42%提升至99%，入职材料齐全率从78%提升至98%。
  - **阅读状态可追踪：** HR实时查看每位员工的阅读状态，未读人员自动触发二次提醒，电话确认工作量降为零。
  - **信息变更即时同步：** 入职信息变更时直接更新原通知状态栏内容，误发通知秒级撤回，信息混淆事件归零。

### **场景二：餐饮连锁门店运营指令高效下发（餐饮连锁行业）**

#### **痛点分析**

某全国连锁餐饮品牌拥有500+门店，总部运营部每周向各门店下发促销活动执行指令、菜品更新通知、食品安全规范等运营文件。原有流程存在以下问题：

- **指令传达不及时：** 通过微信群或邮件下发运营指令，部分店长未及时查看导致活动上线延迟，月度平均延误3.2天，直接影响促销效果。
- **执行进度不可视：** 总部无法确认各门店是否已接收并执行指令，需逐店电话核实，500家门店的核实周期长达2天，管理盲区大。
- **过期通知干扰：** 已结束的活动通知仍显示在消息列表中，店员误按旧通知执行导致价格错误，季度内发生8起客诉事件。

#### **价值验证**

- **自动化流程**

  ![餐饮连锁门店运营指令下发场景图](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1260491971/p1105601.png)
- **关键优势**

  - **运营指令秒级下达：** 促销指令通过钉钉工作通知直达店长手机端，活动上线延迟从3.2天缩短至当天，执行及时率提升至98%。
  - **500店执行可视化：** 总部实时掌握所有门店的阅读和执行状态，未读门店自动标记提醒，核实周期从2天缩短至实时。
  - **过期通知自动清理：** 活动状态变更时实时更新通知状态栏，结束后一键撤回过期通知，误执行客诉事件降为零。

## **实施指南**

### **技术架构**

本方案的技术架构包含以下核心组件：

- **身份鉴权层：** 负责应用凭证管理和访问令牌获取，确保所有服务端调用的身份合法性。
- **消息发送层：** 根据业务事件构建工作通知消息体，调用发送接口将消息推送至目标用户，获取消息任务唯一标识。
- **状态查询层：** 基于消息任务标识查询发送进度和送达结果，为消息触达效果提供实时数据反馈。
- **消息维护层：** 实现已发送消息的状态栏内容更新和消息撤回操作，保障消息内容的准确性和时效性。

### **前置条件**

- **应用准备：**完成[应用创建与配置](../01-XOnnmGCTbn-开发指南/0007-create-application.md)的流程。
- **权限要求：**接口权限默认开通，无需申请。
- **开发环境：**已安装Java开发环境（JDK 8及以上版本）。
- **SDK准备：**下载钉钉旧版服务端SDK，SDK下载详情参见[服务端SDK下载](0002-download-the-server-side-sdk.md)。

### **代码实现**

步骤一：获取应用凭证信息，获取应用 Client ID 和 Client Secret。

步骤二：申请接口权限，申请工作通知相关接口的权限。

步骤三：获取应用访问凭证[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)。调用接口时，通过accessToken鉴权调用者身份。

步骤四：调用工作通知相关API：

1. 调用服务端API-[发送工作通知](0769-asynchronous-sending-of-enterprise-session-messages.md)接口，发送工作通知，获取工作通知消息唯一任务ID`task_id`。
2. 根据唯一任务ID`task_id`，调用服务端API-[获取工作通知消息的发送进度](0772-obtain-the-sending-progress-of-asynchronous-sending-of-enterprise-session.md)接口，获取发送进度。
3. 根据唯一任务ID`task_id`，调用服务端API-[获取工作通知消息的发送结果](0773-gets-the-result-of-sending-messages-asynchronously-to-the-enterprise.md)接口，查看发送结果。
4. 根据唯一任务ID`task_id`，调用服务端API-[更新工作通知状态栏](0771-update-work-notification-status-bar.md)接口，更新工作通知。
5. 根据唯一任务ID`task_id`，调用服务端API-[撤回工作通知消息](0770-notification-of-work-withdrawal.md)接口，撤回工作通知。

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

接口权限默认开通，无需申请。

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

1. 调用服务端API-[发送工作通知](0769-asynchronous-sending-of-enterprise-session-messages.md)接口，发送工作通知，获取工作通知消息唯一任务ID task\_id。

   ```
   public void OAWorkNotice() throws ApiException {
       DingTalkClient client = new DefaultDingTalkClient(
               "https://oapi.dingtalk.com/topapi/message/corpconversation/asyncsend_v2"
       );

       OapiMessageCorpconversationAsyncsendV2Request request = new OapiMessageCorpconversationAsyncsendV2Request();
       request.setAgentId(1185599675L);
       request.setUseridList("manager7675");
       request.setToAllUser(false);

       // 构建 OA 消息头
       OapiMessageCorpconversationAsyncsendV2Request.Head head = new OapiMessageCorpconversationAsyncsendV2Request.Head();
       head.setBgcolor("FFFF6A00");
       head.setText("测试");

       // 构建表单字段
       List<OapiMessageCorpconversationAsyncsendV2Request.Form> list = new ArrayList<>();

       OapiMessageCorpconversationAsyncsendV2Request.Form form1 = new OapiMessageCorpconversationAsyncsendV2Request.Form();
       form1.setKey("姓名:");
       form1.setValue("小钉");

       OapiMessageCorpconversationAsyncsendV2Request.Form form2 = new OapiMessageCorpconversationAsyncsendV2Request.Form();
       form2.setKey("年龄:");
       form2.setValue("21");

       OapiMessageCorpconversationAsyncsendV2Request.Form form3 = new OapiMessageCorpconversationAsyncsendV2Request.Form();
       form3.setKey("身高:");
       form3.setValue("1.8米");

       OapiMessageCorpconversationAsyncsendV2Request.Form form4 = new OapiMessageCorpconversationAsyncsendV2Request.Form();
       form4.setKey("体重:");
       form4.setValue("130斤");

       OapiMessageCorpconversationAsyncsendV2Request.Form form5 = new OapiMessageCorpconversationAsyncsendV2Request.Form();
       form5.setKey("学历:");
       form5.setValue("本科");

       OapiMessageCorpconversationAsyncsendV2Request.Form form6 = new OapiMessageCorpconversationAsyncsendV2Request.Form();
       form6.setKey("爱好:");
       form6.setValue("打球、听音乐");

       list.add(form1);
       list.add(form2);
       list.add(form3);
       list.add(form4);
       list.add(form5);
       list.add(form6);

       // 构建富文本金额
       OapiMessageCorpconversationAsyncsendV2Request.Rich rich = new OapiMessageCorpconversationAsyncsendV2Request.Rich();
       rich.setNum("10.6");
       rich.setUnit("元");

       // 构建 OA 消息体
       OapiMessageCorpconversationAsyncsendV2Request.Body body = new OapiMessageCorpconversationAsyncsendV2Request.Body();
       body.setForm(list);
       body.setRich(rich);
       body.setTitle("正文标题5");
       body.setImage("@lADOADmaWMzazQKA");
       body.setFileCount("3");
       body.setAuthor("小钉");

       // 构建状态栏
       OapiMessageCorpconversationAsyncsendV2Request.StatusBar statusBar = new OapiMessageCorpconversationAsyncsendV2Request.StatusBar();
       statusBar.setStatusBg("0xFFFF6A00");
       statusBar.setStatusValue("进行中");

       // 组装 OA 消息
       OapiMessageCorpconversationAsyncsendV2Request.OA oa = new OapiMessageCorpconversationAsyncsendV2Request.OA();
       oa.setMessageUrl("https://dingtalk.com");
       oa.setHead(head);
       oa.setBody(body);
       oa.setStatusBar(statusBar);

       // 设置消息类型与内容
       OapiMessageCorpconversationAsyncsendV2Request.Msg msg = new OapiMessageCorpconversationAsyncsendV2Request.Msg();
       msg.setMsgtype("oa");
       msg.setOa(oa);

       request.setMsg(msg);

       // 发送请求
       OapiMessageCorpconversationAsyncsendV2Response rsp = client.execute(request, "access_token");
       System.out.println(rsp.getBody());
   }
   ```

   **请求参数：**

   - `agent_id`：应用agentId，可在应用详情页获取。
   - `userid_list`：接收消息的用户userId列表，多个用逗号分隔。
   - `to_all_user`：是否发送给全部用户，true时忽略userid\_list。
   - `msg`：消息体对象，支持OA、文本、图片、语音、文件、链接、Markdown、action\_card卡片等类型。

   **返回字段：**

   - `task_id`：创建的异步发送任务ID，用于后续查询进度、结果、更新和撤回操作。
2. 根据唯一任务`task_id`，调用服务端API-[获取工作通知消息的发送进度](0772-obtain-the-sending-progress-of-asynchronous-sending-of-enterprise-session.md)接口，获取发送进度。

   ```
   public void workNoticeSendProgress() throws ApiException {
       DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/message/corpconversation/getsendprogress");

       OapiMessageCorpconversationGetsendprogressRequest req = new OapiMessageCorpconversationGetsendprogressRequest();
       req.setAgentId(123L);
       req.setTaskId(456L);

       OapiMessageCorpconversationGetsendprogressResponse rsp = client.execute(req, "access_token");
       System.out.println(rsp.getBody());
   }
   ```

   **请求参数：**

   - `agent_id`：应用agentId。
   - `task_id`：发送工作通知时返回的任务ID。

   **返回字段：**

   - `progress`：发送进度对象，包含理的百分比和任务执行状态。
3. 根据唯一任务`task_id`，调用服务端API-[获取工作通知消息的发送结果](0773-gets-the-result-of-sending-messages-asynchronously-to-the-enterprise.md)接口，查看发送结果。

   ```
   public void workNoticeSendResult() throws ApiException {
       DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/message/corpconversation/getsendresult");

       OapiMessageCorpconversationGetsendresultRequest req = new OapiMessageCorpconversationGetsendresultRequest();
       req.setAgentId(123L);
       req.setTaskId(456L);

       OapiMessageCorpconversationGetsendresultResponse rsp = client.execute(req, "access_token");
       System.out.println(rsp.getBody());
   }
   ```

   **请求参数：**

   - `agent_id`：应用agentId。
   - `task_id`：发送工作通知时返回的任务ID。

   **返回字段：**

   - `send_result`：发送结果对象，包含已读用户列表、未读用户列表和无效用户列表。
4. 根据唯一任务 `task_id`，调用服务端API-[更新工作通知状态栏](0771-update-work-notification-status-bar.md)接口，更新工作通知。

   ```
   /**
    * 审批状态颜色参考
    * 已同意 0xFF78C06E
    * 已拒绝 0xFFF65E5E
    * 已撤销 0xFF858E99
    * 待审批 0xFFFF9D46
    */
    public void updateWorkNoticeStatus() throws ApiException {
         DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/message/corpconversation/status_bar/update");
         OapiMessageCorpconversationStatusBarUpdateRequest request = new OapiMessageCorpconversationStatusBarUpdateRequest();
         request.setAgentId(1068622214L);
         request.setStatusValue("已同意");
         request.setStatusBg("0xFF78C06E");
         request.setTaskId(313382528774L);
         OapiMessageCorpconversationStatusBarUpdateResponse response = client.execute(request, "access_token");
         System.out.println(JSON.toJSONString(response));
   }
   ```

   **请求参数：**

   - `agent_id`：应用agentId。
   - `task_id`：发送工作通知时返回的任务ID。
   - `status_value`：状态栏值。
   - `status_bg`：状态栏背景颜色值。

   **返回字段：**

   - `errcode`：错误码，0表示成功。
5. 根据唯一任务ID task\_id，调用服务端API-[撤回工作通知消息](0770-notification-of-work-withdrawal.md)接口，撤回工作通知。

   ```
    public void recallWorkNotice() throws ApiException {
        DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/message/corpconversation/recall");
        OapiMessageCorpconversationRecallRequest req = new OapiMessageCorpconversationRecallRequest();
        req.setAgentId(1000L);
        req.setMsgTaskId(2000L);
        OapiMessageCorpconversationRecallResponse rsp = client.execute(req, "access_token");
        System.out.println(rsp.getBody());
       }
   ```

   **请求参数：**

   - `agent_id`：应用agentId。
   - `msg_task_id`：发送工作通知时返回的任务ID。

   **返回字段：**

   - `errcode`：错误码，0表示成功。

**实施完成检查清单**

- ✅ 已完成应用创建并获取Client ID和Client Secret。
- ✅ 已确认工作通知相关接口权限已开通。
- ✅ 已成功获取accessToken并能正常调用接口。
- ✅ 已成功发送工作通知并获取task\_id。
- ✅ 已通过task\_id查询发送进度和发送结果。
- ✅ 已成功更新工作通知状态栏内容。
- ✅ 已成功撤回测试工作通知消息。
- ✅ 已在生产环境中完成端到端联调验证。

## **常见问题（FAQ）**

- **Q1：工作通知消息有发送频率限制吗？**

  有。

  - 企业内部应用发送消息单次最多只能给5000人发送，第三方企业应用发送消息单次最多能给1000人发送。
  - 给同一员工一天只能发送一条内容相同的消息通知。
  - 企业内部应用每天给每个员工最多可发送500条消息通知，第三方企业应用最多可发送100条。
  - 企业内部应用或第三方企业应用发送消息时，每分钟最多有5000人可以接收到消息。
- **Q2：撤回工作通知有什么限制条件？**

  撤回操作仅限发送后24小时内的消息，且只能撤回本企业应用发送的工作通知。超过24小时的消息无法撤回，建议通过更新状态栏接口修改展示内容作为替代方案。
- **Q3：发送结果中的无效用户是什么意思？**

  无效用户指userId不存在、已离职或被禁用的账号。发送结果接口会分别返回已读用户、未读用户和无效用户列表，业务系统应记录无效用户并清理通讯录数据。
- **Q4：状态栏更新支持哪些颜色配置？**

  状态栏背景色支持自定义十六进制颜色值。常用审批状态颜色参考：已同意0xFF78C06E、已拒绝0xFFF65E5E、已撤销0xFF858E99、待审批0xFFFF9D46。
- **Q5：工作通知支持哪些消息类型？**

  支持OA消息、文本消息、链接消息、Markdown消息、ActionCard消息等多种类型。不同消息类型适用于不同业务场景，OA消息适合结构化信息展示，Markdown消息适合富文本内容。
