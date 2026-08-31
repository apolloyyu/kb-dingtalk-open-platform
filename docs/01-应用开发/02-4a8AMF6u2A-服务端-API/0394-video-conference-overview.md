---
title: "概述"
source_url: "https://open.dingtalk.com/document/development/video-conference-overview"
namespace: "development"
slug: "video-conference-overview"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "音视频 > 概述"
doc_id: "Emt0eX1v74"
updated_at: "2026-07-10 10:05:13"
---

> Source: https://open.dingtalk.com/document/development/video-conference-overview
> Path: 应用开发 / 服务端 API / 音视频 > 概述
> Updated: 2026-07-10 10:05:13

# 概述

## **钉钉视频会议**

### **介绍**

钉钉视频会议是钉钉为用户提供的**安全、清晰、稳定、流畅**的视频会议，与钉钉深度融合，为用户提供会议全生命周期和会议全流程的数字化沉淀。

视频会议最高支持**500人**同时在线， 参会人员可以通过**手机、Pad、电脑**（同时支持window和Mac系统）等设备接入，随时随地一起开会。同时钉钉视频会议为企业组织提供**全视角、全融合、全终端、全流程**的数智化视频会议解决方案。

### **亮点功能**

- 您可以使用钉钉视频会议进行远程音视频会议、共享屏幕和文件、管控会议等， 满足智能沟通协作需求。
- 钉钉视频会议还提供钉钉会议室连接器，打通线上软件会议与线下会议室会议。 1080P高清画质，稳定流畅。
- 一键参会，方式多样。参会者可通过链接、短信、入会口令、会议卡片等多种方式，快速定位指定会议室一键参会。
- 会议安全可控有保障，可以根据需求使用组织内部会议、全员强制静音、锁定会议等丰富的安全管理功能，确保会议全程安全可控，有序进行。
- 在线互动功能丰富有趣，使用全员看TA、参会人置顶、会议白板、美颜、会议录制等丰富的在线互动功能，确保会议高效沟通。
- 会议设备和方式无缝切换，参会人可共享屏幕和文件，共享时还可以播放本地音视频文件；发起人可控制屏幕共享权限，避免参会人随意共享。
- 日程自动创建与同步，召集者可以提前预约会议时间，并将日程同步给所有参会者，届时自动提醒并支持一键发起视频会议，让团队内部沟通变得简单便捷。
- 企业培训实时显示参会者画面，如同面对面沟通，打破时间空间的限制，如同现场会议般提升工作效率。

### **如何发起视频会议**

- 方式一：打开钉钉PC客户端并登录>>单击客户端左侧**会议**![](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/a/RMlYnjDX9tMe5YQa/ffce629dc5f54e0d93827bc2ad207e6b0521.png) 图标>>发起会议。

  ![发起会议](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7032380461/p378290.png)
- 方式二：在对话框中发起视频会议

  - 群聊窗口发起视频会议：单击输入框上方的电话![](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/a/RMlYnjDX9tMe5YQa/230bfe3d8914427b9d656fec170be0920521.png) 图标。

    ![视频会议群聊.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3119463871/p731068.png)
  - 单聊窗口发起视频会议：单击输入框上方的电话![](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/a/RMlYnjDX9tMe5YQa/230bfe3d8914427b9d656fec170be0920521.png) 图标。

    ![视频会议.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3119463871/p731067.png)

### **开放接口列表**

视频会议提供了丰富的接口开放能力，开发者通过API接口可以实现视频会议和企业业务系统打通。

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [创建视频会议](0399-create-a-video-conference.md) | 创建视频会议。 | 新版 |
| [关闭视频会议](0400-close-audio-video-conference.md) | 关闭视频会议，仅限该会议的主持人有关闭视频会议的权限。 | 新版 |
| [查询视频会议信息](0401-querying-video-conference-information.md) | 查询视频会议的基础信息。 | 新版 |
| [批量查询视频会议信息](0403-batch-query-of-video-conference-information.md) | 查询会议信息以及参会人员。 | 新版 |
| [查询视频会议成员](0402-querying-video-conference-members.md) | 分页查询视频会议参会人员的信息。 | 新版 |
| [查询用户进行中会议列表](0404-api-queryuserongoingconference.md) | 查询用户进行中会议列表，返回进行中会议id列表及该用户在会中对应的成员信息。 | 新版 |
| [查询企业进行中会议列表](0405-api-queryorgconferencelist.md) | 调用本接口，可根据分页参数查询企业进行中会议列表。 | 新版 |
| [根据会议号查询会议信息](0406-api-queryconferenceinfobyroomcode.md) | 调用本接口，根据会议 roomCode 和分页参数会议信息。 | 新版 |
| [锁定会议](0407-api-lockconference.md) | 调用本接口，锁定会议。 | 新版 |
| [邀请用户入会](0408-invite-users-to-join.md) | 会议过程中，邀请新的用户加入会议，调用该接口后，被邀请用户会收到加入会议的通知。 | 新版 |
| [踢出会议成员](0409-kick-out-meeting-members.md) | 会议过程中，踢出成员，调用该接口后，被踢用户会离会并提示已被移出会议。 | 新版 |
| [设置全员看他](0410-set-the-whole-staff-to-see-him.md) | 会议过程中，通过该接口设置全员看他或者取消全员看他。 | 新版 |
| [设置联席主持人](0411-set-up-co-hosts.md) | 会议过程中，新增联席主持人或者删除联席主持人。 | 新版 |
| [开启视频会议直播推流](0412-video-conference-enables-live-stream-ingest.md) | 开启视频会议直播推流 | 新版 |
| [停止视频会议直播推流](0413-videoconferencing-stops-live-stream-ingest.md) | 停止视频会议直播推流 | 新版 |
| [指定人员静音或取消静音](0414-specify-person-to-mute-or-unmute.md) | 会议进行过程中，可通过该接口指定人员静音或取消静音。 | 新版 |
| [全员静音或全员取消静音](0415-mute-all-staff-or-unmute-all-staff.md) | 会议过程中，可通过该接口进行全员静音或全员取消静音。 | 新版 |
| [创建预约会议](0416-create-appointment-meeting.md) | 根据创建人、预约会议标题和开始结束时间等信息创建预约会议。 | 新版 |
| [更新预约会议](0417-update-appointment-meeting.md) | 更新预约会议标题和开始结束时间等信息。 | 新版 |
| [取消预约会议](0418-cancel-appointment-meeting.md) | 根据预约会议id取消预约会议。 | 新版 |
| [查询预约会议](0419-query-meeting-reservation.md) | 根据预约会议id查询预约会议标题等信息。 | 新版 |
| [查询预约会议设置](0420-api-queryscheduleconfsettings.md) | 根据预约会议id，查询预约会议设置信息。 | 新版 |
| [更新预约会议设置](0421-api-updatescheduleconfsettings.md) | 调用本接口，更新预约会议设置。 | 新版 |
| [创建用户专属短链](0422-api-createcustomshortlink.md) | 根据用户信息，创建用户专属短链。 | 新版 |
| [查询预约会议历史会议信息](0423-query-appointment-meeting-history-meeting-information.md) | 查询预约会议已开启过的历史会议信息，当前返回最后一次会议信息。 | 新版 |
| [开启视频会议云录制](0424-video-conference-open-cloud-recording.md) | 开启视频会议云录制。 | 新版 |
| [停止视频会议云录制](0425-video-conferencing-stops-cloud-recording.md) | 停止视频会议云录制。 | 新版 |
| [查询会议录制的详情信息](0426-query-recording-information.md) | 查询会议录制的详情信息。 | 新版 |
| [查询会议录制中的视频信息](0427-queries-the-playback-information-about-a-recorded-cloud-video.md) | 查询会议录制中的视频信息。 | 新版 |
| [查询会议录制中的文本信息](0428-queries-the-text-information-about-cloud-recording.md) | 查询视频会议录制的语音转文字信息 | 新版 |

### 回调事件列表

视频会议支持人事档案变动回调事件，更多事件可参考[事件订阅总览](../04-LFcRvVD08N-事件订阅/0002-org-event-overview.md)。

## **直播**

### **介绍**

钉钉直播具有直播预约、权限自由设置、多群联播、实时互动、直播录制、直播数据统计等完善功能，打破时间和空间上的限制，方便的完成一场直播活动，高效上传下达，改变传统培训管理模式。

对于企业培训、招聘宣讲、活动直播、在线课堂等多种场景，钉钉直播能够轻松搞定，同时提供专业的重保服务，确保现场执行团队顺利部署及调试设备，保障直播线上到线下的整体质量和体验。

### **亮点功能**

- 直播预约：可提前获得直播链接进行宣传，打通钉钉日历，开播前进行提醒。
- 权限自由设置：主播可设置直播为公开可见或企业内可见。
- 多群联播：轻松将单场直播同步到多个群。
- 实时互动：指出连麦、聊天、点赞、签到、答题等丰富的互动形式。
- 直播录制：自动保存直播录像，方便直播内容沉淀和二次传播。
- 直播数据统计观看人数、观看时长等数据精细记录，直播培训效果可衡量。

### **如何发起直播**

在**钉钉PC客户端**页面，单击客户端左侧**更多**，依次单击**直播 > 发起直播。**

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2293231661/p480498.png)

### **开放接口列表**

直播提供了丰富的开放接口，开发者通过API接口可以实现钉钉直播原生能力调用。

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [创建直播](0429-create-live-streaming.md) | 创建直播。 | 新版 |
| [删除直播](0430-delete-live-streaming.md) | 删除直播。 | 新版 |
| [查询直播信息](0431-queries-the-live-streaming-information.md) | 根据直播ID查询直播信息。 | 新版 |
| [修改直播属性信息](0432-modify-live-streaming.md) | 修改直播属性信息。 | 新版 |
| [查询直播观看人员信息](0433-queries-the-viewing-information-of-viewers.md) | 查询直播观看人员的具体观看信息。 | 新版 |

### **回调事件列表**

直播支持状态变化、修改信息和观看回放信息回调事件。

- [直播状态变更](../04-LFcRvVD08N-事件订阅/0074-event-live-status-change-event.md)
- [直播信息修改](../04-LFcRvVD08N-事件订阅/0075-event-live-update-event.md)
- [直播回放观看数据推送](../04-LFcRvVD08N-事件订阅/0076-event-live-watch-playback-event.md)
- [直播结束数据处理完成事件](../04-LFcRvVD08N-事件订阅/0077-event-live-statistic-done-event.md)

### **名词解释**

#### **自定义封面**

直播封面，可上传自定义的直播封面图片。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2293231661/p480510.png)

#### **添加直播群**

直播开始后，自动发送开播提醒通知至添加的直播群。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2293231661/p480528.png)

#### **直播ID**

每个直播有唯一的直播ID，定义为liveId。可调用[创建直播](0429-create-live-streaming.md)接口获取liveId参数值。

#### **观看人数**

观看直播人数，不包括主持人，定义为liveUv。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2293231661/p480548.png)

## **智能会议室**

### **介绍**

钉钉智能会议室具有会议室预定、会议室审批管理、智能硬件关联、数据报表统计等完善功能，方便对组织内的物理会议空间高效管理，改变传统会议室管理、预定模式，助力组织实现数字化转型。

![iShot2022-11-03_10](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3119463871/p511863.png)

### **亮点功能**

- 会议室在线化：会议室实现在线预定和管理，预定便捷更有序。
- 会议室资源高效利用：会议室预定超时可抢占，保证资源高效合理利用。
- 会议室管理更高效：支持分组和统计报表导出，管理工作更高效。
- 智能统计会议签到：扫码即可签到，自动统计到会情况。
- 软硬件结合一体化，通过预定日程，硬件视频会议设备一键发会入会。
- 通过预定入会的会议室，自动拥有云会议联席主持人权限，高效会管会控。

### **如何开通智能会议室**

智能会议室是钉钉默认安装的官方应用。员工可以在钉钉工作台添加应用并使用。

- **手机端**

  在钉钉手机客户端**工作台**页面，在**全员**内单击**添加**，在搜索框输入**智能会议室**，单击**添加**。![图片排版-手机展示-4张图1备份 3](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3119463871/p511861.png)
- **电脑端**

  在钉钉电脑客户端**工作台**页面，在**全员**内单击**添加**，在搜索框输入**智能会议室**，单击**添加**。![图片排版-钉钉端展示-1张图1备份 12345](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3119463871/p511855.png)

### **开放接口列表**

智能会议室提供了丰富的开放接口，开发者通过API接口可以实现钉钉智能会议室管理。

#### **会议室**

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [创建会议室](0434-create-a-meeting-room.md) | 创建会议室。 | 新版 |
| [删除会议室](0435-delete-a-meeting-room.md) | 删除会议室。 | 新版 |
| [更新会议室信息](0436-update-meeting-room-information.md) | 更新会议室信息。 | 新版 |
| [查询会议室列表](0437-check-the-meeting-room-list.md) | 查询会议室列表。 | 新版 |
| [查询会议室详情](0438-check-meeting-room-details.md) | 查询会议室详情。 | 新版 |
| [创建会议室预定黑名单](0439-api-createbookingblacklist.md) | 调用本接口，可以创建会议室预定黑名单。 | 新版 |
| [删除会议室预定黑名单](0440-api-deletebookingblacklist.md) | 调用本接口，删除会议室预定黑名单。 | 新版 |
| [查询视频会议设备信息](0441-querying-video-conference-device-information.md) | 查询视频会议设备信息 | 新版 |
| [查询视频会议设备属性信息](0442-querying-video-conference-device-attribute-information.md) | 查询视频会议设备属性信息 | 新版 |
| [发送Rooms中控API信令](0443-api-sendcentralcontrol.md) | 给会议室中的设备发送中控信令，属于高级功能。 | 新版 |

#### **会议室分组**

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [创建会议室分组](0444-create-meeting-room-groups.md) | 创建会议室分组。 | 新版 |
| [删除会议室分组](0445-delete-a-conference-room-group.md) | 删除会议室分组。 | 新版 |
| [获取分组管理员信息](0446-api-querymeetingroomgroupadmin.md) | 查询会议室分组管理员信息。 | 新版 |
| [更新会议室分组信息](0447-update-meeting-room-groups.md) | 更新会议室分组的信息。 | 新版 |
| [查询会议室分组列表](0448-query-meeting-rooms-groups.md) | 查询会议室分组列表。 | 新版 |
| [查询会议室分组信息](0449-query-meeting-room-groups.md) | 查询会议室分组信息。 | 新版 |

#### **自定义屏幕模板**

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [创建自定义屏幕模板](0450-api-createdevicecustomtemplate.md) | 调用本接口，根据模板名称创建自定义屏幕模板。 | 新版 |
| [删除自定义屏幕模板](0451-api-deletedevicecustomtemplate.md) | 调用本接口，根据模板ID，删除自定义屏幕模板。 | 新版 |
| [更新自定义屏幕模板](0452-api-updatedevicecustomtemplate.md) | 根据自定义屏幕模板ID，更新自定义屏幕模板信息内容。 | 新版 |
| [查询自定义屏幕信息](0453-api-querydevicecustomtemplate.md) | 根据模板id，查询自定义屏幕信息。 | 新版 |
| [查询自定义屏幕模板列表](0454-api-querylistdevicecustomscreentemplate.md) | 调用本接口，直接查询自定义屏幕模板列表信息。 | 新版 |

### **回调事件列表**

会议室支持预定等事件，包括预定成功、取消等。

- [设备中控事件](../04-LFcRvVD08N-事件订阅/0079-events-open-meeting-room-central-control.md)
- [会议室事件](../04-LFcRvVD08N-事件订阅/0078-nqrbp8.md)

### **名词解释**

#### **预定会议室**

可通过智能会议室应用，提前预定会议室资源。会议室可预定时间、可预定人员范围等参数，管理员可通过后台进行配置。

#### **会议室分组**

管理员可通过会议室分组功能，对组织内的会议室进行分级管理。例如，区分城市、园区、楼宇三级目录，分别关联不同组会议室。当前支持三级分组功能。

#### **会议室审批**

企业内部分特殊会议室的使用，需要特定管理员进行审批后才可预定使用。哪些会议室需审批、审批人等参数，管理员可通过后台进行配置。

#### **会议室抢占**

会议室作为一种稀缺资源，应尽可能避免浪费。已经预定的会议室，如果超过时间之后仍然无人使用，可配置允许其他人现场抢占会议室。是否可抢占、空置时间等参数，管理员可通过后台进行配置。

#### **会议室专属预定时间**

会议室支持全局配置及单个会议室设置，可在指定会议室中开启“专属预定时间”，对会议室进行参数配置。
