---
title: "常见问题"
source_url: "https://open.dingtalk.com/document/development/attendance-interface-common-problems"
namespace: "development"
slug: "attendance-interface-common-problems"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "考勤 > 常见问题"
doc_id: "G3x9HMVzyY"
updated_at: "2025-09-10 19:29:39"
---

> Source: https://open.dingtalk.com/document/development/attendance-interface-common-problems
> Path: 应用开发 / 服务端 API / 考勤 > 常见问题
> Updated: 2025-09-10 19:29:39

# 常见问题

本文介绍了调用钉钉服务端考勤接口时的常见错误。

## **考勤打卡类**

### **缺卡、不在考勤班次范围内的打卡（无效打卡）与旷工记录何时生成？**

答：记录生成时间如下：

- 无效打卡：实时生成。

  - 旷工记录：旷工记录是计算出来的状态，如果一整天都缺卡则为旷工。
  - 缺卡场景：例如某企业正常工作日班次是09-18点。
- 若未设置打卡时段：

  - 上班考勤结果生成：会按中线生成缺卡，即:（9+18）/ 2 =13.5，即13时30分。
  - 下班考勤结果生成：

    - 次日为工作日时：按两个卡点的中线计算[遵循前8后12规则]，即（18 + 9） /2=13.5，即凌晨01：30。
    - 次日为休息日时：系统会扩大最晚打卡时间，[遵循前8后12规则]，会在12小时后生成考勤结果。
- 设置打卡时段：依据设置的最晚打卡时间生成考勤结果。

### **获取打卡结果，接口返回为空**

答：调用[获取打卡结果](0195-open-attendance-clock-in-data.md)接口返回的信息为空的可能原因包括但不限于以下情况：

- 参数userId值有误，请确认当前企业下是否有该userid。
- isI18n(判断海外企业)参数有误。如果是国内企业，isI18n参数必须传false。
- 检查checkDateFrom，若用户打卡时间点是09:00，调用接口时参数传10:00，获取不到信息。
- userIdList参数的格式不正确。多个userid需用英文逗号隔开。

### **上传打卡记录接口返回成功，OA后台查看未生效**

答：调用[上传打卡记录](0197-upload-punch-records.md)接口返回成功，但在企业OA后台考勤信息统计中未查到，请检查接口参数user\_check\_time值是否为13位毫秒单位时间戳。

### **调用获取打卡结果接口，返回空{"errcode":0,"hasMore":false,"errmsg":"ok","recordresult":[]}**

答：调用[获取打卡结果](0195-open-attendance-clock-in-data.md)时，接口返回的信息为空，请依次确认以下情况：

- 检查接口参数userId值是否正确，使用获取打卡接口接口的accessToken值调用[查询用户详情](0056-query-user-details.md)接口，如果接口返回“userId不存在”，说明userId值不正确。
- 检查isI18n参数，如果是国内企业，isI18n参数必须传false，如果传了true获取不到考勤信息。
- 检查userIdList参数的格式是否正确。

### **调用获取打卡详情接口，返回空{"errcode":0,"errmsg":"ok","recordresult":[]}**

答：调用[获取打卡详情](0196-attendance-clock-in-record-is-open.md)时，接口返回的信息为空，请依次确认以下情况：

- 检查接口参数userId值是否正确，使用获取打卡接口接口的accessToken值调用[查询用户详情](0056-query-user-details.md)接口，如果接口返回“userId不存在”，说明userId值不正确。
- 检查checkDateFrom参数，如果用户打卡时间点是09:00，调用接口时参数传10:00，获取不到信息。
- 检查isI18n参数，如果是国内企业，isI18n参数必须传false，如果传了true获取不到考勤信息。
- 检查userIdList参数的格式是否正确。

## **考勤统计类**

### **获取考勤报表列值，返回的应出勤天数为0**

答：应出勤天数字段，目前只支持获取距今15天内的值。

### **调用获取考勤报表列值接口报错{errcode:850015,errmsg:系统异常，请稍后重试}**

答：调用[获取考勤报表列值](0219-queries-the-column-value-of-the-attendance-report.md)接口报上述错误时，请依次确认以下情况：

- 检查参数column\_id\_list的格式，String类型，多个id用","分割(示例："id1,id2,id3")。
- 检查参数column\_id\_list内的值，是否来自[获取考勤报表列定义](0218-queries-the-enterprise-attendance-report-column.md)接口返回的报表列ID值，而非expression\_id字段。

### **调用获取考勤报表列值接口，返回系统异常{errcode:850015,errmsg:系统异常，请稍后重试,request\_id:woae9xpid4xi}**

答：调用[获取考勤报表列值](0219-queries-the-column-value-of-the-attendance-report.md)时，接口返回系统异常，请依次确认以下情况：

- 检查参数column\_id\_list的格式，String类型，多个id用","分割。示例："id1,ide2,id3"
- 检查参数column\_id\_list内的值，是否来自[获取考勤报表列定义](0218-queries-the-enterprise-attendance-report-column.md)接口返回的id值，非expression\_id字段

### **调用获取考勤报表列值接口，应出勤天数字段value有0的情况**

答：调用[获取考勤报表列值](0219-queries-the-column-value-of-the-attendance-report.md)时，接口返回的信息中应**出勤天数**值为0的情况，如下所示：

```
 {
      "date":"2021-12-27 00:00:00",
      "value":"1.0"
     },
     {
      "date":"2021-12-28 00:00:00",
      "value":"1.0"
     },
     {
      "date":"2021-12-29 00:00:00",
       
"value":"0.0" 

     },
     {
      "date":"2021-12-30 00:00:00",
       
"value":"0.0" 

     },
     {
      "date":"2021-12-31 00:00:00",
       
"value":"0.0" 

     }
```

解决方案：应出勤天数字段，目前只支持获取距今15天内的值。

## **考勤统计类**

### **调用获取用户考勤数据接口，返回信息为空**

答：调用[获取用户考勤数据](0216-obtain-the-attendance-update-data.md)时，接口返回的信息为空，如下所示：

```
{
    "errcode":0,
    "result":{
        "approve_list":[],
        "attendance_result_list":[],
        "check_record_list":[],
        "corpId":"ding027f45xxxxxxxxx",
        "userid":"002",
        "work_date":"2021-12-13 14:00:00"
        },
        "success":true,
        "request_id":"h21upm1yem14"
}
```

解决方案：检查接口参数userId值是否正确，使用获取打卡接口接口的accessToken值调用[查询用户详情](0056-query-user-details.md)接口，如果接口返回“userId不存在”，说明userId值不正确。
