---
title: "最佳实践：企业年度个性化报告"
source_url: "https://open.dingtalk.com/document/aipass/best-practice-annual-personalized-corporate-reporting"
namespace: "aipass"
slug: "best-practice-annual-personalized-corporate-reporting"
group: "数据资产"
tab: "宜数（智能问数）"
breadcrumb: "数据资产 > 最佳实践：企业年度个性化报告"
doc_id: "BYPta157oj"
updated_at: "2026-08-14 09:27:01"
---

> Source: https://open.dingtalk.com/document/aipass/best-practice-annual-personalized-corporate-reporting
> Path: 数据资产 / 宜数（智能问数） / 数据资产 > 最佳实践：企业年度个性化报告
> Updated: 2026-08-14 09:27:01

# 最佳实践：企业年度个性化报告

## **案例介绍**

某金融行业客户会在年末输出面向管理者和普通员工的两份年度数据总结报告，期望通过数据洞察和分析，让管理者快速回顾企业一年的经营状况，发现管理效率提升方向，让员工个人的努力被看见，提升员工的归属感和动力，从而推动整个企业的发展进步。

## **产品方案**

宜数基于钉钉全域数据资产，针对企业年度总结、回顾场景，提供组织、部门、员工多视角的年报数据，支持一键启用，快速上线，同时也提供数据接口服务，支持有研发和设计资源的企业，快速搭建年报页面。

![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0245754371/p889108.png)

## **搭建流程**

> **[!NOTE]**
>
> 以下流程可参考帮助手册：[企业年度报告模板](../01-fIz0pQ6X4y-平台介绍/0016-enterprise-annual-report-template.md)。

### **方案一：使用模板定制专属年报**

提供开箱即用的设计模板，丰富的数据项，5分钟快速定制专属年报。

1. 开通并登录钉钉数据资产平台，申请权限（[平台入口](https://open-dev.dingtalk.com/fe/daas)，[开通及登录方式](../01-fIz0pQ6X4y-平台介绍/0002-opening-and-login-method.md)）。
2. 左侧菜单，选择“数据解决方案”。
3. 方案列表，选择“企业年度报告模板”。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0245754371/p889099.png)
4. 方案选择，提供三种统计对象的预置方案：组织年报（面向管理员和老板）、部门年报（面向部门主管）、员工年报（面向普通员工）。选择其中的一种，点击“查看”进入年报编辑页面，支持用户对预置信息二次编辑，修改范围包括图片、背景音乐、文案、数据源。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0245754371/p889095.png)

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0245754371/p889096.png)
5. 编辑无误后，点击发布，即可投放使用。目前支持二维表、URL链接两种方式查看。

### 方案二：使用接口定制个性化年报

提供年报数据API，开发者可基于API定制个性化年报：

1. 开通并登录钉钉数据资产平台，申请权限（[平台入口](https://open-dev.dingtalk.com/fe/daas)，[开通及登录方式](../01-fIz0pQ6X4y-平台介绍/0002-opening-and-login-method.md)）。
2. 左侧菜单，选择“数据服务-数据API”。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0245754371/p889098.png)
3. 在数据项列表中，选择“专题数据-年度报告-明细数据”；其中提供三种预置数据：企业年报（面向管理员和老板）、部门年报（面向部门主管）、员工年报（面向普通员工）。选择其中的一种，勾选其中需要的指标字段，下一步，进行接口定义。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0245754371/p889094.png)
4. 接口定义，包括指标选择与确认、基础信息配置、数据过滤设置、查看数据样例、测试调用、发布、审核。（具体可参见[打包数据API接口](../01-fIz0pQ6X4y-平台介绍/0017-packaged-data-api-interface.md)）。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0245754371/p889097.png)
5. 接口完成发布审核后，即可在内部系统进行调用使用，企业结合具体需求自行设计年报呈现方式和样式。
