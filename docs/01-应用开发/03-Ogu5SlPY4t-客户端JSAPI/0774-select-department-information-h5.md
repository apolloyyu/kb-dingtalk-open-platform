---
title: "选择部门信息"
source_url: "https://open.dingtalk.com/document/development/select-department-information-h5"
namespace: "development"
slug: "select-department-information-h5"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > H5微应用 > JSAPI参考 > 通讯录选人 > 选择部门信息"
doc_id: "y3K9kgDbqT"
updated_at: "2025-09-17 20:56:15"
---

> Source: https://open.dingtalk.com/document/development/select-department-information-h5
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > H5微应用 > JSAPI参考 > 通讯录选人 > 选择部门信息
> Updated: 2025-09-17 20:56:15

# 选择部门信息

调用**biz.contact.departmentsPicker**选择部门信息。

## 调试

访问[JSAPI Explorer](https://open-dev.dingtalk.com/apiExplorer#/jsapi?api=biz.contact.departmentsPicker)在线调试该接口。

## 使用说明

接口会返回部门的信息，是以部门为维度，不是以人为维度。

| **客户端** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 支持 | 支持 | 支持 |

```
dd.biz.contact.departmentsPicker({
    title:"测试标题",            //标题
    corpId:"xxx",              //企业的corpId
    multiple:true,            //是否多选
    limitTips:"超出了",          //超过限定人数返回提示
    maxDepartments:100,            //最大选择部门数量
    pickedDepartments:[],          //已选部门
    disabledDepartments:[],        //不可选部门
    requiredDepartments:[],        //必选部门（不可取消选中状态）
    appId:158,              //微应用的Id
    permissionType:"xxx",          //选人权限，目前只有GLOBAL这个参数
    onSuccess: function(result) {
        /**
        {
            userCount:1,                              //选择人数
            departmentsCount:1，//选择的部门数量
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
| maxDepartments | Number | 最大可选部门数。 |
| pickedDepartments | Array[String] | 已选的部门id。 |
| disabledDepartments | Array[String] | 不可选的部门id。 |
| requiredDepartments | Array[String] | 必选部门 (不可取消选中状态)。 |
| appId | Number | 微应用ID，企业内部应用请查看AgentId。 |
| permissionType | String | 选人权限，目前只有GLOBAL这个参数。 |

## 返回结果

| 参数 | 说明 |
| --- | --- |
| userCount | 选择人数。 |
| departmentsCount | 选择的部门数。 |
| departments | 返回已选部门列表，列表中每个对象包含id (部门id)、name (部门名称)、number (部门人数)、 code（部门编码）、unionDeptExt(关联部门信息)：   - unionDeptExt包含二个字段 - corpId：关联部门的企业corpId - deptId：关联部门ID   结构如下：   ``` { "id":"1234", "name":"xxx" "number":"xxx" "code":"xxx" "unionDeptExt":{ "corpId":"xxx" "deptId":"xxx"   } } ```   字段最低支持版本：   - code: iOS 7.6.35/android 7.6.35/win 7.6.35/mac 7.6.35 - unionDeptExt: iOS 7.6.35/android7.6.35/win 7.6.35/mac 7.6.35 |

展示效果如下图所示：

> **[!IMPORTANT]**
>
> Android端和iOS端不同系统展示结果可能会出现差别，请以最终的展示效果为准。

![选择部门](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7505834061/p177796.png)
