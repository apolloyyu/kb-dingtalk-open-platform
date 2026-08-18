---
title: "组件监控"
source_url: "https://open.dingtalk.com/document/dingstart/component-monitoring-1"
namespace: "dingstart"
slug: "component-monitoring-1"
group: "工作台"
tab: "使用教程"
breadcrumb: "组件教程 > 全码组件 > 组件监控"
doc_id: "t2O0a94n8v"
updated_at: "2025-10-22 18:05:56"
---

> Source: https://open.dingtalk.com/document/dingstart/component-monitoring-1
> Path: 工作台 / 使用教程 / 组件教程 > 全码组件 > 组件监控
> Updated: 2025-10-22 18:05:56

# 组件监控

本文介绍了工作台组件的监控和告警方式。用户通过组件监控可以有效的了解钉钉组件各项指标运行情况，及时接收关键指标告警。

## 名词解释

| **名词** | **解释** |
| --- | --- |
| 插件 | 组件的代码集，一个插件内可以包含多个组件，每一个组件可单独承载不同的业务形态。每次功能更新、发布时，只能针对插件维度操作。 |

## 访问监控中心

钉钉开放平台提供了对组件进行实时监控的入口，如你需要查看监控，可参考以下步骤：

> **[!NOTE]**
>
> 只有定制服务商的身份才能查看监控，如何成为定制服务商，请参考[通过产品方案商开通](../01-ECKYIf1yqx-平台介绍/0002-how-to-become-a-dingtalk-customization-service-provider-1.md)。

1. 登录[开发者后台](https://open-dev.dingtalk.com/)。
2. 依次选择**定制服务**>**插件管理**，选择目标插件，单击**监控中心。**

   ![组件监控背景截图](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7231115261/p290681.png)

## 监控

### 查看监控大盘

监控中心界面，如下图所示：

![监控中心_查看监控大盘](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8231115261/p290724.png)

### 基本指标

监控基本指标如下图所示：![监控中心_实时大盘](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1014658261/p290726.png)

- js异常
- API成功率（数据源接口成功率）
- 页面访问
- 插件加载：从工作台加载插件到插件加载完毕，x轴为当前时间

  - 上报次数
  - 成功率
  - 加载时长

### 高级查询

如果想查询特定条件的数据（如用户维度、企业维度），需要用到高级查询。

- 查询界面，如下图所示：![高级查询_查询界面](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1014658261/p290735.png)

  **可查询监控指标：**

  - JS异常
  - API请求
  - 插件加载
- 列表界面，如下图所示：![高级查询_列表界面](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1014658261/p290745.png)

  **基础字段介绍（所有监控类型通用的字段）**

  - 用户ID：加密后的uid。
  - 前端版本：插件版本。
  - 自定义字段(c1)：企业的corpId。
  - 自定义字段(c2)：用户的员工id（[OA管理后台](https://oa.dingtalk.com/#/welcome) > 通讯录里的员工工号）。

### 查询某条日志详情

查看日志详情页面，可参考以下步骤：

1. 选择需要查看的日志，单击**设为筛选**。

   ![设为筛选](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1014658261/p290754.png)
2. 设为筛选后，单击**高级查询**，进入高级查询页面。

   ![方式二进入高级查询](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8112858261/p290755.png)
3. 进入高级查询页后，可设置不同搜索条件，查询对应的日志详情。

   ![日志页面详情页面 ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8112858261/p290752.png)

**查询特定指标的访问日志**

如果你需要查询特定指标的访问日志，可参考以下步骤（以corpId为例）：

> **[!NOTE]**
>
> 可以看到这个企业里所有指标日志，也可以将corpId换为前端版本、客户端、操作系统等其它指标。

1. 在高级查询页面，单击**+**号添加参数（可以添加多个参数）。

   ![添加多个参数](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8112858261/p290761.png)
2. 选择**自定义字段(c1)**或者**企业id(c1)**。

   ![选择自定义字段](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9112858261/p290764.png)
3. 在参数值中填入cropid，最后单击**查询**。

   ![单击查询](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9112858261/p290766.png)

**查询用户访问路径**

如果你需要查询用户的访问路径，可通过以下两种方式获取：

- 方式一

  1. 选择需要查看的日志，单击**查看日志**，进入日志信息界面。

     ![查看日志按钮 ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9112858261/p290750.png)
  2. 在日志信息界面，单击**用户路径分析**，进入路径分析界面。

     ![路径分析详情](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6121215261/p290768.png)用户路径分析界面如下图所示：

     ![用户路径分析界面](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9112858261/p290771.png)
- 方式二

  1. 单击**高级查询**，进入日志列表界面。

     ![日志页面详情页面 ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8112858261/p290752.png)
  2. 在日志列表界面，选择**用户ID**，最后选择**用户路径分析**，进入路径分析界面。

     ![高级查询路径分析](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9112858261/p290773.png)用户路径分析界面如下图所示：

     ![用户路径分析界面 ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9112858261/p290771.png)

## 告警

### 扫码进入告警群

如果你需要接收关键指标（数据源接口、jserror等）告警，可参考以下步骤：

1. 登录[开发者后台](https://open-dev.dingtalk.com/)。
2. 依次选择**定制服务** > **插件管理**，选择目标插件，单击**监控中心。**

   ![组件监控背景截图 ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7231115261/p290681.png)
3. 在监控中界面，通过手机扫描二维码加群。

   > **[!NOTE]**
   >
   > 需要在服务商企业内的员工才能进入告警群。

   ![扫描二维码加群](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7121215261/p290775.png)

### 稳定性运营策略

如果你需要了解工作台组件的稳定性规范和稳定性运营策略，可参考[工作台组件稳定性规范](https://open.dingtalk.com/document/services/inventory-management-console-component-stability-specifications)。
