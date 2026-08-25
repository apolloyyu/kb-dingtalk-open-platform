---
title: "任务中心"
source_url: "https://open.dingtalk.com/document/development/yida-task-center"
namespace: "development"
slug: "yida-task-center"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 宜搭 > 旧版宜搭API参考 > 任务中心"
doc_id: "bxHsfWLOc5"
updated_at: "2025-10-17 12:41:03"
---

> Source: https://open.dingtalk.com/document/development/yida-task-center
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 宜搭 > 旧版宜搭API参考 > 任务中心
> Updated: 2025-10-17 12:41:03

# 任务中心

> **[!IMPORTANT]**
>
> 此旧版宜搭API接口文档已于**2021年10月15日**迁移到**历史文档（不推荐）**目录，已经接入的用户可继续使用，正在准备接入宜搭的用户请查看[宜搭应用开发](https://open.dingtalk.com/document/orgapp/overview-yida)。

## 1. 已提交任务

- 接口: [/yida\_vpc/process/getMySubmmitInCorp.json](https://s-api.alibaba-inc.com/yida_vpc/process/getMySubmmitInCorp.json)
- 参数：

  | 参数 | 描述 | 是否必填 | 示例 | 备注 |
  | --- | --- | --- | --- | --- |
  | corpId | 企业ID | 是 |  |  |
  | limit | 每页记录数 | 是 | 10 | 必须大于0 默认10 最大值：100 |
  | language | 语言环境 | 否 | zh\_CN | 可选值：zh\_CN/en\_US |
  | page | 当前页 | 是 | 1 | 必须大于0 默认1 |
  | keyword | 关键词 | 否 |  |  |
  | appTypes | 应用标识列表 | 否 | ["APP\_xxx","APP\_xxx"] |  |
  | processCodes | 流程code列表 | 否 | ["xx","xxx"] |  |
  | createFrom | 创建时间开始 | 否 |  | 时间戳 |
  | createTo | 创建时间结束 | 否 |  | 时间戳 |
  | userId | 钉钉的userId | 是 |  |  |
  | token | 验权token | 是 |  | md5(corpId + userId + corpToken)，每个企业有自己的唯一codemd5取32位大写值corpToken参数目前该参数未从平台透出，需要的话请联系宜搭值班。 |
- 返回值

  - content : 返回内容;
  - success : 请求是否成功;
  - errorMsg : 错误信息;
  - errorCode : 错误码;
  - errorLevel : 错误级别;
- 返回示例

  ```
  {
     "result":{
        "data":[
           {
              "modifiedTime":"2018-04-12 19:44:14",
              "formInstanceId":"FINST-AJ1L4CJVXL0UIAIPR06ZA52U9HKUXXXXXX",
              "title":"单据",
              "instValue":[
                 {
                    "componentId":"node_jfwgghbo",
                    "componentName":"TextField",
                    "fieldId":"textField_jfwggg8e",
                    "label":"姓名",
                    "validation":[
                       
                    ],
                    "fieldData":{
                       "complexType":"custom",
                       "dataType":"CHANGED",
                       "pass":true,
                       "value":"jack"
                    },
                    "errorMsg":null,
                    "hasError":false
                 }
              ],
              "processId":0,
              "appType":"APP_R8MYLKYXXXXXX",
              "dataMap":{
                 "textField_jfXXXXXX":"XXXXXX"
              },
              "originatorId":"XXXXXX",
              "formUuid":"FORM-0G7KPV3WZL0U3AHTOA9BFVXXXXXX",
              "dataType":"finst",
              "originatorAvatar":"http://static.dingtalk.com/media/lADPBbCc1R7VwSHNXXXXXX.jpg",
              "version":0,
              "createTime":"2018-04-12 19:44:14"
           }
        ],
        "totalCount":1,
        "currentPage":1
     },
     "success":true
  }
  ```

## 2. 待办任务

- 接口: [/yida\_vpc/process/getTodoTasksInCorp.json](https://s-api.alibaba-inc.com/yida_vpc/process/getTodoTasksInCorp.json)
- 参数：

  | 参数 | 描述 | 是否必填 | 示例 | 备注 |
  | --- | --- | --- | --- | --- |
  | corpId | 企业ID | 是 |  |  |
  | limit | 每页记录数 | 是 | 10 | 必须大于0 默认10 最大值：100 |
  | language | 语言环境 | 否 | zh\_CN | 可选值：zh\_CN/en\_US |
  | page | 当前页 | 是 | 1 | 必须大于0 默认1 |
  | keyword | 关键词 | 否 |  |  |
  | appTypes | 应用标识列表 | 否 | ["APP\_xxx","APP\_xxx"] |  |
  | processCodes | 流程code列表 | 否 | ["xx","xxx"] |  |
  | createFrom | 创建时间开始 | 否 |  | 时间戳 |
  | createTo | 创建时间结束 | 否 |  | 时间戳 |
  | userId | 钉钉的userId | 是 |  |  |
  | token | 验权token | 是 |  | md5(corpId + userId + corpToken)，每个企业有自己的唯一codemd5取32位大写值corpToken参数目前该参数未从平台透出，需要的话请联系宜搭值班 |
- 返回值

  - content : 返回内容;
  - success : 请求是否成功;
  - errorMsg : 错误信息;
  - errorCode : 错误码;
  - errorLevel : 错误级别;
- 返回示例

  ```
  {
     "result":{
        "data":[
           {
              "processInstanceId":"XXXXXX",
              "originatorName":"XXX",
              "title":"XXX发起的流程",
              "originatorPhoto":"http://static.dingtalk.com/media/lADPdfafafsAXXXXXX.jpg",
              "titleEn":"XXX发起的流程",
              "createTime":"2018-04-13 13:35:58",
              "appType":"APP_R8MdfadfXXXXXX",
              "originatorNameEn":"XXXXXX",
              "originatorId":"XXXXXX",
              "taskId":"XXXXXX",
              "status":"NEW"
           }
        ],
        "totalCount":1,
        "currentPage":1
     },
     "success":true
  }
  ```

## 3. 已完成任务

- 接口: [/yida\_vpc/process/getDoneTasksInCorp.json](https://s-api.alibaba-inc.com/yida_vpc/process/getDoneTasksInCorp.json)
- 参数：

  | 参数 | 描述 | 是否必填 | 示例 | 备注 |
  | --- | --- | --- | --- | --- |
  | corpId | 企业ID | 是 |  |  |
  | limit | 每页记录数 | 是 | 10 | 必须大于0 默认10 最大值：100 |
  | language | 语言环境 | 否 | zh\_CN | 可选值：zh\_CN/en\_US |
  | page | 当前页 | 是 | 1 | 必须大于0 默认1 |
  | keyword | 关键词 | 否 |  |  |
  | appTypes | 应用标识列表 | 否 | ["APP\_xxx","APP\_xxx"] |  |
  | processCodes | 流程code列表 | 否 | ["xx","xxx"] |  |
  | createFrom | 创建时间开始 | 否 |  | 时间戳 |
  | createTo | 创建时间结束 | 否 |  | 时间戳 |
  | userId | 钉钉的userId | 是 |  |  |
  | token | 验权token | 是 |  | md5(corpId + userId + corpToken)，每个企业有自己的唯一codemd5取32位大写值corpToken参数目前该参数未从平台透出，需要的话请联系宜搭值班。 |
- 返回值

  - content : 返回内容;
  - success : 请求是否成功;
  - errorMsg : 错误信息;
  - errorCode : 错误码;
  - errorLevel : 错误级别;
- 返回示例

  ```
  {
      "result": {
          "data": [{
              "processInstanceId": "abc434rfds23XXXXXX",
              "finishTime": "2018-03-28 17:46:14",
              "originatorName": "",
              "title": "XXX发起的流程页面",
              "originatorPhoto": "//img.alicdn.com/tfs/TB1msdfsXXXXXX.jpg",
              "titleEn": "XXX发起的流程页面",
              "createTime": "2018-03-28 17:45:43",
              "appType": "XXXXXX",
              "originatorNameEn": "XXXXXX",
              "originatorId": "XXXXXX",
              "taskId": "XXXXXX",
              "status": "COMPLETED"
          }],
          "totalCount": 1,
          "currentPage": 1
      },
      "success": true
  }
  ```

## 4. 抄送我的任务（应用纬度）

- 接口: [/yida\_vpc/process/getNotifyMeTasksInApp.json](https://s-api.alibaba-inc.com/yida_vpc/process/getMySubmmitInCorp.json)
- 参数：

  | 参数 | 描述 | 是否必填 | 示例 | 备注 |
  | --- | --- | --- | --- | --- |
  | appType | 应用ID | 是 | APP\_PBKT0MFBEBTDO8T7SLVP |  |
  | systemToken | 验权token | 是 |  |  |
  | limit | 每页记录数 | 是 | 10 | 必须大于0 默认10 最大值：100 |
  | language | 语言环境 | 否 | zh\_CN | 可选值：zh\_CN/en\_US |
  | page | 当前页 | 是 | 1 | 必须大于0 默认1 |
  | keyword | 关键词 | 否 |  |  |
  | userId | 钉钉的userId | 是 |  |  |
  | processCodes | 流程code列表 | 否 | ["xx","xxx"] |  |
  | createFrom | 创建时间开始 | 否 |  | 时间戳 |
  | createTo | 创建时间结束 | 否 |  | 时间戳 |
  | instStatus | 实例状态 | 否 |  | 枚举值 |
- 返回值

  - content : 返回内容;
  - success : 请求是否成功;
  - errorMsg : 错误信息;
  - errorCode : 错误码;
  - errorLevel : 错误级别;
- 返回示例

  ```
  {
      "result": {
          "data": [{
              "modifiedTime": "2018-04-12 19:44:14",
              "formInstanceId": "FINST-AJ1L4CJVXL0UIAIPR06ZA52U9HKUXXXXXX",
              "title": "单据",
              "instValue": [{"componentId":"node_jfwgghbo","componentName":"TextField","fieldId":"textField_jfwggg8e","label":"姓名","validation":[],"fieldData":{"complexType":"custom","dataType":"CHANGED","pass":true,"value":"jack"},"errorMsg":null,"hasError":false}],
              "processId": 0,
              "appType": "APP_R8MYLKYXXXXXX",
              "dataMap": {
                  "textField_jfXXXXXX": "XXXXXX"
              },
              "originatorId": "XXXXXX",
              "formUuid": "FORM-0G7KPV3WZL0U3AHTOA9BFVXXXXXX",
              "dataType": "finst",
              "originatorAvatar": "http://static.dingtalk.com/media/lADPBbCc1R7VwSHNXXXXXX.jpg",
              "version": 0,
              "createTime": "2018-04-12 19:44:14"
          }],
          "totalCount": 1,
          "currentPage": 1
      },
      "success": true
  }
  ```

## 5. 抄送我的任务（企业维度）

- 接口: [/yida\_vpc/process/getNotifyMeInCorp.json](https://s-api.alibaba-inc.com/yida_vpc/process/getMySubmmitInCorp.json)
- 参数：

  | 参数 | 描述 | 是否必填 | 示例 | 备注 |
  | --- | --- | --- | --- | --- |
  | corpId | 企业ID | 是 |  |  |
  | token | 验权token | 是 |  | md5(corpId + userId + code)，每个企业有自己的唯一codemd5取32位大写值 |
  | userId | 钉钉的userId | 是 |  |  |
  | page | 当前页 | 是 | 1 | 必须大于0 默认1 |
  | limit | 每页记录数 | 是 | 10 | 必须大于0 默认10 最大值：100 |
  | language | 语言环境 | 否 | zh\_CN | 可选值：zh\_CN/en\_US |
  | keyword | 表单中组件数据模糊搜 | 否 |  |  |
  | appTypes | 应用标识列表 | 否 | ["APP\_xxx","APP\_xxx"] |  |
  | processCodes | 流程code列表 | 否 | ["xx","xxx"] |  |
  | instanceCreateFrom | 数据提交时间开始 | 否 |  | 时间戳 |
  | instanceCreateTo | 数据提交时间结束 | 否 |  | 时间戳 |
  | createFrom | 抄送到达时间开始 | 否 |  | 时间戳 |
  | createTo | 抄送到达时间结束 | 否 |  | 时间戳 |
- 返回示例

  ```
  {
    "result": {
      "data": [
        {
          "gmtModified": "2019-01-24 19:25:23",
          "creator": "manager55",
          "corpId": "ding5d17e3add038d44535c2f4657eb6378f",
          "title": "小蔡发起的流程",
          "gmtCreate": "2019-01-24 19:25:23",
          "url": "https://www.aliwork.com/alibaba/web/APP_VN7I6HVKUTXES7XX4OI8/inst/carbonDetail.html?formInstId=33f6d221-17f8-42b7-836a-682b95a046c2&activityId=sidJRAJ56IZ2JOFOOPZ2MI7",
          "activityId": "sidJRAJ56IZ2JOFOOPZ2MI7",
          "titleEn": "小蔡（小蔡）发起的流程",
          "processCode": "TPROC--S5VKBWKVB4UVLG1BT5NS6229RVSD2MACIA4IJ7",
          "appType": "APP_VN7I6HVKUTXES7XX4OI8",
          "formInstId": "33f6d221-17f8-42b7-836a-682b95a046c2",
          "mobileUrl": "https://www.aliwork.com/alibaba/mobile/APP_VN7I6HVKUTXES7XX4OI8/inst/detail/carbonDetail?formInstId=33f6d221-17f8-42b7-836a-682b95a046c2&activityId=sidJRAJ56IZ2JOFOOPZ2MI7"
        }
      ],
      "currentPage": 1,
      "totalCount": 1
    },
    "success": true
  }
  ```

## 6. 任务转交

- 接口: /yida\_vpc/task/redirectTask.json
- 参数：

  | 参数 | 描述 | 是否必填 | 示例 | 备注 |
  | --- | --- | --- | --- | --- |
  | appType | 应用ID | 是 | APP\_PBKT0MFBEBTDO8T7SLVP |  |
  | systemToken | 验权token | 是 |  | 在应用数据中获取。 |
  | language | 语言环境 | 否 | zh\_CN | 可选值：zh\_CN/en\_US |
  | processInstanceId | 实例ID | 是 |  |  |
  | byManager | 是否应用管理员进行转交 | 否 | y | 可选项 : y/ny,则userId必须传应用管理员工号，或者yida\_pub\_accountn, userId必须传任务的当前执行人 |
  | userId | 钉钉的userId | 是 |  |  |
  | nowActionerId | 新的任务处理人工号 | 是 |  |  |
  | remark | 转交备注 | 是 |  |  |
  | taskId | 任务ID | 是 |  |  |
- 返回值

  - success : 请求是否成功;
  - errorMsg : 错误信息;
  - errorCode : 错误码;
  - errorLevel : 错误级别;
