---
title: "小程序使用网页应用客户端 API"
source_url: "https://open.dingtalk.com/document/dingstart/mini-app-steps"
namespace: "dingstart"
slug: "mini-app-steps"
group: "应用开发"
tab: "开发指南"
breadcrumb: "开发小程序应用 > 小程序使用网页应用客户端 API"
doc_id: "Biiu81d9hq"
updated_at: "2026-07-22 16:55:16"
---

> Source: https://open.dingtalk.com/document/dingstart/mini-app-steps
> Path: 应用开发 / 开发指南 / 开发小程序应用 > 小程序使用网页应用客户端 API
> Updated: 2026-07-22 16:55:16

# 小程序使用网页应用客户端 API

本文档介绍在钉钉小程序内，如何调用钉钉网页应用的API。

## **背景信息**

小程序的JSAPI框架继承了网页应用的所有native plugin，所以基于dingtalk-jsapi框架的JSAPI在小程序内也可以使用。

## **步骤一：钉钉小程序项目安装dingtalk-jsapi**

1. 钉钉小程序项目内创建`node_modules`文件夹。![iShot2022-09-30 17](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8221872871/p499217.png)
2. 在创建的`node_modules`文件夹目录下，安装dingtalk-jsapi。

   ```
   npm install dingtalk-jsapi --save
   ```

## **步骤二：初始化dingtalk-jsapi**

在钉钉小程序app.js文件头部，添加以下代码：

```
import 'dingtalk-jsapi/entry/mobile';
```

![iShot2022-09-30 17](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8221872871/p499220.png)

## **步骤三：在钉钉小程序内调用**

以在钉钉小程序index页面，调用网页应用的[选择部门和人](../03-Ogu5SlPY4t-客户端-JSAPI/0736-select-department-and-person.md)接口为例。

1. 小程序index.js文件头部，添加以下代码：

   ```
   import complexPicker from 'dingtalk-jsapi/api/biz/contact/complexPicker';
   ```

   ![iShot2022-09-30 17](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8221872871/p499223.png)
2. 小程序index.axml文件，定义按钮触发方法。

   ```
   <view>
     <button size="default" type="primary" onTap="complexPicker">选择部门和人</button>
   </view>
   ```
3. 小程序index.js文件，定义方法触发`complexPicker`。

   ```
   import complexPicker from 'dingtalk-jsapi/api/biz/contact/complexPicker';
   Page({
     data: {
     },
     onLoad(query) {
     },
     complexPicker(){
       complexPicker({
         title:"测试标题",            //标题
         corpId:"ding027fxxxxx",              //企业的corpId
         multiple:true,            //是否多选
         maxUsers:1000,            //最大可选人数
         pickedUsers:[],            //已选用户
         pickedDepartments:[],          //已选部门
         disabledUsers:[],            //不可选用户
         disabledDepartments:[],        //不可选部门
         requiredUsers:[],            //必选用户（不可取消选中状态）
         requiredDepartments:[],        //必选部门（不可取消选中状态）
         permissionType:"GLOBAL",          //可添加权限校验，选人权限，目前只有GLOBAL这个参数
         responseUserOnly:false,        //返回人，或者返回人和部门
         startWithDepartmentId:0 ,   //仅支持0和-1
         onSuccess: function(result) {
             console.log(JSON.stringify(result))
         },
        onFail : function(err) {
         console.log(JSON.stringify(err))
        }
       })
     },
   });
   ```
4. 小程序调用效果。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8221872871/p1084298.png)
