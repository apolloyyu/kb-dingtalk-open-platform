---
title: "蓝牙概览"
source_url: "https://open.dingtalk.com/document/development/bluetooth-overview"
namespace: "development"
slug: "bluetooth-overview"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 设备 > 蓝牙 > 蓝牙概览"
doc_id: "Txe5MdPrdP"
updated_at: "2025-09-17 21:00:12"
---

> Source: https://open.dingtalk.com/document/development/bluetooth-overview
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 设备 > 蓝牙 > 蓝牙概览
> Updated: 2025-09-17 21:00:12

# 蓝牙概览

对于有蓝牙接入需求的开发者，需要通过以下步骤完成蓝牙接入，其中涉及的蓝牙API在本文API列表有详细说明。

> **[!NOTE]**
>
> 安卓下部分机型需要有位置权限才能搜索到设备，需留意是否开启了位置权限。

## 业务流程图

![1534131295514-c0cc5b9b-b2bf-48a3-a66a-32690bf4af05.png ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7454199951/p163572.png)

## 基本流程

1. 初始化蓝牙接口(dd.openBluetoothAdapter)
2. 初始化事件监听

   - 蓝牙适配器状态监听(dd.onBluetoothAdapterStateChange)
   - 蓝牙发现事件监听(dd.onBluetoothDeviceFound)
   - 蓝牙连接状态事件监听(dd.onBLEConnectionStateChanged)
3. 搜索设备(dd.startBluetoothDevicesDiscovery)
4. 查找设备并连接(dd.connectBLEDevice)
5. 停止搜索设备(dd.stopBluetoothDevicesDiscovery)
6. 遍历蓝牙外设服务和特征

   - 获取服务(dd.getBLEDeviceServices)
   - 获取特征(dd.getBLEDeviceCharacteristics)
7. 监听特征值变化事件通知(dd.onBLECharacteristicValueChange)
8. 设置读特征通知模式(dd.notifyBLECharacteristicValueChange)
9. 读写数据

   - 向设备的特征值写数据(dd.writeBLECharacteristicValue)
   - 向设备的特征值读数据(dd.readBLECharacteristicValue)
10. 断开连接(dd.disconnectBLEDevice)
11. 关闭蓝牙适配器(dd.closeBluetoothAdapter)

## 示例代码

```
//开始搜索
dd.startBluetoothDevicesDiscovery({
  services: ['fff0'],
  success: (res) => {
    console.log(res)
  },
  fail:(res) => {
  },
  complete: (res)=>{
  }
});

//断开连接
dd.disconnectBLEDevice({
  deviceId: deviceId,
  success: (res) => {
    console.log(res)
  },
  fail:(res) => {
  },
  complete: (res)=>{
  }
});

//注销事件
dd.offBluetoothDeviceFound();
dd.offBLEConnectionStateChanged();
dd.offBLECharacteristicValueChange();

//退出蓝牙模块
dd.closeBluetoothAdapter({
  success: (res) => {
  },
  fail:(res) => {
  },
  complete: (res)=>{
  }
});
```
