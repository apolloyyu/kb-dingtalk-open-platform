---
title: "钉钉云迁移聚石塔"
source_url: "https://open.dingtalk.com/document/development/migrate-data-from-dingtalk-to-alibaba-cloud-1"
namespace: "development"
slug: "migrate-data-from-dingtalk-to-alibaba-cloud-1"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 钉钉云 > 迁移方案 > 钉钉云迁移聚石塔"
doc_id: "2BKkGEME0c"
updated_at: "2025-10-16 14:31:31"
---

> Source: https://open.dingtalk.com/document/development/migrate-data-from-dingtalk-to-alibaba-cloud-1
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 钉钉云 > 迁移方案 > 钉钉云迁移聚石塔
> Updated: 2025-10-16 14:31:31

# 钉钉云迁移聚石塔

如果部署在钉钉云的应用的数据迁移涉及到除ECS, MongoDB, RDS, OSS以外的云产品，请在迁移前，扫描文档底部提供的钉钉群二维码，进行咨询。

## 迁移流程

整体迁移流程如下图所示：

![迁移流程](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9458533061/p175663.png)

## 步骤一：绑定聚石塔账号

首先，需要将钉钉账号绑定到聚石塔。

1. 申请聚石塔账号，详情请参考[入驻聚石塔](https://open.dingtalk.com/document/isvapp/create-tmallcloud-account)。
2. 添加迁移白名单。

   请扫描文档底部提供的钉钉群二维码，提供企业的corpid和要迁移的云产品列表，由钉钉小二添加白名单。
3. 开发者后台绑定聚石塔账号，详情请参考[入驻聚石塔](https://open.dingtalk.com/document/isvapp/create-tmallcloud-account)。

## 步骤二：准备迁移环境

1. 在[聚石塔VPC创建](https://console.cloud.tmall.com/home#/vpc)页面，创建钉钉业务VPC。

   > **[!IMPORTANT]**
   >
   > - 业务域必须选择**钉钉业务**。
   > - 地域必须选**cn-zhangjiakou 华北 3**。
   > - 名称建议是钉钉业务VPC。
   > - 推荐网段选10.0.0.0/8。
2. 购买NAT网关，然后为已创建的VPC配置SNAT规则，绑定一个固定出口IP。

   1. 在[NAT网关列表](https://console.cloud.tmall.com/resourceView#/aliyun/product?productCode=nat)页面，单击**创建NAT网关**。
   2. 选择NAT网关配置，并完成购买。

      > **[!IMPORTANT]**
      >
      > - 确保地域是华北3，VPC是上一步中创建的钉钉业务VPC。
      > - 如果您第一次创建增强型NAT网关，请先使用主账号进行授权: [授权入口](https://ram4service.console.aliyun.com/?spm=5176.14666475.commonbuy2container.4.6780778brQEv7H#/role/authorize?request=%7B%22Requests%22:%20%7B%22request1%22:%20%7B%22RoleName%22:%20%22AliyunNATAccessingNetworkInterfaceRole%22,%20%22TemplateId%22:%20%22ENIRole%22%7D%7D,%20%22ReturnUrl%22:%20%22https:%2F%2Fvpcnext4service.console.aliyun.com%2Fnat%22,%20%22Service%22:%20%22NAT%22%7D)。

      ![购买nat](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0988393061/p177431.png)
   3. 创建NAT网关后，单击**绑定弹性公网IP**，绑定一个公网IP。

      ![绑定eip](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1988393061/p177433.png)
   4. 在[NAT网关详情](https://console.cloud.tmall.com/resourceView#/aliyun/product?productCode=nat)页面，单击**SNAT列表**，然后单击**创建SNAT条目**配置SNAT规则。

      ![snat规则](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1988393061/p177439.png)
3. 钉钉业务VPC创建完成后，联系钉钉小二进行钉钉云上的安全组迁移。

   请扫描文档底部提供的钉钉群二维码进群联系钉钉小二。
4. 在[聚石塔资源](https://console.cloud.tmall.com/home#/)页面，购买与钉钉云上相同配置的云产品，例如ECS、RDS、SLB等。

   > **[!IMPORTANT]**
   >
   > - 确保所有购买的云产品都创建在步骤一中的钉钉业务VPC中。
   > - 如果需要MongoDB，确保实例是单节点实例或副本集并开启公网地址。
   > - RDS版本必须是5.6或5.7。

## 步骤三：云产品迁移

1. 迁移RDS。

   1. 在购买的RDS中创建要迁移的数据库，并且设置用户名密码。

      ![RDS](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5477533061/p175698.png)
   2. 在[聚石塔DTS控制台](https://console.cloud.tmall.com/resourceView#/aliyun/product?productCode=dts)创建数据同步任务，把RDS数据库同步到聚石塔。

      ![迁移任务](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6044044061/p175702.png)![迁移](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6044044061/p175701.png)
   3. 开启DTS同步任务。

      ![启动任务](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5477533061/p175713.png)
2. 迁移MongoDB，可参考[跨账号迁移MongoDB实例](https://help.aliyun.com/document_detail/127834.html?)。

   1. 在[MongoDB控制台](https://console.cloud.tmall.com/resourceView#/aliyun/product?productCode=mongodb)创建MongoDB实例。

      > **[!NOTE]**
      >
      > 实例必须是单节点实例或副本集。
   2. 开启公网地址。
   3. 钉钉云MongoDB开启公网地址，并且在公网地址上添加如下访问白名单。

      ```
      118.178.120.0/24,47.98.51.0/24,116.62.64.0/24,120.55.111.0/24,120.26.106.0/24,101.37.14.0/24,47.97.118.0/24,120.55.241.0/24,118.31.165.0/24,114.55.125.94,120.55.40.0/24,116.62.172.0/24,121.40.125.0/24,47.99.171.0/24,118.31.118.0/24,101.37.13.0/24,47.97.7.0/24,116.62.197.0/24,115.29.182.0/24,121.196.246.0/24,121.196.199.0/24,121.43.179.0/24,120.55.194.0/24,47.97.195.0/24,120.27.211.0/24,47.97.116.0/24,116.62.201.0/24,120.26.116.0/24,121.43.185.141,120.55.12.0/24,47.97.119.0/24,121.196.211.0/24,120.55.108.0/24,47.97.27.142,121.43.162.0/24,116.62.20.0/24,120.55.192.0/24,118.31.246.0/24,47.97.73.210,120.26.117.0/24,118.31.238.0/24,101.37.12.0/24,101.37.25.0/24,47.97.73.0/24,114.55.89.0/24,47.97.27.0/24,121.43.162.118,115.29.198.0/24,120.26.118.0/24,114.55.125.0/24,121.43.174.187,47.97.106.0/24,47.99.43.0/24,115.29.183.0/24,120.55.129.0/24,47.97.125.0/24,118.31.184.0/24,116.62.206.0/24,47.96.39.0/24,121.43.185.0/24,121.43.179.168,47.98.39.0/24,47.98.251.0/24,47.98.52.0/24,121.43.174.0/24,115.29.181.0/24,101.37.15.0/24,118.178.121.0/24,121.196.211.16,116.62.208.0/24,120.55.193.0/24,121.196.198.0/24,116.62.57.0/24
      ```
   4. 在聚石塔账号下创建迁移MongoDB的DTS任务，必须是**增量迁移**。

      - 源数据库：填写钉钉云MongoDB信息

        ![源数据](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6044044061/p178974.png)
      - 目标数据库：填写聚石塔上创建的MongoDB信息

        ![配置任务](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7044044061/p175715.png)
   5. 启动迁移任务。
3. 迁移OSS。

   1. 获取源OSS和目标OSS的AK和SK。
   2. 迁移配置，请参考[OSS数据迁移](https://help.aliyun.com/document_detail/56990.html?)文档。
   3. 启动迁移任务。

      ```
      bash import.sh
      ```
   4. 增量迁移。

      ```
      isIncremental=true   incrementalModeInterval=60
      ```
4. 迁移ECS，详情请参考[ECS迁移](https://open.taobao.com/doc.htm?docId=109536&docType=1)。

   钉钉云的ECS打包生成镜像，通过共享镜像的方式共享给聚石塔账号，然后在聚石塔账号下使用共享镜。

   共享镜像依赖的聚石塔账号的阿里云UID，请扫描文档底部提供的钉钉群二维码进群咨询。

## 步骤四：聚石塔应用部署

1. 使用钉钉账号登录[聚石塔](https://console.cloud.tmall.com/home)。
2. 将EIP绑定到已购买的ECS上，然后在ECS中启动应用。
3. 配置SLB实例，添加监听并将ECS挂载为后端服务器。详情请参考[配置负载均衡](https://help.aliyun.com/document_detail/86451.html?)。
4. 使用SLB的公网IP访问应用，验证服务可访问。

## 步骤五：应用切换

1. RDS切换：

   1. 在开发者后台，设置聚石塔数据源的用户名和密码。

      ![添加数据源](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5477533061/p175733.png)
   2. 联系钉钉小二（文档底部扫码进群咨询）切换推送RDS，需要提供应用的suiteKey和新、旧RDS实例ID。
   3. 应用首页地址切换。

      1. 如果使用的是钉钉安全域名，需要先切换成自己的服务域名。
      2. 如果使用的是自己的服务域名，修改DNS。

## 迁移咨询

请使用钉钉扫描下图的二维码，进群咨询。

![p175759](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4165756161/p254404.png)
