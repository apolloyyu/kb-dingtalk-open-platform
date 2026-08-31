---
title: "官方连接器通用字段获取"
source_url: "https://open.dingtalk.com/document/connection/official-connector-generic-field-acquisition-1"
namespace: "connection"
slug: "official-connector-generic-field-acquisition-1"
group: "连接平台"
tab: "我的连接"
breadcrumb: "开发连接器 > 参考 > 官方连接器通用字段获取"
doc_id: "uteDyhCiGo"
updated_at: "2026-07-24 09:20:47"
---

> Source: https://open.dingtalk.com/document/connection/official-connector-generic-field-acquisition-1
> Path: 连接平台 / 我的连接 / 开发连接器 > 参考 > 官方连接器通用字段获取
> Updated: 2026-07-24 09:20:47

# 官方连接器通用字段获取

## **用户ID（userId）**

用户ID可以登录[钉钉管理后台](https://oa.dingtalk.com/) > 左侧「通讯录」>「成员管理」>「点击成员」>「员工UserID」获取。

![获取用户userId信息..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7406584871/p677250.png)

## **组织Id（corpId）**

企业的corpId，可在[开发者后台](https://open-dev.dingtalk.com/)右上角获取。

![corpId获取..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7406584871/p677251.png)

## **应用Id（agentId）**

应用在企业的AgentId可以在[开发中后台](https://open-dev.dingtalk.com/fe/app#/corp/app)中选择任意企业内部开发的钉钉应用，查看应用信息获取。

![应用agentId..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7406584871/p677252.png)

## **部门Id（deptId）**

部门ID可以登录[钉钉管理后台](https://oa.dingtalk.com/)> 左侧「通讯录」>「部门管理」> 点击对应部门的**编辑**进行查看。

> **[!NOTE]**
>
> 企业最高一级部门，即根部门为1。

1. 单击编辑部门信息。

   ![查看部门id1..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7406584871/p677253.png)
2. 查看部门Id。

   ![查看部门id2..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8406584871/p677254.png)

## **文件Id（mediaId）**

获取方式参见[上传媒体文件](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0646-upload-media-files.md)。

### **SDK方式**

**Maven地址：**

```
<dependency>
    <groupId>com.aliyun</groupId>
    <artifactId>alibaba-dingtalk-service-sdk</artifactId>
    <version>2.0.0</version>
</dependency>
```

**代码示例：**

```
 public static void main(String[] args) throws ApiException {
        DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/media/upload");
        OapiMediaUploadRequest req = new OapiMediaUploadRequest();
        req.setType("image");
        // 要上传的媒体文件
        FileItem item = new FileItem("/****/*****/****/logo.png");
        req.setMedia(item);
        OapiMediaUploadResponse rsp = client.execute(req, "token******");
        System.out.println(rsp.getBody());
    }
```

**输出结果：**

```
{
  "errcode": 0,
  "errmsg": "ok",
  "media_id": "@lALPDfJ*****uSXM8Mzw",
  "created_at": 1685352026322,
  "type": "image"
}
```

### **HTTP方式**

使用[postman](https://www.postman.com/downloads/)工具实现。

配置获取mediaId接口，参数配置如下：

1. ​URL为`POST`请求，填写：`https://oapi.dingtalk.com/media/upload?access_token={{access_token}}`。
2. 在Pre-request Script中填写获取钉钉access\_token：

   > **[!NOTE]**
   >
   > appKey和AppSecret，可通过调用[获取企业内部应用的accessToken](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0033-obtain-the-access-token-of-an-internal-app.md)接口获取。

   ```
   pm.sendRequest("https://oapi.dingtalk.com/gettoken?appkey=xxxx&appsecret=xxxxxx", function (err, response) {
       console.log(response.json());
       pm.environment.set("access_token", response.json().access_token);
   });
   ```

   ![媒体文件postman请求..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8406584871/p683407.png)
3. 配置Body参数：

   需要选择form-data类型，并且media参数需要设置为File类型，然后上传本地文件后发送请求获取media\_id。

   ![配置媒体文件postman请求..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7406584871/p683408.png)
4. 选择文件并发起调用。

   ![获取mediaId 的postman..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7406584871/p683409.png)

## **机器人编码（robotCode）**

在[开发者后台](https://open-dev.dingtalk.com/fe/app#/corp/app)中选择任意企业内部开发的钉钉应用，点击左侧【机器人】，即可找到RobotCode。

> **[!NOTE]**
>
> 查看RobotCode，需该机器人发布完成后，才可查看。

![复制robotCode..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7406584871/p677255.png)

## **机器人（access\_token）**

> **[!NOTE]**
>
> 企业内部应用-机器人添加入群后，单击**群设置** > **机器人 > 机器人管理** > **目标机器人**，即可查看机器人 Webhook 地址。

![image..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7406584871/p677256.png)

## **用户UnionId（unionId）**

> **[!NOTE]**
>
> 不建议使用。

获取方式参见[查询用户详情](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0056-query-user-details.md)接口。

**Maven地址：**

```
<dependency>
  <groupId>com.aliyun</groupId>
  <artifactId>alibaba-dingtalk-service-sdk</artifactId>
  <version>2.0.0</version>
</dependency>
```

**代码示例：**

```
public static void main(String[] args) throws ApiException {
  DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/v2/user/get");
  OapiV2UserGetRequest req = new OapiV2UserGetRequest();
  req.setUserid("01471828*****95079");
  req.setLanguage("zh_CN");
  OapiV2UserGetResponse rsp = client.execute(req, "token******");
  System.out.println(rsp.getBody());
}
```

**输出结果：**

```
{
  "errcode": 0,
  "errmsg": "ok",
  "result": {
    "active": true,
    "admin": true,
    "unionid": "Vwx3eb***********8yAiEiE",
    "userid": "014718280100695079"
  },
  "request_id": "15r6glmanhbtk"
}
```

## **群模板ID（templateId）**

登录[开发者后台 > 开放能力 > 场景群 > 群模板](https://open-dev.dingtalk.com/fe/im#/group/list)查看。

![群模板ID..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7406584871/p677257.png)

## **群会话ID（chatId/openConversationId）**

获取方式参见[根据corpid选择会话](https://open.dingtalk.com/tools/explorer/jsapi?id=10303)JSAPI接口。

> **[!NOTE]**
>
> 使用API Explorer工具，需提前[登录开发者后台](https://open-dev.dingtalk.com/)。

1. 依次填写参数，**发起调用**并使用钉钉客户端**扫码**连接控制台：

   - **corpId：**your corpId。
   - **isAllowCreateGroup**：false。
   - **filterNotOwnerGroup**：false。

     ![获取群id..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8406584871/p677258.png)
2. 连接控制台后，再次发起调用，即可选取群会话，获取群会话Id。

   ![获取会话Id..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7406584871/p677259.png)

## **审批模板code（processCode）**

在oa审批管理后台，每个审批单**编辑页面**的**基础设置**底部。

> **[!NOTE]**
>
> 登录OA审批管理后台，需要拥有OA审批应用的管理权限。

![processCode..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7406584871/p677260.png)

## **审批钉盘空间ID（spaceId）**

获取方式参见[获取审批钉盘空间信息](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0502-obtains-the-information-about-approval-nail-disk.md)接口。

**Maven地址：**

```
<dependency>
  <groupId>com.aliyun</groupId>
  <artifactId>dingtalk</artifactId>
  <version>2.0.18</version>
</dependency>
```

**代码示例：**

```
public void ProcessSpaceInfo() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        com.aliyun.dingtalkworkflow_1_0.Client client = new com.aliyun.dingtalkworkflow_1_0.Client(config);
        com.aliyun.dingtalkworkflow_1_0.models.GetAttachmentSpaceHeaders getAttachmentSpaceHeaders = new com.aliyun.dingtalkworkflow_1_0.models.GetAttachmentSpaceHeaders();
        getAttachmentSpaceHeaders.xAcsDingtalkAccessToken = "accessToken";
        com.aliyun.dingtalkworkflow_1_0.models.GetAttachmentSpaceRequest getAttachmentSpaceRequest = new com.aliyun.dingtalkworkflow_1_0.models.GetAttachmentSpaceRequest()
                .setUserId("manager7675")
                .setAgentId(1185599675L);
        try {
            GetAttachmentSpaceResponse attachmentSpaceWithOptions = client.getAttachmentSpaceWithOptions(getAttachmentSpaceRequest, getAttachmentSpaceHeaders, new RuntimeOptions());
            System.out.println(JSON.toJSONString(attachmentSpaceWithOptions.getBody()));
        } catch (TeaException err) {
            if (!com.aliyun.teautil.Common.empty(err.code) && !com.aliyun.teautil.Common.empty(err.message)) {
                // err 中含有 code 和 message 属性，可帮助开发定位问题
                System.out.println(err.code);
                System.out.println(err.message);
            }
        } catch (Exception _err) {
            TeaException err = new TeaException(_err.getMessage(), _err);
            if (!com.aliyun.teautil.Common.empty(err.code) && !com.aliyun.teautil.Common.empty(err.message)) {
                // err 中含有 code 和 message 属性，可帮助开发定位问题
                System.out.println(err.code);
                System.out.println(err.message);
            }
        }
    }
```

**输出结果：**

```
{
  "result" : {
    "spaceId" : 3996960664
  },
  "success" : true
}
```

## **宜搭表单ID/应用编码/应用密钥**

1. 单击宜搭应用。

   ![单击附件应用..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7406584871/p667629.png)
2. 单击**应用设置** > **部署运维。**

   ![应用参数宜搭..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7406584871/p667694.png)

## **互动卡片Id（cardTemplateId）**

可在[开发者后台](https://open-dev.dingtalk.com/)中选择卡片内容，选择对应卡片的id。

![卡片模板ID..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7406584871/p677261.png)
