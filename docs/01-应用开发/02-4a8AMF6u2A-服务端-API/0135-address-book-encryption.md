---
title: "通讯录加密"
source_url: "https://open.dingtalk.com/document/development/address-book-encryption"
namespace: "development"
slug: "address-book-encryption"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "通讯录管理 > 通讯录ID转译 > 通讯录加密"
doc_id: "IQGJacZxn6"
updated_at: "2025-09-10 19:28:06"
---

> Source: https://open.dingtalk.com/document/development/address-book-encryption
> Path: 应用开发 / 服务端 API / 通讯录管理 > 通讯录ID转译 > 通讯录加密
> Updated: 2025-09-10 19:28:06

# 通讯录加密

本文档介绍了通讯录加密的操作流程。

企业通讯录是企业的重要敏感数据，根据服务商不同的应用部署方式有不同的要求，其中部分需要接入通讯录加密，否则无法上架应用市场。

## 接入须知

### 通讯录敏感数据加密

进入**开发者后台** > **应用开发** > **第三方企业应用** > **找到需部署的应用，**单击**应用部署** ，如果选择部署**方式一**，应用将对通讯录进行加密，无法获取到通讯录敏感数据。

敏感数据包含：**用户名、用户职位、部门名称**。

> **[!IMPORTANT]**
>
> - 只能选择下图方式一，才可以使用通讯录数据加密。
> - 不能选择应用部署的方式二或方式三，均无法达到对通讯录敏感数据加密的效果。

![部署方式](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8620360561/p432937.png)

### 用户侧获取敏感字段解决方案

钉钉为了满足“**在开发者无法获取到敏感字段的前提下，在用户侧获取这些敏感字段**”的需求，提供了如下解决方案：

- 可使用 open-data 组件（安全渲染组件），以提供更加安全良好的体验。
- 如果业务逻辑未用到敏感字段，以下解决方案可忽略跳过。

## 安全渲染组件-小程序

用于展示钉钉开放的数据。

| 客户端 | Android | IOS |
| --- | --- | --- |
| 支持说明 | 支持 | 支持 |
| 最低客户端版本 | 6.0.22 | 6.0.22 |

| 属性 | 类型 | 是否必填 | 说明 |
| --- | --- | --- | --- |
| openType | String | 是 | 开放数据的类型：   - userName：用户名称 - userTitle：用户职位 - departmentName：部门名称 |
| openId | String | 是 | 当openType值为：   - userName或userTitle =>  openId：userId - departmentName =>  openId：departmentId |
| defaultText | String | 否 | 默认显示文案。  **[!NOTE]**  默认显示文案内容。 |
| onError | function | 否 | 发生错误时的回调。 |

### index.js

```
Page({
    data: {
        openDataAvailable: dd.canIUse('open-data'),
        userId: '01114009704103', // userId 需要业务自行获取
        deptId: '151352132' // deptId 需要业务自行获取
        errorInfo: ''
    },
    openDataError(err) {
        console.log(err);
        this.setData({
            errorInfo: JSON.stringify(err)  
        });
        // switch err.code
    }
});
```

错误码

| 参数 | 说明 |
| --- | --- |
| 11 | 系统繁忙，请求失败。 |
| 12 | 参数错误(不合法的**openType**或不合法的**openId**等)。 |
| 13 | 显示值为空, 此时**fallback**到**defaultText**。 |

### index.axml

```
<open-data
    openType="userName/userTitle/departmentName"
    openId="{{data.userId}} 或 {{data.deptId}}"
    defaultText="默认文本"
    onError="openDataError"
    class="open-data-test"
/>
```

## 安全渲染组件-H5

用于展示钉钉开放的数据。

| 客户端 | Android | IOS | Windows | Mac |
| --- | --- | --- | --- | --- |
| 支持说明 | 支持 | 支持 | 支持 | 支持 |
| 最低客户端版本 | 6.0.22 | 6.0.22 | 6.0.22 | 6.0.22 |

1. 构造用户登录态

   > **[!IMPORTANT]**
   >
   > 调用H5安全渲染组件，依赖（钉钉自身能识别）用户登录态。

   构造用户登录态，需要在前端页面按照以下步骤拼接URL（以下统称为：登录态URL），然后在客户端（浏览器、钉钉客户端等）进行跳转访问。

   **登录态URL**的构成，主要依赖**回跳URL**（ISV自己的前端页面链接，比如应用首页URL、使用了H5渲染组件的页面URL等），当在客户端跳转访问**登录态URL**后，最终会重定向到**回跳URL**。

   下面以 https://open.dingtalk.com/document 作为**回跳URL**，进行举例：

   1. 对回跳URL进行encode：

      ```
      https%3A%2F%2Fopen.dingtalk.com%2Fdocument
      ```
   2. 在上一步基础上，添加**固定前缀**【http://auth.dingtalk.com/login?redirectUri=】：

      ```
      http://auth.dingtalk.com/login?redirectUri=https%3A%2F%2Fopen.dingtalk.com%2Fdocument
      ```
   3. 在上一步基础上，进行encode：

      ```
      http%3A%2F%2Fauth.dingtalk.com%2Flogin%3FredirectUri%3Dhttps%253A%252F%252Fopen.dingtalk.com%252Fdocument
      ```
   4. 在上一步基础上，添加**固定前缀**【https://login.dingtalk.com/oauth2/auth?response\_type=code&client\_id=dingwa4tibze6jwz7mgv&scope=openid&state=dddd&redirect\_uri=】：

      ```
      https://login.dingtalk.com/oauth2/auth?response_type=code&client_id=dingwa4tibze6jwz7mgv&scope=openid&state=dddd&redirect_uri=http%3A%2F%2Fauth.dingtalk.com%2Flogin%3FredirectUri%3Dhttps%253A%252F%252Fopen.dingtalk.com%252Fdocument
      ```

      > **[!IMPORTANT]**
      >
      > 固定前缀内容（尤其client\_id参数值）请不要擅自修改，否则会发生页面跳转异常。
2. 前端页面引入 open-data SDK，在页面中引入以下SDK

   ```
   <script src="https://auth.dingtalk.com/opendata-1.1.0.js"></script>
   ```

   > **[!NOTE]**
   >
   > - SDK 脚本需要放在<head>标签中，并置于其他所有的<script>标签之前，否则SDK无法生效。
   > - SDK 内容是动态返回的，请严格按照demo中的方式引入，不要保存到项目本地后打包引入。
3. 前端页面加载 open-data 中的数据

   在页面初始化时，需要调用 DTOpenData.init 方法初始化SDK，入参是**开通应用企业的corpId**。该方法会返回一个boolean值，标识初始化成功或失败。如果初始化失败，通常因为第1步的操作步骤执行有误，或登录态失效，需要重新构造“登录态URL”进行跳转访问。

   ```
   <script>
     if (window.DTOpenData.init('$CORPID$')) {
       // 入参是开通应用企业的corpId
       // SDK初始化成功，继续执行页面逻辑
     } else {
       // 说明当前用户未登录，需要跳转到钉钉统一登录
       window.location.href = '$登录态URL$';
     }
   </script>
   ```

   当页面上有数据需要进行安全渲染时，需要在页面上构造 dt-open-data 元素，并正确设置其 open-type 和 open-id 属性。当dom元素设置完成后，需要调用 DTOpenData.update 方法，传入需要进行渲染的dom元素对象即可自动完成渲染。

   > **[!NOTE]**
   >
   > - 调用DTOpenData.update方法前，一定要确保 DTOpenData.init 方法已经调用成功，否则update方法无法生效。
   > - DTOpenData.update方法一次性传入的dom节点数量不可以超过200个，否则无法正常渲染。

   | 属性 | 类型 | 是否必填 | 说明 |
   | --- | --- | --- | --- |
   | open-type | String | 是 | 开放数据的类型：  - userName：用户名称 - userTitle：用户职位 - departmentName：部门名称 |
   | open-id | String | 是 | 当openType值为：  - userName或userTitle =>  openId：userId - departmentName =>  openId：departmentId |

   ```
   <div>
     <dt-open-data open-type="userName" open-id="manager163711"></dt-open-data>
     <dt-open-data open-type="userTitle" open-id="013768148774791"></dt-open-data>
     <dt-open-data open-type="deptName" open-id="2202079361"></dt-open-data>
   </div>

   <script>
     window.DTOpenData.update(document.querySelectorAll('dt-open-data'));
   </script>
   ```
4. SDK使用Demo

   ```
   <!DOCTYPE html>
   <html lang="en">
     <head>
       <meta charset="UTF-8" />
       <meta http-equiv="X-UA-Compatible" content="IE=edge" />
       <meta name="viewport" content="width=device-width, initial-scale=1.0" />
       <title></title>
       <script src="https://auth.dingtalk.com/opendata-1.1.0.js"></script>
     </head>
     <body>
       <div>
         <dt-open-data open-type="userName" open-id="manager163711"></dt-open-data>
         <dt-open-data open-type="userTitle" open-id="013768148774791"></dt-open-data>
         <dt-open-data open-type="deptName" open-id="2202079361"></dt-open-data>
       </div>
       <div id="load">点击加载数据</div>
       <script>
         if (window.DTOpenData.init('ding1d4b5fc9223daa8e35c2f4657eb6378f')) {
           document.getElementById('load').addEventListener('click', () => {
             window.DTOpenData.update(document.querySelectorAll('dt-open-data'));
           });
         } else {
           // 说明当前用户未登录，需要跳转到钉钉统一登录
           window.location.href = '$登录态URL$';
         }
       </script>
     </body>
   </html>
   ```
5. 若在发消息通知内容中依赖了敏感字段。可以使用**内容转译**。

## 内容转译

通讯录ID转译模板语法。

```
$departmentName=DEPARTMENT_ID$
$userName=USER_ID$
```

其中 DEPARTMENT\_ID 是数字类型的部门id，USER\_ID是用户ID，例如：

- 将$departmentName=1$替换成部门id为“1”对应的部门名，如“钉钉用户体验部”。
- 将$userName=00001$替换成userid为“lisi007”对应的用户名，如“李四”。

### 消息通知内容转译

发通知消息时，可以在内容中以模板参数语法包含id，钉钉会将其替换为成员名或部门名，涉及服务端api：

- [发送工作通知](0769-asynchronous-sending-of-enterprise-session-messages.md)

> **[!NOTE]**
>
> 需要在原接口参数上添加enable\_id\_trans字段且置为true，才能开启转译，仅第三方应用需要用到，企业内部应用可以忽略。

### 搜索排序

| API名称 | 说明 | 申请权限路径 |
| --- | --- | --- |
| [搜索用户userId](0060-address-book-search-user-id.md) | 根据名字或拼音搜索出对应的userid。 | 在开发者后台 -> 打开需申请权限的应用 -> 申请**搜索企业通讯录的权限**。iShot2022-08-30 10 |
| [搜索部门ID](0080-address-book-search-department-id.md) | 根据名字或拼音搜索出对应的部门id。 | 在开发者后台 -> 打开需申请权限的应用 -> 申请**搜索企业通讯录的权限**。iShot2022-08-30 10 |
| [通讯录userId排序](0061-address-book-userid-sorting.md) | 根据姓名拼音升序或者降序排列。 | 在开发者后台 -> 打开需申请权限的应用 -> 申请**成员信息读权限**。iShot2022-08-30 10 |

### 通讯录转译相关API

- [异步转译通讯录ID](0133-asynchronous-address-book-file-content-translation.md)
- [获取异步转译任务结果](0134-obtains-the-results-of-an-asynchronous-translation-task.md)

### 异步任务回调通知

**RDS和SyncHttp推送**

当biz\_type=139时，数据为异步转译通讯录id的相关数据。

该数据为企业发生异步转译通讯录id任务完成的数据推送，插入表open\_sync\_biz\_data\_medium中。

| 字段 | 说明 |
| --- | --- |
| subscribe\_id | 套件suiteid加下划线0。 |
| corp\_id | 开通套件微应用的企业corpId。 |
| biz\_id | 无业务意义，幂等。 |
| biz\_typ | 固定值139，表示发生异步转译通讯录id任务完成相关数据。 |
| biz\_data | 数据为Json格式。 |

biz\_data数据如下：

```
{
     "syncAction": "transfer_contact_id_job_result",
     "jobId": "seejaRmZxVb4pjd4BtM255iIqXY8RQg090G0IAMMsxgzGCyho2SJSHS92xxxxxxx",
     "status": "1"
}
```

字段说明：

| 参数 | 数据类型 | 说明 |
| --- | --- | --- |
| syncAction | String | - transfer\_contact\_id\_job\_result：表示异步转译通讯录id任务完成的推送事件。 |
| jobId | String | 任务ID。 |
| status | String | 任务状态。 |
