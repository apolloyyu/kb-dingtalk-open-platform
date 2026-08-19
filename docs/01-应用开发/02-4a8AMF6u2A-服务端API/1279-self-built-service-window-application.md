---
title: "自建服务窗应用"
source_url: "https://open.dingtalk.com/document/development/self-built-service-window-application"
namespace: "development"
slug: "self-built-service-window-application"
group: "应用开发"
tab: "服务端API"
breadcrumb: "更多开放 > 服务窗 > 使用教程 > 自建服务窗应用"
doc_id: "pA15UV5DLn"
updated_at: "2026-07-20 09:21:59"
---

> Source: https://open.dingtalk.com/document/development/self-built-service-window-application
> Path: 应用开发 / 服务端API / 更多开放 > 服务窗 > 使用教程 > 自建服务窗应用
> Updated: 2026-07-20 09:21:59

# 自建服务窗应用

使用自建的服务窗应用，调用服务窗接口获取服务窗的相关数据，例如联系人数据、企业信息等。

## 功能介绍

服务窗已经提供了自定义链接跳转、企业主页、资料库、发起客户工单等缺省功能，没有很强定制需求的企业只需要在服务窗管理后台进行简单配置即可直接使用，具体操作请参考[开通服务窗](1277-customer-service-overview.md)。

有强定制需求的企业，我们提供了自建服务窗应用功能，通过使用服务窗开放接口，自建服务窗可以具备以下能力：

- 获取关注了服务窗的联系人信息。
- 监听服务窗关注/取消关注的消息事件。
- 发送消息通知。

## 操作步骤

根据以下步骤，完成自建服务窗应用：

1. 创建服务窗。

   > **[!NOTE]**
   >
   > 如果你已经有了一个服务窗，可以跳过此步骤。

   打开工作台上的“服务窗”应用（如果找不到请先到应用市场搜索安装），初次使用会弹出创建服务窗的页面，如下图所示：

   ![a5ab9d253afb4982834d495b598175380579](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3043727161/p259693.png)

   填写资料后提交审核，1-3天内审核完成，审核完成后进入下一步。
2. 创建服务窗应用。

   1. 进入服务窗菜单设置页，依次选择**跳转应用 > 创建新应用**，跳转到服务窗对应的开发者后台界面。

      > **[!NOTE]**
      >
      > 如果有建好的服务窗应用，可以直接在**选择应用**中进行选择。如果需要新建服务窗应用，点击**创建新应用**新建新的服务窗应用。

      ![p259694](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5846867161/p260453.png)

      该服务窗对应的开发者后台界面，如下图所示：

      ![4ffa2dbd840c41dba87578f8924dc1b50579](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4043727161/p259696.png)
   2. 单击**创建应用**，打开创建应用界面。

      > **[!NOTE]**
      >
      > 请选择创建**H5微应用**，暂不支持小程序。

      ![p259696](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4043727161/p259726.png)
   3. 填入对应信息，然后单击确定创建。创建好后可以获得以下三个重要信息，在后面的开发中会被用到。

      - **AppKey/AppSecret**：开发中调用开放接口需要使用AppKey/AppSecret进行授权，点开应用详情可以获取到，如下图所示：

        ![3](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4940154871/p527248.png)
      - **虚拟组织corpId**：确定服务窗企业身份。点击首页可以看到该服务窗对应的虚拟组织的corpId，如下图所示。

        > **[!IMPORTANT]**
        >
        > 这个corpId不是真实组织的corpId，而是一个和真实组织关联的虚拟组织corpId，它专门用于服务窗应用。

        ![服务窗](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0894902261/p260447.png)
3. 接入免登。

   虽然自建服务窗应用是基于虚拟组织开发的，但是免登的处理方式和真实组织企业内部应用是一样的，详情请查看[网页应用（H5微应用）免登](0018-enterprise-internal-application-logon-free.md)。
4. 开发应用。

   免登之后，即可调用开放API进行自建服务窗应用开发了，以下开放能力是服务窗开发中经常使用的：

   > **[!NOTE]**
   >
   > 服务窗的相关API采用新的调用方式进行调用，详情可参考[服务端SDK下载](0002-download-the-server-side-sdk.md)。

   - 获取用户的基本信息，例如联系人昵称、userid等非敏感信息，如果需要获取联系人主企业名称，则需要接入服务窗应用授权JSAPI，取得用户授权后才能获取到。

     - 通过调用[批量获取关注服务窗用户信息](1284-obtains-the-follower-information-from-the-service-window.md)接口获取关注了服务窗的联系人信息。

       > **[!NOTE]**
       >
       > 此接口仅供首次启用应用时全量同步历史数据使用，增量数据请通过关注、取消关注事件回调获取，请合理使用本接口。
     - 通过调用[获取关注服务窗用户信息](1285-queries-the-follower-information-of-the-service-window.md)接口获取已授权的联系人主企业名称。
   - 监听服务窗事件回调，例如监听服务窗的关注和取消关注状态等，详情可参考[服务窗事件](../04-LFcRvVD08N-事件订阅/0002-org-event-overview.md#b1e7c8d084d4e)。
   - 调用[批量发送服务窗消息](1280-batch-sending-of-service-window-messages.md)或[发送服务窗单人消息](1281-sends-a-single-message-from-the-service-window.md)接口发送服务窗消息。
5. 发布应用。

   应用开发完成后进入应用详情页，单击**确认发布**，该应用会出现在服务窗菜单设置页的应用列表中。

   ![52688c927ec54af58242362018b156d50579](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4043727161/p259701.png)在服务窗菜单设置页把应用关联到菜单中即可，如下图所示：

   ![51d0773763ea4c7bb2936ec53bd59bf50579](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4043727161/p259703.png)
