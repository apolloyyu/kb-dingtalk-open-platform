---
title: "常见问题"
source_url: "https://open.dingtalk.com/document/development/common-questions-about-official-oa-approval"
namespace: "development"
slug: "common-questions-about-official-oa-approval"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "OA 审批 > 常见问题"
doc_id: "rrjHdUvwHr"
updated_at: "2026-07-14 09:21:49"
---

> Source: https://open.dingtalk.com/document/development/common-questions-about-official-oa-approval
> Path: 应用开发 / 服务端 API / OA 审批 > 常见问题
> Updated: 2026-07-14 09:21:49

# 常见问题

调用钉钉服务端官方OA审批接口时出现的常见错误。

## **官方 OA 审批**

- **调用第三方企业应用获取表单schema报错“code: 500，未知错误”**

  答：调用[获取表单 schema](0492-obtain-the-form-schema.md)接口报错“code: 500, 未知错误”，可能为权限问题：可以获取的表单是经过用户授权的，获取不到的表单没有经过用户授权的。授权获取审批实例数据文档参见[唤起授权弹窗](../03-Ogu5SlPY4t-客户端-JSAPI/0007-jsapi-request-auth-info.md)。
- **如何在审批中添加附件？**

  答：审批附件的实现需要配合服务端API和前端API实现，详细流程可参考[审批附件的操作流程](0487-new-version-of-attachment-approval-process.md)使用案例。

  > **[!NOTE]**
  >
  > 目前尚未支持通过调用服务端API添加审批附件。

  1. 调用[获取审批钉盘空间信息](0502-obtains-the-information-about-approval-nail-disk.md)接口，得到审批附件专属钉盘空间spaceId。
  2. 调用，从本地选择资源上传到审批附件钉盘获取spaceId、fileId、fileName、fileSize和fileType参数。
  3. 使用步骤2得到的参数，传递给发起审批接口中的附件组件。
- **如何获取审批中的附件？**

  答：审批附件的实现需要配合服务端API和前端API实现，详细流程可参考[审批附件的操作流程](0487-new-version-of-attachment-approval-process.md)使使用案例。

  1. 调用[授权预览审批附件](0503-official-authorized-preview-approval-attachment.md)接口。注意此接口会进行授权，只有传递的userid对应的用户才可以成功预览附件。
  2. 使用参数space\_id，调用[上传附件到钉盘/从钉盘选择文件](../03-Ogu5SlPY4t-客户端-JSAPI/0332-jsapi-upload-attachment-to-ding-talk.md)，获取钉盘附件的信息。
- **审批接口调用失败**

  答：当调用审批接口出错时，请参考以下信息进行排查：

  1. 在OA后台的审批应用中构造审批模板时，选择的组件类型必须是[发起审批实例](0497-create-an-approval-instance.md)中列举的类型，否则发起审批接口会报错。
  2. 构造的审批模板中明细组件内只支持输入框类型和图片组件类型，其他组件类型暂不支持。
  3. 构造的审批模板中最多支持20个组件。
- **调用发起OA审批实例的明细组件内可传入的控件格式有哪些？**

  答：调用[发起审批实例](0497-create-an-approval-instance.md)接口中明细组件内可传入的控件格式有:单行输入框、多行输入框、数字输入框、图片控件

## 自由 OA 审批

### **创建或更新模板接口**

#### **errcode=15**

- **问题描述**

  调用【创建或者更新模板】接口，出现如下错误。

  ```
  {
     " errcode":15,
     " sub_msg":"服务不可用",
     " sub_code":isp.-1,
     " errmsg":"Remote service error"[
        subcode=isp.-1,
        "submsg=服务不可用"
     ]
  }
  ```
- **原因**

  componentName参数不能自定义，要传文档给的几个固定值。
- **解决方案**

  修改componentName参数值，请参考[创建或更新审批模板](0510-create-orupdate-the-approval-template-new.md)。

#### **errcode=810002**

- **问题描述**

  调用【创建或者更新模板】接口，出现如下错误。

  ```
  {
     "errcode":810002,
     "errmsg":"复制的审批流已超过最大数量",
     "request_id":"xsr5qth2j075"
  }
  ```
- **原因**

  已达到创建模板上限200个。
- **解决方案**

  可删除不需要的模板再重试。

### **创建实例接口**

- **问题描述**

  无操作审批流的权限，请检查审批实例或者模板是否正确。

  ```
  {
      "errcode": 810007,
      "errmsg": "没有操作审批流的权限",
      "request_id": "xxx"
  }
  ```
- **原因**

  processCode参数不正确。
- **解决方案**

  processCode必须使用[创建或更新审批模板](0510-create-orupdate-the-approval-template-new.md)接口返回的processCode，并且参数**fake\_mode**必须传**true**。

### **更新实例接口**

#### **errcode=81000****7** **无操作审批流的权限**

- **问题描述**

  调用【更新实例接口process/workrecord/update】接口，出现如下错误。

  ```
  无操作审批流的权限，请检查审批实例或者模版是否正确
  ```

  ```
  {
      "errcode": 810007,
      "errmsg": "没有操作审批流的权限",
      "request_id": "xxx"
  }
  ```
- **原因**

  实例ID（process\_instance\_id）参数不正确。
- **解决方案**

  实例ID（process\_instance\_id）必须是[创建实例](0513-create-a-ticket-approval-instance.md)接口返回的process\_instance\_id值，不能使用官方审批流的实例值。

#### **errorcode=820008**

- **问题描述**

  调用【更新实例接口process/workrecord/update】接口，出现如下错误。

  ```
  {
     "errcode":810002,
     "errmsg":"审批系统错误，原因为【审批表单已被管理员修改】",
     "request_id":"6pz3le495848"
  }
  ```
- **原因**

  没有传result参数。
- **解决方案**

  更新审批单实例时，请传入result值后，再尝试。

### **创建待办接口**

#### **errorcode=820008**

- **问题描述**

  调用【创建待办process/workrecord/task/create】接口，出现如下错误。

  ```
  {
     "errcode":810002,
     "errmsg":"审批系统错误，原因为【引擎已知错误:{0}",
     "request_id":"6pz3le495848"
  }
  ```
- **原因**

  参数URL字符过长。
- **解决方案**

  请修改URL参数，再尝试。

#### **errorcode=820010**

- **问题描述**

  调用【创建待办process/workrecord/task/create】接口，出现如下错误。

  ```
  {
     "errcode":820010,
     "request_id":"6pz3le495848"
  }
  ```
- **原因**

  实例下的待办任务超过限制。
- **解决方案**

  一个实例下，最多只能创建100个待办，请删除不需要的待办任务重试或新建实例。

### **其他**

#### **自有OA审批接口提示“无操作审批流权限”**

此问题是由于将“使用官方OA审批”和“使用自有OA审批”两种场景混用导致的。

1. 调用自有OA审批创建实例接口，参数process\_code必须来自[创建或更新审批模板](0510-create-orupdate-the-approval-template-new.md)接口，不能使用从审批后台地址栏中截取的process\_code。
2. 调用自有OA审批的更新实例状态接口，参数process\_instance\_id必须来自[创建实例](0513-create-a-ticket-approval-instance.md)接口，不能传入官方审批流中发起审批实例接口得到的process\_instance\_id。
