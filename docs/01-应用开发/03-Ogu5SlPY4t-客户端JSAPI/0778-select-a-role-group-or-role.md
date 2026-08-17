---
title: "选择角色组或角色"
source_url: "https://open.dingtalk.com/document/development/select-a-role-group-or-role"
namespace: "development"
slug: "select-a-role-group-or-role"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > H5微应用 > JSAPI参考 > 角色 > 选择角色组或角色"
doc_id: "x0gyoU1OG9"
updated_at: "2025-09-17 20:56:18"
---

> Source: https://open.dingtalk.com/document/development/select-a-role-group-or-role
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > H5微应用 > JSAPI参考 > 角色 > 选择角色组或角色
> Updated: 2025-09-17 20:56:18

# 选择角色组或角色

调用biz.contact.rolesPicker选择用户所在的某个企业中的角色。

![iShot2022-01-13 17](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4674602461/p384501.png)

## 使用说明

| 客户端 | Android | iOS | PC | 是否需要鉴权 |
| --- | --- | --- | --- | --- |
| 支持说明 | 支持 | 支持 | 不支持 | 需要 |

```
dd.biz.contact.rolesPicker ({
  "corpId":"xxxxxxxx",
  "title":"请选择角色",
  "limitTips":"最多可选择10个角色",
  "maxRoles":10
  onSuccess:function(result) {
  },
  onFail:function(err) {
  }
})
```

## 参数说明

| 参数 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| corpId | String | 是 | 企业的corpId。 |
| maxRoles | Number | 否 | 最多可选择多少个。  **[!NOTE]**  如果入参超过5000个，会按5000来处理。 |
| limitTips | String | 否 | 用户选择的角色数超过**maxRoles**时的提示文案。 |
| title | String | 否 | 组件的页面title。 |

## 返回结果

### 成功

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| roles | Array<Map<name, roleId>> | 调用成功后返回的角色列表。 |

### 失败

| 名称 | 描述 |
| --- | --- |
| -1 | 用户取消 |
| 2 | 无效的corpId |
| 4 | 横屏调用（不支持横屏） |
| 7 | jsapi接口无权限 |

### 返回示例

```
{
    "roles": [
        {
            "name": "出纳",
            "roleId": 525940602
        },
        {
            "name": "默认",
            "roleId": 525940594
        },
        {
            "name": "财务",
            "roleId": 525940600
        },
        {
            "name": "经理",
            "roleId": 525940612
        },
        {
            "name": "人事",
            "roleId": 525940601
        }
    ]
}
```
