---
title: "常用服务（Service）"
source_url: "https://open.dingtalk.com/document/development/print-log-1"
namespace: "development"
slug: "print-log-1"
group: "专属版客户端插件"
tab: "iOS 插件"
breadcrumb: "iOS 插件 > 常用服务（Service）"
doc_id: "j5KX5bJ49p"
updated_at: "2026-05-22 18:16:15"
---

> Source: https://open.dingtalk.com/document/development/print-log-1
> Path: 专属版客户端插件 / iOS 插件 / iOS 插件 > 常用服务（Service）
> Updated: 2026-05-22 18:16:15

# 常用服务（Service）

## **打印日志**

### **功能描述**

钉钉提供了日志服务，日志以文件的形式存储在本地，可用于用户线上问题排查的场景。我们强烈建议在前期开发过程中将关键路径均埋入日志，避免出现问题是无法追踪排查。

### **接口详情**

接口文件：DTKExternalLogServiceProtocol.h

| **接口** | **描述** |
| --- | --- |
| DTKExternalLogInfo | 输出info级别的日志，常用于记录关键路径 |
| DTKExternalLogError | 输出错误级别的日志 |

> **[!WARNING]**
>
> 请不要将敏感信息打印到日志中。
>
> 请避免在循环语句中打印，单条日志避免过长（最大500字符）。

### **代码示例**

```
 id<DTKExternalLogServiceProtocol> logger = DTKExternalGetLogger(@"your_bundle_id");
 DTKExternalLog(logger, @"log some infos");
 DTKExternalLogError(logger, @"log some error: xx");
```

### **如何查看日志**

可点击：设置与隐私 - 连续多次点击图标 - 手动上传日志到服务区，即可将打印的日志发给对应的技术人员。

## **UI 服务**

### **视图层级**

#### **功能描述**

假如你的插件需要获取当前视图层级，建议优先使用该服务。

#### **接口详情**

接口文件：DTKExternalUIHierarchyServiceProtocol.h

| **接口** | **描述** |
| --- | --- |
| currentTopViewController | 当前顶部的vc |
| currentNavigationController | 当前vc对应的导航控制器 |
| rootViewController | 当前window的根vc |
| pushWebView: | 打开指定URL的网页页面 |
| pushWebView:toNavigation:animated: | 在指定导航控制器打开指定URL的网页页面 |
| generateWebViewControllerWithUrl: | 以指定URL生成一个VC |
| wkWebviewWithFrame:configuration: | 以指定参数创建webView实例 |

#### **代码示例**

```
id<DTKExternalUIHierarchyServiceProtocol> UIHierarchy = DTKExternalGetImpl(@"your_bundle_id", DTKExternalUIHierarchyServiceProtocol);
UIView *view = [UIHierarchy currentTopViewController].view
```

### **Toast服务**

#### **功能描述**

假如你的插件需要弹出Toast时，建议优先使用该服务，可用于弹出钉钉标准样式的Toast。

#### **接口详情**

接口文件：DTKExternalToastSerivceProtocol.h

| **接口** | **描述** |
| --- | --- |
| showMessage:inView: | 在指定视图中，弹出普通样式的Toast |
| showSuccessMessage:inView: | 在指定视图中，弹出附带成功样式的Toast |
| showErrorMessage:inView: | 在指定视图中，弹出附带失败样式的Toast |
| showWarningMessage:inView: | 在指定视图中，弹出附带警告样式的Toast |
| showLoadingInView: | 在指定视图中，展示loading图 |
| showLoadingMessage:inView: | 在指定视图中，展示带信息的loading图 |
| hideInView: | 移除指定视图中的toast |

#### **代码示例**

```
id<DTKExternalUIHierarchyServiceProtocol> uiHierarchy = DTKExternalGetImpl(GlobalAppId, DTKExternalUIHierarchyServiceProtocol);
id<DTKExternalToastSerivceProtocol> toastHandler = DTKExternalGetImpl(BundleId, DTKExternalToastSerivceProtocol);
toastHandler showMessage:@"demo" inView:[uiHierarchy currentTopViewController].view];
```

### **Alert服务**

#### **功能描述**

假如你的插件需要弹出Alert时，建议优先使用该服务，与系统Alert接口类似。

#### **接口详情**

接口文件：DTKExternalAlertServiceProtocol.h

| **接口** | **描述** |
| --- | --- |
| alertWithTitle:message: | 创建一个alert实例 |
| showAlert:inViewController: | 在指定VC中弹出Alert |
| dismissAlert: | 移除Alert |

#### **代码示例**

```
id<DTKExternalAlertServiceProtocol> alertHandler = DTKExternalGetImpl(GlobalAppId, DTKExternalAlertServiceProtocol);
[alertHandler alertWithTitle:@"demo" message:@"demo message"];
```

## **APP 基础信息**

### **功能描述**

获取钉钉APP的一些基础信息。

### **接口详情**

接口文件：DTKExternalHostAppServiceProtocol.h

| **接口** | **描述** |
| --- | --- |
| getHostAppDisplayName | 获取App的显示名称 |
| getHostAppVersion | 获取App当前的版本号 |
| getHostAppScheme | 获取App的Scheme |

### **代码示例**

```
id<DTKExternalHostAppServiceProtocol> service = DTKExternalGetImpl(@"your_bundle_id", DTKExternalHostAppServiceProtocol);
NSString* displayName = [service getHostAppDisplayName];
```
