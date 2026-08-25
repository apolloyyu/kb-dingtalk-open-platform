---
title: "钉钉云的安全限制"
source_url: "https://open.dingtalk.com/document/development/security-restrictions-of-dingtalk-cloud"
namespace: "development"
slug: "security-restrictions-of-dingtalk-cloud"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 钉钉云 > 钉钉云介绍 > 钉钉云的安全限制"
doc_id: "HcJocoYUzh"
updated_at: "2025-10-16 14:31:13"
---

> Source: https://open.dingtalk.com/document/development/security-restrictions-of-dingtalk-cloud
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 钉钉云 > 钉钉云介绍 > 钉钉云的安全限制
> Updated: 2025-10-16 14:31:13

# 钉钉云的安全限制

本文介绍了钉钉云的安全设置。

## VPC

钉钉云账号没有创建及修改VPC的权限。平台会为你初始化好钉钉云VPC，并在该VPC内创建好路由器，在该region中每个可用区创建一台交换机。你使用的ECS、RDS等各种基础设施，都必须在该VPC内。

## 安全组

钉钉云账号没有创建及修改安全组的权限。平台会为你初始化默认的安全组，你创建的ecs实例必须选择该安全组。安全组有以下规则：

| **规则** | **描述** |
| --- | --- |
| 入方向 | 允许来自任意IP的ICMP请求 |
| 入方向 | 允许来自任意IP对80及443端口的TCP请求 |
| 入方向 | 允许来自任意IP对22及3389端口的TCP请求 |
| 入方向 | 拒绝不符合以上入方向规则的所有其他请求 |
| 出方向 | 允许发起对钉钉开放平台接口的所有TCP请求 |
| 出方向 | 允许发起到内网的所有端口的所有协议的请求 |
| 出方向 | 拒绝不符合以上出方向规则的所有其他请求 |

原则上钉钉云不允许跟外部系统有数据交换，如果你的系统需要依赖钉钉云外部的服务，需要增加更多的安全组权限，请在[开发者后台](https://open-dev.dingtalk.com/)提交相应的申请。

## RAM

钉钉云账号没有使用RAM（访问控制）服务的权限。平台默认会为你创建一个用户账号，如果你需要其他权限子集的子账号（例如财务人员账号、运维人员账号等），请联系我们。

## ECS

钉钉云账号没有为ECS实例分配公网IP的权限。如果希望ECS实例有公网访问能力，请使用EIP。

## RDS

钉钉云账号没有以下RDS权限

（1）删除实例

（2）修改实例网络类型

（3）为实例分配公网地址

（4）不能下载数据库的备份
