---
title: "场景群机器人消息推送：群助手自动化通知与业务提醒"
source_url: "https://open.dingtalk.com/document/development/group-assistant-sends-a-message"
namespace: "development"
slug: "group-assistant-sends-a-message"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "即时通信 > 会话管理 > 集成方案 > 场景群机器人消息推送：群助手自动化通知与业务提醒"
doc_id: "ItyRrLUMsj"
updated_at: "2026-10-16 09:23:08"
---

> Source: https://open.dingtalk.com/document/development/group-assistant-sends-a-message
> Path: 应用开发 / 服务端 API / 即时通信 > 会话管理 > 集成方案 > 场景群机器人消息推送：群助手自动化通知与业务提醒
> Updated: 2026-10-16 09:23:08

# 场景群机器人消息推送：群助手自动化通知与业务提醒

## **概述**

本方案面向企业需要在钉钉场景群中实现自动化消息推送、业务状态实时通知的场景，通过钉钉场景群提供的群助手API，支持三方业务系统申请场景群机器人、创建群模板并绑定机器人，在业务事件触发时调用发送群助手消息接口向指定场景群推送结构化通知。审批人和群成员无需手动刷新即可实时获取业务动态，提升信息触达效率和团队协作响应速度。

### 方案背景

企业业务系统（如监控告警、订单状态变更、审批超时）需向指定钉钉群推送实时通知，但人工转发效率低且易遗漏。通过场景群机器人消息推送，可将业务事件自动转化为结构化群消息，支持@指定人员、富文本卡片、交互按钮等能力，确保关键信息及时触达。

企业在日常运营中常面临以下痛点：

- **通知依赖人工**： 运维人员需手动将告警信息复制粘贴到群聊，夜间或节假日响应延迟可达数小时，错过最佳处置窗口。
- **消息格式混乱**： 不同人员转发的通知格式不统一，关键信息（如故障等级、影响范围）被淹没在冗长文本中，阅读效率低。
- **无法精准触达**： 群消息全员可见但无针对性，责任人无法第一时间感知与自己相关的告警，非相关人员被无关消息干扰。
- **通知记录难追溯**： 群聊消息滚动后无法检索历史通知，故障复盘时难以还原当时的告警时间线和处理过程。

### **核心价值**

本方案的核心价值体现在以下三个方面：

- **实时触达：** 业务事件触发后毫秒级推送至目标场景群，群成员无需手动查询即可实时获取通知，避免信息滞后导致的决策延误。
- **结构化呈现：** 群助手消息支持标题、摘要、跳转链接等结构化字段，关键信息一目了然，区别于普通文本消息的扁平化展示。
- **统一管理：** 通过群模板集中配置机器人绑定关系和消息推送规则，新增业务线只需复用模板，无需重复申请机器人和配置群会话。

### **适用场景**

本方案适用于需要高频自动化消息推送、业务事件实时通知的企业协作场景，典型包括：

- **业务异常告警：** 电商订单支付失败、物流延迟、库存低于阈值等异常事件需第一时间通知运营团队，传统方式依赖人工监控和转发，响应延迟高达30分钟以上。
- **任务进度催办：** 关键任务即将超时或已被驳回时，自动向负责人及协作者所在群组推送提醒消息，避免任务积压影响业务进度。
- **数据日报推送：** 每日定时向管理层群组推送销售/运营/财务等核心指标摘要，替代人工整理Excel截图发送的低效方式。

## **典型业务场景**

### 场景一：跨境电商多平台订单异常实时告警（跨境电商行业）

#### **痛点分析**

某中型跨境电商企业同时运营Amazon、Shopee、Lazada三个平台店铺，使用自研ERP系统管理订单履约、仓储物流、客服工单，三套系统独立运行。运营主管和各平台店长每天需处理大量异常事件，原有流程存在以下问题：

- **异常响应延迟：** 日均异常事件40+起（支付失败/物流停滞/差评预警），ERP系统仅记录日志无主动通知，运营人员需每2小时手动登录系统查看，平均发现延迟90分钟，错过最佳处理窗口导致客户投诉率上升15%。
- **信息分散难协同：** 同一订单的支付、物流、客服异常分散在三套系统中，运营主管需在三个群分别转发消息才能同步信息，单次异常协调耗时15分钟，跨部门响应效率低下。
- **消息淹没风险：** 工作群内日常沟通频繁，异常通知以纯文本形式发送后被大量聊天记录覆盖，夜班值班人员次日上班时已错过3起紧急客诉处理时机。

#### **价值验证**

- **自动化流程**

  ![跨境电商多平台订单异常实时告警场景图](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8160491971/p1105473.png)
- **关键优势**

  - **秒级触达：** 异常事件从发生到群通知推送延迟从90分钟缩短至3秒，客户投诉率从15%降至2%。
  - **聚合呈现：** 三平台异常统一推送至同一场景群，运营主管无需切换系统即可掌握全局，单次异常协调耗时从15分钟降至2分钟。
  - **置顶可见：** 群助手消息以独立卡片形式展示，不被日常聊天淹没，夜班值班人员次日上班仍可快速定位未处理异常。

### 场景二：保险经纪公司理赔案件进度实时同步（保险经纪行业）

#### **痛点分析**

某大型保险经纪公司拥有50+经纪人团队，使用自研CRM系统管理客户保单、理赔申请、核保进度，系统独立运行且无移动端通知能力。团队主管和各组经纪人每天需跟进大量理赔案件，原有流程存在以下问题：

- **进度更新滞后：** 日均理赔案件60+笔，核保/赔付状态变更仅记录在CRM系统，经纪人需主动登录查询才能获知进展，平均获知延迟4小时，客户反复电话追问增加沟通成本。
- **关键节点遗漏：** 理赔材料补交截止日、核保补充资料要求等关键时间节点无主动提醒，曾发生8起因经纪人未及时通知客户补材料导致理赔延期拒付的案例。
- **团队协作低效：** 一个复杂理赔案件涉及核保部、理赔部、财务部多方协作，进度信息分散在各环节负责人手中，主管需逐一电话确认才能掌握整体进度，每日浪费40分钟无效沟通。

#### **价值验证**

- **自动化流程**

  ![保险经纪公司理赔案件进度实时同步场景图](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8160491971/p1105474.png)
- **关键优势**

  - **实时同步：** 理赔状态变更从系统记录到群通知推送延迟从4小时缩短至5秒，客户电话追问量下降70%。
  - **节点保障：** 关键时间节点提前24小时自动推送提醒，材料补交逾期案例从8起降为零，理赔周期平均缩短3天。
  - **透明协作：** 多方协作案件进度统一推送至项目群，主管无需逐一电话确认即可掌握全局，每日无效沟通时间从40分钟降至零。

## **实施指南**

### **技术架构**

本方案的技术架构包含以下核心组件：

- **身份鉴权层：** 负责应用凭证管理和访问令牌获取，确保所有API调用的身份合法性。
- **机器人管理层：** 在开发者后台场景群页面申请场景群机器人，审核通过后获取`robotCode`参数。
- **模板配置层：** 在开发者后台场景群页面创建群模板，获取`template_id`参数，并将场景群机器人与群模板绑定。
- **群会话创建层：** 依据`template_id`调用创建场景群接口，获取`open_conversation_id`作为消息推送目标。
- **消息推送层：** 调用发送群助手消息接口，向指定场景群推送结构化通知消息。
- **权限管控层：** 申请`qyapi_chat_manage`接口权限，确保应用具备发送群助手消息的能力。

### **前置条件**

- **应用准备：** 完成[应用创建与配置](../01-XOnnmGCTbn-开发指南/0007-create-application.md)的流程。
- **权限要求：** 拥有钉钉企业管理员或子管理员权限，并申请以下接口权限：

  - `qyapi_chat_manage`（场景群管理权限）
- **开发环境：** 已安装Java开发环境（JDK1.6及以上）及Maven构建工具。
- **SDK准备：** 下载钉钉服务端SDK，支持Java/Python/Go等多语言。

### **代码实现**

步骤一：进入应用详情页，获取应用 Client ID 和 Client Secret。

步骤二：申请接口权限，在权限搜索框中输入`qyapi_chat_manage`并申请权限。

步骤三：调用[获取企业内部应用的accessToken](0032-obtain-the-access-token-of-an-internal-app.md)接口，应用访问凭证。调用接口时，通过accessToken鉴权调用者身份。

步骤四：获取关键参数：

1. 在开发者后台-场景群页面，申请[机器人](https://open-dev.dingtalk.com/fe/im#/robot/list)，审核通过后获取机器人id参数**robotCode**。
2. 在开发者后台-场景群页面，创建[群模板](https://open-dev.dingtalk.com/fe/im#/group/list)，获取群模板id参数**template\_id**。
3. 绑定[场景群-机器人](https://open-dev.dingtalk.com/fe/im#/robot/list)到[场景群-群模板](https://open-dev.dingtalk.com/fe/im#/group/list)，保存编辑，返回群场景列表。
4. 进入对应群模板，提交审核，点击发布。

步骤五：核心API调用：

1. 依据`template_id`调用[创建场景群](0744-create-a-scene-group.md)接口，获取`open_conversation_id`。
2. 调用[发送群助手消息](0761-group-template-robot-message.md)接口，实现机器人群消息的发送。

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

   - `qyapi_chat_manage`（场景群管理权限）：用于创建群模板、发送群助手消息。

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

### **步骤四：获取关键参数**

1. 在开发者后台-场景群页面，申请[机器人](https://open-dev.dingtalk.com/fe/im#/robot/list)。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9112993871/p1086792.png)
2. 获取机器人ID参数，即**robotCode**。

   > **[!NOTE]**
   >
   > 申请机器人需要审核，审批通过后可以查看ID，如下图所示。

   ![创建机器人](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9112993871/p355281.png)
3. 在开发者后台-场景群页面，创建[群模板](https://open-dev.dingtalk.com/fe/im#/group/list)，获取群模板id参数**template\_id**。

   ![创建群模板1](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9112993871/p355273.png)
4. 绑定[场景群-机器人](https://open-dev.dingtalk.com/fe/im#/robot/list)到[场景群-群模板](https://open-dev.dingtalk.com/fe/im#/group/list)，保存编辑，返回群场景列表。

   ![保存群模板](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9112993871/p379280.png)
5. 进入对应群模板，进行提交审核，点击发布。

   > **[!NOTE]**
   >
   > 审核自动通过，无需审批。

   ![发布流程](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2473821461/p379282.png)

### **步骤五：核心API调用**

1. 通过`template_id`调用[创建场景群](0744-create-a-scene-group.md)接口，获取`open_conversation_id`。

   ```
   public void createSceneGroup() throws Exception {
           Config config = new Config();
           config.protocol = "https";
           config.regionId = "central";
           com.aliyun.dingtalkim_1_0.Client client = new com.aliyun.dingtalkim_1_0.Client(config);
           CreateSceneGroupHeaders createSceneGroupHeaders = new CreateSceneGroupHeaders();
           createSceneGroupHeaders.xAcsDingtalkAccessToken = "accessToken";
           CreateSceneGroupRequest createSceneGroupRequest = new CreateSceneGroupRequest()
                   .setTitle("客户群")
                   .setIcon("@lADOADma*****QKA")
                   .setTemplateId("c354***-***-***-b4ea-6f1ab***65")
                   .setOwnerUserId("1107****2120");
           try {
               CreateSceneGroupResponse createSceneGroupWithOptions = client.createSceneGroupWithOptions(createSceneGroupRequest, createSceneGroupHeaders, new RuntimeOptions());
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

   - `title`：群名称，最长不超过30字符，建议长度在10字符以内。
   - `template_id`：群模板唯一ID。
   - `owner_userid`：群主userid。
   - `name`：场景群名称。

   **返回字段：**

   - `open_conversation_id`：场景群唯一ID，用于后续消息推送。
2. 调用[发送群助手消息](0761-group-template-robot-message.md)接口，实现机器人群消息的发送。

   ```
   DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/im/chat/scencegroup/message/send_v2");
   OapiImChatScencegroupMessageSendV2Request req = new OapiImChatScencegroupMessageSendV2Request();
   req.setMsgTemplateId("inner_app_template_markdown");
   req.setIsAtAll(false);
   req.setMsgParamMap("{\"title\":\"测试\",\"markdown_content\":\"# 测试内容 \n @180xxxx3120\"}");
   req.setMsgMediaIdParamMap("{\"pic1\":\"@123\",\"pic2\":\"@456\"}");
   req.setTargetOpenConversationId("cid9FTRQSLo+sK*****==");
   req.setAtMobiles("137*****000");
   req.setAtUsers("072*****");
   req.setReceiverUserIds("072*****,manager422*****");
   req.setReceiverUnionIds("jHs*****,atc*****");
   req.setRobotCode("fTv5O*****");
   OapiImChatScencegroupMessageSendV2Response rsp = client.execute(req, access_token);
   System.out.println(rsp.getBody());
   ```

   **请求参数：**

   - `target_open_conversation_id`：群ID。
   - `msg_template_id`：消息模板ID。
   - `robot_code`：机器人编码。

   **返回字段：**

   - `success`：调用是否成功。
   - `open_msg_id`：processQueryKey，可用此key调用其他接口，获取消息的已读状态。

**实施完成检查清单**

- ✅ 应用已完成创建并获取Client ID和Client Secret。
- ✅ 已申请`qyapi_chat_manage`权限。
- ✅ accessToken获取成功且缓存策略已配置。
- ✅ 场景群机器人申请成功并获取`robotCode`。
- ✅ 群模板创建成功并获取`template_id`。
- ✅ 机器人与群模板绑定成功。
- ✅ 群模板发布成功。
- ✅ 场景群创建成功并获取`open_conversation_id`。
- ✅ 群助手消息发送成功并获取`message_id`。
- ✅ 群成员收到结构化通知消息。
- ✅ 消息跳转链接可正常访问。

## **常见问题（FAQ）**

- **Q：qyapi\_chat\_manage权限如何申请？**

  在应用详情页的开发配置-权限管理中搜索`qyapi_chat_manage`并申请。该权限涵盖群模板创建、发送群助手消息等全部场景群操作，无需额外申请子权限。
- **Q：**`robotCode`**和**`template_id`**的获取方式是什么？**

  `robotCode`在开发者后台-场景群页面申请机器人并通过审核后获取；`template_id`在同一页面创建群模板后获取。两者均为场景群功能的核心标识参数，缺一不可。
- **Q：调用群助手消息API失败的常见原因有哪些？**

  常见原因包括：

  - ①`qyapi_chat_manage`权限未申请；
  - ②`open_conversation_id`无效或群已被解散；
  - ③`robotCode`与`template_id`未正确绑定。建议优先检查权限状态和参数有效性。
- **Q：群助手消息是否有发送频率限制？**

  有，发送群助手消息接口QPS：1000 次/秒。超出限制的消息将被丢弃并返回限流错误码。建议对高频事件进行聚合处理（如合并同类异常为一条汇总消息），避免触发限流。
