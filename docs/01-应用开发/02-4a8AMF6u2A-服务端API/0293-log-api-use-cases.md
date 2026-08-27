---
title: "三方系统发起和查看日志信息"
source_url: "https://open.dingtalk.com/document/development/log-api-use-cases"
namespace: "development"
slug: "log-api-use-cases"
group: "应用开发"
tab: "服务端API"
breadcrumb: "日志 > 使用教程 > 三方系统发起和查看日志信息"
doc_id: "N0slg35yJ3"
updated_at: "2026-07-08 14:13:48"
---

> Source: https://open.dingtalk.com/document/development/log-api-use-cases
> Path: 应用开发 / 服务端API / 日志 > 使用教程 > 三方系统发起和查看日志信息
> Updated: 2026-07-08 14:13:48

# 三方系统发起和查看日志信息

本文介绍了创建一个企业内部应用，使用**日志**提供的API，实现在第三方系统中直接发起钉钉日志。

> **[!NOTE]**
>
> 本流程的案例实现仅支持钉钉PC客户端内实现，手机端暂不支持。

## **前提条件**

1. 完成[应用创建与配置](../01-XOnnmGCTbn-开发指南/0007-create-application.md)的流程。
2. 申请[接口调用权限](0003-add-api-permission.md)，在权限搜索框分别输入`qyapi_report_query`和`qyapi_report_manage`，并申请权限。

## 操作步骤

1. 获取应用访问凭证[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)。调用接口时，通过accessToken鉴权调用者身份。
2. 手动在钉钉的日志中创建一个日志模板。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5600089071/p776197.png)
3. 调用[保存日志内容](0295-save-custom-log-content.md)接口，获取contentId。
4. 拼接URL，在三方系统页面内访问该URL，可以跳转进入日志发起页面，拼接的URL如下

   ```
   dingtalk://dingtalkclient/action/openapp?corpid={corpid}
   &container_type=work_platform
     &app_id=2
     &redirect_type=jump
     &redirect_url="+encodeURIComponent("https://landray.dingtalkapps.com/alid/app/reportpc/createreport.html?corpid={corpid}&templateid={templateid}&contentid={contentid}&callbackUrl={callback_url}&dd_from=ThirdParty")
   ```

   1. **URL参数说明**

      - corpId：该日志模板所在企业的CorpId，登录[钉钉开发者后台](https://open-dev.dingtalk.com/)获取。
      - container\_type：固定值work\_platform。
      - app\_id：固定值2。
      - templateid：日志模板Id，调用[获取模板详情](0296-query-template-details.md)接口获取。
      - contentid：调用[保存日志内容](0295-save-custom-log-content.md)接口返回的contentId。
      - redirect\_url：跳转的日志提交页面地址，**必须encodeURL处理**。
      - callbackUrl：第三方自己提供的回调的url，用于用户提交日志成功之后，通知第三方生成的日志ID，第三方可以基于此ID拼接成日志详情页的url，可以关联到钉钉里面的日志详情。(回调的url由企业自己提供，钉钉日志前端在提交日志时会带上这个url，服务端在提交日志成功之后触发回调。)
      - dd\_from：固定为ThirdParty。
   2. **callbackUrl的说明**

      提交日志成功时，钉钉服务器会以GET请求的方式，请求构造的回调URL

      例如，开发者构造的回调URL为http://www.dingtalk.com/callback，提交日志时，钉钉服务器的请求为

      ```
      GET  http://www.dingtalk.com/callback?reportId=17d6xxxxxx
      ```

      开发者构造回调URL的示例如下

      ```
      @RestController
      public class reportCallBack {
          @RequestMapping(value = "/callback",method = RequestMethod.GET)
          public void report(@RequestParam(value = "reportId")String reportId){
              System.out.println(reportId);
          }
      }
      ```
5. 拼接好的URL，在企业自有系统内访问跳转，即可打开钉钉填写日志页面，如下图所示。

   ![同步日志](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3244199951/p162640.png)
6. 主体流程图示说明。

   ![编辑后在发送流程](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8221943871/p162641.png)

## 场景一：编辑后再发送

### **主体流程**

主体流程是在企业内部系统中，点击“生成周报”的时候：

1. 获取要生成的模板的详情，根据模板和周报内容组装对应的内容，并调用开放平台的接口上传内容，开放平台会返回对应的contentId。
2. 拼接写日志页面的url，跳转到钉钉日志的写日志页面。
3. 在写日志页面进行编辑（可选），选择接收人后进行发送。
4. 发送完，触发对应企业的回调url，通知已发出的日志id。

调用流程图如下：![编辑后在发送流程](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8221943871/p162641.png)

> **[!NOTE]**
>
> 开放平台已开通上传图片接口。

### **回调URL**

企业保存完日志内容后，点击跳转到钉钉的URL完整的格式如下：

```
dingtalk://dingtalkclient/action/openapp?corpid={corpid}&container_type=work_platform&app_id=2&redirect_type=jump&redirect_url="+ encodeURIComponent("https://landray.dingtalkapps.com/alid/app/reportpc/createreport.html?corpid={corpid}&templateid={templateid}&contentid={contentid}&callbackUrl={callback_url}&dd_from=ThirdParty")
```

- corpId：企业的corpId。
- templateid：日志模板ID。
- contentid：保存内容后返回的contentId。
- callbackUrl：第三方自己提供的回调的url，用于用户提交日志成功之后，通知第三方生成的日志id，第三方可以基于此id拼接成日志详情页的url，可以关联到钉钉里面的日志详情。(回调的url由企业自己提供，钉钉日志前端在提交日志时会带上这个url，服务端在提交日志成功之后触发回调。)
- dd\_from：固定为ThirdParty。

## 场景二：直接发送

日志集成后，在企业内部系统中，点击“生成周报”时：

1. 后端先调用开放平台接口获取模板详情。
2. 调用开放平台接口上传周报中的图片，获取上传图片后的mediaId。
3. 根据模板字段组装日志内容(包括上传图片后的mediaId)，再调用开放平台接口创建日志。
4. 钉钉日志创建并发送完日志后，会返回对应的日志id。

调用流程图如下：

![直接发送流程](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8221943871/p162647.png)

## **场景三：查看日志阅读情况**

获取日志的阅读情况，包含已读人数、评论条数、评论人数和点赞人数等，并供企业员工查看。

1. 企业开通日志，员工使用日志并提交周报、日报等。
2. 各部门日志填报完成后，企业内部可以通过[数据资产平台](../../07-数据资产/01-fIz0pQ6X4y-平台介绍/0001-dataopen-overview.md)获取日志相关数据。
