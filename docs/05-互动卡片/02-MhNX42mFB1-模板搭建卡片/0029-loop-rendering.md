---
title: "循环渲染"
source_url: "https://open.dingtalk.com/document/development/loop-rendering"
namespace: "development"
slug: "loop-rendering"
group: "互动卡片"
tab: "模板搭建卡片"
breadcrumb: "模板搭建器 > 绑定卡片变量 > 循环渲染"
doc_id: "RBDNWrZvge"
updated_at: "2026-08-05 09:10:19"
---

> Source: https://open.dingtalk.com/document/development/loop-rendering
> Path: 互动卡片 / 模板搭建卡片 / 模板搭建器 > 绑定卡片变量 > 循环渲染
> Updated: 2026-08-05 09:10:19

# 循环渲染

通过本文你将了解到如何使用循环渲染容器来展示列表内容。

## **内容介绍**

循环渲染通过数据动态展示内容项，是典型场景如报名用户列表。下面借助用户列表渲染示例快速了解使用方法。

如图所示，卡片中展示了用户信息列表，且每个用户都有序号、头像以及昵称信息。

> **[!NOTE]**
>
> 循环渲染的结果只能在预览模式下才生效，且在编辑模式下当没有数据时「渲染渲染容器」不会展示子元素。为了更方便地进行布局的搭建调整，在循环渲染前建议先定义变量和模拟数据。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9122985871/p550581.png)

## **步骤一：创建变量**

循环渲染需要列表，每位用户需展示序列号、头像和昵称。首先创建 `userList` 对象数组表示用户列表，每项包含：

- **index**：序列号
- **userName**：用户昵称
- **avatar**：用户头像

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9122985871/p550582.png)

## **步骤二：数据模拟**

为`userList`模拟相关数据并保存：

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9122985871/p550590.png)

## **步骤三：布局搭建并绑定变量**

利用变量进行循环渲染需借助「循环渲染容器」绑定变量。布局搭建分为**基础布局实现**、**用户序列号展示**、**用户头像展示**和**用户昵称展示**四部分。

### **基础布局实现**

1. 添加「循环渲染容器」组件，绑定`userLIst` 变量后设置样式。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9122985871/p550593.png)

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9122985871/p550628.png)
2. 确定循环项布局。分析每项用户信息，切分为三部分分别放置序列号、头像和昵称。
3. 使用「1:1:1」布局方式，将组件拖入「循环渲染容器」。

   ![drag_1_1_1](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7192293761/p537977.gif)

### **用户序列号展示**

1. 使用「基础文本」组件展示序列号。为美观，修改「布局容器」子元素位置为「左中」使垂直居中。

   ![loop_step2](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7192293761/p537978.gif)
2. 序号宽度不长，为「布局」组件添加合适固定宽度。

   ![loop_step3](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7192293761/p537979.gif)
3. 为「基础文本」组件绑定循环数组中的 `index` 字段。

   ![loop_step4](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7192293761/p537980.gif)
4. 预览模式下已能展示模拟数据中的所有序列号。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9122985871/p550641.png)

### **用户头像展示**

1. 与序列号展示类似。在中间布局中使用「头像」组件展示头像，绑定循环里的 `avatar` 变量，简单调整样式。

   ![loop_step5](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7192293761/p537989.gif)
2. 调整「布局」宽度为合适值。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9122985871/p550655.png)
3. 预览模式下同样能展示所有头像。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9122985871/p550656.png)

### **用户昵称展示**

用户昵称展示与序列号展示一样，均使用「基础文本」组件：

![loop_step6](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7192293761/p537994.gif)

至此循环渲染示例结束，最终效果如下：

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9122985871/p550661.png)
