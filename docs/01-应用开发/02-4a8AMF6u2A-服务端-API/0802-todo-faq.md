---
title: "常见问题"
source_url: "https://open.dingtalk.com/document/development/todo-faq"
namespace: "development"
slug: "todo-faq"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "待办任务 > 常见问题"
doc_id: "RgsiZC07KH"
updated_at: "2025-09-10 19:34:58"
---

> Source: https://open.dingtalk.com/document/development/todo-faq
> Path: 应用开发 / 服务端 API / 待办任务 > 常见问题
> Updated: 2025-09-10 19:34:58

# 常见问题

本文介绍钉钉待办任务的常见问题和错误。

## 创建待办接口调用成功，为什么在钉钉客户端上没有出现红点？

答：待办创建完成后，会显示在所有参与者的待办列表中。如果此待办任务指定了截止时间，且截止时间为当天或者待办状态为已逾期时，则会在待办任务的创建者和执行者的待办首页展示小红点。

钉钉待办红点规则：

**待办入口显示的红数字 = 已逾期待办数量 + 当前待办数量**

## 创建待办接口调用成功，为什么在我的待办列表中未实时显示？

答：调用[创建钉钉待办任务](0793-add-dingtalk-to-do-task.md)出现该问题的原因可能如下:

传入的isOnlyShowExecutor参数设置为true。在isOnlyShowExecutor为true时表示该待办只会出现在执行人的待我处理列表中。若执行人executorIds参数未传的情况，则看不到待办。

## 通过接口创建的待办，是否可以在待办列表操作完成？

答：待办业务接入目前主要有两类场景：

### 待办通知场景

待办通知场景完全复用钉钉官方待办能力（与用户在钉钉客户端创建的待办完全一致），调用新增待办接口创建待办时不需要传三方详情页链接，用户在钉钉客户端操作时可以在待办列表直接完成，点击跳转详情时将跳转至钉钉官方待办详情页。

流程如下图所示：

![待办通知](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8630104361/p337455.png)

### 第三方业务自闭环场景

第三方业务自闭环场景是创建待办时，需传入业务自身应用详情页链接，用户在钉钉客户端操作时无法在列表直接完成，仅支持直接跳转至三方应用详情页进行操作。

流程如下图所示：

![第三方业务闭环](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8630104361/p337456.png)

## 开放接口path中的unionId、creatorId、executorId、participantId、operatorId有什么区别？

答：区别如下：

- **unionId**：设计用于区分个人、企业场景资源归属地，目前开放接口仅支持企业场景，这个可以理解为创建者，直接传创建者ID即可。
- **creatorId**：创建该待办的用户。
- **executorId**：要执行待办任务的人。
- **participantId**：待办任务的参与人，仅关注查看任务信息，无操作权限。
- **operatorId**：本次请求的操作用户。

## 创建钉钉待办任务，提示“EXTRA string=call hsf service result error: task existed, string= and taskId is xxx”

答：**sourceId**（业务系统侧的唯一标识ID，即来源业务ID）重复导致，请保持唯一。

> **[!NOTE]**
>
> 当三方业务接入钉钉待办后，需传递三方应用业务系统侧的唯一标识任务ID。当待办创建成功后，需要更换新的sourceId，保持一个待办任务对应一个sourceId。

## 为什么我下载的是最新的SDK, 但是没有待办任务2.0的API呢?

答：建议参考新版服务端API SDK地址：[服务端SDK下载](0002-download-the-server-side-sdk.md)。

## 待办每个接口的调用频率限制，有对应的文档吗？

答：企业内部应用和第三方企业应用均可以参考[调用频率限制](0012-call-frequency-limit.md)文档。

## 新增待办任务时，用户收不到DING提醒

答：调用[创建钉钉待办任务](0793-add-dingtalk-to-do-task.md)出现上述问题的可能原因包括但不限于以下情况：

- 入参中的notifyConfigs(DING通知配置)未正确传入。
- 未传入executorIds(执行者的unionId)。
- 如果creatorId(创建者的unionid)和executorIds(执行者的unionid)相同时，则收不到DING通知。

## 查询企业下用户待办列表获取不到待办或待办有缺失

答：调用[查询企业下用户待办列表](0798-query-the-to-do-list-of-enterprise-users.md)出现上述问题的可能原因包括但不限于以下情况：

- 该接口最多可获取180天内已完成状态的待办任务（未完成状态的待办任务无此限制）。
- 需为通过[创建钉钉待办任务](0793-add-dingtalk-to-do-task.md)发起且detailUrl参数不为空的待办任务才能通过该接口查出，在客户端手动创建的个人待办无法查出。
