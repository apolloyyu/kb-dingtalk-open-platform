---
title: "会议室事件"
source_url: "https://open.dingtalk.com/document/development/meeting-room-events"
namespace: "development"
slug: "meeting-room-events"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "历史文档（不推荐） > HTTP回调 > 企业内部应用回调事件 > 会议室事件"
doc_id: "r4FIlNs6o9"
updated_at: "2025-10-16 14:31:56"
---

> Source: https://open.dingtalk.com/document/development/meeting-room-events
> Path: 应用开发 / 事件订阅 / 历史文档（不推荐） > HTTP回调 > 企业内部应用回调事件 > 会议室事件
> Updated: 2025-10-16 14:31:56

# 会议室事件

本文介绍了会议室事件的相关说明。

## 事件类型

| **事件类型** | **说明** |
| --- | --- |
| meetingroom\_book | 会议室预定等事件，预定成功、取消等。 |
| meetingroom\_room\_info | 会议室创建、更新、删除等。 |

## 会议室预定等事件

注册回调事件时填写的事件类型“call\_back\_tag”，包含事件“meetingroom\_book”，推送结构体以json的形式封装，通过eventSubType字段代表不同事件。eventSubType会随着业务增加而新增。示例详见会议室预定事件-附录。

> **[!IMPORTANT]**
>
> 监控新值，根据业务需要调整逻辑。

**会议室状态流转**![image.png ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1364199951/p165428.png)![image.png ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1364199951/p165429.png)

**枚举值 preStatus：**

| **状态** | **说明** |
| --- | --- |
| INIT | 初始态。 |
| SUCCESS | 预定已成功。 |
| APPROVALING | 审批中。 |

- 审批预定

  **参数说明：**

  | **参数** | **说明** |
  | --- | --- |
  | EventType | 事件类型。  **参数值**：meetingroom\_book |
  | eventSubType | **参数值**：appvaral |
  | bookId | 预定id。 |
  | preStatus | 事件触发前的状态，枚举值详见状态流转。后续会新增前置状态值,接入方需要监控新值，根据自己业务调需要调整逻辑，例子详见附录。 |
  | userId | 用户userId。 |
  | userName | 用户名称。 |
  | roomId | 会议室id。 |
  | roomName | 会议室名称。 |
  | corpId | 企业id。 |
  | bookTime | 预定时间。 |
  | startTime | 开始时间。  格式：yyyy-MM-dd hh:mm:ss  例如：2019-11-10 15:00:40 |
  | endTime | 结束时间。  格式：yyyy-MM-dd hh:mm:ss  例如：2019-11-11 15:30:40 |
  | title | 会议名称。 |
  | isApproval | 是否是审批预定。 |

  **示例：**

  ```
  {
    "EventType":"meetingroom_book",
      "eventSubType":"appvaral",
    "corpId":"ding123xxxx",
    "bookTime":"2019-12-18 12:33:58",
    "preStatus":"INIT",
    "title":"会议",
    "userName":"吴同学",
    "userId":"123",
     "roomId":"1",
     "roomName":"董事长会议室",
     "bookId":"ding234xxxx",
     "isApproval":true,
     "startTime":"2019-12-18 15:00:00",
     "endTime":"2019-12-18 17:30:00"
  }
  ```
- 预定成功

  **参数说明：**

  | **参数** | **说明** |
  | --- | --- |
  | EventType | 事件类型。  **参数值****：**meetingroom\_book |
  | eventSubType | **参数值：**bookSuccess |
  | bookId | 预定id. |
  | preStatus | 事件触发前的状态,枚举值详见状态流转。后续会新增前置状态值,接入方需要监控新值，根据自己业务调需要调整逻辑，例子详见附录。 |
  | userId | 用户userId。 |
  | userName | 用户名称。 |
  | roomId | 会议室id。 |
  | roomName | 会议室名称。 |
  | corpId | 企业id。 |
  | bookTime | 预定时间。  格式：yyyy-MM-dd hh:mm:ss  例如：2019-11-10 15:00:40 |
  | startTime | 开始时间。  格式：yyyy-MM-dd hh:mm:ss  例如：2019-11-11 15:00:40 |
  | endTime | 结束时间。  格式：yyyy-MM-dd hh:mm:ss  例如：2019-11-11 15:30:40 |
  | title | 会议名称。 |
  | isApproval | 是否是审批预定。 |

  **示例：**

  ```
  {
    "EventType":"meetingroom_book",
    "eventSubType":"bookSuccess",
    "corpId":"ding123xxxx",
    "bookTime":"2019-12-18 00:00:19",
    "preStatus":"INIT",
    "title":"会议",
    "userName":"吴同学",
    "userId":"1234",
    "roomId":"1",
    "roomName":"培训室",
    "bookId":"ding234xxxx",
    "isApproval":false,
    "startTime":"2019-12-21 09:30:00",
    "endTime":"2019-12-21 10:00:00"
  }
  ```
- 预定取消

  **参数说明：**

  | **参数** | **说明** |
  | --- | --- |
  | EventType | 事件类型。  **参数值：**meetingroom\_book |
  | eventSubType | **参数值：**bookCancel |
  | bookId | 预定id。 |
  | preStatus | 事件触发前的状态,枚举值详见状态流转。后续会新增前置状态值,接入方需要监控新值，根据自己业务调需要调整逻辑，例子详见附录。 |
  | corpId | 企业id。 |
  | isApproval | 是否是审批预定。 |

  **示例：**

  ```
  {
    "EventType":"meetingroom_book",
    "eventSubType":"bookCancel",
    "isApproval":false,
    "corpId":"ding123xxxx",
    "preStatus":"SUCCESS",
    "bookId":"ding234xxxx"
  }
  ```
- 审批拒绝

  **参数说明：**

  | **参数** | **说明** |
  | --- | --- |
  | EventType | 事件类型。  **参数值：**meetingroom\_book |
  | eventSubType | **参数值：**bookRefuse |
  | bookId | 预定id。 |
  | preStatus | 事件触发前的状态,枚举值详见状态流转。后续会新增前置状态值,接入方需要监控新值，根据自己业务调需要调整逻辑，例子详见附录。 |
  | corpId | 企业id。 |
  | isApproval | 是否是审批预定。 |

  **示例：**

  ```
  {
    "EventType":"meetingroom_book",
    "eventSubType":"bookRefuse",
    "isApproval":true,
    "corpId":"ding123************123",
    "preStatus":"APPROVALING",
    "bookId":"ding234************123"
  }
  ```
- 会议预定更新

  参数说明：

  | **参数** | **含义** |
  | --- | --- |
  | EventType | 事件类型。  **参数值：**meetingroom\_book |
  | eventSubType | **参数值：**bookUpdate |
  | bookId | 预定id。 |
  | corpId | 企业id。 |
  | title | 会议名称 。 |
  | isApproval | 是否是审批预定。 |

  **示例：**

  ```
  {
    "EventType":"meetingroom_book",
    "isApproval":false,
    "eventSubType":"bookUpdate",
    "corpId":"ding123xxxx",
    "title":"会议",
    "roomName":"培训室",
    "bookId":"ding234xxxx"
  }
  ```
- 参会人变动

  **参数说明：**

  | **参数** | **说明** |
  | --- | --- |
  | EventType | 事件类型。  **参数值：**meetingroom\_book |
  | eventSubType | **参数值：**bookMemberChang |
  | bookId | 预定id。 |
  | corpId | 企业id。 |
  | isApproval | 是否是审批预定。 |

  **示例：**

  ```
  {
    "EventType":"meetingroom_book",
    "eventSubType":"bookMemberChange",
    "isApproval":false,
    "corpId":"ding123xxxx",
    "bookId":"ding234xxxx"
  }
  ```
- 附录

  - **eventSubType新增取值举例**

    起初只有普通预定，后续新增了审批预定业务，eventSubType新增了“appvaral”和“bookRefuse”值。
  - **preStatus新增****取值****举例**

    起初只有普通预定，“预定取消”回调(eventSubType=bookCancel)的preStatus只有“SUCCESS”取值，后续新增了审批预定业务，该回调的preStatus新增了“APPROVALING”值。

## 会议室创建等事件

注册回调事件时填写的事件类型“call\_back\_tag”，包含事件“meetingroom\_room\_info”，推送结构体以json的形式封装，通过eventSubType字段代表不同功能。

- 会议室创建

  | **参数** | **说明** |
  | --- | --- |
  | EventType | 事件类型。  **参数值：**meetingroom\_room\_info |
  | eventSubType | **参数值：**create |
  | roomName | 会议室名称。 |
  | corpId | 企业id。 |
  | roomId | 会议室id。 |
  | labels | 支持的设备标签。  - **1**：tv - **2**：电话 - **3**：投影仪 - **4**：白板 - **5**：视频 |
  | capacity | 容量。"20人" 或"100"或"500人以上"或"500以上"。 |

  **示例：**

  ```
  {
    "EventType":"meetingroom_room_info",
    "eventSubType":"create",
    "corpId":"ding123xxxx",
    "roomId":"231",
    "roomName":"报告厅",
    "labels":"[3,5]",
    "capacity":"500"
  }
  ```
- 会议室更新

  | **参数** | **说明** |
  | --- | --- |
  | EventType | 事件类型。  **参数值：**meetingroom\_room\_info |
  | eventSubType | **参数值：**update |
  | roomName | 会议室名称。 |
  | corpId | 企业id。 |
  | roomId | 会议室id。 |
  | labels | 支持的设备标签。  - **1**：tv - **2**：电话 - **3**：投影仪 - **4**：白板 - 5：视频 |
  | capacity | 容量。"20人" 或"100"或"500人以上"或"500以上"。 |

  **示例：**

  ```
  {
    "EventType":"meetingroom_room_info",
    "eventSubType":"update",
    "corpId":"ding123xxxx",
    "roomId":"271",
    "roomName":"培训室",
    "labels":[3,5],
    "capacity":"100人"
  }
  ```
- 会议室删除

  | **参数** | **说明** |
  | --- | --- |
  | EventType | 事件类型。  **参数值：**meetingroom\_room\_info |
  | eventSubType | **参数值：**del |
  | corpId | 企业id。 |
  | roomId | 会议室id。 |

  **示例：**

  ```
  {
    "EventType":"meetingroom_room_info",
    "eventSubType":"del",
    "corpId":"ding123xxxx",
    "roomId":"278"
  }
  ```
