---
title: "选人与部门"
source_url: "https://open.dingtalk.com/document/development/candidates-and-departments"
namespace: "development"
slug: "candidates-and-departments"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 开放接口 > 通讯录选人 > 选人与部门"
doc_id: "n2ZicjJuMk"
updated_at: "2025-09-17 21:01:08"
---

> Source: https://open.dingtalk.com/document/development/candidates-and-departments
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 开放接口 > 通讯录选人 > 选人与部门
> Updated: 2025-09-17 21:01:08

# 选人与部门

调用**dd.complexChoose**选择人和部门，选择部门后把该部门转换成对应部门下的人。

## 示例代码

```
dd.complexChoose({
    title:"测试标题",            //标题
    multiple:true,            //是否多选
    limitTips:"超出了",          //超过限定人数返回提示
    maxUsers:1000,            //最大可选人数
    pickedUsers:[],            //已选用户，值为userId列表
    pickedDepartments:[],          //已选的部门id
    disabledUsers:[],            //不可选用户，值为userId列表
    disabledDepartments:[],        //不可选部门id
    requiredUsers:[],            //必选用户（不可取消选中状态）
    requiredDepartments:[],        //必选部门（不可取消选中状态）
    permissionType:"xxx",          //可添加权限校验，选人权限，目前只有GLOBAL这个参数
    responseUserOnly:false,        //返回人，或者返回人和部门
    success:function(res){
        /**
        {
            "selectedCount":1, //选择人数
            "users":[{"name":"xxx","avatar":"xxx","userId":"xxx"}], //返回选人的列表，列表中的对象包含name（用户名），avatar（用户头像），userId（用户工号）三个字段
            "departments":[{"id":123,"name":"xxx","count":1}] //返回已选部门列表，列表中每个对象包含id（部门id）、name（部门名称）、number（部门人数）
        }
        */    
    },
    fail:function(err){
    }
})
```

## 入参

| **参数** | **类型** | **说明** |
| --- | --- | --- |
| title | String | 标题。 |
| multiple | Boolean | 是否多选：   - **true** - **false** |
| limitTips | String | 超过限定人数返回提示。 |
| maxUsers | Number | 最大可选人数。 |
| pickedUsers | String[] | 已选用户，值为userId列表。 |
| pickedDepartments | String[] | 已选的部门id。 |
| disabledUsers | String[] | 不可选用户，值为userId列表。 |
| disabledDepartments | String[] | 不可选部门id。 |
| requiredUsers | String[] | 必选用户（不可取消选中状态），值为userid列表。 |
| requiredDepartments | String[] | 必选部门（不可取消选中状态）。 |
| permissionType | String | 选人权限，目前只有GLOBAL这个参数。 |
| responseUserOnly | Boolean | 接口返回的信息中是否包含人员或部门信息（在选人页面搜索姓名返回内容和此字段无关）。   - **true**：返回人员信息。 - **false**：返回人员和部门信息。 |
| startWithDepartmentId | Number | 仅支持0和-1两个值：   - **0**：表示从企业最上层开始。 - **-1**：表示从自己部门开始，为-1时仅在Android端生效。 |

## 返回结果

| **参数** | 类型 | **说明** |
| --- | --- | --- |
| selectedCount | Number | 选择人数。 |
| users | String[] | 返回选人的列表，列表中的对象包含name（用户名）、avatar（用户头像）、userId（用户工号）三个字段。 |
| departments | String[] | 返回已选部门列表，列表中每个对象包含id（部门id）、name（部门名称）、count（部门人数）。 |
