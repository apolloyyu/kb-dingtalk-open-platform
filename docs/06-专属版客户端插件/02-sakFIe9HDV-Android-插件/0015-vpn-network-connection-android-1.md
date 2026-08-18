---
title: "VPN网络连接"
source_url: "https://open.dingtalk.com/document/development/vpn-network-connection-android-1"
namespace: "development"
slug: "vpn-network-connection-android-1"
group: "专属版客户端插件"
tab: "Android 插件"
breadcrumb: "解决方案 > VPN网络连接"
doc_id: "AfuDviKlNm"
updated_at: "2026-08-18 09:08:02"
---

> Source: https://open.dingtalk.com/document/development/vpn-network-connection-android-1
> Path: 专属版客户端插件 / Android 插件 / 解决方案 > VPN网络连接
> Updated: 2026-08-18 09:08:02

# VPN网络连接

本文仅为建议方案，不一定适合所有业务场景，仅供参考。

> **[!NOTE]**
>
> 建议优先采用系统提供的VPNService，即全局VPN方案，不建议hook底层ip代理的方式，即APP范围的网络方案，可能会影响钉钉原有业务。

## **场景描述**

- 外访内：即钉钉处于外网环境，需要访问企业内网地址，也是最常见的场景。
- 内访外：即钉钉处于内网环境，需要访问外网登录并使用钉钉功能。通常是企业提供工作机器，并在企业内部的工作环境中使用。

## **关键扩展点**

请参考使用以下扩展点。

| **扩展点** | **描述** |
| --- | --- |
| [登录流程扩展](0011-login-process-extension-android-1.md) | 主要用于内访外的场景，需要在登录前连接VPN |
| [首页生命周期扩展](0012-home-lifecycle-extension-android-1.md) | 主要用于外访内的场景，唤起钉钉后自动连接VPN |
| [设置项扩展点](0010-set-item-extension-point-android-1.md) | 可用于添加VPN相关的用户设置 |

## **关键开放API**

请参考使用以下开放API。

| **开放API** | **描述** |
| --- | --- |
| [获取员工信息](../01-XYCsE5MGJh-功能介绍/0007-get-employee-information.md) | 主要用于校验用户身份的场景 |

## **解决方案：**访问内网

### **基本思路**

假如存在一系列的H5/小程序内网应用，用户在使用专属钉钉时期望能够访问这些内网应用。

- 方式1：

  额外开发一个H5/小程序应用，用户可以在该应用中开启/断开VPN连接，可以参考[开发自定义JSAPI](0004-define-extension-jsapi.md)自定义JSAPI实现。
- 方式2：

  在设置项中新增VPN设置页，用户可以在页面中开启/断开VPN连接。方案较简单，可以参考[设置项扩展点](0010-set-item-extension-point-android-1.md)自定义Activity实现。
- 方式3（推荐）：

  专属版钉钉App启动时自动连接VPN网络，下文中重点描述该方式。

### **实现步骤**

APP启动进入前台后（或者登录后）自动连接VPN，APP进入后台后自动断开VPN。

#### **步骤一：**使用首页生命周期扩展点启动VPNService

HomeLifecyclePlugin接口会在杀进程重启APP以及账密重登后均会触发指定回调onCreate，因此在此时机触发链接VPN。

```
@Extension(id="vpn_extension", target="home_lifecycle")
public class VPNHomeLifecycleExtension extends HomeLifecyclePlugin {

    @Override
    public void onCreate(IExtensionWrapperActivity activity) {
        // 启动VPNService
    }

    @Override
    public void onActivityResult(int requestCode, int resultCode, Intent data) {
    	// DO Something
    }
}
```

#### **步骤二：监听前后台、登录登出事件，断开VPN**

为了不影响手机其他功能，可以在进入后台时，或者用户账号登出时断开VPN。

```
@Event(event = "dingtalk.enter.foreground,dingtalk.enter.background")
public class VpnEventReceiver implements EventReceiver {

    @Override
    public void onEvent(String e, Bundle bundle) {
        switch (e) {
            case "dingtalk.enter.background":
                // 断开VPN，为了避免用户临时进入后台，可以考虑做延迟策略
                break;
        }
    }
}
```

#### **步骤三：账号管控**

在VPN连接时，还可以进一步使用开放API（[获取员工信息](../01-XYCsE5MGJh-功能介绍/0007-get-employee-information.md)）做账号的入网管控，即获取用户员工ID（可映射成工号），根据员工身份获取相应的入网策略。

## **解决方案：内网访问外网**

当用户设备网络处于内网无法访问外部互联网时，为了能够正常使用钉钉，需要在钉钉登录前建立VPN通道。

### **基本思路**

- 使用[登录流程扩展](0011-login-process-extension-android-1.md)，在账号登录前连接VPN通道
- 在BundleApplication.onCreate回调中，判断应用是否已有登录态，解决APP杀进程重启时的VPN通道建立；
- 监听logout等事件，在账号退出等时机完成VPN通道断开；

### **实现步骤**

#### **步骤一：**使用登录扩展点EpLoginNode

```
@Extension(id="vpn_login_node", target="login_nodes")
public class PrepareNode extends EpLoginNode {

    @Override
    public NodeType getNodeType() {
        return NodeType.Prepare;
    }

    @Override
    public void execute(ApiCallback<Void> callback) {
        // 建立VPN通道
    }
}
```

#### **步骤二：**App启动时补偿VPN连接

假如账号已经登录，在下次冷启动时需要补偿VPN通道的连接。

```
@Bundle
public MainBundle extension BundleApplication {

		public void onCreate(BundleContext context) {
        ApiRequest request = new ApiRequest();
        request.api = "dd.user.isLogin";

        ApiResponse response = bundleContext.invokeSyncApi(request);
        if (response.getBoolean()) {
            // 账号已经登录过，冷启动时补偿建立VPN通道
        } else {
          	// 没有登录态，不需要补偿
        }
    }
}
```

#### **步骤三：监听前后台、登录登出事件，断开VPN**

在用户账号登出，或者进入后台时可断开VPN。

```
@Event(event = "dingtalk.logout,dingtalk.enter.background")
public class VpnEventReceiver implements EventReceiver {

    @Override
    public void onEvent(String e, Bundle bundle) {
        switch (e) {
            case "dingtalk.logout":
                // 断开VPN
                break;
        }
    }
}
```

#### **步骤四：账号管控**

在VPN连接时，还可以进一步使用开放API（[获取员工信息](../01-XYCsE5MGJh-功能介绍/0007-get-employee-information.md)）做账号的入网管控，即获取用户员工ID（可映射成工号），根据员工身份获取相应的入网策略。

#### **步骤五：使用设置扩展点，完善体验**

可使用[设置项扩展点](0010-set-item-extension-point-android-1.md)，添加网络设置页面，完善在网络异常时自检测等功能。
