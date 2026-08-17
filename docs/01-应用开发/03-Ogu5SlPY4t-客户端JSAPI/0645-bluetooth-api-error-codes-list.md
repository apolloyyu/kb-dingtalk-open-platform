---
title: "蓝牙 API 错误码对照表"
source_url: "https://open.dingtalk.com/document/development/bluetooth-api-error-codes-list"
namespace: "development"
slug: "bluetooth-api-error-codes-list"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 设备 > 蓝牙 > 蓝牙 API 错误码对照表"
doc_id: "zOfIunRZGk"
updated_at: "2025-09-17 21:00:13"
---

> Source: https://open.dingtalk.com/document/development/bluetooth-api-error-codes-list
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 设备 > 蓝牙 > 蓝牙 API 错误码对照表
> Updated: 2025-09-17 21:00:13

# 蓝牙 API 错误码对照表

| **错误码** | **说明** | **解决方案** |
| --- | --- | --- |
| 10000 | 未初始化蓝牙适配器 | 调用dd.openBluetoothAdapter。 |
| 10001 | 当前蓝牙适配器不可用 | 检查当前设备是否支持BLE并开启蓝牙功能。 |
| 10002 | 没有找到指定设备 | 检查deviceId是否错误，或者是否开启外设广播。 |
| 10003 | 连接失败 | 检查deviceId是否错误，目标蓝牙外设是否开启广播。 |
| 10004 | 没有找到指定服务 | 检查serviceId，确认目标外设是否拥有该服务。 |
| 10005 | 没有找到指定特征值 | 检查characteristId是否正确，检查目标外设特定service下是否具备该特征。 |
| 10006 | 当前连接已断开 | 连接断开，重新连接。 |
| 10007 | 当前特征值不支持此操作 | 检查特征是否具备读\写\通知等功能。 |
| 10008 | 其余所有系统上报的异常 | 其他未知错误，具体问题具体分析。 |
| 10009 | Android 系统特有，系统版本低于 4.3 不支持BLE | 提示用户不支持。 |
| 10010 | 没有找到指定描述符 | 检查serviceId、characteristId是否正确。 |
| 10011 | 设备 id 不可用/为空 | 使用正确的deviceId。 |
| 10012 | 服务 id 不可用/为空 | 使用正确的serviceId。 |
| 10013 | 特征 id 不可用/为空 | 使用正确的characteristId。 |
| 10014 | 发送的数据为空或格式错误 | 检查写数据或者HEX转化是否错误。 |
| 10015 | 操作超时 | 重新操作。 |
| 10016 | 缺少参数 | 检查调用的参数，并重新操作。 |
| 10017 | 写入特征值失败 | 写失败，检查外设特征是否支持写操作，是否断开连接。 |
| 10018 | 读取特征值失败 | 读失败，检查外设特征是否支持读操作，是否断开连接。 |
