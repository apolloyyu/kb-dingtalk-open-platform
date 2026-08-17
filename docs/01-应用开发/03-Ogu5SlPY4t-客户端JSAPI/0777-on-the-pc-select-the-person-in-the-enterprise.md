---
title: "PC端选择企业内部的人"
source_url: "https://open.dingtalk.com/document/development/on-the-pc-select-the-person-in-the-enterprise"
namespace: "development"
slug: "on-the-pc-select-the-person-in-the-enterprise"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > H5微应用 > JSAPI参考 > 通讯录选人 > PC端选择企业内部的人"
doc_id: "8WgRzY8Fxm"
updated_at: "2025-09-17 20:56:17"
---

> Source: https://open.dingtalk.com/document/development/on-the-pc-select-the-person-in-the-enterprise
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > H5微应用 > JSAPI参考 > 通讯录选人 > PC端选择企业内部的人
> Updated: 2025-09-17 20:56:17

# PC端选择企业内部的人

调用**biz.contact.choose** PC端选择企业内部的人。

## 使用说明

此接口只能选人，不能选择部门。

| **客户端** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 不支持 | 不支持 | 支持 |

```
dd.biz.contact.choose({
    multiple: true, //是否多选：true多选 false单选； 默认true
    users: ['10001', '10002', ...], //默认选中的用户列表，员工userid；成功回调中应包含该信息
    corpId: 'dingb4ff1079f84f8d54', //企业id
    max: 10, //人数限制，当multiple为true才生效，可选范围1-1500
    onSuccess: function(data) {
    /* data结构
      [{
        "name": "张三", //姓名
        "avatar": "
http://g.alicdn.com/avatar/zhangsan.png
" //头像图片url，可能为空
        "emplId": '0573', //员工userid
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
| multiple | Boolean | 是否多选：   - **true**（默认）：多选 - **false**：单选 |
| users | Array[String] | 默认选中的用户userid列表；成功回调中应包含该信息。 |
| corpId | String | 企业的corpid。 |
| max | Number | 人数限制，当**multiple**为**true**才生效，可选范围1-1500。 |

## 返回结果

| 参数 | 说明 |
| --- | --- |
| name | 姓名。 |
| avatar | 头像图片url，可能为空。 |
| emplId | 员工userid。 |
