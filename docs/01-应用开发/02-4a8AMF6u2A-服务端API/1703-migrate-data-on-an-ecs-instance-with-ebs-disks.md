---
title: "带EBS数据盘ECS迁移"
source_url: "https://open.dingtalk.com/document/development/migrate-data-on-an-ecs-instance-with-ebs-disks"
namespace: "development"
slug: "migrate-data-on-an-ecs-instance-with-ebs-disks"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 钉钉云 > 迁移方案 > 带EBS数据盘ECS迁移"
doc_id: "ucq77lXsqU"
updated_at: "2025-12-22 14:28:23"
---

> Source: https://open.dingtalk.com/document/development/migrate-data-on-an-ecs-instance-with-ebs-disks
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 钉钉云 > 迁移方案 > 带EBS数据盘ECS迁移
> Updated: 2025-12-22 14:28:23

# 带EBS数据盘ECS迁移

参考本文迁移带EBS数据盘的ECS实例。

## 迁移说明

不建议单独迁移EBS数据盘，如果ECS实例有挂在EBS数据盘，可以通过共享镜像的方式来实现整机（系统盘+数据盘）一起迁移。如下图所示，migration-test-puzhu除了系统盘外，挂载一个EBS数据盘。

![实例云盘](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4953807061/p188469.png)

## 步骤一：**创建带EBS数据盘的ECS镜像**

1. 实例列表中找到要迁移的ECS实例，然后单击**更多 > 云盘和镜像 > 创建自定义镜像**。

   ![创建自定义镜像](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4953807061/p188471.png)
2. 填写镜像信息，然后单击**创建**。

   ![创建镜像页面](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5953807061/p188472.png)

## 步骤二：复制镜像至目标地域

跨区域复制镜像，将钉钉云账号下自定义镜像通过“复制镜像”复制到目标地域（Region）。

> **[!IMPORTANT]**
>
> 如果钉钉云账号与聚石塔账号在同一个Region，可以跳步本步骤。

1. 在镜像列表中找到刚创建的镜像，单击**复制镜像**按钮。

   ![复制镜像](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5953807061/p188473.png)
2. 在“复制镜像”页面，选择目标地域（如华北3），填写复制后的镜像名称。

   ![复制镜像页面](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5953807061/p188474.png)
3. 单击**确定**启动复制任务，状态显示为“复制中”，通常耗时与镜像大小成正比，建议预留30分钟以上。

## 步骤三：共享自定义镜像给聚石塔账号

到目标Region找到自定义镜像，然后配置共享自定义镜像。

1. 在镜像详情页，单击**共享镜像**，进入共享设置页面。

   ![共享镜像](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5953807061/p188475.png)
2. 选择聚石塔目标账号的阿里云账号ID或ARN（如 `acs:ram::123456789012:role/JushitaMigrationRole`），建议提前获取准确ARN信息。

   ![共享镜像](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5953807061/p188476.png)

## 步骤四：在目标地域创建ECS实例

由聚石塔账号在目标地域使用共享镜像创建新ECS实例。

1. 切换至目标账号登录ECS控制台，进入镜像列表，查看共享镜像是否可见。
2. 选择共享镜像 ，并配置数据盘信息。

   ![创建ECS](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5953807061/p188477.png)
