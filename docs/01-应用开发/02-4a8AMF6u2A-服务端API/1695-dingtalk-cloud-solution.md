---
title: "钉钉云解决方案"
source_url: "https://open.dingtalk.com/document/development/dingtalk-cloud-solution"
namespace: "development"
slug: "dingtalk-cloud-solution"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 钉钉云 > 开通/购买云产品 > 钉钉云解决方案"
doc_id: "yGGUp5U7cZ"
updated_at: "2026-07-24 09:16:15"
---

> Source: https://open.dingtalk.com/document/development/dingtalk-cloud-solution
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 钉钉云 > 开通/购买云产品 > 钉钉云解决方案
> Updated: 2026-07-24 09:16:15

# 钉钉云解决方案

钉钉云解决方案是基于钉钉云/阿里云基础设施，为应用提供服务端的一站式云服务解决方案，是钉钉云架构最佳实践的具体实现方案。帮助开发者实现资源自动购买、应用快速创建和基础监控自动化，显著降低接入成本。

## **核心优势**

- **提高效率**

  提供一键式构建方案，大幅降低钉钉应用接入门槛，缩短部署周期。
- **高可用性**

  基于阿里云高可用、可扩展的技术架构设计，支持自有业务快速增长，保障系统稳定性。
- **合规上架推荐**

  **对于需上架到钉钉广场的应用，强烈推荐使用钉钉云解决方案。**钉钉云解决方案已将架构最佳实践整合，符合上架规范，开发者只需一键式构建方案，减少上架过程中的问题。

  > **[!NOTE]**
  >
  > 若开发者自行购买资源，资源配置等需与解决方案相同，可能会影响上架时效。

## 解决方案版本

针对用户的差异化需求，钉钉云提供三种标准化版本：**基础版、升级版、高级版**。不同版本在资源数量配置、带宽等方面不同。

> **[!NOTE]**
>
> 以下价格仅供参考，实际以购买时页面展示为准。计费模式默认为按量付费，单位为人民币（元）。详细产品介绍见：[什么是云服务器ECS](https://www.aliyun.com/product/ecs)、[RDS](https://help.aliyun.com/product/26090.html?spm=a2c4g.11186623.6.539.109b576bLuDbQ8)、[负载均衡](https://help.aliyun.com/product/27537.html?spm=a2c4g.11186623.6.539.6cce6327GQ0wtt)、[NAT](https://help.aliyun.com/product/44413.html?spm=a2c4g.11186623.6.539.515b24d6zXp2k5)、[EIP](https://help.aliyun.com/product/61789.html?spm=a2c4g.11186623.6.539.55641742VUr3GA) 。

| **版本** |  | **ECS** | **RDS** | **SLB** | **NAT** | **EIP** | **价格** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **基础版**  (支持几百企业客户) | **规格** | sn1ne.large | MySQL 5.7 高可用版 2核4G 20G存储 | 标准型I(slb.s2.small) | 小型 | 5M（入）2M（出） | 17,618.10/年  79.128/天(流量0.8/G) |
| **数量** | 2 | 1 | 1 | 1 | 2 |
| **升级版**  (支持几千企业客户) | **规格** | sn1ne.xlarge | MySQL 5.7 高可用版 4核8G 20G存储 | 标准型II(slb.s2.medium) | 中型 | 10M(入)4M（出） | 41,517.11/年  190.592/天(流量0.8/G) |
| **数量** | 3 | 1 | 1 | 1 | 2 |
| **高级版**  (支持几万企业客户) | **规格** | sn1ne.2xlarge | MySQL 5.7 高可用版 8核16G 20G存储 | 高阶型I(slb.s3.small) | 大型 | 20M(入)8M（出） | 95,776.02/年  462.744/天(流量0.8/G) |
| **数量** | 4 | 1 | 1 | 1 | 2 |

### **注意事项**

- **NAT 共享机制**

  NAT为钉钉云账号共用，多个解决方案会共用一套NAT。购买基础版解决方案(带NAT)后，再次购买解决方案不会加入NAT费用，NAT费用请以实际创建解决方案时为准。如果NAT为多解决方案共用，开发者需要考虑NAT绑定EIP带宽问题，必要时自行升级。
- **计费模式说明**

  用户根据规格，选配合适的解决方案，**默认为按量收费**，可在解决方案详情页“转包年包月”。
- **扩容与变配规则**

  支持对现有解决方案进行**扩容**（增加 ECS 实例数量）或**升配**（提升 ECS/RDS 规格），但**不支持降配或删除资源**。例如购买解决方案之后，通过钉钉云解决方案扩容，或在阿里云控制台购买OSS，Redis等。
- **版本升级限制**

  解决方案不支持直接升级（例如基础版升级为高级版，需要手动迁移），可根据自己需求购买合适的解决方案后进行升级配置和扩容来提升服务性能。**其中体验版不支持扩容，支持升配。**

## 购买解决方案

钉钉云账户可以购买多个解决方案，建议每个应用购买一个解决方案。购买前请确认账户余额 **大于 100 元**（最低消费门槛，低于此金额无法下单）。

更多财务操作（充值、退款等）详见：[充值/退款等财务问题](https://open.dingtalk.com/document/isvapp/financial-problems-such-as-recharge-refund)。

### **步骤一，登录解决方案控制台**

**未注册用户**：请先申请钉钉云账号，操作指引见 [申请钉钉云账号](https://open.dingtalk.com/document/isvapp/apply-for-a-dingtalk-cloud-account-1)。

**已有账号**：

1. 进入[开发者后台](https://open-dev.dingtalk.com/#/cloudHome) > **钉钉云** > **基础信息**，点击**登录控制台**。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0354299951/p163335.png "image.png")
2. 输入用户名密码，登录控制台。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0354299951/p163336.png "image.png")
3. 登录后，进入钉钉云解决方案首页，在解决方案首页可以创建、管理钉钉云解决方案，查看解决方案的基础监控。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0354299951/p163337.png "image.png")

### **步骤二，创建解决方案**

1. 点击解决方案页面右上角“创建新方案”按钮，创建解决方案。

   - 输入解决方案名称：建议和小程序名称一致，方便区分。

     ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1354299951/p163338.png "image.png")
   - 选择运行环境：如 Java、PHP、Node.js、Python 或纯净 CentOS 7.x。

     ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1354299951/p163339.png "image.png")
   - 选择“资源规格”。

     > **[!NOTE]**
     >
     > 购买默认为按量付费（按使用天数及流量计费），页面显示为包年价格。

     ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1354299951/p163340.png "image.png")
2. 选择规格后，点击**立即购买**，并完成付款流程。系统开始自动创建钉钉云解决方案，如下图所示：

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1354299951/p163341.png "image.png")
3. 约等待 **10 分钟**，刷新列表，当状态变为 **“运行中”** 表示创建成功。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1354299951/p163342.png "image.png")
4. 点击“详情”，“参数信息”一栏，Public Address 处，点击公网Ip进行验证，页面显示Demo正常即为创建成功。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1354299951/p163343.png "image.png")

> **[!IMPORTANT]**
>
> 在钉钉云解决方案中，仍然保持钉钉云所有安全相关的限制（安全组限制，资源释放限制避免意外释放导致事故等）。如购买错误，请通过[技术答疑](https://ding-doc.dingtalk.com/document/contactus)联系管理员释放资源。

### **步骤三，解决方案运行环境**

当前支持运行环境包括（可根据服务自行选择）：

- 纯净 CentOS 7.x
- Java
- PHP
- NodeJS
- Python

**Windows用户注意**：若需部署 IIS 或其他 Windows 服务，可选择“纯净 CentOS”版本，在 ECS 创建完成后停止实例，更换操作系统为 Windows Server，并自行安装所需软件完成部署。

## 解决方案管理

购买解决方案后，进入解决方案首页，跳转到解决方案管理页面，可以进行解决方案的管理。开发者常使用解决方案管理主要有：扩容升配、转包年包月、资源监控等。

### **1.扩容升配**

如果在使用过程中随流量增加，需要更高的配置或更多的资源，可在解决方案详情页面进行扩容，或直接在[云产品控制台](https://home.console.aliyun.com/new#/)对应资源项目中变更配置（详情页面资源列表可以找到解决方案对应资源，进行升配）。操作详情查看[钉钉云解决方案](#)。

### **2.转包年包月**

将按量付费转换为包年包月模式，可获得更低单价，适合长期稳定运行的应用。

操作步骤：进入解决方案详情页 → 右上角点击“转包年包月” → 选择购买时长（≥6个月）→ 完成支付。

更多详情请参阅：[转包年包月](#MkIYa)。

![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2354299951/p163355.png "image.png")

## **扩容升配置操作流程**

如果在使用过程中随流量增加，需要更高的配置或更多的资源，可在解决方案详情页面进行扩容，或直接在[云产品控制台](https://home.console.aliyun.com/new#/)对应资源项目中变更配置（详情页面资源列表可以找到解决方案对应资源，进行升配）。

### **步骤一：打开解决方案列表页面**

查看所有已购方案，点击名称或“详情”可进入详情页，也可以点击资源直接进入解决方案资源列表。

![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1354299951/p163344.png "image.png")

左侧tab第二栏提供了解决方案的基础监控，支持按方案查看 CPU、磁盘、数据库连接等关键指标。

![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1354299951/p163345.png "image.png")

### **步骤二：打开解决方案详情页**

从列表点击标题或者详情，可以进入如下解决方案详情页，着这里可以查看解决方案的基本信息，环境语言，状态参数等。

![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1354299951/p163346.png "image.png")

点击 Public Address 中的 IP 地址，可在浏览器中预览部署效果。

#### **（1）应用列表**

展示当前方案下的所有应用（内部/外部），支持查看详情或跳转至项目管理页面。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2354299951/p163347.png "image")

#### **（2）订单列表**

查看在解决方案中的消费记录，支持对未支付订单进行支付或作废操作。“详情”链接跳转至钉钉云费用中心查阅账单详情。

![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2354299951/p163348.png "image.png")

#### **（3）资源列表**

列出 ECS、RDS、SLB、EIP 等核心资源，点击实例 ID 或订单 ID 可直达对应资源详情和订单详情页面。

![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2354299951/p163349.png "image.png")

#### **（4）资源监控**

提供 ECS CPU 使用率、系统磁盘 IO、RDS连接使用率、EIP 流量等实时监控图表，支持切换时间周期（1小时/1天/7天）查看趋势。

![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2354299951/p163350.png "image.png")

#### 步骤三：执行扩容（可选）

点击右上角“扩容”按钮，根据业务需要调整 ECS 和 RDS 的数量或规格。

> **[!NOTE]**
>
> 单独在钉钉云控制台购买ECS无法加入到解决方案中，要在解决方案控制台中扩容。

![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2354299951/p163351.png "image.png")

根据自己需求，对RDS和ECS进行扩容，最少6个月周期。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2354299951/p163352.png "image")

完成支付后，扩容实例会显示在“资源列表”中显示。

**提示：**

**（1）未完成支付订单将在1天后作废。**

**（2）如果未完成支付，“扩容按钮”会变成“支付未完成扩容”，点击进入支付流程，支付未完成订单即可继续扩容**

**（3）如果需作废订单，在“订单列表”或“资源列表”中，点击未完成订单ID进入对应订单详情，作废订单即可。**

#### 步骤四：执行升配（可选）

在“资源列表”中找到要变配的资源，点击实例 ID 跳转至控制台，对要变配的 ECS 或 RDS 实例进行变配（提示：需要停止机器进行变配）。

- **ECS升配参考**

  ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2354299951/p163353.png "image.png")
- **RDS升配参考**

  ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2354299951/p163354.png "image.png")

## 转包年包月

包年包月会有更低的折扣价格。和扩容类似，所购买的解决方案也可以在对应详情页面，点击右上角转包年包月， 将按量付费方式转为包年包月方式，最短购买周期6个月。

![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2354299951/p163355.png "image.png")

## 常见问题

### Q1：一个解决方案能否支持多个小程序？

不推荐。建议 **一个小程序对应一个解决方案**，以实现资源隔离、权限管控和独立监控。多个应用混用可能导致故障扩散或管理混乱。

### Q2：解决方案与小程序/微应用的关系

- **钉钉小程序**

  [钉钉小程序](https://open.dingtalk.com/document/isvapp/introduction-to-dingtalk-mini-programs)服务端需要部署在钉钉云解决方案中，建议一个小程序部署在一个解决方案中。解决方案中所创建的应用为Service应用。Service应用对应服务化概念中的Service，可以有单个或多个Service应用构成你的小程序产品后端。对于小程序来说，至少要有一个外部Service应用以提供对外访问的入口。
- **微应用**

  微应用的前端及服务端均需部署在同一解决方案中，建议一个微应用部署在一个解决方案中，Service应用（解决方案中所创建的应用）可以是微应用的前端、服务端。
