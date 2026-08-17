---
title: "选取手机通讯录"
source_url: "https://open.dingtalk.com/document/development/select-phone-address-book"
namespace: "development"
slug: "select-phone-address-book"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > H5微应用 > JSAPI参考 > 通讯录选人 > 选取手机通讯录"
doc_id: "h9HxMPmPla"
updated_at: "2025-09-17 20:56:16"
---

> Source: https://open.dingtalk.com/document/development/select-phone-address-book
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > H5微应用 > JSAPI参考 > 通讯录选人 > 选取手机通讯录
> Updated: 2025-09-17 20:56:16

# 选取手机通讯录

调用**biz.contact.chooseMobileContacts**选取手机通讯录。

## 调试

访问[JSAPI Explorer](https://open-dev.dingtalk.com/apiExplorer#/jsapi?api=biz.contact.chooseMobileContacts)在线调试该接口。

## 使用说明

此接口用于选取用户的手机联系人。

| **客户端** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 支持 | 支持 | 不支持 |

```
dd.biz.contact.chooseMobileContacts({
  multiple: Boolean, //是否多选： true多选 false单选； 默认true
  maxUsers: Number, //人数限制，当multiple为true才生效，可选范围1-1500
  limitTips:"xxx", //超过人数限制的提示语可以用这个字段自定义
  title : "xxx", // 如果你需要修改选人页面的title，可以在这里赋值 
  onSuccess: function(data) {
  //onSuccess将在选人结束，点击确定按钮的时候被回调
  /* data结构
    [{
      "name": "张三", //姓名
      "mobile": "110" //用户手机号
      "mediaId": 'RSDFS', //用户头像id
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
| title | String | 选择页面的标题。 |
| multiple | Boolean | 是否多选：   - **true**（默认）：多选 - **false**：单选 |
| maxUsers | Number | 人数限制，当**multiple**为**true**才生效，可选范围1-1500。 |
| limitTips | String | 超出选人的人数限制之后的提示。 |

## 返回结果

| 参数 | 说明 |
| --- | --- |
| name | 姓名。 |
| mediaId | 头像图片id，可能为空。 |
| mobile | 用户手机号。 |

展示效果如下图所示：

> **[!IMPORTANT]**
>
>  Android端和iOS端不同系统展示结果可能会出现差别，请以最终的展示效果为准。

![通讯录选人 ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9505834061/p177816.png)
