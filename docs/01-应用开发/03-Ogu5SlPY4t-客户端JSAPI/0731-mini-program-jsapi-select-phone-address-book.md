---
title: "选取手机通讯录"
source_url: "https://open.dingtalk.com/document/development/mini-program-jsapi-select-phone-address-book"
namespace: "development"
slug: "mini-program-jsapi-select-phone-address-book"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 开放接口 > 通讯录选人 > 选取手机通讯录"
doc_id: "g4Zrv5K756"
updated_at: "2025-09-17 21:01:10"
---

> Source: https://open.dingtalk.com/document/development/mini-program-jsapi-select-phone-address-book
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 开放接口 > 通讯录选人 > 选取手机通讯录
> Updated: 2025-09-17 21:01:10

# 选取手机通讯录

调用**dd.choosePhonebook**选取用户手机联系人。

## 示例代码

```
dd.choosePhonebook({
  multiple: Boolean, //是否多选： true多选 false单选； 默认true
  maxUsers: Number, //人数限制，当multiple为true才生效，可选范围1-1500
  limitTips:"xxx", //超过人数限制的提示语可以用这个字段自定义
  title : "xxx", // 如果你需要修改选人页面的title，可以在这里赋值
  success:function(res){
    //onSuccess将在选人结束，点击确定按钮的时候被回调
    /* res结构
    [{
      "name": "张三", //姓名
      "mobile": "110", //用户手机号
      "avatar": 'RSDFS', //用户头像id
     },
     ...
    ]
    */      
  },
  fail:function(err){
  } 
});
```

## 入参

| **参数** | **类型** | **说明** |
| --- | --- | --- |
| multiple | Boolean | 是否多选。   - **true**：多选 - **false**：单选   **默认值**：**true**。 |
| maxUsers | Number | 人数限制，当multiple为true才生效，可选范围1-1500。 |
| limitTips | String | 超过人数限制的提示语可以用这个字段自定义。 |
| title | String | 如果你需要修改选人页面的title，可以在这里赋值。 |

## 返回结果

| **参数** | **说明** |
| --- | --- |
| name | 姓名。 |
| avatar | 头像图片id，可能为空。 |
| mobile | 用户手机号。 |
