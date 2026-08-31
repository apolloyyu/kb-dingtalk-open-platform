---
title: "complexChoose"
source_url: "https://open.dingtalk.com/document/development/jsapi-complex-choose"
namespace: "development"
slug: "jsapi-complex-choose"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "通讯录 > complexChoose"
doc_id: "CucGIH88i7"
updated_at: "2025-08-27 18:08:42"
---

> Source: https://open.dingtalk.com/document/development/jsapi-complex-choose
> Path: 应用开发 / 客户端 JSAPI / 通讯录 > complexChoose
> Updated: 2025-08-27 18:08:42

# complexChoose

调用complexChoose，选择人和部门。

![](https://gw.alicdn.com/imgextra/i1/O1CN01kfcX9r24hmoE66zrS_!!6000000007423-0-tps-536-1020.jpg)

支持选择企业关联的上下游组织

![](https://gw.alicdn.com/imgextra/i2/O1CN01POFp0q1yNjmI18vRD_!!6000000006567-0-tps-1164-1032.jpg)

## 支持说明

| 应用能力 | Android | iOS | Harmony | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 6.0.0 | 6.0.0 | 7.0.0 | 6.0.0 | 6.0.0 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10309) |
| 小程序 | 6.0.0 | 6.0.0 | 7.0.0 | 6.0.0 | 6.0.0 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10309) |

## 支持应用类型

| 应用类型 | 是否支持调用 |
| --- | --- |
| 企业内部应用 | 是 |
| 第三方企业应用 | 是 |
| 第三方个人应用 | 是 |

## 鉴权规则

在H5应用中，调用[dd.config](https://open.dingtalk.com/document/orgapp/jsapi-authentication)完成鉴权后使用

在小程序应用中，无需鉴权即可直接调用

## **参数说明**

继承[通用输入对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性描述：

### 入参

- `corpId`（string）：企业id。
- `rootPage`（string）：初始页面是组织架构或组织列表页，默认为组织架构页（如示例图1）。可选填CommonOrgContact，组织列表页（如示例图2）。  
    
  > 此场景下corpId选填。
- `showLabelPick`（boolean）：组织列表上是否展示按角色选择（如示例图2）。  
  > PC 端暂不支持该参数。
- `showOrgEcological`（boolean）：组织列表上是否展示组织关联的上下游组织入口（如 示例图2 框选入口）。
- `filterOrgEcological`（boolean）：显示指定企业的上下游组织列表（如示例图3）。  
    
  > 请同时设置rootPage=CommonOrgContact，corpId必填。
- `requiredDepartments`（array）：必选部门 (不可取消选中状态)。
- `appId`（string）：三方应用使用appId，企业内部应用使用agentId。
- `title`（string）：选择页面的标题。
- `multiple`（boolean）：是否可多选：  
    
  \* true: 可多选  
  \* false：仅单选  
    
  > 默认仅单选（false）。
- `limitTips`（string）：超过限定人数返回的提示内容。
- `maxUsers`（number）：最大可选人数，最大值为10000。
- `pickedUsers`（array）：已选用户的userId列表。  
  > 当`multiple`字段为false仅单选状态时，pickedUsers字段移动端不支持。
- `pickedDepartments`（array）：已选的部门id列表。
- `disabledUsers`（array）：不可选用户的userId列表。
- `disabledDepartments`（array）：不可选部门id列表。
- `requiredUsers`（array）：必选用户 (不可取消选中状态)。
- `responseUserOnly`（boolean）：是否仅返回人员信息：  
    
  \* true：仅返回人员信息  
  \* false：返回人员和部门信息  
    
  > 默认为false。
- `startWithDepartmentId`（string）：选择部门和人时的开始位置  
    
  \* 0：表示从企业根目录开始  
  \* -1：表示从自己所在部门开始  
    
  > 该参数只支持Android端，IOS端可使用deptId参数。
- `deptId`（string）：选择部门和人时的开始位置：  
    
  \* -1：表示从企业根目录部门开始  
  \* 0：表示从自己所在的部门开始  
    
  > 该参数只支持IOS端，Android端可使用startWithDepartmentId参数。

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性描述：

### 入参

- `users`（array，必填）
- `users[].name`（string，必填）：用户名
- `users[].avatar`（string，必填）：用户头像
- `users[].emplId`（string，必填）：用户工号
- `departments`（array，必填）
- `departments[].id`（string，必填）：部门id
- `departments[].number`（number，必填）：部门人数
- `departments[].name`（string，必填）：部门名称
- `selectedCount`（number，必填）：已选部门下的总人数和已选用户数的总和

## **示例****代码**

### 默认出入参

```
dd.complexChoose({
  appId: '013324',
  title: '选择员工',
  corpId: 'ding1234xxxxx',
  deptId: '0987',
  maxUsers: 100,
  multiple: true,
  rootPage: `rootPage示例值`,
  limitTips: '选择人数不能超过20个',
  pickedUsers: ['userId0', 'userId2'],
  disabledUsers: ['userId0', 'userId2'],
  requiredUsers: ['userId0', 'userId2'],
  showLabelPick: true,
  responseUserOnly: true,
  pickedDepartments: ['deptId0', 'deptId1'],
  showOrgEcological: false,
  disabledDepartments: ['deptId0', 'deptId1'],
  filterOrgEcological: false,
  requiredDepartments: ['deptId0', 'deptId1'],
  startWithDepartmentId: '0332',
  success: (res) => {
    const { users, departments, selectedCount } = res;
  },
  fail: () => {},
  complete: () => {},
});
```

`success`返回对象示例：

```
{
  "users": [
    {
      "name": "钉小二",
      "avatar": "https://static.dingtalk.com/media/lADPDiCpu12oVqvNApTNApQ_660_660.jpg",
      "emplId": "22055215283702319x"
    }
  ],
  "departments": [{ "id": "68094649x", "name": "人事部", "number": 10 }],
  "selectedCount": 4
}
```
