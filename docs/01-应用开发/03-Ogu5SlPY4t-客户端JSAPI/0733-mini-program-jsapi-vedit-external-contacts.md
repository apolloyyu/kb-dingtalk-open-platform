---
title: "编辑外部联系人"
source_url: "https://open.dingtalk.com/document/development/mini-program-jsapi-vedit-external-contacts"
namespace: "development"
slug: "mini-program-jsapi-vedit-external-contacts"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 开放接口 > 通讯录选人 > 编辑外部联系人"
doc_id: "BBvBiNCwde"
updated_at: "2025-09-17 21:01:11"
---

> Source: https://open.dingtalk.com/document/development/mini-program-jsapi-vedit-external-contacts
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 开放接口 > 通讯录选人 > 编辑外部联系人
> Updated: 2025-09-17 21:01:11

# 编辑外部联系人

调用**dd.editExternalUser**编辑外部联系人。

## 示例代码

```
dd.editExternalUser({
    title:"测试标题",//标题
    emplId:"",//需要编辑的员工id，不填，则为新增外部联系人
    name:"",//需要新增的外部联系人的名字
    mobile:"",//需要预填的手机号
    companyName:"",//需要预填的公司名
    deptName:"",//预填部门名字
    job:"",//预填职位
    remark:"",//备注信息
    success:function(res){
      /* res结构
      {
          "userId":"",//需要编辑的员工id，不填，则为新增外部联系人
          "name":"",//需要新增的外部联系人的名字，emplId为空时生效
          "mobile":"",//需要预填的手机号，emplId为空时生效
          "companyName":"",//需要预填的公司名，emplId为空时生效
          "deptName":"",//预填部门名字，emplId为空时生效
          "job":"",//预填职位，emplId为空时生效
          "remark":""//备注信息，emplId为空时生效
      }
      */
    },
    fail:function(err){}
});
```

## 入参

| **参数** | **类型** | **说明** |
| --- | --- | --- |
| title | String | 标题。 |
| emplId | String | 需要编辑的外部联系人的userid；不填，则为新增外部联系人。 |
| name | String | 需要新增的外部联系人的名字。 |
| mobile | String | 需要预填的手机号。 |
| companyName | String | 需要预填的公司名。 |
| deptName | String | 预填部门名字。 |
| job | String | 预填职位。 |
| remark | String | 备注信息。 |

## 返回结果

| **参数** | **说明** |
| --- | --- |
| userId | 外部联系人的userid。 |
| name | 外部联系人的姓名。 |
| mobile | 外部联系人的电话。 |
| companyName | 外部联系人的的公司名。 |
| deptName | 外部联系人的部门。 |
| job | 外部联系人的职位。 |
| remark | 外部联系人的备注信息。 |
