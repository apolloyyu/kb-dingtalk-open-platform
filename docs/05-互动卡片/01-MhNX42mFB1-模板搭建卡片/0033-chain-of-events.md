---
title: "事件链"
source_url: "https://open.dingtalk.com/document/development/chain-of-events"
namespace: "development"
slug: "chain-of-events"
group: "互动卡片"
tab: "模板搭建卡片"
breadcrumb: "模板搭建器 > 添加卡片交互 > 事件链"
doc_id: "uozu6spWyw"
updated_at: "2026-08-07 14:50:40"
---

> Source: https://open.dingtalk.com/document/development/chain-of-events
> Path: 互动卡片 / 模板搭建卡片 / 模板搭建器 > 添加卡片交互 > 事件链
> Updated: 2026-08-07 14:50:40

# 事件链

本文将介绍什么是事件链以及如何配置使用事件链。

## **概述**

事件链允许为单次事件配置并编排多个异步事件，同时支持配置这些事件的成功、失败回调。

### **核心价值**

- **多事件并发执行**：例如按钮点击时同时更新本地变量和发起回传请求。
- **差异化回调处理**：根据回传请求的成功或失败展示不同的弹窗提示。

### **适用场景**

当需要在单次交互中执行多个独立操作（如更新状态、发起请求、显示反馈）时，使用事件链可以避免编写复杂的自定义代码，通过可视化配置即可完成。

## **配置步骤**

### **选择事件类型**

选中需要配置事件链的组件，单击**事件** > **事件类型**，选择**事件链**。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0445806871/p772723.png)

### 打开编辑界面

单击**编辑事件链**，打开编辑事件链弹窗。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0445806871/p772749.png)

### 添加事件节点

在编辑事件链弹窗中，单击**新增事件**来添加需要调用的事件类型。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1445806871/p772753.png)

### 配置事件参数

以回传请求为例，根据业务需求，在下方表单中填入回传参数：

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1445806871/p775454.png)

到这里，你就已经完成基础的事件链配置了。

## **运行机制**

### **异步执行逻辑**

在事件链中，所有配置的事件会按照定义的顺序异步执行，每个事件可以独立执行，互不阻塞。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0445806871/p772762.png)

事件链的执行流程包含三个主要阶段：

1. **触发事件链**：当一个触发条件（如按钮点击、容器点击）满足时，事件链启动。
2. **顺序执行事件**：事件链中的事件按照配置顺序依次执行，但每个事件是异步的，不会等待前一个事件完成。
3. **回调处理**：每个事件可以配置成功和失败回调，事件链会根据事件的执行结果，调用相应的回调处理事件。

### **回调配置方法**

如果需要在事件执行后进行一些后续操作，可以通过事件链的回调来实现。目前支持回调的事件有：回传请求、动作面板等。回传请求的具体配置可以参考文档[事件回调](0007-event-callback-card.md)。

事件的回调分为成功回调和失败回调，每个事件回调可以配置以下内容：

| **回调类型** | **定义** | **配置方法** | **示例** |
| --- | --- | --- | --- |
| 成功回调 | 当事件成功执行后，要进行的操作。 | 在事件链事件的事件回调里选择**添加事件执行成功回调**。 | 回传请求调用成功后，弹窗提示成功信息。 |
| 失败回调 | 当事件执行失败后，要进行的操作。 | 在事件链事件的事件回调里选择**添加事件执行失败回调**。 | 回传请求调用失败后，弹窗提示失败信息。 |

#### 配置入口

在支持配置回调的事件中单击**添加回调**，就可以选择对应的事件执行结果的回调配置：

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1445806871/p815923.png)

这里的事件回调配置与上面的事件链配置类似，不同的是这里的事件执行成功回调配置可以使用事件返回值。

### **使用事件返回值**

如果你需要使用事件的返回值进行配置，你可以参考下方内容：

- **字段类型为事件返回值**：对应的事件链返回值变量格式应为：`cardData/cardPrivateData.****`。

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0445806871/p815921.png)
- **固定值类型中使用事件返回值**：格式应为 ：`${event.cardData/cardPrivateData.****}`。

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0445806871/p815920.png)

  具体是使用 cardData 还是 cardPrivateData 请根据服务端事件回调返回的数据结构来确定，这里填写的参数层级需与服务端下发的数据结构保持一致。
- **条件触发**：如果希望根据条件（运行环境、变量、事件返回值）来配置不同执行的事件，还可以通过单击**条件**按钮来配置附加的执行条件，使得仅当事件的返回结果与配置的条件相匹配时，才会触发设定的回调。

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0445806871/p815922.png)

  > **[!IMPORTANT]**
  >
  > - **回传请求成功**：指的是回传的网络请求发送成功。
  > - **回传请求失败**：指的是回传的网络请求发送失败。

## **典型应用**

### **请求后弹窗提示**

1. 添加**回传请求**事件，并配置相关参数：

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1445806871/p775456.png)
2. 添加事件的成功和失败回调，事件回调类型选择**弹窗提示**，并配置需要提示的内容：

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0445806871/p775458.png)

   假设业务服务端[事件回调](0007-event-callback-card.md)返回的数据为：

   ```
   {
     "cardData": {
       "cardParamMap": {
         "result": "https://open-dev.dingtalk.com/fe/card"
       }
     },
     "userPrivateData": {
       "cardParamMap": {}
     },
     "cardUpdateOptions": {
       "updateCardDataByKey": true,
       "updatePrivateDataByKey": true
     }
   }
   ```

   实现效果应为：

   ![image.gif](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7799089071/p772165.gif)

### **按钮禁用与恢复**

1. 添加**更新本地变量**事件，将控制按钮状态的变量`buttonStatus`更新为`disabled`：

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0445806871/p775460.png)
2. 添加**回传请求**事件并配置相关参数：

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0445806871/p775463.png)
3. 添加**事件成功回调**和**事件失败回调**，并在其中将`buttonStatus`更新为`normal`：

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0445806871/p775466.png)

   > **[!NOTE]**
   >
   > 由于这里需要将按钮的初始值设为`normal`，但是本地变量的初始值为空，所以需要将按钮的状态绑定一个[表达式变量](0027-variable-type.md#d5f7b6e08c31r)，参考如下实现：
   >
   > ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0445806871/p1093267.png)

   实现效果应为：

   ![image.gif](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6799089071/p772171.gif)

## **相关内容**

事件链使用的代码示例：[事件链配置演示](https://github.com/open-dingtalk/dingtalk-card-examples/tree/main/examples/事件链配置演示)。

如果你需要了解更多互动卡片示例，请参考[互动卡片示例中心](https://github.com/open-dingtalk/dingtalk-card-examples)。
