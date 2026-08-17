---
title: "打开应用内页面"
source_url: "https://open.dingtalk.com/document/development/open-the-in-application-page"
namespace: "development"
slug: "open-the-in-application-page"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > H5微应用 > JSAPI参考 > 打开新页面 > 打开应用内页面"
doc_id: "d0SrfLvri3"
updated_at: "2025-09-17 20:57:26"
---

> Source: https://open.dingtalk.com/document/development/open-the-in-application-page
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > H5微应用 > JSAPI参考 > 打开新页面 > 打开应用内页面
> Updated: 2025-09-17 20:57:26

# 打开应用内页面

调用**biz.util.open**打开应用内页面。

## 调试

访问[JSAPI Explorer](https://open-dev.dingtalk.com/apiExplorer#/jsapi?api=biz.util.open)在线调试该接口。

## 使用说明

| **客户端** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 支持 | 支持 | 支持 (**PC端仅支持打开个人资料页)** |

```
dd.biz.util.open({
    name:String,//页面名称
    params:JSONObject,//传参
    onSuccess : function() {
        /**/
    },
    onFail : function(err) {}
});
```

## 参数说明

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| name | String | 页面名称。 |
| params | JSONObject | 传参。 |

目前支持以下页面，具体参数示例如下：

- **个人资料页**

  ```
  // 页面名称：
    profile
  // 传参：
      id:用户userId //String
      corpId:'' //企业id
  ```
- **聊天页面**

  ```
  // 页面名称：
      chat
  // 传参：
      users: ['123'] 用户列表,工号
      corpId: '' //企业id
  ```
- **免费电话页面**

  ```
  // 页面名称：
      call
  // 传参：
  ```
- **联系人添加页面**

  ```
  // 页面名称：
      contactAdd
  // 传参：
  ```
- **唤起添加好友页面**

  ```
  // 页面名称：
      friendAdd
  // 传参：
  ```
- **唤起员工管理页面**

  ```
  // 页面名称：
      manageOrg
  // 传参：
  "corpId":"dingd90ce2ec337f2f13", "isManager": "true"
  ```
