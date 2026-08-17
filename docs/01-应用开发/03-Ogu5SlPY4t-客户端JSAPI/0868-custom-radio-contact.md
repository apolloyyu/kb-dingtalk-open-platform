---
title: "单选自定义联系人"
source_url: "https://open.dingtalk.com/document/development/custom-radio-contact"
namespace: "development"
slug: "custom-radio-contact"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > H5微应用 > JSAPI参考 > 自定义联系人 > 单选自定义联系人"
doc_id: "kRmZC1sZe0"
updated_at: "2025-09-17 20:57:24"
---

> Source: https://open.dingtalk.com/document/development/custom-radio-contact
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > H5微应用 > JSAPI参考 > 自定义联系人 > 单选自定义联系人
> Updated: 2025-09-17 20:57:24

# 单选自定义联系人

调用**biz.customContact.choose，**可以自定义选择企业内员工或者外部联系人，支持单选。

## **效果示例**

![iShot2022-11-08 11](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5607892761/p514585.png)

## 调试

访问[JSAPI Explorer](https://open-dev.dingtalk.com/apiExplorer#/jsapi?api=biz.customContact.choose)在线调试该接口。

## 使用说明

调用本接口前，请先引入钉钉js，参考[准备工作](https://open.dingtalk.com/document/orgapp/read-before-development)。

选取单个自定义联系人。

| **客户端** | **是否需要鉴权** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- | --- |
| 支持说明 | 需要 | 支持 | 支持 | 支持 |

```
dd.biz.customContact.choose({
    title: '选人的标题', //标题
    users: ['10001', '10002', ...],//一组员工userId，可以是外部联系人也可以是企业内部员工userId
    corpId: 'dingb4ffxxxxx',//企业corpID，
    isShowCompanyName: true,   //true|false，默认为 false
    disabledUsers: ["78308"], //不能选的人
    onSuccess: function(data) {
    /* data结构
      [{
        "name": "张三", //姓名
        "avatar": "http://g.alicdn.com/avatar/zhangsan.png" //头像图片url，可能为空
        "emplId": '0573', //即被选员工的userId

       },
       ...
      ]
    */
    },
    onFail : function(err) {}
});
```

## 参数说明

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| corpId | String | 企业的corpid，请参考[基础概念-CorpId](https://open.dingtalk.com/document/orgapp/basic-concepts)。 |
| users | Array[String] | 员工列表。 |
| isShowCompanyName | Boolean | 是否显示公司名称。   - true：显示 - false：不显示 |
| title | String | 页面标题。 |

## 返回结果

| 参数 | 说明 |
| --- | --- |
| name | 被选人的姓名。 |
| avatar | 被选人的头像图片url，可能为空。 |
| emplId | 被选人的userId。 |
