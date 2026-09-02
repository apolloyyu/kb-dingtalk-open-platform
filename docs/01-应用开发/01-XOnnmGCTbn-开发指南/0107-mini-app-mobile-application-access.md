---
title: "介绍"
source_url: "https://open.dingtalk.com/document/dingstart/mini-app-mobile-application-access"
namespace: "dingstart"
slug: "mini-app-mobile-application-access"
group: "应用开发"
tab: "开发指南"
breadcrumb: "接入移动客户端 > 接入钉钉登录 > 介绍"
doc_id: "bku6WgLaAa"
updated_at: "2026-05-13 09:01:00"
---

> Source: https://open.dingtalk.com/document/dingstart/mini-app-mobile-application-access
> Path: 应用开发 / 开发指南 / 接入移动客户端 > 接入钉钉登录 > 介绍
> Updated: 2026-05-13 09:01:00

# 介绍

移动应用钉钉登录是基于[OAuth2.0协议标准](https://oauth.net/2/)构建的钉钉OAuth2.0授权登录系统。

> **[!NOTE]**
>
> - 目前移动应用上钉钉登录只提供原生的登录方式，需要用户安装钉钉客户端才能配合使用。
> - 对于Android应用，建议一直显示钉钉登录按钮，当用户手机没有安装钉钉客户端时，请引导用户下载安装钉钉客户端。

## 使用场景

某员工在使用企业自研发的APP客户端时，需要登录账号密码，为了方便登录，可以在登录页面内直接点击钉钉进行登录，使用钉钉账号密码实现登录该APP客户端。

下图是中银国际客户端的登录页面，已注册钉钉账号并且本机已安装钉钉客户端的用户，可以直接使用钉钉授权登录，无需输入账号密码。![iShot2022-01-20 16](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6387662461/p390456.png)

## 使用说明

当您的应用需要使用钉钉登录时，需要先在**钉钉开放平台**中新增钉钉应用，配合使用钉钉开放平台提供的SDK进行授权登录请求接入。正确接入SDK后并拥有相关授权域scope（即授权的范围，目前钉钉仅支持授权登录，获取用户的基本信息）权限后，开发者移动应用会在终端本地拉起钉钉应用进行授权登录，钉钉用户确认后钉钉将拉起开发者移动应用，并带上授权临时票据code参数。再调用钉钉的个人用户信息接口可获取登录人的基本信息，包括手机号、钉钉昵称、钉钉头像URL等。
