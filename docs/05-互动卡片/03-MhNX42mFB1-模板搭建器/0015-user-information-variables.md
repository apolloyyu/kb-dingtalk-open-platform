---
title: "用户信息变量"
source_url: "https://open.dingtalk.com/document/development/user-information-variables"
namespace: "development"
slug: "user-information-variables"
group: "互动卡片"
tab: "模板搭建器"
breadcrumb: "变量协议 > 用户信息变量"
doc_id: "jFSHqtFTX4"
updated_at: "2026-08-28 10:26:12"
---

> Source: https://open.dingtalk.com/document/development/user-information-variables
> Path: 互动卡片 / 模板搭建器 / 变量协议 > 用户信息变量
> Updated: 2026-08-28 10:26:12

# 用户信息变量

通过本文你可以了解到什么是用户信息变量以及它的协议定义。

## **概述**

用户信息类型的变量提供了一个固定的模板，你可以使用它快速地模拟一个用户的基本数据，它的使用方式与其他变量相同。用户信息变量包含了`avatar`、`uid`、`nick`等字段：

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3392293761/p523110.png)

## **变量数据协议**

```
interface IUser {
  /** 用户头像地址 */
  avatar: string;
  /** 用户昵称 */
  nick: string;
  /** 用户 id */
  uid: string;
}
```
