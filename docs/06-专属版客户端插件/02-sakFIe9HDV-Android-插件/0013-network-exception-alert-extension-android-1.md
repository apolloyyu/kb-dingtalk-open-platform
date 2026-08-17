---
title: "网络异常提醒扩展（Android）"
source_url: "https://open.dingtalk.com/document/development/network-exception-alert-extension-android-1"
namespace: "development"
slug: "network-exception-alert-extension-android-1"
group: "专属版客户端插件"
tab: "Android 插件"
breadcrumb: "使用扩展点 > 网络异常提醒扩展"
doc_id: "0StAFpurmg"
updated_at: "2025-10-15 17:02:23"
---

> Source: https://open.dingtalk.com/document/development/network-exception-alert-extension-android-1
> Path: 专属版客户端插件 / Android 插件 / 使用扩展点 > 网络异常提醒扩展
> Updated: 2025-10-15 17:02:23

# 网络异常提醒扩展（Android）

## **基础信息**

| **扩展点编码** | **接口类** | **支持的平台** |
| --- | --- | --- |
| home\_network\_err\_banner | EpNetworkErrBanner | Android |

## **功能说明**

当没有网络时，钉钉首页顶部会弹出一个网络异常提醒Banner，当开发者提供的插件是网络相关的服务时，则可能期望点击时能够跳转到自定义的网络设置页面。该扩展点则提供了相关扩展能力，开发者可自定义点击响应事件。

![image_d7c6b230ccy0](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0490535861/p610890.png)

## **接口说明**

| **名称** | **说明** |
| --- | --- |
| boolean onClick() | 返回值：   - true代表拦截点击事件，不再执行钉钉的默认点击响应； - false代表不拦截，执行完SDK的自定义扩展响应后，会继续执行钉钉的默认点击响应。 |

## **代码示例**

Java

```
@Extension(id = "example_network_err", target="home_network_err_banner")
public class NetErrExtension extends EpNetworkErrBanner {

    @Override
    public boolean onClick(View v) {
        ToastUtils.show(v.getContext(), "net扩展");
				return true;	// 请注意返回值代表的意义
    }
}
```
