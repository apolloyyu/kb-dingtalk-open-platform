---
title: "常见问题"
source_url: "https://open.dingtalk.com/document/development/development-building-ios-faq"
namespace: "development"
slug: "development-building-ios-faq"
group: "专属版客户端插件"
tab: "iOS 插件"
breadcrumb: "常见问题"
doc_id: "zcD8lBN06y"
updated_at: "2026-08-18 09:08:03"
---

> Source: https://open.dingtalk.com/document/development/development-building-ios-faq
> Path: 专属版客户端插件 / iOS 插件 / 常见问题
> Updated: 2026-08-18 09:08:03

# 常见问题

本章节提供一些常见问题的解决方案。

- **我提供的SDK中，依赖了开源的三方库，与钉钉有冲突怎么办？**

  SDK需要依据钉钉内现有三方库版本进行代码适配，确保在钉钉内的三方库环境下能够编译和功能正常运行。钉钉对大部分三方库都做了定制，需要适配可直接联系钉钉开发人员获得钉钉内三方库的framework进行适配。

  如果某些底层C++库实在无法适配（比如libssl），可以考虑用动态库的方式，操作方式如下：

  - 将调用方和三方库放在一起，打成一个framework，并且设置build setting中的mach-o格式为dynamic（动态库），对外统一暴露OC的类和方法。
  - 钉钉侧不会在编译阶段自动链接，不会在运行阶段自动load，需要手动加载和使用反射的方式进行调用。
  - 参考代码：

    ```
    //手动加载动态库
    + (BOOL)loadxxxxIfNeeded {
       static BOOL loaded = NO;
       if (loaded) { return YES; }
      
       NSDate *begin = [NSDate date];
       NSString *bundlePath = [[NSBundle mainBundle] bundlePath];
       NSString *path = [bundlePath stringByAppendingPathComponent:@"Frameworks/xxxx.framework/xxx"];
      
       if (path == nil) {
           NSLog(@"xxxx dose not exist");
           return NO;
       }
       void *lib = dlopen([path UTF8String], RTLD_LAZY);
       if (lib == NULL) {
           NSLog(@"xxx lazy load faile path:%@",path);
           return NO;
       }
      
       NSDate *end = [NSDate date];
       int64_t interval_ms = [end timeIntervalSinceDate:begin] * 1000;
       NSLog(@"xxx load interval:%@ms",@(interval_ms));
       loaded = YES;
       return YES;
    }
    ```

    ```
    //反射调用动态库中的内容
     Class owtConfigCalss = NSClassFromString(@"xxxxxxClass");
     xxxxxxClass* config = [[owtConfigCalss alloc]init];
     [config dosomething];
    ```

    > **[!WARNING]**
    >
    > 体积较大或者独立性不强的库不能用动态库的方式接入，否则会大量增大包的体积和库加载时长。
- **我的页面需要横屏，要怎么处理？**

  请直接覆盖ViewController的三个函数方法，并使用present的方式来展示横屏页面。

  参考代码：

  ```
  - (UIInterfaceOrientationMask)supportedInterfaceOrientations
  {
     return UIInterfaceOrientationMaskLandscapeRight;
  }

  - (UIInterfaceOrientation)preferredInterfaceOrientationForPresentation
  {
     return UIInterfaceOrientationLandscapeRight;
  }

  - (BOOL)shouldAutorotate
  {
     return NO;
  }
  ```
- **AFNetworking编译失败？**

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6567946871/p1094257.png)

  请在模块的podspec中指定spec.ios.deployment\_target = '12.0'
