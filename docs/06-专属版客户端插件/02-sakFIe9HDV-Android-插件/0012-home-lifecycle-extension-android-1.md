---
title: "首页生命周期扩展（Android）"
source_url: "https://open.dingtalk.com/document/development/home-lifecycle-extension-android-1"
namespace: "development"
slug: "home-lifecycle-extension-android-1"
group: "专属版客户端插件"
tab: "Android 插件"
breadcrumb: "使用扩展点 > 首页生命周期扩展"
doc_id: "tH6cnJnKWs"
updated_at: "2025-10-15 17:02:21"
---

> Source: https://open.dingtalk.com/document/development/home-lifecycle-extension-android-1
> Path: 专属版客户端插件 / Android 插件 / 使用扩展点 > 首页生命周期扩展
> Updated: 2025-10-15 17:02:21

# 首页生命周期扩展（Android）

## **基础信息**

| **扩展点编码** | **接口类** | **支持的平台** |
| --- | --- | --- |
| home\_lifecycle | HomeLifecyclePlugin | Android |

## **功能说明**

钉钉首页是常驻于进程中的Tab容器Activity，通常在应用重启、账密登录完成后创建并执行扩展插件的接口回调。该插件可用于监听钉钉首页的生命周期，常用于在首页创建时执行操作，比如期望在钉钉进程重启后建立VPN通道的场景（通过Activity的startActivityForResult方式启动VPNService）。

## **接口说明**

| **名称** | **说明** |
| --- | --- |
| onCreate() | 首页Activity的onCreate回调事件，UI线程中调用，请避免耗时操作 |
| startActivityForResult() | requestCode取值范围必须为 [0,100) |
| onActivityResult() | 首页onActivityResult回调事件, UI线程中调用，请避免耗时操作 |

> **[!IMPORTANT]**
>
> HomeLifecycle的插件中请务必不要添加耗时任务，如果存在耗时操作请独立创建线程执行，避免阻塞主线程导致ANR。

## **代码示例**

Java

```
@Extension(id="example_homelifecycle", target="home_lifecycle")
public class DemoHomeLifecycleExtension extends HomeLifecyclePlugin {

    private static final String BUNDLE_ID = "demo_sdk";
    // 取值范围：[0, 100)
    private static final int REQUEST_CODE = 1;

    @Override
    public void onCreate(IExtensionWrapperActivity activity) {
        if (activity == null) {
            return;
        }
        Intent intent = activity.createIntent(DemoActivity.class);
        activity.startActivityForResult(APP_ID, intent, REQUEST_CODE);
    }

    @Override
    public void onActivityResult(int requestCode, int resultCode, Intent data) {
    }

    @Override
    public String getBundleId() {
        return BUNDLE_ID;
    }
}
```
