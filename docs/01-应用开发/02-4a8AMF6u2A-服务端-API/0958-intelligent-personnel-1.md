---
title: "常见问题"
source_url: "https://open.dingtalk.com/document/development/intelligent-personnel-1"
namespace: "development"
slug: "intelligent-personnel-1"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "智能人事 > 常见问题"
doc_id: "MWOu1PWZXF"
updated_at: "2025-09-10 19:34:10"
---

> Source: https://open.dingtalk.com/document/development/intelligent-personnel-1
> Path: 应用开发 / 服务端 API / 智能人事 > 常见问题
> Updated: 2025-09-10 19:34:10

# 常见问题

本文介绍了智能人事相关的常见问题。

## 第三方企业应用获取员工花名册字段信息报错“{ errcode:400020, success:false, errmsg:无访问权限 }”

答：第三方企业应用[获取员工花名册字段信息](0939-api-getemployeerosterbyfield.md)出现上述报错时，请先提交[员工档案开放接口权限申请](https://yida.alibaba-inc.com/o/integrate/roster/apply)，审批通过后才可调用该接口获取花名册字段信息。

## 调用获取花名册元数据接口获取不到在花名册中新增的字段

答：调用[获取花名册元数据](0937-intelligent-personnel-roster-metadata-query.md)获取不到新增数据时，请先确认[企业管理后台](https://oa.dingtalk.com/) **> 通讯录 > 智能人事 > 设置 > 员工档案字段设置**中是否已经添加的该字段。员工档案字段设置图例如下:![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6463897661/p510125.png)

## 调用更新员工花名册信息接口在更新主部门sys00-mainDeptId不生效

答：[更新员工花名册信息](0940-intelligent-personnel-update-employee-file-information.md)出现更新主部门不生效时，可能原因是入参的userid不在该部门。
