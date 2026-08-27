---
title: "批量获取考勤组详情"
source_url: "https://open.dingtalk.com/document/development/batch-obtain-attendance-group-details"
namespace: "development"
slug: "batch-obtain-attendance-group-details"
group: "应用开发"
tab: "服务端API"
breadcrumb: "考勤 > 考勤组管理 > 批量获取考勤组详情"
doc_id: "9xG00GMLmL"
updated_at: "2026-05-27 13:09:51"
---

> Source: https://open.dingtalk.com/document/development/batch-obtain-attendance-group-details
> Path: 应用开发 / 服务端API / 考勤 > 考勤组管理 > 批量获取考勤组详情
> Updated: 2026-05-27 13:09:51

# 批量获取考勤组详情

调用本接口，查询所有的考勤组详情信息。

## **接口调用说明**

在钉钉考勤应用中，考勤组是一类具有相同的班次、考勤位置等考勤规则的人或部门的组合，企业可根据实际业务设置多个考勤组。

> **[!NOTE]**
>
> 本接口与[获取考勤组详情](0174-query-a-single-attendance-group.md)接口的区别，该接口可以获取包含考勤组内的班次设置相关信息。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1547328471/p960289.png)

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/attendance/getsimplegroups |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_base-调用企业API时需要具备的基本权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | bE74xxxx | 调用该API的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 - 第三方企业应用，通过[获取第三方企业的access\_token](1448-obtain-isvapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| offset | Number | 否 | 0 | 支持分页查询，与size参数同时设置时才生效，该参数代表偏移量，偏移量从0开始，下次调用传上次调用时的size与offset之和。 |
| size | Number | 否 | 10 | 分页大小，最大10。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/attendance/getsimplegroups" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=c4a715xxxx0a0da2' \
-d 'offset=0' \
-d 'size=10'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/getsimplegroups");
OapiAttendanceGetsimplegroupsRequest req = new OapiAttendanceGetsimplegroupsRequest();
req.setOffset(0L);
req.setSize(10L);
OapiAttendanceGetsimplegroupsResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiAttendanceGetsimplegroupsRequest("https://oapi.dingtalk.com/topapi/attendance/getsimplegroups")

req.offset=0
req.size=10
try:
  resp= req.getResponse(access_token)
  print(resp)
except Exception,e:
  print(e)
```

PHP

```
include "TopSdk.php";
date_default_timezone_set('Asia/Shanghai');

$c = new DingTalkClient(DingTalkConstant::$CALL_TYPE_OAPI, DingTalkConstant::$METHOD_POST , DingTalkConstant::$FORMAT_JSON);
$req = new OapiAttendanceGetsimplegroupsRequest;
$req->setOffset("0");
$req->setSize("10");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/attendance/getsimplegroups");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/getsimplegroups");
OapiAttendanceGetsimplegroupsRequest req = new OapiAttendanceGetsimplegroupsRequest();
req.Offset = 0L;
req.Size = 10L;
OapiAttendanceGetsimplegroupsResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| request\_id | String | 8pi2725sgame | 请求ID。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| result | AtGroupListForTopVo |  | 返回结果。 |
| has\_more | Boolean | true | 分页用，表示是否有更多数据。   - **true**：有 - **false**：没有 |
| groups | AtGroupForTopVo[] |  | 考勤组列表。 |
| group\_id | Number | 20015047 | 考勤组ID。 |
| is\_default | Boolean | false | 是否是默认考勤组。   - **false**：不是 - **true**：是 |
| group\_name | String | 固定排班 | 考勤组名称。 |
| selected\_class | AtClassVo[] |  | 考勤组对应的考勤班次列表。 |
| enable\_emp\_select\_class | Boolean | true | 未排班时是否允许员工选择班次打卡。   - **true**：允许 - **false**：不允许 |
| disable\_check\_without\_schedule | Boolean | false | 未排班时是否禁止员工打卡。   - **true**：禁止 - **false**：不禁止 |
| disable\_check\_when\_rest | Boolean | true | 休息日打卡是否需审批：   - **true**：需要 - **false**：不需要 |
| setting | ClassSettingVo |  | 考勤组班次配置。 |
| class\_setting\_id | Number | 1 | 考勤组班次ID。 |
| rest\_begin\_time | AtTimeVo |  | 休息开始时间，只有一个时间段的班次有。 |
| check\_time | Date | 2017-04-11 11:11:11 | 开始时间。 |
| permit\_late\_minutes | Number | 10 | 允许迟到时长，单位分钟（-1表示关闭该功能）。 |
| work\_time\_minutes | Number | -1 | 工作时长，单位分钟（-1表示关闭该功能）。 |
| rest\_end\_time | AtTimeVo |  | 休息结束时间，只有一个时间段的班次有。 |
| check\_time | Date | 2017-04-11 11:11:11 | 结束时间。 |
| absenteeism\_late\_minutes | Number | 30 | 旷工迟到时长，单位分钟（-1表示关闭该功能）。 |
| serious\_late\_minutes | Number | 20 | 严重迟到时长，单位分钟（-1表示关闭该功能）。 |
| is\_off\_duty\_free\_check | String | Y | 是否强制下班打卡。   - **Y**：不强制打卡 - **N**：强制打卡 |
| class\_id | Number | 20008010 | 考勤班次ID。 |
| sections | AtSectionVo[] |  | 班次打卡时间段。 |
| times | SetionTimeVO[] |  | 时间段列表。 |
| check\_time | Date | 2017-04-11 11:11:11 | 打卡时间。 |
| check\_type | String | OnDuty | 打卡类型。   - **OnDuty**：上班 - **OffDuty**：下班 |
| across | Number | 0 | 打卡时间跨度。 |
| class\_name | String | A | 考勤班次名称。 |
| type | String | FIXED | 考勤类型。   - **FIXED**为固定排班 - **TURN**为轮班排班 - **NONE**为无班次 |
| member\_count | Number | 1 | 参与考勤人员人数。 |
| default\_class\_id | Number | 111 | 默认班次ID。 |
| work\_day\_list | String[] | ["0","12","12","12","12","12","0"] | 固定班次的工作日班次。  **[!NOTE]**     - 0表示休息。 - 数组内的值，从左到右依次代表周日到周六，每日的排班情况。 |
| classes\_list | String[] | ["周一、二、三、四、五 白班班次 09:00-16:00 ","周六、日 休息"] | 一周的班次时间展示列表。 |
| manager\_list | String[] | ["manager4220"] | 考勤组子负责人。 |
| dept\_name\_list | String[] | ["市场部"] | 参与考勤的部门名称。 |
| owner\_user\_id | String | user456 | 考勤组主负责人。 |

### **响应体示例**

```
{
  "errcode": 0,
  "result": {
    "groups": [
      {
        "group_id": 677765054,
        "group_name": "周末加班",
        "is_default": false,
        "owner_user_id": "user456",
        "manager_list": [
          "manager4220"
        ],
        "member_count": 0,
        "selected_class": [],
        "enable_emp_select_class": true,
        "disable_check_without_schedule": false,
        "disable_check_when_rest": true,
        "type": "NONE",
        "work_day_list": [
          "0",
          "0",
          "0",
          "0",
          "0",
          "0",
          "0"
        ]
      },
      {
        "classes_list": [
          "周一、二、三、四 A 09:30-18:30 ",
          "周五 B 19:00-次日05:00 ",
          "周六、日 休息"
        ],
        "default_class_id": 677995086,
        "dept_name_list": [
          "市场部",
          "技术支持",
          "文档部门"
        ],
        "group_id": 685935028,
        "group_name": "考勤",
        "is_default": false,
        "manager_list": [
          "manager4220"
        ],
        "member_count": 3,
        "selected_class": [
          {
            "class_id": 677995086,
            "class_name": "A",
            "sections": [
              {
                "times": [
                  {
                    "across": 0,
                    "check_time": "1970-01-01 09:30:00",
                    "check_type": "OnDuty"
                  },
                  {
                    "across": 0,
                    "check_time": "1970-01-01 18:30:00",
                    "check_type": "OffDuty"
                  }
                ]
              }
            ],
            "setting": {
              "absenteeism_late_minutes": -1,
              "class_setting_id": 588655171,
              "is_off_duty_free_check": "N",
              "permit_late_minutes": -1,
              "serious_late_minutes": -1,
              "work_time_minutes": 540
            }
          },
          {
            "class_id": 678215070,
            "class_name": "B",
            "sections": [
              {
                "times": [
                  {
                    "across": 0,
                    "check_time": "1970-01-01 19:00:00",
                    "check_type": "OnDuty"
                  },
                  {
                    "across": 1,
                    "check_time": "1970-01-01 05:00:00",
                    "check_type": "OffDuty"
                  }
                ]
              }
            ],
            "setting": {
              "absenteeism_late_minutes": -1,
              "class_setting_id": 586985140,
              "is_off_duty_free_check": "N",
              "permit_late_minutes": 0,
              "serious_late_minutes": -1,
              "work_time_minutes": 600
                        }
                    }
                ],
                "type": "FIXED",
                "work_day_list": [
                    "0",
                    "677995086",
                    "677995086",
                    "677995086",
                    "677995086",
                    "678215070",
                    "0"
                ],
                "enable_emp_select_class": true,
                "disable_check_without_schedule": false,
                "disable_check_when_rest": true
            }
        ],
        "has_more": false
    },
    "request_id": "8pi2725sgame"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
