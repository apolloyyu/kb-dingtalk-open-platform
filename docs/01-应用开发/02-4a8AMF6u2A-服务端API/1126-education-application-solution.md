---
title: "钉钉教育接入流程"
source_url: "https://open.dingtalk.com/document/development/education-application-solution"
namespace: "development"
slug: "education-application-solution"
group: "应用开发"
tab: "服务端API"
breadcrumb: "行业与生态 > 行业开放 > 新教育 > 使用教程 > 钉钉教育接入流程"
doc_id: "jcPeRP46Rc"
updated_at: "2026-07-20 09:21:43"
---

> Source: https://open.dingtalk.com/document/development/education-application-solution
> Path: 应用开发 / 服务端API / 行业与生态 > 行业开放 > 新教育 > 使用教程 > 钉钉教育接入流程
> Updated: 2026-07-20 09:21:43

# 钉钉教育接入流程

## **应用服务商接入流程**

### **使用场景**

开发者以钉钉、教育组织（教育局/学校/教培机构）之外的第三方身份，基于钉钉的开放能力开发应用，并提供教育组织使用。

### **接入要求**

开发教育应用前，确保应用服务商满足以下要求：

1. 已完成应用服务商入驻，详情请参考[合作全流程指引](../07-TjCzIgfQs3-平台服务/0027-isv-cooperation-guide.md)。
2. 应用需要符合目前钉钉教育类目运营需求，招商规划。
3. 服务商入驻需要是教育行业垂直分类领域排名TOP5，需要在教育行业内有一定的市场份额和行业知名度。
4. 应用需要有明确的目标服务人群，分类清晰。
5. 应用审批中需要提供非常清晰的产品介绍，要有明确的运营规划，商业规划及目标。
6. 应用需要投入专门的人力物力投入到钉钉的合作运营。

### **应用上架流程**

第三方企业应用上架流程如下图所示。

![教育isv](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4830613061/p174708.png)

### **开发流程**

1. 创建并配置应用。

   在开始开发前，需要先创建并配置钉钉应用。钉钉支持创建小程序和H5微应用，推荐使用小程序。详情请参考[应用创建与配置](../01-XOnnmGCTbn-开发指南/0007-create-application.md)。
2. 实现应用免登。

   1. 推送suiteTicket，推送方式请参考[配置事件推送方式](../04-LFcRvVD08N-事件订阅/0003-configure-stream-push.md)文档说明。
   2. 获取corpid。corpid是企业的唯一标识。

      - 小程序使用dd.corpId获取企业corpId。
      - H5微应用的首页URL，可以使用$CORPID$做为参数占位符，钉钉容器会将$CORPID$替换为当前访问的企业的CorpId。示例：https://xxxx?corpId=$CORPID$
   3. 获取免登授权码。

      - 小程序获取授权码示例如下，详情请参考[免登授权码](../03-Ogu5SlPY4t-客户端JSAPI/0005-jsapi-get-auth-code.md)。

        ```
        dd.getAuthCode({
          corpId: 'ding12345xxx',
          success: (res) => {
            const { authCode } = res;
          },
          fail: () => {},
          complete: () => {},
        });
        ```
      - H5微应用获取授权码示例如下，详情请参考[免登流程](../03-Ogu5SlPY4t-客户端JSAPI/0006-jsapi-request-auth-code.md)。

        ```
        dd.ready(function() {
          dd.requestAuthCode({
            corpId: 'corpid',
            clientId: 'clientid',
            onSuccess: function (result) {
              /*{
                code: 'hYLK98jkf0m' //string authCode
            }*/
            },
            onFail: function (err) {},
          });
        });
        ```
   4. 获取企业凭证，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取企业的凭证access\_token。
   5. 获取用户信息，调用[通过免登码获取用户信息](0024-obtain-the-userid-of-a-user-by-using-the-log-free.md)接口获取用户信息。
3. 集成教育相关接口。

   我们提供了集成教育相关接口的的demo，查看[demo地址](https://github.com/open-dingtalk/dingtalk-edu-openapi-demo)。

   教育相关接口，见下方常用接口说明。

### **常用接口说明**

- **JSAPI鉴权**

  钉钉提供的JSAPI有很多是手机的基础能力，对这些JSAPI的调用不需要进行鉴权（**即不需要进行dd.config**），只需要在dd.ready里调用即可。对于一些钉钉业务相关、安全相关的JSAPI的调用，需要先进行鉴权然后再调用。

  详见[JSAPI鉴权](../03-Ogu5SlPY4t-客户端JSAPI/0003-jsapi-authentication.md)。
- **数据变更推送**

  - RDS推送：

    在保障数据安全的前提下，极大的简化了推送协议，减少了数据传输次数，提高了数据传输速度，提升了推送的稳定性。详情请参考[配置RDS推送表](../04-LFcRvVD08N-事件订阅/0346-configure-rds-push-table.md)。
  - SyncHTTP回调推送：

    SyncHTTP回调推送是使用回调地址推送数据的方式，开发者提供HTTP回调服务，钉钉服务器会向此回调地址推送数据，数据需要经过加解密的处理。详情请参考[配置 SyncHTTP 推送（不推荐）](../04-LFcRvVD08N-事件订阅/0003-configure-stream-push.md#421584309ds03)。
- **消息通知**

  钉钉提供以下消息通知方式：

  - **工作通知消息**：是以企业工作通知会话中某个微应用的名义推送到员工的通知消息，例如生日祝福、入职提醒等。
  - **群消息**：是指可以调用接口以系统名义向群里推送群聊消息。
  - **普通消息**：是指员工个人在使用应用时，可以通过界面操作的方式往群或其他人的会话里推送消息，例如发送日志的场景。
  - **任务类通知**：是指需要发送一条任务提醒给员工，比如审批任务等，这类情况下可参考[创建钉钉待办任务](0793-add-dingtalk-to-do-task.md)。

    消息类型和样例可参考[消息通知类型](0775-message-types-and-data-format.md)文档。
- 新教育相关接口：

  - **通用基础：**

    钉钉定义的教育行业标准主数据（如学段、学科），提供了一个行业标准，供合作伙伴参考。

    合作伙伴基于钉钉定义的元数据，自己做个性化定义，沉淀的数据实例。
  - **教学：**

    钉钉提供排课、授课及教学数据等教学相关接口，供合作伙伴集成。

    接入时序图如下：

    ![教学时序图](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4830613061/p174709.png)
  - **家校通讯录接口：**

    家校通讯录接口，支持通讯录类型为“基础教育通讯录”和“自定义家校通讯录”。

    文档详见：[家校通讯录2.0](1125-ai-overview-of-education.md#2e213c808bjzu)

## **内部应用SI接入流程**

### **使用场景**

钉钉上的教育相关组织除了使用钉钉提供的通用基础功能外，为满足教育场景中的个性化需求，可以基于钉钉的开放能力，自主开发应用，供组织内部使用。

但教育组织（教育局/学校/教培机构等）内部没有开发团队，因此需要寻找定制服务商在钉钉上为其做开发，实现个性化的需求。

主要场景：

- 教务、教学、教研等关联系统接入钉钉。
- 重新开发一款应用，供其内部使用，实现移动化办公。

### **接入流程**

定制服务商为学校、教育局交付定制应用的接入流程如下图所示。

![si流程](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0908913061/p175173.png)

### **开发流程**

1. 准备工作：

   1. 定制服务商在钉钉开放平台申请定制服务商认证并通过审核；未认证的定制服务商无法被企业授权进行开发。
   2. 定制服务商与企业已沟通，确定了企业的需求与即将开发的应用，供企业内部使用。
   3. 定制服务商需要将自己的corpid提供给企业，作为授权的唯一凭证。
2. 企业创建并配置应用。

   在开始开发前，需要先创建并配置钉钉应用。钉钉支持创建小程序和H5微应用，推荐使用小程序。详情请参考[应用创建与配置](../01-XOnnmGCTbn-开发指南/0007-create-application.md)。
3. 企业授权定制服务商，完整配置请参考[产品方案商定制服务合作流程](../07-TjCzIgfQs3-平台服务/0017-cooperation-process-of-customized-services-from-product-solution-providers.md)。

   1. 选择要授权开发的定制服务商。

      ![授权定制服务商](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0908913061/p175174.png)
   2. 添加接口权限。

      为了保证企业的数据安全与应用稳定，请根据应用的功能，对服务商可在应用内使用的权限进行合理分配。

      其中通讯录权限，需要选择授权的范围，表示服务商可获取哪些人员的通讯录信息。建议开发期间，根据需要，合理授权。![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8432889661/p525204.png)
4. 定制服务商获取授权信息。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8432889661/p525208.png)
5. 定制服务商集钉钉API。

   - **JSAPI鉴权**

     钉钉提供的JSAPI有很多是手机的基础能力，对这些JSAPI的调用不需要进行鉴权（**即不需要进行dd.config**），只需要在dd.ready里调用即可。对于一些钉钉业务相关、安全相关的JSAPI的调用，需要先进行鉴权然后再调用。

     详见[JSAPI鉴权](../03-Ogu5SlPY4t-客户端JSAPI/0003-jsapi-authentication.md)。
   - **消息通知**

     钉钉提供以下消息通知方式：

     - **工作通知消息**：是以企业工作通知会话中某个微应用的名义推送到员工的通知消息，例如生日祝福、入职提醒等。
     - **群消息**：是指可以调用接口以系统名义向群里推送群聊消息。
     - **普通消息**：是指员工个人在使用应用时，可以通过界面操作的方式往群或其他人的会话里推送消息，例如发送日志的场景。
     - **任务类通知**：是指需要发送一条任务提醒给员工，比如审批任务等，这类情况请参考[创建钉钉待办任务](0793-add-dingtalk-to-do-task.md)。

       消息类型和样例可参考[消息通知类型](0775-message-types-and-data-format.md)文档。
   - **新教育API**

     - **通用基础**

       钉钉定义的教育行业标准主数据（如学段、学科），提供了一个行业标准，供合作伙伴参考。

       合作伙伴基于钉钉定义的元数据，自己做个性化定义，沉淀的数据实例。
     - **在线课堂：**

       钉钉提供排课、授课及教学数据等教学相关接口，供合作伙伴集成。

       接入时序图如下：

       ![教育时序图](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0908913061/p175176.png)
     - **家校通讯录接口：**

       家校通讯录接口，支持通讯录类型为“基础教育通讯录”和“自定义家校通讯录”。

       文档详见:

       我们提供了集成教育相关接口的的demo，查看[demo地址](https://github.com/open-dingtalk/dingtalk-edu-openapi-demo)。

## **问题排查**

在接入钉钉时，如果您可以通过以下方式进行问题排查：

查看是否触发了接口调用频率限制，详情请参考[调用频率限制](0012-call-frequency-limit.md)。
