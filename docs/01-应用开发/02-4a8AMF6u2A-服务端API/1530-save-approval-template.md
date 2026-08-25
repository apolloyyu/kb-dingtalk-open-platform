---
title: "创建或更新审批模板"
source_url: "https://open.dingtalk.com/document/development/save-approval-template"
namespace: "development"
slug: "save-approval-template"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > OA审批 > 创建或更新审批模板"
doc_id: "VVsKKZHtS8"
updated_at: "2026-08-25 09:37:52"
---

> Source: https://open.dingtalk.com/document/development/save-approval-template
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > OA审批 > 创建或更新审批模板
> Updated: 2026-08-25 09:37:52

# 创建或更新审批模板

调用本接口创建或更新审批模板。

> **[!IMPORTANT]**
>
> - 本接口已完成升级，后续将维持现有功能且不再新增能力。
> - 未接入的开发者建议使用新版[创建或更新审批模板](0510-create-orupdate-the-approval-template-new.md)接口，已接入用户不受影响。

## **接口说明**

- 每个企业最多创建200个自有审批模板，超过最大数量后调用接口会报错。
- 钉钉客户端展示审批列表时，仅展示模板表单的前三个选项。
- 调用该接口创建的自有审批流模板，使用的**模板名称**和接口返回的**process\_code**值，请务必注意保存，方便后续调用其他接口使用。
- 自有OA审批模板仅支持文档下方所展示的审批组件，其他组件均不支持。

## 权限

服务端API是以应用维度授权的，在调用接口前，确保已经为应用添加了接口权限。

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 是 | **[!NOTE]**  不支持新增 | — |
| 第三方企业应用 | 是 | — |
| 第三方个人应用 | 否 | — |

## 基本信息

**请求方式**：POST

**请求地址**：`https://oapi.dingtalk.com/topapi/process/save`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用该接口的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](1444-obtain-orgapp-token.md)接口获取。 - 第三方企业应用，通过[服务商获取第三方应用授权企业的access\_token](1446-obtain-isvapp-token.md)接口获取。 |

## Body参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| saveProcessRequest | SaveProcessRequest | 是 |  | 审批模板信息。 |
| agentid | Number | 是 | 123 | 应用标识。可在开发者后台的应用详情页获取。 |
| process\_code | String | 否 | PROC-EF6YJL35P2xxxx | 审批流的唯一码。  **[!NOTE]**   - 如果该参数没有赋值，表示新建一个模板。 - 如果赋值，表示更新所传值对应的审批模板。 |
| name | String | 是 | 请假 | 审批模板名称。 |
| description | String | 是 | 特殊请假流程 | 审批模板描述。 |
| form\_component\_list | FormComponentVo[] | 是 |  | 表单列表。 |
| component\_name | String | 是 | TextField | 表单名称。每种表单组件的component\_name是固定的。表单组件的props里的id，必须在模板里唯一，可以有两段字符串组成，第一段为表单的component\_name；第二段为8位随机字符串。  **[!NOTE]**  只支持下表中的表单，不支持其他值。 |
| props | FormComponentPropVo | 是 |  | 表单属性。 |
| id | String | 是 | TextField-78Fxxxx | 表单ID，最大不能超过22个字符。 |
| label | String | 是 | 单行输入框 | 表单名称。 |
| required | Boolean | 否 | true | 是否必填：   - **true**：是 - **false**：否。 |
| fake\_mode | Boolean | 否 | true | 是否配置流程。  **[!IMPORTANT]**  必须传**true**，表示不带流程的审批模板。 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| request\_id | String | 5av7ifh2atw0 | 请求ID。 |
| errmsg | String | 成功 | 返回码描述。 |
| errcode | Number | 0 | 返回码。 |
| result | ProcessTopVo |  | 创建接口。 |
| process\_code | String | PROC-CODE | 审批模板唯一码。 |

## 示例

**请求示例（HTTP）**

```
POST https://oapi.dingtalk.com/topapi/process/save?access_token=ACCESS_TOKEN
```

请求正文

```
{
  "saveProcessRequest":{
    "name":"自定义审批2",
    "form_component_list":{
      "component_name":"TextField",
      "props":{
        "id":"TextField-J78F056R",
        "label":"单行输入框"
      }
    }
  }
}
```

**请求示例（JAVA SDK）**

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/process/save");

OapiProcessSaveRequest request = new OapiProcessSaveRequest();
OapiProcessSaveRequest.SaveProcessRequest saveProcessRequest = new OapiProcessSaveRequest.SaveProcessRequest();
saveProcessRequest.setDisableFormEdit(true);
saveProcessRequest.setName("test2.0");
saveProcessRequest.setProcessCode("PROC-BE7FC6B2-E95B-45CA-AD9A-A62819EDA2FE");
saveProcessRequest.setAgentid(260536001L);
saveProcessRequest.setFakeMode(true);

// 注意，每种表单组件，对应的componentName是固定的，参照以下示例代码
List<FormComponentVo> formComponentList = Lists.newArrayList();

// 单行文本框
OapiProcessSaveRequest.FormComponentVo singleInput = new OapiProcessSaveRequest.FormComponentVo();
singleInput.setComponentName("TextField");
OapiProcessSaveRequest.FormComponentPropVo singleInputProp = new OapiProcessSaveRequest.FormComponentPropVo();
singleInputProp.setRequired(true);
singleInputProp.setLabel("单行输入框");
singleInputProp.setPlaceholder("请输入");
singleInputProp.setId("TextField-J78F056R");
singleInput.setProps(singleInputProp);
formComponentList.add(singleInput);

// 多行文本框
OapiProcessSaveRequest.FormComponentVo multipleInput = new OapiProcessSaveRequest.FormComponentVo();
multipleInput.setComponentName("TextareaField");
OapiProcessSaveRequest.FormComponentPropVo multipleInputProp = new OapiProcessSaveRequest.FormComponentPropVo();
multipleInputProp.setRequired(true);
multipleInputProp.setLabel("多行输入框");
multipleInputProp.setPlaceholder("请输入");
multipleInputProp.setId("TextareaField-J78F056S");
multipleInput.setProps(multipleInputProp);
formComponentList.add(multipleInput);

// 金额组件
OapiProcessSaveRequest.FormComponentVo moneyComponent = new OapiProcessSaveRequest.FormComponentVo();
moneyComponent.setComponentName("MoneyField");
OapiProcessSaveRequest.FormComponentPropVo moneyComponentProp = new OapiProcessSaveRequest.FormComponentPropVo();
moneyComponentProp.setRequired(true);
moneyComponentProp.setLabel("金额（元）大写");
moneyComponentProp.setPlaceholder("请输入");
moneyComponentProp.setId("MoneyField-J78F0571");
moneyComponentProp.setNotUpper("1"); // 是否禁用大写
moneyComponent.setProps(moneyComponentProp);
formComponentList.add(moneyComponent);

// 数字输入框
OapiProcessSaveRequest.FormComponentVo numberComponent = new OapiProcessSaveRequest.FormComponentVo();
numberComponent.setComponentName("NumberField");
OapiProcessSaveRequest.FormComponentPropVo numberComponentProp = new OapiProcessSaveRequest.FormComponentPropVo();
numberComponentProp.setRequired(true);
numberComponentProp.setLabel("数字输入框带单位");
numberComponentProp.setPlaceholder("请输入");
numberComponentProp.setId("NumberField-J78F057N");
numberComponentProp.setUnit("元");
numberComponent.setProps(numberComponentProp);
formComponentList.add(numberComponent);

// 日期
OapiProcessSaveRequest.FormComponentVo dateComponent = new OapiProcessSaveRequest.FormComponentVo();
dateComponent.setComponentName("DDDateField");
OapiProcessSaveRequest.FormComponentPropVo dateComponentProp = new OapiProcessSaveRequest.FormComponentPropVo();
dateComponentProp.setRequired(true);
dateComponentProp.setLabel("日期");
dateComponentProp.setPlaceholder("请选择");
dateComponentProp.setUnit("小时"); // 小时或天
dateComponentProp.setId("DDDateField-J8MTJZVE");
dateComponent.setProps(dateComponentProp);
formComponentList.add(dateComponent);

// 日期区间
OapiProcessSaveRequest.FormComponentVo dateRangeComponent = new OapiProcessSaveRequest.FormComponentVo();
dateRangeComponent.setComponentName("DDDateRangeField");
OapiProcessSaveRequest.FormComponentPropVo dateRangeComponentProp = new OapiProcessSaveRequest.FormComponentPropVo();
dateRangeComponentProp.setRequired(true);
dateRangeComponentProp.setLabel(JSON.toJSONString(Arrays.asList("a", "b")));
dateRangeComponentProp.setPlaceholder("请选择");
dateRangeComponentProp.setUnit("小时"); // 小时或天
dateRangeComponentProp.setId("DDDateRangeField-J78F057Q");
dateRangeComponent.setProps(dateRangeComponentProp);
formComponentList.add(dateRangeComponent);

saveProcessRequest.setFormComponentList(formComponentList);
request.setSaveProcessRequest(saveProcessRequest);

OapiProcessSaveResponse response = client.execute(request, accessToken);
System.out.println(JSON.toJSONString(response));
```

**返回示例**

```
{
  "errcode": 0,
  "result": {
    "process_code": "PROC-7C8BB7AE-E758-4A96-9375-27CFD376B19C"
  },
  "request_id": "5av7ifh2atw0"
}
```

## 支持的表单组件（component\_name）

- 单行文本-TextField

  ```
  {
    "component_name": "TextField",
    "props": {
      "required": true,
      "placeholder": "请输入1",
      "label": "单行输入框",
      "id": "TextField-J78F056R"
    }
  }
  ```
- 多行文本-TextareaField

  ```
  {
    "component_name": "TextareaField",
    "props": {
      "required": true,
      "placeholder": "请输入2",
      "label": "多行输入框",
      "id": "TextareaField-J78F056S"
    }
  }
  ```
- 金额-MoneyField

  ```
  {
    "component_name": "MoneyField",
    "props": {
      "required": true,
      "placeholder": "请输入6",
      "label": "金额（元）大写",
      "id": "MoneyField-J78F0571",
      "not_upper": "1" // 是否禁用大写
    }
  }
  ```
- 数字输入框-NumberField

  ```
  {
    "component_name": "NumberField",
    "props": {
      "required": true,
      "placeholder": "请输入4",
      "label": "数字输入框带单位",
      "unit": "元",
      "id": "NumberField-J78F057N"
    }
  ```
- 计算公式-CalculateField

  ```
  {
    "component_name": "CalculateField",
    "props": {
      "required": true,
      "placeholder": "自动计算数值",
      "label": "计算公式",
      "id": "CalculateField-JF85Z4ZP"
    }
  }
  ```
- 单选框-DDSelectField

  > **[!IMPORTANT]**
  >
  > 选项最多200项，每项最多50个字。

  ```
  {
    "component_name": "DDSelectField",
    "props": {
      "required": true,
      "placeholder": "请选择7",
      "options": [
        "选项1",
        "选项2",
        "选项3"
      ],
      "label": "单选框",
      "id": "DDSelectField-J78F056U"
    }
  }
  ```
- 多选框-DDMultiSelectField

  ```
  {
    "component_name": "DDMultiSelectField",
    "props": {
      "required": true,
      "placeholder": "请选择",
      "options": [
        "选项1",
        "选项2",
        "选项3"
      ],
      "label": "多选框",
      "id": "DDMultiSelectField-J78F056V"
    }
  }
  ```

  > **[!IMPORTANT]**
  >
  > 选项最多200项，每项最多50个字。

  ```
  {
      value: Array<string>; // 如 ["选项1"，"选项2"]
  }
  ```
- 日期-DDDateField

  ```
  {
    "component_name": "DDDateField",
    "props": {
      "required": true,
      "placeholder": "请选择",
      "label": "日期时分",
      "unit": "小时",    // 小时或天
      "id": "DDDateField-J8MTJZVE"
    }
  }
  ```
- 日期区间-DDDateRangeField

  ```
  {
    "component_name": "DDDateRangeField",
    "props": {
      "required": true,
      "placeholder": "请选择888",
      "unit": "小时", // 小时或天
      "label": [
        "开始时间小时",
        "结束时间小时"
      ],
      "id": "DDDateRangeField-J78F057Q"
    }
  }
  ```
- 关联组件-RelateField

  ```
  {
    "component_name": "RelateField",
    "props": {
      "required": true,
      "label": "关联审批单",
      "placeholder": "请选择",
      "not_print": "1",
      "id": "RelateField-JF85Z4ZO"
    }
  }
  ```
- 图片-DDPhotoField

  ```
  {
    "component_name": "DDPhotoField",
    "props": {
      "required": true,
      "label": "图片",
      "id": "DDPhotoField-J78F056Y"
    }
  }
  ```
- 附件-DDAttachment

  ```
  {
    "component_name": "DDAttachment",
    "props": {
      "required": true,
      "label": "附件",
      "id": "DDAttachment-J78F0572"
    }
  }
  ```
- 内部联系人-InnerContactField

  ```
  {
    "component_name": "InnerContactField",
    "props": {
      "required": true,
      "placeholder": "请选择",
      "label": "联系人多选",
      "choice": "1", // 是否支持多选 "1" or "0"
      "id": "InnerContactField-J78F0574"
    }
  }
  ```
- 明细-TableField

  ```
  {
    "component_name": "TableField",
    "props": {
      "action_name": "增加明细", //明细按钮显示文案
      "stat_field": [ //统计总和的组件
        {
          "id": "NumberField-JT435KJO",
          "label": "数字输入框",
          "upper": false //统计总和是否大写
        }
      ],
      "label": "明细",
      "id": "TableField-JT435H4C"
    },
    "children": [ //明细内组件(不支持明细嵌套)
      {
        "component_name": "TextField",
        "props": {
          "placeholder": "请输入",
          "label": "单行输入框",
          "id": "TextField-JT435KJN"
        }
      },
      {
        "component_name": "NumberField",
        "props": {
          "placeholder": "请输入数字",
          "label": "数字输入框",
          "required": true,
          "id": "NumberField-JT435KJO"
        }
      }
    ]
  }
  ```

## 错误码

| **错误码（errorcode）** | **错误码描述（errmsg）** | **错误原因** | **解决方案** |
| --- | --- | --- | --- |
| 43007 | 需要授权 | access\_token不正确 | 请确认access\_token是否正确 |
| 810002 | 复制的审批流已超过最大数量 | 已达到创建模板上限200个 | 可删除不需要的模板再重试 |
| 15 | subcode=isp.-1,  "submsg=服务不可用" | componentName参数不能自定义，要传文档给的几个固定值 | 修改componentName参数值，请参考上方固定组件 |
| 8100017 | 没有访问权限 | 没有访问审批表单的权限 | 请确认表单code参数是否正确 |
| 820017 | 已有相同名称表单 | 表单名称重复 | 请确保表单名称唯一 |
| -1 | 系统繁忙 | 系统繁忙 | 请稍后重试 |
| 400001 | 系统繁忙 | 系统繁忙 | 请稍后重试 |

## 常见问题

1. **需要创建哪些模板？模板名称是否可以重复？**

   企业内部应用接入OA审批时，所有的审批模板，均需要调用钉钉接口初始化创建对应的模板。创建模板的时候，需确保模板名称（即name字段）的全局唯一性。
2. **该怎么设计表单？用什么类型的表单组件**

   钉钉审批、待办页面，展示审批单时，只会展示概要数据，即展示表单的前三个组件。因此，在设计模板时，前三个组件可根据业务场景设计，确保展示核心数据。

   表单类型可以使用本文已列支持的表单组件，包括单行文本框、金额、数字输入框等。
3. **创建的模板，是否会在钉钉审批管理后台出现？**

   调用接口的时候，fake\_mode参数必须传true，创建的模板不会在钉钉审批管理后台出现。
4. **调用接口返回错误码810002，错误信息是复制的审批流已超过最大数量**

   目前一个企业最多可创建200个自有审批模板，超过最大数量后调用接口会报错。
