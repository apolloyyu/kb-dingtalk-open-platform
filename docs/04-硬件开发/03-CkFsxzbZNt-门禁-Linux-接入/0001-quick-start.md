---
title: "SDK概览"
source_url: "https://open.dingtalk.com/document/development/quick-start"
namespace: "development"
slug: "quick-start"
group: "硬件开发"
tab: "门禁 Linux 接入"
breadcrumb: "SDK概览"
doc_id: "90XfisLJhA"
updated_at: "2026-08-04 09:07:13"
---

> Source: https://open.dingtalk.com/document/development/quick-start
> Path: 硬件开发 / 门禁 Linux 接入 / SDK概览
> Updated: 2026-08-04 09:07:13

# SDK概览

钉钉门禁SDK作为门禁设备端的一个软件开发包，旨在将这些核心数据以安全的方式开放给合作方。通过门禁SDK的集成，传统厂商可快速具备基于云平台的设备管理能力。

## **SDK 功能介绍**

门禁SDK运行在Linux操作系统上，支持的功能主要有：

- 支持基本的设备接入钉钉云，通过微应用绑定与解绑设备
- 支持考勤打卡
- 支持刷卡身份识别
- 支持测温
- 支持人脸识别开门和开门记录
- 支持远程开门

## SDK 目录介绍

钉钉门禁Linux的顶层SDK目录如下：

```
include
   dtiot      //钉钉sdk相关头文件
   nolwp    //三方开源头文件，例如sqlitex.h
lib
   libsdk.so        //钉钉sdk主文件
   libsqlitex.so    //阿里定制版sqlite，注意不能与开源sqlite一起使用
   libsgmain.so   //安全相关 
demo
   demo.c       //demo程序
```

> **[!IMPORTANT]**
>
> 运行时依赖的libz, libcurl, libopenssl不包含在里面，需要由厂商自行准备。

## SDK Demo说明

SDK中提供了Demo文件（`demo.c`）方便厂商快速接入。Demo使用说明如下：

1. 设备初始化，参看demo中的main函数，请严格按照demo中的初始化步骤。
2. 切换特征服务器。

   不采用阿里巴巴算法的厂家，可以通过如下接口切换算法服务器。参数一是算法服务器的feature\_type,参数二是feature\_version。
   例如，以魔点Y2为例，切换算法到魔点自己布署的算法服务器方法是：

   ```
   dtiot_face_service_singleton()->switch_feature_type(601, "5");
   ```
3. 设备绑定，参看demo中**get\_static\_qr\_code**函数，三方需要将获取到的url转换为二维码展示在屏幕上。

   > **[!NOTE]**
   >
   > 注意事项：
   >
   > - 除蓝牙绑定外的其他绑定方式一定要先配置网络，等网络通（三方自己监测网络）后要先ntp同步，钉钉通信协议依赖时钟，偏差在几小时内，再调用static\_bind\_start或其他绑定开始函数。
   > - 部分系统在网络同步后会存在dns更新不及时问题，注意在网络通后一定要调用res\_init问题（如果钉钉SDK报错日志显示解析lwp.dingtalk.com失败可能是此问题导致）。
   > - 一定要先device\_init然后再获取二维码。
4. 绑定后信息同步及回调。

   设备与服务端信息同步，如果在初始化的过程中有注册绑定事件回调，回调注册函数，如果是解绑，第三方设备厂商务必要主动删除`dtiot_device_service_singleton()->set_storage_path`目录中的内容，删除后重启进程或设备。
5. 设置离线时存储门禁记录的上限。

   由于门禁记录包含了图片资源，所以有必要根据厂家自己的存储容量来合理设定上限值，不然，离线时，积累在本地没有上传的图片会占用过多的存储空间。
   如设置只存2000条离线开门记录，方法如下：

   ```
   dtiot_entrance_service_singleton()->set_entrance_record_number(2000);
   ```

   当已经累积达到2000条开门记录都没有上传之后，新的开门记录将丢弃。
6. 设备名称变更事件注册。

   ```
   dtiot_inside_service_singleton()->register_config(inside_service_config_callback);
   ```

   通过注册变更回调事件，当微应用上修改了设备名称之后，回调函数得到调用。可以在回调函数中修改界面上显示的设备名称。
7. 开关变化注册。

   ```
   dtiot_inside_service_singleton()->register_switch(inside_service_switch_callback);
   ```

   目前，支持如下开关控制：
   是否开启极速检测模式，当开启时，设备将关闭红外活体检测，以便检测速度更快，但安全性下降。
