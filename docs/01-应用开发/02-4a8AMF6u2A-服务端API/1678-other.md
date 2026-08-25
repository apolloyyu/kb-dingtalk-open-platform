---
title: "其他"
source_url: "https://open.dingtalk.com/document/development/other"
namespace: "development"
slug: "other"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 宜搭 > 旧版宜搭API参考 > 其他"
doc_id: "EGU8bPGKvI"
updated_at: "2025-10-17 12:41:04"
---

> Source: https://open.dingtalk.com/document/development/other
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 宜搭 > 旧版宜搭API参考 > 其他
> Updated: 2025-10-17 12:41:04

# 其他

> **[!IMPORTANT]**
>
> 此旧版宜搭API接口文档已于**2021年10月15日**迁移到**历史文档（不推荐）**目录，已经接入的用户可继续使用，正在准备接入宜搭的用户请查看[宜搭应用开发](https://open.dingtalk.com/document/orgapp/overview-yida)。

## 1. 宜搭附件地址转临时免登地址

- 接口: [/yida\_vpc/](https://s-api.alibaba-inc.com/yida_vpc/formDesign/getFormComponentDefinationList.json)file/getOpenUrl.json
- 参数：

  | 参数 | 描述 | 是否必填 | 示例 | 备注 |
  | --- | --- | --- | --- | --- |
  | appType | 应用ID | 是 | APP\_PBKT0MFBEBTDO8T7SLVP |  |
  | systemToken | 应用秘钥 | 是 | hexxxx | 在应用数据中获取。 |
  | userId | 钉钉的userId | 是 |  |  |
  | language | 语言 | 否 | zh\_CN | 可选值：zh\_CN/en\_US默认：zh\_CN |
  | fileUrl | 宜搭附件地址 | 是 | https://www.aliwork.com/fileHandle?appType=APP\_VN7I6HVKUTXES7XX4OI8&fileName=2a4103a6-44d5-4114-990d-4147a2d53811.xlsx&instId=&type=download |  |
  | timeout | 临时地址多久失效,单位毫秒 | 是 | 60000 | 60000表示一分钟后临时地址失效 |
- 返回值

  - success : 请求是否成功;
  - errorMsg : 错误信息;
  - errorCode : 错误码;
  - result：[]
- 返回示例

  ```
  {
    "result": "免登的附件地址",
    "success": true
  }
  ```

## 2. 增加评论

- 接口: /yida\_vpc/remark/save.json
- 参数：​​

  | 参数 | 描述 | 是否必填 | 示例 | 备注 |
  | --- | --- | --- | --- | --- |
  | appType | 应用ID | 是 | APP\_PBKT0MFBEBTDO8T7SLVP |  |
  | systemToken | 应用秘钥 | 是 | hexxxx | 在应用数据中获取。 |
  | userId | 评论人钉钉的userId | 是 |  |  |
  | language | 语言 | 否 | zh\_CN | 可选值：zh\_CN/en\_US默认：zh\_CN |
  | formInstId | 实例ID | 是 |  |  |
  | replyId | 对评论进行回复 | 否 | 12 |  |
  | atUserId | 将评论内容通过钉钉发给指定用户 | 否 | 多个工号,用英文逗号分隔 |  |
  | content | 评论内容 | 是 |  |  |
- 返回值

  - success : 请求是否成功;
  - errorMsg : 错误信息;
  - errorCode : 错误码;
  - result：评论ID
- 返回示例

  ```
  {
    "result": 14,
    "success": true
  }
  ```

## 3. 获取应用下面包含表单页面的列表

- 接口: /yida\_vpc/app/listNavigationByFormType.json
- 参数：​​

  | 参数 | 描述 | 是否必填 | 示例 | 备注 |
  | --- | --- | --- | --- | --- |
  | 参数名 | 描述 | 是否必填 | 示例 | 备注 |
  | appType | 应用ID | 是 | APP\_PBKT0MFBEBTDO8T7SLVP |  |
  | systemToken | 应用秘钥 | 是 | hexxxx | 在应用数据中获取。 |
  | userId | 评论人钉钉的userId | 是 |  |  |
  | language | 语言 | 否 | zh\_CN | 可选值：zh\_CN/en\_US默认：zh\_CN |
  | formType | 页面类型 | 是 |  | - receipt单据页面 - process流程页面 - report报表页面 |
- 返回值

  - success : 请求是否成功;
  - errorMsg : 错误信息;
  - errorCode : 错误码;
  - result：页面列表
- 返回示例

  ```
  {
    "result": [
      {
        "formUuid": "FORM-92GKRGIVZ5xxJZ6XB7WU3G4XNHV1YXYNELXJ0",
        "processCode": "TPROC--92GKRGIxx5V6LJZ6XB7WU3G4XNHV15YYNELXJ1",
        "title": {
          "pureEn_US": "普通流程01",
          "en_US": "普通流程01",
          "zh_CN": "普通流程01",
          "type": "i18n"
        },
      },
      {
        "formUuid": "FORM-92GKRGIV63X6K8X8ZH432CWBEGFN1DZ9V3OXJ0",
        "processCode": "TPROC--92GKRGIV63X6K8X8ZH432CWBEGFN1G3AV3OXJ1",
        "title": {
          "pureEn_US": "普通流程01(carbon)",
          "en_US": "普通流程01(carbon)",
          "zh_CN": "普通流程01-01-抄送人",
          "type": "i18n"
        }
      }
    ],
    "success": true,
    "errorCode": null,
    "content": null,
    "errorMsg": null
  }
  ```
