---
title: "发送、查询、撤回工作通知"
source_url: "https://open.dingtalk.com/document/development/work-notice-option"
namespace: "development"
slug: "work-notice-option"
group: "应用开发"
tab: "服务端API"
breadcrumb: "即时通信 > 消息通知 > 使用教程 > 发送、查询、撤回工作通知"
doc_id: "uykrgz2Wnq"
updated_at: "2026-07-14 09:22:11"
---

> Source: https://open.dingtalk.com/document/development/work-notice-option
> Path: 应用开发 / 服务端API / 即时通信 > 消息通知 > 使用教程 > 发送、查询、撤回工作通知
> Updated: 2026-07-14 09:22:11

# 发送、查询、撤回工作通知

本文介绍了如何调用工作通知消息相关接口实现发送，查询，撤回等行为。

## **预期效果**

工作通知发送效果，如下图所示：

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0430534661/p496415.png)

## **接入流程简介**

本文档展示了，创建一个企业内部应用，使用考勤相关的API，实现发送工作通知消息等相关的流程：

前提条件：完成[应用创建与配置](../01-XOnnmGCTbn-开发指南/0007-create-application.md)的流程。

步骤一：获取应用凭证信息，获取应用 Client ID 和 Client Secret。

步骤二：申请接口权限，申请工作通知相关接口的权限。

步骤三：获取应用访问凭证[获取企业内部应用的access\_token](1444-obtain-orgapp-token.md)。调用接口时，通过accessToken鉴权调用者身份。

步骤四：调用工作通知相关API：

1. 调用服务端API-[发送工作通知](0769-asynchronous-sending-of-enterprise-session-messages.md)接口，发送工作通知，获取工作通知消息唯一任务ID`task_id`。
2. 根据唯一任务ID`task_id`，调用服务端API-[获取工作通知消息的发送进度](0772-obtain-the-sending-progress-of-asynchronous-sending-of-enterprise-session.md)接口，获取发送进度。
3. 根据唯一任务ID`task_id`，调用服务端API-[获取工作通知消息的发送结果](0773-gets-the-result-of-sending-messages-asynchronously-to-the-enterprise.md)接口，查看发送结果。
4. 根据唯一任务ID`task_id`，调用服务端API-[更新工作通知状态栏](0771-update-work-notification-status-bar.md)接口，更新工作通知。
5. 根据唯一任务ID`task_id`，调用服务端API-[撤回工作通知消息](0770-notification-of-work-withdrawal.md)接口，撤回工作通知。

## **前提条件**

完成[应用创建与配置](../01-XOnnmGCTbn-开发指南/0007-create-application.md)的流程。

## **步骤一：获取应用凭证**

1. 选择目标应用，进入应用详情页，单击**基础信息** > **凭证与基础信息**。
2. 获取应用 Client ID 和 Client Secret。

## **步骤二：添加接口权限**

接口权限默认开通，无需申请。

## **步骤三：获取应用访问凭证accessToken**

> **[!IMPORTANT]**
>
> 服务端API差异详情参见[新版API VS 旧版API](0002-download-the-server-side-sdk.md#section-8lr-id4-rbz)。以下接口均使用服务端API接口，SDK下载详情参见[服务端SDK下载](0002-download-the-server-side-sdk.md)。

根据步骤一中的 Client ID 和 Client Secret，获取应用访问凭证[获取企业内部应用的access\_token](1444-obtain-orgapp-token.md)。

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

## **步骤四：调用服务端相关API**

1. 调用服务端API-[发送工作通知](0769-asynchronous-sending-of-enterprise-session-messages.md)接口，发送工作通知，获取工作通知消息唯一任务ID task\_id。

   ```
   public void OAWorkNotice() throws ApiException {
           DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/message/corpconversation/asyncsend_v2");
           OapiMessageCorpconversationAsyncsendV2Request request = new OapiMessageCorpconversationAsyncsendV2Request();
           request.setAgentId(1185599675L);
           request.setUseridList("manager7675");
           request.setToAllUser(false);

           OapiMessageCorpconversationAsyncsendV2Request.Msg msg = new OapiMessageCorpconversationAsyncsendV2Request.Msg();
           OapiMessageCorpconversationAsyncsendV2Request.OA oa = new OapiMessageCorpconversationAsyncsendV2Request.OA();

           OapiMessageCorpconversationAsyncsendV2Request.Head head = new OapiMessageCorpconversationAsyncsendV2Request.Head();
           head.setBgcolor("FFFF6A00");
           head.setText("测试");
           OapiMessageCorpconversationAsyncsendV2Request.Body body = new OapiMessageCorpconversationAsyncsendV2Request.Body();
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

           OapiMessageCorpconversationAsyncsendV2Request.Rich rich = new OapiMessageCorpconversationAsyncsendV2Request.Rich();
           rich.setNum("10.6");
           rich.setUnit("元");

           list.add(form1);
           list.add(form2);
           list.add(form3);
           list.add(form4);
           list.add(form5);
           list.add(form6);

           body.setForm(list);
           body.setRich(rich);
           body.setTitle("正文标题5");
           body.setImage("@lADOADmaWMzazQKA");
           body.setFileCount("3");
           body.setAuthor("小钉");

           OapiMessageCorpconversationAsyncsendV2Request.StatusBar statusBar = new OapiMessageCorpconversationAsyncsendV2Request.StatusBar();
           statusBar.setStatusBg("0xFFFF6A00");
           statusBar.setStatusValue("进行中");

           oa.setMessageUrl("https://dingtalk.com");
           oa.setHead(head);
           oa.setBody(body);
           oa.setStatusBar(statusBar);
           msg.setOa(oa);
           msg.setMsgtype("oa");
           msg.setOa(oa);
           request.setMsg(msg);
           OapiMessageCorpconversationAsyncsendV2Response rsp = client.execute(request, "access_token");
           System.out.println(rsp.getBody());
       }
   ```
2. 根据唯一任务ID task\_id，调用服务端API-[获取工作通知消息的发送进度](0772-obtain-the-sending-progress-of-asynchronous-sending-of-enterprise-session.md)接口，获取发送进度。

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
3. 根据唯一任务ID task\_id，调用服务端API-[获取工作通知消息的发送结果](0773-gets-the-result-of-sending-messages-asynchronously-to-the-enterprise.md)接口，查看发送结果。

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
4. 根据唯一任务ID task\_id，调用服务端API-[更新工作通知状态栏](0771-update-work-notification-status-bar.md)接口，更新工作通知。

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
