---
title: "关于新增专业版和专属版钉钉专享OpenAPI的说明"
source_url: "https://open.dingtalk.com/document/development/description-of-the-new-professional-and-exclusive-editions-of-nail-exclusive-openapi"
namespace: "development"
slug: "description-of-the-new-professional-and-exclusive-editions-of-nail-exclusive-openapi"
group: "应用开发"
tab: "服务端API"
breadcrumb: "平台公告与计费 > 平台公告 > 关于新增专业版和专属版钉钉专享OpenAPI的说明"
doc_id: "0Zf81laZek"
updated_at: "2026-07-22 16:25:04"
---

> Source: https://open.dingtalk.com/document/development/description-of-the-new-professional-and-exclusive-editions-of-nail-exclusive-openapi
> Path: 应用开发 / 服务端API / 平台公告与计费 > 平台公告 > 关于新增专业版和专属版钉钉专享OpenAPI的说明
> Updated: 2026-07-22 16:25:04

# 关于新增专业版和专属版钉钉专享OpenAPI的说明

为满足广大开发者在个性化应用开发方面的需求，钉钉新增了一批面向[专业版](dingtalk://dingtalkclient/page/link?url=https%3A%2F%2Fn.dingtalk.com%2Fdingding%2Fdd-pro-composite-order%2Fpc%2Findex.html%3Fpopup_wnd%3Dtrue%26dd_tab%3Dtrue%26width%3D900%26height%3D600%26title%3D%25E9%2592%2589%25E9%2592%2589%25E6%2595%25B0%25E5%25AD%2597%25E8%25B5%2584%25E4%25BA%25A7%26articleCode%3DDT_GOODS_dingtalkmemberplus%26channel%3Dopenpf_web_devdoc%26corpId%3D${corpId}%26accessoryProduct%3DpaasWithConnector%26tabKey%3DDT_GOODS_dingtalkmemberplus&popup_wnd=true&height=600&width=900)和[专属版](https://partner.dingtalk.com/opportunity_web.html?channel=openpf_web_devdoc_trial&templateId=092b3722b3fd4dd08fb641a194a90691#/consultingService)客户的专享OpenAPI。这些专享OpenAPI将提供更丰富的能力，支持不同场景下的企业内部应用开发，建议开发者更合理、有效地使用OpenAPI，打造更健康的钉钉开放生态。

## 一、新增专享OpenAPI列表

> **[!NOTE]**
>
> 钉钉可能会因法律法规或政策调整、执行监管指令所需，或者为维护钉钉服务安全性等，对以下接口的范围或具体功能进行增加、修改或删除。实际对客户开放的接口以钉钉开放平台届时公示的内容为准。

| **OpenAPI名称** | **OpenAPI详情** | **是否已上线** |
| --- | --- | --- |
| [添加待入职员工](0945-add-employees-to-be-hired-supports-system-and-custom-fields.md) | 在企业自有通讯录系统内，添加待入职员工时，调用本接口在钉钉智能人事应用内同步添加待入职员工 | 是 |
| [配置考勤排班附加信息](0211-synchronization-scheduling-information.md) | 企业考勤排班信息较多，手动配置排班的打卡位置、打卡WiFi信息比较繁琐，可调用本接口，更新排班的附加信息 | 是 |
| [查询指定用户的封账规则](0242-encapsulate-account-sealing-and-unsealing-rules.md) | 开启封账后，封账范围内的考勤结果将封存不允许修改。包含以下操作：请假，外出，出差，加班，补卡申请；员工排班，修改考勤结果等，调用本接口根据企业员工userId列表，获取员工的封账规则信息 | 是 |
| [发送DING消息](0712-robot-sends-nail-message.md) | 企业在紧急场景下，可调用本接口给指定员工发起应用内DING消息、短信DING消息和电话DING消息提醒 | 是 |
| [撤回已经发送的DING消息](0713-robot-withdraws-pin-message.md) | 已发送的DING消息，支持调用本接口进行撤回 | 是 |
| [上传打卡记录](0197-upload-punch-records.md) | 企业使用三方打卡设备或门禁系统刷卡，调用本接口，可将三方打卡或刷卡记录上传到钉钉考勤，作为员工的考勤打卡信息 | 是 |

## 二、专享OpenAPI上线时间

2023年08月01日起将陆续上线。

## **三、**专享OpenAPI**的使用条件**

上述专享 OpenAPI，标准版钉钉需要[升级专业版](dingtalk://dingtalkclient/page/link?url=https%3A%2F%2Fn.dingtalk.com%2Fdingding%2Fdd-pro-composite-order%2Fpc%2Findex.html%3Fpopup_wnd%3Dtrue%26dd_tab%3Dtrue%26width%3D900%26height%3D600%26title%3D%25E9%2592%2589%25E9%2592%2589%25E6%2595%25B0%25E5%25AD%2597%25E8%25B5%2584%25E4%25BA%25A7%26articleCode%3DDT_GOODS_dingtalkmemberplus%26channel%3Dopenpf_web_devdoc%26corpId%3D${corpId}%26accessoryProduct%3DpaasWithConnector%26tabKey%3DDT_GOODS_dingtalkmemberplus&popup_wnd=true&height=600&width=900)或[升级专属版](https://partner.dingtalk.com/opportunity_web.html?channel=openpf_web_devdoc_trial&templateId=092b3722b3fd4dd08fb641a194a90691#/consultingService)后才可申请使用；部分客户在 8 月 1 日上线前已经参与公测，获得了这些 OpenAPI的调用权限，请按以下规则调用：

| **客户类型** | **是否参与公测** | **是否受影响** |
| --- | --- | --- |
| 专业版/专属版客户 | 已参与公测 | 不受影响，继续正常调用 |
| 未参与公测 | 申请接口使用权限后，可调用 |
| 标准版客户 | 已参与公测 | 不可调用，需升级至专业/专属版后，申请接口调用权限后才能恢复调用；权限申请步骤请参考本文档第四部分的说明 |
| 未参与公测 | 不可调用，需升级至专业/专属版后，申请接口调用权限后才能调用；权限申请步骤请参考本文档第四部分的说明 |

## **四、专享**OpenAPI **权限申请步骤**

申请入口：「[**开发者后台**](https://open-dev.dingtalk.com/) **> 应用开发 > 钉钉应用 > 新建应用或已有应用 > 点击应用 > 权限管理 > 只看专业版专享接口」**

- 专业/专属版客户，在「权限申请」处，点击即可申请对应接口权限

  ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9122178861/p690996.png)
- 标准版客户，在「权限申请」处，点击跳转专业版的购买页面，[升级专业版](dingtalk://dingtalkclient/page/link?url=https%3A%2F%2Fn.dingtalk.com%2Fdingding%2Fdd-pro-composite-order%2Fpc%2Findex.html%3Fpopup_wnd%3Dtrue%26dd_tab%3Dtrue%26width%3D900%26height%3D600%26title%3D%25E9%2592%2589%25E9%2592%2589%25E6%2595%25B0%25E5%25AD%2597%25E8%25B5%2584%25E4%25BA%25A7%26articleCode%3DDT_GOODS_dingtalkmemberplus%26channel%3Dopenpf_web_devdoc%26corpId%3D${corpId}%26accessoryProduct%3DpaasWithConnector%26tabKey%3DDT_GOODS_dingtalkmemberplus&popup_wnd=true&height=600&width=900)或[升级专属版](https://partner.dingtalk.com/opportunity_web.html?channel=openpf_web_devdoc_trial&templateId=092b3722b3fd4dd08fb641a194a90691#/consultingService)后再申请接口权限。

  ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9122178861/p690995.png)

## **五、常见问题**

1. 专享OpenAPI的计费规则是什么？

   答：标准版钉钉客户无法使用专业版和专属版的专享OpenAPI，需要先[升级专业版](dingtalk://dingtalkclient/page/link?url=https%3A%2F%2Fn.dingtalk.com%2Fdingding%2Fdd-pro-composite-order%2Fpc%2Findex.html%3Fpopup_wnd%3Dtrue%26dd_tab%3Dtrue%26width%3D900%26height%3D600%26title%3D%25E9%2592%2589%25E9%2592%2589%25E6%2595%25B0%25E5%25AD%2597%25E8%25B5%2584%25E4%25BA%25A7%26articleCode%3DDT_GOODS_dingtalkmemberplus%26channel%3Dopenpf_web_devdoc%26corpId%3D${corpId}%26accessoryProduct%3DpaasWithConnector%26tabKey%3DDT_GOODS_dingtalkmemberplus&popup_wnd=true&height=600&width=900)或[升级专属版](https://partner.dingtalk.com/opportunity_web.html?channel=openpf_web_devdoc_trial&templateId=092b3722b3fd4dd08fb641a194a90691#/consultingService)后才能调用这些接口，专业版和专属版的专享OpenAPI（除发DING接口）使用时消耗专业版和专属版的OpenAPI额度，发DING接口消耗OpenAPI发DING额度。
2. 标准版客户能看到这些专享OpenAPI吗？

   答：2023年 08月 01日起，开发者可在开放平台开发者文档及[开发者后台](https://open-dev.dingtalk.com/)中看到本次上线的专享OpenAPI。
