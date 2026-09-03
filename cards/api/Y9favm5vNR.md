# 更新发送文件的检测状态

doc_id: Y9favm5vNR
completeness: full
archived: false
method: PUT
endpoint: https://api.dingtalk.com/v1.0/exclusive/sending/files/status
api_version: v2-new
app_types: 企业内部应用
permissions: Custom.FileCheck.ReadWrite

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，可调用获取企业内部应用的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- requestIds (Array of String, required): 文件发送的请求requestId，从订阅的企业员工发送文件的检测事件中获取。
- status (Integer, required): 更新状态，取值： - 1：检测通过。 - 2：检测不通过。 - 3：需要额外审批（需要先勾选“启用DLP后审批”） 如果检测不通过或额外审批未通过，文件接收方无法预览或者下载该文件。

## Returns
- optional: success(Boolean)

## Limits
- 专属钉钉组织管理员登录企业管理后台，在**钉钉专属版 > 专属安全 > 安全引擎中心 > 三色管控**中设置了DLP策略后，员工发送的文件将进入检测状态。调用本接口可更改发送文件的检测状态，修改文件检测状态为检测通过、检测不通过或额外审批。 ![](https://img.alicdn.com/imgextra/i3/O1CN01TaYLbT1tRnFIp7kbI_!!6000000005899-0-tps-1108-880.jpg)

source_url: https://open.dingtalk.com/document/development/update-the-detection-status-of-a-sent-file
updated_at: 2026-07-14 09:22:18
