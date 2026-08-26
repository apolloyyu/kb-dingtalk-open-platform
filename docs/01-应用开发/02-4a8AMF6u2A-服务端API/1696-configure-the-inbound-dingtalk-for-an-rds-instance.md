---
title: "设置RDS实例接收钉钉推送"
source_url: "https://open.dingtalk.com/document/development/configure-the-inbound-dingtalk-for-an-rds-instance"
namespace: "development"
slug: "configure-the-inbound-dingtalk-for-an-rds-instance"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 钉钉云 > 钉钉云数据推送 > 设置RDS实例接收钉钉推送"
doc_id: "eheBmHW1j7"
updated_at: "2025-12-18 09:27:37"
---

> Source: https://open.dingtalk.com/document/development/configure-the-inbound-dingtalk-for-an-rds-instance
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 钉钉云 > 钉钉云数据推送 > 设置RDS实例接收钉钉推送
> Updated: 2025-12-18 09:27:37

# 设置RDS实例接收钉钉推送

本文档指导开发者如何配置自有或钉钉云RDS实例，用于接收钉钉云推送的数据。请根据实际使用场景选择对应的配置方式。

> **[!IMPORTANT]**
>
> - 开发调试阶段可使用自有MySQL数据库，但线上环境必须使用钉钉云RDS实例。
> - 钉钉云RDS实例不可被公网访问，以保障数据安全。
> - 自有MySQL数据库需满足以下条件：
>
>   - 支持公网访问。
>   - 从钉钉云批量插入50条数据总耗时 < 3秒，以确保推送成功率。
>   - 建议使用 MySQL 5.6 或 5.7 版本，不支持 MySQL 8.x 及以上版本。

## 设置自有的RDS用于接收钉钉推送

> **[!IMPORTANT]**
>
> 请务必使用 MySQL 5.6 或 5.7 版本，避免因版本兼容性导致连接失败或功能异常。

### **1.** （可选）卸载已有MySQL

若系统中已安装旧版MySQL，建议清理残留文件：

```
yum remove mysql mysql-server mysql-libs compat-mysql51
rm -rf /var/lib/mysql
rm /etc/my.cnf
rm -rf /var/log/mysqld.log
```

### 2. 安装并启动MySQL

```
# 安装MySQL服务
yum install mysql-server

# 启动MySQL实例
service mysqld start

# 查看默认密码（首次安装后）
cat /var/log/mysqld.log|grep 'password'
```

### 3. 修改默认密码

1. 使用获取的默认账号登录后执行以下命令修改密码（替换 `${ip}`、`${port}`、`${username}` 为实际值）：

   ```
   mysql -h ${ip} -P ${port} -u ${username} -p
   ```
2. 进入MySQL命令行后，执行命令更改root用户默认密码：

   ```
   -- 修改root用户密码（示例密码：1#QAZ2@wsx，请自行更换为强密码）
   set password = password('1#QAZ2@wsx');

   -- 设置密码永不过期
   alter user 'root'@'localhost' password expire never;

   -- 刷新权限
   flush privileges;
   ```

### 4. 设置字符集为 utf8mb4（支持Emoji）

#### 检查当前字符集设置：

使用命令查看mysql字符集设置。如果字符集不是utf8mb4请按照下面指引修改。支持emoji表情存储。

```
show variables like '%char%';
```

可以看到实例的字符集默认为latin1或者utf8。

> **[!NOTE]**
>
> 若输出中 `character_set_server`、`character_set_database` 等非 `utf8mb4`，需进行修改。

```
+--------------------------------------+----------------------------+
| Variable_name                        | Value                      |
+--------------------------------------+----------------------------+
| character_set_client                 | utf8                       |
| character_set_connection             | utf8                       |
| character_set_database               | latin1                     |
| character_set_filesystem             | binary                     |
| character_set_results                | utf8                       |
| character_set_server                 | latin1                     |
| character_set_system                 | utf8                       |
| character_sets_dir                   | /usr/share/mysql/charsets/ |
| validate_password_special_char_count | 1                          |
+--------------------------------------+----------------------------+
```

#### 修改配置文件 `/etc/my.cnf`

在对应段落添加如下配置：

> **[!IMPORTANT]**
>
> 若文件不存在，请创建；若已有内容，请勿重复添加。

```
[mysqld]
character-set-server=utf8mb4 

[client]
default-character-set=utf8mb4 

[mysql]
default-character-set=utf8mb4
```

#### 重启MySQL服务

更改配置之后重启mysql：

```
service mysqld restart
```

#### 验证字符集是否生效

再次查看实例字符集设置，已经改为了utf8mb4。

```
+--------------------------------------+----------------------------+
| Variable_name                        | Value                      |
+--------------------------------------+----------------------------+
| character_set_client                 | utf8mb4                    |
| character_set_connection             | utf8mb4                    |
| character_set_database               | utf8mb4                    |
| character_set_filesystem             | binary                     |
| character_set_results                | utf8mb4                    |
| character_set_server                 | utf8mb4                    |
| character_set_system                 | utf8                       |
| character_sets_dir                   | /usr/share/mysql/charsets/ |
| validate_password_special_char_count | 1                          |
+--------------------------------------+----------------------------+
```

### 5. 创建数据库与表结构

#### 创建数据库

```
CREATE DATABASE ding_cloud_push DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
```

#### 创建专用数据库用户

创建一个数据库用户，用于连接ding\_cloud\_push数据库。

> **[!NOTE]**
>
> **密码要求：** 必须包含大写字母、小写字母、数字和特殊符号，符合MySQL密码安全策略。

```
-- 替换 your_name 和 your_pass 为实际用户名和强密码
-- xx.xx.xxx.xx 为钉钉服务器访问该数据库的公网IP地址
CREATE USER 'your_name'@'xx.xx.xxx.xx' IDENTIFIED BY 'your_pass';

-- 授权该用户对ding_cloud_push数据库的增删改查权限，xx.xx.xxx.xx是钉钉连接开发者DB的外网IP。
GRANT SELECT, INSERT, UPDATE, DELETE ON `ding_cloud_push`.* TO 'your_name'@'xx.xx.xx.xx';

-- 使权限立即生效
FLUSH PRIVILEGES;
```

#### 创建数据表

在 `ding_cloud_push` 数据库中执行以下语句，创建两张表：

```
-- 高优先级事件推送表，用于接收高优先级事件的推送信息。
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
  `status` int(11) NOT NULL COMMENT '处理状态：0表示未处理，其他由开发者自定义',
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_subscribe_corp_biz` (`subscribe_id`,`corp_id`,`biz_id`,`biz_type`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8mb4 COMMENT='高优先级数据';

-- 中低优先级事件推送表，用于接收低优先级事件的推送信息。
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
  `status` int(11) NOT NULL COMMENT '处理状态：0表示未处理，其他由开发者自定义',
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_subscribe_corp_biz` (`subscribe_id`,`corp_id`,`biz_id`,`biz_type`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8mb4 COMMENT='中低优先级数据';
```

### 6. 在开发者后台绑定数据库

1. 登录[开发者后台](https://open-dev.dingtalk.com)，选择**钉钉云 > 云推送数据源 > 添加MySql实例**。

   ![添加mysql本地](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4295446061/p185360.png)
2. 输入您配置的数据库连接信息（IP、端口、用户名、密码）。
3. 保存并测试连接，确保网络可达且认证成功。

## 设置钉钉云RDS推送

参考以下步骤配置钉钉云RDS实例用于接收推送数据。

1. 登录[开发者后台](https://open-dev.dingtalk.com/#/dingCloudPortal)，然后单击**钉钉云 > 基础信息** > **登录控制台**。

   ![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4030487951/p141521.png)
2. 在**方案列表**页面，单击**资源**进入资源列表页。
3. 找到已创建的RDS实例，点击其ID链接进入详情页。

   ![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4030487951/p141525.png)
4. 在RDS实例详情页面，在左侧菜单选择**账号管理**，然后单击**重置账号密码**，设置新的数据库登录密码。

   ![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4030487951/p141531.png)
5. 单击**数据安全性** > **添加白名单分组**，将钉钉云ECS服务器的私网IP地址加入白名单，确保内网互通。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2538725671/p1033562.png)
6. 单击**参数设置**，将**character\_set\_server**参数默认字符集修改为**utf8mb4**，将**character\_set\_filesystem**参数的默认字符集修改为**utf8**，单击**提交参数**使修改生效。

   > **[!NOTE]**
   >
   > RDS默认字符集为 `utf8`，不支持完整Emoji存储，需调整为 `utf8mb4`。

   ![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4030487951/p141743.png)
7. 单击**数据库连接** > **登录数据库**，在弹出页面输入数据库账号和密码（可在【账号管理】中查看）。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2538725671/p1033563.png)
8. 在数据库管理页面，打开**ding\_cloud\_push**数据库的SQL操作界面，执行以下SQL语句：

   ```
   sql
   -- 高优先级事件表，用于接收高优先级事件的推送信息。
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
     `status` int(11) NOT NULL COMMENT '处理状态：0表示未处理，其他由开发者自定义',
     PRIMARY KEY (`id`),
     UNIQUE KEY `uk_subscribe_corp_biz` (`subscribe_id`,`corp_id`,`biz_id`,`biz_type`) USING BTREE
   ) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8mb4 COMMENT='高优先级数据';

   -- 中低优先级事件表，用于接收低优先级事件的推送信息。
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
     `status` int(11) NOT NULL COMMENT '处理状态：0表示未处理，其他由开发者自定义',
     PRIMARY KEY (`id`),
     UNIQUE KEY `uk_subscribe_corp_biz` (`subscribe_id`,`corp_id`,`biz_id`,`biz_type`) USING BTREE
   ) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8mb4 COMMENT='中低优先级数据';
   ```
9. 创建名称为**isv\_dingtalk\_biz**的数据库。

   ```
   -- 创建业务数据库
   CREATE DATABASE isv_dingtalk_biz DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;

   -- 使用该数据库
   USE isv_dingtalk_biz;
   ```
10. 执行以下SQL创建两张数据表，用来存储业务数据。

    ```
    -- 创建同步锁表
    CREATE TABLE `biz_lock` (
      `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT COMMENT '主键',
      `gmt_create` datetime NOT NULL COMMENT '创建时间',
      `gmt_modified` datetime NOT NULL COMMENT '修改时间',
      `lock_key` varchar(128) NOT NULL COMMENT '锁Key',
      `expire` bigint(20) unsigned NOT NULL COMMENT '锁过期时间戳',
      PRIMARY KEY (`id`),
      UNIQUE KEY `uk_lock` (`lock_key`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='同步业务锁';

    --创建授权企业信息表
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

## **绑定数据库**

1. 登录[开发者后台](https://open-dev.dingtalk.com/)，选择**钉钉云>云推送数据源**，找到数据库，然后单击**设置**。

   ![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4475299951/p143370.png)
2. 在弹出的对话框，输入已创建RDS数据库的账号和密码，然后单击**确定**，完成绑定。

   ![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5030487951/p141761.png)
