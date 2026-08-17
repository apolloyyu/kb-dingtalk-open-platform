---
title: "单选自定义联系人"
source_url: "https://open.dingtalk.com/document/development/mini-program-jsapi-custom-radio-contact"
namespace: "development"
slug: "mini-program-jsapi-custom-radio-contact"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 开放接口 > 通讯录选人 > 单选自定义联系人"
doc_id: "rFdqat0Qrk"
updated_at: "2025-09-17 21:01:12"
---

> Source: https://open.dingtalk.com/document/development/mini-program-jsapi-custom-radio-contact
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 开放接口 > 通讯录选人 > 单选自定义联系人
> Updated: 2025-09-17 21:01:12

# 单选自定义联系人

调用**dd.chooseUserFromList**选取单个自定义联系人。

## 示例代码

```
dd.chooseUserFromList({
    title: '选人的标题', //标题
    users: ['10001', '10002', ...],//一组员工userid
    isShowCompanyName: true,   //true|false，默认为 false
    disabledUsers: ["78308"], //不能选的人
    success:function(res){
     /* res结构
      [{
        "name": "张三", //姓名
        "avatar": "http://g.alicdn.com/avatar/zhangsan.png", //头像图片url，可能为空
        "userId": '0573'    
       },
       ...
      ]
     */
    },
    fail:function(err){}
});
```

## 入参

| **参数** | **类型** | **说明** |
| --- | --- | --- |
| users | String[] | 一组员工userId。 |
| isShowCompanyName | Boolean | 是否显示公司名称。 |
| title | String | 标题。 |
| disabledUsers | String[] | 不能选择的人；PC端不支持此参数。 |

## 返回结果

| **参数** | **说明** |
| --- | --- |
| name | 姓名。 |
| avatar | 头像图片url，可能为空。 |
| userId | 即员工userid。 |
