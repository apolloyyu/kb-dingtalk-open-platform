---
title: "使用聚石塔RDS数据库"
source_url: "https://open.dingtalk.com/document/development/use-tmallcloud-rds"
namespace: "development"
slug: "use-tmallcloud-rds"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "历史文档（不推荐） > RDS推送/SyncHTTP推送 > 聚石塔 > 使用聚石塔RDS数据库"
doc_id: "doc_7335798e2fc64f30"
updated_at: "2026-09-02 18:14:25"
---

> Source: https://open.dingtalk.com/document/development/use-tmallcloud-rds
> Path: 应用开发 / 事件订阅 / 历史文档（不推荐） > RDS推送/SyncHTTP推送 > 聚石塔 > 使用聚石塔RDS数据库
> Updated: 2026-09-02 18:14:25

# 使用聚石塔RDS数据库

首先，需要在聚石塔中创建一个RDS实例用来存储钉钉推送的数据，然后再将RDS实例添加为数据源既可。

## 准备工作

已完成聚石塔入驻，详情请参考[入驻聚石塔](0334-create-tmallcloud-account.md)。

## 步骤一：创建RDS实例

如果您已经在聚石塔中购买了RDS实例，请忽略本操作。

1. 登录[开发者后台](https://open-dev.dingtalk.com/#/tmallCloudPortal/tmalldataPush)，选择**聚石塔 > 云推送数据源**，然后单击**添加MySql实例**。

   或使用钉钉账号登录[聚石塔](https://console.cloud.tmall.com/home#/)。
2. 在[RDS控制台](https://console.cloud.tmall.com/resourceView#/aliyun/product?productCode=rds)，选择**华北3（张家口）**地域，然后单击**创建实例**。

   ![创建实例](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5839633061/p175852.png)
3. 完成RDS购买。

   > **[!IMPORTANT]**
   >
   > - RDS的版本必须是**5.7**或**5.6**。
   > - 确保RDS的专有网络和应用部署的ECS属于同一个钉钉业务VPC。

   ![购买RDS](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5839633061/p175855.png)
4. 在[RDS实例列表](https://console.cloud.tmall.com/resourceView#/aliyun/product?productCode=rds)页面，单击已创建的RDS实例ID链接进入RDS实例详情页面。

   数据库创建大概需要5分钟左右的时间，默认会在RDS实例中创建一个普通账号。

   ![单击链接](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5839633061/p175857.png)
5. 单击**数据库管理**，然后单击**创建数据库**，创建用于接收钉钉推送的数据库。

   在配置数据库时，授权默认账号的读写权限。也可以选择后续添加数据库账号。

   ![创建数据库](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5839633061/p175862.png)
6. RDS默认字符集是utf8，不支持emoji表情。单击**参数设置**，将**character\_set\_server**参数的默认字符集修改为**utf8mb4**，将**character\_set\_filesystem**参数的默认字符集修改为**utf8**。修改后，单击**提交参数**使修改生效。

   ![设置字符集](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2752963061/p175870.png)
7. 首次登录RDS，需要先设置初始登录密码。在RDS实例详情页面，单击**账号管理**，然后单击**重置账号密码**。

   ![重置密码](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5839633061/p175859.png)
8. 单击**数据安全性**，然后单击**添加白名单分组**设置可以访问该数据库的IP地址。

   设置完IP白名单之后才可以使用DMS连接数据库。

   ![rds白名单](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5839633061/p175863.png)
9. 单击**数据库连接**，然后单击**登录数据库**。然后在弹出的页面输入数据库账号和数据库密码。

   您可以在**账号管理**页面查看数据库账号。
10. 在数据库管理页面，打开已创建的数据库**ding\_cloud\_push**，然后打开SQL操作界面，执行如下SQL创建数据表。

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

    ![执行SQL ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5839633061/p175867.png)

## 步骤二：设置数据推送源

1. 登录[开发者后台](https://open-dev.dingtalk.com/#/tmallCloudPortal/tmalldataPush)，选择**聚石塔 > 云推送数据源**。
2. 找到已创建的RDS实例，然后单击**设置**。

   ![设置RDS密码](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2752963061/p175868.png)
3. 输入MySQL实例的账号和密码，然后单击**确定**完成添加。
