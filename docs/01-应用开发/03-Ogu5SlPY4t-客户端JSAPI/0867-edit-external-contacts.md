---
title: "编辑外部联系人"
source_url: "https://open.dingtalk.com/document/development/edit-external-contacts"
namespace: "development"
slug: "edit-external-contacts"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > H5微应用 > JSAPI参考 > 外部联系人 > 编辑外部联系人"
doc_id: "cufXOGQl8w"
updated_at: "2025-09-17 20:57:23"
---

> Source: https://open.dingtalk.com/document/development/edit-external-contacts
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > H5微应用 > JSAPI参考 > 外部联系人 > 编辑外部联系人
> Updated: 2025-09-17 20:57:23

# 编辑外部联系人

调用**biz.contact.externalEditForm**编辑外部联系人。

## **效果示例**

![iShot2022-11-08 10](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3607892761/p514493.png)

## 使用说明

调用本接口前，请先引入钉钉js，参考[准备工作](https://open.dingtalk.com/document/orgapp/read-before-development)。

| **客户端** | **是否需要鉴权** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- | --- |
| 支持说明 | 需要 | 支持 | 支持 | 不支持 |

```
dd.biz.contact.externalEditForm({
    "title":"测试标题",//标题
    "corpId":"xxx",//当前企业的corpId
    "emplId":"",//需要编辑的外部联系人userId，不填，则为新增外部联系人
    "name":"",//需要新增的外部联系人的名字，emplId为空时生效
    "mobile":"",//需要新增外部联系人的手机号，emplId为空时生效
    "companyName":"",//需要新增外部联系人的公司名，emplId为空时生效
    "deptName":"",//需要新增外部联系人的部门名字，emplId为空时生效
    "job":"",//需要新增外部联系人的职位，emplId为空时生效
    "remark":""//需要新增外部联系人的备注信息，emplId为空时生效
         onSuccess: function(data) {
        /* data结构
    {
     "emplId":"",//需要编辑的员工id，不填，则为新增外部联系人
     "name":"",//需要新增的外部联系人的名字，emplID为空时生效
     "mobile":"",//需要预填的手机号，emplID为空时生效
    "companyName":"",//需要预填的公司名，emplID为空时生效
    "deptName":"",//预填部门名字，emplID为空时生效
    "job":"",//预填职位，emplID为空时生效
    "remark":""//备注信息，emplID为空时生效
    }
        */
        },
        onFail : function(err) {}
});
```

## 参数说明

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| title | String | 标题。 |
| corpId | String | 企业的corpid，请参考[基础概念-CorpId](https://open.dingtalk.com/document/orgapp/basic-concepts)。 |
| emplId | String | 需要编辑的外部联系人的userId，不填，则为新增外部联系人。 |
| name | String | 需要新增的外部联系人的名字。 |
| mobile | String | 需要新增的外部联系人的手机号。 |
| companyName | String | 需要新增的外部联系人的公司名。 |
| deptName | String | 新增的外部联系人部门名字。 |
| job | String | 新增的外部联系人职位。 |
| remark | String | 新增的外部联系人备注信息。 |

## 返回结果

| 参数 | 说明 |
| --- | --- |
| emplId | 外部联系人的userId。 |
| name | 外部联系人的名字。 |
| mobile | 手机号。 |
| companyName | 公司名。 |
| deptName | 部门。 |
| job | 职位。 |
| remark | 备注信息。 |
