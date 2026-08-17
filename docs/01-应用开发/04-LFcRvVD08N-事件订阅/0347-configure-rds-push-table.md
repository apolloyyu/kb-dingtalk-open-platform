---
title: "配置RDS推送表"
source_url: "https://open.dingtalk.com/document/development/configure-rds-push-table"
namespace: "development"
slug: "configure-rds-push-table"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "历史文档（不推荐） > RDS推送/SyncHTTP推送 > 配置数据推送 > RDS数据推送（推荐） > 配置RDS推送表"
doc_id: "lcBu5OMCIz"
updated_at: "2025-10-16 15:06:28"
---

> Source: https://open.dingtalk.com/document/development/configure-rds-push-table
> Path: 应用开发 / 事件订阅 / 历史文档（不推荐） > RDS推送/SyncHTTP推送 > 配置数据推送 > RDS数据推送（推荐） > 配置RDS推送表
> Updated: 2025-10-16 15:06:28

# 配置RDS推送表

本文介绍计算巢配置RDS推送流程，首先要购买RDS数据库，然后配置推送表。

## RDS区域选择

| 部署方式 | 支持的区域 |
| --- | --- |
| 阿里云+计算巢（推荐） | 华东1（杭州）或者华北3（张家口） |
| 聚石塔（不推荐） | 华北3（张家口） |
| 钉钉云（不推荐） | 华东1（杭州） |

> **[!IMPORTANT]**
>
> RDS的版本必须是**5.7**或**5.6**。

## 登录阿里云控制台

登录[阿里云控制台](https://rdsnext.console.aliyun.com/dashboard/cn-hangzhou)，创建实例。![阿里云控制台-创建实例](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4795808461/p421651.png)

## 配置RDS推送表

1. 在阿里云上购买MySQL类型的RDS，建议RDS是高可用版本。![RDS](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5795808461/p420785.png)
2. 在[RDS实例列表](https://rdsnext.console.aliyun.com/rdsList/cn-zhangjiakou/basic)页面，单击已购买的RDS实例ID链接。![RDS](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5795808461/p420724.png)
3. 在RDS实例详情页面，单击**数据库管理**，然后单击**创建数据库**，创建用于接收钉钉推送的数据库**ding\_cloud\_push**。![RDS设置数据库](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7022018461/p422193.png)
4. 配置用于推送的账号，建议账号名称为dinguser，授权数据库**ding\_cloud\_push**的读写权限。![RDS](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4795808461/p420758.png)![完成数据库创建](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7022018461/p422209.png)
5. RDS默认字符集是utf8，不支持emoji表情。单击**参数设置**，修改完后单击提交参数使修改生效。

   - 将**character\_set\_server**参数的默认字符集修改为**utf8mb4**。
   - 将**character\_set\_filesystem**修改为**utf8**。![设置RDS编码类型](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7022018461/p422210.png)
6. 设置**数据安全性**，**添加白名单分组**后钉钉推送才可以访问该数据库。

   - 华北3（张家口）RDS添加 100.104.69.0/24 。
   - 华东1 （杭州）RDS添加 100.104.136.0/24。![添加白名单分组](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7022018461/p422211.png)
7. 单击**数据库连接**，然后单击**登录数据库**，在弹出的页面输入数据库账号和数据库密码。

   > **[!NOTE]**
   >
   > DMS登录报错时请参考[登录数据库失败文档](https://help.aliyun.com/document_detail/52244.html?spm=a2ccf.n-dtm-index.0.0.6a0adff7VptFvM)。
8. 在数据库管理页面，打开已创建的数据库**ding\_cloud\_push**，然后打开SQL操作界面，执行如下SQL创建数据表。

   - open\_sync\_biz\_data表用于接收高优先级事件的推送信息。
   - open\_sync\_biz\_data\_medium用于接收低优先级事件的推送信息。

     ```
     CREATE TABLE `open_sync_biz_data` (
       `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT 'ID',
       `gmt_create` datetime NOT NULL COMMENT '创建时间',
       `gmt_modified` datetime NOT NULL COMMENT '更新时间',
       `subscribe_id` varchar(64) NOT NULL COMMENT '订阅方ID',
       `corp_id` varchar(64) NOT NULL COMMENT '企业ID',
       `biz_id` varchar(128) NOT NULL COMMENT '业务ID',
       `biz_type` int(11) NOT NULL COMMENT '业务类型',
       `biz_data` text NOT NULL COMMENT '业务数据',
       `open_cursor` bigint(20) NOT NULL COMMENT '对账游标',
       `status` int(11) NOT NULL COMMENT '处理状态0为未处理。其他状态开发者自行定义',
       PRIMARY KEY (`id`),
       UNIQUE KEY `uk_subscribe_corp_biz` (`subscribe_id`,`corp_id`,`biz_id`,`biz_type`) USING BTREE
     ) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8mb4 COMMENT='高优先级数据';

     CREATE TABLE `open_sync_biz_data_medium` (
       `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT 'ID',
       `gmt_create` datetime NOT NULL COMMENT '创建时间',
       `gmt_modified` datetime NOT NULL COMMENT '更新时间',
       `subscribe_id` varchar(64) NOT NULL COMMENT '订阅方ID',
       `corp_id` varchar(64) NOT NULL COMMENT '企业ID',
       `biz_id` varchar(128) NOT NULL COMMENT '业务ID',
       `biz_type` int(11) NOT NULL COMMENT '业务类型',
       `biz_data` text NOT NULL COMMENT '业务数据',
       `open_cursor` bigint(20) NOT NULL COMMENT '对账游标',
       `status` int(11) NOT NULL COMMENT '处理状态0为未处理。其他状态开发者自行定义',
       PRIMARY KEY (`id`),
       UNIQUE KEY `uk_subscribe_corp_biz` (`subscribe_id`,`corp_id`,`biz_id`,`biz_type`) USING BTREE
     ) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8mb4 COMMENT='中低优先级数据';
     ```
