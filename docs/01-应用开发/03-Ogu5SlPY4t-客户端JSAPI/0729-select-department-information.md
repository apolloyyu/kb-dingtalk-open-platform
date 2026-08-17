---
title: "选择部门信息"
source_url: "https://open.dingtalk.com/document/development/select-department-information"
namespace: "development"
slug: "select-department-information"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 开放接口 > 通讯录选人 > 选择部门信息"
doc_id: "IAByPIwPDU"
updated_at: "2025-09-17 21:01:09"
---

> Source: https://open.dingtalk.com/document/development/select-department-information
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 开放接口 > 通讯录选人 > 选择部门信息
> Updated: 2025-09-17 21:01:09

# 选择部门信息

调用**dd.chooseDepartments**返回部门的信息，是以部门为纬度，不是以人为纬度。

## 示例代码

```
dd.chooseDepartments({
    title:"测试标题",            //标题
    multiple:true,            //是否多选
    limitTips:"超出了",          //超过限定人数返回提示
    maxDepartments:100,            //最大选择部门数量
    pickedDepartments:[],          //已选的部门id
    disabledDepartments:[],        //不可选部门id
    requiredDepartments:[],        //必选部门（不可取消选中状态）
    permissionType:"xxx",          //选人权限，目前只有GLOBAL这个参数
    success:function(res){
        /**
        {
            "userCount":1, //选择人数
            "departmentsCount":1, //选择的部门数量
            "departments":[{"id":123,"name":"xxx","count":1}]//返回已选部门列表，列表中每个对象包含id（部门id）、name（部门名称）、count（部门人数）
        }
        */    
    },
    fail:function(err){
    }
});
```

## 入参

| **参数** | **类型** | **说明** |
| --- | --- | --- |
| title | String | 标题。 |
| multiple | Boolean | 是否多选：   - **true** - **false** |
| limitTips | String | 超过限定人数返回提示。 |
| maxDepartments | Number | 最大可选部门数。 |
| pickedDepartments | String[] | 已选的部门id。 |
| disabledDepartments | String[] | 不可选部门id。 |
| requiredDepartments | String[] | 必选部门（不可取消选中状态）。 |
| permissionType | String | 选人权限，目前只有“GLOBAL”这个参数。 |

## 返回结果

| **参数** | **说明** |
| --- | --- |
| userCount | 选择人数。 |
| departmentsCount | 选择的部门数。 |
| departments | 返回已选部门列表，列表中每个对象包含id (部门id)、name (部门名称)、number (部门人数)、 code（部门编码）、unionDeptExt(关联部门信息)：   - unionDeptExt包含二个字段 - corpId：关联部门的企业corpId - deptId：关联部门ID   结构如下：   ``` { "id":"1234", "name":"xxx" "number":"xxx" "code":"xxx" "unionDeptExt":{ "corpId":"xxx" "deptId":"xxx"   } } ```   字段最低支持版本：   - code: iOS 7.6.35/android 7.6.35/win 7.6.35/mac 7.6.35 - unionDeptExt: iOS 7.6.35/android7.6.35/win 7.6.35/mac 7.6.35 |
