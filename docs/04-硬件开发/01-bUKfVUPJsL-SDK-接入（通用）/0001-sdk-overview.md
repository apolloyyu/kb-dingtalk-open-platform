---
title: "SDK概览"
source_url: "https://open.dingtalk.com/document/development/sdk-overview"
namespace: "development"
slug: "sdk-overview"
group: "硬件开发"
tab: "SDK 接入（通用）"
breadcrumb: "SDK概览"
doc_id: "UXG1gv3OYY"
updated_at: "2026-08-03 09:19:30"
---

> Source: https://open.dingtalk.com/document/development/sdk-overview
> Path: 硬件开发 / SDK 接入（通用） / SDK概览
> Updated: 2026-08-03 09:19:30

# SDK概览

本文档为指导接入厂商能够高效快速使用本SDK进行接入开发工作，详细描述了钉钉蓝牙SDK的接入方法，以及使用注意事项。请接入厂商在拿到SDK之前，详细阅读本文档。

> **[!NOTE]**
>
> 本SDK为针对具有蓝牙BLE能力的智能硬件开发，为其接入钉钉平台提供能力。可适用于LINUX，RTOS，类RTOS等多种操作系统，具有广泛的适配性和移植性。

## SDK 架构介绍

SDK的整体分层架构如下图所示。

![架构](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5850886061/p187162.png)

- 从SDK所提供给接入厂商的能力上，主要为模块绑定和蓝牙的通讯。

  - SDK的绑定模块实现了与钉钉端完成绑定的能力。
  - SDK的蓝牙通讯模块实现了一个厂商业务层与钉钉端时间的蓝牙通道，在该通道上，将业务数据封装成物模型协议传输。
  - SDK的设备模块与功能模块，只对设备的基础信息和能力做了抽象和接口统一，因各个接入平台的具体实现千差万别，所以功能实现部分由接入厂商完成OSHAL层的实现。
- 业务通讯协议

  接入SDK后，接入厂家可以通过蓝牙通道上的物模型协议，完成各种不同业务场景的业务实现，理论上SDK不会限制接入设备的任何类型和业务形态。

  关于物模型请参考[使用说明](https://open.dingtalk.com/document/device-side-development-guide/overview-27)。

  在网络通讯能力上，如果接入厂家设备支持WIFI，4G等能力，目前建议采用阿里云AIOT开源方案通过网络接入钉钉服务端。
- SDK资源使用情况

  本SDK最大的特点为可兼容cotexA/M/R等全系列平台芯片，针对系统资源相对紧缺的产品，目前SDK本身在最小情况下耗费资源为：

  - **FLASHA需要20K**
  - **RAM需要4K**

## SDK 文件介绍

发布版本SDK提供如下文件：

![sdk文件 ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2018786061/p186357.png)

- `dtiot-sdk.lib`为钉钉接入SDK在接入厂商平台上编译输出的库文件。配套的头文件在`include`目录下。
- `dtiot_os_hal.c`为接入厂商要实现的本平台的os层接口函数，请不要修改封装好的函数定义，该文件为SDK内部提供在接入平台上的基础OS\_HAL能力。
- `main.c` 、`bind_demo.c` 、 `bind_demo.h`三个文件为源代码demo，方便接入厂商快速接入钉钉SDK。Demo中针对SDK的各个接口的接入方法做了详细说明。

  > **[!NOTE]**
  >
  > 示例demo中没有实现的SDK接口，可参考头文件的接口定义说明。

从提供的头文件可见，接入厂商要完成三个模块的对接，同时还要实现dtiot\_os\_hal.c中定义的各个函数接口。

| SDK模块 | 模块说明 |
| --- | --- |
| diot\_bind\_service | SDK绑定模块，所有绑定相关操作均在此模块完成。 |
| diot\_ble\_hal\_service | 蓝牙基础能力对接模块（广播、收发蓝牙数据等） |
| diot\_device\_service | 设备信息模块（SN, MAC, 接入信息等） |

## **SDK 下载**

本SDK是钉钉物联网（IoT）设备接入的核心开发工具包，专为嵌入式设备与钉钉平台的快速集成而设计。通过该SDK，开发者可实现设备身份认证、消息通信、数据上报与指令接收等功能，支持多种主流MCU架构，适用于智能家居、工业物联网、智能办公等场景。

- cortex-m3：[下载](https://osupload.cn-hangzhou.oss.aliyun-inc.com/pack/2020-12-01/1606833711697_992/dtiot-cm3.zip)
- cortex-m4：[下载](https://osupload.cn-hangzhou.oss.aliyun-inc.com/pack/2020-12-01/1606833772511_958/dtiot-cm4.zip)
- cortex-m33：[下载](https://osupload.cn-hangzhou.oss.aliyun-inc.com/pack/2020-12-01/1606833738425_321/dtiot-cm33.zip)
- cortex-m7：[下载](https://osupload.cn-hangzhou.oss.aliyun-inc.com/pack/2020-12-01/1606833805413_199/dtiot-cm7.zip)
- nrf52840:[下载](https://osupload.cn-hangzhou.oss.aliyun-inc.com/pack/2020-12-01/1606833834751_9/dtiot-nrf52840.zip)
- himix200: [下载](https://osupload.cn-hangzhou.oss.aliyun-inc.com/pack/2020-12-01/1606833664191_117/dtiot-himix200.zip)

## 厂商技术接入流程

1. 技术人员支持

   为协助厂商顺利完成设备接入钉钉平台，钉钉侧会提供如下技术人员进行支持：

   - 设备端：提供SDK导入的相关技术支持工作
   - 前端：实现与接入设备小程序相关的技术支持工作
   - 服务端：实现对接入设备业务实现以及通过蓝牙/阿里云IOT进行服务端业务支持工作
2. 厂商对接流程

   1. 先提供给钉钉设备端人员您所使用系统平台的开发环境。

      - 如果使用的是LINUX系统，请提供该平台在LINUX环境下的交叉编译工具链。
      - 如果使用的是RTOS类的系统，请提供对应的开发编译环境，如（KEIL IAR 或者芯片厂家提供的开发IDE等）。

        对于使用KEIL，IAR等通用IDE用户，需要提供具体的芯片信息，如果集成IDE中没有您所使用的芯片库，需要您提供相关的芯片库安装插件。

        ![ARM](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9820886061/p186361.png)
   2. 钉钉设备侧同学拿到您提供的开发环境后，会将SDK编译成库的形式提供给您。LINUX平台提供动态库，非LINUX平台提供静态库。
   3. 请向钉钉服务端同学申请如下基础信息：

      | 参数 | 说明 |
      | --- | --- |
      | PRODUCT\_KEY | 产品的蓝牙绑定接入密钥 |
      | DTIOT\_DEV\_TYPE | 产品的接入类型 |
      | DTIOT\_DEVICE\_SERVE\_ID | 产品的接入型号 |
      | PRODUCT\_DEVICE\_NAME | 产品的接入名称 |

      > **[!IMPORTANT]**
      >
      > 上述信息需要在初始化SDK的时候，传给SDK，SDK附带的示例demo有详细示例。
   4. 按照本文档下面描述的要求完成对SDK的对接。
   5. 根据自己产品的相关业务和服务端同学索要物模型定义文档并在服务端和前端同学的配合下，实现您接入产品的相关业务。
   6. 自测并提交您公司的内部测试。
   7. 钉钉端测试验收。
   8. 完成产品发布上市。
   > **[!NOTE]**
   >
   > - 产品开发调试过程中，可联系钉钉同学到杭州进行联合开发，也可以远程开发。
   > - 产品上市之后的问题分析定位，需要又接入厂商自行完成，需要钉钉协助帮助的，请提供问题的复现场景以及完备的日志信息。
