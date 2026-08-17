---
title: "二维码接入"
source_url: "https://open.dingtalk.com/document/development/xvdsha"
namespace: "development"
slug: "xvdsha"
group: "硬件开发"
tab: "Android设备接入"
breadcrumb: "二维码接入"
doc_id: "EGWnc2jg9J"
updated_at: "2026-08-04 09:07:17"
---

> Source: https://open.dingtalk.com/document/development/xvdsha
> Path: 硬件开发 / Android设备接入 / 二维码接入
> Updated: 2026-08-04 09:07:17

# 二维码接入

本文档介绍了摄像头反向二维码功能的SDK接入方式，包括启动与停止绑定流程。

## 引入SDK依赖类

请确保项目中已引入以下类：

```
import com.alibaba.dingtalk.inside.bind.DingTalkInsideSdk;
```

## **动态二维码接入**

### **流程说明**

1. 调用 `dynamicBindStart()` 启动动态二维码绑定流程。
2. 实现 `DynamicBindListener` 回调以接收二维码更新事件。
3. 绑定完成后调用 `dynamicBindStop()` 停止服务，释放资源。

### **启动动态二维码绑定**

**场景**：启动动态二维码绑定，用于发起一次新的设备或身份绑定请求。

**函数**：

```
public static void dynamicBindStart(DynamicBindListener listener);
```

**参数**：

```
//此回调用于二维码更新的回调
public interface DynamicBindListener {
    void onQrcodeUpdate(String qrcode);
}
```

### **停止动态二维码绑定**

**场景**：停止当前正在进行的动态二维码绑定任务，关闭监听器并释放资源。

**函数**：

```
public static void dynamicBindStop();
```

### **代码示例**

```
// 初始化并启动动态二维码绑定
public void startBinding() {
    // 注册回调监听器
    DynamicBindListener listener = new DynamicBindListener() {
        @Override
        public void onQrcodeUpdate(String qrcode) {
            // 将二维码内容传递给前端展示
            System.out.println("最新二维码: " + qrcode);
            renderQrCodeToPage(qrcode); // 自定义渲染逻辑
        }
    };

    // 启动绑定流程
    DingTalkInsideSdk.dynamicBindStart(listener);
}

// 停止绑定流程（例如绑定成功或取消操作）
public void stopBinding() {
    DingTalkInsideSdk.dynamicBindStop();
    System.out.println("动态二维码绑定已停止");
}
```

**验证方式：**

- 查看控制台日志是否输出最新二维码信息。
- 确认前端能否正常渲染并显示二维码。

## 静态二维码接入

### **流程说明**

1. 调用 `staticBindStart()` 开启绑定模式；
2. 根据业务需要调用 `staticBindStop()` 结束绑定；
3. 通过日志或调试工具验证流程是否正常执行。

### **启动静态二维码绑定**

**场景**：启动静态二维码绑定。

**函数**：

```
public static void staticBindStart();
```

### **停止静态二维码绑定**

**场景**：停止静态二维码绑定。

**函数**：

```
public static void staticBindStop();
```

### **代码示例**

```
// 初始化并启动静态二维码绑定
public void startBinding() {
  // 设备启动后初始化并开启绑定
  if (DingTalkInsideSdk.isInitialized()) {
    DingTalkInsideSdk.staticBindStart();
  } else {
    Log.e("SDK", "未初始化，请先调用init()");
  }
}

// 停止绑定流程（例如绑定成功或取消操作）
public void stopBinding() {
  // 用户扫码完成后或设备关机前调用
  DingTalkInsideSdk.staticBindStop();
  System.out.println("静态二维码绑定已停止");
}

// 或结合生命周期管理
@Override
protected void onDestroy() {
    DingTalkInsideSdk.staticBindStop();
    super.onDestroy();
}
```

- 查看控制台日志是否输出最新二维码信息。
- 确认前端能否正常渲染并显示二维码。

## **摄像头反向二维码接入**

### **启动二维码绑定**

**场景**：使用摄像头反向二维码绑定. 当设备扫描到二维码后调用此api启动摄像头反向二维码绑定。

**函数**：

```
public static void cameraBindStart(String qrcode);
```

### **停止二维码绑定**

**场景**：停止摄像头反向二维码绑定。

**函数**：

```
public static void cameraBindStop();
```

### **示例代码**

```
// 初始化并启动摄像头反向二维码绑定
public void startBinding() {
  String scannedQrCode = qrScanner.scan(); // 获取扫描结果
  if (scannedQrCode != null && !scannedQrCode.isEmpty()) {
    DingTalkInsideSdk.cameraBindStart(scannedQrCode); // 启动绑定
    System.out.println("摄像头反向二维码绑定成功");
  }
}

// 停止绑定流程（例如绑定成功或取消操作）
public void stopBinding() {
  DingTalkInsideSdk.cameraBindStop();
  System.out.println("摄像头反向二维码绑定已停止");
}
```
