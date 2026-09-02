---
title: "JSAPI总览"
source_url: "https://open.dingtalk.com/document/development/mini-program-jsapi-overview"
namespace: "development"
slug: "mini-program-jsapi-overview"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > JSAPI总览"
doc_id: "6ZDGHB3l20"
updated_at: "2026-09-01 09:15:53"
---

> Source: https://open.dingtalk.com/document/development/mini-program-jsapi-overview
> Path: 应用开发 / 客户端 JSAPI / 历史文档（不推荐） > 小程序 > JSAPI总览
> Updated: 2026-09-01 09:15:53

# JSAPI总览

**扫码体验**

![小程序JSAPI预览地址](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7866091161/p236554.png)

## 基础

| **API名称** | **API说明** | **支持范围** |
| --- | --- | --- |
| [dd.corpId](0476-dd-corpid.md) | 获取当前用户的企业corpId | - 企业内部应有 - 第三方企业应用 |
| [dd.canIUse](0477-dd-caniuse.md) | 判断小程序的API、回调、参数、组件等是否在当前版本可用 | - 企业内部应有 - 第三方企业应用 - 第三方个人应用 |
| [获取基础库版本号](0479-gets-the-version-number-of-the-base-database.md) | 获取基础库版本号 |
| [dd.getAppIdSync](0480-synchronously-obtain-the-appid-of-the-mini-program.md) | 同步获取小程序AppId |
| [dd.getLaunchOptionsSync](0482-obtains-the-startup-parameters-of-mini-programs.md) | 获取小程序启动时的参数 |
| [dd.getRunScene](0481-obtain-the-running-version-of-the-mini-program.md) | 获取小程序的运行版本 |

## 免登

| **API名称** | **API说明** | **支持范围** |
| --- | --- | --- |
| [dd.getAuthCode](0478-mini-program-free-login.md) | 免登授权码 | - 企业内部应有 - 第三方企业应用 - 第三方个人应用 |

## 更新管理小程序

| **API名称** | **API说明** | **支持范围** |
| --- | --- | --- |
| [使用UpdateManager更新小程序](0483-updatemanager.md) | 获取全局唯一的版本更新管理器，用于管理小程序更新 | - 企业内部应有 - 第三方企业应用 - 第三方个人应用 |
| [UpdateManager.applyUpdate()](0483-updatemanager.md) | 强制小程序重启并使用新版本使用 |
| [UpdateManager.onCheckForUpdate(function callback)](0483-updatemanager.md) | 监听向钉钉后台请求检查更新结果事件 |
| [UpdateManager.onUpdateReady(function callback)](0483-updatemanager.md) | 监听小程序有版本更新事件 |
| [UpdateManager.onUpdateFaile(function callback)](0483-updatemanager.md) | 监听小程序更新失败事件 |

## 网络

| **类目** | **API名称** | **API说明** | **支持范围** |
| --- | --- | --- | --- |
| **发网络请求** | [dd.httpRequest](0484-send-network-requests.md) | 发网络请求 | - 企业内部应有 - 第三方企业应用 - 第三方个人应用 |
| **上传下载** | [dd.uploadFile](0485-dd-upload-objects.md) | 上传文件 |
| [dd.downloadFile](0486-mini-program-download-objects.md) | 下载文件 |
| **WebSocket** | [dd.connectSocket](0488-dd-connectsocket.md) | 创建WebSocket连接 |
| [dd.onSocketOpen](0495-dd-onsocketopen.md) | 监听WebSocket连接打开事件 |
| [dd.offSocketOpen](0497-dd-offsocketopen.md) | 取消监听WebSocket连接打开事件 |
| [dd.onSocketError](0489-dd-onsocketerror.md) | 监听WebSocket错误 |
| [dd.offSocketError](0494-dd-offsocketerror.md) | 取消监听WebSocket错误 |
| [dd.sendSocketMessage](0487-dd-sendsocketmessage.md) | 发送数据 |
| [dd.onSocketMessage](0492-dd-onsocketmessage.md) | 监听接收到的消息事件 |
| [dd.offSocketMessage](0493-dd-offsocketmessage.md) | 取消监听接收消息事件 |
| [dd.closeSocket](0490-dd-closesocket.md) | 关闭WebSocket连接 |
| [dd.onSocketClose](0491-dd-onsocketclose.md) | 监听WebSocket关闭 |
| [dd.offSocketClose](0496-dd-offsocketclose.md) | 取消监听WebSocket关闭事件 |

## 多媒体

| **类目** | **API名称** | **API说明** | **支持范围** |
| --- | --- | --- | --- |
| **图片** | [dd.chooseImage](0498-dd-chooseimage.md) | [选择图片](https://open.dingtalk.com/document/orgapp/dd-chooseimage) | - 企业内部应有 - 第三方企业应用 - 第三方个人应用 |
| [dd.previewImage](0499-dd-previewimage.md) | [预览图片](https://open.dingtalk.com/document/orgapp/dd-previewimage) |
| [dd.saveImage](0503-dd-saveimage.md) | [保存图片到手机相册](https://open.dingtalk.com/document/orgapp/dd-saveimage) |
| [dd.compressImage](0500-dd-compressimage.md) | [压缩图片](https://open.dingtalk.com/document/orgapp/dd-compressimage) |
| [dd.getImageInfo](0502-dd-getimageinfo.md) | [获取图片信息](https://open.dingtalk.com/document/orgapp/dd-getimageinfo) |
| [dd.editPicture](0501-dd-editpicture.md) | [编辑图片](https://open.dingtalk.com/document/orgapp/dd-editpicture) |
| **录音管理** | [dd.getRecorderManager](0504-dd-getrecordermanager.md) | [获取录音管理器](https://open.dingtalk.com/document/orgapp/dd-getrecordermanager) |
| **背景音频管理** | [dd.getBackgroundAudioManager](0505-dd-getbackgroundaudiomanager.md) | [获取背景音频管理](https://open.dingtalk.com/document/orgapp/dd-getbackgroundaudiomanager) |
| **视频** | [dd.chooseVideo](0506-dd-choosevideo.md) | [选择视频](https://open.dingtalk.com/document/orgapp/dd-choosevideo) |
| [dd.createVideoContext(videoId)](0507-dd-createvideocontext-videoid.md) | [创建video对象](https://open.dingtalk.com/document/orgapp/dd-createvideocontext-videoid) |

## 界面

| **类目** | **API名称** | **API说明** | **支持范围** |
| --- | --- | --- | --- |
| **导航栏** | [dd.navigateTo](0509-dd-navigateto.md) | 页面跳转（保留当前页） | - 企业内部应有 - 第三方企业应用 - 第三方个人应用 |
| [dd.redirectTo](0510-dd-redirectto.md) | 页面跳转（关闭当前页） |
| [dd.reLaunch](0511-dd-relaunch.md) | 页面跳转（关闭所有页面） |
| [dd.navigateBack](0512-dd-navigateback.md) | 返回上一级或多级页面 |
| [dd.setNavigationBar](0508-dd-setnavigationbar.md) | 设置导航栏 |
| **TabBar** | [dd.switchTab](0519-dd-switchtab.md) | 跳转到指定tabBar页面 |
| [dd.setTabBarBadge](0513-dd-settabbarbadge.md) | 添加tabBar文本 |
| [dd.removeTabBarBadge](0514-dd-removetabbarbadge.md) | 移除tabBar文本 |
| [dd.showTabBarRedDot](0515-dd-showtabbarreddot.md) | 显示tabBar红点 |
| [dd.hideTabBarRedDot](0516-dd-hidetabbarreddot.md) | 隐藏tabBar红点 |
| [dd.addTabBarItem](0517-dd-addtabbaritem.md) | 添加tabBar页面 |
| [dd.removeTabBarItem](0518-dd-removetabbaritem.md) | 移除tabBar页面 |
| **显示模式** | [dd.getColorSchemeSync](0520-display-mode.md) | 显示模式 |
| **交互反馈** | [dd.alert](0521-dd-alert.md) | 显示警告框 |
| [dd.confirm](0522-dd-confirm.md) | 显示确认框 |
| [dd.showToast](0523-dd-showtoast.md) | 显示弱提示 |
| [dd.hideToast](0524-dd-hidetoast.md) | 隐藏弱提示 |
| [dd.showLoading](0525-dd-showloading.md) | 显示加载提示 |
| [dd.hideLoading](0526-dd-hideloading.md) | 隐藏加载提示 |
| [dd.showActionSheet](0527-dd-showactionsheet.md) | 显示操作菜单 |
| **离开页面二次确认** | [dd.enableLeaveConfirm](0528-dd-enableleaveconfirm.md) | 离开二次确认配置 |
| [dd.disableLeaveConfirm](0529-dd-disableleaveconfirm.md) | 取消当前页面的离开二次确认 |
| **下拉刷新** | [dd.stopPullDownRefresh](0530-dd-stoppulldownrefresh.md) | 停止下拉刷新 |
| [onPullDownRefresh](0531-onpulldownrefresh.md) | 下拉刷新 |
| **选择日期** | [dd.datePicker](0532-dd-datepicker.md) | 打开日期选择列表 |
| **动画** | [dd.createAnimation](0533-dd-createanimation.md) | 创建动画实例 |
| **画布** | [dd.createCanvasContext](0535-create-a-canvas.md) | 创建canvas |
| **键盘** | [dd.onKeyboardShow](0576-dd-onkeyboardshow.md) | 监听键盘弹起事件 |
| [dd.onKeyboardHide](0577-dd-onkeyboardhide.md) | 监听键盘收起事件 |
| [dd.hideKeyboard](0575-dd-hidekeyboard.md) | 隐藏键盘 |
| **滚动** | [dd.pageScrollTo](0578-dd-pagescrollto.md) | 滚动到页面的目标位置 |
| **字体** | [dd.loadFontFace](0579-dynamically-load-network-fonts.md) | 动态加载网络字体 |

## **小程序跳转**

| **API名称** | **API说明** | **支持范围** |
| --- | --- | --- |
| [dd.navigateToMiniProgram](0581-inter-mini-program-jump.md) | 跳转到另一个钉钉小程序 | - 企业内部应有 - 第三方企业应用 - 第三方个人应用 |
| [dd.navigateBackMiniProgram](0580-return-to-the-previous-dingtalk-mini-program.md) | 返回上一个钉钉小程序 |

## 节点查询

| **API名称** | **API说明** | **支持范围** |
| --- | --- | --- |
| [dd.createIntersectionObserver](0582-dd-createintersectionobserver.md) | 创建IntersectionObserver对象实例 | - 企业内部应有 - 第三方企业应用 - 第三方个人应用 |
| [dd.createSelectorQuery](0584-dd-createselectorquery.md) | 创建SelectorQuery节点查询对象 |

## 位置

| **API名称** | **API说明** | **支持范围** |
| --- | --- | --- |
| [dd.getLocation](0587-dd-getlocation.md) | 获取用户当前的地理位置信息 | - 企业内部应有 - 第三方企业应用 - 第三方个人应用 |
| [dd.openLocation](0586-dd-openlocation.md) | 使用内置地图查看位置 |

## 缓存

| **API名称** | **API说明** | **支持范围** |
| --- | --- | --- |
| [dd.setStorage](0591-dd-setstorage.md) | 将数据存储在本地缓存 | - 企业内部应有 - 第三方企业应用 - 第三方个人应用 |
| [dd.setStorageSync](0590-dd-setstoragesync.md) | 同步将数据存储 |
| [dd.getStorage](0594-dd-getstorage.md) | 异步获取指定key的缓存数据 |
| [dd.getStorageSync](0595-dd-getstoragesync.md) | 同步获取指定key的缓存数据 |
| [dd.removeStorage](0589-dd-removestorage.md) | 删除缓存数据 |
| [dd.removeStorageSync](0596-dd-removestoragesync.md) | 同步删除指定key的缓存数据 |
| [dd.getStorageInfoSync](0597-obtains-information-about-the-current-cache.md) | 同步获取当前storage的相关信息 |
| [dd.getStorageInfo](0598-get-current-cached-data-asynchronously.md) | 异步获取当前storage的相关信息 |
| [dd.clearStorageSync](0592-synchronous-deletion-of-locally-cached-data.md) | 同步清除本地缓存数据 |
| [dd.clearStorage](0593-delete-locally-cached-data-asynchronously.md) | 异步清除本地缓存数据 |

## 设备

| **类目** | **API名称** | **API说明** | **支持范围** |
| --- | --- | --- | --- |
| **系统信息** | [dd.getSystemInfo](0599-dd-getsysteminfo.md) | 获取手机系统信息 | - 企业内部应有 - 第三方企业应用 - 第三方个人应用 |
| [dd.getSystemInfoSyn](0600-dd-getsysteminfosync.md) | 获取手机系统信息的同步接口 |
| **网络状态** | [dd.getNetworkType](0601-dd-getnetworktype.md) | 获取当前网络状态 |
| **剪切板** | [dd.getClipboard](0603-dd-getclipboard.md) | 获取系统剪贴板的内容 |
| [dd.setClipboard](0602-dd-setclipboard.md) | 设置剪切板数据 |
| **振动** | [dd.vibrate](0606-dd-vibrate.md) | 使用振动功能 |
| [dd.vibrateShort](0604-dd-vibrateshort.md) | 使用短振动 |
| [dd.vibrateLong](0605-dd-vibratelong.md) | 使用长振动 |
| **蓝牙** | [dd.connectBLEDevice](0611-dd-connectbledevice.md) | 低耗电蓝牙：查找设备并连接 |
| [dd.disconnectBLEDevice](0608-dd-disconnectbledevice.md) | 低耗电蓝牙：断开蓝牙链接 |
| [dd.getBLEDeviceCharacteristics](0622-dd-getbledevicecharacteristics.md) | 低耗电蓝牙：获取蓝牙设备所有特征值 |
| [dd.getBLEDeviceServices](0619-dd-getbledeviceservices.md) | 低耗电蓝牙：获取蓝牙设备所有服务 |
| [dd.notifyBLECharacteristicValueChange](0616-dd-notifyblecharacteristicvaluechange.md) | 低耗电蓝牙：设置读特征通知模式 |
| [dd.onBLECharacteristicValueChange](0617-dd-onblecharacteristicvaluechange.md) | 低耗电蓝牙：监听特征值变化事件 |
| [dd.offBLECharacteristicValueChange](0623-dd-offblecharacteristicvaluechange.md) | 低耗电蓝牙：移除监听特征值变化事件 |
| [dd.offBLEConnectionStateChanged](0625-dd-offbleconnectionstatechanged.md) | 低耗电蓝牙：移除监听连接状态变化事件 |
| [dd.onBLEConnectionStateChanged(callback)](0620-dd-onbleconnectionstatechanged.md) | 低耗电蓝牙：监听蓝牙连接状态事件 |
| [dd.readBLECharacteristicValue](0624-dd-readblecharacteristicvalue.md) | 低耗电蓝牙：读取蓝牙设备特征值数据 |
| [dd.writeBLECharacteristicValue](0629-dd-writeblecharacteristicvalue.md) | 低耗电蓝牙：向蓝牙设备特征值中写入数据 |
| [dd.openBluetoothAdapter](0609-dd-openbluetoothadapter.md) | 传统蓝牙：初始化蓝牙接口 |
| [dd.closeBluetoothAdapter](0612-dd-closebluetoothadapter.md) | 传统蓝牙：关闭蓝牙适配器 |
| [dd.getBluetoothAdapterState](0618-dd-getbluetoothadapterstate.md) | 传统蓝牙：获取本机蓝牙模块状态 |
| [dd.startBluetoothDevicesDiscovery](0613-dd-startbluetoothdevicesdiscovery.md) | 传统蓝牙：搜寻附近蓝牙设备 |
| [dd.stopBluetoothDevicesDiscovery](0621-dd-stopbluetoothdevicesdiscovery.md) | 传统蓝牙：停止搜寻附近的蓝牙设备 |
| [dd.getBluetoothDevices](0626-dd-getbluetoothdevices.md) | 传统蓝牙：获取所有已发现的蓝牙设备 |
| [dd.getConnectedBluetoothDevices](0610-dd-getconnectedbluetoothdevices.md) | 传统蓝牙：获取已连接设备 |
| [dd.onBluetoothAdapterStateChange(callback)](0627-dd-onbluetoothadapterstatechange.md) | 传统蓝牙：开启监听蓝牙状态变化事件 |
| [dd.offBluetoothAdapterStateChange](0628-dd-offbluetoothadapterstatechange.md) | 传统蓝牙：移除监听蓝牙状态变化事件 |
| [dd.onBluetoothDeviceFound](0614-dd-onbluetoothdevicefound.md) | 传统蓝牙：监听发现新设备事件 |
| [dd.offBluetoothDeviceFound](0615-bluetooth-faq.md) | 传统蓝牙：移除发现新设备事件 |
| Wi-Fi | [dd.startWifi](0639-initialize-the-wi-fi-module.md) | 初始化Wi-Fi模块 |
| [dd.stopWifi](0638-close-wi-fi-module.md) | 关闭Wi-Fi模块 |
| [dd.connectWifi](0633-connection-wi-fi.md) | 连接Wi-Fi |
| [dd.getWifiList](0637-get-wi-fi-list.md) | 获取Wi-Fi列表 |
| [dd.setWifiList](0634-set-wi-fi.md) | 设置 Wi-Fi 中 AP 的相关信息 |
| [dd.onWifiConnected](0640-listening-for-connection-wi-fi-events.md) | 监听连接Wi-Fi事件 |
| [dd.offWifiConnected](0642-stop-listening-for-connection-wi-fi-events.md) | 停止监听连接Wi-Fi事件 |
| [dd.onGetWifiList](0643-listener-to-get-wi-fi-list-event.md) | 监听获取到Wi-Fi列表事件 |
| [dd.offGetWifiList](0644-stop-listening-to-the-obtained-wi-fi-list-data-event.md) | 停止监听已获取Wi-Fi列表数据事件 |
| [dd.getConnectedWifi](0641-get-connected-wi-fi-information.md) | 获取已连接Wi-Fi信息 |
| [dd.registerSSID](0635-trust-ssid.md) | 信任SSID |
| [dd.unregisterSSID](0636-no-longer-trust-this-ssid.md) | 不再信任SSID |

## 地图

| **API名称** | **API说明** | **支持范围** |
| --- | --- | --- |
| [dd.createMapContext](0645-create-the-map-object-mapcontex.md) | 创建并返回一个地图上下文对象 | - 企业内部应有 - 第三方企业应用 - 第三方个人应用 |

## 应用级事件

| **API名称** | **API说明** | **支持范围** |
| --- | --- | --- |
| [dd.onError](0663-listen-for-mini-program-error-events.md) | 监听小程序错误事件 | - 企业内部应有 - 第三方企业应用 - 第三方个人应用 |
| [dd.offError](0666-cancels-the-listening-applet-error-event.md) | 取消监听小程序错误事件 |
| [dd.onAppShow](0664-listen-for-events-that-occur-when-the-mini-program-is.md) | 监听小程序切前台事件 |
| [dd.offAppShow](0667-stops-listening-to-events-that-occur-when-the-mini-program.md) | 取消监听小程序切前台事件 |
| [dd.onAppHide](0665-listens-to-events-related-to-background-switching-of-mini-programs.md) | 监听小程序切后台事件 |
| [dd.offAppHide](0668-cancels-the-listener-for-a-mini-program.md) | 取消监听小程序切后台事件 |
| [dd.onPageNotFound](0669-enable-the-listener-the-page-does-not-exist.md) | 监听要打开的页面不存在事件 |
| [dd.onComponentError](0670-listen-to-error-events-in-custom-components.md) | 监听自定义组件内的error事件 |
| [dd.offComponentError](0671-cancels-the-error-event-of-a-custom-component.md) | 取消监听自定义组件内的error事件 |

## **文件管理器**

| **API名称** | **API说明** | **支持范围** |
| --- | --- | --- |
| [FileSystemManager.mkdir](0675-creat-folder.md) | 创建本地用户目录 | - 企业内部应有 - 第三方企业应用 - 第三方个人应用 |
| [FileSystemManager.access](0683-determine-whether-a-file-or-directory-exists.md) | 判断文件或目录是否存在 |
| [FileSystemManager.saveFile](0673-save-file.md) | 将本地临时文件保存为本地缓存文件或本地用户文件 |
| [FileSystemManager.getFileInfo](0674-get-file-information.md) | 获取本地临时文件、本地缓存文件和本地用户文件的信息 |
| [FileSystemManager.readdir](0685-obtains-a-list-of-local-user-files.md) | 获取本地用户文件和目录列表 |
| [FileSystemManager.stat](0684-obtain-the-file-status-object.md) | 获取文件或目录的status对象 |
| [FileSystemManager.getSavedFileList](0679-obtains-a-list-of-local-cached-files.md) | 获取本地缓存文件列表 |
| [FileSystemManager.readFile](0680-read-local-user-file.md) | 读取本地用户文件内容 |
| [FileSystemManager.rmdir](0681-delete-local-user-file-directory.md) | 删除本地用户文件目录 |
| [FileSystemManager.unlink](0676-delete-objects-local.md) | 删除本地用户文件 |
| [FileSystemManager.removeSavedFile](0677-delete-local-cache-files.md) | 删除本地缓存文件 |
| [FileSystemManager.copyFile](0687-copy-the-file-to-the-local-user-directory.md) | 复制文件保存到本地用户目录内 |
| [FileSystemManager.rename](0688-rename-and-move-local-user-files-or-directories.md) | 重命名并移动本地用户文件或目录 |
| [FileSystemManager.writeFile](0682-write-file-to-local-user-directory.md) | 向本地用户目录写入文件 |
| [FileSystemManager.appendFile](0686-append-content-to-the-end-of-the-local-user-file.md) | 向本地用户文件末尾添加内容 |
| [FileSystemManager.unzip](0678-unzip-local-user-files.md) | 解压本地用户文件 |

## 开放接口

### **扫码**

| **API名称** | **API说明** | **支持范围** |
| --- | --- | --- |
| [扫码](0689-mini-program-jsapi-sweep-code.md) | 使用扫一扫功能 | - 企业内部应有 - 第三方企业应用 - 第三方个人应用 |

### **分享**

| **API名称** | **API说明** | **支持范围** |
| --- | --- | --- |
| [dd.onShareAppMessage](0690-mini-program-jsapi-share.md) | 自定义页面分享内容 | - 企业内部应有 - 第三方企业应用 - 第三方个人应用 |

### **通讯录选人**

| **API名称** | **API说明** | **支持范围** |
| --- | --- | --- |
| [dd.complexChoose](0691-candidates-and-departments.md) | 选择人和部门，选择部门后把该部门转换成对应部门下的人 | - 企业内部应有 - 第三方企业应用 |
| [dd.chooseDepartments](0692-select-department-information.md) | 返回部门的信息，以部门为纬度 |
| [dd.createGroupChat](0693-create-enterprise-group-chat.md) | 创建企业群聊天 |
| [dd.choosephonebook](0694-mini-program-jsapi-select-phone-address-book.md) | 选取用户手机联系人 |
| [dd.chooseExternalUsers](0695-mini-program-jsapi-select-external-contacts.md) | 选择外部联系人 |
| [dd.editExternalUser](0696-mini-program-jsapi-vedit-external-contacts.md) | 编辑外部联系人 |
| [dd.chooseUserFromList](0697-mini-program-jsapi-custom-radio-contact.md) | 选取单个自定义联系人 |

### **Ding**

| **API名称** | **API说明** | **支持范围** |
| --- | --- | --- |
| [DING](0698-ding-1.md) | 发起DING | - 企业内部应有 - 第三方企业应用 |

### **电话**

| **API名称** | **API说明** | **支持范围** |
| --- | --- | --- |
| [dd.callUsers](0699-call-dingtalk.md) | 拨打钉钉电话 | - 企业内部应有 - 第三方企业应用   不支持 |
| [dd.checkBizCall](0701-check-the-status-of-office-phone-numbers-of-an-enterprise.md) | 检查某企业办公电话开通状态 |
| [dd.showCallMenu](0700-call-menu.md) | 唤起拨打电话菜单 | - 企业内部应有 - 第三方企业应用 - 第三方个人应用 |

### **支付**

| **API名称** | **API说明** | **支持范围** |
| --- | --- | --- |
| [dd.pay](0702-mini-program-jsapi-payment.md) | 发起支付 | - 企业内部应有 - 第三方企业应用 - 第三方个人应用 |

### **钉盘**

| **API名称** | **API说明** | **支持范围** |
| --- | --- | --- |
| [dd.saveFileToDingTalk](0705-transfer-files-to-a-nail-drive.md) | 转存文件到钉盘 | - 企业内部应有 - 第三方企业应用 - 第三方个人应用 |
| [dd.previewFileInDingTalk](0703-nail-plate-file-preview.md) | 钉盘文件预览 |
| [dd.uploadAttachmentToDingTalk](0706-upload-attachment-to-nail-plate-select-file-from-nail-plate.md) | 传附件到钉盘，或从钉盘选择文件 |
| [dd.chooseDingTalkDir](0704-select-a-pin-plate-directory.md) | 唤起钉盘选择器， 从用户当前的企业空间或个人空间选择一个目录 |

### **会话**

| **API名称** | **API说明** | **支持范围** |
| --- | --- | --- |
| [dd.chooseChat](0707-select-session.md) | 选择会话 | - 企业内部应有 - 第三方企业应用 |
| [dd.openChatByChatId](0708-redirects-to-a-specific-session-based-on-the-chatid.md) | 根据chatId跳转到对应会话 |
| [dd.openChatByUserId](0709-open-a-chat-page-one-on-one-chat-session-with-a-user.md) | 打开与某个用户的聊天页面（单聊会话） |

### **授权**

| **API名称** | **API说明** | **支持范围** |
| --- | --- | --- |
| [授权获取审批实例数据](0711-authorize-to-obtain-approved-instance-data-1.md) | 审批：唤起授权弹窗，提示用户授权 | - 企业内部应有 - 第三方企业应用 |
