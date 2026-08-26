---
title: "获取年报数据"
source_url: "https://open.dingtalk.com/document/development/obtain-annual-report-data"
namespace: "development"
slug: "obtain-annual-report-data"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 数据目录 > 数据统计 > 获取年报数据 > 获取年报数据"
doc_id: "dnZKannTqH"
updated_at: "2025-09-08 19:05:47"
---

> Source: https://open.dingtalk.com/document/development/obtain-annual-report-data
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 数据目录 > 数据统计 > 获取年报数据 > 获取年报数据
> Updated: 2025-09-08 19:05:47

# 获取年报数据

调用本接口获取企业年报数据，涵盖当年参与音视频会议的次数和时长等。在一个自然年按照组织、部门和员工三个维度生产数据。

> **[!IMPORTANT]**
>
> 1. 为了更好支持组织对钉钉数据分析和管理的需求，钉钉数据资产平台将统一所有数据资产相关的产品和服务，从数据层、功能层、业务层做升级，提供更好的服务体验。为此，我们将数据资产类 OpenAPI 接口的使用路径和产品定位做了调整，本开发者文档中所述 OpenAPI 接口及 60 个其他的[数据资产类OpenAPI](https://open.dingtalk.com/document/dataservice/data-asset-interface-adjustment-description)接口，已于 2023 年 9 月 1 日**关闭开发者后台应用开发的权限申请入口**，客户可以通过[钉钉数据资产平台](https://open.dingtalk.com/document/dataservice/overview)获取相应的数据服务。
> 2. 本文档已于 2023 年 9 月 1 日迁移至历史文档（不推荐）目录，且本接口仅保持现有功能，不再新增支持其他能力，说明如下：
>
>    - 如果未使用本接口，推荐使用[钉钉数据资产平台](https://open.dingtalk.com/document/dataservice/overview)。
>    - 如果已使用本接口，建议您根据自身实际情况评估是否切换至[钉钉数据资产平台](https://open.dingtalk.com/document/dataservice/overview)。

> **[!NOTE]**
>
> 日常查询只能查询上一个年度已经生产的数据，数据不会动态更新。

## 权限

服务端API是以应用维度授权的，在调用接口前，确保已经为应用添加了接口权限。

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 是 | 专属钉钉企业年报读权限 | **[!IMPORTANT]**  暂不支持新增申请。 |
| 第三方企业应用 | 否 | — | — |
| 第三方个人应用 | 否 | — | — |

## 基本信息

**请求方式**：POST

**请求地址**：`https://oapi.dingtalk.com/topapi/kac/datav/annual_report/get`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用该接口的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](https://open.dingtalk.com/document/orgapp/obtain-orgapp-token)接口获取。 |

## Body参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| year | String | 是 | 2020 | 年份标识。 |
| type | Number | 是 | 1 | 年报的数据维度。   - **1**：企业维度 - **2**：部门维度 - **3**：员工维度   **[!NOTE]**  员工维度的数据需要额外授权，请联系对接BD。 |
| user\_id | String | 否 | user01 | 用户的userid。  **[!NOTE]**  当**type**值为3（员工维度）时，需要传入该参数。 |
| dept\_id | Number | 否 | 23434 | 部门id。  **[!NOTE]**  当**type**值为2（部门维度）时，需要传入该参数。 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | Object |  | 返回结果。 |
| isw\_msg\_click\_cnt\_1y | String | 100 | 年累计阅读互动服务窗文章数量。 |
| max\_step\_count\_1y | Number | 100 | 年累计最高运动步数。  **[!NOTE]**  仅当type为3（员工维度）时有效。 |
| min\_process\_duration\_1y | String | 100.00 | 年累计审批最短处理时间，单位分钟。  **[!NOTE]**  仅当type为1（企业维度）或2（部门维度）时有效。 |
| send\_calendar\_user\_cnt\_1y | Number | 100 | 年累计新建日程人数。  **[!NOTE]**  仅当type为1（企业维度）或2（部门维度）时有效。 |
| join\_calendar\_user\_cnt\_1y | Number | 100 | 年累计参加日程人数。  **[!NOTE]**  仅当type为1（企业维度）时有效。 |
| create\_process\_cnt\_1y | Number | 100 | 年累计创建审批数。  **[!NOTE]**  仅当type为1（企业维度）或2（部门维度）时有效。 |
| use\_smartwork\_cnt\_1y | Number | 100 | 年累计参与智能填表数。  **[!NOTE]**  仅当type为3（员工维度）时有效。 |
| send\_ding\_cnt\_1y | Number | 100 | 年累计发送DING数。 |
| recv\_ding\_cnt\_1y | Number | 100 | 年累计接收DING数。  **[!NOTE]**  仅当type为3（员工维度）时有效。 |
| new\_group\_cnt\_1y | Number | 100 | 年累计新增群数。  **[!NOTE]**  仅当type为1（企业维度）或3（员工维度）时有效。 |
| join\_calendar\_cnt\_1y | Number | 100 | 年累计参加日程数。 |
| act\_usr\_days\_1y | Number | 100 | 年累计活跃天数。  **[!NOTE]**  仅当type为3（员工维度）时有效。 |
| send\_group\_file\_message\_cnt\_1y | Number | 100 | 年累计发送群文件数。 |
| send\_ding\_user\_cnt\_1y | Number | 100 | 年累计发送DING人数。  **[!NOTE]**  仅当type为1（企业维度）时有效。 |
| send\_group\_msg\_user\_cnt\_1y | Number | 100 | 年累计发送群聊人数。  **[!NOTE]**  仅当type为1（企业维度）或2（部门维度）时有效。 |
| join\_group\_cnt\_1y | Number | 100 | 年累计加入群数。  **[!NOTE]**  仅当type为3（员工维度）时有效。 |
| avg\_process\_duration\_1y | String | 100.10 | 年累计审批平均处理时间，单位分钟。  **[!NOTE]**  仅当type为1（企业维度）或2（部门维度）时有效。 |
| send\_report\_user\_cnt\_1y | Number | 100 | 年累计发送日志人数。  **[!NOTE]**  仅当type为1（企业维度）或2（部门维度）时有效。 |
| start\_succ\_video\_conf\_len\_1y | Number | 100 | 发起视频会议时长，单位分钟。  **[!NOTE]**  仅当type为3（员工维度）时有效。 |
| create\_doc\_cnt\_1y | Number | 100 | 年累计创建文档数。 |
| send\_message\_group\_cnt\_1y | Number | 100 | 年累计活跃群数，发消息群。  **[!NOTE]**  仅当type为1（企业维度）时有效。 |
| create\_smartwork\_cnt\_1y | Number | 100 | 年累计创建智能填表数。 |
| send\_calendar\_cnt\_1y | Number | 100 | 年累计新建日程数。 |
| at\_me\_msg\_cnt\_1y | Number | 100 | 年累计被@数。  **[!NOTE]**  仅当type为3（员工维度）时有效。 |
| send\_report\_cnt\_1y | Number | 100 | 年累计发送日志数。 |
| corp\_app\_process\_inst\_cnt\_1y | Number | 100 | 年累计企业自建应用发起的审批数。  **[!NOTE]**  仅当**type**为1（企业维度）或2（部门维度）时有效。 |
| send\_group\_msg\_cnt\_1y | Number | 100 | 年累计发送群聊消息数。  **[!NOTE]**  仅当type为1（企业维度）或3（员工维度）时有效。 |
| use\_doc\_user\_cnt\_1y | Number | 100 | 使用文档用户数。  包括创建、编辑、分享、阅读文档。  **[!NOTE]**  仅当type为1（企业维度）或2（部门维度）时有效。 |
| join\_succ\_voip\_conf\_user\_cnt\_1y | Number | 100 | 年累计参与（含发起）语音会议人次。  **[!NOTE]**  仅当**type**值为1（企业维度）时有效。 |
| join\_succ\_video\_conf\_user\_cnt\_1y | Number | 100 | 年累计参与（含发起）视频会议人次。  **[!NOTE]**  仅当**type**值为1（企业维度）时有效。 |
| outside\_days\_1y | Number | 100 | 年累计外勤天数。 |
| inner\_group\_cnt\_1y | Number | 100 | 年累计新增内部群聊数量。  **[!NOTE]**  仅当**type**值为3（员工维度）时有效。 |
| process\_inst\_operate\_cnt\_1y | Number | 20 | 处理审批数。 |
| process\_inst\_submit\_cnt\_1y | Number | 20 | 发起审批数。 |
| at\_check\_days\_1y | Number | 365 | 年累计打卡天数。 |
| live\_join\_succ\_time\_len\_1y | String | 222.32 | 年累计参与直播时长，单位为分钟。 |
| live\_join\_succ\_cnt\_1y | Number | 25 | 年累计参与直播次数。 |
| join\_succ\_voip\_conf\_len\_1y | String | 234.51 | 年累计参与（含发起）语音会议时长，单位为分钟。 |
| join\_succ\_voip\_conf\_num\_1y | Number | 24 | 年累计参与（含发起）语音会议次数。 |
| join\_succ\_video\_conf\_len\_1y | String | 340.52 | 年累计发起视频会议时长，单位分钟。 |
| join\_succ\_video\_conf\_num\_1y | Number | 23 | 年累计参与（含发起）视频会议次数。 |
| use\_micro\_app\_cnt\_1y | Number | 20 | 年累计使用的应用数量。 |
| general\_form\_user\_cnt\_1y | Number | 300 | 年累计智能填表的人次。  **[!NOTE]**  仅当**type**值为1（企业维度）时有效。 |
| use\_micro\_user\_cnt\_1y | Number | 500 | 年累计使用的应用人数。  **[!NOTE]**  仅当**type**为1（企业维度）或2（部门维度）时有效。 |
| errmsg | String | 0 | 返回码描述。 |
| errcode | Number | ok | 返回码。 |
| request\_id | String | 1e44yqb6snq1 | 请求ID。 |

## 示例

**请求示例（HTTP）**

```
POST https://oapi.dingtalk.com/topapi/kac/datav/annual_report/get?access_token=ACCESS_TOKEN
```

请求正文

```
{
        "year":"2020",
        "user_id":"user01",
        "type":1,
        "dept_id":"23434"
}
```

**请求示例（JAVA SDK）**

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/kac/datav/annual_report/get");
OapiKacDatavAnnualReportGetRequest req = new OapiKacDatavAnnualReportGetRequest();
req.setYear("2020");
req.setType(1L);
req.setUserId("user01");
req.setDeptId(23434L);
OapiKacDatavAnnualReportGetResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

**返回示例**

```
{
  "result":{
    "isw_msg_click_cnt_1y":"100",
    "use_doc_user_cnt_1y":"100",
    "corp_app_process_inst_cnt_1y":"100",
    "live_join_succ_cnt_1y":"25",
    "send_group_msg_cnt_1y":"100",
    "send_report_cnt_1y":"100",
    "at_me_msg_cnt_1y":"100",
    "inner_group_cnt_1y":"100",
    "send_calendar_cnt_1y":"100",
    "live_join_succ_time_len_1y":"222.32",
    "use_micro_app_cnt_1y":"20",
    "create_smartwork_cnt_1y":"100",
    "send_message_group_cnt_1y":"100",
    "process_inst_submit_cnt_1y":"20",
    "join_succ_voip_conf_user_cnt_1y":"100",
    "use_micro_user_cnt_1y":"500",
    "send_report_user_cnt_1y":"100",
    "create_doc_cnt_1y":"100",
    "start_succ_video_conf_len_1y":"100",
    "avg_process_duration_1y":"100.10",
    "join_group_cnt_1y":"100",
    "send_group_msg_user_cnt_1y":"100",
    "send_ding_user_cnt_1y":"100",
    "join_succ_voip_conf_num_1y":"24",
    "send_group_file_message_cnt_1y":"100",
    "act_usr_days_1y":"100",
    "join_calendar_cnt_1y":"100",
    "general_form_user_cnt_1y":"300",
    "new_group_cnt_1y":"100",
    "recv_ding_cnt_1y":"100",
    "send_ding_cnt_1y":"100",
    "join_succ_video_conf_user_cnt_1y":"100",
    "join_succ_voip_conf_len_1y":"234.51",
    "use_smartwork_cnt_1y":"100",
    "create_process_cnt_1y":"100",
    "process_inst_operate_cnt_1y":"20",
    "join_calendar_user_cnt_1y":"100",
    "at_check_days_1y":"365",
    "join_succ_video_conf_num_1y":"23",
    "outside_days_1y":"100",
    "send_calendar_user_cnt_1y":"100",
    "min_process_duration_1y":"100.10",
    "join_succ_video_conf_len_1y":"340.52",
    "max_step_count_1y":"100"
  },
  "errcode":0,
  "errmsg":"ok",
  "request_id": "1e44yqb6snq1"
}
```
