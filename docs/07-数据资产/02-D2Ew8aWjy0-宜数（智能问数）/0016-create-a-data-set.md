---
title: "创建数据集"
source_url: "https://open.dingtalk.com/document/aipass/create-a-data-set"
namespace: "aipass"
slug: "create-a-data-set"
group: "数据资产"
tab: "宜数（智能问数）"
breadcrumb: "数据工厂 > 创建数据集"
doc_id: "onp4YyFGWM"
updated_at: "2026-08-14 09:26:55"
---

> Source: https://open.dingtalk.com/document/aipass/create-a-data-set
> Path: 数据资产 / 宜数（智能问数） / 数据工厂 > 创建数据集
> Updated: 2026-08-14 09:26:55

# 创建数据集

> **[!NOTE]**
>
> 当前**高级版**可使用。

## **概述**

数据集是在产品内进行数据消费的基本单元，是用于数据消费抽象出来的一个逻辑概念，数据工厂内，数据集的来源分为四种：

- **本地表格**：本地离线excel文件上传注册为数据集。
- **数据库：**关系型数据库中的表，注册为数据集
- **钉钉连接器：**自定义数据模型（接收连接器执行动作同步数据）注册为数据集
- **数据准备：**对上述3种数据集进行加工处理，生成新的数据集

## **功能价值**

通过创建数据集，可以实现数据在宜数产品内各个场域内（问数助理、互动大屏、自定义仪表盘、数据API等）的流通与消费。

## 场景一：本地Excel注册为数据集

1. 单击“数据工厂”菜单，选择“数据集管理”菜单，选择“新建数据集”按钮，进入数据集类型选择界面，选择“本地表格”。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5180766871/p890622.png)
2. 将本地数据，按照模板要求进行处理好之后，拖拽文件至上传区域。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5180766871/p890623.png)
3. 填写数据集配置信息，系统会自动解析模板内容，读取字段信息及字段类型，按照实际需求场景，填写业务场景名称，数据集名称及描述等信息，点击保存即可创建成功。

   - **业务场景名称**：用于在后续的数据服务中筛选出该数据集。
   - **数据集名称**：用于标识此数据集，不可重名。
   - **数据集字段**：上架到数据资产平台的字段 。
   > **[!NOTE]**
   >
   > 可以点击右上角“自动填充字段描述” 按钮，由AI对字段名称及描述自动填充，提高效率。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5180766871/p890624.png)

## **场景二：自有数据库注册为数据集**

1. 单击“数据工厂”菜单，选择“数据集管理”菜单，选择“新建数据集”按钮，进入数据集类型选择界面，选择“数据库”类型。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5180766871/p890625.png)
2. 进入选择数据源界面，选择相应的数据库（如没有对应的数据库，可以选择下方新建数据库），单击“下一步”即可。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5180766871/p890627.png)
3. 填写数据集配置信息：

   选择数据库中对应的表信息，系统会自动拉取表结构信息，根据实际业务，填写字段自定义名称集描述，点击 “保存”按钮，即完成数据库类型数据集的创建：

   - **业务场景名称**：用于在后续的数据服务中筛选出该数据集。
   - **数据集名称**：用于标识此数据集，不可重名
   - **数据集字段**：上架到数据资产平台的字段
   > **[!NOTE]**
   >
   > 可以点击右上角“自动填充字段描述” 按钮，由AI对字段名称及描述自动填充，提高效率。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5180766871/p890629.png)

## **场景三：企业连接器注册为数据集**

1. 单击“数据工厂”菜单，选择“数据集管理”菜单，选择“新建数据集”按钮，进入数据集类型选择界面，选择“钉钉连接器”类型。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5180766871/p890630.png)
2. 配置数据集的信息：

   - **业务场景名称**：用于在后续的数据服务中筛选出该数据集。
   - **数据集名称**：用于标识此数据集，不可重名
   - **数据集字段**：上架到数据资产平台的字段

     - 系统默认字段biz\_time，用于标识数据集时间维度的字段，例如数据的创建日期、更新日期等Date类型的字段，建议选为主键加快查询效率。
     - 自定义字段，由用户按需创建。

     ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5180766871/p890633.png)
3. 保存数据集，连接器方式创建的数据集，保存后无法编辑，如若修改，需要删除重新创建。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5180766871/p890634.png)
4. 跳转到连接平台，配置连接流**（重要）：**

   1. 创建完数据集后，跳转到[连接平台](https://open-dev.dingtalk.com/fe/connector#/myFlow)，依次单击**我的连接流** > **创建连接流**。

      ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5180766871/p890636.png)
   2. 在流程配置中，配置**触发事件**和**执行动作**。

      ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5180766871/p890637.png)
   3. 配置连接流—触发条件：用户自定义，参考[连接器帮助文档](../../02-连接平台/02-XdgyZifJkr-我的连接/0001-create-a-connection-flow-1.md)：

      - 选择连接器：官方/自建/三方连接器

        - 执行动作：自定义
        - 配置参数：自定义

        ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5180766871/p890638.png)
   4. 配置连接流—执行动作：用户需要按以下步骤配置：

      1. 选择连接器：选择【数据资产品台】连接器。

         ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5180766871/p890639.png)
      2. 执行动作：选择【接收并储存数据】执行动作。

         ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5180766871/p890640.png)
      3. 配置参数：在数据资产平台配置的连接器类型数据集，都会在这里回显。

         ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5180766871/p890641.png)

         ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5180766871/p890643.png)
5. 测试&发布，配置完连接流后，可以先调试，调试成功后再发布。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5180766871/p890646.png)

## **场景四：**加工数据生成新数据集

1. 单击“数据工厂”菜单，选择“数据集管理”菜单，选择“新建数据集”按钮，进入数据集类型选择界面，选择“数据准备”类型。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5180766871/p890647.png)
2. 配置数据集的信息：

   - **业务场景名称**：用于在后续的数据服务中筛选出该数据集。
   - **数据集名称**：用于标识此数据集，不可重名。
   - **数据集描述**：数据集更详细的用途信息。

   从“**数据源**”中选择对应的表，拖拽至画板区域，配置关联关系等（详细配置见加工数据集部分），点击右上方“**配置数据集**”按钮，进行字段及数据预览，没问题后点击保存数据集，即完成数据集创建。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5180766871/p890649.png)
