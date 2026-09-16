---
title: "文件上传问题自查手册"
source_url: "https://open.dingtalk.com/document/development/self-examination-manual-for-file-upload-issues"
namespace: "development"
slug: "self-examination-manual-for-file-upload-issues"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "文档/文件 > 存储管理 > 文件传输 > 文件上传问题自查手册"
doc_id: "Ji4SHyWNSi"
updated_at: "2025-09-10 19:36:08"
---

> Source: https://open.dingtalk.com/document/development/self-examination-manual-for-file-upload-issues
> Path: 应用开发 / 服务端 API / 文档/文件 > 存储管理 > 文件传输 > 文件上传问题自查手册
> Updated: 2025-09-10 19:36:08

# 文件上传问题自查手册

本文主要介绍如何自查文件上传遇到的常见问题。

## 提交文件失败

文件的上传有三个步骤，请参考[获取文件上传信息](0674-obtain-file-upload-informations.md)文档内的步骤。

1. 获取文件上传信息。
2. 通过HTTP将文件上传到OSS。
3. 提交文件。

**需要确认下第二步将文件上传到OSS有没有成功返回200。**

## 上传文件到OSS失败问题

排查下代码问题，将<authorization>、<x-oss-date>、<url>替换成第一步获取文件上传信息接口返回的值。a.txt替换成本地存在的文件，执行以下命令。

```
curl -v -T a.txt \
--header "Authorization: <authorization>" \
--header "x-oss-date: <x-oss-date>" \
--url "<url>"
```

- 如果curl返回RequestTimeTooSkewed错误，表示上传信息过期，重新获取文件上传信息。
- 如果curl返回200，说明是代码问题。文档中已经有对应语言的demo，参照对应示例，排查代码问题。
- 如果代码上传返回SignatureDoesNotMatch，大概率是HTTP请求headers多传了contentType，主动设置为空(可以将请求header打印出来, 查看headers中的contentType)。
- 如果curl没有返回200。

  - 如果提示域名解析失败或者连接失败, 按照以下方式排查。

    - ping <对应域名或ip>
    - telnet <对应域名或ip> 443
    - 连接手机热点ping和telnet，更换其它网络ping和telnet
    - 关闭电脑防火墙ping和telnet
    - 联系IT对存储OSS公网域名加白，域名见本文档下方**附录I**
    - 如果是专属存储，联系专属存储运维同学，查看网络连通性问题

## 附录I 存储OSS公网域名

- sz.trans.dingtalk.com
- sh.trans.dingtalk.com
- zjk.trans.dingtalk.com
- lippi-space-zjk.oss-cn-zhangjiakou.aliyuncs.com
- lippi-space-sh.oss-cn-shanghai.aliyuncs.com
- lippi-space-sz.oss-cn-shenzhen.aliyuncs.com
- cdn-zjk-trans.dingtalk.com
- cdn-sh-trans.dingtalk.com
- cdn-sz-trans.dingtalk.com
