---
title: "资源的购买"
source_url: "https://open.dingtalk.com/document/development/purchase-resources"
namespace: "development"
slug: "purchase-resources"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 钉钉云 > 常见问题 > 资源的购买"
doc_id: "kfZ1w3M6f2"
updated_at: "2025-10-16 14:31:29"
---

> Source: https://open.dingtalk.com/document/development/purchase-resources
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 钉钉云 > 常见问题 > 资源的购买
> Updated: 2025-10-16 14:31:29

# 资源的购买

**重要提示****：**目前钉钉云**仅支持****华东1****区域，**购买资源时请只选择**华东1****区域，****以免购买错误耽误接入钉钉云****。**

## 推荐配置

基于上面的最佳实践，结合不同规模ISV的需求，我们推荐以下的资源配置。同时也给出相应的一年期费用，做为你进行预算申请的参考。

**注意**：以下推荐的资源配置及费用，只是相应的最小需求，并不意味着可以满足你所有的需求。如果你需要额外的云产品（例如消息队列，OSS存储等），你将需要支付相应的费用。

## 小型应用服务商

价格会随折扣变化，表格费用仅供参考，具体以购买为准。

| **云产品** | **规格** | **数量** | **包年费用** |
| --- | --- | --- | --- |
| 云服务器ECS | sn1ne.large | 2 | 2368.54 \* 2 |
| 云数据库RDS | MySQL 5.7 高可用版 2核4G 20G存储 | 1 | 4476.82 |
| 负载均衡SLB | 标准型I (slb.s2.small) | 1 | 190.00 \* 12 |
| NAT网关 | 小型 | 1 | 12 \* 365 |
| 弹性公网IP及带宽-SLB | 5M | 1 | 1275.00 |
| 弹性公网IP及带宽-NAT | 2M | 1 | 469.20 |
| 总计 |  |  | **17654.1** |

## 中型应用服务商

价格会随折扣变化，表格费用仅供参考，具体以购买为准。

| **云产品** | **规格** | **数量** | **包年费用** |
| --- | --- | --- | --- |
| 云服务器ECS | sn1ne.xlarge | 3 | 4615.63 \* 3 |
| 云数据库RDS | MySQL 5.7 高可用版 4核8G 20G存储 | 1 | 8381.02 |
| 负载均衡SLB | 标准型II (slb.s2.medium) | 1 | 380.00 \* 12 |
| NAT网关 | 中型 | 1 | 23 \* 365 |
| 弹性公网IP及带宽-SLB | 10M | 1 | 5355.00 |
| 弹性公网IP及带宽-NAT | 4M | 1 | 979.20 |
| 总计 |  |  | **41517.11** |

## 大型应用服务商

价格会随折扣变化，表格费用仅供参考，具体以购买为准。

| **云产品** | **规格** | **数量** | **包年费用** |
| --- | --- | --- | --- |
| 云服务器ECS | sn1ne.2xlarge | 4 | 9309.35 \* 4 |
| 云数据库RDS | MySQL 5.7 高可用版 8核16G 20G存储 | 1 | 15755.62 |
| 负载均衡SLB | 高阶型I (slb.s3.small) | 1 | 760.00 \* 12 |
| NAT网关 | 大型 | 1 | 45 \* 365 |
| 弹性公网IP及带宽-SLB | 20M | 1 | 13515.00 |
| 弹性公网IP及带宽-NAT | 8M | 1 | 3723.00 |
| 总计 |  |  | **95776.02** |

## ECS的购买

1. ECS的购买入口，注意区域选择华东1.

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7875299951/p163429.png)

![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7875299951/p163430.png "image.png")

2. 选择计费方式及地域，可用区选择随机分配

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8875299951/p163431.png)

3. 选择专有网络标签，选择名为dingcloud-vpc的专有网络。交换机暂时不用选择，可以先选择实例规格，因为不同的实例规格及库存情况会导致可以选择的交换机不同，如果先选择了交换机可能导致你想要的实例规格当前无可用库存。先选择实例规格将大大降低上述的问题。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8875299951/p163432.png)

4. 选择实例规格。推荐使用sn1ne类型。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8875299951/p163433.png)

5. 选择安全组。请选择名为default的安全组。

![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8875299951/p163434.png "image.png")

6. 选择交换机。每个可用区对应着一个交换机，当你购买多台ECS的时候，尽量将ECS放置在不同的可用区，这样可以提供更好的可用性，降低因为整个机房故障导致的可用性问题。

7. 选择“按固定带宽”，带宽为0Mbps，也就是不实用公网带宽。后继我们将通过SLB，NAT及弹性公网IP获得公网访问相关带宽。这样将会有更好的扩展性，详情参见架构的最佳实践。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8875299951/p163435.png)

8. 选择镜像和存储。根据你自己的需要选择相关的镜像和存储。

9. 选择购买周期，是否自动续费及数量。设置ECS的登录密码。不同的购买周期将有不同的折扣，建议按整年进行购买。正式上线的微应用环境至少要确保有3个月及以上的周期，否则将可能导致上线审核无法通过。如果你是用于测试的目的，可以选择按量付费，或者较短的包年包月周期。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8875299951/p163436.png)

10. 点击“立即购买”下单购买。

## RDS的购买

1. 购买入口。请选择华东1区域。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8875299951/p163437.png)

2. 选择计费类型：包年包月、按量付费；选择地域华东1；选择数据库类型；选择对应的数据库版本；系列请选择高可用版及以上，避免单点故障，同时也可以提供读写分离的能力。新的套件的创建将需要RDS进行数据推送，其支持的数据库是MySQL。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8875299951/p163438.png)

3. 选择“专有网路”网络类型，选择钉钉云缺省的的专有网络dingcloud-vpc，对应的交换机将根据上面的选择的可用区自动确定。再根据你的需要选择对应的规格、存储空间、购买时长及数量。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9875299951/p163439.png)

4. 预览当前的配置及价格，点击“立即购买”下单。

![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9875299951/p163440.png "image.png")

## SLB的购买

1. 购买入口，请选择地域华东1，保持与ECS在相同的地域。

![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9875299951/p163441.png "image.png")

2. 创建负载均衡。选择付费类型、地域（华东1）及主备可用区。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9875299951/p163442.png)

3. 选择实例规格，实例类型选择私网（后继将绑定弹性公网IP来提供对外服务），选择专有网络类型，专有网络选择钉钉云缺省的dingcloud-vpc，交换机将根据选择的主可用区自动选择。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9875299951/p163443.png)

4. 预览当前配置及费用，点击“立即购买”下单。

![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9875299951/p163444.png "image.png")

5. 创建成功后，在实例列表中点击负责均衡ID或者点击管理进入详情页。

![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9875299951/p163445.png "image.png")

![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0975299951/p163446.png "image.png")

6. 创建监听端口

![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0975299951/p163447.png "image.png")

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0975299951/p163448.png)

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0975299951/p163449.png)![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0975299951/p163450.png)

7. 添加后端服务器。因创建的负载均衡在专有网络中，因此只能添加相同专有网络内的ECS。

![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0975299951/p163451.png "image.png")

8. 检查添加服务器后的健康状态。这里需要你在相应的后端服务器提供相关的服务，否则健康检查会异常。

![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0975299951/p163452.png "image.png")

## NAT的购买

1. 购买入口。请选择华东1区域。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1975299951/p163453.png)

2. 创建NAT网关。选择华东1（杭州），VPC自动选择缺省的dingcloud-vpc，选择规格，点击“立即购买”下单。

![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1975299951/p163454.png "image.png")

![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1975299951/p163455.png "image.png")

3. 设置SNAT条目。设置SNAT条目需要首先购买弹性公网IP并绑定到NAT网关。请设置所有交换机的SNAT条目，这样可以保证所有可用区内的ECS都可以通过SNAT访问外网。

![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1975299951/p163456.png "image.png")

![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1975299951/p163457.png "image.png")

![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1975299951/p163458.png "image.png")

## EIP的购买

1. 购买入口。请选择华东1区域。

![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1975299951/p163459.png "image.png")

2. 购买EIP，选择付费方式，地域华东1，带宽，数量及购买时长。点击“立即购买”下单。

![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1975299951/p163460.png "image.png")

3. 绑定EIP到SLB和NAT。SLB和NAT将分别需要一个EIP。

![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2975299951/p163461.png "image.png")

![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2975299951/p163462.png "image.png")

![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2975299951/p163463.png "image.png")
