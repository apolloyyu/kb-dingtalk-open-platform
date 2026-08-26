---
title: "查看RDS中钉钉推送的数据"
source_url: "https://open.dingtalk.com/document/development/view-the-data-pushed-by-dingtalk-in-rds"
namespace: "development"
slug: "view-the-data-pushed-by-dingtalk-in-rds"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 钉钉云 > 钉钉云数据推送 > 查看RDS中钉钉推送的数据"
doc_id: "5nifp7w8WE"
updated_at: "2025-12-18 09:29:06"
---

> Source: https://open.dingtalk.com/document/development/view-the-data-pushed-by-dingtalk-in-rds
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 钉钉云 > 钉钉云数据推送 > 查看RDS中钉钉推送的数据
> Updated: 2025-12-18 09:29:06

# 查看RDS中钉钉推送的数据

本文档介绍如何查看RDS中钉钉云推送的同步数据。本操作适用于已配置钉钉云与阿里云RDS对接的开发者，帮助您快速定位并查询组织、用户等变更事件数据。在开始前，请确保已完成钉钉云订阅配置，并授权数据同步至目标RDS实例。

## 登录阿里云管理控制台

1. 打开浏览器，访问 [开发者后台](https://open-dev.dingtalk.com)。
2. 在开发者后台依次选择 **钉钉云 > 基础信息**。
3. 点击页面中的 **登录控制台** 按钮，系统将跳转至[阿里云管理控制台](https://home.console.aliyun.com/)。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7675299951/p163371.png "image.png")
4. 登录后，在产品与服务中选择**云数据库 RDS版**。
5. 在实例列表中找到已绑定钉钉云的目标RDS实例，点击其实例ID进入详情页。
6. 进入DMS后，即可查看数据库中存储的钉钉推送数据。

   > **[!NOTE]**
   >
   > 参考文档：具体回调数据字段说明，请参见[钉钉云推送数据格式](https://open.dingtalk.com/document/isvapp/deprecated-dingtalk-cloud-push-data-format)。

## **进入DMS管理界面**

1. 在RDS实例详情页中，点击 **登录数据库** 按钮。
2. 选择使用 **DMS（Data Management Service）** 方式登录。

   > **[!NOTE]**
   >
   > DMS是阿里云提供的数据库可视化管理工具，支持SQL执行、数据查询和结构管理等功能。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8675299951/p163372.png "image")
3. 成功登录后，系统将进入DMS数据库管理控制台。
4. 在左侧数据库对象列表中，展开表结构，找到以下数据表：

   - `open_sync_biz_data`：用于常规数据量场景
   - `open_sync_biz_data_medium`：适用于中等数据量场景

> **[!NOTE]**
>
> - 数据存储周期：推送数据在RDS中保留 7天，过期数据将被自动清理。
> - 同步延迟时间：一般情况下，数据从钉钉云推送至RDS的延迟不超过 5分钟。
> - 权限要求：需具备对目标表的 SELECT 查询权限，建议使用最小权限账号以保障安全。

## 执行SQL查看数据

使用以下SQL语句可查询指定来源和业务类型的推送数据：

- `subscribe_id`：代表钉钉端配置的订阅ID，用于标识数据来源。
- `biz_type`：表示业务类型，不同数值对应不同的事件类型（如1表示组织变更，2表示用户变更等），具体取值请参考[钉钉云推送数据格式](https://open.dingtalk.com/document/isvapp/deprecated-dingtalk-cloud-push-data-format)。

### 查询语句

> **[!NOTE]**
>
> 请根据实际业务需求替换 `'xxx'` 和 `x` 为真实的 `subscribe_id` 和 `biz_type` 值进行查询。

```
-- 适用于常规数据量场景
SELECT * FROM open_sync_biz_data WHERE subscribe_id = 'xxx' AND biz_type = x;
 ---- 适用于中等数据量场景
SELECT * FROM open_sync_biz_data_medium WHERE subscribe_id='xxx' AND biz_type=x
```

### **性能建议**

若数据量较大，建议添加时间范围过滤条件，例如：

```
AND gmt_create >= '2025-04-01 00:00:00'
```

对 `subscribe_id` 和 `biz_type` 字段建立联合索引，可显著提升查询效率。

## **注意事项**

**无数据返回可能原因**：

- 订阅未成功启用或未触发相关事件。
- 查询时间范围内无符合条件的数据。
- 使用了错误的 `subscribe_id` 或 `biz_type` 值。

  - 如遇权限不足报错，请联系管理员授予相应数据库表的SELECT权限。
  - 推荐使用DMS的“SQL窗口”功能保存常用查询语句，提高后续分析效率。
