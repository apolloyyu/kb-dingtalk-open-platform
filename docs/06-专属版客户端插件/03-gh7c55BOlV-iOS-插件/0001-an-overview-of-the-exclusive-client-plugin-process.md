---
title: "开发 iOS 插件"
source_url: "https://open.dingtalk.com/document/development/an-overview-of-the-exclusive-client-plugin-process"
namespace: "development"
slug: "an-overview-of-the-exclusive-client-plugin-process"
group: "专属版客户端插件"
tab: "iOS 插件"
breadcrumb: "开发 iOS 插件"
doc_id: "ShJGbuVEHv"
updated_at: "2026-08-12 09:20:41"
---

> Source: https://open.dingtalk.com/document/development/an-overview-of-the-exclusive-client-plugin-process
> Path: 专属版客户端插件 / iOS 插件 / 开发 iOS 插件
> Updated: 2026-08-12 09:20:41

# 开发 iOS 插件

本文档详细介绍了从零开始创建并开发一个钉钉客户端开发 iOS 插件的完整流程，特别针对iOS平台进行说明。通过本指南，开发者可系统掌握如何构建一个可在钉钉环境中运行的本地功能插件，并实现与前端页面的JSAPI交互。

## **预期效果**

本文以开发一个用于预览本地文件的自定义JSAPI为例，展示完整的插件开发流程。该JSAPI将允许前端H5应用在钉钉客户端中唤起系统文件选择器，并实现所选文件的查看与预览功能。

- 开发名称为“demo.localfile.preview”的JSAPI，前端应用可调用该JSAPI唤起文件选择界面。
- 用户选择文件后可打开并预览文件内容。

  ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7214602961/p705756.png)![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7214602961/p705757.png)![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7214602961/p705764.png)

## **准备开发环境**

### **开发环境说明**

| iOS版本号 | >= iOS 12.0 |
| --- | --- |
| Xcode | >= 14.1 |
| Cocoapods | 1.11.3 |

### **下载开发调试工具**

请先扫码加入“钉钉native定制扩展开放”组织，申请通过后单击[开发与调试工具](https://alidocs.dingtalk.com/i/nodes/D1YKdxGX7EqVQYOLN2jmVe4QrZk95AzP?# 「开发与调试工具」)，并在下载文档中钉钉iOS端开发调试工具以及示例代码。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8648114861/p632059.png)

> **[!IMPORTANT]**
>
> **申请时请务必明确说明：****开发者所在公司 + 开发的项目。未说明的将不予通过。**

## **创建插件工程**

### **创建Framework插件**

1. 安装并启动Xcode后，在启动界面找到并单击“Create a new Xcode project”，如下示意图：

   ![截屏2023-08-11 14.05.25.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6214602961/p705218.png)
2. 进入创建工程界面，选择“Framework”，填入相关信息以完成创建。模块名称规范：DTK+[your project name] ，例如 DTKDemoFramework。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6214602961/p705383.png)
3. 在终端使用命令 cd 进入 DTKDemoFramework 文件夹，执行以下Shell命令，创建 podspec 文件。

   ```
   # pod spec create [yourAppName]
   # 此处以DTKDemoFramework为例
   pod spec create DTKDemoFramework
   ```
4. 创建完成 podspec 文件之后，需要将相关字段修改为自己公司的信息，并且引入钉钉侧的依赖。可以参考以下 podspec 内容：

   ```
   Pod::Spec.new do |s|
       s.name         = "DTKDemoFramework"
       s.version      = "1.0.0"
       s.summary      = "DingTalk DTKDemoFramework Module."

       s.description  = <<-DESC
                        DingTalk DTKDemoFramework Module.
                        DESC

       s.homepage     = "http://gitlab.yourcompany.com/DTKDemoFramework"
       s.license      = {
         :type => 'Copyright',
         :text => <<-LICENSE
                yourcompany copyright
         LICENSE
       }
       s.authors      = { "NoName" => "noname@yourcompany.com" }
       
       #platform 不能高于12.0
       s.platform     = :ios, "10.0"
       s.source       = { :git => "git@gitlab.yourcompany.com:ios/DTKDemoFramework.git", :tag => "#{s.version}" }

       s.source_files = 'DTKDemoFramework/**/*.{h,m}'
      
       s.requires_arc = true
       s.static_framework = true
       
       #必须添加以下钉钉依赖库
       s.dependency 'DTKExternalModule'
       s.dependency 'DTKExclusiveExtensionAPI'

     end
   ```

### **引入Framework插件**

1. 将创建的 DTKDemoFramework 工程文件，放入前提条件中下载的 DTKExternalDemoApp 文件夹下，最终的目录如图所示：

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7214602961/p705393.png)
2. 打开 DTKExternalDemoApp.xcworkspace 主工程，在 podfile 中引入该 framework。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7214602961/p705402.png)
3. 执行 pod update 指令，更新主工程。可以看到，DTKDemoFramework 被加载入主工程。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7214602961/p705424.png)

## **编写插件功能**

1. 注册模块并绑定 BundleID。

   > **[!NOTE]**
   >
   > - 这里的 BunduleID 不是指苹果定义的APP BunduleID，而是开发者的开发产物（Bundle）的唯一标识，用于钉钉侧识别SDK并鉴权。后续，我们默认提到BunduleID时均指开发产物的标识。
   > - 开发时Bundle ID可以先自定义一个值，本地测试完成后，再到平台创建专属插件时填入该值。
   > - 为了避免重复，我们建议采用类似“公司\_产品”的多段式格式填写。支持字母、数字、下划线，请勿使用其他特殊字符。
   > - 禁止包含“DingTalk”、“Alibaba”等钉钉相关特殊字符串。
   > - 如果插件是多端的（比如Android、iOS），请务必使用相同的值。
   >
   > 此处 BunduleID 必须与[创建客户端插件](../01-XYCsE5MGJh-功能介绍/0002-creating-a-client-plug-in-1.md)中设置的 BunduleID 保持一致。

   ```
   //DTKDemoFramework.h
   //继承DTKExternalModuleProtocol
   @interface DTKDemoFramework : NSObject <DTKExternalModuleProtocol>
   @end

   //DTKDemoFramework.m
   //使用DTKExternalBundleRegister注册注册
   DTKExternalBundleRegister(DTKDemoFramework)
   static NSString *const MyBundleID = @"your_bundle_id";

   @implementation DTKDemoFramework

   //绑定BundleID
   - (nonnull NSString *)bundleId {
       return MyBundleID;
   }

   @end
   ```
2. 定义并注册 JSAPI

   ```
   //注册JSAPI
   DTKExternalJSAPIRegister(your_bundle_id, DTKDemoFilePreviewJSAPI)

   //预览实现类定义
   @interface DTKDemoFilePreviewJSAPI : NSObject<DTKExternalJSAPIHandlerProtocol>
   @end
   ```
3. 实现 JSAPI

   1. 事件响应

      ```
      - (void)handleRequest:(nonnull id<DTKExternalAPIRequest>)request
                withContext:(nonnull id<DTKExternalJSAPIContext>)context
                   callback:(nonnull DTKExternalAPICallback)callback {
          if ([request.apiName isEqualToString:@"demo.localfile.preview"]) {
              self.callback = callback;
              self.webVc = context.webViewController;
              [self pickAndPreviewLocalFile];
          }
      }
      ```
   2. 选择本地文件

      ```
      //选择本地文件
      - (void)pickAndPreviewLocalFile{
          NSString *filePath = nil;
          NSArray <NSString *> *types = @[@"public.content",
                                          @"public.item"];
          UIDocumentPickerViewController *vc = [[UIDocumentPickerViewController alloc] initWithDocumentTypes:types inMode:UIDocumentPickerModeImport];
          vc.delegate = self;
          vc.modalPresentationStyle = UIModalPresentationFormSheet;
          [self.webVc presentViewController:vc animated:YES completion:NULL];
      }

      //UIDocumentPickerDelegate
      - (void)documentPicker:(UIDocumentPickerViewController *)controller didPickDocumentAtURL:(NSURL *)url {
          [self handlePick:url];
      }

      //处理URL，获取最终文件路径
      - (void)handlePick:(NSURL*)url {
          if (!self.callback) return;
          if (!url|| [url path] == 0) {
              self.callback(@{@"error":@"no file picked",
                              @"result":@"failed"
              });
              return;
          }
          //创建沙盒目录
          NSFileManager *fm = [NSFileManager defaultManager];
          NSString *baseFilePath = [NSTemporaryDirectory() stringByAppendingPathComponent:@"DTKDemoPreviewFile"];
          NSError *err = nil;
          if (![fm fileExistsAtPath:baseFilePath]) {
              BOOL suc = [fm createDirectoryAtPath:baseFilePath withIntermediateDirectories:YES attributes:nil error:&err];
              if (!suc || err) {
                  self.callback(@{
                      @"error":err ? ([NSString stringWithFormat:@"%ld", (long)err.code]):@"create filepath failed",
                      @"result":@"failed"
                  });
                  return;
              }
          }
          //删除同名文件
          NSString *path = [url path];
          NSString *targetPath = [baseFilePath stringByAppendingPathComponent:[path lastPathComponent]];
          if ([fm fileExistsAtPath:targetPath]) {
              if (![fm removeItemAtPath:targetPath error:&err] || err) {
                  self.callback(@{
                      @"error":err ? ([NSString stringWithFormat:@"%ld", (long)err.code]):@"remove failed",
                      @"result":@"failed"
                  });
                  return;
              }
          }
          //拷贝文件    
          [fm copyItemAtPath:path toPath:targetPath error:&err];
          if (err) {
              self.callback(@{
                  @"error":err ? ([NSString stringWithFormat:@"%ld", (long)err.code]):@"copy failed",
                  @"result":@"failed"
              });
              return;
          }
          
          NSURL *fileURL = [NSURL fileURLWithPath:targetPath];
          if (!fileURL || !fileURL.isFileURL) {
              self.callback(@{
                  @"error":@"invalid fileURL ",
                  @"result":@"failed"
              });
              return;
          }else{
              self.callback(@{
                  @"result":@"succeed"
              });
              [self previewLocalFile:fileURL];
          }
        
      }
      ```
   3. 文件预览

      ```
      - (void)previewLocalFile:(NSURL*)fileURL{
        //DTKLocalPreviewViewController为加载本地文件的VC，此处省略具体实现代码
         DTKLocalPreviewViewController *vc = [[DTKLocalPreviewViewController alloc]initWithFilePath:fileURL];
         [self.webVc.navigationController pushViewController:vc animated:YES];
      }
      ```

> **[!IMPORTANT]**
>
> 插件SDK中，无论成功还是失败请务必回调callback，告知小程序（H5微应用）执行结果。

## **编译生成产物**

1. 使用 XCode 编译工程，并生成 Framework 产物。
2. 将 Framework 产物打包压缩生成 \*.zip 文件（比如 DTKDemoFramework.framework.zip）

## **其他说明**

为保障插件在钉钉环境中的稳定性与兼容性，钉钉对部分常用开源库进行了定制化改造，并设定了固定版本要求。若开发者引入的SDK存在版本冲突，可能导致编译失败或运行时异常。

随着版本的升级和更新，三⽅依赖还会进⼀步增加，⽬前基本每个三⽅库都做了⾃定义修改。部分三方库Framework和头文件可以在Demo工程中下载查看，其余未提供Framework的三方库为钉钉定制版，请联系钉钉开发人员确认。

> **[!NOTE]**
>
> 为了减少正式集成时出现的各种编译问题，请仔细核对以下三方依赖库列表及其版本。

| **依赖库名称** |
| --- |
| YYKit |
| SDWebImage |
| libwebp |
| OpenSSL（包含libssl.a和libcrypto.a） |
| Masonry |
| MBProgressHUD |
| AFNetworking |
| Xlite |
| ZipArchive |
| Protobuf |
| MBProgressHUD |
| FLAnimatedImage |
| AMap |
| MNN |
| YapDatabase |
| pop |
| JotUI |
| GCanvas |
| Reachability |
| libqrencode |
| SWTableViewCell |
| tnet |
| JDYThreadTrace |
| CocoaHTTPServer |
| KTVHTTPCache |
| AlipaySDK |
| OpenCV |

## **常见问题**

如果遇到开发问题，请先查阅[开发 IOS 插件](../02-sakFIe9HDV-Android-插件/0016-development-building-faq.md#4825a346b7o6u)自行解决。
