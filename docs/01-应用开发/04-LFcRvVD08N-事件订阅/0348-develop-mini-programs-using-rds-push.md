---
title: "开发小程序（RDS推送）"
source_url: "https://open.dingtalk.com/document/development/develop-mini-programs-using-rds-push"
namespace: "development"
slug: "develop-mini-programs-using-rds-push"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "历史文档（不推荐） > RDS推送/SyncHTTP推送 > 开发小程序（RDS推送）"
doc_id: "2Cr3DCDG4q"
updated_at: "2025-10-16 15:06:26"
---

> Source: https://open.dingtalk.com/document/development/develop-mini-programs-using-rds-push
> Path: 应用开发 / 事件订阅 / 历史文档（不推荐） > RDS推送/SyncHTTP推送 > 开发小程序（RDS推送）
> Updated: 2025-10-16 15:06:26

# 开发小程序（RDS推送）

通过本教程你将学会使用RDS推送方式开发一个第三方小程序。

## 教程介绍

本教程以给登录用户发送一条消息的小程序为例演示小程序开发的完整流程。通过本教程您将学习到：

- 上架市场应用开发、发布的完整流程。
- 聚石塔应用部署。
- 应用开通授权。

![发送消息demo](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6038884061/p169831.png)

## 准备工作

- 注册了钉钉管理员账号。若未注册，单击[这里](https://oa.dingtalk.com/register_new.htm?source=1008_OA&lwfrom=2018122711522903000&succJump=oa#/)完成注册。
- 绑定聚石塔账号，详情请参考[入驻聚石塔](https://open.dingtalk.com/document/isvapp/create-tmallcloud-account)。
- 安装小程序开发者工具IDE，单击[这里](https://open.dingtalk.com/document/resourcedownload/miniapp-tool#topic-2625633)下载安装。
- 本教程中的示例Demo使用Java开发，确保您已经安装了Java开发环境（安装JDK）以及Java项目构建工具Maven。

## 步骤一：创建应用

参考以下操作，创建应用：

1. 登录[开发者后台](https://open-dev.dingtalk.com/)。
2. 单击**应用开发**，选择**第三方企业应用**，单击**创建应用**。

   ![p141770](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9353360261/p256635.png)
3. 在弹出的页面，应用类型选择**小程序**，并填写基本信息，然后单击**确定创建**。

   ![create](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3401117161/p259097.png)

## 步骤二：创建RDS实例并配置数据源

参考以下操作，在聚石塔环境中购买并配置用来存储钉钉推送数据的RDS实例。

1. 使用钉钉账号登录[聚石塔](https://console.cloud.tmall.com/home#/)。
2. 创建部署钉钉应用的专有网络VPC。

   1. 打开创建VPC链接：<https://console.cloud.tmall.com/home#/vpc>
   2. 根据以下信息配置VPC，然后单击**确定**。

      | 配置 | 说明 |
      | --- | --- |
      | **业务域** | 必须选择**钉钉业务**。 |
      | **地域** | 必须选择**cn-zhangjiakou 华北3**。 |
      | **名称** | VPC的名称。长度为2-128个字符，以大小字母或中文开头，可包含数字、下划线（\_）和连字符（-）。  建议使用：钉钉业务VPC |
      | **单选** | 选择**推荐网段**配置模式。 |
      | **IPv4网段** | 选择使用的IPv4网段。  推荐使用10.0.0.0/8，该网段的私网IP地址数量最多。 |
      | **描述** | 输入VPC的描述信息。  描述可以为空，或输入2-256个中英文字符，不能以http://和https://开头。 |

      ![创建VPC](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1038823061/p175500.png)
3. 在[RDS控制台](https://console.cloud.tmall.com/resourceView#/aliyun/product?productCode=rds)，选择**华北3（张家口）**地域，然后单击**创建实例**。

   ![创建实例](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5839633061/p175852.png)
4. 完成RDS购买。

   > **[!IMPORTANT]**
   >
   > - RDS的版本必须是**5.7**或**5.6**。
   > - 确保RDS的专有网络是上一步创建的钉钉业务VPC。

   ![购买RDS](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5839633061/p175855.png)
5. 在[RDS实例列表](https://console.cloud.tmall.com/resourceView#/aliyun/product?productCode=rds)页面，单击已创建的RDS实例ID链接进入RDS实例详情页面。

   数据库创建大概需要5分钟左右的时间，默认会在RDS实例中创建一个普通账号。

   ![单击链接](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5839633061/p175857.png)
6. 单击**数据库管理**，然后单击**创建数据库**，创建用于接收钉钉推送的数据库。

   在配置数据库时，授权默认账号的读写权限。也可以选择后续添加数据库账号。

   ![创建数据库](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5839633061/p175862.png)
7. RDS默认字符集是utf8，不支持emoji表情。单击**参数设置**，将**character\_set\_server**参数的默认字符集修改为**utf8mb4**，将**character\_set\_filesystem**参数的默认字符集修改为**utf8**。修改后，单击**提交参数**使修改生效。

   ![设置字符集](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2752963061/p175870.png)
8. 首次登录RDS，需要先设置初始登录密码。在RDS实例详情页面，单击**账号管理**，然后单击**重置账号密码**。

   ![重置密码](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5839633061/p175859.png)
9. 单击**数据安全性**，然后单击**添加白名单分组**设置可以访问该数据库的IP地址。

   设置完IP白名单之后才可以使用DMS连接数据库。

   ![rds白名单](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5839633061/p175863.png)
10. 单击**数据库连接**，然后单击**登录数据库**。然后在弹出的页面输入数据库账号和数据库密码。

    您可以在**账号管理**页面查看数据库账号。
11. 在数据库管理页面，打开已创建的数据库**ding\_cloud\_push**，然后打开SQL操作界面，执行如下SQL创建数据表。

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
12. 创建一个名称为**isv\_dingtalk\_biz**的数据库并执行以下SQL创建两张数据表，用来存储业务数据。

    ```
    CREATE TABLE `biz_lock` (
      `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT COMMENT '主键',
      `gmt_create` datetime NOT NULL COMMENT '创建时间',
      `gmt_modified` datetime NOT NULL COMMENT '修改时间',
      `lock_key` varchar(128) NOT NULL COMMENT '锁Key',
      `expire` bigint(20) unsigned NOT NULL COMMENT '锁过期时间戳',
      PRIMARY KEY (`id`),
      UNIQUE KEY `uk_lock` (`lock_key`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='同步业务锁';
    CREATE TABLE `authed_corp` (
      `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT 'ID',
      `gmt_create` datetime NOT NULL COMMENT '创建时间',
      `gmt_modified` datetime NOT NULL COMMENT '更新时间',
      `corp_name` varchar(128) NOT NULL COMMENT '企业名称',
      `corp_id` varchar(64) NOT NULL COMMENT '企业ID',
      `access_token` varchar(128) NOT NULL COMMENT '企业访问AccessToken',
      `access_token_expire` bigint(20) NOT NULL COMMENT '企业访问AccessToken过期时间毫秒',
      `permanent_code` varchar(128) NOT NULL COMMENT '企业访问开通应用的永久授权码',
      `suite_key` varchar(128) NOT NULL COMMENT '企业开通的应用/套件',
      `agent_id` bigint(20) unsigned DEFAULT NULL COMMENT '企业开通应用实例id',
      PRIMARY KEY (`id`),
      UNIQUE KEY `uk_corp_suite` (`corp_id`,`suite_key`) USING BTREE
    ) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COMMENT='授权开通应用套件的企业';
    ```
13. 登录[开发者后台](https://open-dev.dingtalk.com/#/tmallCloudPortal/tmalldataPush)，选择**聚石塔 > 云推送数据源**。
14. 找到已创建的RDS实例，然后单击**设置**。

    ![设置RDS密码](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2752963061/p175868.png)
15. 输入MySQL实例的账号和密码，然后单击**确定**完成添加。

## 步骤三：应用开发与部署

为方便开发者快速体验钉钉小程序的开发流程，我们提供了小程序的服务端和前端代码示例。

参考以下操作开发钉钉小程序：

1. 参考以下操作完成服务端配置：

   1. 执行以下代码，下载服务端代码。

      ```
      git clone https://github.com/opendingtalk/eapp-isv-project.git
      ```
   2. 在已下载的项目中打开`eapp-isv-project/src/main/resources/application.properties`文件，配置以下信息：

      1. 配置数据库地址和账号密码，使用步骤二中创建的数据库存储钉钉推送的数据。
      2. 配置应用的suiteID、suiteKey和suiteSecret。在开发者后台的应用详情页可以获取这些信息。
      3. 配置corpid。在开发者后台首页获取。![数据库配置](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3056884061/p178979.png)
   3. 在已下载的服务端代码项目的根目录执行以下命令，完成服务端打包。生成的jar包（`eapp-isv-project-1.0.0.jar`）存储在已下载项目的target文件中。

      ```
      mvn clean package -Dmaven.test.skip=true
      ```
2. 购买ECS。

   1. 在[ECS实例列表](https://console.cloud.tmall.com/resourceView#/aliyun/product?productCode=ecs)页面，单击**创建实例**。

      ![创建ECS实例](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2038823061/p175503.png)
   2. 根据需要配置ECS，请注意以下配置项。

      | 配置 | 说明 |
      | --- | --- |
      | **地域及可用区** | 必须选择**华北3（张家口）**。 |
      | **实例规格** | 建议使用4 CPU及以上规格的实例。 |
      | **网络** | 必须选择上一步中创建的钉钉业务域的VPC。 |
      | **安全组** | 使用钉钉业务默认安全。 |
3. 创建并配置NAT网关。

   1. 在[NAT网关列表](https://console.cloud.tmall.com/resourceView#/aliyun/product?productCode=nat)页面，地域选择**华北3（张家口）**，然后单击**创建NAT网关**。
   2. 设置SNAT规则，配置一个固定出口公网IP。

      ![snat规则](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3056884061/p180058.png)
4. 创建容器集群。

   1. 在[容器集群列表](https://console.cloud.tmall.com/component/operationcenter#/index)页面，单击**新建集群**。

      ![集群列表](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2038823061/p175513.png)
   2. 根据实际情况，配置集群。

      > **[!IMPORTANT]**
      >
      > VPC必须选择第一步中创建的钉钉业务域VPC。

      ![创建集群](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2038823061/p175514.png)
5. 添加ECS到创建的集群中。

   1. 在[容器集群列表](https://console.cloud.tmall.com/component/operationcenter#/index)页面，单击已创建的集群对应的**管理**按钮。

      ![管理](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2038823061/p175515.png)
   2. 单击**节点列表**，然后选择**添加已有节点**。

      ![添加节点](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2038823061/p175516.png)
   3. 选择已购买的ECS，并设置登录方式和系统镜像类型。

      ![添加节点](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2038823061/p175517.png)
6. 创建用来发布后端服务的应用。

   1. 在[发布管理](https://console.cloud.tmall.com/appconsole?appId=22696#/releaseMgmt)页面，单击**新建发布单**。

      ![新建发布单](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1597433061/p175577.png)
   2. 填写发布单名称，上传步骤一中生成的后端jar文件。

      ![发布单](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4056884061/p175580.png)
   3. 单击**确认发布**开始发布。

      ![确认发布](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1597433061/p175587.png)
   4. 在**发布管理**页面，单击**详情**查看发布日志。

      ![发布详情](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1597433061/p175589.png)
   5. 应用部署完成后，可以启动应用。

      ![发布完成](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2597433061/p175593.png)
7. 配置负载均衡服务SLB作为应用访问入口。

   1. 在[负载均衡实例](https://console.cloud.tmall.com/resourceView#/aliyun/product?productCode=slb)页面，单击**创建负载均衡**。

      ![创建slb](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2597433061/p175605.png)
   2. 选择SLB的地址和规格等配置，然后单击**立即购买**。确保SLB的地域为**张家口**，网络类型为**公网**。

      ![slb购买](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4903928161/p175607.png)
   3. 在[流量接入](https://console.cloud.tmall.com/appconsole?appId=22696#/networkTraffic)页面，单击**新建SLB接入**。

      ![新建SLB](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4903928161/p175597.png)
   4. 配置SLB。

      > **[!IMPORTANT]**
      >
      > - **网络类型**：选择外网访问。
      > - **RS端口**：输入容器服务端口。

      ![配置slb监听](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2597433061/p175601.png)
   5. 创建成功后，使用SLB的公网IP访问：http://slb公网ip/welcome，出现如下页面表示服务发布成功。

      ![发布服务](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5056884061/p179014.png)

## 步骤四：发布小程序

1. 登录[开发者后台](https://open-dev.dingtalk.com/#/dingCloudPortal)，选择**应用开发 > 第三方企业应用 > 小程序**。
2. 单击已创建的小程序，然后单击**开发管理**，完成以下基础配置。

   1. **服务器出口IP**：部署后端服务的公网IP地址。多个IP请以英文逗号隔开。

      本教程中输入聚石塔中配置的SNAT规则中使用的弹性公网IP。
   2. **推送类型**：选择**钉钉云推送**。
   3. **推送数据源**：选择步骤二中设置的RDS实例。
   4. **回调事件**：全部选择。如果想要接收的回调事件无法选择，请单击**权限管理**添加对应的接口权限。

      ![p179113](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7899787161/p256156.png)
3. 单击**安全中心**，然后单击**添加**添加一个HTTP安全域名。小程序前端只能通过配置的安全域名（或IP）与服务端进行网络通信。当安全域名更新时，需要在IDE重新打包上传版本，设置的域名才会生效。

   本教程输入作为流量接入的SLB的公网IP。

   ![p179116](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4401117161/p256216.png)
4. 单击**版本管理与发布**，然后单击**设置体验组织**。添加组织后，再单击**开通应用**。

   ![p179285](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7899787161/p256305.png)

   为方便开发者快速体验钉钉小程序的开发流程，我们提供了小程序的服务端和前端代码示例。执行以下命令，下载前端小程序项目文件。

   ```
   git clone https://github.com/opendingtalk/eapp-isv-project-fe.git
   ```
5. 在小程序IDE中打开已下载的小程序项目，项目类型选择钉钉**第三方企业应用**。

   ![开发本地项目](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5056884061/p179032.png)
6. 使用钉钉账号登录IDE，选择已设置的体验组织，然后打开`index.js`文件修后端服务URL。

   本教程中设置为SLB的公网IP。

   ![小程序ide](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5056884061/p180060.png)
7. 在调试器页面，单击**自动免登并获取用户信息**。

   ![自动免登](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5056884061/p180061.png)
8. 成功获取到用户信息后，单击测试发消息，查看是否接收到了推送消息。至此，已完成全部小程序的体验内容。

   ![小程序](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5056884061/p180063.png)
9. 在IDE中，单击**上传**上传开发版本至开发者后台。

   ![上传](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8038884061/p180067.png)
10. 登录开发者后台，在小程序详情页面，单击版本**管理与发布**，然后单击**灰度**添加使用该小程序的企业的corpid。

    ![p180068](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4401117161/p256315.png)
11. 灰度版本测试稳定后，单击**发布**。

    线上版本仅供20家企业安装并使用，用于开发过程中测试与共创。

    至此，您已完成第三方小程序开发的全部流程。
