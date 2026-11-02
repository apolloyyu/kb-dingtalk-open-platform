---
title: "概述"
source_url: "https://open.dingtalk.com/document/development/apsara-file-storage-for-hdfs-overview"
namespace: "development"
slug: "apsara-file-storage-for-hdfs-overview"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "文档/文件 > 媒体文件 > 概述"
doc_id: "Q1QMwbp3hB"
updated_at: "2026-05-15 18:19:38"
---

> Source: https://open.dingtalk.com/document/development/apsara-file-storage-for-hdfs-overview
> Path: 应用开发 / 服务端 API / 文档/文件 > 媒体文件 > 概述
> Updated: 2026-05-15 18:19:38

# 概述

本文介绍了什么是媒体文件，媒体文件开放了哪些接口能力，以及如何接入媒体文件接口能力等。

## 什么是媒体文件

媒体文件是钉钉提供的开放能力之一，可以在企业内部应用和第三方企业应用内的文件储存场景使用。

### 媒体文件位置说明

本功能媒体文件使用的空间是钉钉提供给组织的特定存储空间，不属于组织的钉盘空间，调用本功能接口上传文件，不占用钉钉组织的钉盘空间

### 存储有效期说明

本功能文件的存储有效期无限制，通常钉钉组织没有解散，上传文件返回的media\_id可以一直使用。

## 开放概览

媒体文件提供了丰富的接口开放能力，开发者通过API接口可以实现媒体文件和企业业务系统打通。

| API | 说明 | API版本 |
| --- | --- | --- |
| [上传媒体文件](0646-upload-media-files.md) | 上传图片、语音媒体资源文件以及普通文件。 | 旧版 |

## 使用教程

钉钉提供了媒体文件接口接入流程示例，请参见下方表格：

| **教程名称** | **功能介绍** | **教学范围** | **Demo 下载** |
| --- | --- | --- | --- |
| [上传媒体文件后发送工作通知](0645-procedure-for-using-media-files.md) | 上传媒体文件、发送消息通知 | 所有钉钉开发者 | [file-demo.zip](https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20250729/qrbdtr/file-demo.zip?spm=ding_open_doc.document.0.0.18684a70zYmQDC&file=file-demo.zip) |
