---
title: "卡片调试工具"
source_url: "https://open.dingtalk.com/document/development/card-debugging-tool"
namespace: "development"
slug: "card-debugging-tool"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "即时通信 > 互动卡片 > 示例与工具 > 卡片调试工具"
doc_id: "eMjetpSOiA"
updated_at: "2025-09-23 19:18:12"
---

> Source: https://open.dingtalk.com/document/development/card-debugging-tool
> Path: 应用开发 / 服务端 API / 即时通信 > 互动卡片 > 示例与工具 > 卡片调试工具
> Updated: 2025-09-23 19:18:12

# 卡片调试工具

如果你需要进行卡片调试，你可以参考本文档内容完成调试操作。

## **调试入口**

你可以登录[卡片平台](https://open-dev.dingtalk.com/fe/card#/)，单击调试工具。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3853591171/p786915.png)

输入发出卡片的 outTrackId 进行查询，查询成功后下面查询历史记录会刷新最新查询的结果，点击绿色的时间标签右边的操作按钮，可以在「桌面端」、「移动端」打开卡片调试工具。查询历史记录会保留最近查询的 10 条记录。

> **[!NOTE]**
>
> 卡片调试工具目前只支持 IM 场域下的消息卡片、标准卡片、吊顶卡片、AI 卡片的调试使用，暂不支持通讯录卡片和工作台卡片的调试使用。

## **调试卡片**

打开调试工具后，可以看到卡片的基本信息、卡片预览、卡片数据，以及导出模板按钮、清除模板缓存并刷新按钮。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3853591171/p787197.png)

> **[!IMPORTANT]**
>
> 因为调试工具只会获取**客户端本地**的卡片数据， 所以无法获取到在客户端上没有使用过的卡片数据。

### **卡片数据**

#### **原始数据**

可以查看下发到客户端上的卡片数据。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3853591171/p787199.png)

#### 数据校验

在数据校验模块可以查看当前卡片数据是否存在潜在问题，如变量值为空、变量类型不匹配等。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3853591171/p787202.png)

### **清除模板数据**

修改卡片模板并保存：

![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3853591171/p786914.png)

在卡片调试工具中**点击清除缓存并刷新**按钮：

[](https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20240401/cipdfr/4%E6%9C%881%E6%97%A5+%E5%8D%A1%E7%89%87%E8%B0%83%E8%AF%95.mp4)

在开发过程中经常会涉及到模板的更新， 由于缓存机制可能会导致端上实际使用的不是最新版本的模板。针对这种情况可以手动执行清除模板操作来使用最新版本的模板。

> 如果发现模板仍然没有更新，可以尝试重新发送一张卡片后切换会话触发卡片重渲染拉取最新的卡片模板。
