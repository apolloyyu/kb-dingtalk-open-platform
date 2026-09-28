---
title: "变量类型"
source_url: "https://open.dingtalk.com/document/development/variable-type"
namespace: "development"
slug: "variable-type"
group: "互动卡片"
tab: "模板搭建卡片"
breadcrumb: "模板搭建器 > 绑定卡片变量 > 变量类型"
doc_id: "0b70J0DXRY"
updated_at: "2026-08-05 09:10:17"
---

> Source: https://open.dingtalk.com/document/development/variable-type
> Path: 互动卡片 / 模板搭建卡片 / 模板搭建器 > 绑定卡片变量 > 变量类型
> Updated: 2026-08-05 09:10:17

# 变量类型

通过本文你将会了解到卡片变量的所有类型以及它们的适用场景。

## **变量类型**

卡片变量分为三种类型：[普通变量](#b339d2f08cjj9)、表达式变量和本地变量。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7122985871/p550138.png)

## **普通变量**

普通变量是最常用的变量类型，与发送卡片时配置的 `cardData` 字段一一对应。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7122985871/p532278.png)

普通变量的变量配置如下：

- **变量名**：唯一的变量名称
- **变量类型**：普通变量的变量类型，如数字、字符串、布尔值等等
- **变量描述**：该变量的描述，非必填
- **是否为私有变量**：详见下文**公有变量与私有变量的区别**

### **普通变量的类型**

| **变量类型** | **描述** | **示例** |
| --- | --- | --- |
| 字符串 | 字符串内容 | ``` "string" ``` |
| 字符串数组 | 由字符串组成的数组 | ``` ["str_1", "str_2"] ``` |
| 布尔值 | 布尔值内容，`true`或者`false` | ``` true ``` |
| 布尔数组 | 由布尔值组成的数组 | ``` [true, false] ``` |
| 数字 | 数字内容 | ``` 1688 ``` |
| 数字数组 | 由数字组成的数组 | ``` [1688, 1111] ``` |
| 对象 | 具有多个属性和对应值的结构体 | ``` {   "title": "标题",   "desc": "描述" } ``` |
| 对象数组 | 由多个对象构成的数组 | ``` [   {     "title": "标题_1",     "desc": "描述_1"   },   {     "title": "标题_2",     "desc": "描述_2"   } ] ``` |
| Markdown 内容 | 供「Markdown 内容」组件使用的数据类型，支持展示彩色文本、加粗、斜体、不同字号、链接、艾特人、钉钉表情展示等功能，语法规范请参考[Markdown 变量](0038-markdown-variable-new.md) | ``` "## 二级标题" ``` |
| 图表 | 供「图表」组件使用的数据类型，相关协议请参考[图表变量](0034-chart-variable.md) | ``` {   "data": [     {       "x": "N0",       "type": "line",       "y": 48     },     {       "x": "N1",       "type": "line",       "y": 74     }   ],   "type": "lineChart",   "config": {} } ``` |
| 用户信息 | 展示用户信息的数据类型，相关协议请参考[用户信息变量](0037-user-information-variables.md) | ``` {   "avatar": "",   "nick": "",   "uid": "" } ``` |
| 表格 | 供「表格」组件使用的数据类型，相关协议请参考[表格变量](0035-table-variables.md) | 参考[表格变量](0035-table-variables.md) |
| 表单 | 供「表单」组件使用的数据类型，相关协议请参考[表单变量](0036-form-variables.md) | 参考[表单变量](0036-form-variables.md) |

### **公有变量和私有变量**

根据定义时是否选中私有选项，变量分为公有变量和私有变量。定义为私有变量后，**卡片从私有数据中获取对应数据，若获取不到则从公有数据中获取**。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7122985871/p550149.png)

公有、私有变量的区别如下：

| **数据类型** | **公有变量** | **私有变量** |
| --- | --- | --- |
| **对应的数据类型** | 公有数据（cardData） | 私有数据（cardPrivateData） |
| 可见范围 | 数据对所有人可见 | 只针对自己可见 |

通过私有变量和私有数据的结合，服务端可用同一模板为不同用户推送不同数据，实现个性化展示。

> **[!NOTE]**
>
> 关于公有数据和私有数据具体的差异，请参考[公有、私有和本地数据](0030-public-private-and-local-data.md)。

## **表达式变量**

表达式变量通过对多个变量进行引用和组合计算得到，具有强大的能力，支持数字运算、大小判断、字符串拼接截取、类型转换、数组对象取值、时间格式化等功能。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7122985871/p550157.png)

其变量配置如下：

- **变量名**：唯一的变量名称
- **表达式**：表达式内容，如`variable_1 + variable_2`
- **变量描述**：该变量的描述，非必填

### **表达式文档**

点击表达式变量旁的帮助图标可打开表达式文档，查看所有表达式及用法示例。

![exp_variable_doc](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8092293761/p532552.gif)

### **使用示例**

假设已有展示文章列表的卡片，（如 `https://example.com/article/${id}`）。

假设目前已有一个展示文章列表的卡片：

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7122985871/p550158.png)

卡片变量中有一个叫`content` 对象数组用于循环渲染，每项含 `id` 字段，代表文章的`id`，想要实现点击文章时自动打开拼接好的链接，如

```
"https://www.dingtalk.com/?id=${id}"
```

为此创建表达式变量表示每项的最终链接：

1. 新增表达式变量并输入名称（即绑定时的变量名）。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7122985871/p550160.png)
2. 输入表达式。使用 `concat` 方法拼接字符串，先写入链接前缀。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7122985871/p550183.png)
3. 拼接第二个参数为 `content` 数组中每项的 `id`。使用 `subdata` 方法，选中 `content` 数组后输入 `subdata("id")`，从数组中取出每项的 `id` 与链接拼接，代表从`content` 数组中取出每一项的`id`与链接进行拼接。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7122985871/p550189.png)
4. 最终表达式即为完整拼接逻辑。

   ```
   concat("https://www.dingtalk.com/?id=", subdata("id"))
   ```
5. 在循环容器上设置点击事件并绑定该变量。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7122985871/p550196.png)
6. 进入预览模式后，点击不同文章会跳转到不同链接。

## **本地变量**

本地变量是特殊的私有变量，作为卡片的临时状态。修改值不会发送请求到服务端，但可通过组件（如按钮）的回传请求事件将值回传，适用于表单收集等场景。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7122985871/p550205.png)

### **使用示例**

实现简单表单询问是否参加活动，包含选择框和提交按钮。用户勾选后点击提交携带值。此场景适合用本地变量存储「是否参加」的值，点击提交时再收集。

> **[!NOTE]**
>
> 由于示例较为简单，此处略过卡片搭建的过程，从事件和变量的处理开始讲解。

从事件和变量处理开始讲解：

1. 创建名为 `join` 的本地变量代表是否参加。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7122985871/p550224.png)
2. 为选择框绑定 `join` 变量，实时展示参加状态。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7122985871/p550227.png)
3. 为实现点击选择框后切换值，添加事件更新本地变量 `join`。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7122985871/p550231.png)
4. 为提交按钮添加回传请求事件，点击后将 `join` 提交回服务端。回传参数配置为变量类型，选择 `join` 变量。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7122985871/p550239.png)
5. 卡片设计完毕，实际发出的卡片中点击提交即可提交 `join` 变量值。

   ```
   {
     "actionType": "0",
     "cardInstanceId": "String",
     "actionId": "1",
     "actionData": "{\"cardPrivateData\":{\"params\":{\"join\":true},\"actionIds\":[\"1\"]}}",
     "requestEventId": "String",
     "requestStatusKey": "String"
   }
   ```
