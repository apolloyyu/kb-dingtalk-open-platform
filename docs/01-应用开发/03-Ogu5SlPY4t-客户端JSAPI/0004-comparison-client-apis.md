---
title: "版本对比与迁移"
source_url: "https://open.dingtalk.com/document/development/comparison--client-apis"
namespace: "development"
slug: "comparison--client-apis"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "版本对比与迁移"
doc_id: "iqQUVizgyp"
updated_at: "2026-07-22 16:25:06"
---

> Source: https://open.dingtalk.com/document/development/comparison--client-apis
> Path: 应用开发 / 客户端JSAPI / 版本对比与迁移
> Updated: 2026-07-22 16:25:06

# 版本对比与迁移

本文档详细说明钉钉客户端API的新旧版本差异、SDK引入方式、迁移操作指南，帮助开发者平滑过渡到新版API。

## **客户端SDK**

### SDK简介

`dingtalk-jsapi` 是钉钉官方提供的客户端JavaScript SDK，用于在H5微应用和小程序中调用钉钉原生能力。

### 引入方式

#### 方式一：使用npm引入（推荐）

```
npm install dingtalk-jsapi --save
```

> *dingtalk-jsapi 3.0.27 版本后支持一段式，例如：chooseChat，同时也支持三段式，例如：biz.contact.choose。*

在代码中引入：

```
import * as dd from 'dingtalk-jsapi'; // 此方式为整体加载，也可按需进行加载
```

优势：

- 支持按需加载，减少包体积
- 易于版本管理和更新
- 获得底层依赖模块的快速修复支持

#### 方式二：使用CDN引入（不推荐）

在HTML中直接引入：

```
<script src="https://g.alicdn.com/dingding/dingtalk-jsapi/3.1.0/dingtalk.open.js"></script>
```

局限性：

- 无法按需加载，包体积较大
- 难以获得底层依赖模块的快速修复支持
- 仅建议在简单场景或快速原型开发中使用

## 新旧版API对比

### **背景优势**

钉钉开放平台将客户端 API 调用方式由“三段式”统一升级为“一段式”，旨在简化调用逻辑、提升开发效率并增强跨端一致性。

- **三段式调用（旧版）**：格式为 `namespace.function.action`，如 `biz.util.chooseImage`
- **一段式调用（新版）**：格式为单一函数名，如 `chooseImage`。

**升级优势**：

- 接口命名更简洁直观
- 函数语义更清晰，易于记忆和使用
- 支持更灵活的参数结构和返回值设计
- 更好地支持 TypeScript 类型推导

**参考文档**：

- 新版客户端 API，详情参考新版[JSAPI 总览](0001-jsapi-overview.md)。
- 旧版客户端 API，分为小程序和H5微应用：

  - 小程序详情参考旧版[小程序JSAPI总览](0434-mini-program-jsapi-overview.md)。
  - H5微应用详情参考旧版[H5微应用JSAPI总览](0750-jsapi-overview-1.md)。

### 核心区别

| 特性 | 旧版API（三段式） | 新版API（一段式） |
| --- | --- | --- |
| 调用方式 | `dd.biz.contact.choose` | `dd.chooseChat` |
| 命名规范 | 按功能模块分层（biz/device/ui等） | 扁平化命名，语义更清晰 |
| 兼容性 | 所有版本均支持 | 需要 3.0.27+ 版本 |
| 推荐程度 | 兼容保留，不推荐新项目使用 | 推荐使用 |
| 参数结构 | 部分API参数复杂 | 参数更统一、简洁 |
| 返回值 | 部分API返回结构不一致 | 返回值更规范 |

### 调用示例对比

以"选择会话"为例：

- 旧版（三段式）

  ```
  dd.biz.chat.choose({
    corpId: 'dingxxxxxxxx',
    isAllowCreateGroup: true,
    onSuccess: (result) => {
      console.log('选择的会话ID:', result.cid);
    },
    onFail: (err) => {
      console.error('选择失败', err);
    }
  });
  ```
- 新版（一段式）

  ```
  dd.chooseChat({
    corpId: 'dingxxxxxxxx',
    isAllowCreateGroup: true,
    onSuccess: (result) => {
      console.log('选择的会话ID:', result.cid);
    },
    onFail: (err) => {
      console.error('选择失败', err);
    }
  });
  ```

### **API对照表**

#### **界面**

用于控制页面导航、弹窗反馈、日期选择等用户界面交互行为。

| **类目** | **新版客户端API** | **旧版客户端API** |
| --- | --- | --- |
| **地图** | [chooseDistrict](0132-jsapi-choose-district.md) | biz.util.chooseRegion |
| **导航栏** | [setNavigationTitle](0048-jsapi-set-navigation-title.md) | biz.navigation.setTitle |
| [setNavigationIcon](0047-jsapi-set-navigation-icon.md) | biz.navigation.setIcon |
| [setNavigationLeft](0049-jsapi-set-navigation-left.md) | biz.navigation.setLeft |
| [goBackPage](0043-jsapi-go-back-page.md) | biz.navigation.goBack |
| [replacePage](0045-jsapi-replace-page.md) | biz.navigation.replace |
| [closePage](0042-jsapi-close-page.md) | biz.navigation.close |
| [quitPage](0044-jsapi-quit-page.md) | biz.navigation.quit |
| **交互反馈** | [alert](0150-jsapi-alert.md) | device.notification.alert |
| [confirm](0152-jsapi-confirm.md) | device.notification.confirm |
| [showToast](0156-jsapi-show-toast.md) | device.notification.toast |
| [hideLoading](0153-jsapi-hide-loading.md) | device.notification.hidePreloader |
| [hideToast](0151-jsapi-hide-toast.md) | device.notification.hideToast |
| [showLoading](0157-jsapi-show-loading.md) | device.notification.showPreloader |
| [showActionSheet](0158-jsapi-show-action-sheet.md) | device.notification.actionSheet |
| [showModal](0155-jsapi-show-modal.md) | device.notification.extendModal |
| [prompt](0154-jsapi-prompt.md) | device.notification.prompt |
| **选择日期** | [datePicker](0182-jsapi-date-picker.md) | biz.util.datetimepicker |
| [dateRangePicker](0183-jsapi-date-range-picker.md) | biz.calendar.chooseInterval |
| [timePicker](0184-jsapi-time-picker.md) | biz.util.timepicker |
| [chooseDateTime](0179-jsapi-choose-date-time.md) | biz.calendar.chooseDateTime |
| [chooseOneDayInCalendar](0180-jsapi-choose-one-day-in-calendar.md) | biz.calendar.chooseOneDay |
| [chooseHalfDayInCalendar](0181-jsapi-choose-half-day-in-calendar.md) | biz.calendar.chooseHalfDay |
| **下拉刷新** | [enablePullDownRefresh](0160-jsapi-enable-pull-down-refresh.md) | ui.pullToRefresh.enable |
| [disablePullDownRefresh](0159-jsapi-disable-pull-down-refresh.md) | ui.pullToRefresh.disable |
| **选项选择器** | [singleSelect](0186-jsapi-single-select.md) | biz.util.chosen |
| [multiSelect](0185-jsapi-multi-select.md) | biz.util.multiSelect |

#### **设备**

提供对手机硬件功能的访问能力，如 NFC、振动、剪贴板等。

| **类目** | **新版客户端API** | **旧版客户端API** |
| --- | --- | --- |
| **UUID** | [getDeviceUUID](0356-jsapi-get-device-uuid.md) | device.base.getUUID |
| **NFC** | [writeNFC](0409-jsapi-write-nfc.md) | device.nfc.nfcWrite |
| [readNFC](0408-jsapi-read-nfc.md#undefined) | device.nfc.nfcRead |
| **振动** | [vibrate](0381-jsapi-vibrate.md) | device.notification.vibrate |
| **扫码** | [scanCard](0407-jsapi-scan-card.md) | biz.util.scanCard |
| **摇一摇** | [clearShake](0410-jsapi-clear-shake.md) | device.accelerometer.clearShake |
| [watchShake](0411-jsapi-watch-shake.md) | device.accelerometer.watchShake |
| **剪贴板** | [setClipboard](0380-jsapi-set-clipboard.md) | biz.clipboardData.setData |
| **Wi-Fi** | [getWifiStatus](0368-jsapi-get-wifi-status.md) | device.base.getWifiStatus |
| **屏幕亮度** | [setKeepScreenOn](0414-jsapi-set-keep-screen-on.md) | biz.util.setScreenKeepOn |
| [setScreenBrightness](0413-jsapi-set-screen-brightness.md) | device.screen.setScreenBrightness |
| **拨打电话** | [addPhoneContact](0416-jsapi-add-phone-contact.md) | biz.phoneContact.add |
| **设备电量** | [getBatteryInfo](0415-jsapi-get-battery-info.md) | device.base.getBatteryInfo |
| **网络状态** | [getNetworkType](0364-jsapi-get-network-type.md) | device.connection.getNetworkType |
| [getWifiHotspotStatus](0365-jsapi-get-wifi-hotspot-status.md) | device.base.getInterface |
| **系统信息** | [getSystemInfo](0358-jsapi-get-system-info.md) | device.base.getPhoneInfo |
| [rsa](0362-jsapi-rsa.md) | biz.data.rsa |
| [showAuthGuide](0363-jsapi-show-auth-guide.md) | biz.util.showAuthGuide |
| [checkAuth](0357-jsapi-check-auth.md) | biz.util.checkAuth |
| [isScreenReaderEnabled](0361-jsapi-is-screen-reader-enabled.md) | device.screen.isScreenReaderEnabled |
| [getSystemSettings](0359-jsapi-get-system-settings.md) | device.base.openSystemSetting |
| **设备方向** | [resetScreenView](0417-jsapi-reset-screen-view.md) | device.screen.resetView |
| [rotateScreenView](0418-jsapi-rotate-screen-view.md) | device.screen.rotateView |

#### **跳转**

用于实现页面跳转、本地缓存等通用功能。

| **新版客户端API** | **旧版客户端API** |
| --- | --- |
| [openLink](0192-jsapi-open-link.md) | biz.util.openLink |
| [isInTabWindow](0187-jsapi-is-in-tab-window.md) | biz.tabwindow.isTab |
| [getStorage](0034-jsapi-get-storage.md) | util.domainStorage.getItem |
| [removeStorage](0038-jsapi-remove-storage.md) | util.domainStorage.removeItem |
| [navigateBackPage](0189-jsapi-navigate-back-page.md) | biz.navigation.navigateBackPage |
| [navigateToPage](0188-jsapi-navigate-to-page.md) | biz.navigation.navigateToPage |
| [openMicroApp](0193-jsapi-open-micro-app.md) | biz.microApp.openApp |
| [openPageInMicroApp](0194-jsapi-open-page-in-micro-app.md) | biz.util.open |
| [openPageInWorkBenchForPC](0197-jsapi-open-page-in-work-bench-for-pc.md) | biz.util.invokeWorkbench |
| [openPageInSlidePanelForPC](0196-jsapi-open-page-in-slide-panel-for-pc.md) | biz.util.openSlidePanel |

#### **多媒体**

支持图像、音频的采集与播放控制。

| **类目** | **新版客户端API** | **旧版客户端API** |
| --- | --- | --- |
| **图片** | [chooseImage](0206-jsapi-choose-image.md) | biz.util.chooseImage |
| [previewImage](0210-jsapi-preview-image.md) | biz.util.previewImage |
| **录音** | [translateVoice](0223-jsapi-translate-voice.md) | device.audio.translateVoice |
| [onPlayAudioEnd](0216-jsapi-on-play-audio-end.md) | device.audio.onPlayEnd |
| [onRecordEnd](0215-jsapi-on-record-end.md) | device.audio.onRecordEnd |
| [downloadAudio](0214-jsapi-download-audio.md) | device.audio.download |
| [resumeAudio](0219-jsapi-resume-audio.md) | device.audio.resume |
| [pauseAudio](0218-jsapi-pause-audio.md) | device.audio.pause |
| [stopAudio](0222-jsapi-stop-audio.md) | device.audio.stop |
| [playAudio](0217-jsapi-play-audio.md) | device.audio.play |
| [stopRecord](0220-jsapi-stop-record.md) | device.audio.stopRecord |
| [startRecord](0221-jsapi-start-record.md) | device.audio.startRecord |

#### **缓存**

用于在客户端进行数据持久化存储。

| **新版客户端API** | **旧版客户端API** |
| --- | --- |
| [setStorage](0040-jsapi-set-storage.md) | util.domainStorage.setItem |
| [getStorage](0034-jsapi-get-storage.md) | util.domainStorage.getItem |
| [removeStorage](0038-jsapi-remove-storage.md) | util.domainStorage.removeItem |

#### **位置**

提供定位、地图展示、搜索等功能。

| **新版客户端API** | **旧版客户端API** |
| --- | --- |
| [getLocation](0322-jsapi-get-location.md) | device.geolocation.get |
| [openLocation](0325-jsapi-open-location.md) | biz.map.view |
| [searchMap](0326-jsapi-search-map.md) | biz.map.search |
| [locateInMap](0324-jsapi-locate-in-map.md) | biz.map.locate |
| [getLocatingStatus](0323-jsapi-get-locating-status.md) | device.geolocation.status |
| [stopLocating](0327-jsapi-stop-locating.md) | device.geolocation.stop |
| [startLocating](0328-jsapi-start-locating.md) | device.geolocation.start |

#### **网络**

支持文件下载等网络操作。

| **类目** | **新版客户端API** | **旧版客户端API** |
| --- | --- | --- |
| **上传下载** | [downloadFile](0011-jsapi-download-file.md) | biz.file.downloadFile |

#### **分享**

实现内容分享至会话或其他渠道。

| **新版客户端API** | **旧版客户端API** |
| --- | --- |
| [share](0199-jsapi-share.md) | biz.util.share |
| [showSharePanel](0200-jsapi-show-share-panel.md) | biz.util.showSharePanel |

#### **获取凭证**

用于获取用户身份凭证。

| **新版客户端API** | **旧版客户端API** |
| --- | --- |
| [getAuthCode](0006-jsapi-get-auth-code.md) | runtime.permission.requestAuthCode |
| [getOperateAuthCode](0008-jsapi-get-operate-auth-code.md) | runtime.permission.requestOperateAuthCode |

#### **会话管理**

用于打开或选择聊天窗口。

| **新版客户端API** | **旧版客户端API** |
| --- | --- |
| [chooseChat](0318-jsapi-choose-chat.md) | biz.chat.chooseConversationByCorpId |
| [openChatByChatId](0319-jsapi-open-chat-by-chat-id.md) | biz.chat.toConversation |
| [openChatByUserId](0320-jsapi-open-chat-by-user-id.md) | biz.chat.openSingleChat |
| [openChatByConversationId](0321-jsapi-open-chat-by-conversation-id.md) | biz.chat.toConversationByOpenConversationId |

#### **通讯录**

用于从组织架构中选择人员或部门。

| **新版客户端API** | **旧版客户端API** |
| --- | --- |
| [choosePhonebook](0269-jsapi-choose-phonebook.md) | biz.contact.chooseMobileContacts |
| [complexChoose](0267-jsapi-complex-choose.md) | biz.contact.complexPicker |
| [chooseDepartments](0270-jsapi-choose-departments.md) | biz.contact.departmentsPicker |
| [chooseExternalUsers](0272-jsapi-choose-external-users.md) | biz.contact.externalComplexPicker |
| [editExternalUser](0273-jsapi-edit-external-user.md) | biz.contact.externalEditForm |
| [chooseUserFromList](0271-jsapi-choose-user-from-list.md) | chooseUserFromList |
| [chooseStaffForPC](0268-jsapi-choose-staff-for-pc.md) | biz.contact.choose |

#### **DING**

用于创建和发送 DING 消息。

| **新版客户端API** | **旧版客户端API** |
| --- | --- |
| [createDing](0265-jsapi-create-ding.md) | biz.ding.create |
| [createDingForPC](0266-jsapi-create-ding-for-pc.md) | biz.ding.post |

#### **办公电话**

支持云呼叫、快速拨号等功能。

| **新版客户端API** | **旧版客户端API** |
| --- | --- |
| [callUsers](0311-jsapi-call-users.md) | biz.telephone.call |
| [checkBizCall](0312-jsapi-check-biz-call.md) | biz.telephone.checkBizCall |
| [getCloudCallList](0314-jsapi-get-cloud-call-list.md) | biz.conference.getCloudCallList |
| [makeCloudCall](0315-jsapi-make-cloud-call.md) | biz.conference.createCloudCall |
| [getCloudCallInfo](0313-jsapi-get-cloud-call-info.md) | biz.conference.getCloudCallInfo |
| [quickCallList](0316-jsapi-quick-call-list.md) | biz.telephone.quickCallList |

#### **钉盘**

用于文件保存、预览和上传。

| **新版客户端API** | **旧版客户端API** |
| --- | --- |
| [saveFileToDingTalk](0332-jsapi-save-file-to-ding-talk.md) | biz.cspace.saveFile |
| [previewFileInDingTalk](0330-jsapi-preview-file-in-ding-talk.md) | biz.cspace.preview |
| [uploadAttachmentToDingTalk](0333-jsapi-upload-attachment-to-ding-talk.md) | biz.util.uploadAttachment |
| [chooseDingTalkDir](0329-jsapi-choose-ding-talk-dir.md) | biz.cspace.chooseSpaceDir |
| [previewImagesInDingTalkBatch](0331-jsapi-preview-images-in-ding-talk-batch.md) | biz.cspace.previewDentryImages |

#### **文件**

操作设备本地文件。

| **新版客户端API** | **旧版客户端API** |
| --- | --- |
| [openLocalFile](0335-jsapi-open-local-file.md) | biz.util.openLocalFile |
| [isLocalFileExist](0334-jsapi-is-local-file-exist.md) | biz.util.isLocalFileExist |

#### **视频**

发起视频会议呼叫。

| **新版客户端API** | **旧版客户端API** |
| --- | --- |
| [makeVideoConfCall](0308-jsapi-make-video-conf-call.md) | biz.conference.videoConfCall |

#### **专属开放**

面向特定客户开放的能力。

| **新版客户端API** | **旧版客户端API** |
| --- | --- |
| [getUserExclusiveInfo](0424-jsapi-get-user-exclusive-info.md) | biz.realm.getUserExclusiveInfo |

## 迁移操作指南

### 迁移策略

#### 新项目（直接使用）

直接使用新版API（一段式）：

- 确保 `dingtalk-jsapi` 版本 >= 3.0.27
- 优先使用一段式调用方式
- 参考官方文档中的最新示例代码

#### 已有项目（渐进式迁移）

**阶段一：评估现状**

- 统计项目中使用的三段式API数量
- 识别哪些API有对应的一段式版本
- 评估迁移工作量

**阶段二：逐步替换**

- 从非核心功能开始替换（如UI组件、工具类API）
- 逐个模块迁移，每完成一个模块进行测试
- 保持向后兼容，确保旧代码仍能正常工作

**阶段三：全面验证**

- 完成所有可迁移API的替换
- 进行全面的回归测试
- 更新文档和代码注释

### 迁移示例

以下是一个完整的迁移示例，展示如何将旧版代码升级为新版：

**迁移前（旧版）**：

```
import dd from 'dingtalk-jsapi';

// 选择人员
dd.biz.contact.choose({
  startWithDepartmentId: -1,
  multiple: true,
  onSuccess: (result) => {
    console.log('选择的人员:', result.users);
  },
  onFail: (err) => {
    console.error('选择失败', err);
  }
});

// 获取位置
dd.device.geolocation.get({
  targetAccuracy: 200,
  coordinate: 1,
  withReGeocode: false,
  useCache: true,
  onSuccess: (result) => {
    console.log('位置信息:', result);
  },
  onFail: (err) => {
    console.error('获取位置失败', err);
  }
});
```

迁移后（新版）：

```
import dd from 'dingtalk-jsapi';

// 选择人员
dd.chooseContact({
  startWithDepartmentId: -1,
  multiple: true,
  onSuccess: (result) => {
    console.log('选择的人员:', result.users);
  },
  onFail: (err) => {
    console.error('选择失败', err);
  }
});

// 获取位置
dd.getLocation({
  targetAccuracy: 200,
  coordinate: 1,
  withReGeocode: false,
  useCache: true,
  onSuccess: (result) => {
    console.log('位置信息:', result);
  },
  onFail: (err) => {
    console.error('获取位置失败', err);
  }
});
```

### 注意事项

1. **兼容性测试**：迁移后务必在不同版本的钉钉客户端上进行测试
2. **参数一致性**：大部分API的参数保持不变，但建议重新核对官方文档
3. **回调函数**：`onSuccess` 和 `onFail`的使用方式保持一致
4. **鉴权配置**：H5应用的鉴权流程不受影响，无需修改
5. **错误处理**：新版的错误码和错误信息可能有所优化，建议更新错误处理逻辑

## **常见问题**

- **Q1：我的项目必须使用旧版API吗？**

  答：不是必须的。新版SDK（3.0.27+）同时支持一段式和三段式调用，你可以根据实际情况选择：

  - 新项目：推荐使用一段式
  - 老项目：可以继续使用三段式，或逐步迁移到一段式
- **Q2：一段式API是否在所有钉钉版本中都可用？**

  答：一段式API需要满足以下条件：

  - `dingtalk-jsapi` 版本 >= 3.0.27
  - 钉钉客户端版本较新（建议升级到最新版本）

    如果在不支持的环境中调用一段式API，会返回错误。建议在调用前进行能力检测：

    ```
    <javascript>

      if (typeof dd.chooseChat === 'function') {  // 支持一段式API  dd.chooseChat({...});} else {  // 降级使用三段式API  dd.biz.chat.choose({...});}
    ```
- **Q3: 迁移后是否需要重新发布应用？**

  答：是的。任何代码变更都需要重新构建并发布应用。建议在低峰期发布，并做好回滚准备。
- **Q4: 旧版API会被废弃吗？**

  答：目前钉钉官方尚未宣布废弃三段式API的计划，但推荐新项目使用一段式API。三段式API将继续保持兼容，以确保存量应用的稳定运行。
- **Q5: 如何确认当前使用的SDK版本？**

  答：可以通过以下方式查看：

  ```
  <javascript>

  console.log(dd.version); // 输出SDK版本号
  ```

  或在 `package.json` 中查看：

  ```
  <json>

  {  
    "dependencies": {
      "dingtalk-jsapi": "^3.0.27"  
    }
  }
  ```
