---
title: "概述"
source_url: "https://open.dingtalk.com/document/development/overview-of-e-sign-open-ability"
namespace: "development"
slug: "overview-of-e-sign-open-ability"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "行业与生态 > 生态开放 > e签宝 2.0 > 概述"
doc_id: "4PVkytyOst"
updated_at: "2026-06-23 18:05:03"
---

> Source: https://open.dingtalk.com/document/development/overview-of-e-sign-open-ability
> Path: 应用开发 / 服务端 API / 行业与生态 > 生态开放 > e签宝 2.0 > 概述
> Updated: 2026-06-23 18:05:03

# 概述

本文档介绍了什么是e签宝，如何开通e签宝，e签宝接口能力和咨询方式等。

## 什么是e签宝

e签宝是一款第三方电子合同签名的SaaS服务产品，主要服务于政企大客户，实名认证企业和个人身份、管理用户密钥和签名、印章、提供在线签名、签章服务、提供第三方举证服务，用户可以通过手机或电脑实现有法律效力的电子文件签署或签章。

e签宝提供了丰富的API接口，为用户提供一套完整的全生态电子签名服务，为客户提供具有法律效力的电子合同全生命周期服务，将原本需要耗费数日之久的文件签署环节，压缩到只需几十秒，降本增效。

开发者（企业和产品方案商）可以通过按照自己的业务流程选择对应的API接口，**通过电子签名能力集成，助力用户系统性解决传统纸质签署难题，是企业全面实现企业数字化的重要一环。**

电子签名产品不单单是用印盖章，还包含了**认证服务**（依托高品质数据源对比、人脸识别技术等、为用户提供可信、可靠、灵活的身份认证以广泛应用，满足各行业的身份认证需要）和**区块链数据存证服务**（使用数字签名、时间戳等技术加密保存，全方位保全电子数据以备司法所需）。

e签宝的核心价值包括：

- 便捷：在钉钉中微应用天然存在的便捷优势。
- 免注册，免邀请，免登录。
- 自动拥有企业组织架构。
- 与钉钉通讯录打通。
- 通过钉钉工作通知下发电子签相关任务等。
- 智能：融合钉钉的智能合同。
- 融合钉钉审批、钉钉e签宝等钉钉核心功能和电子合同做融合，与企业在钉钉里的各业务流程结合，助力钉钉用户签电子合同时减少人工搬运数据，人工搬运文件等人为操作（例如自动填充合同）实现钉钉里特色的智能合同。

### **基本功能**

基于数字证书实现的电子签名具有以下三种基本的安全功能：

- **身份认证**：数字证书可以用于证明签署人在网络上的身份，通过判断证书的有效性和证书内容，可以识别签署人的身份信息。
- **防抵赖**：在签订电子合同时需要签署人使用自己的私钥证书进行签名，签名后合同文件数据和签名数据都将保存到PDF文件中，一旦出现纠纷，使用签署人的公钥证书即可证明本次签名为签署人行为，从而实现签名的防抵赖。
- **防篡改**：电子合同签订后不应该再被修改，使用签署人的公钥证书就可以验证电子合同中的数据是否被篡改，从而实现电子合同的完整性和防篡改性。

![电子合同示例](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8161684261/p289677.png)

### **合法性**

e签宝成立于2002年12月，是中国互联网电子签名行业的领跑者。

e签宝提供的系列产品服务受到公安部、国密局、法院、仲裁委、公证处等专业资质认可。

2005年4月1日《中国人民共和国电子签名法》（以下简称《电子签名法》）正式施行，从法律上保障了电子签名的效力。

![司法实践判例](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8161684261/p289666.png)

### **应用场景**

所有企业需要用印、签合同、签字的场景都可以选择e签宝提供的这套电子签名API与业务流程对接实现线上化、数字化。

- **人力资源**：劳动合同、保密协议、竞业协议、工作证明等
- **B2C**：在线教育服务合同、装修协议、租赁合同等
- **B2B**：销售合同、采购合同、供应链合同、分销协议、产品授权书等

#### **【人事场景】电子签名API与CMS系统集成**

门店店长通过CMS管理系统录入员工入职信息，总部HR审核生成的合同信息，确认无误实名认证员工信息，发起签署盖章，员工收到签署短信，手机上完成劳动合同签署。

![场景一](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8161684261/p289696.png)

#### **【供应链场景】电子签名API与采购平台集成**

采用了e签宝电子合同后，合同管理成本大大降低了，合同签署的周期也大大缩短了。

![场景二](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8161684261/p289697.png)

## 如何开通e签宝免费版

1. 钉钉扫码安装e签宝微应用。

   ![二维码 ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8712693161/p242337.png)
2. 进入e签宝微应用完成企业认证。如何完成企业认证，详情可参考[企业实名认证](https://www.yuque.com/docs/share/3f0db464-f414-406d-aa28-4c8f06a6dd60?#)。

## 开放概览

> **[!IMPORTANT]**
>
> **接口能力属于e签宝付费版功能，如需使用请联系您的客户经理。**

e签宝提供了丰富的接口开放能力，开发者通过API接口可以实现e签宝和企业业务系统打通。

### **鉴权**

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [e签宝数据初始化](1071-isv-service-provider-data-initialization.md) | 帮助钉钉企业进行e签宝开放平台的数据初始化。 | 新版 |
| [获取授权的页面地址](1072-obtain-the-address-of-the-authorized-page.md) | 获取企业授权的页面地址。 | 新版 |
| [取消企业授权](1073-cancel-enterprise-authorization.md) | 取消授权过企业的授权状态。 | 新版 |

### **套餐**

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [套餐转售—分润模式](1074-package-resale-1-distribution-mode.md) | 为使用电子合同的用户创建转售订单。 | 新版 |
| [套餐转售—底价结算模式](1075-package-resale-2-reserve-price-settlement-mode.md) | 直接转售e签宝订单给最终真正使用电子合同的用户。 | 新版 |
| [查询套餐余量](1076-query-package-balance.md) | 查询当前企业的套餐余量。 | 新版 |

### **用户**

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [获取企业的e签宝微应用状态](1077-obtain-the-current-status-of-the-company-s-e-sign-micro-application.md) | 查询企业是否已在e签宝完成实名认证。 | 新版 |
| [查询企业是否实名认证](1078-query-enterprise-information.md) | 直接转售e签宝订单给最终真正使用电子合同的用户。 | 新版 |
| [获取企业控制台地址](1079-get-enterprise-console-address.md) | 获取的企业在e签宝的控制台地址。 | 新版 |
| [查询个人是否实名认证](1080-query-personal-information.md) | 查询当前用户是否已在e签宝完成实名认证。 | 新版 |
| [获取个人实名的地址](1081-obtain-the-address-that-is-redirected-to-the-user-s-real.md) | 通过个人信息接口查询到个人未实名时，可调用本接口获取个人实名认证地址。 | 新版 |
| [获取跳转到企业实名的地址](1082-obtain-the-address-that-is-redirected-to-the-enterprise-s-real.md) | 通过企业信息接口查询到企业未实名时，可调用本接口获取实名地址，在应用内展示给企业。 | 新版 |

### **文件**

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [获取文件上传地址](1085-obtain-the-upload-url-of-a-file-1.md) | 获取到文件上传地址。 | 新版 |
| [获取文件详情](1084-gets-the-file-details.md) | 查询文件详情。 | 新版 |

### **签署流程**

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [获取发起签署任务的地址](1089-obtain-the-address-used-to-initiate-a-signed-task.md) | 获取发起签署任务的地址。 | 新版 |
| [创建签署流程](1086-use-the-api-to-initiate-a-signature-process.md) | 当ISV侧企业有文件需签署时，可调用本接口获取发起签署地址。 | 新版 |
| [获取签署人签署地址](1087-get-signatory-address.md) | 获取签署人签署地址。 | 新版 |
| [获取流程的签署详情](1088-get-the-details-of-process-signing.md) | 根据taskId获取流程签署相关的详细信息。 | 新版 |
| [获取流程任务用印审批列表](1090-obtains-the-print-approval-list-for-process-tasks.md) | 获取流程任务用印审批列表。 | 新版 |
| [获取流程详细信息及操作记录](1091-obtains-the-task-details.md) | 获取流程详细信息及操作记录。 | 新版 |
| [获取流程任务的所有合同列表](1092-get-a-list-of-all-contracts-for-the-process-task.md#undefined) | 获取流程任务的所有合同列表，收到签署完成消息后查询。 | 新版 |
