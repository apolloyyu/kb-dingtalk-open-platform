---
title: "单据实例"
source_url: "https://open.dingtalk.com/document/development/yida-document-instance"
namespace: "development"
slug: "yida-document-instance"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 宜搭 > 旧版宜搭API参考 > 单据实例"
doc_id: "lFlwQwDMXA"
updated_at: "2025-10-17 12:41:02"
---

> Source: https://open.dingtalk.com/document/development/yida-document-instance
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 宜搭 > 旧版宜搭API参考 > 单据实例
> Updated: 2025-10-17 12:41:02

# 单据实例

> **[!IMPORTANT]**
>
> 此旧版宜搭API接口文档已于**2021年10月15日**迁移到**历史文档（不推荐）**目录，已经接入的用户可继续使用，正在准备接入宜搭的用户请查看[宜搭应用开发](https://open.dingtalk.com/document/orgapp/overview-yida)。

## 1. 新增单据实例

- 接口: [/yida\_vpc/form/saveFormData.json](https://s-api.alibaba-inc.com/yida_vpc/form/saveFormData.json?spm=a1ztn6.10384403.0.0.3c5264faPwMds7&file=saveFormData.json)
- 参数：

  | 参数 | 描述 | 是否必填 | 示例 | 备注 |
  | --- | --- | --- | --- | --- |
  | appType | 应用ID | 是 | APP\_PBKT0MFBEBTDO8T7SLVP |  |
  | systemToken | 应用秘钥 | 是 | hexxxx | 在应用数据中获取。 |
  | userId | 钉钉的userId | 是 |  |  |
  | language | 语言 | 否 | zh\_CN | 可选值：zh\_CN/en\_US默认：zh\_CN |
  | formUuid | 表单ID | 是 | FORM-NJYJZELV8YZRDEI2N5IQ7L6VEDMR1VE9GMPCJB |  |
  | appType | 应用ID | 是 | APP\_DR4OK27ZKL5N22B907E8 |  |
  | formDataJson | 表单数据 | 是 | {"textField\_jcpm6agt": "单行","employeeField\_jcos0sar": ["workno"]} | 参考：附录1保存/更新 表单数据格式说明 |
- 返回值

  - result : 实例ID;
  - success : 请求是否成功;
  - errorMsg : 错误信息;
  - errorCode : 错误码;
- 返回示例

  ```
  {
     "result":"FINST-EF6Y93URN2UZ1SBPLIP9NAV6HR2GEO1Z4ZCHSCJ0",
     "success":true
  }
  ```

## 2. 更新单据中指定组件值

- 接口: [/yida\_vpc/form/updateFormData.json](https://s-api.alibaba-inc.com/yida_vpc/form/updateFormData.json)
- 参数：​​

  | 参数 | 描述 | 是否必填 | 示例 | 备注 |
  | --- | --- | --- | --- | --- |
  | appType | 应用ID | 是 | APP\_PBKT0MFBEBTDO8T7SLVP |  |
  | systemToken | 应用秘钥 | 是 | helxxx | 在应用数据中获取。 |
  | userId | 钉钉的userId | 是 |  |  |
  | language | 语言 | 否 | zh\_CN | 可选值：zh\_CN/en\_US默认：zh\_CN |
  | formInstId | 要更新的表单数据ID | 是 | FINST-NJYJZELVVYZRVGJHR7M6FJW3ESJN1P1TCNPCJ9 |  |
  | updateFormDataJson | 要更新的表单组件值，必填 | 是 | {"employeeField\_jcpm5gy2": ["workno"]} | 参考：附录1保存/更新 表单数据格式说明。 参数有的组件更新，没有的组件保持不变。 明细的值只能统一更新，无法只更新明细下某个组件的值 |
- 返回值

  - success : 请求是否成功;
  - errorMsg : 错误信息;
  - errorCode : 错误码;
- 返回示例

  ```
  {
   
     "success":true
  }
  ```

## 3. 删除单据实例

- 接口: [/yida\_vpc/form/deleteFormData.json](https://s-api.alibaba-inc.com/yida_vpc/form/deleteFormData.json)
- 参数：​​

  | 参数 | 描述 | 是否必填 | 示例 | 备注 |
  | --- | --- | --- | --- | --- |
  | appType | 应用ID | 是 | APP\_PBKT0MFBEBTDO8T7SLVP |  |
  | systemToken | 应用秘钥 | 是 | helxxx | 在应用数据中获取。 |
  | userId | 钉钉的userId | 是 |  |  |
  | language | 语言 | 否 | zh\_CN | 可选值：zh\_CN/en\_US默认：zh\_CN |
  | formInstId | 要删除的表单数据ID | 是 | FINST-NJYJZELVVYZRVGJHR7M6FJW3ESJN1P1TCNPCJ9 |  |
- 返回值

  - success : 请求是否成功;
  - errorMsg : 错误信息;
  - errorCode : 错误码;
- 返回示例

  ```
  {
   
     "success":true
  }
  ```

## 4. 根据单据实例ID查询单据实例详情

- 接口:[/yida\_vpc/form/getFormDataById.json](https://s-api.alibaba-inc.com/yida_vpc/form/getFormDataById.json)
- 参数：​​

  | 参数 | 描述 | 是否必填 | 示例 | 备注 |
  | --- | --- | --- | --- | --- |
  | appType | 应用ID | 是 | APP\_PBKT0MFBEBTDO8T7SLVP |  |
  | systemToken | 应用秘钥 | 是 | helxx | 在应用数据中获取。 |
  | userId | 钉钉的userId | 是 |  |  |
  | language | 语言 | 否 | zh\_CN | 可选值：zh\_CN/en\_US默认：zh\_CN |
  | formInstId | 要查询的实例的实例ID | 是 | FINST-NJYJZELVVYZRVGJHR7M6FJW3ESJN1P1TCNPCJ9 |  |
- 返回值

  - success : 请求是否成功;
  - errorMsg : 错误信息;
  - errorCode : 错误码;
  - result：单据实例详情。

## 5. 根据条件搜索单据实例ID列表

- 接口: [/yida\_vpc/form/searchFormDataIds.json](https://s-api.alibaba-inc.com/yida_vpc/form/searchFormDataIds.json)
- 说明：只有应用管理员才能使用这个接口
- 参数：​​

  | 参数 | 描述 | 是否必填 | 示例 | 备注 |
  | --- | --- | --- | --- | --- |
  | appType | 应用ID | 是 | APP\_PBKT0MFBEBTDO8T7SLVP |  |
  | systemToken | 应用秘钥 | 是 | hexxx | 在应用数据中获取。 |
  | userId | 钉钉的userId | 是 |  |  |
  | language | 语言 | 否 | zh\_CN | 可选值：zh\_CN/en\_US默认：zh\_CN |
  | formUuid | 表单ID | 是 | FORM-EF6Y4G8WO2FN0SUB43TDQ3CGC3FMFQ1G9400RCJ3 |  |
  | searchFieldJson | 根据表单内组件值查询 | 否 |  | 格式见附录2：根据组件值进行条件搜索，组件值格式说明 |
  | currentPage | 当前页 | 否 | 1 | 必须大于0默认1 |
  | pageSize | 每页记录数 | 否 | 10 | 必须大于0默认10不能大于100 |
  | originatorId | 根据数据提交人工号查询 | 否 |  |  |
  | createFrom | createFrom和createTo两个时间构造一个时间段。查询在该时间段创建的数据列表 | 否 | 2018-01-01 | 字符串格式，且为yyyy-MM-DD格式 |
  | createTo | createFrom和createTo两个时间构造一个时间段。查询在该时间段创建的数据列表。 | 否 | 2018-02-01 | 字符串格式，且为yyyy-MM-DD格式。和createFrom一起，相当于查询在2018-01-01到2018-01-31之间(包含01和31号)创建的数据。 |
  | modifiedFrom | modifiedFrom和modifiedTo构成一个时间段，查询在该时间段有修改的数据列表 | 否 | 2018-01-01 | 字符串格式，且为yyyy-MM-DD格式 |
  | modifiedTo | modifiedFrom和modifiedTo构成一个时间段，查询在该时间段有修改的数据列表。 | 否 | 2018-02-01 | 字符串格式，且为yyyy-MM-DD格式。 和modifiedFrom一起，相当于查询在 2018-01-01到2018-01-31之间(包含01和31号)被修改的数据。 |
- 返回值

  - success : 请求是否成功;
  - errorMsg : 错误信息;
  - errorCode : 错误码;
  - result：

    - currentPage : 当前页
    - totalCount : 符合条件的实例总数
    - data : 实例ID列表
- 返回示例

  ```
  {
     "result":{
        "data":[
           "FINST-EF6Y93URN2F02S745LTMW2D2G4WVDS16O17ISCJ0"
        ],
        "totalCount":1,
        "currentPage":1
     },
     "success":true
  }
  ```

## 6. 根据条件搜索单据实例详情列表

- 接口: [/yida\_vpc/form/searchFormDataIds.json](https://s-api.alibaba-inc.com/yida_vpc/form/searchFormDataIds.json)
- 说明：只有应用管理员才能使用这个接口
- 参数：​​

  | 参数 | 描述 | 是否必填 | 示例 | 备注 |
  | --- | --- | --- | --- | --- |
  | appType | 应用ID | 是 | APP\_PBKT0MFBEBTDO8T7SLVP |  |
  | systemToken | 应用秘钥 | 是 | hellxxx | 在应用数据中获取。 |
  | userId | 钉钉的userId | 是 |  |  |
  | language | 语言 | 否 | zh\_CN | 可选值：zh\_CN/en\_US默认：zh\_CN |
  | formUuid | 表单ID | 是 | FORM-EF6Y4G8WO2FN0SUB43TDQ3CGC3FMFQ1G9400RCJ3 |  |
  | searchFieldJson | 根据表单内组件值查询 | 否 |  | 格式见附录2：根据组件值进行条件搜索，组件值格式说明 |
  | currentPage | 当前页 | 否 | 1 | 必须大于0，默认1 |
  | pageSize | 每页记录数 | 否 | 10 | 必须大于0默认10不能大于100 |
  | originatorId | 根据数据提交人工号查询 | 否 |  |  |
  | createFrom | createFrom和createTo两个时间构造一个时间段。查询在该时间段创建的数据列表 | 否 | 2018-01-01 | 字符串格式，且为yyyy-MM-DD格式（或者精确到秒yyyy-MM-DD HH:mm:ss） |
  | createTo | createFrom和createTo两个时间构造一个时间段。查询在该时间段创建的数据列表。 | 否 | 2018-02-01 | 字符串格式，且为yyyy-MM-DD格式（或者精确到秒yyyy-MM-DD HH:mm:ss）和createFrom一起，相当于查询在2018-01-01到2018-01-31之间(包含01和31号)创建的数据。 |
  | modifiedFrom | modifiedFrom和modifiedTo构成一个时间段，查询在该时间段有修改的数据列表 | 否 | 2018-01-01 | 字符串格式，且为yyyy-MM-DD格式（或者精确到秒yyyy-MM-DD HH:mm:ss） |
  | modifiedTo | modifiedFrom和modifiedTo构成一个时间段，查询在该时间段有修改的数据列表。 | 否 | 2018-02-01 | 字符串格式，且为yyyy-MM-DD格式。 （或者精确到秒yyyy-MM-DD HH:mm:ss）和modifiedFrom一起，相当于查询在 2018-01-01到2018-01-31之间(包含01和31号)被修改的数据。 |
  | dynamicOrder | 指定排序字段 | 否 | {"numberField\_1ac":"+"} | 表示按照字段numberField\_1ac升序排列 |
- 返回值

  - success : 请求是否成功;
  - errorMsg : 错误信息;
  - errorCode : 错误码;
  - result：

    - currentPage : 当前页
    - totalCount : 符合条件的实例总数
    - data : 实例ID列表

## 7. 获取表单定义

- 接口: [/yida\_vpc/formDesign/getFormComponentDefinationList.json](https://s-api.alibaba-inc.com/yida_vpc/formDesign/getFormComponentDefinationList.json)
- 参数：​​

  | 参数 | 描述 | 是否必填 | 示例 | 备注 |
  | --- | --- | --- | --- | --- |
  | appType | 应用ID | 是 | APP\_PBKT0MFBEBTDO8T7SLVP |  |
  | systemToken | 应用秘钥 | 是 | hexxxx | 在应用数据中获取。 |
  | userId | 钉钉的userId | 是 |  |  |
  | language | 语言 | 否 | zh\_CN | 可选值：zh\_CN/en\_US默认：zh\_CN |
  | formUuid | 表单ID | 是 | FORM-NJYJZELV8YZRDEI2N5IQ7L6VEDMR1VE9GMPCJB |  |
  | version | 表单版本 | 否 | 1 | 可以传入formData中的version字段。为空时返回最新的版本定义 |
- 返回值

  - success : 请求是否成功;
  - errorMsg : 错误信息;
  - errorCode : 错误码;
  - result：[]
- 返回示例

  ```
  {
      "success":true,
      "content":[
          {
              "label":"{"en_US":"CheckBox Field","zh_CN":"多选","type":"i18n"}",
              "key":"checkboxField_jiwvhkdi"
          },
          {
              "label":"{"en_US":"Textarea Field","zh_CN":"多行输入框","type":"i18n"}",
              "key":"textareaField_jiwvhkdh"
          },
          {
              "label":"{"en_US":"Select Field","zh_CN":"下拉单选","type":"i18n"}",
              "key":"selectField_jiwvhkdg"
          }
      ]
  }
  ```
