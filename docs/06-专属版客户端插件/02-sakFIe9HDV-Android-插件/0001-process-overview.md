---
title: "开发 Android 插件"
source_url: "https://open.dingtalk.com/document/development/process-overview"
namespace: "development"
slug: "process-overview"
group: "专属版客户端插件"
tab: "Android 插件"
breadcrumb: "开发 Android 插件"
doc_id: "L59bQVLpsB"
updated_at: "2026-08-12 09:20:40"
---

> Source: https://open.dingtalk.com/document/development/process-overview
> Path: 专属版客户端插件 / Android 插件 / 开发 Android 插件
> Updated: 2026-08-12 09:20:40

# 开发 Android 插件

本流程概览介绍了从零创建并开发一个客户端Android 插件。本流程概览将提供一个自定义水印插件的示例，帮助你快速掌握开发客户端插件。

## **预期效果**

- 我们将开发一个自定义水印的插件，可显示水印“客户端演示插件”。
- 我们将在设置中新增一个“客户端演示插件设置”的自定义设置项，用于配置我们的水印功能。

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2084449771/p489027.png)![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2084449771/p489026.png)

**示例工程**：[单击下载示例代码](https://exclusive-app-cdn.dingtalk.com/exclusive_plugin_client_bundle-DingTalk-OpenDevKit-23.0811.zip_1691736775493.zip?spm=ding_open_doc.document.0.0.3d8113b4fxSxht&file=exclusive_plugin_client_bundle-DingTalk-OpenDevKit-23.0811.zip_1691736775493.zip)

## **开发插件**

### **使用Dingtalk DevKit工具**

#### **下载并复制**

下载 [最新的 Dingtalk DevKit 版本插件](https://exclusive-app-cdn.dingtalk.com/exclusive_plugin_client_bundle-DingTalk-OpenDevKit-23.0811.zip_1691736775493.zip?spm=ding_open_doc.document.0.0.4b87332b5Dl274&file=exclusive_plugin_client_bundle-DingTalk-OpenDevKit-23.0811.zip_1691736775493.zip)（注意不需要解压），将下载的zip文件拷贝到固定目录中。

> **[!NOTE]**
>
> - 拷贝到固定目录后，不要删除文件。
> - Dingtalk DevKit 是一个 Android Studio IDEA 插件，可用于辅助创建工程、生成代码以及辅助开发等。

#### **安装 Dingtalk DevKit 工具**

**Windows 系统：**

1. 打开 Plugins 菜单：

   - 在 Android Studio 的 Welcome 界面中单击 **Plugins**，进入插件菜单。
   - 进入 Android Studio，单击 **File** > **Settings** > **Plugins，**进入插件菜单 。

     | **Welcome启动界面入口** | **AndroidStudio里面的File菜单入口** |
     | --- | --- |
     | image |  |
2. 单击设置图标，并单击 **Install plugin from Disk**，选择已经下载好的 Dingtalk DevKit.zip 文件，安装并重启 IDE。

**Mac系统**：

1. 打开 Plugins 菜单：

   - 在 Android Studio 的 Welcome 界面中单击 **Plugins**，进入插件菜单。
   - 进入 Android Studio，单击 **Preferences** > **Plugins，**进入插件菜单 。
2. 单击设置图标，并单击 **Install plugin from Disk** ，选择已经下载好的 Dingtalk DevKit.zip 文件，安装并重启 IDE。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0467946871/p1094222.png)

### **创建插件工程**

1. 单击![设置按钮IDE.jpg](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7122489961/p732037.jpg) > **Create Dingtalk Bundle Project**。

   ![](https://alidocs.oss-accelerate.aliyuncs.com/res/NybEnBQEjLLPlP13/img/0687285c-d940-4554-bafd-7e34508257ae.tif?x-oss-process=image/format,jpeg/auto-orient,1#7962)
2. 进入创建工程界面，填写参数信息。

   | **配置项** | **说明** |
   | --- | --- |
   | Project Location | 项目位置。 |
   | Project Name | 项目名称。 |
   | Bundle Name | 插件名称。 |
   | Bundle ID | 插件的 ID。平台用于识别插件身份的ID，可自定义。  **[!IMPORTANT]**  - 为了避免重复，我们建议采用类似“公司\_产品”的格式填写。支持字母、数字、下划线，请勿使用其他特殊字符。 - 如果插件是多端的（比如Android、iOS），请务必使用相同的值。 - 禁止包含“DingTalk”、“Alibaba”等钉钉相关特殊字符串。 - 如果期望调整Bundle ID，代码中请同时修改 MainBundle.java、bundle.xml 中的值。 |
   | Package Name | 包的名称。 |

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5648114861/p632057.png)
3. 单击 Finish，你就完成了插件工程的初始化了。

### **编写插件功能**

1. 在 MainBundle 中的 `onApplicationCreate` 方法中添加初始化代码，注册 Activity 生命周期回调，并为所有恢复的 Activity 注入水印。

   ```
   @Bundle
     public class MainBundle extends BundleApplication {
   		
       ... ...
       
       @Override
       public void onApplicationCreate(BundleContext context) {
         super.onApplicationCreate(context);
         this.bundleContext = context;   // 该行不要删除

         context.getApplication().registerActivityLifecycleCallbacks(new Application.ActivityLifecycleCallbacks() {
               
           @Override
           public void onActivityResumed(@NonNull Activity activity) {
             Watermark.show(activity);
           }				
           ... ...
         });
       }
     }
   ```
2. 使用“设置”扩展点添加自定义设置菜单项。通过 Dingtalk DevKit 工具中的**New Extension**功能创建扩展实现类，选择扩展类型为 **EpSettingMenu**。

   下图为使用 DevKit 创建 EpSettingMenu 扩展的界面示例：

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2207553661/p488904.png)
3. 补充设置菜单实现。

   ```
   @Extension(id = "example_securit_setting", target = "setting_items")
     public class ExampleSettingMenu extends EpSettingMenu {

       @Override
       public SettingMenuObject getMenuObject() {
         SettingMenuObject menu = new SettingMenuObject();
         menu.title = "演示设置";
         return menu;
       }
       
       ... ...
       
       @Override
       public void onClick(View v) {
         // 此处可startActivity，打开自定义的Activity
         // Demo工程演示效果
         Toast.makeText(v.getContext(), "点击自定义设置菜单", Toast.LENGTH_SHORT).show();
       }
     }
   ```
4. （可选）打开项目中`consumer-rules.pro` 文件，并在文件中补充必要的混淆规则。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2207553661/p488943.png)

   > **[!NOTE]**
   >
   > - 1. 如涉及到Gson等反射场景时，请务必添加Keep规则。
   > - 2. 请不要添加通用规则，仅添加插件代码相关Keep规则。

### **编译生成产物（\*.deb）**

> **[!NOTE]**
>
> 建议同时阅读[配置插件依赖项](0003-client-specific-configuration-plugin-dependencies.md)章节，了解钉钉的插件构建产物配置说明。

1. 使用 Task “publishBundle” 编译构建，如下图：

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5648114861/p632072.png)
2. 构建完成后，我们在 ./outputs/bundle 目录中可以看到产物结果。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5648114861/p632073.png)
3. 至此，你已经完成了第一个插件的开发。

### **调试插件**

> **[!NOTE]**
>
> 钉钉平台为开发者提供了客户端插件的调试环境，使用调试环境可以将插件SDK同钉钉基线包合并生成可调试的APK文件。
>
> - 调试环境裁剪掉了部分功能，比如电话、会议、ding、邮箱、考勤等
> - 调试环境包与最终集成包由于集成方式不同，可能会存在集成时编译失败以及部分功能异常

1. 扫码加入“钉钉native定制扩展开放”组织，申请通过后单击[下载最新的调试环境](https://alidocs.dingtalk.com/i/nodes/AY39rGpMPmeVNOPZZKloJOZkXKnaoNQ7)。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8648114861/p632059.png)

   > **[!NOTE]**
   >
   > 申请时请务必明确说明：开发者所在公司 + 开发的项目。未说明的将不予通过。
2. 安装调试环境：

   1. 解压调试环境文件到任意目录（建议统一放到钉钉插件的工作空间目录中），你可以看到 “Android-MergeApp”工程目录。

      ![image_a5c13080ccaj](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4434731861/p610529.png)

      | **核心目录项** | **说明** |
      | --- | --- |
      | source | 用于放置客户端插件包文件（\*.deb），**插件开发完成后请拷贝产物到该目录中。** |
      | outputs | 合并插件后的产物目录，不需要做处理。 |
      | host | 钉钉基线包，不需要做处理。 |
   2. 配置环境，假如你是Windows电脑，请打开merge-install.bat文件，并修改下图中的参数：![image_f1d33812ccqi](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4434731861/p610533.png)

      - ANDROID\_SDK\_DIR：请参考安卓工程中的 local.properties，修改成安卓 sdk 根目录
      - ANDROID\_SDK\_BUILD\_TOOL\_DIR：请参考你的电脑 Android SDK目录中 build-tools 子目录，将版本“28.0.3”改成你的电脑中存在的任意一个存在的版本（如下图所示）。

        ![image_f1d38630cc58](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4434731861/p610532.png)
3. 打包插件：

   1. 构建 Bundle 工程，生成客户端插件 \*.deb 文件，并把最新的插件包拷贝到调试环境的 ./source 目录中。
   2. 使用 AndroidStudio 打开调试环境工程，并打开底部的 Ternimal 面板执行脚本：

      - Mac系统： `./merge-install` （如果报错请先执行 `chmod 777 ./merge-install` ）。
      - Windows：`merge-install.bat`。

      执行结束后可以在outputs目录中看到打包产物 “dingtalk\_signed.apk”。安装后可以看到手机桌面多出一个“专属钉钉开发版”，点开运行可验证插件功能。

      ![image_7ada4270cctj](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4434731861/p610541.png)
4. 申请授权，调试环境首次登录或者长时间未登录时，会需要申请授权使用，请完整填写信息并申请授权。

   > **[!IMPORTANT]**
   >
   > 申请时请明确说明你所在的公司以及负责开发的钉钉插件项目名称，信息不完整的将不予通过。

   ![image_457e9770ccod](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4434731861/p610537.png)![image_457e9771ccxv](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4434731861/p610539.png)![image_457ebe80cceo](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4434731861/p610538.png)

   申请后通常当天会处理完成，可等1个小时或更久再重新登录确认是否授权通过。
5. 调试代码，运行“专属钉钉开发版” App ，打开 Bundle 工程代码，并运行 Android Studio 的“ Attach Debugger to Android Process ”，按照下图选择专属钉钉开发版进程，这样便可关联上代码并调试运行。

   ![image_f3b6cfb3cczc](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4434731861/p610544.png)

## **相关信息**

### **调试自定义扩展JSAPI**

假如你的插件中自定义了扩展JSAPI，可以使用钉钉官方提供的小程序完成JSAPI调用测试。

- 工作台请切换到“钉钉Native定制扩展开放”组织
- 单击工作台应用“专属插件JSAPI调试”

如下图：

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8648114861/p632060.png)![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8648114861/p632061.png)

### **DevKit辅助**

每次插件包构建完成后，手工拷贝到调试环境总是比较麻烦，为此开发者工具（DevKit）提供了绑定调试环境的功能，如下图：

![image..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9515096861/p678030.png)

- 单击重置：设置调试环境目录
- Copy Bundle to Debug Env：将已经构建好的插件包（\*.deb）拷贝到绑定的调试环境中
- Merge Install APK：合并bundle并安装APK到手机中（请先链接ADB）

### **辅助问题排查**

调试环境也提供了一些辅助功能，可用于辅助排查问题。

1. 单击首页加号菜单或者设置页 > 开发者中心。
2. 单击“查看SDK中定义的JSAPI清单”：可展示自定义JSAPI清单，常用于验证钉钉插件中自定义的JSAPI能够被钉钉平台识别。

   ![image_2fd7e0b0cc4v](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4434731861/p610547.png)![image_854896c0ccz2](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4434731861/p610552.png)

## **常见问题**

### **开发中的编译问题**

- **AndroidManifest.xml 配置限制**

  请避免在 `<application>` 标签中配置 `android:allowBackup`、`tools:replace` 等属性，该节点应尽可能为空，仅包含子组件（如 Activity、Service）。否则可能导致与宿主钉钉冲突而编译失败。

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
- **FileProvider 使用规范**

  若需使用 FileProvider，请继承FileProvider并自定义类class，避免直接在AndroidManifest文件中配置FileProvider。同时，`android:resource` 引用的 XML 路径文件建议添加唯一前缀（如 `sdk.tag`），避免文件名冲突。

  > **[!IMPORTANT]**
  >
  > 此处 `android:resource` 定义的 path 文件命名**请务必追加自定义前缀**，避免使用常规命名被覆盖。

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

### **so架构引入**

新引入的 so 文件必须提供 32 位与 64 位两个版本，即`armeabi-v7`、 `arm64-v8a`两种版本。

如遇 so 冲突，可从[钉钉官网](https://open.dingtalk.com/document/direction/www.dingtalk.com)下载最新版本，解压后查看 `lib/` 目录是否存在同名 so 文件。如果有请验证使用钉钉的版本是否存在功能异常。

### **外部依赖三方SDK冲突**

- **禁止将第三方 jar 包直接打包进插件 SDK**，否则会导致集成时出现类重复问题。
- 所有开源库应通过 Maven 仓库坐标方式引入。
- 当存在相同依赖但版本不一致时，优先适配钉钉当前使用的版本；若业务强依赖特定版本，请联系钉钉技术确认解决方案。

### **Support库版本适配**

钉钉已经使用AndroidX版本，请确认你的插件是否适配。参考版本：

```
androidx.activity:activity:1.1.0@aar
androidx.appcompat:appcompat:1.2.0@aar
androidx.arch.core:core-common:2.1.0@jar
androidx.arch.core:core-runtime:2.1.0@aar
androidx.browser:browser:1.0.0@aar
androidx.cardview:cardview:1.0.0@aar
androidx.constraintlayout:constraintlayout:1.1.3@aar
androidx.coordinatorlayout:coordinatorlayout:1.0.0@aar
androidx.core:core:1.3.2@aar
androidx.customview:customview:1.0.0@aar
androidx.documentfile:documentfile:1.0.0@aar
androidx.drawerlayout:drawerlayout:1.0.0@aar
androidx.exifinterface:exifinterface:1.0.0@aar
androidx.fragment:fragment:1.2.0@aar
androidx.media:media:1.0.0@aar
androidx.palette:palette:1.0.0@aar
androidx.recyclerview:recyclerview:1.0.0@aar
androidx.savedstate:savedstate:1.0.0@aar
androidx.slidingpanelayout:slidingpanelayout:1.0.0@aar
androidx.swiperefreshlayout:swiperefreshlayout:1.0.0@aar
androidx.vectordrawable:vectordrawable:1.1.0@aar
androidx.viewpager:viewpager:1.0.0@aar
androidx.webkit:webkit:1.3.0@aar
androidx.window:window:1.1.0-alpha03@aar
com.alibaba:fastjson:1.1.71.android@jar
com.google.android.material:material:1.0.0@aar
com.google.android.play:core:1.8.3@aar
com.google.android:flexbox:1.0.0@aar
com.google.code.gson:gson:2.2.4@jar
com.google.dagger:dagger:2.23@jar
com.squareup.okhttp3:okhttp:3.11.0@jar
io.reactivex.rxjava2:rxandroid:2.0.2@aar
org.jetbrains.kotlin:kotlin-stdlib:1.7.10@jar
org.jetbrains.kotlinx:kotlinx-coroutines-android:1.6.1@jar
org.jsoup:jsoup:1.8.2@ja
```

### **调试插件**

- **使用调试环境集成deb后，调试时无法执行到插件代码**

  对于早期的\*.deb文件调试环境是无法支持的，因此需要使用最新版本的工具构建生成新的\*.deb并重新尝试调试。
- **编译失败**

  如遇到类似“Could not initialize class org.codehaus.groovy.reflection.ReflectionCache”的编译gradle异常时，可尝试升级最新版本Android Studio解决。
- **调试环境运行Crash，类找不到问题**

  NoClassDefFoundError 问题，通常是由于deb包信息缺失引起，请参考文档[常见问题](0016-development-building-faq.md#f9502a802etoo)解决。
- **调试环境已经验证通过了，集成包会遇到编译失败或者功能异常**

  由于集成环境和调试环境集成原理不同，集成打包时有可能遇到编译代码冲突等问题，因此：

  1. 请先确认你的插件SDK中是否将一些通用的三方库源码打进来了，如果是请先删除并使用maven远程坐标依赖的方式引入。
  2. 功能异常请先确认代码是否执行，可通过日志确认。如果插件没有执行输出任何日志，那么极大可能是打包时插件没有参与编译打进去，请到打包平台确认配置是否正常。
  3. 如果插件代码输出了日志，但功能表现异常，请确认混淆配置是否正确配置，可能由于你的代码存在反射场景，但混淆配置未正确配置。
