---
title: "发起审批实例"
source_url: "https://open.dingtalk.com/document/development/oa-approval-initiates-approval-instances"
namespace: "development"
slug: "oa-approval-initiates-approval-instances"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > OA审批 > 发起审批实例"
doc_id: "Ux5oJcLPwl"
updated_at: "2025-12-05 19:25:32"
---

> Source: https://open.dingtalk.com/document/development/oa-approval-initiates-approval-instances
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > OA审批 > 发起审批实例
> Updated: 2025-12-05 19:25:32

# 发起审批实例

调用本接口发起一个审批。

> **[!IMPORTANT]**
>
> 为提升接口使用体验，针对OA审批相关接口规范进行升级，从[旧版升级到新版](https://open.dingtalk.com/document/orgapp/differences-between-server-apis-and-new-server-apis)。本文旧版规范接口文档已于2022年10月8日迁移至历史文档（不推荐）目录，且本接口仅保持现有功能，不再新增支持其他能力。
>
> - 如果未使用本接口，推荐使用新版规范[发起审批实例](https://open.dingtalk.com/document/orgapp/create-an-approval-instance)接口。
> - 如果已使用本接口，建议您根据自身实际情况评估是否切换至推荐接口。

> **[!IMPORTANT]**
>
> 发起审批实例后，无法通过API修改审批实例信息。

发起审批实例后，审批人可以通过**OA审批-待处理的**和**待办-我的待办**进行查看。

OA审批-待处理查看审批实例，如下图所示。![待处理审批 ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9681796361/p352397.png)

待办-我的待办查看审批实例，如下图所示。![待办审批](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0885696361/p352386.png)

根据是否指定审批人，发起审批实例有2种方式：

- 指定审批人

  调用接口时，通过**approvers**或**approvers\_v2**参数指定审批人。其中，**approvers\_v2**支持或签和会签。

  > **[!NOTE]**
  >
  > 指定审批人方式，不支持审批模板的高级设置，比如手写签名、表单操作权限等均无法使用等。
- 不指定审批人，复用审批后台设置的审批流程

  > **[!NOTE]**
  >
  > 复用审批后台设置的审批流程时，**cc\_list**和**cc\_position**参数**不生效**，会复用审批后台设置的抄送人员。

  调用接口时，不传入**approvers**或**approvers\_v2**参数，会自动复用在[审批管理后台](https://aflow.dingtalk.com/dingtalk/web/query/dashboard?dinghash=aflowSetting#/aflowSetting)预设的审批人，如下图所示：

  ![审批流 ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4734199951/p162108.png)

## 权限

服务端API是以应用维度授权的，在调用接口前，确保已经为应用添加了接口权限。

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 是 | 开发者后台申请 | **[!IMPORTANT]**  暂不支持新增申请。 |
| 第三方企业应用 | 是 | 开发者后台申请 | **[!IMPORTANT]**  暂不支持新增申请。 |
| 第三方个人应用 | 否 | — | — |

## 基本信息

**请求方式**：POST

**请求地址**：`https://oapi.dingtalk.com/topapi/processinstance/create`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用服务端API的应用凭证。   - 企业内部应用可通过[获取企业内部应用的access\_token](https://open.dingtalk.com/document/orgapp/obtain-orgapp-token)接口获取 - 第三方企业应用可通[获取第三方应用授权企业的access\_token](https://open.dingtalk.com/document/isvapp/obtains-the-enterprise-authorized-credential) |

## Body参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| agent\_id | Number | 否 | 41605932 | 应用标识。可在开发者后台的应用详情页获取。  **[!IMPORTANT]**  如果是第三方企业应用必须指定该参数。 |
| process\_code | String | 是 | PROC-EF6YJL35P2xxxx | 审批流的唯一码。  process\_code在审批模板编辑页面的URL中获取。 |
| originator\_user\_id | String | 是 | manager432 | 审批实例发起人的userid。 |
| dept\_id | Number | 是 | 100 | 发起人所在的部门，如果发起人属于根部门，传-1。 |
| approvers | String | 否 | manager01, manager02 | 审批人userid列表，最大列表长度20。  多个审批人用逗号分隔，按传入的顺序依次审批。 |
| approvers\_v2 | ProcessInstanceApproverVo[] | 否 |  | 审批人列表，最大列表长度20。  支持会签/或签，优先级高于approvers变量。 |
| task\_action\_type | String | 否 | AND | 审批类型：   - **会签**：AND - **或签**：OR - **单人**：NONE |
| user\_ids | String[] | 否 | []user1,user2 | 审批人userid列表：   - 会签/或签列表长度必须大于1 - 非会签/或签列表长度只能为1   最大列表长度20。 |
| cc\_list | String | 否 | user2,user3 | 抄送人userid列表，最大列表长度20。  **[!NOTE]**  该参数需要与approvers或approvers\_v2参数一起传，抄送人才会生效。 |
| cc\_position | String | 否 | START | 在什么节点抄送给抄送人：   - **START** - **FINISH** - **START\_FINISH** |
| form\_component\_values | FormComponentValueVo[] | 是 |  | 审批流表单参数，最大列表长度200。  仅支持下表列举的表单控件。  **[!NOTE]**     - 明细内组件个数上限是200个。 - 明细内使用的联系人组件上限是50个，过多使用联系人组件会导致超时。 |
| name | String | 是 | 请假类型 | 表单每一栏的名称。 |
| value | String | 是 | 事假 | 表单每一栏的值。   - 单行输入框内的值，使用建议不超过1000个字符。 - 多行输入框内的值，使用建议不超过8000个字符。 |
| ext\_value | String | 否 | 总天数:1 | 扩展值。 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| request\_id | String | rj8u1oqx0hi6 | 请求ID。 |
| process\_instance\_id | String | 7fc61e3e-7282-xxxx | 审批实例ID。 |

## 示例

**请求示例（HTTP）**

```
POST https://oapi.dingtalk.com/topapi/processinstance/create?access_token=ACCESS_TOKEN
```

请求正文

```
{
    "form_component_values": [
        {
            "name": "单行输入框",
            "value": "测试单行输入框"
        },
        {
            "name": "多行输入框",
            "value": "测试多行输入框"
        },
        {
            "name": "金额（元）大写",
            "value": "1"
        },
        {
            "name": "数字输入框",
            "value": "100"
        },
        {
            "name": "单选框",
            "value": "a"
        },
        {
            "name": "多选框",
            "value": "[\"a\",\"b\"]"
        }, 
        {
            "name": "日期",
            "value": "2021-08-17"
        },
        {
            "name": "[\"开始时间\",\"结束时间\"]",
            "value": "[\"2019-02-19\",\"2019-02-25\"]"
        },
        {
            "name": "图片",
            "value": ["http://url1","http://url2","http://url3"]
        },
        {
            "name": "附件",
            "value": [{"spaceId": "163xxxx658", "fileName": "2644.JPG", "fileSize": "333", "fileType": "jpg", "fileId": "643xxxx140"}]
        },
        {
            "name": "联系人",
            "value": "[\"4525xxxxxxxx77041\"]"
        },
        {
            "name":"关联审批单",
            "value":[
                "fa2aa864-xxxx-xxxx-xxxx-75572c0e2cdf",
                "7125778e-xxxx-xxxx-xxxx-faa987478a9b"
                
            ]
        },
        {
            "name": "明细",
            "value": [
                [
                    {
                        "name":"单行输入框",
                        "value":"明细单行输入框"
                    },
                    {
                        "name":"数字输入框",
                        "value":"100"
                    }
                    
                ]
            ]
        }
        
        
    ],
    "agent_id": 115xxxx211,
    "process_code": "PROC-37801FB3-xxxx-xxxx-xxxx-6C6ADB87CD9A",
    "cc_position": "FINISH",
    // "approvers": "4525xxxxxxxx77041,2643xxxxxxx69379",
    "cc_list": "4525xxxxxxxx77041",
    "dept_id": 70041378,
    "approvers_v2": [      //设置审批人，会签、或签设置的审批人必须大于等于2个人
         {
            "task_action_type": "AND",
            "user_ids": [
                "4525xxxxxxxx77041",
                "2643xxxxxxx69379"
            ]
        },
        {
            "task_action_type": "OR",
            "user_ids": [
                "4525xxxxxxxx77041",
                "2643xxxxxxx69379"
            ]
        }
       
    ],
    "originator_user_id": "4525xxxxxxxx77041"
}
```

**请求示例（JAVA SDK）**

```
   DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/processinstance/create");
        OapiProcessinstanceCreateRequest req = new OapiProcessinstanceCreateRequest();
        req.setAgentId(115xxxx211L);
        req.setProcessCode("PROC-37801FB3-xxxx-xxxx-xxxx-6C6ADB87CD9A");
        req.setOriginatorUserId("4525xxxxxxxx77041");
        req.setDeptId(70xxxx78L);
        req.setCcList("4525xxxxxxxx77041");
        req.setCcPosition("FINISH");

        //单行输入框
        List<OapiProcessinstanceCreateRequest.FormComponentValueVo> formComponentValueVoList = new ArrayList<OapiProcessinstanceCreateRequest.FormComponentValueVo>();
        OapiProcessinstanceCreateRequest.FormComponentValueVo formComponentValueVo = new OapiProcessinstanceCreateRequest.FormComponentValueVo();
        formComponentValueVoList.add(formComponentValueVo);
        formComponentValueVo.setName("单行输入框");
        formComponentValueVo.setValue("测试单行输入框");

        //多行输入框
        OapiProcessinstanceCreateRequest.FormComponentValueVo formComponentValueVo1 = new OapiProcessinstanceCreateRequest.FormComponentValueVo();
        formComponentValueVoList.add(formComponentValueVo1);
        formComponentValueVo1.setName("多行输入框");
        formComponentValueVo1.setValue("测试多行输入框");

        //金额输入框
        OapiProcessinstanceCreateRequest.FormComponentValueVo formComponentValueVo2 = new OapiProcessinstanceCreateRequest.FormComponentValueVo();
        formComponentValueVoList.add(formComponentValueVo2);
        formComponentValueVo2.setName("金额（元）大写");
        formComponentValueVo2.setValue("1");

        //数字输入框
        OapiProcessinstanceCreateRequest.FormComponentValueVo formComponentValueVo3 = new OapiProcessinstanceCreateRequest.FormComponentValueVo();
        formComponentValueVoList.add(formComponentValueVo3);
        formComponentValueVo3.setName("数字输入框");
        formComponentValueVo3.setValue("100");

        //单选框组件
        OapiProcessinstanceCreateRequest.FormComponentValueVo formComponentValueVo5 = new OapiProcessinstanceCreateRequest.FormComponentValueVo();
        formComponentValueVoList.add(formComponentValueVo5);
        formComponentValueVo5.setName("单选框");
        formComponentValueVo5.setValue("a");

        //多选框组件
        OapiProcessinstanceCreateRequest.FormComponentValueVo formComponentValueVo6 = new OapiProcessinstanceCreateRequest.FormComponentValueVo();
        formComponentValueVoList.add(formComponentValueVo6);
        formComponentValueVo6.setName("多选框");
        formComponentValueVo6.setValue("[\"a\",\"b\"]");

        //日期组件
        OapiProcessinstanceCreateRequest.FormComponentValueVo formComponentValueVo7 = new OapiProcessinstanceCreateRequest.FormComponentValueVo();
        formComponentValueVoList.add(formComponentValueVo7);
        formComponentValueVo7.setName("日期");
        formComponentValueVo7.setValue("2021-08-17");

        //日期区间组件
        OapiProcessinstanceCreateRequest.FormComponentValueVo formComponentValueVo8 = new OapiProcessinstanceCreateRequest.FormComponentValueVo();
        formComponentValueVoList.add(formComponentValueVo8);
        formComponentValueVo8.setName("[\"开始时间\",\"结束时间\"]");
        formComponentValueVo8.setValue("[\"2019-02-19\",\"2019-02-25\"]");

        //上传图片
        OapiProcessinstanceCreateRequest.FormComponentValueVo formComponentValueVo9 = new OapiProcessinstanceCreateRequest.FormComponentValueVo();
        formComponentValueVoList.add(formComponentValueVo9);
        formComponentValueVo9.setName("图片");
        formComponentValueVo9.setValue(JSON.toJSONString(new String[]{"https://xxxxxxxx", "https://xxxxxxxxx"}));

        //上传审批附件
        OapiProcessinstanceCreateRequest.FormComponentValueVo formComponentValueVo10 = new OapiProcessinstanceCreateRequest.FormComponentValueVo();
        formComponentValueVoList.add(formComponentValueVo10);
        JSONObject jsonObject = new JSONObject();
        jsonObject.put("spaceId", "163xxxx658");
        jsonObject.put("fileName", "IMG_2322.PNG");
        jsonObject.put("fileSize", "276297");
        jsonObject.put("fileType", "png");
        jsonObject.put("fileId", "405xxxxx777");
        Object o[] = new Object[]{jsonObject};
        String s = JSON.toJSONString(o);
        formComponentValueVo10.setName("附件");
        formComponentValueVo10.setValue(s);

        //联系人
        OapiProcessinstanceCreateRequest.FormComponentValueVo formComponentValueVo11 = new OapiProcessinstanceCreateRequest.FormComponentValueVo();
        formComponentValueVoList.add(formComponentValueVo11);
        formComponentValueVo11.setName("联系人");
        formComponentValueVo11.setValue("[\"4525xxxxxxxx77041\"]");

        //明细
        OapiProcessinstanceCreateRequest.FormComponentValueVo formComponentValueVo12 = new OapiProcessinstanceCreateRequest.FormComponentValueVo();
        OapiProcessinstanceCreateRequest.FormComponentValueVo Item1 = new OapiProcessinstanceCreateRequest.FormComponentValueVo();
        Item1.setName("单行输入框");
        Item1.setValue("明细单行输入框");
        OapiProcessinstanceCreateRequest.FormComponentValueVo Item2 = new OapiProcessinstanceCreateRequest.FormComponentValueVo();
        Item2.setName("数字输入框");
        Item2.setValue("100");
        formComponentValueVo12.setName("明细");
        formComponentValueVo12.setValue(JSON.toJSONString(Arrays.asList(Arrays.asList(Item1, Item2))));
        formComponentValueVoList.add(formComponentValueVo12);

        //关联审批单
        OapiProcessinstanceCreateRequest.FormComponentValueVo formComponentValueVo13 = new OapiProcessinstanceCreateRequest.FormComponentValueVo();
        formComponentValueVoList.add(formComponentValueVo13);
        formComponentValueVo13.setName("关联审批单");
        formComponentValueVo13.setValue(JSON.toJSONString(Arrays.asList("fa2aa864-xxxx-xxxx-xxxx-75572c0e2cdf")));

        //设置审批人，会签、或签设置的审批人必须大于等于2个人
        List<OapiProcessinstanceCreateRequest.ProcessInstanceApproverVo> processInstanceApproverVoList = new ArrayList<OapiProcessinstanceCreateRequest.ProcessInstanceApproverVo>();
        OapiProcessinstanceCreateRequest.ProcessInstanceApproverVo processInstanceApproverVo = new OapiProcessinstanceCreateRequest.ProcessInstanceApproverVo();
        processInstanceApproverVoList.add(processInstanceApproverVo);
        processInstanceApproverVo.setTaskActionType("AND");
        processInstanceApproverVo.setUserIds(Arrays.asList("4525xxxxxxxx77041","2643xxxxxxx69379"));
        OapiProcessinstanceCreateRequest.ProcessInstanceApproverVo processInstanceApproverVo1 = new OapiProcessinstanceCreateRequest.ProcessInstanceApproverVo();
        processInstanceApproverVoList.add(processInstanceApproverVo1);
        processInstanceApproverVo1.setTaskActionType("OR");
        processInstanceApproverVo1.setUserIds(Arrays.asList("4525xxxxxxxx77041","2643xxxxxxx69379"));
        req.setApproversV2(processInstanceApproverVoList);

        req.setFormComponentValues(formComponentValueVoList);
        OapiProcessinstanceCreateResponse rsp = client.execute(req, AccessToken);
        System.out.println(JSON.toJSONString(rsp));
```

**返回示例**

```
{
    "errcode": 0,
    "process_instance_id": "7fc61e3e-7282-xxxx",
    "errmsg":"ok",
    "request_id": "rj8u1oqx0hi6",
}
```

## 多级审批人设置

在一些比较复杂的审批场景中，如果单独使用**approvers**设置审批人往往不能满足实际需求，此时就需要使用**approver\_v2**参数。参数**approver\_v2**支持多级审批，其使用的代码示例如下：

```
// ApproverV2 表单审批开始
List<ProcessInstanceApproverVo> processInstanceApproverVoList = new ArrayList<>();

// 1.配置第一个节点，两个审批人会签
ProcessInstanceApproverVo approverVo1 = new ProcessInstanceApproverVo();
processInstanceApproverVoList.add(approverVo1);
approverVo1.setTaskActionType("AND");
approverVo1.setUserIds(Arrays.asList("user123","user456"));
System.out.println("第一个节点，两个审批人会签");
System.out.println(JSON.toJSONString(processInstanceApproverVoList,true));

// 2.配置第二个节点，两个审批人或签
ProcessInstanceApproverVo approverVo2 = new ProcessInstanceApproverVo();
processInstanceApproverVoList.add(approverVo2);
approverVo2.setTaskActionType("OR");
approverVo2.setUserIds(Arrays.asList("manager123","manager456"));
System.out.println("第二个节点，两个审批人或签");
System.out.println(JSON.toJSONString(processInstanceApproverVoList,true));
request.setApproversV2(processInstanceApproverVoList);
```

## 支持的表单控件

表单控件采用key/value的形式，其中key是每个控件对应的名称，value可以是普通字符串，也可以是json字符串。发起审批实例接口支持使用以下表单控件。

| 控件 | 使用说明 |
| --- | --- |
| 附件 | value是一个数组，可以传多个文件或图片，格式如下：   ``` [     {         "spaceId":"1635477658",         "fileName":"2644.JPG",         "fileSize":"333",         "fileType":"jpg",         "fileId":"6433971140"     } ] ```   开发者必须通过以下步骤才可获取附件相关参数，且必须在钉钉客户端内调用：   1. 调用[获取审批钉盘空间信息](https://open.dingtalk.com/document/orgapp/query-the-space-of-an-approval-nail)，获取spaceId。 2. 上传文件到步骤一的spaceId对应的钉盘空间，获取fileId、fileName、fileSize及fileType参数，以下两种方式均可获取，且都需要在钉钉客户端下进行：     - **推荐使用：**调用H5微应用[上传附件到钉盘/从钉盘选择文件](https://open.dingtalk.com/document/orgapp/upload-attachment-to-nail-plate-select-file-from-nail-plate-h5)或者小程序[上传附件到钉盘/从钉盘选择文件](https://open.dingtalk.com/document/orgapp/upload-attachment-to-nail-plate-select-file-from-nail-plate)。    - 调用服务端API[保存文件到自定义或审批钉盘空间](https://open.dingtalk.com/document/orgapp/add-file-to-user-s-dingtalk-disk)，上传钉盘文件。 |
| 输入框 | value是普通字符串。 |
| 图片 | value是json数组，每个数组元素必须为图片的URL。例如：   ``` ["http://url1","http://url2","http://url3"] ```   **[!IMPORTANT]**    图片组件的value值内一次性最多支持9张图片，否则会报错**审批表单组件格式错误。** |
| 明细 | 明细控件内部只能由**输入框控件**和**图片控件**组成，value格式如下：   ``` [    [       {          "name":"单行输入框",          "value":"单行输入框内容"       },       {          "name":"多行输入框",          "value":"多行输入框内容"       }    ] ] ``` |
| 金额/数字/计算公式 | value是数字。 |
| 单选框 | value是字符串，必须是在审批模板设计时预设值的单选框的值。 |
| 多选框 | value是字符串数组，数组里的每个元素必须是模板里预设的值，格式如下：   ``` {       "name": "多选框",       "value": "[\"a\",\"b\"]" } ``` |
| 日期 | value是字符串，根据日期类型来传值，分别为“yyyy-mm-dd hh:mm” 和“yyyy-mm-dd”。 |
| 日期区间 | name是一个数组，value也是对应数组，格式如下：   ``` {       "name": "[\"开始时间\",\"结束时间\"]",       "value": "[\"2019-02-19\",\"2019-02-25\"]" } ``` |
| 联系人 | value为企业用户UserID列表，格式如下：   ``` {       "name": "联系人",       "value": "[\"userid1\",\"userid2\"]" } ``` |
| 关联审批单 | value为审批实例ID数组，格式如下：   ``` [    {       "name":"关联审批单",       "value":[          "9d38735a-56bd-4d9d-9bb5-b12cce3c25ab"       ]    } ] ```   **[!IMPORTANT]**    关联审批单组件的value值内一次性最多支持9个实例id，并且要确保每一个实例id值都是真实存在的，否则会报错**审批表单组件格式错误。** |
