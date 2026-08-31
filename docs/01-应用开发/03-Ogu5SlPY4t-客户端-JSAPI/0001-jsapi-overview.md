---
title: "JSAPI 总览"
source_url: "https://open.dingtalk.com/document/development/jsapi-overview"
namespace: "development"
slug: "jsapi-overview"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "JSAPI 总览"
doc_id: "zvuIBJqMbq"
updated_at: "2026-05-22 17:54:25"
---

> Source: https://open.dingtalk.com/document/development/jsapi-overview
> Path: 应用开发 / 客户端 JSAPI / JSAPI 总览
> Updated: 2026-05-22 17:54:25

# JSAPI 总览

## **获取凭证**

| **API名称** | **API说明** |
| --- | --- |
| [getAuthCode](0006-jsapi-get-auth-code.md) | 获取小程序免登授权码 |
| [requestAuthCode](0007-jsapi-request-auth-code.md) | 获取微应用免登授权码。 |
| [getOperateAuthCode](0008-jsapi-get-operate-auth-code.md) | 获取微应用反馈式操作的临时授权码 |
| [requestAuthInfo](0009-jsapi-request-auth-info.md) | 唤起授权弹窗，获取用户授权 |

## **基础交互**

### **网络**

| **类目** | **API名称** | **API说明** |
| --- | --- | --- |
| **网络请求** | [httpRequest](0010-jsapi-http-request.md) | 向指定服务器发起一个跨域 http(s) 请求 |
| **上传下载** | [downloadFile](0011-jsapi-download-file.md) | 下载文件资源到本地 |
| [uploadFile](0012-jsapi-upload-file.md) | 上传本地资源到开发者服务器 |
| **WebSocket** | [closeSocket](0013-jsapi-close-socket.md) | 关闭WebSocket连接 |
| [connectSocket](0014-jsapi-connect-socket.md) | 创建一个 WebSocket 的连接 |
| [onSocketOpen](0015-jsapi-on-socket-open.md) | 监听WebSocket连接打开事件 |
| [offSocketOpen](0016-jsapi-off-socket-open.md) | 取消监听WebSocket连接打开事件 |
| [onSocketError](0017-jsapi-on-socket-error.md) | 监听WebSocket错误 |
| [offSocketError](0018-jsapi-off-socket-error.md) | 取消监听WebSocket错误 |
| [onSocketClose](0019-jsapi-on-socket-close.md) | 监听WebSocket关闭 |
| [offSocketClose](0020-jsapi-off-socket-close.md) | 取消监听WebSocket关闭事件 |
| [offSocketMessage](0021-jsapi-off-socket-message.md) | 取消监听WebSocket接收到服务器的消息事件 |
| [onSocketMessage](0022-jsapi-on-socket-message.md) | 监听WebSocket接收到服务器的消息事件 |
| [sendSocketMessage](0023-jsapi-send-socket-message.md) | 通过WebSocket连接发送数据 |

### **基础**

| **API名称** | **API说明** |
| --- | --- |
| [canIUse](0024-jsapi-can-i-use.md) | 判断 API 是否可用 |
| [corpId](0025-jsapi-corp-id.md) | 获取当前访问用户的企业corpId |
| [exit](0026-jsapi-exit.md) | 关闭钉钉小程序 |
| [ExtSDKVersion](0027-jsapi-ext-sdk-version.md) | 使用本接口获取基础库版本号 |
| [getRunScene](0028-jsapi-get-run-scene.md) | 获取当前小程序的运行版本 |
| [getAppIdSync](0029-jsapi-get-app-id-sync.md) | 同步获取小程序的AppId，即MiniAppId |
| [getLaunchOptionsSync](0030-jsapi-get-launch-options-sync.md) | 获取小程序启动时的参数 |
| [SDKVersion](0031-jsapi-sdk-version.md) | 使用本接口获取基础库版本号 |

### **缓存**

| **API名称** | **API说明** |
| --- | --- |
| [clearStorage](0032-jsapi-clear-storage.md) | 异步清除本地缓存数据 |
| [clearStorageSync](0033-jsapi-clear-storage-sync.md) | 同步清除本地storage缓存的数据 |
| [getStorage](0034-jsapi-get-storage.md) | 可以获取指定key的单条缓存数据 |
| [getStorageInfo](0035-jsapi-get-storage-info.md) | 异步获取当前storage下所有缓存信息的key |
| [getStorageSync](0036-jsapi-get-storage-sync.md) | 同步获取缓存数据 |
| [getStorageInfoSync](0037-jsapi-get-storage-info-sync.md) | 同步获取当前storage下所有缓存信息的key、已占用空间大小和限制最大的缓存空间大小信息 |
| [removeStorage](0038-jsapi-remove-storage.md) | 删除缓存数据 |
| [removeStorageSync](0039-jsapi-remove-storage-sync.md) | 同步删除缓存数据 |
| [setStorage](0040-jsapi-set-storage.md) | 将数据存储在本地缓存中指定的 key 中，会覆盖掉原来该 key 对应的数据 |
| [setStorageSync](0041-jsapi-set-storage-sync.md) | 同步将数据存储在本地缓存中指定的 key 中 |

### **界面**

| **类目** | **API名称** | **API说明** |
| --- | --- | --- |
| **导航栏** | [closePage](0042-jsapi-close-page.md) | 关闭当前页面 |
| [goBackPage](0043-jsapi-go-back-page.md) | 返回上一级页面 |
| [quitPage](0044-jsapi-quit-page.md) | PC端关闭页面 |
| [replacePage](0045-jsapi-replace-page.md) | 替换页面 |
| [setNavigationBar](0046-jsapi-set-navigation-bar.md) | 设置小程序导航栏样式及标题等 |
| [setNavigationTitle](0048-jsapi-set-navigation-title.md) | 设置导航栏标题 |
| [setNavigationIcon](0047-jsapi-set-navigation-icon.md) | 标题栏添加问号图标 |
| [setNavigationLeft](0049-jsapi-set-navigation-left.md) | 设置左侧导航按钮文本 |
| **TabBar** | [addTabBarItem](0050-jsapi-add-tab-bar-item.md) | 添加tabBar页面 |
| [hideTabBarRedDot](0051-jsapi-hide-tab-bar-red-dot.md) | 隐藏tabBar红点 |
| [removeTabBarItem](0052-jsapi-remove-tab-bar-item.md) | 移除tabBar页面 |
| [removeTabBarBadge](0053-jsapi-remove-tab-bar-badge.md) | 移除tabBar文本 |
| [setTabBarBadge](0054-jsapi-set-tab-bar-badge.md) | 为 tabBar 某一项的右上角添加文本 |
| [showTabBarRedDot](0055-jsapi-show-tab-bar-red-dot.md) | 显示tabBar红点 |
| [enableLeaveConfirm](0056-jsapi-enable-leave-confirm.md) | 对当前页面进行离开二次确认 |
| **路由** | [navigateTo](0057-jsapi-navigate-to.md) | 跳转到应用内的某个指定页面 |
| [navigateBack](0058-jsapi-navigate-back.md) | 返回上一级或返回多级页面 并且关闭当前页面 |
| [reLaunch](0059-jsapi-re-launch.md) | 跳转到小程序应用内指定页面并且关闭当前所有页面 |
| [redirectTo](0060-jsapi-redirect-to.md) | 跳转到应用内的某个指定页面 |
| [switchTab](0061-jsapi-switch-tab.md) | 跳转到指定 tabBar 页面 |
| **动画** | [createAnimation](0062-jsapi-create-animation.md) | 创建动画实例 |
| [Animation.bottom](0063-jsapi-animation-bottom.md) | 设置动画实例bottom值 |
| [Animation.backgroundColor](0064-jsapi-animation-background-color.md) | 设置动画背景色 |
| [Animation.height](0065-jsapi-animation-height.md) | 设置动画实例高度值 |
| [Animation.left](0066-jsapi-animation-left.md) | 设置动画实例Left值 |
| [Animation.matrix](0067-jsapi-animation-matrix.md) | 设置动画实例Matrix值 |
| [Animation.matrix3d](0068-jsapi-animation-matrix3d.md) | 设置动画实例Matrix3d |
| [Animation.opacity](0069-jsapi-animation-opacity.md) | 设置动画透明度 |
| [Animation.right](0070-jsapi-animation-right.md) | 设置动画实例Right值 |
| [Animation.rotate](0071-jsapi-animation-rotate.md) | 设置动画实例旋转Rotate值 |
| [Animation.rotateX](0072-jsapi-animation-rotate-x.md) | 设置动画实例RotateX值 |
| [Animation.rotateY](0073-jsapi-animation-rotate-y.md) | 设置动画实例RotateY值 |
| [Animation.rotateZ](0074-jsapi-animation-rotate-z.md) | 设置动画实例RotateZ值 |
| [Animation.rotate3d](0075-jsapi-animation-rotate3d.md) | 设置动画实例Rotate3D值 |
| [Animation.scale](0076-jsapi-animation-scale.md) | 设置动画实例Scale值 |
| [Animation.scaleX](0077-jsapi-animation-scale-x.md) | 设置动画实例ScaleX值 |
| [Animation.scaleY](0078-jsapi-animation-scale-y.md) | 设置动画实例ScaleY值 |
| [Animation.scaleZ](0079-jsapi-animation-scale-z.md) | 设置动画实例ScaleZ值 |
| [Animation.scale3d](0080-jsapi-animation-scale3d.md) | 设置动画实例Scale3d值 |
| [Animation.skew](0081-jsapi-animation-skew.md) | 设置动画实例Skew |
| [Animation.skewX](0082-jsapi-animation-skew-x.md) | 设置动画实例SkewX |
| [Animation.skewY](0083-jsapi-animation-skew-y.md) | 设置动画实例SkewY |
| [Animation.top](0084-jsapi-animation-top.md) | 设置动画实例Top值 |
| [Animation.translate](0085-jsapi-animation-translate.md) | 设置动画实例Translate |
| [Animation.translateX](0086-jsapi-animation-translate-x.md) | 设置动画实例TranslateX值 |
| [Animation.translateY](0087-jsapi-animation-translate-y.md) | 设置动画实例TranslateY值 |
| [Animation.translateZ](0088-jsapi-animation-translate-z.md) | 设置动画实例TranslateZ值 |
| [Animation.translate3d](0089-jsapi-animation-translate3d.md) | 设置动画实例Translate3d值 |
| [Animation.width](0090-jsapi-animation-width.md) | 设置动画实例长度值 |
| **画布** | [createCanvasContext](0091-jsapi-create-canvas-context.md) | 创建canvas绘图上下文 |
| [CanvasContext.arc](0092-jsapi-canvas-context-arc.md) | 画一条弧线 |
| [CanvasContext.addColorStop](0093-jsapi-canvas-context-add-color-stop.md) | 创建渐变点 |
| [CanvasContext.beginPath](0094-jsapi-canvas-context-begin-path.md) | 创建一个路径 |
| [CanvasContext.bezierCurveTo](0095-jsapi-canvas-context-bezier-curve-to.md) | 创建三次方贝塞尔曲线路径 |
| [CanvasContext.clip](0096-jsapi-canvas-context-clip.md) | 创建的路径设置为当前剪切路径 |
| [CanvasContext.clearRect](0097-jsapi-canvas-context-clear-rect.md) | 清除画布上在该矩形区域内的内容 |
| [CanvasContext.closePath](0098-jsapi-canvas-context-close-path.md) | 关闭一个路径 |
| [CanvasContext.createLinearGradient](0099-jsapi-canvas-context-create-linear-gradient.md) | 创建一个线性的渐变色 |
| [CanvasContext.createCircularGradient](0100-jsapi-canvas-context-create-circular-gradient.md) | 创建一个圆形的渐变色 |
| [CanvasContext.draw](0101-jsapi-canvas-context-draw.md) | 在绘图上下文中的描述（路径、变形、样式）画到 canvas 中 |
| [CanvasContext.drawImage](0102-jsapi-canvas-context-draw-image.md) | 绘制图像 |
| [CanvasContext.fill](0103-jsapi-canvas-context-fill.md) | 对当前路径中的内容进行填充 |
| [CanvasContext.fillRect](0104-jsapi-canvas-context-fill-rect.md) | 填充矩形 |
| [CanvasContext.fillText](0105-jsapi-canvas-context-fill-text.md) | 在画布上绘制被填充的文本 |
| [CanvasContext.getImageData](0106-jsapi-canvas-context-get-image-data.md) | 获取canvas区域隐含的像素数据 |
| [CanvasContext.lineTo](0107-jsapi-canvas-context-line-to.md) | 创建一条从上次指定点到目标点的线 |
| [CanvasContext.moveTo](0108-jsapi-canvas-context-move-to.md) | 将路径移动到画布中的指定点 |
| [CanvasContext.putImageData](0109-jsapi-canvas-context-put-image-data.md) | 将像素数据绘制到画布 |
| [CanvasContext.quadraticCurveTo](0110-jsapi-canvas-context-quadratic-curve-to.md) | 创建二次贝塞尔曲线路径 |
| [CanvasContext.rect](0111-jsapi-canvas-context-rect.md) | 创建一个矩形 |
| [CanvasContext.rotate](0112-jsapi-canvas-context-rotate.md) | 以原点为中心（原点可以用translate方法修改），顺时针旋转当前坐标轴。多次调用rotate，旋转的角度会叠加 |
| [CanvasContext.restore](0113-jsapi-canvas-context-restore.md) | 恢复之前保存的绘图上下文 |
| [CanvasContext.save](0114-jsapi-canvas-context-save.md) | 保存当前的绘图上下文 |
| [CanvasContext.scale](0115-jsapi-canvas-context-scale.md) | 调用scale方法后，之后创建的路径其横纵坐标会被缩放。多次调用scale，倍数会相乘 |
| [CanvasContext.stroke](0116-jsapi-canvas-context-stroke.md) | 画出当前路径的边框 |
| [CanvasContext.strokeRect](0117-jsapi-canvas-context-stroke-rect.md) | 画一个非填充矩形 |
| [CanvasContext.setFillStyle](0118-jsapi-canvas-context-set-fill-style.md) | 设置填充色 |
| [CanvasContext.setFontSize](0119-jsapi-canvas-context-set-font-size.md) | 设置字体大小 |
| [CanvasContext.setShadow](0120-jsapi-canvas-context-set-shadow.md) | 设置阴影样式 |
| [CanvasContext.setLineCap](0121-jsapi-canvas-context-set-line-cap.md) | 设置线条的端点样式 |
| [CanvasContext.setLineJoin](0122-jsapi-canvas-context-set-line-join.md) | 设置线条的交点样式 |
| [CanvasContext.setTextAlign](0123-jsapi-canvas-context-set-text-align.md) | 设置文本的对齐方式 |
| [CanvasContext.setMiterLimit](0124-jsapi-canvas-context-set-miter-limit.md) | 设置最大斜接长度 |
| [CanvasContext.setLineWidth](0125-jsapi-canvas-context-set-line-width.md) | 设置线条的宽度 |
| [CanvasContext.setStrokeStyle](0126-jsapi-canvas-context-set-stroke-style.md) | 设置边框颜色 |
| [CanvasContext.setGlobalAlpha](0127-jsapi-canvas-context-set-global-alpha.md) | 设置全局画笔透明度 |
| [CanvasContext.setTextBaseline](0128-jsapi-canvas-context-set-text-baseline.md) | 设置当前文本基线的属性 |
| [CanvasContext.translate](0129-jsapi-canvas-context-translate.md) | 对当前坐标系的原点(0, 0)进行变换，默认的坐标系原点为页面左上角 |
| [CanvasContext.toTempFilePath](0130-jsapi-canvas-context-to-temp-file-path.md) | 画布内容导出成图片 |
| **字体** | [loadFontFace](0131-jsapi-load-font-face.md) | 动态的加载网络字体 |
| **地图** | [chooseDistrict](0132-jsapi-choose-district.md) | 选择地区 |
| [createMapContext](0133-jsapi-create-map-context.md) | 创建并返回一个地图上下文对象 |
| [MapContext.clearRoute](0134-jsapi-map-context-clear-route.md) | 清除地图上的步行导航路线 |
| [MapContext.changeMarkers](0135-jsapi-map-context-change-markers.md) | 用于添加、删除、更新指定的标记 |
| [MapContext.calculateDistance](0136-jsapi-map-context-calculate-distance.md) | 提供地图路径计算能力，用于计算途径地图上多个点的总路线距离 |
| [MapContext.getRegion](0137-jsapi-map-context-get-region.md) | 获取地图东北角、西南角的经纬度，从而获取地图整体的视野范围 |
| [MapContext.gestureEnable](0138-jsapi-map-context-gesture-enable.md) | 设置所有手势是否可用 |
| [MapContext.getMapProperties](0139-jsapi-map-context-get-map-properties.md) | 获取地图的属性信息 |
| [MapContext.getCenterLocation](0140-jsapi-map-context-get-center-location.md) | 获取当前地图中心位置 |
| [MapContext.moveToLocation](0141-jsapi-map-context-move-to-location.md) | 将视野移动到定位点并恢复到默认缩放级别 |
| [MapContext.showRoute](0142-jsapi-map-context-show-route.md) | 规划默认步行路线，只能显示一条 |
| [MapContext.showsScale](0143-jsapi-map-context-shows-scale.md) | 设置比例尺控件是否可见 |
| [MapContext.showsCompass](0144-jsapi-map-context-shows-compass.md) | 设置指南针是否可见 |
| [MapContext.smoothMoveMarker](0145-jsapi-map-context-smooth-move-marker.md) | 指定标记（marker）进行动画 |
| [MapContext.smoothMovePolyline](0146-jsapi-map-context-smooth-move-polyline.md) | 用于轨迹动画 |
| [MapContext.translateMarker](0147-jsapi-map-context-translate-marker.md) | 用于平移点标记 |
| [MapContext.updateComponents](0148-jsapi-map-context-update-components.md) | 用于增量更新地图 |
| **滚动** | [pageScrollTo](0149-jsapi-page-scroll-to.md) | 滚动到页面的目标位置 |
| **交互反馈** | [alert](0150-jsapi-alert.md) | 显示警告框 |
| [confirm](0152-jsapi-confirm.md) | 显示确认框 |
| [hideToast](0151-jsapi-hide-toast.md) | 隐藏弱提示 |
| [hideLoading](0153-jsapi-hide-loading.md) | 隐藏加载提示 |
| [prompt](0154-jsapi-prompt.md) | 弹出输出入对话框 |
| [showModal](0155-jsapi-show-modal.md) | 增强版modal弹浮层 |
| [showToast](0156-jsapi-show-toast.md) | 显示一个弱提示 |
| [showLoading](0157-jsapi-show-loading.md) | 显示加载提示 |
| [showActionSheet](0158-jsapi-show-action-sheet.md) | 显示操作菜单 |
| **下拉刷新** | [disablePullDownRefresh](0159-jsapi-disable-pull-down-refresh.md) | 禁用下拉刷新 |
| [enablePullDownRefresh](0160-jsapi-enable-pull-down-refresh.md) | 启用下拉刷新 |
| [onPullDownRefresh](0161-jsapi-on-pull-down-refresh.md) | 监听下拉刷新 |
| [stopPullDownRefresh](0162-jsapi-stop-pull-down-refresh.md) | 停止当前页面的下拉刷新 |
| **键盘输入** | [hideKeyboard](0163-jsapi-hide-keyboard.md) | 隐藏键盘 |
| [onKeyboardHide](0164-jsapi-on-keyboard-hide.md) | 监听键盘收起 |
| [onKeyboardShow](0165-jsapi-on-keyboard-show.md) | 监听键盘弹起事件 |
| **节点查询** | [createIntersectionObserver](0166-jsapi-create-intersection-observer.md) | 创建并返回一个IntersectionObserver对象实例 |
| [IntersectionObserver.disconnect](0167-jsapi-intersection-observer-disconnect.md) | 停止监听 |
| [IntersectionObserver.observe](0168-jsapi-intersection-observer-observe.md) | 指定目标节点并开始监听相交状态变化情况 |
| [IntersectionObserver.relativeTo](0169-jsapi-intersection-observer-relative-to.md) | 使用选择器指定一个节点，作为参照区域之一 |
| [IntersectionObserver.relativeToViewport](0170-jsapi-intersection-observer-relative-to-viewport.md) | 指定页面显示区域作为参照区域之一 |
| [createSelectorQuery](0171-jsapi-create-selector-query.md) | 创建一个节点查询对象SelectorQuery |
| [SelectorQuery.boundingClientRect](0172-jsapi-selector-query-bounding-client-rect.md) | 将当前选择节点的位置信息放入查询结果， 返回对象包含 width/height/left/top/bottom/right |
| [SelectorQuery.exec](0173-jsapi-selector-query-exec.md) | 查询结果放入 callback 回调中 |
| [SelectorQuery.select](0174-jsapi-selector-query-select.md) | 选择当前第一个匹配选择器的节点，选择器支持 id 选择器以及 class 选择器 |
| [SelectorQuery.selectAll](0175-jsapi-selector-query-select-all.md) | 选择所有匹配选择器的节点，选择器支持 id 选择器以及 class 选择器 |
| [SelectorQuery.scrollOffset](0176-jsapi-selector-query-scroll-offset.md) | 将当前选择节点的滚动信息放入查询结果，返回对象包含 scrollTop/scrollLeft |
| [SelectorQuery.selectViewport](0177-jsapi-selector-query-select-viewport.md) | 选择窗口对象 |
| **暗黑模式** | [getColorSchemeSync](0178-jsapi-get-color-scheme-sync.md) | 获取钉钉当前显示模式。返回当前系统的显示模式"light" 或 "dark" |
| **选择日期** | [chooseDateTime](0179-jsapi-choose-date-time.md) | 选择日期和时间 |
| [chooseOneDayInCalendar](0180-jsapi-choose-one-day-in-calendar.md) | 月历组件，选择某天 |
| [chooseHalfDayInCalendar](0181-jsapi-choose-half-day-in-calendar.md) | 月历组件，选择半天 |
| [datePicker](0182-jsapi-date-picker.md) | 打开日期选择列表 |
| [dateRangePicker](0183-jsapi-date-range-picker.md) | 月历组件，选择日期区间 |
| [timePicker](0184-jsapi-time-picker.md) | 时间选择器 |
| 选项选择器 | [multiSelect](0185-jsapi-multi-select.md) | 多选组件 |
| [singleSelect](0186-jsapi-single-select.md) | 单选组件 |

### **跳转**

| **API名称** | **API说明** |
| --- | --- |
| [isInTabWindow](0187-jsapi-is-in-tab-window.md) | 判断当前页面是否为弹窗页面 |
| [navigateToPage](0188-jsapi-navigate-to-page.md) | 跳转到另一个钉钉H5微应用 |
| [navigateBackPage](0189-jsapi-navigate-back-page.md) | 返回上一个应用 |
| [navigateToMiniProgram](0190-jsapi-navigate-to-mini-program.md) | 跳转到其他钉钉小程序 |
| [navigateBackMiniProgram](0191-jsapi-navigate-back-mini-program.md) | 返回到上一个钉钉小程序 |
| [openLink](0192-jsapi-open-link.md) | 打开目标页面 |
| [openMicroApp](0193-jsapi-open-micro-app.md) | 打开应用 |
| [openPageInMicroApp](0194-jsapi-open-page-in-micro-app.md) | 打开应用内页面 |
| [openPageInModalForPC](0195-jsapi-open-page-in-modal-for-pc.md) | 打开模态框 |
| [openPageInSlidePanelForPC](0196-jsapi-open-page-in-slide-panel-for-pc.md) | 打开侧边面板 |
| [openPageInWorkBenchForPC](0197-jsapi-open-page-in-work-bench-for-pc.md) | PC端打开新弹窗页面 |

### **分享**

| **API名称** | **API说明** |
| --- | --- |
| [onShareAppMessage](0198-jsapi-on-share-app-message.md) | 自定义该页面的分享内容 |
| [share](0199-jsapi-share.md) | 实现分享功能 |
| [showSharePanel](0200-jsapi-show-share-panel.md) | 唤起H5或小程序分享面板的API |

### **更新管理**

| **API名称** | **API说明** |
| --- | --- |
| [getUpdateManager](0201-jsapi-get-update-manager.md) | 用来管理小程序更新 |
| [UpdateManager.applyUpdate](0202-jsapi-update-manager-apply-update.md) | 强制小程序重启并使用新版本 |
| [UpdateManager.onUpdateFailed](0203-jsapi-update-manager-on-update-failed.md) | 监听小程序更新失败事件 |
| [UpdateManager.onUpdateReady](0204-jsapi-update-manager-on-update-ready.md) | 监听小程序有版本更新事件 |
| [UpdateManager.onCheckForUpdate](0205-jsapi-update-manager-on-check-for-update.md) | 监听向钉钉后台请求检查更新结果事件 |

## **多媒体**

| **类目** | **API名称** | **API说明** |
| --- | --- | --- |
| **图片** | [chooseImage](0206-jsapi-choose-image.md) | 拍照或从本地相册选择图片 |
| [compressImage](0207-jsapi-compress-image.md) | 压缩图片 |
| [editPicture](0208-jsapi-edit-picture.md) | 编辑图片 |
| [getImageInfo](0209-jsapi-get-image-info.md) | 获取图片信息 |
| [previewImage](0210-jsapi-preview-image.md) | 预览图片 |
| [saveImage](0211-jsapi-save-image.md) | 保存在线、本地临时或者永久地址图片到手机相册 |
| [saveImageToPhotosAlbum](0212-jsapi-save-image-to-photos-album.md) | 保存图片到系统相册 |
| [chooseMedia](0213-jsapi-choose-media.md) | 拍摄或从手机相册中选择图片或视频 |
| **录音** | [downloadAudio](0214-jsapi-download-audio.md) | 下载音频 |
| [onRecordEnd](0215-jsapi-on-record-end.md) | 监听录音自动停止 |
| [onPlayAudioEnd](0216-jsapi-on-play-audio-end.md) | 监听播放自动停止 |
| [playAudio](0217-jsapi-play-audio.md) | 播放语音 |
| [pauseAudio](0218-jsapi-pause-audio.md) | 暂停播放语音 |
| [resumeAudio](0219-jsapi-resume-audio.md) | 恢复暂停播放的语音 |
| [stopRecord](0220-jsapi-stop-record.md) | 停止录音 |
| [startRecord](0221-jsapi-start-record.md) | 开始录音 |
| [stopAudio](0222-jsapi-stop-audio.md) | 停止播放音频 |
| [translateVoice](0223-jsapi-translate-voice.md) | 语音转文字 |
| [getRecorderManager](0224-jsapi-get-recorder-manager.md) | 获取当前小程序全局唯一的录音管理器 |
| [RecorderManager.onstart](0225-jsapi-recorder-manager-on-start.md) | 录音开始时的回调 |
| [RecorderManager.onstop](0226-jsapi-recorder-manager-on-stop.md) | 录音停止时的回调 |
| [RecorderManager.onerror](0227-jsapi-recorder-manager-on-error.md) | 录音管理监听错误 |
| [RecorderManager.onpause](0228-jsapi-recorder-manager-on-pause.md) | 录音管理监听暂停 |
| [RecorderManager.onresume](0229-jsapi-recorder-manager-on-resume.md) | 录音管理监听继续 |
| [RecorderManager.onframerecorded](0230-jsapi-recorder-manager-on-frame-recorded.md) | 录音管理监听已录制完制定帧大小的文件 |
| [RecorderManager.pause](0231-jsapi-recorder-manager-pause.md) | 录音管理暂停录音 |
| [RecorderManager.resume](0232-jsapi-recorder-manager-resume.md) | 录音管理继续录音 |
| [RecorderManager.stop](0233-jsapi-recorder-manager-stop.md) | 停止录音 |
| [RecorderManager.start](0234-jsapi-recorder-manager-start.md) | 开始录音 |
| **音频** | [getBackgroundAudioManager](0246-jsapi-get-background-audio-manager.md) | 获取当前小程序全局唯一的背景音频管理 |
| [BackgroundAudioManager.onPlay](0247-jsapi-background-audio-manager-on-play.md) | 监听背景音频播放事件 |
| [BackgroundAudioManager.onStop](0248-jsapi-background-audio-manager-on-stop.md) | 监听背景音频停止事件 |
| [BackgroundAudioManager.onPause](0249-jsapi-background-audio-manager-on-pause.md) | 监听背景音频暂停事件 |
| [BackgroundAudioManager.onEnded](0250-jsapi-background-audio-manager-on-ended.md) | 监听背景音频结束事件 |
| [BackgroundAudioManager.onPrev](0251-jsapi-background-audio-manager-on-prev.md) | 监听用户在系统音乐播放面板点击上一曲事件 |
| [BackgroundAudioManager.onNext](0252-jsapi-background-audio-manager-on-next.md) | 监听用户在系统音乐播放面板点击下一曲事件 |
| [BackgroundAudioManager.onCanplay](0253-jsapi-background-audio-manager-on-canplay.md) | 监听背景音频进入可以播放事件 |
| [BackgroundAudioManager.onSeeked](0254-jsapi-background-audio-manager-on-seeked.md) | 监听背景音频完成播放进度跳转操作事件 |
| [BackgroundAudioManager.onSeeking](0255-jsapi-background-audio-manager-on-seeking.md) | 监听背景音频开始播放进度跳转事件 |
| [BackgroundAudioManager.onWaiting](0256-jsapi-background-audio-manager-on-waiting.md) | 监听音频加载中事件。 |
| [BackgroundAudioManager.onTimeUpdate](0257-jsapi-background-audio-manager-on-time-update.md) | 监听背景音频播放进度更新事件 |
| [BackgroundAudioManager.play](0258-jsapi-background-audio-manager-play.md) | 播放背景音乐 |
| [BackgroundAudioManager.pause](0259-jsapi-background-audio-manager-pause.md) | 暂停背景音频 |
| [BackgroundAudioManager.stop](0260-jsapi-background-audio-manager-stop.md) | 停止播放背景音乐 |
| [BackgroundAudioManager.seek](0261-jsapi-background-audio-manager-seek.md) | 跳转到指定位置position |
| [onAudioInterruptionEnd](0262-jsapi-on-audio-interruption-end.md) | 监听音频被中断的结束事件。 |
| [onAudioInterruptionBegin](0263-jsapi-on-audio-interruption-begin.md) | 监听音频因为系统占用而被中断的开始事件 |
| [saveVideoToPhotosAlbum](0264-jsapi-save-video-to-photos-album.md) | 保存视频到系统相册 |
| **视频** | [chooseVideo](0235-jsapi-choose-video.md) | 拍摄视频或从手机相册中选视频 |
| [createVideoContext](0236-jsapi-create-video-context.md) | 创建并返回一个 video上下文对象videoContext |
| [VideoContext.exitFullScreen](0237-jsapi-video-context-exit-full-screen.md) | 控制相应video组件的全屏退出 |
| [VideoContext.mute](0238-jsapi-video-context-mute.md) | 切换静音状态 |
| [VideoContext.play](0239-jsapi-video-context-play.md) | 控制相应video组件的播放 |
| [VideoContext.pause](0240-jsapi-video-context-pause.md) | 控制相应video组件的暂停 |
| [VideoContext.playbackRate](0241-jsapi-video-context-playback-rate.md) | 设置倍速播放 |
| [VideoContext.requestFullScreen](0242-jsapi-video-context-request-full-screen.md) | 控制相应video组件的全屏进入 |
| [VideoContext.stop](0243-jsapi-video-context-stop.md) | 控制相应video组件的终止 |
| [VideoContext.seek](0244-jsapi-video-context-seek.md) | 控制相应video组件的定位 |
| [VideoContext.snapshot](0245-jsapi-video-context-snapshot.md) | 控制相应video组件的截图 |

## **DING**

| **API名称** | **API说明** |
| --- | --- |
| [createDing](0265-jsapi-create-ding.md) | 发起DING |
| [createDingForPC](0266-jsapi-create-ding-for-pc.md) | 发起PC端发钉 |

## **通讯录**

| **API名称** | **API说明** |
| --- | --- |
| [complexChoose](0267-jsapi-complex-choose.md) | 选择人和部门 |
| [chooseStaffForPC](0268-jsapi-choose-staff-for-pc.md) | PC端选择企业内部的人 |
| [choosePhonebook](0269-jsapi-choose-phonebook.md) | 选取用户手机联系人 |
| [chooseDepartments](0270-jsapi-choose-departments.md) | 选择部门 |
| [chooseUserFromList](0271-jsapi-choose-user-from-list.md) | 选取单个自定义联系人 |
| [chooseExternalUsers](0272-jsapi-choose-external-users.md) | 选择外部联系人 |
| [editExternalUser](0273-jsapi-edit-external-user.md) | 编辑外部联系人 |

## **音频会议**

| **API名称** | **API说明** |
| --- | --- |
| [makeVideoConfCall](0308-jsapi-make-video-conf-call.md) | 发起视频会议 |

## **办公电话**

| **API名称** | **API说明** |
| --- | --- |
| [callUsers](0311-jsapi-call-users.md) | 拨打钉钉电话 |
| [checkBizCall](0312-jsapi-check-biz-call.md) | 检查某企业办公电话开通状态 |
| [getCloudCallInfo](0313-jsapi-get-cloud-call-info.md) | 查询企业是否已开办公电话 |
| [getCloudCallList](0314-jsapi-get-cloud-call-list.md) | 查询话单列表 |
| [makeCloudCall](0315-jsapi-make-cloud-call.md) | 发起办公电话呼叫 |
| [quickCallList](0316-jsapi-quick-call-list.md) | 拨打单人电话选项 |
| [showCallMenu](0317-jsapi-show-call-menu.md) | 唤起拨打电话菜单 |

## **会话管理**

| **API名称** | **API说明** |
| --- | --- |
| [chooseChat](0318-jsapi-choose-chat.md) | 选择会话 |
| [openChatByChatId](0319-jsapi-open-chat-by-chat-id.md) | 打开对应会话 |
| [openChatByUserId](0320-jsapi-open-chat-by-user-id.md) | 打开与某个用户的聊天页面 |
| [openChatByConversationId](0321-jsapi-open-chat-by-conversation-id.md) | 跳转到对应会话 |

## **位置**

| **API名称** | **API说明** |
| --- | --- |
| [getLocation](0322-jsapi-get-location.md) | 获取用户当前的地理位置信息 |
| [getLocatingStatus](0323-jsapi-get-locating-status.md) | 批量获取连续定位状态 |
| [locateInMap](0324-jsapi-locate-in-map.md) | 地图定位 |
| [openLocation](0325-jsapi-open-location.md) | 使用内置地图查看位置 |
| [searchMap](0326-jsapi-search-map.md) | 唤起地图页面 |
| [stopLocating](0327-jsapi-stop-locating.md) | 停止连续定位 |
| [startLocating](0328-jsapi-start-locating.md) | 连续获取当前地理位置信息（持续定位） |

## **文件储存**

### **钉盘**

| **API名称** | **API说明** |
| --- | --- |
| [chooseDingTalkDir](0329-jsapi-choose-ding-talk-dir.md) | 唤起钉盘选择器 |
| [previewFileInDingTalk](0330-jsapi-preview-file-in-ding-talk.md) | 预览钉盘文件 |
| [previewImagesInDingTalkBatch](0331-jsapi-preview-images-in-ding-talk-batch.md) | 批量预览钉盘图片 |
| [saveFileToDingTalk](0332-jsapi-save-file-to-ding-talk.md) | 转存文件到钉盘 |
| [uploadAttachmentToDingTalk](0333-jsapi-upload-attachment-to-ding-talk.md) | 上传附件到钉盘，或从钉盘选择文件 |

### **文件**

| **API名称** | **API说明** |
| --- | --- |
| [isLocalFileExist](0334-jsapi-is-local-file-exist.md) | 批量检测本地文件是否存在 |
| [openLocalFile](0335-jsapi-open-local-file.md) | 打开本地文件 |
| [getFileSystemManager](0338-jsapi-get-file-system-manager.md) | 获取FileSystemManager文件管理器 |
| [FileSystemManager.access](0339-jsapi-file-system-manager-access.md) | 判断文件或者目录是否存在 |
| [FileSystemManager.appendFile](0340-jsapi-file-system-manager-append-file.md) | 向本地用户文件末尾添加内容 |
| [FileSystemManager.copyFile](0341-jsapi-file-system-manager-copy-file.md) | 复制文件保存到本地用户目录 |
| [FileSystemManager.getFileInfo](0342-jsapi-file-system-manager-get-file-info.md) | 获取本地临时文件、本地缓存文件和本地用户文件的信息 |
| [FileSystemManager.getSavedFileList](0343-jsapi-file-system-manager-get-saved-file-list.md) | 获取本地缓存文件列表 |
| [FileSystemManager.mkdir](0344-jsapi-file-system-manager-mkdir.md) | 创建本地用户目录 |
| [FileSystemManager.rmdir](0345-jsapi-file-system-manager-rmdir.md) | 删除本地用户文件目录 |
| [FileSystemManager.rename](0346-jsapi-file-system-manager-rename.md) | 重命名本地用户文件或目录的名称并且可以移动到新目录下 |
| [FileSystemManager.readdir](0347-jsapi-file-system-manager-readdir.md) | 获取本地用户文件列表 |
| [FileSystemManager.readFile](0348-jsapi-file-system-manager-read-file.md) | 读取本地用户文件的内容 |
| [FileSystemManager.removeSavedFile](0349-jsapi-file-system-manager-remove-saved-file.md) | 删除本地缓存文件 |
| [FileSystemManager.stat](0350-jsapi-file-system-manager-stat.md) | 获取文件或目录的status对象 |
| [FileSystemManager.saveFile](0351-jsapi-file-system-manager-save-file.md) | 本地临时文件保存为本地缓存文件或本地用户文件 |
| [FileSystemManager.unzip](0352-jsapi-file-system-manager-unzip.md) | 解压本地用户文件 |
| [FileSystemManager.unlink](0353-jsapi-file-system-manager-unlink.md) | 删除本地用户文件 |
| [FileSystemManager.writeFile](0354-jsapi-file-system-manager-write-file.md) | 向本地用户目录内写入文件 |

## **移动支付**

| **API名称** | **API说明** |
| --- | --- |
| [pay](0355-jsapi-pay.md) | 完成支付 |

## **设备能力**

| **类目** | **API名称** | **API说明** |
| --- | --- | --- |
| **UUID** | [getDeviceUUID](0356-jsapi-get-device-uuid.md) | 获取uuid |
| **系统信息** | [checkAuth](0357-jsapi-check-auth.md) | 检查手机权限授权状态 |
| [getSystemInfo](0358-jsapi-get-system-info.md) | 获取手机系统信息 |
| [getSystemSettings](0359-jsapi-get-system-settings.md) | 打开系统设置 |
| [getSystemInfoSync](0360-jsapi-get-system-info-sync.md) | 获取手机系统信息的同步接口 |
| [isScreenReaderEnabled](0361-jsapi-is-screen-reader-enabled.md) | 判断是否开启无障碍模式 |
| [rsa](0362-jsapi-rsa.md) | 实现rsa加解密 |
| [showAuthGuide](0363-jsapi-show-auth-guide.md) | 授权引导 |
| **网络状态** | [getNetworkType](0364-jsapi-get-network-type.md) | 获取当前网络状态 |
| [getWifiHotspotStatus](0365-jsapi-get-wifi-hotspot-status.md) | 获取热点接入信息 |
| **Wi-Fi** | [connectWifi](0366-jsapi-connect-wifi.md) | 连接 Wi-Fi |
| [getWifiList](0367-jsapi-get-wifi-list.md) | 获取 Wi-Fi 列表 |
| [getWifiStatus](0368-jsapi-get-wifi-status.md) | 获取wifi状态 |
| [getConnectedWifi](0369-jsapi-get-connected-wifi.md) | 获取已连接 Wi-Fi 信息 |
| [onGetWifiList](0370-jsapi-on-get-wifi-list.md) | 监听获取到 Wi-Fi 列表事件 |
| [offGetWifiList](0371-jsapi-off-get-wifi-list.md) | 停止监听已获取 Wi-Fi 列表数据事件 |
| [onWifiConnected](0372-jsapi-on-wifi-connected.md) | 监听连接上 Wi-Fi 事件 |
| [offWifiConnected](0373-jsapi-off-wifi-connected.md) | 停止监听连接 Wi-Fi 事件 |
| [registerSSID](0374-jsapi-register-ssid.md) | 信任该 SSID(iOS) |
| [stopWifi](0375-jsapi-stop-wifi.md) | 关闭 Wi-Fi 模块 |
| [startWifi](0376-jsapi-start-wifi.md) | 初始化 Wi-Fi 模块 |
| [unregisterSSID](0378-jsapi-unregister-ssid.md) | 不再信任该 SSID(iOS) |
| [setWifiList](0377-jsapi-set-wifi-list.md) | 设置入参中 wifiList 的 AP 相关信息 |
| **剪贴板** | [getClipboard](0379-jsapi-get-clipboard.md) | 获取系统剪贴板的内容 |
| [setClipboard](0380-jsapi-set-clipboard.md) | 设置剪切板数据 |
| **振动** | [vibrate](0381-jsapi-vibrate.md) | 使用振动功能 |
| [vibrateLong](0382-jsapi-vibrate-long.md) | 使用长振动功能 |
| [vibrateShort](0383-jsapi-vibrate-short.md) | 使用短振动功能 |
| **低功耗蓝牙** | [connectBLEDevice](0384-jsapi-connect-bledevice.md) | 连接低功耗蓝牙设备 |
| [disconnectBLEDevice](0385-jsapi-disconnect-bledevice.md) | 断开与低功耗蓝牙设备的连接 |
| [getBLEDeviceServices](0386-jsapi-get-ble-device-services.md) | 获取蓝牙设备所有服务 |
| [getBLEDeviceCharacteristics](0387-jsapi-get-ble-device-characteristics.md) | 获取蓝牙设备所有特征值 |
| [notifyBLECharacteristicValueChange](0388-jsapi-notify-ble-haracteristic-value-change.md) | 启用低功耗蓝牙设备特征值变化时的notify功能 |
| [onBLEConnectionStateChanged](0389-jsapi-on-ble-connection-state-changed.md) | 监听低功耗蓝牙连接的错误事件，包括设备丢失，连接异常断开等 |
| [offBLEConnectionStateChanged](0390-jsapi-off-ble-connection-state-changed.md) | 移除低功耗蓝牙连接状态变化事件的监听 |
| [onBLECharacteristicValueChange](0391-jsapi-on-ble-characteristic-value-change.md) | 监听低功耗蓝牙设备的特征值变化的事件 |
| [offBLECharacteristicValueChange](0392-jsapi-off-ble-characteristic-value-change.md) | 移除低功耗蓝牙设备的特征值变化事件的监听 |
| [readBLECharacteristicValue](0393-jsapi-read-ble-characteristic-value.md) | 读取低功耗蓝牙设备特征值中的数据 |
| [writeBLECharacteristicValue](0394-jsapi-write-ble-characteristic-value.md) | 向低功耗蓝牙设备特征值中写入数据 |
| **传统蓝牙** | [closeBluetoothAdapter](0395-jsapi-close-bluetooth-adapter.md) | 关闭本机蓝牙模块 |
| [getBluetoothDevices](0396-jsapi-get-bluetooth-devices.md) | 获取所有已发现的蓝牙设备 |
| [getBluetoothAdapterState](0397-jsapi-get-bluetooth-adapter-state.md) | 获取本机蓝牙模块状态 |
| [getConnectedBluetoothDevices](0398-jsapi-get-connected-bluetooth-devices.md) | 获取处于已连接状态的设备 |
| [onBluetoothDeviceFound](0399-jsapi-on-bluetooth-device-found.md) | 搜索到新的蓝牙设备时触发此事件 |
| [offBluetoothDeviceFound](0400-jsapi-off-bluetooth-device-found.md) | 移除寻找到新的蓝牙设备事件的监听 |
| [onBluetoothAdapterStateChange](0402-jsapi-on-bluetooth-adapter-state-change.md) | 监听本机蓝牙状态变化的事件 |
| [offBluetoothAdapterStateChange](0403-jsapi-off-bluetooth-adapter-state-change.md) | 停止监听本机蓝牙状态变化的事件 |
| [openBluetoothAdapter](0401-jsapi-open-bluetooth-adapter.md) | 初始化小程序蓝牙模块 |
| [stopBluetoothDevicesDiscovery](0404-jsapi-stop-bluetooth-devices-discovery.md) | 停止搜寻附近的蓝牙外围设备 |
| [startBluetoothDevicesDiscovery](0405-jsapi-start-bluetooth-devices-discovery.md) | 开始搜寻附近的蓝牙外围设备 |
| **扫码** | [scanCard](0407-jsapi-scan-card.md) | 扫名片 |
| [scan](0406-jsapi-scan.md) | 扫一扫功能 |
| **NFC** | [readNFC](0408-jsapi-read-nfc.md) | 读取NFC芯片内容 |
| [writeNFC](0409-jsapi-write-nfc.md) | 实现NFC数据写入 |
| **摇一摇** | [clearShake](0410-jsapi-clear-shake.md) | 停止摇一摇 |
| [watchShake](0411-jsapi-watch-shake.md) | 启动摇一摇 |
| **屏幕亮度** | [getScreenBrightness](0412-jsapi-get-screen-brightness.md) | 获取屏幕亮度 |
| [setScreenBrightness](0413-jsapi-set-screen-brightness.md) | 设置屏幕亮度 |
| [setKeepScreenOn](0414-jsapi-set-keep-screen-on.md) | 设置屏幕常亮 |
| **拨打电话** | [addPhoneContact](0416-jsapi-add-phone-contact.md) | 添加手机联系人 |
| **设备电量** | [getBatteryInfo](0415-jsapi-get-battery-info.md) | 获取设备电量 |
| **设备方向** | [rotateScreenView](0418-jsapi-rotate-screen-view.md) | 旋转屏幕 |
| [resetScreenView](0417-jsapi-reset-screen-view.md) | 重置旋转屏幕 |
| **内存不足处理** | [removeCachedAPIResponse](0419-jsapi-remove-cached-a-p-i-response.md) | 删除已缓存的JSAPI返回值 |
| [getCachedAPIResponse](0420-jsapi-get-cached-a-p-i-response.md) | 获取已缓存的JSAPI返回值 |
| [enableAPIResponseCache](0421-jsapi-enable-a-p-i-response-cache.md) | 开启JSAPI返回值缓存 |
| [getPageTerminateInfo](0422-jsapi-get-page-terminate-info.md) | 获取WebView崩溃信息 |

## **专属开放**

| **API名称** | **API说明** |
| --- | --- |
| [exclusiveLiveCheck](0423-jsapi-exclusive-live-check.md) | 专属实人认证 |
| [getUserExclusiveInfo](0424-jsapi-get-user-exclusive-info.md) | 获取钉钉客户端是否为专属钉钉 |

## **DingTalk A1**

| **API名称** | **API说明** |
| --- | --- |
| [startDingerRecord](0425-jsapi-start-dinger-record.md) | DingTalk A1 发起录音 |
| [stopDingerRecord](0426-jsapi-stop-dinger-record.md) | DingTalk A1 停止录音 |
| [getDingerDeviceStatus](0427-jsapi-get-dinger-device-status.md) | 查询 DingTalk A1 设备状态 |
