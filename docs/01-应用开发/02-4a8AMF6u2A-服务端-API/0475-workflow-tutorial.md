---
title: "审批实现及发送通知"
source_url: "https://open.dingtalk.com/document/development/workflow-tutorial"
namespace: "development"
slug: "workflow-tutorial"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "OA 审批 > 使用教程 > 自由OA 审批 > 审批实现及发送通知"
doc_id: "qUMnu25eGJ"
updated_at: "2026-07-10 10:11:12"
---

> Source: https://open.dingtalk.com/document/development/workflow-tutorial
> Path: 应用开发 / 服务端 API / OA 审批 > 使用教程 > 自由OA 审批 > 审批实现及发送通知
> Updated: 2026-07-10 10:11:12

# 审批实现及发送通知

本文介绍了以一个简单的出差审批为例如何发起一个审批的实现过程。

## 教程介绍

本教程以一个简单的出差审批为例展示如何发起一个审批。为了方便开发者体验，我们提供了服务端和前端代码，您只需要根据本文档的操作，完成基础配置既可。

![出差申请](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9976382061/p162030.png)

## 前提条件

在开始接入前，确保您已经完成以下准备工作：

- 安装小程序IDE，单击[小程序开发工具](../06-JDICnQyZLF-开发工具/0001-miniapp-tool.md)下载。
- 已安装并配置Java开发环境。
- 完成[应用创建与配置](../01-XOnnmGCTbn-开发指南/0007-create-application.md)的流程。

## **步骤一：配置应用**

1. 单击**应用能力** > **添加应用能力**，选择小程序完成添加操作。
2. 单击**开发配置** > **权限管理**。
3. 在搜索框输入`qyapi_aflow`和`qyapi_get_member`，并申请权限。
4. 进入应用详情页，单击**开发配置** > **安全设置**，进入安全设置页面。
5. 配置安全设置，并单击**保存**：

   | **配置项** | **说明** |
   | --- | --- |
   | 服务器出口IP | 调用钉钉服务端API时的合法IP列表，多个IP请以","隔开，支持带一个\*号通配符的IP格式。    本教程示例：  127.0.0.1 |
   | 重定向URL（回调域名） | 添加重定向URL作为免登授权码跳转地址,多个地址用”,“分隔。    本教程示例：  http://127.0.0.1 |
   | HTTP 可信域名 | 钉钉小程序应用需要事先设置一个通讯域名，应用可以跟指定的域名进行网络通信。    本教程示例：  127.0.0.1 |

## 步骤二：创建出差申请表单

参考以下操作，在OA管理后台创建审批模板：

1. 使用管理员账号登录[OA管理后台](https://oa.dingtalk.com/index.htm#/microApp/microAppList)，然后选择**工作台 > OA审批**。

   ![OA审批页面](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8145229951/p160985.png)
2. 在**表单管理**页面，单击**创建新表单**，然后选择**自定义流程表单**。

   ![自定义流程表单button](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8145229951/p160986.png)
3. 在**基础配置**页面，完成基础信息配置。并保存[processCode](0473-workflow-overview.md)。

   ![审批-基础配置](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8145229951/p160993.png)
4. 单击**表单设计**，然后在控件库中根据下表设计出差申请表单，

   > **[!NOTE]**
   >
   > 拖拽控件后，需要修改控件标题。

   | 表单项 | 使用控件 |
   | --- | --- |
   | 行程明细 | 明细/表格控件 |
   | 出差地点 | 单行输入框控件 |
   | 图片 | 图片控件 |
   | 开始时间，结束时间 | 日期区间控件 |
   | 出差人数 | 数字控件 |
   | 出差金额 | 金额控件 |
   | 出差同伴 | 单选框控件（添加的时候，把选项改为A,B,C） |
   | 交通工具 | 单行输入框控件 |
   | 出差事由 | 多行输入框控件 |
5. 单击**流程设计**，单击**+**设置审批条件和审批人，如下图所示。

   ![流程设计](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9145229951/p161042.png)
6. 单击**发布**完成表单设计。

## 步骤三：服务端开发

本示例提供了服务端代码，方便开发者快速接入。

参考以下操作，完成服务端开发：

1. 执行以下代码，下载服务端代码。

   ```
   git clone https://github.com/opendingtalk/eapp-corp-project.git
   ```
2. 修改`com.config.Constant.java`文件：

   | **配置项** | **说明** |
   | --- | --- |
   | CORP\_ID | 企业[CorpId](../01-XOnnmGCTbn-开发指南/0001-basic-concepts-beta.md#91c2ae57b23p9)。 |
   | APPKEY | 应用[Client ID](../01-XOnnmGCTbn-开发指南/0001-basic-concepts-beta.md#7d9825efaadw7)。 |
   | APPSECRET | 应用[Client Secret](../01-XOnnmGCTbn-开发指南/0001-basic-concepts-beta.md#7d9825efaadw7)。 |
   | PROCESS\_CODE | 审批表单[processCode](0473-workflow-overview.md#6fada3928c317)。 |
3. 在已下载的项目根目录，执行以下代码完成编译。

   ```
   mvn clean compile -U
   ```
4. 代码打包，生成可运行的jar文件。

   ```
   mvn clean package -Dmaven.test.skip=true
   ```
5. 执行以下命令，启动服务端。

   ```
   java -jar target/eapp-corp-project-1.0.0.jar
   ```
6. 服务端启动后，在浏览器中访问http://localhost:8080/welcome，打开如下页面表示启动成功。

   ![welcome](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9145229951/p161949.png)

## 步骤四：前端开发

本示例提供了前端代码，方便开发者快速接入。

参考以下操作，完成前端开发：

1. 执行以下命令，下载前端代码。

   ```
   git clone https://github.com/opendingtalk/eapp-corp-project-fe
   ```
2. 打开小程序IDE开发工具，打开已下载的项目。

   > **[!NOTE]**
   >
   > 项目类型选择钉钉**企业内部应用**。

   ![打开项目](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9145229951/p161951.png)
3. 关联步骤一中创建的小程序应用。

   ![小程序](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9145229951/p161952.png)
4. 打开`eapp-corp-project-fe/page/index/index.js`文件修改服务端URL，URL中的IP或者域名必须是开发者后台中设置的本应用的安全域名。小程序前端发起网络请求时是直连安全域名或IP的。

   本示例中设置为`http://127.0.0.1:8080`。

   ![本地iD](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9145229951/p162028.png)
5. 单击**发起审批**即可发起一个审批实例。

   为了保持代码的简洁，本次demo发起的审批实例中，审批发起人、审批人和抄送人是同一个用户，即当前免登的用户。
6. 打开钉钉打开移动端或PC端钉钉，找到该企业工作通知，查看收到的审批通知。

   ![工作通知](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2086382061/p162029.png)
