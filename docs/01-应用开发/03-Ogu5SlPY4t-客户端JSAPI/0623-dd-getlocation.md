---
title: "获取用户当前的地理位置信息"
source_url: "https://open.dingtalk.com/document/development/dd-getlocation"
namespace: "development"
slug: "dd-getlocation"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 位置 > 获取用户当前的地理位置信息"
doc_id: "ZPtRXBntMi"
updated_at: "2025-09-17 20:59:57"
---

> Source: https://open.dingtalk.com/document/development/dd-getlocation
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 位置 > 获取用户当前的地理位置信息
> Updated: 2025-09-17 20:59:57

# 获取用户当前的地理位置信息

调用dd.getLocation获取用户当前的地理位置信息。

## 扫码体验

![1595556011116-11](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3445382061/p174267.png)

## **示例****代码**

```
dd.getLocation({
      success(res) {
        this.setData({
          hasLocation: true,
          location: formatLocation(res.longitude, res.latitude)
        })
      },
      fail() {
        dd.alert({ title: '定位失败' });
      },
    })
```

## **入参**

| **参数** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| cacheTimeout | Number | 否 | 钉钉客户端经纬度定位缓存过期时间，单位秒。使用缓存会加快定位速度，缓存过期会重新定位。  **默认值**：30s |
| type | Number | 否 | 获取经纬度和详细到区县级别的逆地理编码数据。   - **0**：获取经纬度 - **1**：默认 |
| success | Function | 否 | 调用成功的回调函数。 |
| fail | Function | 否 | 调用失败的回调函数。 |
| complete | Function | 否 | 调用结束的回调函数（调用成功、失败都会执行）。 |

**success返回值**

| **名称** | **类型** | **描述** |
| --- | --- | --- |
| longitude | String | 经度。 |
| latitude | String | 纬度。 |
| accuracy | String | 精确度，单位 米。 |
| province | String | 省份，type>0生效。 |
| city | String | 城市，type>0生效。 |
| address | String | 格式化地址，type>0生效。如：北京市朝阳区南磨房镇北京国家广告产业园区。 |

## **错误码**

| **错误码** | **描述** | **解决方案** |
| --- | --- | --- |
| 11 | 请确认定位相关权限已开启 | 提示用户打开定位权限。 |
| 12 | 网络异常，请稍后再试 | 提示用户检查当前网络。 |
| 13 | 定位失败，请稍后再试 | - |
| 14 | 业务定位超时 | 提示用户再次尝试。 |
