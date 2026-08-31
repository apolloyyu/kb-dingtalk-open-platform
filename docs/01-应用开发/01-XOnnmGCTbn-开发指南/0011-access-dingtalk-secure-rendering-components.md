---
title: "方式二：接入钉钉安全渲染组件"
source_url: "https://open.dingtalk.com/document/dingstart/access-dingtalk-secure-rendering-components"
namespace: "dingstart"
slug: "access-dingtalk-secure-rendering-components"
group: "应用开发"
tab: "开发指南"
breadcrumb: "开发指南 > 三方应用部署 > 保障企业通讯录数据安全 > 方式二：接入钉钉安全渲染组件"
doc_id: "AzTIlhS2mc"
updated_at: "2025-09-03 15:55:01"
---

> Source: https://open.dingtalk.com/document/dingstart/access-dingtalk-secure-rendering-components
> Path: 应用开发 / 开发指南 / 开发指南 > 三方应用部署 > 保障企业通讯录数据安全 > 方式二：接入钉钉安全渲染组件
> Updated: 2025-09-03 15:55:01

# 方式二：接入钉钉安全渲染组件

本文档介绍如何接入钉钉安全渲染组件，实现通讯录加密。

## **背景信息**

企业通讯录（用户名、用户职位、部门名称）是企业的重要敏感数据，根据服务商不同的应用部署方式有不同的要求，其中部分需要接入通讯录加密，否则无法上架应用市场。

钉钉为了满足“**在开发者无法获取到敏感字段的前提下，在用户侧获取这些敏感字段**”的需求，提供了安全渲染组件（open-data）解决方案，以提供更加安全良好的体验。

## **操作步骤**

1. 在前端页面中拼接用户登录态URL。

   > **[!NOTE]**
   >
   > **登录态URL**的构成，主要依赖**回调URL**（ISV自己的前端页面链接，比如应用首页URL、使用了H5渲染组件的页面URL等）。当在客户端跳转访问**登录态URL**后，最终会重定向到**回调URL**。

   1. 对回调 URL 进行 encode。

      > **[!NOTE]**
      >
      > 步骤中均以 *https://open.dingtalk.com/document* 举例。

      ```
      https%3A%2F%2Fopen.dingtalk.com%2Fdocument
      ```
   2. 添加**固定前缀** `http://auth.dingtalk.com/login?redirectUri=`。

      ```
      http://auth.dingtalk.com/login?redirectUri=https%3A%2F%2Fopen.dingtalk.com%2Fdocument
      ```
   3. 再次进行 encode。

      ```
      http%3A%2F%2Fauth.dingtalk.com%2Flogin%3FredirectUri%3Dhttps%253A%252F%252Fopen.dingtalk.com%252Fdocument
      ```
   4. 添加**固定前缀**`https://login.dingtalk.com/oauth2/auth?response_type=code&client_id=dingwa4tibze6jwz7mgv&scope=openid&state=dddd&redirect_uri=`，拼接得到**登录态URL**。

      ```
      https://login.dingtalk.com/oauth2/auth?response_type=code&client_id=dingwa4tibze6jwz7mgv&scope=openid&state=dddd&redirect_uri=http%3A%2F%2Fauth.dingtalk.com%2Flogin%3FredirectUri%3Dhttps%253A%252F%252Fopen.dingtalk.com%252Fdocument
      ```
   5. 在前端页面引入 open-data SDK。

      ```
      <script src="https://auth.dingtalk.com/opendata-1.1.0.js"></script>
      ```

      > **[!NOTE]**
      >
      > - SDK 脚本需要放在<head>标签中，并置于其他所有的<script>标签之前，否则SDK无法生效。
      > - SDK 内容是动态返回的，请严格按照demo中的方式引入，不要保存到项目本地后打包引入。
   6. 前端页面加载 open-data 中的数据。

      1. 调用 DTOpenData.init 方法进行初始化。

         | **配置项** | **说明** |
         | --- | --- |
         | `CorpId` | 开通应用企业的 CorpId 值。 |
         | `登录态URL` | 最终添加固定前缀拼接得到的登录态URL。 |

         > **[!NOTE]**
         >
         > 该方法会返回一个 Boolean 值，标识初始化成功或失败。如果初始化失败，通常因为步骤一的操作步骤执行有误，或登录态失效，需要重新构造“登录态URL”进行跳转访问。

         ```
         <script>
           if (window.DTOpenData.init('$CorpId$')) {
             // 入参是开通应用企业的corpId值
             // SDK初始化成功，继续执行页面逻辑
           } else {
             // 说明当前用户未登录，需要跳转到钉钉统一登录
             window.location.href = '$登录态URL$';
           }
         </script>
         ```
      2. 当页面上有数据需要进行安全渲染时，需要在页面上构造 dt-open-data 元素，并正确设置其 open-type 和 open-id 属性。当dom元素设置完成后，需要调用 DTOpenData.update 方法，传入需要进行渲染的dom元素对象即可自动完成渲染。

         > **[!NOTE]**
         >
         > DTOpenData.update方法一次性传入的dom节点数量不可以超过200个，否则无法正常渲染。

         ```
         <div>
           <dt-open-data open-type="userName" open-id="manager163711"></dt-open-data>
           <dt-open-data open-type="userTitle" open-id="013768148774791"></dt-open-data>
           <dt-open-data open-type="departmentName" open-id="2202079361"></dt-open-data>
         </div>

         <script>
           window.DTOpenData.update(document.querySelectorAll('dt-open-data'));
         </script>
         ```

         | **属性** | **类型** | **是否必填** | **说明** |
         | --- | --- | --- | --- |
         | open-type | String | 是 | 开放数据的类型：  - userName：用户名称 - userTitle：用户职位 - deptName：部门名称 |
         | open-id | String | 是 | 当openType值为：  - userName：用户userId - userTitle：用户userId - deptName：部门名称 |

## **SDK 使用示例**

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

## **（可选）内容转译**

#### **消息通知模板内容转译**

发通知消息时，可以在内容中以模板参数语法包含id，钉钉会将其替换为成员名或部门名，涉及服务端api：[发送工作通知](../02-4a8AMF6u2A-服务端-API/0769-asynchronous-sending-of-enterprise-session-messages.md)

需要在原接口参数上添加`enable_id_trans`字段且置为true，才能开启转译，仅第三方应用需要用到，企业内部应用可以忽略。

**通讯录ID转译模板语法**

```
$departmentName=DEPARTMENT_ID$
$userName=USER_ID$
```

其中 DEPARTMENT\_ID 是数字类型的部门id，USER\_ID 是用户ID，例如：

- 将$departmentName=1$替换成部门id为“1”对应的部门名称，如“钉钉用户体验部”。
- 将$userName=00001$替换成userid为“lisi007”对应的用户名，如“李四”。

#### **通讯录转译**

- [异步转译通讯录ID](../02-4a8AMF6u2A-服务端-API/0133-asynchronous-address-book-file-content-translation.md)
- [获取异步转译任务结果](../02-4a8AMF6u2A-服务端-API/0134-obtains-the-results-of-an-asynchronous-translation-task.md)

## **后续步骤**

接入安全渲染组件后，你需要[导入资源到计算巢](0012-import-resources-compute-nest.md)。
