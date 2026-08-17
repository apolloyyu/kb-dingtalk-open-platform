---
title: "JSAPI总览"
source_url: "https://open.dingtalk.com/document/development/mini-program-jsapi-overview"
namespace: "development"
slug: "mini-program-jsapi-overview"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > JSAPI总览"
doc_id: "6ZDGHB3l20"
updated_at: "2025-09-17 20:58:37"
---

> Source: https://open.dingtalk.com/document/development/mini-program-jsapi-overview
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > JSAPI总览
> Updated: 2025-09-17 20:58:37

# JSAPI总览

**扫码体验**

![小程序JSAPI预览地址](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7866091161/p236554.png)

## 基础

| **API说明** | **API名称** | **企业内部应用** | **第三方企业应用** | **第三方个人应用** |
| --- | --- | --- | --- | --- |
| [判断小程序的API、回调、参数、组件等是否在当前版本可用](https://open.dingtalk.com/document/orgapp/dd-caniuse) | dd.canIUse | 支持 | 支持 | 支持 |
| [获取当前用户的企业corpId](https://open.dingtalk.com/document/orgapp/dd-corpid) | dd.corpId | 支持 | 支持 | 不支持 |
| [获取基础库版本号](https://open.dingtalk.com/document/orgapp/gets-the-version-number-of-the-base-database) | 获取基础库版本 | 支持 | 支持 | 支持 |
| [同步获取小程序AppId](https://open.dingtalk.com/document/orgapp/synchronously-obtain-the-appid-of-the-mini-program) | dd.getAppIdSync | 支持 | 支持 | 支持 |
| [获取小程序启动时的参数](https://open.dingtalk.com/document/orgapp/obtains-the-startup-parameters-of-mini-programs) | dd.getLaunchOptionsSync | 支持 | 支持 | 支持 |
| [获取小程序的运行版本](https://open.dingtalk.com/document/orgapp/obtain-the-running-version-of-the-mini-program) | dd.getRunScene | 支持 | 支持 | 支持 |

## 免登

| **API说明** | **API名称** | **企业内部应用** | **第三方企业应用** | **第三方个人应用** |
| --- | --- | --- | --- | --- |
| [免登授权码](https://open.dingtalk.com/document/orgapp/mini-program-free-login) | dd.getAuthCode | 支持 | 支持 | 支持 |

## 更新管理小程序

| **API名称** | **API说明** | **企业内部应用** | **第三方企业应用** | **第三方个人应用** |
| --- | --- | --- | --- | --- |
| [获取全局唯一的版本更新管理器，用于管理小程序更新](https://open.dingtalk.com/document/orgapp/updatemanager) | 使用UpdateManager更新小程序 | 支持 | 支持 | 支持 |
| [强制小程序重启并使用新版本使用](https://open.dingtalk.com/document/orgapp/updatemanager) | UpdateManager.applyUpdate() | 支持 | 支持 | 支持 |
| [监听向钉钉后台请求检查更新结果事件](https://open.dingtalk.com/document/orgapp/updatemanager) | UpdateManager.onCheckForUpdate(function callback) | 支持 | 支持 | 支持 |
| [监听小程序有版本更新事件](https://open.dingtalk.com/document/orgapp/updatemanager) | UpdateManager.onUpdateReady(function callback) | 支持 | 支持 | 支持 |
| [监听小程序更新失败事件](https://open.dingtalk.com/document/orgapp/updatemanager) | UpdateManager.onUpdateFaile(function callback) | 支持 | 支持 | 支持 |

## 网络

| **类目** | **API说明** | **API名称** | **企业内部应用** | **第三方企业应用** | **第三方个人应用** |
| --- | --- | --- | --- | --- | --- |
| **发网络请求** | [发网络请求](https://open.dingtalk.com/document/orgapp/send-network-requests) | dd.httpRequest | 支持 | 支持 | 支持 |
| **上传下载** | [上传文件](https://open.dingtalk.com/document/orgapp/dd-upload-objects) | dd.uploadFile | 支持 | 支持 | 支持 |
| [下载文件](https://open.dingtalk.com/document/orgapp/mini-program-download-objects) | dd.downloadFile | 支持 | 支持 | 支持 |
| **WebSocket** | [创建WebSocket连接](https://open.dingtalk.com/document/orgapp/dd-connectsocket) | dd.connectSocket | 支持 | 支持 | 支持 |
| [监听WebSocket连接打开事件](https://open.dingtalk.com/document/orgapp/dd-onsocketopen) | dd.onSocketOpen | 支持 | 支持 | 支持 |
| [取消监听WebSocket连接打开事件](https://open.dingtalk.com/document/orgapp/dd-offsocketopen) | dd.offSocketOpen | 支持 | 支持 | 支持 |
| [监听WebSocket错误](https://open.dingtalk.com/document/orgapp/dd-onsocketerror) | dd.onSocketError | 支持 | 支持 | 支持 |
| [取消监听WebSocket错误](https://open.dingtalk.com/document/orgapp/dd-offsocketerror) | dd.offSocketError | 支持 | 支持 | 支持 |
| [发送数据](https://open.dingtalk.com/document/orgapp/dd-sendsocketmessage) | dd.sendSocketMessage | 支持 | 支持 | 支持 |
| [监听接收到的消息事件](https://open.dingtalk.com/document/orgapp/dd-onsocketmessage) | dd.onSocketMessage监听 | 支持 | 支持 | 支持 |
| [取消监听接收消息事件](https://open.dingtalk.com/document/orgapp/dd-offsocketmessage) | dd.offSocketMessage | 支持 | 支持 | 支持 |
| [关闭WebSocket连接](https://open.dingtalk.com/document/orgapp/dd-closesocket) | dd.closeSocket | 支持 | 支持 | 支持 |
| [监听WebSocket关闭](https://open.dingtalk.com/document/orgapp/dd-onsocketclose) | dd.onSocketClose | 支持 | 支持 | 支持 |
| [取消监听WebSocket关闭事件](https://open.dingtalk.com/document/orgapp/dd-offsocketclose) | dd.offSocketClose | 支持 | 支持 | 支持 |

## 多媒体

| **类目** | **API说明** | **API名称** | **企业内部应用** | **第三方企业应用** | **第三方个人应用** |
| --- | --- | --- | --- | --- | --- |
| **图片** | [选择图片](https://open.dingtalk.com/document/orgapp/dd-chooseimage) | dd.chooseImage | 支持 | 支持 | 支持 |
| [预览图片](https://open.dingtalk.com/document/orgapp/dd-previewimage) | dd.previewImage | 支持 | 支持 | 支持 |
| [保存图片到手机相册](https://open.dingtalk.com/document/orgapp/dd-saveimage) | dd.saveImage | 支持 | 支持 | 支持 |
| [压缩图片](https://open.dingtalk.com/document/orgapp/dd-compressimage) | dd.compressImage | 支持 | 支持 | 支持 |
| [获取图片信息](https://open.dingtalk.com/document/orgapp/dd-getimageinfo) | dd.getImageInfo | 支持 | 支持 | 支持 |
| [编辑图片](https://open.dingtalk.com/document/orgapp/dd-editpicture) | dd.editPicture | 支持 | 支持 | 支持 |
| **录音管理** | [获取录音管理器](https://open.dingtalk.com/document/orgapp/dd-getrecordermanager) | dd.getRecorderManager | 支持 | 支持 | 支持 |
| **背景音频管理** | [获取背景音频管理](https://open.dingtalk.com/document/orgapp/dd-getbackgroundaudiomanager) | dd.getBackgroundAudioManager | 支持 | 支持 | 支持 |
| **视频** | [选择视频](https://open.dingtalk.com/document/orgapp/dd-choosevideo) | dd.chooseVideo | 支持 | 支持 | 支持 |
| [创建video对象](https://open.dingtalk.com/document/orgapp/dd-createvideocontext-videoid) | dd.createVideoContext(videoId) | 支持 | 支持 | 支持 |

## 界面

| **类目** | **API说明** | **API名称** | **企业内部应用** | **第三方企业应用** | **第三方个人应用** |
| --- | --- | --- | --- | --- | --- |
| **导航栏** | [页面跳转（保留当前页）](https://open.dingtalk.com/document/orgapp/dd-navigateto) | dd.navigateTo | 支持 | 支持 | 支持 |
| [页面跳转（关闭当前页）](https://open.dingtalk.com/document/orgapp/dd-redirectto) | dd.redirectTo | 支持 | 支持 | 支持 |
| [页面跳转（关闭所有页面）](https://open.dingtalk.com/document/orgapp/dd-relaunch) | dd.reLaunch | 支持 | 支持 | 支持 |
| [返回上一级或多级页面](https://open.dingtalk.com/document/orgapp/dd-navigateback) | dd.navigateBack | 支持 | 支持 | 支持 |
| [设置导航栏](https://open.dingtalk.com/document/orgapp/dd-setnavigationbar) | dd.setNavigationBar | 支持 | 支持 | 支持 |
| **TabBar** | [跳转到指定tabBar页面](https://open.dingtalk.com/document/orgapp/dd-switchtab) | dd.switchTab | 支持 | 支持 | 支持 |
| [添加tabBar文本](https://open.dingtalk.com/document/orgapp/dd-settabbarbadge) | dd.setTabBarBadge | 支持 | 支持 | 支持 |
| [移除tabBar文本](https://open.dingtalk.com/document/orgapp/dd-removetabbarbadge) | dd.removeTabBarBadge | 支持 | 支持 | 支持 |
| [显示tabBar红点](https://open.dingtalk.com/document/orgapp/dd-showtabbarreddot) | dd.showTabBarRedDot | 支持 | 支持 | 支持 |
| [隐藏tabBar红点](https://open.dingtalk.com/document/orgapp/dd-hidetabbarreddot) | dd.hideTabBarRedDot | 支持 | 支持 | 支持 |
| [添加tabBar页面](https://open.dingtalk.com/document/orgapp/dd-addtabbaritem) | dd.addTabBarItem | 支持 | 支持 | 支持 |
| [移除tabBar页面](https://open.dingtalk.com/document/orgapp/dd-removetabbaritem) | dd.removeTabBarItem | 支持 | 支持 | 支持 |
| **显示模式** | [显示模式](https://open.dingtalk.com/document/orgapp/display-mode) | dd.getColorSchemeSync | 支持 | 支持 | 支持 |
| **交互反馈** | [显示警告框](https://open.dingtalk.com/document/orgapp/dd-alert) | dd.alert | 支持 | 支持 | 支持 |
| [显示确认框](https://open.dingtalk.com/document/orgapp/dd-confirm) | dd.confirm | 支持 | 支持 | 支持 |
| [显示弱提示](https://open.dingtalk.com/document/orgapp/dd-showtoast) | dd.showToast | 支持 | 支持 | 支持 |
| [隐藏弱提示](https://open.dingtalk.com/document/orgapp/dd-hidetoast) | dd.hideToast | 支持 | 支持 | 支持 |
| [显示加载提示](https://open.dingtalk.com/document/orgapp/dd-showloading) | dd.showLoading | 支持 | 支持 | 支持 |
| [隐藏加载提示](https://open.dingtalk.com/document/orgapp/dd-hideloading) | dd.hideLoading | 支持 | 支持 | 支持 |
| [显示操作菜单](https://open.dingtalk.com/document/orgapp/dd-showactionsheet) | dd.showActionSheet | 支持 | 支持 | 支持 |
| **离开页面二次确认** | [离开二次确认配置](https://open.dingtalk.com/document/orgapp/dd-enableleaveconfirm) | dd.enableLeaveConfirm | 支持 | 支持 | 支持 |
| [取消当前页面的离开二次确认](https://open.dingtalk.com/document/orgapp/dd-disableleaveconfirm) | dd.disableLeaveConfirm | 支持 | 支持 | 支持 |
| **下拉刷新** | [停止下拉刷新](https://open.dingtalk.com/document/orgapp/dd-stoppulldownrefresh) | dd.stopPullDownRefresh | 支持 | 支持 | 支持 |
| [下拉刷新](https://open.dingtalk.com/document/orgapp/onpulldownrefresh) | onPullDownRefresh | 支持 | 支持 | 支持 |
| **选择日期** | [打开日期选择列表](https://open.dingtalk.com/document/orgapp/dd-datepicker) | dd.datePicker | 支持 | 支持 | 支持 |
| **动画** | [创建动画实例](https://open.dingtalk.com/document/orgapp/dd-createanimation) | dd.createAnimation | 支持 | 支持 | 支持 |
| **画布** | [创建canvas](https://open.dingtalk.com/document/orgapp/create-a-canvas) | dd.createCanvasContext | 支持 | 支持 | 支持 |
| **键盘** | [监听键盘弹起事件](https://open.dingtalk.com/document/orgapp/dd-onkeyboardshow) | dd.onKeyboardShow | 支持 | 支持 | 支持 |
| [监听键盘收起事件](https://open.dingtalk.com/document/orgapp/dd-onkeyboardhide) | dd.onKeyboardHide | 支持 | 支持 | 支持 |
| [隐藏键盘](https://open.dingtalk.com/document/orgapp/dd-hidekeyboard) | dd.hideKeyboard | 支持 | 支持 | 支持 |
| **滚动** | [滚动到页面的目标位置](https://open.dingtalk.com/document/orgapp/dd-pagescrollto) | dd.pageScrollTo | 支持 | 支持 | 支持 |
| **字体** | [动态加载网络字体](https://open.dingtalk.com/document/orgapp/dynamically-load-network-fonts) | dd.loadFontFace | 支持 | 支持 | 支持 |

## **小程序跳转**

| **API说明** | **API名称** | **企业内部应用** | **第三方企业应用** | **第三方个人应用** |
| --- | --- | --- | --- | --- |
| [跳转到另一个钉钉小程序](https://open.dingtalk.com/document/orgapp/inter-mini-program-jump) | dd.navigateToMiniProgram | 支持 | 支持 | 支持 |
| [返回上一个钉钉小程序](https://open.dingtalk.com/document/orgapp/return-to-the-previous-dingtalk-mini-program) | dd.navigateBackMiniProgram | 支持 | 支持 | 支持 |

## 节点查询

| **API说明** | **API名称** | **企业内部应用** | **第三方企业应用** | **第三方个人应用** |
| --- | --- | --- | --- | --- |
| [创建IntersectionObserver对象实例](https://open.dingtalk.com/document/orgapp/dd-createintersectionobserver) | dd.createIntersectionObserver | 支持 | 支持 | 支持 |
| [创建SelectorQuery节点查询对象](https://open.dingtalk.com/document/orgapp/dd-createselectorquery) | dd.createSelectorQuery | 支持 | 支持 | 支持 |

## 位置

| **API说明** | **API名称** | **企业内部应用** | **第三方企业应用** | **第三方个人应用** |
| --- | --- | --- | --- | --- |
| [获取用户当前的地理位置信息](https://open.dingtalk.com/document/orgapp/dd-getlocation) | dd.getLocation | 支持 | 支持 | 支持 |
| [使用内置地图查看位置](https://open.dingtalk.com/document/orgapp/dd-openlocation) | dd.openLocation | 支持 | 支持 | 支持 |

## 缓存

| **API说明** | **API名称** | **企业内部应用** | **第三方企业应用** | **第三方个人应用** |
| --- | --- | --- | --- | --- |
| [将数据存储在本地缓存](https://open.dingtalk.com/document/orgapp/dd-setstorage) | dd.setStorage | 支持 | 支持 | 支持 |
| [同步将数据存储](https://open.dingtalk.com/document/orgapp/dd-setstoragesync) | dd.setStorageSync | 支持 | 支持 | 支持 |
| [异步获取指定key的缓存数据](https://open.dingtalk.com/document/orgapp/dd-getstorage) | dd.getStorage | 支持 | 支持 | 支持 |
| [同步获取指定key的缓存数据](https://open.dingtalk.com/document/orgapp/dd-getstoragesync) | dd.getStorageSync | 支持 | 支持 | 支持 |
| [删除缓存数据](https://open.dingtalk.com/document/orgapp/dd-removestorage) | dd.removeStorage | 支持 | 支持 | 支持 |
| [同步删除指定key的缓存数据](https://open.dingtalk.com/document/orgapp/dd-removestoragesync) | dd.removeStorageSync | 支持 | 支持 | 支持 |
| [同步获取当前storage的相关信息](https://open.dingtalk.com/document/orgapp/obtains-information-about-the-current-cache) | dd.getStorageInfoSync | 支持 | 支持 | 支持 |
| [异步获取当前storage的相关信息](https://open.dingtalk.com/document/orgapp/get-current-cached-data-asynchronously) | dd.getStorageInfo | 支持 | 支持 | 支持 |
| [同步清除本地缓存数据](https://open.dingtalk.com/document/orgapp/synchronous-deletion-of-locally-cached-data) | dd.clearStorageSync | 支持 | 支持 | 支持 |
| [异步清除本地缓存数据](https://open.dingtalk.com/document/orgapp/delete-locally-cached-data-asynchronously) | dd.clearStorage | 支持 | 支持 | 支持 |

## 设备

| **类目** | **API说明** | **API名称** | 企业内部应用 | **第三方企业应用** | **第三方个人应用** |
| --- | --- | --- | --- | --- | --- |
| **系统信息** | [获取手机系统信息](https://open.dingtalk.com/document/orgapp/dd-getsysteminfo) | dd.getSystemInfo | 支持 | 支持 | 支持 |
| [获取手机系统信息的同步接口](https://open.dingtalk.com/document/orgapp/dd-getsysteminfosync) | dd.getSystemInfoSyn | 支持 | 支持 | 支持 |
| **网络状态** | [获取当前网络状态](https://open.dingtalk.com/document/orgapp/dd-getnetworktype) | dd.getNetworkType | 支持 | 支持 | 支持 |
| **剪切板** | [获取系统剪贴板的内容](https://open.dingtalk.com/document/orgapp/dd-getclipboard) | dd.getClipboard | 支持 | 支持 | 支持 |
| [设置剪切板数据](https://open.dingtalk.com/document/orgapp/dd-setclipboard) | dd.setClipboard | 支持 | 支持 | 支持 |
| **振动** | [使用振动功能](https://open.dingtalk.com/document/orgapp/dd-vibrate) | dd.vibrate | 支持 | 支持 | 支持 |
| [使用短振动](https://open.dingtalk.com/document/orgapp/dd-vibrateshort) | dd.vibrateShort | 支持 | 支持 | 支持 |
| [使用长振动](https://open.dingtalk.com/document/orgapp/dd-vibratelong) | dd.vibrateLong | 支持 | 支持 | 支持 |
| **蓝牙** | 低耗电蓝牙：[查找设备并连接](https://open.dingtalk.com/document/orgapp/dd-connectbledevice) | dd.connectBLEDevice | 支持 | 支持 | 支持 |
| 低耗电蓝牙：[断开蓝牙链接](https://open.dingtalk.com/document/orgapp/dd-disconnectbledevice) | dd.disconnectBLEDevice | 支持 | 支持 | 支持 |
| 低耗电蓝牙：[获取蓝牙设备所有特征值](https://open.dingtalk.com/document/orgapp/dd-getbledevicecharacteristics) | dd.getBLEDeviceCharacteristics | 支持 | 支持 | 支持 |
| 低耗电蓝牙：[获取蓝牙设备所有服务](https://open.dingtalk.com/document/orgapp/dd-getbledeviceservices) | dd.getBLEDeviceServices | 支持 | 支持 | 支持 |
| 低耗电蓝牙：[设置读特征通知模式](https://open.dingtalk.com/document/orgapp/dd-notifyblecharacteristicvaluechange) | dd.notifyBLECharacteristicValueChange | 支持 | 支持 | 支持 |
| 低耗电蓝牙：[监听特征值变化事件](https://open.dingtalk.com/document/orgapp/dd-onblecharacteristicvaluechange) | dd.onBLECharacteristicValueChange | 支持 | 支持 | 支持 |
| 低耗电蓝牙：[移除监听特征值变化事件](https://open.dingtalk.com/document/orgapp/dd-offblecharacteristicvaluechange) | dd.offBLECharacteristicValueChange | 支持 | 支持 | 支持 |
| 低耗电蓝牙：[移除监听连接状态变化事件](https://open.dingtalk.com/document/orgapp/dd-offbleconnectionstatechanged) | dd.offBLEConnectionStateChanged | 支持 | 支持 | 支持 |
| 低耗电蓝牙：[监听蓝牙连接状态事件](https://open.dingtalk.com/document/orgapp/dd-onbleconnectionstatechanged) | dd.onBLEConnectionStateChanged(callback) | 支持 | 支持 | 支持 |
| 低耗电蓝牙：[读取蓝牙设备特征值数据](https://open.dingtalk.com/document/orgapp/dd-readblecharacteristicvalue) | dd.readBLECharacteristicValue | 支持 | 支持 | 支持 |
| 低耗电蓝牙：[向蓝牙设备特征值中写入数据](https://open.dingtalk.com/document/orgapp/dd-writeblecharacteristicvalue) | dd.writeBLECharacteristicValue | 支持 | 支持 | 支持 |
| 传统蓝牙：[初始化蓝牙接口](https://open.dingtalk.com/document/orgapp/dd-openbluetoothadapter) | dd.openBluetoothAdapter | 支持 | 支持 | 支持 |
| 传统蓝牙：[关闭蓝牙适配器](https://open.dingtalk.com/document/orgapp/dd-closebluetoothadapter) | dd.closeBluetoothAdapter | 支持 | 支持 | 支持 |
| 传统蓝牙：[获取本机蓝牙模块状态](https://open.dingtalk.com/document/orgapp/dd-getbluetoothadapterstate) | dd.getBluetoothAdapterState | 支持 | 支持 | 支持 |
| 传统蓝牙：[搜寻附近蓝牙设备](https://open.dingtalk.com/document/orgapp/dd-startbluetoothdevicesdiscovery) | dd.startBluetoothDevicesDiscovery | 支持 | 支持 | 支持 |
| 传统蓝牙：[停止搜寻附近的蓝牙设备](https://open.dingtalk.com/document/orgapp/dd-stopbluetoothdevicesdiscovery) | dd.stopBluetoothDevicesDiscovery | 支持 | 支持 | 支持 |
| 传统蓝牙：[获取所有已发现的蓝牙设备](https://open.dingtalk.com/document/orgapp/dd-getbluetoothdevices) | dd.getBluetoothDevices | 支持 | 支持 | 支持 |
| 传统蓝牙：[获取已连接设备](https://open.dingtalk.com/document/orgapp/dd-getconnectedbluetoothdevices) | dd.getConnectedBluetoothDevices | 支持 | 支持 | 支持 |
| 传统蓝牙：[开启监听蓝牙状态变化事件](https://open.dingtalk.com/document/orgapp/dd-onbluetoothadapterstatechange) | dd.onBluetoothAdapterStateChange(callback) | 支持 | 支持 | 支持 |
| 传统蓝牙：[移除监听蓝牙状态变化事件](https://open.dingtalk.com/document/orgapp/dd-offbluetoothadapterstatechange) | dd.offBluetoothAdapterStateChange | 支持 | 支持 | 支持 |
| 传统蓝牙：[监听发现新设备事件](https://open.dingtalk.com/document/orgapp/dd-onbluetoothdevicefound) | dd.onBluetoothDeviceFound | 支持 | 支持 | 支持 |
| 传统蓝牙：[移除发现新设备事件](https://open.dingtalk.com/document/orgapp/bluetooth-faq) | dd.offBluetoothDeviceFound | 支持 | 支持 | 支持 |
| Wi-Fi | [初始化Wi-Fi模块](https://open.dingtalk.com/document/orgapp/initialize-the-wi-fi-module) | dd.startWifi | 支持 | 支持 | 支持 |
| [关闭Wi-Fi模块](https://open.dingtalk.com/document/orgapp/close-wi-fi-module) | dd.stopWifi | 支持 | 支持 | 支持 |
| [连接Wi-Fi](https://open.dingtalk.com/document/orgapp/connection-wi-fi) | dd.connectWifi | 支持 | 支持 | 支持 |
| [获取Wi-Fi列表](https://open.dingtalk.com/document/orgapp/get-wi-fi-list) | dd.getWifiList | 支持 | 支持 | 支持 |
| [设置Wi-Fi](https://open.dingtalk.com/document/orgapp/set-wi-fi) | dd.setWifiList | 支持 | 支持 | 支持 |
| [监听连接Wi-Fi事件](https://open.dingtalk.com/document/orgapp/listening-for-connection-wi-fi-events) | dd.onWifiConnected | 支持 | 支持 | 支持 |
| [停止监听连接Wi-Fi事件](https://open.dingtalk.com/document/orgapp/stop-listening-for-connection-wi-fi-events) | dd.offWifiConnected | 支持 | 支持 | 支持 |
| [监听获取到Wi-Fi列表事件](https://open.dingtalk.com/document/orgapp/listener-to-get-wi-fi-list-event) | dd.onGetWifiList | 支持 | 支持 | 支持 |
| [停止监听已获取Wi-Fi列表数据事件](https://open.dingtalk.com/document/orgapp/stop-listening-to-the-obtained-wi-fi-list-data-event) | dd.offGetWifiList | 支持 | 支持 | 支持 |
| [获取已连接Wi-Fi信息](https://open.dingtalk.com/document/orgapp/get-connected-wi-fi-information) | dd.getConnectedWifi | 支持 | 支持 | 支持 |
| [信任SSID](https://open.dingtalk.com/document/orgapp/trust-ssid) | dd.registerSSID | 支持 | 支持 | 支持 |
| [不再信任SSID](https://open.dingtalk.com/document/orgapp/no-longer-trust-this-ssid) | dd.unregisterSSID | 支持 | 支持 | 支持 |

## 地图

| **API说明** | **API名称** | **企业内部应用** | **第三方企业应用** | **第三方个人应用** |
| --- | --- | --- | --- | --- |
| [创建地图对象MapContext](https://open.dingtalk.com/document/orgapp/create-the-map-object-mapcontex) | dd.createMapContext | 支持 | 支持 | 支持 |

## 应用级事件

| **API说明** | **API名称** | **企业内部应用** | **第三方企业应用** | **第三方个人应用** |
| --- | --- | --- | --- | --- |
| [监听小程序错误事件](https://open.dingtalk.com/document/orgapp/listen-for-mini-program-error-events) | dd.onError | 支持 | 支持 | 支持 |
| [取消监听小程序错误事件](https://open.dingtalk.com/document/orgapp/cancels-the-listening-applet-error-event) | dd.offError | 支持 | 支持 | 支持 |
| [监听小程序切前台事件](https://open.dingtalk.com/document/orgapp/listen-for-events-that-occur-when-the-mini-program-is) | dd.onAppShow | 支持 | 支持 | 支持 |
| [取消监听小程序切前台事件](https://open.dingtalk.com/document/orgapp/stops-listening-to-events-that-occur-when-the-mini-program) | dd.offAppShow | 支持 | 支持 | 支持 |
| [监听小程序切后台事件](https://open.dingtalk.com/document/orgapp/listens-to-events-related-to-background-switching-of-mini-programs) | dd.onAppHide | 支持 | 支持 | 支持 |
| [取消监听小程序切后台事件](https://open.dingtalk.com/document/orgapp/cancels-the-listener-for-a-mini-program) | dd.offAppHide | 支持 | 支持 | 支持 |
| [监听要打开的页面不存在事件](https://open.dingtalk.com/document/orgapp/enable-the-listener-the-page-does-not-exist) | dd.onPageNotFound | 支持 | 支持 | 支持 |
| [监听自定义组件内的error事件](https://open.dingtalk.com/document/orgapp/listen-to-error-events-in-custom-components) | dd.onComponentError | 支持 | 支持 | 支持 |
| [取消监听自定义组件内的error事件](https://open.dingtalk.com/document/orgapp/cancels-the-error-event-of-a-custom-component) | dd.offComponentError | 支持 | 支持 | 支持 |

## **文件管理器**

| **API说明** | **API名称** | **企业内部应用** | **第三方企业应用** | **第三方个人应用** |
| --- | --- | --- | --- | --- |
| [创建本地用户目录](https://open.dingtalk.com/document/orgapp/creat-folder) | FileSystemManager.mkdir | 支持 | 支持 | 支持 |
| [判断文件或目录是否存在](https://open.dingtalk.com/document/orgapp/determine-whether-a-file-or-directory-exists) | FileSystemManager.access | 支持 | 支持 | 支持 |
| [保存文件](https://open.dingtalk.com/document/orgapp/save-file) | FileSystemManager.saveFile | 支持 | 支持 | 支持 |
| [获取文件信息](https://open.dingtalk.com/document/orgapp/get-file-information) | FileSystemManager.getFileInfo | 支持 | 支持 | 支持 |
| [获取本地用户文件和目录列表](https://open.dingtalk.com/document/orgapp/obtains-a-list-of-local-user-files) | FileSystemManager.readdir | 支持 | 支持 | 支持 |
| [获取文件或目录的status对象](https://open.dingtalk.com/document/orgapp/obtain-the-file-status-object) | FileSystemManager.stat | 支持 | 支持 | 支持 |
| [获取本地缓存文件列表](https://open.dingtalk.com/document/orgapp/obtains-a-list-of-local-cached-files) | FileSystemManager.getSavedFileList | 支持 | 支持 | 支持 |
| [读取本地用户文件内容](https://open.dingtalk.com/document/orgapp/read-local-user-file) | FileSystemManager.readFile | 支持 | 支持 | 支持 |
| [删除本地用户文件目录](https://open.dingtalk.com/document/orgapp/delete-local-user-file-directory) | FileSystemManager.rmdir | 支持 | 支持 | 支持 |
| [删除本地用户文件](https://open.dingtalk.com/document/orgapp/delete-objects-local) | FileSystemManager.unlink | 支持 | 支持 | 支持 |
| [删除本地缓存文件](https://open.dingtalk.com/document/orgapp/delete-local-cache-files) | FileSystemManager.removeSavedFile | 支持 | 支持 | 支持 |
| [复制文件保存到本地用户目录内](https://open.dingtalk.com/document/orgapp/copy-the-file-to-the-local-user-directory) | FileSystemManager.copyFile | 支持 | 支持 | 支持 |
| [重命名并移动本地用户文件或目录](https://open.dingtalk.com/document/orgapp/rename-and-move-local-user-files-or-directories) | FileSystemManager.rename | 支持 | 支持 | 支持 |
| [向本地用户目录写入文件](https://open.dingtalk.com/document/orgapp/write-file-to-local-user-directory) | FileSystemManager.writeFile | 支持 | 支持 | 支持 |
| [向本地用户文件末尾添加内容](https://open.dingtalk.com/document/orgapp/append-content-to-the-end-of-the-local-user-file) | FileSystemManager.appendFile | 支持 | 支持 | 支持 |
| [解压本地用户文件](https://open.dingtalk.com/document/orgapp/unzip-local-user-files) | FileSystemManager.unzip | 支持 | 支持 | 支持 |

## 开放接口

**扫码**

| **API说明** | **API名称** | **企业内部应用** | **第三方企业应用** | **第三方个人应用** |
| --- | --- | --- | --- | --- |
| [扫码](https://open.dingtalk.com/document/orgapp/mini-program-jsapi-sweep-code) | dd.scan | 支持 | 支持 | 支持 |

**分享**

| **API名称** | **API说明** | **企业内部应用** | **第三方企业应用** | **第三方个人应用** |
| --- | --- | --- | --- | --- |
| [分享](https://open.dingtalk.com/document/orgapp/mini-program-jsapi-share) | dd.onShareAppMessage | 支持 | 支持 | 支持 |

**通讯录选人**

| **API名称** | **API说明** | **企业内部应用** | **第三方企业应用** | **第三方个人应用** |
| --- | --- | --- | --- | --- |
| [选人与部门](https://open.dingtalk.com/document/orgapp/candidates-and-departments) | dd.complexChoose | 支持 | 支持 | 不支持 |
| [选择部门信息](https://open.dingtalk.com/document/orgapp/select-department-information) | dd.chooseDepartments | 支持 | 支持 | 不支持 |
| [创建企业群](https://open.dingtalk.com/document/orgapp/create-enterprise-group-chat) | dd.createGroupChat | 支持 | 支持 | 不支持 |
| [选取手机通讯录](https://open.dingtalk.com/document/orgapp/mini-program-jsapi-select-phone-address-book) | dd.choosephonebook | 支持 | 支持 | 不支持 |
| [选择外部联系人](https://open.dingtalk.com/document/orgapp/mini-program-jsapi-select-external-contacts) | dd.chooseExternalUsers | 支持 | 支持 | 不支持 |
| [编辑外部联系人](https://open.dingtalk.com/document/orgapp/mini-program-jsapi-vedit-external-contacts) | dd.editExternalUser | 支持 | 支持 | 不支持 |
| [单选自定义联系人](https://open.dingtalk.com/document/orgapp/mini-program-jsapi-custom-radio-contact) | dd.chooseUserFromList | 支持 | 支持 | 不支持 |

**Ding**

| **API说明** | **API名称** | **企业内部应用** | **第三方企业应用** | **第三方个人应用** |
| --- | --- | --- | --- | --- |
| [DING](https://open.dingtalk.com/document/orgapp/ding) | dd.createDing | 支持 | 支持 | 不支持 |

**电话**

| **API** | **说明API名称** | **企业内部应用** | **第三方企业应用** | **第三方个人应用** |
| --- | --- | --- | --- | --- |
| [拨打钉钉电话](https://open.dingtalk.com/document/orgapp/call-dingtalk) | dd.callUsers | 支持 | 支持 | 不支持 |
| [唤起拨打电话菜单](https://open.dingtalk.com/document/orgapp/call-menu) | dd.showCallMenu | 支持 | 支持 | 支持 |
| [检查某企业办公电话开通状态](https://open.dingtalk.com/document/orgapp/check-the-status-of-office-phone-numbers-of-an-enterprise) | dd.checkBizCall | 支持 | 支持 | 不支持 |

**支付**

| **API名称** | **API说明** | **企业内部应用** | **第三方企业应用** | **第三方个人应用** |
| --- | --- | --- | --- | --- |
| [支付](https://open.dingtalk.com/document/orgapp/mini-program-jsapi-payment) | dd.pay | 支持 | 支持 | 支持 |

**钉盘**

| **API名称** | **API说明** | **企业内部应用** | **第三方企业应用** | **第三方个人应用** |
| --- | --- | --- | --- | --- |
| [转存文件到钉盘](https://open.dingtalk.com/document/orgapp/transfer-files-to-a-nail-drive) | dd.saveFileToDingTalk | 支持 | 支持 | 不支持 |
| [钉盘文件预览](https://open.dingtalk.com/document/orgapp/nail-plate-file-preview) | dd.previewFileInDingTalk | 支持 | 支持 | 不支持 |
| [上传附件到钉盘/从钉盘选择文件](https://open.dingtalk.com/document/orgapp/upload-attachment-to-nail-plate-select-file-from-nail-plate) | dd.uploadAttachmentToDingTalk | 支持 | 支持 | 不支持 |
| [选取钉盘目录](https://open.dingtalk.com/document/orgapp/select-a-pin-plate-directory) | dd.chooseDingTalkDir | 支持 | 支持 | 不支持 |

**会话**

| **API说明** | **API名称** | **企业内部应用** | **第三方企业应用** | **第三方个人应用** |
| --- | --- | --- | --- | --- |
| [选择会话](https://open.dingtalk.com/document/orgapp/select-session) | dd.chooseChat | 支持 | 支持 | 不支持 |
| [根据chatId跳转到对应会话](https://open.dingtalk.com/document/orgapp/redirects-to-a-specific-session-based-on-the-chatid) | dd.openChatByChatId | 支持 | 支持 | 不支持 |
| [打开与某个用户的聊天页面（单聊会话）](https://open.dingtalk.com/document/orgapp/open-a-chat-page-one-on-one-chat-session-with-a-user) | dd.openChatByUserId | 支持 | 支持 | 不支持 |

**授权**

| **API名称** | **API说明** | **企业内部** | **第三方企业应用** | **第三方个人应用** |
| --- | --- | --- | --- | --- |
| 审批：[授权获取审批实例数据](https://open.dingtalk.com/document/direction-test/authorize-to-obtain-approved-instance-data) | dd.requestAuthInfo | 支持 | 支持 | 不支持 |
