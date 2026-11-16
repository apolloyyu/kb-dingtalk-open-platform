---
title: "JSAPI总览"
source_url: "https://open.dingtalk.com/document/development/jsapi-overview-1"
namespace: "development"
slug: "jsapi-overview-1"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "历史文档（不推荐） > H5微应用 > JSAPI总览"
doc_id: "CYiXZzNLb5"
updated_at: "2026-09-02 18:13:52"
---

> Source: https://open.dingtalk.com/document/development/jsapi-overview-1
> Path: 应用开发 / 客户端 JSAPI / 历史文档（不推荐） > H5微应用 > JSAPI总览
> Updated: 2026-09-02 18:13:52

# JSAPI总览

钉钉提供的前端JSAPI总览。

**扫码体验**

![微应用JSAPI预览地址](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8902091161/p236462.png)

同时，钉钉提供了前端API调试工具[JSAPI Explorer](https://open-dev.dingtalk.com/apiExplorer#/jsapi?api=biz.util.multiSelect)，供开发者体验提供的前端JSAPI功能。

| 分类 | **JSAPI名称** | **接口说明** | **是否需鉴权** | **系统支持** |  |
| --- | --- | --- | --- | --- | --- |
| **免登** | [runtime.permission.requestAuthCode](0717-obtain-the-micro-application-exemption-authorization-code.md) | 获取微应用免登授权码 | 不需要 | - **Android** - **iOS** - **PC** | |
| [runtime.permission.requestOperateAuthCode](0718-obtain-the-temporary-authorization-code-for-micro-application-feedback-operation.md) | 获取微应用反馈式操作的临时授权码 | 需要 |
| **设备** | [device.base.getPhoneInfo](0725-obtain-basic-mobile-phone-information.md) | 获取手机基础信息 | 不需要 | - **Android** - **iOS** | |
| [device.base.getUUID](0719-get-uuid.md) | 获取uuid | 需要 |
| [device.base.getInterface](0726-queries-the-hotspot-access-information.md) | 获取热点接入信息 | 需要 |
| [device.base.getWifiStatus](0720-get-wifi-status.md) | 获取wifi状态 | 不需要 |
| [device.connection.getNetworkType](0721-queries-the-network-type.md) | 获取网络类型 | 不需要 |
| [device.nfc.nfcRead](0727-read-nfc-chip-content.md) | 读取NFC芯片内容 | 不需要 | - **Android** | |
| [device.nfc.nfcWrite](0722-nfc-data-write.md) | NFC数据写入 | 需要 |
| [biz.util.setScreenKeepOn](0723-the-setting-screen-is-always-on.md) | 设置屏幕常亮 | 不需要 | - **Android** - **iOS** | |
| [runtime.monitor.getLoadTime](0728-obtains-the-h5-container-startup-time.md) | 获取H5容器启动时间 | 不需要 |
| [device.base.openSystemSetting](0724-open-ios-system-settings.md) | 打开iOS系统设置 | 不需要 | - **iOS** | |
| [device.base.openSystemSetting](0729-open-android-system-settings.md) | 打开Android系统设置 | 不需要 | - **Android** | |
| **日期和月历** | [biz.util.datepicker](0730-date-selector.md) | 日期选择器 | 不需要 | - **Android** - **iOS** | |
| [biz.util.timepicker](0731-time-picker.md) | 时间选择器 | 不需要 |
| [biz.util.datetimepicker](0732-date-and-time-selector.md) | 日期及时间选择器 | 不需要 |
| [biz.calendar.chooseDateTime](0735-monthly-calendar-component-select-a-specific-time.md) | 月历组件：选择某时间 | 不需要 |
| [biz.calendar.chooseOneDay](0733-monthly-calendar-component-select-a-certain-day.md) | 月历组件：选择某天 | 不需要 |
| [biz.calendar.chooseHalfDay](0734-monthly-calendar-component-select-a-date-range.md) | 月历组件：选择半天 | 不需要 |
| [biz.calendar.chooseInterval](0736-month-calendar-component-select-date-range.md) | 月历组件：选择日期区间 | 不需要 |
| **通讯录选人** | [biz.contact.complexPicker](0737-select-department-and-person.md) | 选择部门和人 | 需要 | - **Android** - **iOS** - **PC** | |
| [biz.contact.departmentsPicker](0738-select-department-information-h5.md) | 选择部门信息 | 需要 |
| [biz.contact.createGroup](0739-create-enterprise-chat.md) | 创建企业聊天 | 需要 | - **Android** - **iOS** | |
| [biz.contact.chooseMobileContacts](0740-select-phone-address-book.md) | 选取手机通讯录 | 需要 |
| [biz.contact.choose](0741-on-the-pc-select-the-person-in-the-enterprise.md) | PC端选择企业内部的人 | 需要 | - **PC** | |
| **角色** | [biz.contact.rolesPicker](0742-select-a-role-group-or-role.md) | 选择角色组或角色 | 需要 | - **Android** - **iOS** | |
| **业务** | [biz.util.share](0743-share-1.md) | 分享 | 不需要 |
| [biz.util.chosen](0744-drop-down-control.md) | 下拉控件 | 不需要 |
| [biz.clipboardData.setData](0746-copy-to-clipboard.md) | 复制到粘贴板 | 需要 |
| [biz.microApp.openApp](0745-open-an-application.md) | 打开应用 | 不需要 |
| **导航栏** | [拼接dd\_nav\_bgcolor参数](0750-set-the-navigation-bar-color.md) | 设置导航栏颜色 | 不需要 |
| [拼接dd\_orientation参数](0753-microapplication-page-supports-horizontal-dashboard-h5.md) | 微应用页面支持横屏 | 不需要 |
| [biz.navigation.setTitle](0751-set-the-navigation-bar-title.md) | 设置导航栏标题 | 不需要 | - **Android** - **iOS** - **PC** | |
| [biz.navigation.setIcon](0754-title-bar-add-question-mark-icon.md) | 标题栏添加问号图标 | 不需要 | - **Android** - **iOS** | |
| [biz.navigation.setLeft](0755-set-left-navigation-button-text.md) | 设置左侧导航按钮文本 | 不需要 | - **iOS** - **PC** | |
| [biz.navigation.close](0749-close-the-current-page.md) | 关闭当前页面 | 不需要 | - **Android** - **iOS** | |
| [biz.navigation.quit](0747-close-page.md) | 关闭页面 | 不需要 | - **PC** | |
| [biz.navigation.goBack](0752-return-to-previous-page.md) | 返回上一级页面 | 不需要 | - **Android** - **iOS** | |
| [biz.navigation.replace](0748-replace-page.md) | 替换页面 | 不需要 |
| **弹窗** | [device.notification.alert](0756-alert.md) | 显示警告框，可以设置警告框的标题、内容、按钮文字等 | 不需要 | - **Android** - **iOS** - **PC** | |
| [device.notification.confirm](0759-confirm.md) | 显示确认框，可以配置确认框的标题、内容、按钮的文字等 | 不需要 |
| [device.notification.prompt](0758-prompt.md) | 显示可提示用户进行输入的对话框，可以配置输入框的标题、内容、提示、按钮的文字等 | 不需要 |
| [device.notification.vibrate](0763-mobile-phone-vibration.md) | 手机震动 | 不需要 | - **Android** - **iOS** | |
| [device.notification.showPreloader](0760-show-load.md) | 显示加载 | 不需要 |
| [device.notification.hidePreloader](0761-hide-loading.md) | 隐藏加载 | 不需要 |
| [device.notification.toast](0757-toast.md) | 实现toast弹窗 | 不需要 | - **Android** - **iOS** - **PC** | |
| [device.notification.actionSheet](0764-actionsheet.md) | 实现actionsheet弹窗 | 不需要 |
| [device.notification.modal](0767-modal-pop-up-layer.md) | 实现modal弹浮层 | 不需要 | - **Android** - **iOS** | |
| [device.notification.extendModal](0765-extendmodal-1.md) | 增强版modal弹浮层，支持自定义每一个Cell的内容 | 不需要 |
| [biz.util.multiSelect](0762-multiple-select-components.md) | 多选组件 | 不需要 |
| **会话** | [biz.chat.chooseConversationByCorpId](0768-select-session-based-on-corpid.md) | 根据corpid选择会话 | 需要 | - **Android** - **iOS** - **PC** | |
| [biz.chat.toConversation](0769-redirects-to-a-specific-session-based-on-the-chatid-h5.md) | 根据chatId跳转到对应会话 | 需要 | - **Android** - **iOS** | |
| [biz.chat.toConversationByOpenConversationId](0771-redirects-to-the-specified-session-based-on-the-openconversationid.md) | 根据openConversationId跳转到对应会话 | 需要 | - **Android** - **iOS** - **PC** | |
| [biz.chat.openSingleChat](0770-open-a-one-on-one-chat-session-with-a-user.md) | 打开与某个用户的单聊会话 | 需要 | - **Android** - **iOS** | |
| **电话** | [biz.telephone.call](0773-call-dingtalk-h5.md) | 拨打钉钉电话 | 需要 |
| [biz.telephone.showCallMenu](0772-universal-phone-call-h5.md) | 通用电话拨打 | 需要 |
| [biz.telephone.checkBizCall](0775-check-the-status-of-office-telephones-of-an-enterprise-h5.md) | 检查某企业的办公电话开通状态 | 需要 |
| [biz.telephone.quickCallList](0774-make-a-single-call-option-customizable-h5.md) | 拨打单人电话选项（可定制） | 需要 | - **Android** - **iOS** - **PC** | |
| **DING** | [biz.ding.create](0777-ding-2-0-hair-pin.md) | 实现DING 2.0 发钉 | 需要 |
| [biz.ding.post](0776-ding-1-0-hair-pin.md) | DING 1.0 发钉 | 需要 | - **PC** | |
| **文件** | [biz.util.isLocalFileExist](0781-checks-for-local-files-in-batches.md) | 批量检测本地文件是否存在 | 不需要 |
| [biz.util.openLocalFile](0780-open-a-local-file.md) | 打开本地文件 | 不需要 |
| [biz.util.uploadFile](0778-upload-objects-jsapi.md) | 上传本地资源到开发者服务器 | 不需要 | - **Android** | |
| [biz.util.downLoadFile](0779-download-objects.md) | 下载文件 | 不需要 | - **PC** | |
| **存储** | [util.domainStorage.setItem](0782-set-storage-information.md) | 设置存储信息 | 不需要 | - **Android** - **iOS** | |
| [util.domainStorage.getItem](0783-obtain-storage-information.md) | 获取存储信息 | 不需要 |
| [util.domainStorage.removeItem](0784-delete-storage-information.md) | 删除存储信息 | 不需要 |
| **钉盘** | [biz.cspace.saveFile](0787-save-file-to-nail-plate.md) | 保存文件到钉盘 | 需要 |
| [biz.util.uploadAttachment](0789-upload-attachment-to-nail-plate-select-file-from-nail-plate-h5.md) | 上传附件到钉盘、从钉盘选择文件 | 需要 | - **Android** - **iOS** - **PC** | |
| [biz.cspace.preview](0785-preview-nail-plate-file.md) | 预览钉盘文件 | 需要 |
| [biz.cspace.previewDentryImages](0788-batch-preview-of-nail-plate-pictures.md) | 批量预览钉盘图片 | 不需要 | - **Android** - **iOS** | |
| [biz.cspace.chooseSpaceDir](0786-select-a-pin-plate-directory-h5.md) | 选取钉盘目录 | 需要 |
| **图片** | [biz.util.chooseImage](0790-select-picture.md) | 拍照或者选择本地照片 | 需要 |
| biz.util.compressImage | [压缩图片](https://open.dingtalk.com/document/orgapp/compress-images) | 不需要 |
| [biz.util.previewImage](0791-compress-images.md) | 压缩图片 | 不需要 | - **Android** - **iOS** - **PC** | |
| **地图** | [device.geolocation.get](0798-obtain-current-geographic-location-information-single-positioning.md) | 获取当前地理位置信息（单次定位） | 需要 | - **Android** - **iOS** | |
| [device.geolocation.start](0799-continuous-retrieval-of-current-geographic-information-continuous-location.md) | 连续获取当前地理位置信息（持续定位） | 需要 |
| [device.geolocation.stop](0795-stop-continuous-positioning.md) | 停止连续定位 | 需要 |
| [device.geolocation.status](0796-batch-continuous-positioning-status.md) | 批量获取连续定位的状态 | 不需要 |
| [biz.map.locate](0793-map-positioning.md) | 地图定位 | 需要 |
| [biz.map.search](0797-map-page-supports-search.md) | 地图页面支持搜索 | 需要 |
| [biz.map.view](0794-display-position.md) | 展示传入的经纬度位置 | 需要 |
| **音频** | [device.audio.startRecord](0800-start-recording.md) | 开始录音 | 需要 |
| [device.audio.stopRecord](0801-stop-recording.md) | 停止录音 | 需要 |
| [device.audio.onRecordEnd](0807-automatic-stop-of-monitoring-and-recording.md) | 监听录音自动停止 | 需要 |
| [device.audio.download](0803-download-audio.md) | 下载音频 | 需要 |
| [device.audio.play](0802-playback-voice.md) | 播放语音 | 需要 |
| [device.audio.pause](0805-pause-playback-of-speech.md) | 暂停播放语音 | 需要 |
| [device.audio.resume](0809-resume-paused-voice.md) | 恢复暂停播放的语音 | 需要 |
| [device.audio.stop](0806-stop-audio-playback.md) | 停止播放音频 | 需要 |
| [device.audio.onPlayEnd](0808-automatically-stops-playback.md) | 监听播放自动停止 | 需要 |
| [device.audio.translateVoice](0804-voice-to-text.md) | 语音转文字 | 需要 |
| **摇一摇** | [device.accelerometer.watchShake](0810-start-a-shake.md) | 启动摇一摇 | 不需要 |
| [device.accelerometer.clearShake](0811-stop-a-shake.md) | 停止摇一摇 | 不需要 |
| **UI控件** | [ui.input.plain](0812-input-box.md) | 设置输入框基本信息 | 不需要 |
| [ui.progressBar.setColors](0816-set-the-color-of-the-top-progress-bar.md) | 设置顶部进度条颜色 | 不需要 |
| [ui.pullTorefresh.enable](0813-enable-pull-down-refresh.md) | 启用下拉刷新 | 不需要 |
| [ui.pullToRefresh.stop](0814-refresh.md) | 收起下拉刷新 | 不需要 |
| [ui.pullToRefresh.disable](0815-disable-pull-down-refresh.md) | 禁用下拉刷新 | 不需要 |
| [ui.webViewBounce.enable](0817-enable-webview-for-ios.md) | 启用iOS Webview弹性效果 | 不需要 | - **iOS** | |
| [ui.webViewBounce.disable](0818-disable-webview-autoscaling-for-ios.md) | 禁用iOS Webview弹性效果 | 不需要 |
| **扫码** | [biz.util.scan](0820-scan-barcodes-and-qr-codes.md) | 扫条形码或二维码 | 不需要 | - **Android** - **iOS** | |
| [biz.util.scanCard](0819-scan-business-cards.md) | 扫名片 | 需要 |
| **支付** | [biz.alipay.pay](0821-payment-interface.md) | 支付接口 | 需要 |
| **转屏横屏** | [拼接dd\_orientation=auto参数](0827-microapplication-page-supports-screen-rotation.md) | 微应用页面支持转屏 | 不需要 |
| [拼接dd\_orientation参数](0828-microapplication-page-supports-horizontal-dashboard.md) | 微应用页面支持横屏 | 不需要 |
| [拼接dd\_full\_screen=true参数](0829-full-screen-display-of-microapplication-page.md) | 微应用页面全屏展示 | 不需要 |
| [拼接dd\_nav\_translucent=true参数](0830-the-microapplication-navigation-bar-is-transparent.md) | 微应用页面导航栏透明 | 不需要 |
| [device.screen.rotateView](0825-rotate-screen.md) | 旋转屏幕 | 不需要 |
| [device.screen.resetView](0826-reset-rotation-screen.md) | 重置旋转屏幕 | 不需要 |
| **外部联系人** | [biz.contact.externalComplexPicker](0831-select-external-contacts.md) | 选择外部联系人 | 需要 |
| [biz.contact.externalEditForm](0832-edit-external-contacts.md) | 编辑外部联系人 | 需要 |
| **自定义联系人** | [biz.customContact.choose](0833-custom-radio-contact.md) | 自定义选择企业内员工或者外部联系人，支持单选 | 需要 | - **Android** - **iOS** - **PC** | |
| [biz.customContact.multipleChoose](0834-multiple-custom-contacts.md) | 多选自定义联系人 | 需要 |
| **打开新页面** | [biz.util.open](0838-open-the-in-application-page.md) | 打开应用内页面 | 需要 |
| [biz.util.openLink](0836-open-link-on-new-window.md) | 打开目标页面 | 不需要 |
| [biz.util.openModal](0835-open-modal-box.md) | 打开模态框 | 不需要 | - **PC** | |
| [biz.util.openSlidePanel](0837-open-side-panel.md) | 打开侧边面板 | 不需要 |
| [biz.util.invokeWorkbench](0839-open-new-tab.md) | PC端打开新弹窗页面 | 需要 |
| [biz.tabwindow.isTab](0840-determines-whether-it-is-a-pop-up-window.md) | 判断是否为弹窗窗口 | 不需要 |
| **打开应用** | [biz.navigation.navigateToPage](0841-jump-to-h5-micro-application.md) | 跳转H5微应用 | 不需要 | - **Android** - **iOS** | |
| [biz.navigation.navigateBackPage](0842-return-to-previous-application.md) | [返回上一个应用](https://open.dingtalk.com/document/orgapp/return-to-previous-application) | 不需要 |
| **数据加解密** | [biz.util.encrypt](0843-data-encryption.md) | [数据加密](https://open.dingtalk.com/document/orgapp/data-encryption) | 需要 |
| [biz.util.decrypt](0844-data-decryption.md) | [数据解密](https://open.dingtalk.com/document/orgapp/data-decryption) | 需要 |
| **视频会议** | [biz.conference.videoConfCall](0845-initiate-video-conference.md) | [发起视频会议](https://open.dingtalk.com/document/orgapp/initiate-video-conference) | 需要 | - **Android** - **iOS** - **PC** | |
| **办公电话** | [biz.conference.getCloudCallInfo](0848-check-whether-the-enterprise-has-an-office-phone-number.md) | [查询企业是否已开办公电话](https://open.dingtalk.com/document/orgapp/check-whether-the-enterprise-has-an-office-phone-number) | 需要 |
| [biz.conference.createCloudCall](0847-direct-dialing.md) | [发起办公电话呼叫](https://open.dingtalk.com/document/orgapp/direct-dialing) | 需要 |
| [biz.conference.getCloudCallList](0846-query-the-number-list.md) | [查询话单列表](https://open.dingtalk.com/document/orgapp/query-the-number-list) | 需要 |
| **在线课堂** | [biz.live.startClassRoom](0849-online-classroom-initiation.md) | [发起在线课堂](https://open.dingtalk.com/document/orgapp/online-classroom-initiation) | 需要 | - **PC** | |
| **专属钉钉** | [biz.realm.getUserExclusiveInfo](0851-retrieve-user-information-info.md) | 获取钉钉客户端是否为专属钉钉 | 不需要 | - **Android** - **iOS** - **PC** | |
| [biz.ATMBle.exclusiveLiveCheck](0850-id-verification.md) | 实现实人人脸对比 | 需要 | - **Android** - **iOS** | |
