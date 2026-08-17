---
title: "选择部门和人"
source_url: "https://open.dingtalk.com/document/development/select-department-and-person"
namespace: "development"
slug: "select-department-and-person"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > H5微应用 > JSAPI参考 > 通讯录选人 > 选择部门和人"
doc_id: "K2kn8NJs1z"
updated_at: "2025-09-17 20:56:15"
---

> Source: https://open.dingtalk.com/document/development/select-department-and-person
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > H5微应用 > JSAPI参考 > 通讯录选人 > 选择部门和人
> Updated: 2025-09-17 20:56:15

# 选择部门和人

调用**biz.contact.complexPicker**选择部门和人。

## 效果示例

> **[!IMPORTANT]**
>
> Android端、iOS端、PC端不同系统展示结果可能会出现差别，请以最终的展示效果为准。

![选择部门和人示例图](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1042099461/p429862.png)

## 调试

访问[JSAPI Explorer](https://open-dev.dingtalk.com/apiExplorer#/jsapi?api=biz.contact.complexPicker)在线调试该接口。

## 使用说明

支持选人和选部门。选择部门后，把所选部门转换成对应部门下的人。

| **客户端** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 支持 | 支持 | 支持 |

```
dd.biz.contact.complexPicker({
    title:"测试标题",            //标题
    corpId:"xxx",              //企业的corpId
    multiple:true,            //是否多选
    limitTips:"超出了",          //超过限定人数返回提示
    maxUsers:1000,            //最大可选人数
    pickedUsers:[],            //已选用户
    pickedDepartments:[],          //已选部门
    disabledUsers:[],            //不可选用户
    disabledDepartments:[],        //不可选部门
    requiredUsers:[],            //必选用户（不可取消选中状态）
    requiredDepartments:[],        //必选部门（不可取消选中状态）
    appId:158,              //微应用Id，企业内部应用查看AgentId
    permissionType:"xxx",          //可添加权限校验，选人权限，目前只有GLOBAL这个参数
    responseUserOnly:false,        //返回人，或者返回人和部门
    startWithDepartmentId:0 ,   //仅支持0和-1
    onSuccess: function(result) {
        /**
        {
            selectedCount:1,                              //选择人数
            users:[{"name":"","avatar":"","emplId ":""}]，//返回选人的列表，列表中的对象包含name（用户名），avatar（用户头像），emplId（用户工号）三个字段
            departments:[{"id":,"name":"","number":}]//返回已选部门列表，列表中每个对象包含id（部门id）、name（部门名称）、number（部门人数）
        }
        */
    },
   onFail : function(err) {}
});
```

## 参数说明

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| title | String | 选择页面的标题。 |
| corpId | String | 企业的corpId。 |
| multiple | Boolean | 是否多选：   - **true** - **false** |
| limitTips | String | 超过限定人数返回的提示内容。 |
| maxUsers | Number | 最大可选人数，最大值为10000。 |
| pickedUsers | Array[String] | 已选用户的userid。 |
| pickedDepartments | Array[String] | 已选的部门id。 |
| disabledUsers | Array[String] | 不可选用户的userid。 |
| disabledDepartments | Array[String] | 不可选部门id。 |
| requiredUsers | Array[String] | 必选用户 (不可取消选中状态)。 |
| requiredDepartments | Array[String] | 必选部门 (不可取消选中状态)。 |
| appId | Number | 微应用ID，企业内部应用请查看AgentId。 |
| permissionType | String | 选人权限，目前只有GLOBAL这个参数。 |
| responseUserOnly | Boolean | 返回信息：   - **true**：返回人员信息 - **false**：返回人员和部门信息 |
| startWithDepartmentId | Number | Android端选择部门和人时的开始位置。   - **0**：表示从企业根目录开始 - **-1**：表示从自己所在部门开始   **[!NOTE]**  该参数只支持Android端，IOS端可使用**deptId**参数。 |
| deptId | Number | IOS端选择部门和人时的开始位置。   - -1：表示从企业根目录部门开始 - 0：表示从自己所在的部门开始   **[!NOTE]**  该参数只支持IOS端，Android端可使用**startWithDepartmentId**参数。 |

## 返回结果

| 参数 | 说明 |
| --- | --- |
| selectedCount | 选择人数。 |
| users | 返回选人的列表，列表中的对象包含name (用户名)、avatar (用户头像)、emplId (用户工号)三个字段。 |
| departments | 返回已选部门列表，列表中每个对象包含id (部门id)、name (部门名称)、number (部门人数)。 |
