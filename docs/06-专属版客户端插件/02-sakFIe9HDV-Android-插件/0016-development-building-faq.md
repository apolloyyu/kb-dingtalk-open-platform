---
title: "常见问题"
source_url: "https://open.dingtalk.com/document/development/development-building-faq"
namespace: "development"
slug: "development-building-faq"
group: "专属版客户端插件"
tab: "Android 插件"
breadcrumb: "常见问题"
doc_id: "3qecXiEAyN"
updated_at: "2026-08-12 09:20:56"
---

> Source: https://open.dingtalk.com/document/development/development-building-faq
> Path: 专属版客户端插件 / Android 插件 / 常见问题
> Updated: 2026-08-12 09:20:56

# 常见问题

本章节提供一些常见问题的解决方案。

## **开发 Android 插件**

- **自定义的JsApi不生效**

  - **现象**

    Bundle里定义了JsModule，但相关的JsApi调用时没有反应，调试也运行不到JsMethod中？
  - **常见原因**

    - **JSAPI没有正确注册到钉钉框架中**

      在老版本的编译工具中，JsApi需要显式在自定义JsServicePlugin中注册，很多开发者只定义了JsModule和JsSubject，但忘记定义JsServicePlugin，导致JsModule未注册到钉钉框架中，因此JS调用是无法调用到SDK。
    - **H5应用调用是传入的参数错误**

      经常会遇到H5应用调用JsApi时传入的"bundle\_id"参数和插件SDK中定义的不一致。
    - **编译插件问题**

      当各种方式均已确认正常但在调试环境中调用仍存在问题，请先确认编译插件版本是否是官网文档中最新版本，如果是，请删除本地定义的JsServicePlugin子类（该类在新版中已废弃），并重新构建尝试。
  - **自查方法**

    假如你使用的是调试环境构建的包，或者测试环境构建的包，请到钉钉 “设置” - “开发者控制台” - “JSAPI清单”，点开后如果页面为空，代表你的插件在注册JSAPI时异常，未能正确注册到平台中导致无法识别。同时对比该页面中的参数和前端调用传入的是否一致。
- **常见的编译错误**

  > **[!NOTE]**
  >
  > Android Studio存在cache，假如你已经按照错误提示修正了代码，但仍报错，请先使用clean，然后重新构建。

  - AndroidManifest.xml文件，请避免配置allowBackup、tool:replace等属性，该节点属性应尽可能为空，只包含子节点（Activity、Service等），避免和钉钉冲突导致集成编译失败。

    ```
    <application>  	<!-- 建议application节点不要添加任何参数-->

      <!-- 如果依赖了某个sdk的miniSDKVersion和钉钉不一致，
      请配置overrideLibrary属性-->
      <uses-sdk
        android:minSdkVersion="21"
        android:targetSdkVersion="29"
        tools:overrideLibrary="com.airbnb.lottie"/>

      <meta-data
        android:name="example_key"
        android:value="example_value" />

      <activity
        android:name="com.example.DemoActivity"
        android:launchMode="singleTop"
        android:screenOrientation="portrait"/>

    </application>
    ```
  - 如果使用了FileProvider，请自定义class并继承FileProvider，避免直接在AndroidManifest文件中配置FileProvider，同时配置的resource.xml文件建议附带sdk.tag的命名，避免文件名冲突。

    > **[!IMPORTANT]**
    >
    > 此处android:resource定义的path文件命名**请务必追加自定义前缀**，避免使用常规命名被覆盖。

    ```
    // 建议改为如下形式
    <provider
      // 此处Provider命名请使用自定义Provider类	
      android:name="com.example.DemoFileProvider"
      android:authorities="com.example.fileprovider"
      android:exported="false"
      android:grantUriPermissions="true">
      <meta-data
        android:name="android.support.FILE_PROVIDER_PATHS"
        android:resource="@xml/example_paths" />  
      //此处android:resource的文件名命名请注意，避免重复！！！
    </provider>
    ```
- **ERROR::no valid apt file dingtalk-bundle.xml found, hook failed ！**

  该问题通常是编译时钉钉构建插件发现不合法的配置等，比如：@Extension 注解的ID不能重复出现的冲突失败；注解缺失;类文件被标记成了final。

  ![image_a78598d0ccco](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7698314861/p610885.png)

  可翻找打包日志详情，会有具体错误描述，可参考修改，如下图为ID冲突错误：

  ![image_a785e6f2ccwu](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7698314861/p610887.png)
- **Execution failed for task ':demo-bundle:transformClassesWithBundle-module-transformForDebug'**

  该问题也是打包插件插件的编译错误，通常也是由于钉钉构建插件校验规则失败导致。比如注解相关修饰类不能是private、final等。

  请点击Android Studio打包日志详情查看具体错误信息。

  ![image_a7863513ccui](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7698314861/p610886.png)
- **NoClassDefFoundError**

  通常该问题是两个原因引起：

  - **混淆导致**：通常发生在代码使用到反射（比如涉及到glide、fastjson等）的场景，假如你的类没有正确配置keep规则，有可能会出现类找不到（因为被混淆了）。请参考“自定义混淆规则”的章节描述，正确配置sdk的混淆配置。
  - **SDK未被正确打包集成**：通常发生在你的工程依赖了其他SDK的场景。在分析原因之前，请先了解插件包（\*.deb）文件的基本原理。deb文件理论上应该包含插件集成时所有的依赖信息，比如依赖的自研SDK、三方库等。当你的依赖库没有正确声明时（即不在deb描述信息中），则会发生 NoClassDefFoundError的问题：

    - 插件工程打包时，会将工程 ./libs 目录下的所有aar以及jar文件共同打包到deb文件中（可以解压deb文件确认），对于本地依赖的sdk请直接放到bundle工程的libs目录中引用，不可自行配置成其他路径。
    - deb中包含了BundleManifest.xml，该文件里面描述了插件关联的所有maven仓库依赖清单（可解压deb文件确认是否正确）。假如你依赖的不在清单中，请参考“发布产物”章节描述，并在bundle.xml中添加相关的依赖清单（<implimentation>节点）。

## **开发 IOS 插件**

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
