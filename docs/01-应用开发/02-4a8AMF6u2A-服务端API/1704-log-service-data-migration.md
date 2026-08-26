---
title: "SLS数据迁移"
source_url: "https://open.dingtalk.com/document/development/log-service-data-migration"
namespace: "development"
slug: "log-service-data-migration"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 钉钉云 > 迁移方案 > SLS数据迁移"
doc_id: "l025wNZcto"
updated_at: "2025-10-16 14:31:32"
---

> Source: https://open.dingtalk.com/document/development/log-service-data-migration
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 钉钉云 > 迁移方案 > SLS数据迁移
> Updated: 2025-10-16 14:31:32

# SLS数据迁移

可以利用SLS的数据加工功能进行LogStore存量数据的迁移，注意迁移过程会产生读写流量、数据加工等的计量和计费，因此除非业务上必须，否则不建议SLS存量日志数据的迁移，一般将业务切到新的SLS Project， 源SLS Project LogStore的数据过期后自动清理掉。

## 迁移说明

本文档迁移环境说明：

- 源SLS 信息：region 为 华北2（北京），源项目为 nginx-log-charles ，源logstore为nginx-logstore-charles
- 目标SLS信息：region 为华北3（张家口），目标项目为sls-migration-test，目标logstore为sls-migration-test。

## 操作步骤

1. **钉钉云账号：配置数据加工。**

   1. 在SLS服务页面，进入到待迁移的源SLS Project，选择要迁移的源 logstore，然后单击**数据加工**。

      ![sls](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1063237061/p188480.png)
   2. 单击**保存数据加工**。

      ![数据加工](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1063237061/p188481.png)
   3. 输入正确的信息。

      > **[!IMPORTANT]**
      >
      > 其中存储目标务必填写已经创建好的迁移目标Project和LogStore，存储目标和授权方式务必填写正确，此处是能否正常完成SLS数据迁移的关键。

      ![数据加工](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2063237061/p188482.png)

      加工范围的时间区间务必包括所有要迁移SLS日志的时间，其他的不需要配置，然后单击**确定**。

      ![加工范围](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2063237061/p188483.png)
2. **钉钉云账号：查看数据加工任务状态。**

   找到“数据加工”列表，点击创建的数据加工任务，在概览页可以看到数据加工的状态，当加工速率“delieverd”和“accept”有数据时，表示已经开始通过数据加工来进行logstore迁移，如下所示：

   ![数据加工状态](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2063237061/p188479.png)
3. **聚石塔账号：查看迁移的SLS数据。**

   如果迁移目的SLS有开启索引，通过查询就可以看到迁移过来的数据了。

   ![sls数据迁移](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3683807061/p188478.png)
