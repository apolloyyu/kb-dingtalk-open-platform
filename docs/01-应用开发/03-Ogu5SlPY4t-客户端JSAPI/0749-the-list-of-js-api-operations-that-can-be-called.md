---
title: "小程序内支持调用的微应用JSAPI列表"
source_url: "https://open.dingtalk.com/document/development/the-list-of-js-api-operations-that-can-be-called"
namespace: "development"
slug: "the-list-of-js-api-operations-that-can-be-called"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 小程序内支持调用的微应用JSAPI列表"
doc_id: "SL1u4OqnUN"
updated_at: "2025-09-17 21:01:25"
---

> Source: https://open.dingtalk.com/document/development/the-list-of-js-api-operations-that-can-be-called
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 小程序内支持调用的微应用JSAPI列表
> Updated: 2025-09-17 21:01:25

# 小程序内支持调用的微应用JSAPI列表

本文介绍了小程序内，支持调用的微应用JSAPI。

| **分类** | **接口说明** | **JSAPI名称** | **Android** | **IOS** | **企业内部小程序** | **第三方企业小程序** |
| --- | --- | --- | --- | --- | --- | --- |
| **免登** | [获取微应用免登授权码](https://open.dingtalk.com/document/orgapp/obtain-the-micro-application-exemption-authorization-code) | runtime.permission.requestAuthCode | 支持 | 支持 | 支持 | 支持 |
| **设备** | [获取手机基础信息](https://open.dingtalk.com/document/orgapp/obtain-basic-mobile-phone-information) | device.base.getPhoneInfo | 支持 | 支持 | 支持 | 支持 |
| [获取uuid](https://open.dingtalk.com/document/orgapp/get-uuid) | device.base.getUUID | 支持 | 支持 | 支持 | 支持 |
| [获取热点接入信息](https://open.dingtalk.com/document/orgapp/queries-the-hotspot-access-information) | device.base.getInterface | 支持 | 支持 | 支持 | 支持 |
| [获取wifi状态](https://open.dingtalk.com/document/orgapp/get-wifi-status) | device.base.getWifiStatus | 支持 | 支持 | 支持 | 支持 |
| [获取网络类型](https://open.dingtalk.com/document/orgapp/queries-the-network-type) | device.connection.getNetworkType | 支持 | 支持 | 支持 | 支持 |
| [读取NFC芯片内容](https://open.dingtalk.com/document/orgapp/read-nfc-chip-content) | device.nfc.nfcRead | 支持 | 不支持 | 支持 | 支持 |
| [NFC数据写入](https://open.dingtalk.com/document/orgapp/nfc-data-write) | device.nfc.nfcWrite | 支持 | 不支持 | 支持 | 支持 |
| **日期和月历** | [日期选择器](https://open.dingtalk.com/document/orgapp/date-selector) | biz.util.datepicker | 支持 | 支持 | 支持 | 支持 |
| [时间选择器](https://open.dingtalk.com/document/orgapp/time-picker) | biz.util.timepicker | 支持 | 支持 | 支持 | 支持 |
| [日期及时间选择器](https://open.dingtalk.com/document/orgapp/date-and-time-selector) | biz.util.datetimepicker | 支持 | 支持 | 支持 | 支持 |
| [月历组件：选择某时间](https://open.dingtalk.com/document/orgapp/monthly-calendar-component-select-a-specific-time) | biz.calendar.chooseDateTime | 支持 | 支持 | 支持 | 支持 |
| [月历组件：选择某天](https://open.dingtalk.com/document/orgapp/monthly-calendar-component-select-a-certain-day) | biz.calendar.chooseOneDay | 支持 | 支持 | 支持 | 支持 |
| [月历组件：选择半天](https://open.dingtalk.com/document/orgapp/monthly-calendar-component-select-a-date-range) | biz.calendar.chooseHalfDay | 支持 | 支持 | 支持 | 支持 |
| [月历组件：选择日期区间](https://open.dingtalk.com/document/orgapp/month-calendar-component-select-date-range) | biz.calendar.chooseInterval | 支持 | 支持 | 支持 | 支持 |
| **通讯录选人** | [选择部门和人](https://open.dingtalk.com/document/orgapp/select-department-and-person) | biz.contact.complexPicker | 支持 | 支持 | 支持 | 支持 |
| [选择部门信息](https://open.dingtalk.com/document/orgapp/select-department-information-h5) | biz.contact.departmentsPicker | 支持 | 支持 | 支持 | 支持 |
| [创建企业聊天](https://open.dingtalk.com/document/orgapp/create-enterprise-chat) | biz.contact.createGroup | 支持 | 支持 | 支持 | 支持 |
| [选取手机通讯录](https://open.dingtalk.com/document/orgapp/select-phone-address-book) | biz.contact.chooseMobileContacts | 支持 | 支持 | 支持 | 支持 |
| **业务** | [分享](https://open.dingtalk.com/document/orgapp/share) | biz.util.share | 支持 | 支持 | 支持 | 支持 |
| [下拉控件](https://open.dingtalk.com/document/orgapp/drop-down-control) | biz.util.chosen | 支持 | 支持 | 支持 | 支持 |
| [复制到粘贴板](https://open.dingtalk.com/document/orgapp/copy-to-clipboard) | biz.clipboardData.setData | 支持 | 支持 | 支持 | 支持 |
| **导航栏** | [关闭当前页面](https://open.dingtalk.com/document/orgapp/close-the-current-page) | biz.navigation.close | 支持 | 支持 | 支持 | 支持 |
| **弹窗** | [alert](https://open.dingtalk.com/document/orgapp/alert) | device.notification.alert | 支持 | 支持 | 支持 | 支持 |
| [confirm](https://open.dingtalk.com/document/orgapp/confirm) | device.notification.confirm | 支持 | 支持 | 支持 | 支持 |
| [prompt](https://open.dingtalk.com/document/orgapp/prompt) | device.notification.prompt | 支持 | 支持 | 支持 | 支持 |
| [手机震动](https://open.dingtalk.com/document/orgapp/mobile-phone-vibration) | device.notification.vibrate | 支持 | 支持 | 支持 | 支持 |
| [显示加载](https://open.dingtalk.com/document/orgapp/show-load) | device.notification.showPreloader | 支持 | 支持 | 支持 | 支持 |
| [隐藏加载](https://open.dingtalk.com/document/orgapp/hide-loading) | device.notification.hidePreloader | 支持 | 支持 | 支持 | 支持 |
| [toast](https://open.dingtalk.com/document/orgapp/toast) | device.notification.toast | 支持 | 支持 | 支持 | 支持 |
| [actionsheet](https://open.dingtalk.com/document/orgapp/actionsheet) | device.notification.actionSheet | 支持 | 支持 | 支持 | 支持 |
| [modal弹浮层](https://open.dingtalk.com/document/orgapp/modal-pop-up-layer) | device.notification.modal | 支持 | 支持 | 支持 | 支持 |
| [extendModal](https://open.dingtalk.com/document/orgapp/extendmodal) | device.notification.extendModal | 支持 | 支持 | 支持 | 支持 |
| [多选组件](https://open.dingtalk.com/document/orgapp/multiple-select-components) | biz.util.multiSelect | 支持 | 支持 | 支持 | 支持 |
| **会话** | [根据corpid选择会话](https://open.dingtalk.com/document/orgapp/select-session-based-on-corpid) | biz.chat.chooseConversationByCorpId | 支持 | 支持 | 支持 | 支持 |
| [根据chatId跳转到对应会话](https://open.dingtalk.com/document/orgapp/redirects-to-a-specific-session-based-on-the-chatid-h5) | biz.chat.toConversation | 支持 | 支持 | 支持 | 支持 |
| [根据openConversationId跳转到对应会话](https://open.dingtalk.com/document/orgapp/redirects-to-the-specified-session-based-on-the-openconversationid) | biz.chat.toConversationByOpenConversationId | 支持 | 支持 | 支持 | 支持 |
| [打开与某个用户的单聊会话](https://open.dingtalk.com/document/orgapp/open-a-one-on-one-chat-session-with-a-user) | biz.chat.openSingleChat | 支持 | 支持 | 支持 | 支持 |
| **电话** | [拨打钉钉电话](https://open.dingtalk.com/document/orgapp/call-dingtalk-h5) | biz.telephone.call | 支持 | 支持 | 支持 | 支持 |
| [通用电话拨打](https://open.dingtalk.com/document/orgapp/universal-phone-call-h5) | biz.telephone.showCallMenu | 支持 | 支持 | 支持 | 支持 |
| [检查某企业的办公电话开通状态](https://open.dingtalk.com/document/orgapp/check-the-status-of-office-telephones-of-an-enterprise-h5) | biz.telephone.checkBizCall | 支持 | 支持 | 支持 | 支持 |
| [拨打单人电话选项（可定制）](https://open.dingtalk.com/document/orgapp/make-a-single-call-option-customizable-h5) | biz.telephone.quickCallList | 支持 | 支持 | 支持 | 支持 |
| **DING** | [DING 2.0 发钉](https://open.dingtalk.com/document/orgapp/ding-2-0-hair-pin) | biz.ding.create | 支持 | 支持 | 支持 | 支持 |
| **文件** | [上传文件](https://open.dingtalk.com/document/orgapp/upload-objects-jsapi) | biz.util.uploadFile | 支持 | 不支持 | 支持 | 支持 |
| **存储** | [设置存储信息](https://open.dingtalk.com/document/orgapp/set-storage-information) | util.domainStorage.setItem | 支持 | 支持 | 支持 | 支持 |
| [获取存储信息](https://open.dingtalk.com/document/orgapp/obtain-storage-information) | util.domainStorage.getItem | 支持 | 支持 | 支持 | 支持 |
| [删除存储信息](https://open.dingtalk.com/document/orgapp/delete-storage-information) | util.domainStorage.removeItem | 支持 | 支持 | 支持 | 支持 |
| **钉盘** | [保存文件到钉盘](https://open.dingtalk.com/document/orgapp/save-file-to-nail-plate) | biz.cspace.saveFile | 支持 | 支持 | 支持 | 支持 |
| [上传附件到钉盘/从钉盘选择文件](https://open.dingtalk.com/document/orgapp/upload-attachment-to-nail-plate-select-file-from-nail-plate-h5) | biz.util.uploadAttachment | 支持 | 支持 | 支持 | 支持 |
| [预览钉盘文件](https://open.dingtalk.com/document/orgapp/preview-nail-plate-file) | biz.cspace.preview | 支持 | 支持 | 支持 | 支持 |
| [批量预览钉盘图片](https://open.dingtalk.com/document/orgapp/batch-preview-of-nail-plate-pictures) | biz.cspace.previewDentryImages | 支持 | 支持 | 支持 | 支持 |
| [选取钉盘目录](https://open.dingtalk.com/document/orgapp/select-a-pin-plate-directory-h5) | biz.cspace.chooseSpaceDir | 支持 | 支持 | 支持 | 支持 |
| **图片** | [选择图片](https://open.dingtalk.com/document/orgapp/select-picture) | biz.util.chooseImage | 支持 | 支持 | 支持 | 支持 |
| [压缩图片](https://open.dingtalk.com/document/orgapp/compress-images) | biz.util.previewImage | 支持 | 支持 | 支持 | 支持 |
| **地图** | [获取当前地理位置信息（单次定位）](https://open.dingtalk.com/document/orgapp/obtain-current-geographic-location-information-single-positioning) | device.geolocation.get | 支持 | 支持 | 支持 | 支持 |
| [连续获取当前地理位置信息（持续定位）](https://open.dingtalk.com/document/orgapp/continuous-retrieval-of-current-geographic-information-continuous-location) | device.geolocation.start | 支持 | 支持 | 支持 | 支持 |
| [停止连续定位](https://open.dingtalk.com/document/orgapp/stop-continuous-positioning) | device.geolocation.stop | 支持 | 支持 | 支持 | 支持 |
| [批量获取连续定位的状态](https://open.dingtalk.com/document/orgapp/batch-continuous-positioning-status) | device.geolocation.status | 支持 | 支持 | 支持 | 支持 |
| [地图定位](https://open.dingtalk.com/document/orgapp/map-positioning) | biz.map.locate | 支持 | 支持 | 支持 | 支持 |
| [地图页面支持搜索](https://open.dingtalk.com/document/orgapp/map-page-supports-search) | biz.map.search | 支持 | 支持 | 支持 | 支持 |
| [展示位置](https://open.dingtalk.com/document/orgapp/display-position) | biz.map.view | 支持 | 支持 | 支持 | 支持 |
| **音频** | [开始录音](https://open.dingtalk.com/document/orgapp/start-recording) | device.audio.startRecord | 支持 | 支持 | 支持 | 支持 |
| [停止录音](https://open.dingtalk.com/document/orgapp/stop-recording) | device.audio.stopRecord | 支持 | 支持 | 支持 | 支持 |
| [监听录音自动停止](https://open.dingtalk.com/document/orgapp/automatic-stop-of-monitoring-and-recording) | device.audio.onRecordEnd | 支持 | 支持 | 支持 | 支持 |
| [下载音频](https://open.dingtalk.com/document/orgapp/download-audio) | device.audio.download | 支持 | 支持 | 支持 | 支持 |
| [播放语音](https://open.dingtalk.com/document/orgapp/playback-voice) | device.audio.play | 支持 | 支持 | 支持 | 支持 |
| [暂停播放语音](https://open.dingtalk.com/document/orgapp/pause-playback-of-speech) | device.audio.pause | 支持 | 支持 | 支持 | 支持 |
| [恢复暂停播放的语音](https://open.dingtalk.com/document/orgapp/resume-paused-voice) | device.audio.resume | 支持 | 支持 | 支持 | 支持 |
| [停止播放音频](https://open.dingtalk.com/document/orgapp/stop-audio-playback) | device.audio.stop | 支持 | 支持 | 支持 | 支持 |
| [监听播放自动停止](https://open.dingtalk.com/document/orgapp/automatically-stops-playback) | device.audio.onPlayEnd | 支持 | 支持 | 支持 | 支持 |
| [语音转文字](https://open.dingtalk.com/document/orgapp/voice-to-text) | device.audio.translateVoice | 支持 | 支持 | 支持 | 支持 |
| **摇一摇** | [启动摇一摇](https://open.dingtalk.com/document/orgapp/start-a-shake) | device.accelerometer.watchShake | 支持 | 支持 | 支持 | 支持 |
| [停止摇一摇](https://open.dingtalk.com/document/orgapp/stop-a-shake) | device.accelerometer.clearShake | 支持 | 支持 | 支持 | 支持 |
| **UI控件** | [输入框](https://open.dingtalk.com/document/orgapp/input-box) | ui.input.plain | 支持 | 支持 | 支持 | 支持 |
| **扫码** | [扫条形码、二维码](https://open.dingtalk.com/document/orgapp/scan-barcodes-and-qr-codes) | biz.util.scan | 支持 | 支持 | 支持 | 支持 |
| [扫名片](https://open.dingtalk.com/document/orgapp/scan-business-cards) | biz.util.scanCard | 支持 | 支持 | 支持 | 支持 |
| **支付** | [支付接口](https://open.dingtalk.com/document/orgapp/payment-interface) | biz.alipay.pay | 支持 | 支持 | 支持 | 支持 |
| **外部联系人** | [选择外部联系人](https://open.dingtalk.com/document/orgapp/select-external-contacts) | biz.contact.externalComplexPicker | 支持 | 支持 | 支持 | 支持 |
| [编辑外部联系人](https://open.dingtalk.com/document/orgapp/edit-external-contacts) | biz.contact.externalEditForm | 支持 | 支持 | 支持 | 支持 |
| **自定义联系人** | [单选自定义联系人](https://open.dingtalk.com/document/orgapp/custom-radio-contact) | biz.customContact.choose | 支持 | 支持 | 支持 | 支持 |
| [多选自定义联系人](https://open.dingtalk.com/document/orgapp/multiple-custom-contacts) | biz.customContact.multipleChoose | 支持 | 支持 | 支持 | 支持 |
| **打开新页面** | [打开目标页面](https://open.dingtalk.com/document/orgapp/open-link-on-new-window) | biz.util.openLink | 支持 | 支持 | 支持 | 支持 |
| **专属钉钉** | [获取钉钉客户端是否为专属钉钉](https://open.dingtalk.com/document/orgapp/retrieve-user-information-info) | biz.realm.getUserExclusiveInfo | 支持 | 支持 | 支持 | 支持 |
| [专属实人认证](https://open.dingtalk.com/document/orgapp/id-verification) | biz.ATMBle.exclusiveLiveCheck | 支持 | 支持 | 支持 | 支持 |
