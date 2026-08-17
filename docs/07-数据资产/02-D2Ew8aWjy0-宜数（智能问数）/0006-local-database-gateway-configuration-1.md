---
title: "本地数据库网关配置"
source_url: "https://open.dingtalk.com/document/aipass/local-database-gateway-configuration-1"
namespace: "aipass"
slug: "local-database-gateway-configuration-1"
group: "数据资产"
tab: "宜数（智能问数）"
breadcrumb: "问数助理 > 本地数据库网关配置"
doc_id: "6pk5vLicID"
updated_at: "2026-08-13 09:05:21"
---

> Source: https://open.dingtalk.com/document/aipass/local-database-gateway-configuration-1
> Path: 数据资产 / 宜数（智能问数） / 问数助理 > 本地数据库网关配置
> Updated: 2026-08-13 09:05:21

# 本地数据库网关配置

## **本地网关介绍**

**智能问数本地网关**是基于钉钉开放平台 Stream 能力构建的数据连接器，方便用户快速将本地环境的数据库连接到智能问数上，免去了繁琐的公网IP、白名单等步骤。它的原理是，在用户本地部署客户端代理（agent），以提供反向代理服务，通过钉钉开发平台 Stream 网关连接到智能问数。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8831450471/p920883.png)

Stream模式的智能问数本地网关有以下优点：

- **零公网IP**：不需要依赖公网IP或域名，也不需要暴露公网IP，减少了公网暴露服务的安全风险并降低了开发门槛。
- **零加解密/签名/TLS证书管理**：使用应用身份对连接进行鉴权，通过反向连接的方式与钉钉开放平台建立TLS加密连接，提供了快速、安全的通信体验。
- **零防火墙白名单**：Stream 模式下开发者无需向公网开放提供任何服务端口，无需部署防火墙和配置白名单。
- **轻量级网关部署**：通过反向连接的方式建立通道，开发者只需保证运行环境具备公网访问能力即可，无需部署网关。

## **本地网关客户端安装**

### **下载本地网关**

| **版本** | **客户端** | **下载地址** |
| --- | --- | --- |
| **V0.0.2** | mac | [dpaas-agent-mac.zip](https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20250303/rrquqb/dpaas-agent-mac.zip) |
| win 64 | [dpaas-agent-win.zip](https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20250327/orvwle/dpaas-agent-win.zip) |
| linux 64 | [dpaas-agent-linux .zip](https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20250303/gsczmu/dpaas-agent-linux+.zip) |
| **V0.0.1** | mac | [dpaas-agent-mac.zip](https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20250226/tfeuhe/dpaas-agent-mac.zip) |
| win 64 | [dpaas-agent-win.zip](https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20250226/vmwowx/dpaas-agent-win.zip) |
| linux 64 | [dpaas-agent-linux.zip](https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20250226/fyyrxv/dpaas-agent-linux.zip) |

### **配置本地网关**

1. 配置应用信息，获取应用凭证信息：

   1. 创建企业应用信息，详情参考[应用创建与配置](../../01-应用开发/01-XOnnmGCTbn-开发指南/0007-create-application.md)。
   2. 创建完成后，获取应用凭证信息，单击**基础信息** > **凭证与基础信息**，即可查看。

      | **凭证信息** | **说明** |
      | --- | --- |
      | APP ID | 统一应用唯一标识（UnifiedAppId）。 |
      | Client ID | 客户端 ID。 |
      | Client Secret | 客户端密码。 |

      ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1213856871/p920988.png)
   3. 解压下载的本地网关软件，打开配置文件（config.json），填写 client 信息，配置文件中 client 部分用于身份验证和与钉钉开放平台的通信。

      > 对应上述凭证信息中的 Client ID 和 Client Secret。
2. 配置数据库信息，配置文件中 db\_config 部分是用来定义数据库连接的，它可以包含多个数据库配置（列表格式）。每个数据库配置包括以下字段：

   | **配置项** | **说明** |
   | --- | --- |
   | host | 数据库服务器的主机名或IP地址。 |
   | port | 数据库服务器的端口号。 |
   | username | 用于连接数据库的用户名称。 |
   | password | 用于连接数据库的密码。 |
   | database | 要连接的数据库名。 |
   | config\_key | 此数据库配置的引用键名，用于在后续配置中引用对应的数据库，保持唯一即可。 |

   示例配置如下：

   > **[!NOTE]**
   >
   > - 当前每个网关仅支持配置一个数据库，暂不支持在配置文件中配置多个数据库。
   > - 每个网关对应一个开放平台上创建的钉钉应用，不同网关需要创建不同的钉钉应用。
   > - 同一个网关支持负载均衡，部署在多个节点，但是底层数据库需同时支持集群式访问，这种情况下，查询请求会随机打到某个网关节点。

   | **数据库** | **样例** |
   | --- | --- |
   | MySQL | ``` client:   client_id: dingexxxx       client_secret: xxxx #mysql db_config:  - host: localhost    addr: localhost:3306    username: 填写用户名    password: 填写密码    database: 填写数据库名称    config_key: my_mysql ``` |
   | PostgreSQL | ``` client:   client_id: dingexxxx   client_secret: xxxx  db_config:  - host: localhost    addr: localhost:5432    username: 填写用户名    password: 填写密码    database: 填写数据库名称    config_key: my_postgresql ``` |
   | SQLserver | ``` client:   client_id: dingexxxx   client_secret: xxxx  db_config:  - host: localhost    addr: localhost:1433    username: 填写用户名    password: 填写密码    database: 填写数据库名称    config_key: my_sqlserver ``` |
   | Oracle | ``` client:   client_id: dingexxxx   client_secret: xxxx  db_config:  - host: localhost    port: 1521    addr: localhost:1521    username: 填写用户名    password: 填写密码    database: 填写数据库名称(Oracle的PDB名称/Service Name)    config_key: my_oracle ``` |

### **启动客户端**

运行网关，根据不同的使用场景，运行本地网关dpaas-agent，如下：

| **配置项** | **说明** |
| --- | --- |
| Windows 系统 | - 方式一：双击 dpaas-agent 应用程序的图标，这将以普通模式启动程序。 - 方式二：通过命令行以后台模式运行，打开命令提示符或 PowerShell，然后输入以下命令以使 dpaas-agent 在后台运行（假设 dpaas-agent 位于 `C:\path\to\dpaas-agent` ），启动命令如下：     ```   start /b C:\path\to\dpaas-agent\dpaas-agent.exe   ``` |
| macOS 系统 和 Linux 系统 | 打开终端，切换到包含 dpaas-agent 的目录，然后执行以下命令直接运行，命令如下：   ``` ./dpaas-agent ```   如果要在后台持续运行`dpaas-agent`，同时屏蔽输出，可以使用`nohup`命令。在终端中执行以下命令`nohup ./dpaas-agent >/dev/null 2>&1 &`。这将启动`dpaas-agent`，所有的输出信息会被重定向到`/dev/null`，即不会显示任何输出信息。`&`符号表示`dpaas-agent`将在后台运行。  **[!NOTE]**  确保`dpaas-agent`有执行权限。在Linux和macOS上，你可能需要通过`chmod +x dpaas-agent`命令来给予执行权限。 |

## **智能问数配置**

1. 进入智能问数配置页面，单击**添加**并选择本地数据库。
2. 选择本地网关配置的数据库。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8831450471/p920902.png)
3. 配置数据库信息：

   | **配置项** | **说明** |
   | --- | --- |
   | 数据源名称 | 任意填写，同一个助理内保持唯一即可。 |
   | 数据源描述 | 任意填写，一般用于描述数据库的用途。 |
   | 数据库名称 | 本地网关底层配置的数据库名称（同JDBC URL里面配置的数据库名称）。 |
   | 数据库 ID | 本地网关数据库配置的引用键名（config.json）。 |
   | 应用 App ID（UnifiedAppId） | 上文中获取到的统一应用唯一标识。  image |

   配置完成后，你就可以单击测试连通性。连接成功后，你就可以单击**下一步**。
4. 在数据表配置页面，单击**新建数据表，**选择对应数据表**，**完成字段配置说明。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1213856871/p920906.png)
5. 选择本地网关配置的数据库。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8831450471/p920902.png)
6. 配置数据库信息：

   | **配置项** | **说明** |
   | --- | --- |
   | 数据源名称 | 任意填写，同一个助理内保持唯一即可。 |
   | 数据源描述 | 任意填写，一般用于描述数据库的用途。 |
   | 数据库名称 | 本地网关底层配置的数据库名称（同JDBC URL里面配置的数据库名称）。 |
   | 数据库 ID | 本地网关数据库配置的引用键名（config.json）。 |
   | 应用 App ID（UnifiedAppId） | 上文中获取到的统一应用唯一标识。  image |

   配置完成后，你就可以单击测试连通性。连接成功后，你就可以单击**下一步**。
7. 在数据表配置页面，单击**新建数据表，**选择对应数据表**，**完成字段配置说明。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1213856871/p920906.png)
