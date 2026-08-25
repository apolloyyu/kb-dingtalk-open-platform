---
title: "接入常见问题"
source_url: "https://open.dingtalk.com/document/development/access-common-problems"
namespace: "development"
slug: "access-common-problems"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 钉钉云 > 常见问题 > 接入常见问题"
doc_id: "JCedJH4BP7"
updated_at: "2025-10-16 14:31:27"
---

> Source: https://open.dingtalk.com/document/development/access-common-problems
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 钉钉云 > 常见问题 > 接入常见问题
> Updated: 2025-10-16 14:31:27

# 接入常见问题

## 遇到问题如何咨询

1. 云产品(ECS、RDS、SLB等)使用问题首先可搜索[阿里云文档](https://help.aliyun.com/)解决，如无法得到解决可到钉钉云(阿里云)[管理控制台](https://home.console.aliyun.com/)，右上角工单-[提交工单](https://selfservice.console.aliyun.com/ticket/createIndex) ，提工单咨询
2. 钉钉云开发者后台使用问题、钉钉云解决方案相关问题可按上述流程咨询，也可登录[开发者后台](http://open-dev.dingtalk.com/)-[技术答疑](https://ding-doc.dingtalk.com/doc#/qasupport/ngliko)提交工单解决。

## 为什么要上钉钉云

1. 钉钉要保证**用户数据安全**，因此要保证ISV通过**《钉钉云推送》**等途径获取到的用户通讯录，审批等数据**不能出钉钉云，“钉钉云推送”也只能推送到钉钉云账号默认VPC中RDS中（MySql）**
2. 为了防止用户使用服务异常终止，合作终止等情况发生，钉钉要保证在用户合约期内能继续使用服务，要求用户**在ISV应用内产生的数据要在钉钉云内有留存**，保证ISV停止提供服务后钉钉能接管服务，钉钉用户能按合约正常使用服务到期为止。
3. 为避免出现**稳定性**和**安全问题，**推出了[架构最佳实践](https://open.dingtalk.com/document/isvapp/architecture-best-practices)。从技术架构上保证服务稳定性（每一项推荐产品是从故障中总结而来，是推荐架构的最低要求），例如：

（1）禁止单点服务，推荐SLB + 至少2个ECS

（2）禁止自建数据库，推荐高可用RDS

（3）禁止用户文件存储在ecs，建议用OSS

[钉钉云解决方案](https://open.dingtalk.com/document/isvapp/dingtalk-cloud-solution)是推荐技术架构的**最低要求**，因此ISV在购买[钉钉云解决方案](https://open.dingtalk.com/document/isvapp/dingtalk-cloud-solution)**基础上，**只能增加服务器（ECS，RDS）数量或升级服务器配置。

## 钉钉云和阿里云的区别

钉钉云基于阿里云基础设施，所有云产品使用和阿里云一致，区别：

1. 每个ISV拥有一个账号，与钉钉组织对应，但主账号禁用(钉钉方也无法解禁)，分配账号为[钉钉云的安全限制](https://open.dingtalk.com/document/isvapp/security-restrictions-of-dingtalk-cloud)的**子账号**
2. 钉钉云默认不开放对外网的访问，访问外网服务方法见[钉钉云的安全限制](https://open.dingtalk.com/document/isvapp/security-restrictions-of-dingtalk-cloud)，[申请钉钉云安全组白名单](https://open.dingtalk.com/document/isvapp/apply-for-dingtalk-security-group-whitelist)原因见下文
3. 钉钉云提供了钉钉相关的附加功能例如《钉钉云推送》，钉钉云解决方案购买

## 上钉钉云对于应用开发商有什么好处？

1. 让用户对数据安全放心，更大程度赢得用户信任，带来更多长久合作的用户；

2. 获取更多的接口权限，站在钉钉的“肩膀上”，提供高品质的用户体验，提升产品竞争力。

## 钉钉云入驻流程及账号问题

## 账号创建问题

登录[钉钉开发者后台](http://open-dev.dingtalk.com/)-钉钉云-用户管理，可以创建、管理用户、组，并实现授权等相关功能，且只有第三方企业应用所在企业的主管理员有操作权限。

![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2875299951/p163414.png "image.png")

## 产品无法使用或权限不足如何解决

由于钉钉云内权限限制，产品开通可在[开发者后台](https://open-dev.dingtalk.com/#/manageConsole)中开通(可翻页),操作文档见《云产品开通》

1. RAM权限已禁止开放，防止授权开通外网访问
2. VPC操作权限已禁止开放，防止授权开通外网访问
3. RDS释放权限为防止ISV误操作，为保证数据安全，请登录[开发者后台](http://open-dev.dingtalk.com/)-[技术答疑](https://ding-doc.dingtalk.com/doc#/qasupport/ngliko)提交工单
4. 由于第3点中的原因，解决方案释放也需要，请登录[开发者后台](http://open-dev.dingtalk.com/)-[技术答疑](https://ding-doc.dingtalk.com/document/contactus)提交工单
5. RDS公网地址禁止开放（迁移期间可临时开放便于DTS迁移，原因见“哪些数据要在钉钉云内”）
6. DTS禁止开通（迁移期间报备后可临时开放，报备请登录[开发者后台](http://open-dev.dingtalk.com/)-[技术答疑](https://ding-doc.dingtalk.com/doc#/qasupport/ngliko)提交工单）

## 钉钉云部署问题

## 哪些数据要在钉钉云内

1. 钉钉用户的数据（通讯录，审批，特殊接口获取数据）只能获取并存放在钉钉云内，不可以传出钉钉云，数据库也不可以开放对公网访问地址
2. 钉钉用户在ISV应用中产生的数据要在钉钉云内有留存
3. 钉钉云内服务产生的**日志信息**不能出钉钉云，分析处理要在钉钉云内进行。
4. OSS，RDS等数据相关产品需要用**内网地址**访问，如无法通过内网操作，可在[开发者后台](http://open-dev.dingtalk.com/)申请安全组白名单。开发者提交申请时，需提供充分理由。
5. 由于上述各原则钉钉业务相关服务要迁移到钉钉云内，规模和风险较大的情况需短期上线要承诺完整迁移时间点并按上述原则有限开放访问权限

## 如何访问外网服务和外网访问申请原则

外网访问原则是，**钉钉用户数据不能出钉钉云，**一切可能造成钉钉用户数据泄漏的外网访问端口都不予开放

1. 由于“**哪些数据要在钉钉云内**”中原则，将钉钉**用户数据导出钉钉云的一切接口、服务不允许开通访问**（作为用户企业，一定不希望自己的组织架构，人员信息，内部流程暴露到公网，因此这些数据不能出钉钉云）
2. “商务合作规定”限制使用和钉钉有利益冲突的服务商提供的服务（例如其他服务商提供的企业效能工具，沟通工具等），以免造成数据泄漏
3. 对外部数据库访问的安全组规则不批准开放，同样外网访问钉钉云数据库端口，rds的接口也不批准开放
4. 申请过程中

（1）二方服务是指阿里集团产品直接提供的服务，通常可以审批通过或自动审批。ISV或三方租用阿里云服务器，部署在阿里云公有云的业务或OSS存储之类不算阿里2方服务。

（2）三方服务通常指第三方机构例如讯飞语音服务，三方短信服务，国家征信查询接口等由可靠公共第三方服务商提供的服务。如阿里云有替代服务，应选用阿里云服务，若无法迁移需提供详细充分理由，否则系统会自动审批拒绝

（3）ISV自建服务

服务商自家架设服务，申请时需详细列出出网访问接口文档和充分申请理由并满足1，2，3原则，否则直接拒绝不予通过

详细文档见[钉钉云的安全限制](https://open.dingtalk.com/document/isvapp/security-restrictions-of-dingtalk-cloud)，[申请钉钉云安全组白名单](https://open.dingtalk.com/document/isvapp/apply-for-dingtalk-security-group-whitelist)

## 部署ECS登录相关问题

ECS默认无公网IP不可直接连接SSH进行部署

**推荐方案：**

1. 通过ECS提供的WebShell或远程桌面工具进行登录部署，部署期间，申请通讯录权限前，可申请安全组白名单临时开放完成部署，部署后恢复安全组限制
2. 开通堡垒机，通过堡垒机实现登录ECS完成部署

**不推荐方案：**

1. 购买EIP绑定ECS 直接通过EIP访问ECS
2. SLB绑定22端口转发到ECS

**此两种方案非常容易被黑客利用，造成严重损失。此前已有ISV因长期绑定EIP到ECS方便连接部署而被黑客利用并造成损失。**

## 是否可以不购买钉钉云解决方案

参考[接入必读](https://open.dingtalk.com/document/isvapp/access-required)，这些情况是必须部署在钉钉云[钉钉云解决方案](https://open.dingtalk.com/document/isvapp/dingtalk-cloud-solution)中。并且如解决方案，只能增加或提高配置，不能减少。

若企业使用非MYSQL数据库，而解决方案中只包含MYSQL的RDS数据库。则需要在解决方案基础上添加购买自己需要的数据库（例如mongodb等）

由于钉钉云推送使用的是解决方案中RDS，因此不能释放。免登推送，通讯录推送都是需要解决方案中的RDS。

## 钉钉云财务/支付等问题

## 先开发票，签订合同后申请财务报销

目前原生钉钉云无法申请信控（信用额度），也无法支持客户已获得的阿里云折扣，只能享受钉钉云统一折扣

因此钉钉云需要产生交易并付款后，才可以申请合同和发票。

针对需要先提供发票和合同的开发者，建议和本公司财务沟通，走公司借款流程购买，之后再申请发票合同进行报销。大客户特殊折扣可选用钉钉云无迁移方案，具体请提交[技术支持](https://ding-doc.dingtalk.com/document/contactus)咨询。

## 如果钉钉云中现有支付方式无法满足需求，如何充值

钉钉云线下汇款用这个账号，需要您走对公打款流程，打款成功后提交汇款底单认领款项到您的钉钉云账号。提交方式：登录钉钉云(阿里云)[管理控制台](https://home.console.aliyun.com/)，右上角工单-[提交工单](https://selfservice.console.aliyun.com/ticket/createIndex)反馈。

汇款信息如下：

![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2875299951/p163415.png "image.png")

## 费用/合同/发票问题

**（1）付款** 钉钉云**不收取费用,**基础设施,云产品由阿里云直接提供,在管理控制台直接操作即可,方式流程和阿里云一致详见“[充值/退款等财务问题](https://open.dingtalk.com/document/isvapp/financial-problems-such-as-recharge-refund)”

**（2）合同申请** 同阿里云流程，直接在“管理控制台”右上角“费用中心”、[“合同管理”](https://expense.console.aliyun.com/#/contract/apply/selectOrder)申请，文档见“[合同管理文档](https://help.aliyun.com/document_detail/92606.html?spm=5176.11065259.1996646101.searchclickresult.26e432ae4bz6mX)”

**（3）发票申请** 同样在[费用中心](https://expense.console.aliyun.com/#/account/home)中申请发票,发票信息为钉钉开发者后台高级认证时提供公司信息，文档见“[充值/退款等财务问题](https://open.dingtalk.com/document/isvapp/financial-problems-such-as-recharge-refund)”

## 钉钉云数据推送问题

排查方案请查看[钉钉云推送概述](https://open.dingtalk.com/document/isvapp/dingtalk-push-service)。

## 原有服务迁移到钉钉云

| **迁移方案** | **说明** |
| --- | --- |
| **阿里云迁移到钉钉云** | 钉钉云基础设施由阿里云提供，因此云产品和阿里云使用保持一致。在迁移到钉钉云过程中，只需要将数据利用阿里云迁移工具（例如DTS等）迁移到钉钉云，按同样方式将服务重新部署在钉钉云内即可完成迁移。 |
| **自建机房迁移到钉钉云** | 自建机房迁移到钉钉云需先了解阿里云[公有云产品](https://www.aliyun.com/product/list)，然后对应ECS类比为服务器，RDS为数据库产品等在钉钉云上进行公有云部署。 |
| **由于迁移服务工作量大等原因无法迁移至钉钉云** | 钉钉云提供一套无迁移入驻方案，开发者可以使用自有阿里云账号钉钉云托管的方式，在原有阿里云中提供服务。前提条件：愿意禁用自有账号主账号并托管给钉钉管理，其他一切安全规则和钉钉云保持一致。具体操作细节工单询问钉钉云管理员。 |
