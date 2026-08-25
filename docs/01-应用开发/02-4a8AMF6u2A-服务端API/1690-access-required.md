---
title: "接入必读"
source_url: "https://open.dingtalk.com/document/development/access-required"
namespace: "development"
slug: "access-required"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 钉钉云 > 接入必读"
doc_id: "b3ntbzadVy"
updated_at: "2025-10-16 14:31:10"
---

> Source: https://open.dingtalk.com/document/development/access-required
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 钉钉云 > 接入必读
> Updated: 2025-10-16 14:31:10

# 接入必读

> **[!IMPORTANT]**
>
> 服务商可以根据不同的分发方式选择部署方式，请参考[部署概述](https://open.dingtalk.com/document/isvapp/deployment-overview)。

钉钉云专注于提供安全、稳定、易用、好用的云服务。目前钉钉云的服务目标主要是应用服务商，后续钉钉云也会为企业提供简单易用的上云服务，帮助企业快速接入钉钉生态体系，进入移动云服务时代。以下是推荐接入流程：

![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9475299951/p163325.png "image.png")

**1.了解钉钉云**

（1）开发者需了解钉钉云的目标、钉钉云和阿里云的关系，详情参考[钉钉云介绍](https://open.dingtalk.com/document/isvapp/dingtalk-cloud-2)。

（2）原则上钉钉云不允许跟外部系统有数据交换，开发者需了解钉钉的安全限制，用于评估是否接入钉钉云，详情参考[钉钉云的安全限制](https://open.dingtalk.com/document/isvapp/security-restrictions-of-dingtalk-cloud)。

（3）在钉钉云购买的阿里云资源可享受折扣优惠，开发者可以初步了解钉钉云价格（仅供参考，价格请以实际购买时产生的费用为准），用于评估是否接入钉钉云，详情参考

[钉钉云产品的价格](https://open.dingtalk.com/document/isvapp/dingtalk-prices-of-cloud-products)。

（4）在钉钉云购买云产品时，开发者可能会遇到财务问题，详情参考[充值/退款等财务问题](https://open.dingtalk.com/document/isvapp/financial-problems-such-as-recharge-refund)。

**2.评估是否接入钉钉云**

开发者初步了解钉钉云后，评估当前的应用是否需要接入钉钉云。当前需上架到广场的第三方企业应用必须接入钉钉云，其他场景开发者可以评估后按需接入。详情参考[使用钉钉云的场景](https://yuque.antfin-inc.com/bgrkdl/ln6dmh/wbhq0x)。

**3.申请钉钉云账号**

如果确定应用需接入钉钉云，需申请钉钉云账号，可以选择以下其中一种方式申请钉钉云账号。

（1）申请钉钉云账号，开发者登录[开发者后台](http://open-dev.dingtalk.com/)，申请钉钉云账号。申请流程参考[申请钉钉云账号](https://open.dingtalk.com/document/isvapp/apply-for-a-dingtalk-cloud-account-1)。

（2）如果已有阿里云账号，开发者可以将阿里云账号托管成钉钉云账号。参考[阿里云账号托管为钉钉云账号](https://open.dingtalk.com/document/isvapp/hosted-as-dingtalk-alibaba-cloud-account)。

**4.开通/购买云产品**

阿里云有较多的云产品，不同的云产品开通方法不同。

（1）针对需上架到广场的第三方企业应用，钉钉云提供了解决方案，便于开发者减少上架时遇到的稳定性审核问题，提升上架效率。应用在上架过程中，需提交稳定性审核报告，稳定性会审核架构等内容。钉钉云解决方案符合最佳实践，开发者无需自行购买云产品进行配置。

如果开发的是第三方企业应用类型，且需上架到广场，需要使用钉钉云解决方案。购买流程参考[钉钉云解决方案](https://open.dingtalk.com/document/isvapp/dingtalk-cloud-solution)。

（2）其他云产品开通，开通参考[开通云产品](https://open.dingtalk.com/document/isvapp/activate-alibaba-cloud-products)。

**5.应用部署**

应用部署阶段，包括申请白名单、钉钉云推送数据等，开发者可以按需接入；

**（1）申请钉钉云安全组白名单**

原则上钉钉云不允许跟外部系统有数据交换，如果系统需要依赖钉钉云外部的服务，需要增加更多的安全组权限，请在[开发者后台](https://open-dev.dingtalk.com/)提交相应的申请。 申请方法参考[申请钉钉云安全组白名单](https://open.dingtalk.com/document/isvapp/apply-for-dingtalk-security-group-whitelist)。

**（2）钉钉云数据推送**

钉钉云推送支持钉钉和ISV之间的数据传输，也能够支持钉钉和企业开发者之间的数据传输，并且支持开发者的本地开发调试和线上部署运维，简化了企业接入钉钉的流程。开发者可以按需使用，详情参考[钉钉云推送概述](https://open.dingtalk.com/document/isvapp/dingtalk-push-service)。

[接入常见问题](https://open.dingtalk.com/document/isvapp/access-common-problems)列出了接入过程中的常见问题，开发者在接入过程中遇到问题，可通过文档查找解决方法。
