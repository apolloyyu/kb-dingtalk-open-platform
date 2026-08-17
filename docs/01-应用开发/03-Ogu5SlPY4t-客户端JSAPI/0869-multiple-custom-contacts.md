---
title: "多选自定义联系人"
source_url: "https://open.dingtalk.com/document/development/multiple-custom-contacts"
namespace: "development"
slug: "multiple-custom-contacts"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > H5微应用 > JSAPI参考 > 自定义联系人 > 多选自定义联系人"
doc_id: "YlDKg2JFV9"
updated_at: "2025-09-17 20:57:25"
---

> Source: https://open.dingtalk.com/document/development/multiple-custom-contacts
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > H5微应用 > JSAPI参考 > 自定义联系人 > 多选自定义联系人
> Updated: 2025-09-17 20:57:25

# 多选自定义联系人

调用**biz.customContact.multipleChoose**多选自定义联系人。

## 调试

访问[JSAPI Explorer](https://open-dev.dingtalk.com/apiExplorer#/jsapi?api=biz.customContact.multipleChoose)在线调试该接口。

## 使用说明

选取多个自定义联系人。

| **客户端** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 支持 | 支持 | 支持 |

```
dd.biz.customContact.multipleChoose({
    title: '多选人的标题', //标题
    users: ['10001', '10002', ...],//一组员工工号
    corpId: 'dingb4ff1079f84f8d54',//企业 ID，
    isShowCompanyName: false,   //true|false，默认为 false
    selectedUsers: ["18658"], //默认选中的人，注意:已选中不可以取消
    disabledUsers: ["78308"], //不能选的人
    max: 10, //人数限制
    onSuccess: function(data) {
    /* data结构
      [{
        "name": "张三", //姓名
        "avatar": "http://g.alicdn.com/avatar/zhangsan.png" //头像图片url，可能为空
        "emplId": '0573', //工号
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
| corpId | String | 企业的corpid。 |
| users | Array[String] | 员工列表。 |
| isShowCompanyName | Boolean | 是否显示公司名称。 |
| title | String | 标题。 |
| selectedUsers | Array[String] | 默认选中的人。  **[!NOTE]**  已选中不可以取消。 |
| disabledUsers | Array[String] | 不能选中的人。 |
| max | Number | 人数限制。 |

## 返回结果

| 参数 | 说明 |
| --- | --- |
| name | 姓名。 |
| avatar | 头像图片url，可能为空。 |
| emplId | 员工的userid。 |
