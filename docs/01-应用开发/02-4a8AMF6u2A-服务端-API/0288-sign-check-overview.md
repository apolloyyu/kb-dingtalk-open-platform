---
title: "概述"
source_url: "https://open.dingtalk.com/document/development/sign-check-overview"
namespace: "development"
slug: "sign-check-overview"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "签到 > 概述"
doc_id: "IcHeHSUtzQ"
updated_at: "2026-07-02 10:36:28"
---

> Source: https://open.dingtalk.com/document/development/sign-check-overview
> Path: 应用开发 / 服务端 API / 签到 > 概述
> Updated: 2026-07-02 10:36:28

# 概述

本文介绍签到产品、如何开通签到应用、签到提供的接口能力，以及如何接入签到能力流程。

## 什么是签到

员工可以在工作台或群中进行签到，快速上报当前位置。更多使用详情可参考[钉钉使用手册-签到介绍](https://alidocs.dingtalk.com/i/p/Y7kmbokZp3pgGLq2/docs/Y7kmbEZDOqnQMXLq?dontjump=true)。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3722809661/p522438.png)

## 如何开通签到

签到是钉钉默认安装的官方应用。员工可以在钉钉工作台打开应用并使用。

- 手机端：钉钉手机客户端-工作台

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2722809661/p522435.png)
- 电脑端：钉钉电脑客户端-工作台

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2722809661/p522433.png)

## 开放概览

### **开放接口列表**

签到提供了丰富的接口开放能力，开发者通过API接口可以实现签到和企业自由的业务系统打通。

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [获取用户签到记录](0290-obtain-the-check-in-records-of-multiple-users.md) | 获取用户签到记录。 | 旧版 |
| [获取部门用户签到记录](0291-get-check-in-data.md) | 以部门维度获取员工签到记录。 | 旧版 |

### 签到回调事件列表

签到支持[用户签到](../04-LFcRvVD08N-事件订阅/0014-event-check-in.md)回调事件。

## 使用教程

钉钉提供了签到接口接入流程示例，请参见[获取员工签到信息](0289-obtain-check-in-information.md)。

## 名词解释

- **拜访对象（visit\_user）：**拜访对象，可以是外部联系人或者用户输入。

  ![iShot2022-04-18_09](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0426420561/p430863.png)
- **备注信息（remark）：**员工签到时填写的备注信息。

  ![iShot2022-04-18_09](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1426420561/p430864.png)
