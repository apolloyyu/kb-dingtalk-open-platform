---
title: "inside业务接口"
source_url: "https://open.dingtalk.com/document/development/inside-business-interface"
namespace: "development"
slug: "inside-business-interface"
group: "硬件开发"
tab: "门禁 Linux 接入"
breadcrumb: "SDK接入接口 > inside业务接口"
doc_id: "V8mGHCN5tD"
updated_at: "2026-08-04 09:07:15"
---

> Source: https://open.dingtalk.com/document/development/inside-business-interface
> Path: 硬件开发 / 门禁 Linux 接入 / SDK接入接口 > inside业务接口
> Updated: 2026-08-04 09:07:15

# inside业务接口

inside业务接口定义在dtiot\_inside\_service.h中，INSIDE负责完成门禁和考勤两个业务，在注册inside业务时，不要再去注册门禁、考勤两个单独模块。

模块初始化时，注册回调。当SDK调用方身份识别后发送请求后会通过回调来通知sdk调用方业务结果，包含门禁、考勤。

## 注册INSIDE业务回调

**接口：**int(\*register\_response)(int(\*response)(struct dtiot\_inside\_resp\_t\* resp));

**请求参数：**

| 参数 | 是否必填 | 说明 |
| --- | --- | --- |
| response | 否 | 回调函数。  **[!NOTE]**  在注册inside业务时，不要再去注册门禁、考勤两个单独模块。 |

**返回结果：**

- **0**：成功
- **其他**：失败

第三方门禁设备向SDK注册业务调用结果函数，SDK将业务调用结果异步形式返回给调用方。返回的数据如下：

```
struct dtiot_inside_resp_t {
    unsigned long feature_id;                       /*feature ID,只有人脸的时候此字段才有意义*/
    unsigned long long session_id;                  /*回话ID, 由设备维护，可以从一个随机数开始*/
    unsigned long long timestamp;                   /*时间戳, 1970至今, localtime, 毫秒, 请求的时间*/
    enum dtiot_identify_class type;                 /*触发方式*/
    enum dtiot_identify_act act;                    /*触发动作*/
    dtiot_card_info_t *card_info;                /*卡片信息,为NULL表示此回复不包含此业务信息或者未查到此卡片信息*/
    struct dtiot_user_info_t *user_info;                /*用户信息,为NULL表示此回复不包含此业务信息*/
    struct dtiot_attendance_result_t *attendance_resp;  /*考勤回复消息,为NULL表示此回复不包含此业务信息*/
    struct dtiot_entrance_result_t *entrance_resp;      /*门禁回复消息,为NULL表示此回复不包含此业务信息*/
    struct dtiot_temperature_result_t *temperature_resp;/*测温回复消息,为NULL表示此回复不包含此业务信息*/
};

第三方判断出如果是门禁回复的消息，可根据具体包含的数据采取相应的设备开门控制。
struct dtiot_entrance_result_t {
    enum dtiot_entrance_act act;                    /*开门动作*/ 
    unsigned int durations;                         /*开门持续的时长*/
};
```

第三方判断消息属于考勤回复的消息，要根据具体包含极速考勤结果或者凝视考勤结果，进一步进行设备UI提示。

```
struct  dtiot_attendance_result_t {
    enum dtiot_attendance_class type;                       /*考勤类型,如果为凝视u则为gaze_resp,其他为face_resp*/
    enum dtiot_attendance_act act;                          /*考勤动作*/
    union {
        struct dtiot_attendance_face_resp_t speed_resp;      /*极速考勤结果*/
        struct dtiot_attendance_gaze_resp_t gaze_resp;      /*凝视考勤结果*/
    } data;
};
```

关于凝视考勤，SDK的处理逻辑如下：

- 第三方负责模块：控制模块，识别模块。
- 钉钉负责模块：考勤模块，凝视子模块。

![a3abc92222884bd28116e866490545bc0579](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3226558061/p203842.png)

## 请求完成INSIDE业务

**接口：**int(\*request)(struct dtiot\_identify\_req\_t\* req);

**请求参数：**

| 参数 | 是否必填 | 说明 |
| --- | --- | --- |
| req | 否 | 考勤、门禁业务参数。 |

**返回结果：**

- **0**：成功
- **其他**：失败

关于考勤、门禁业务参数,其使用场景是在人脸识别后，根据得到的识别结果，进一步调用此接口进行门禁和考勤业务。

业务触发时机如下：

![inside业务完成](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7780389061/p203845.png)

如图，当第三方特征识别成功，分数达标，可以调用本接口进行考勤与门禁业务，当请求进入enum dtiot\_identify\_act ac值DTIOT\_IDENTIFY\_ACT\_ENTER，代表人脸进入了。SDK开始进行规则的匹配，门禁业务判断是否有权限，考勤还判断是否已经是进入了凝视状态等。最后给出结果。

结构体详情介绍如下：

```
struct dtiot_identify_req_t {
    unsigned long feature_id;                                           /*feature ID, 人脸的时候才有*/
    unsigned long long session_id;                                      /*回话ID, 由设备维护, 可以从一个随机数开始*/
    unsigned long long timestamp;                                       /*时间戳, 1970至今, localtime，毫秒, 请求的时间*/
    enum dtiot_identify_class type;                                     /*触发方式*/
    enum dtiot_identify_act act;                                        /*触发动作*/
    union {
        struct dtiot_face_identify_data_t face_identify_data;           /*人脸识别数据*/
        struct dtiot_card_identify_data_t card_identify_data;           /*卡片数据*/
    } feature_data;
    char data[0];                                                       /*扩展字段*/
};
```
