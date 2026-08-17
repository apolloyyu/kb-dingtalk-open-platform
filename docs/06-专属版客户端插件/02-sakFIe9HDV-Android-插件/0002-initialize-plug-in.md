---
title: "初始化插件（MainBundle）"
source_url: "https://open.dingtalk.com/document/development/initialize-plug-in"
namespace: "development"
slug: "initialize-plug-in"
group: "专属版客户端插件"
tab: "Android 插件"
breadcrumb: "Android 插件 > 初始化插件（MainBundle）"
doc_id: "dIEoNIxWyi"
updated_at: "2026-08-12 09:20:44"
---

> Source: https://open.dingtalk.com/document/development/initialize-plug-in
> Path: 专属版客户端插件 / Android 插件 / Android 插件 > 初始化插件（MainBundle）
> Updated: 2026-08-12 09:20:44

# 初始化插件（MainBundle）

插件可能期望在App启动时完成自己的初始化任务，此时可以使用BundleApplication。

## **BundleApplication**

BundleApplication类似Android的Application，可用于插件在应用启动时初始化的场景，该类对于一个插件只能定义一个，使用@Bundle注解标注。

> **[!WARNING]**
>
> 默认所有回调函数均在主进程中调用，因此请务必不要执行耗时操作，否则可能出现ANR问题。

| **接口** | **说明** |
| --- | --- |
| **onAttachBaseApplication** | Application的attachBaseContext()事件，请谨慎使用，优先使用onApplicationCreate。 |
| **onApplicationPreCreate** | Application的onCreate() 事件，但在钉钉的初始化任务之前执行，请谨慎使用，优先使用onApplicationCreate。 |
| **onApplicationCreate** | Application.onCreate() 事件，在钉钉的核心初始化任务执行完成后执行，建议业务SDK的初始化放在该事件中。 |
| **runInProcess** | 需要回调的进程。默认都在钉钉主进程中回调，如果期望在所有进程中调用，可重写该方法并返回ProcessName.ALL; 如果需要在钉钉子进程中回调，可重写该方法并返回ProcessName.SUB。子进程回调只支持onAttachBaseApplication、onApplicationPreCreate和onApplicationCreate方法。 |

## **BundleContext**

BundleContext类实例仅能在BundleApplication初始化回调接口时获取，开发者不能直接实例化。该类提供了插件上下文信息。

| **接口** | **功能说明** |
| --- | --- |
| getApplication() | 可获取App的Application对象。 |
| invokeApi() | 调用开放API（异步API），API清单请参考《使用开放API》章节 |
| invokeSyncApi() | 调用开放API（同步API），API清单请参考《使用开放API》章节 |
| getBundleId() | 获取BundleID |
| getService() | 获取服务（Service） |

## **如何使用**

钉钉开发者工具包中提供了自动生成并初始化工程的能力，开发者使用后会默认创建一个BundleApplication的模板代码：MainBundle类，开发者可根据需求添加自己的代码。如下图示例：

```
@Bundle
  public class MainBundle extends BundleApplication {

    // 该值需要同钉钉方提前约定，务必与bundle.xml保持相同，请不要随意修改
    public static final String BUNDLE_ID = "P_security_8ecc1d9_example_plugin";

    private static BundleContext bundleContext;

    public static BundleContext getBundleContext() {
      return bundleContext;
    }

    @Override
    public String getBundleId() {
      return BUNDLE_ID;
    }

    @Override
    public void onApplicationCreate(BundleContext context) {
      // 此处可添加插件初始化代码
    }
  }
```
