---
title: "入驻聚石塔"
source_url: "https://open.dingtalk.com/document/development/create-tmallcloud-account"
namespace: "development"
slug: "create-tmallcloud-account"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "历史文档（不推荐） > RDS推送/SyncHTTP推送 > 聚石塔 > 入驻聚石塔"
doc_id: "doc_e24894ae988a473b"
updated_at: "2026-08-27 12:31:33"
---

> Source: https://open.dingtalk.com/document/development/create-tmallcloud-account
> Path: 应用开发 / 事件订阅 / 历史文档（不推荐） > RDS推送/SyncHTTP推送 > 聚石塔 > 入驻聚石塔
> Updated: 2026-08-27 12:31:33

# 入驻聚石塔

产品方案商需要先将钉钉账号和聚石塔绑定，然后才可以在聚石塔购买用于应用部署的资源。

> **[!IMPORTANT]**
>
> - 如果开发者后台没有聚石塔入口，需要确认当前企业是否入驻为钉钉产品方案商，入驻成功后，就会显示聚石塔入口。
> - 钉钉云和聚石塔只能选择一个。
> - 如果要从钉钉云切换到聚石塔，请在开发者后台首页右下角提交工单。

## 入驻流程

钉钉产品方案商入驻聚石塔流程如下图所示：

![入驻聚石塔](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2848433061/p175431.png)

## 步骤一：申请淘宝企业账号

参考以下操作，申请淘宝企业账号。

1. 打开[淘宝网首页](https://www.taobao.com/)，点击**免费注册**。

   ![注册淘宝](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2848433061/p175483.png)
2. 单击**切换成企业账户注册**。

   ![切换企业账户注册](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3848433061/p175484.png)
3. 根据提示输入完成企业账号注册，需要在邮箱完成激活。

   ![企业注册信息](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3848433061/p175486.png)
4. 使用企业账号登录淘宝。

   ![淘宝登录页](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3848433061/p175488.png)
5. 单击**账号管理 > 支付宝绑定设置，**绑定企业支付宝账号。

   企业支付宝账号主要用于聚石塔上开发票的抬头。

   ![支付宝账号绑定](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3848433061/p175489.png)

## 步骤二：获取令牌

1. 使用**淘宝企业账号**登录[聚石塔](https://console.cloud.tmall.com/member/login)。

   ![登录聚石塔](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3848433061/p175490.png)
2. 查看聚石塔身份认证令牌，钉钉绑定聚石塔账号时需要使用。在聚石塔首页左侧导航栏，单击**权限管理**。

   ![权限管理](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3848433061/p175491.png)
3. 选择**访问控制 > 企业钉钉**查看企业令牌。

   > **[!IMPORTANT]**
   >
   > 如果是老的聚石塔账号，并且已经绑定过钉钉企业的话，需要在企业里把聚石塔小程序解除授权，然后才能看到认证令牌。

   ![企业令牌](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3848433061/p175492.png)

## 步骤三：绑定聚石塔账号

参考以下操作，在钉钉开发者后台绑定聚石塔账号：

1. 登录钉钉[开发者后台](https://open-dev.dingtalk.com/)，然后单击**聚石塔**。

   > **[!NOTE]**
   >
   > 如果开发者后台没有聚石塔入口，需要确认当前企业是否入驻为钉钉产品方案商，入驻成功后，就会显示聚石塔入口。

   ![聚石塔button](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3848433061/p175494.png)
2. 在**基础信息**页面，单击**登录聚石塔**。

   ![登录聚石塔开放平台](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3848433061/p175495.png)
3. 输入聚石塔身份令牌，然后单击**立即绑定**。

   ![绑定令牌](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3246204061/p177970.png)
4. 登录到聚石塔后，在**权限管理 > 成员管理**页面，单击**钉钉导入**添加其他需要登录到聚石塔进行开发的钉钉员工，并且设置相应的聚石塔操作权限。

   ![成员管理](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3910533061/p175668.png)

## 步骤四：使用钉钉账号登录聚石塔

1. 打开[聚石塔](https://console.cloud.tmall.com/member/login)，使用钉钉扫码后就可以登录聚石塔网站。

   ![聚石塔钉钉登录](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4848433061/p175497.png)
2. 登录成功后请选择钉钉业务域进行应用部署。

   ![钉钉业务](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3910533061/p175672.png)
