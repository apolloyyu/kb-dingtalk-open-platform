---
title: "权限（Permission）"
source_url: "https://open.dingtalk.com/document/development/permission-service-permissionservice"
namespace: "development"
slug: "permission-service-permissionservice"
group: "专属版客户端插件"
tab: "Android 插件"
breadcrumb: "Android 插件 > 权限（Permission）"
doc_id: "5iNyBbced0"
updated_at: "2026-08-12 09:20:45"
---

> Source: https://open.dingtalk.com/document/development/permission-service-permissionservice
> Path: 专属版客户端插件 / Android 插件 / Android 插件 > 权限（Permission）
> Updated: 2026-08-12 09:20:45

# 权限（Permission）

## **功能概述**

提供动态申请系统敏感权限服务。请优先使用本服务接口，可为用户提供统一的权限交互。

## **接口详情**

| **接口** | **描述** |
| --- | --- |
| hasSelfPermissions | 判断App是否已经具有指定权限 |
| checkRequestPermissions | 请求安卓系统权限，如果app已经拥有权限，则直接回调onGrant；如果app尚未拥有权限，则向用户弹窗申请。 |
| checkRequestDingtalkPermissions | 请求钉钉数据权限。 |

> **[!NOTE]**
>
> 对于同一个Activity如果需要多次调用接口申请不同权限时，需要保证requestCode不一样，否则会导致回调之间互相影响。

## **权限声明**

使用PermissionService前，请务必在bundle.xml中声明需要使用的权限。

如下示例：

```
<dingtalk-bundle>
  <use-permissions>
    <use-permission>android.permission.BLUETOOTH</use-permission>
  </use-permissions>
</dingtalk-bundle>
```

## **代码示例**

```
int requestCode = 1001;
String permissionName = Manifest.permission.WRITE_EXTERNAL_STORAGE;
PermissionService service = MainBundle.getBundleContext().getService(PermissionService.class);
if (service != null) {
  service.checkRequestPermissions(activity, requestCode, permissionName, new PermissionService.PermissionCallback() {
    @Override
    public void grant() {		// 用户授权	}

      @Override
        public void onDenied() { // 用户拒绝	}

        @Override
          public void onNeverAsk() {	// 用户拒绝且不再询问 }

          @Override
            public void onException(String code, String message) {
            // 权限申请失败，如：获取不到Activity
          }
        });
      }
```
