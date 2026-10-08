---
title: "OA审批附件同步到知识库"
source_url: "https://open.dingtalk.com/document/connection/oa-approval-attachment-is-synchronized-to-the-knowledge-base"
namespace: "connection"
slug: "oa-approval-attachment-is-synchronized-to-the-knowledge-base"
group: "连接平台"
tab: "连接器中心"
breadcrumb: "官方连接器 > 使用教程 > OA审批 > OA审批附件同步到知识库"
doc_id: "883mSIfSHk"
updated_at: "2026-07-30 09:19:03"
---

> Source: https://open.dingtalk.com/document/connection/oa-approval-attachment-is-synchronized-to-the-knowledge-base
> Path: 连接平台 / 连接器中心 / 官方连接器 > 使用教程 > OA审批 > OA审批附件同步到知识库
> Updated: 2026-07-30 09:19:03

# OA审批附件同步到知识库

本教程为您讲解如何将OA审批表单中的附件同步到文档知识库。

## 简介

OA审批表单通过后，将表单附件文件同步到文档知识库对很多行业都有重大意义，特别是在法律、政府机构、医疗行业可以提高工作效率和精准度，减少工作量和文档信息的丢失。更好地管理和保护文件记录，提高流程管理等方面的精细化和自动化程度。

## **准备工作**

1. 拥有所在钉钉组织开发者后台的[开发者权限](../../01-应用开发/01-XOnnmGCTbn-开发指南/0006-get-developer-permissions.md)。
2. 拥有OA审批的管理员权限。
3. 拥有一个所在钉钉组织的[知识库](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0553-knowledge-base-overview.md)。
4. 已开通[钉钉专业版](dingtalk://dingtalkclient/page/link?url=https%3A%2F%2Fn.dingtalk.com%2Fdingding%2Fdd-pro-composite-order%2Fpc%2Findex.html%3Fpopup_wnd%3Dtrue%26dd_tab%3Dtrue%26width%3D900%26height%3D600%26title%3D%25E9%2592%2589%25E9%2592%2589%25E6%2595%25B0%25E5%25AD%2597%25E8%25B5%2584%25E4%25BA%25A7%26articleCode%3DDT_GOODS_dingtalkmemberplus%26channel%3Dopenpf_web_devdoc%26corpId%3D${corpId}%26accessoryProduct%3DpaasWithConnector%26tabKey%3DDT_GOODS_dingtalkmemberplus&popup_wnd=true&height=600&width=900)。（OA审批中使用连接器必备）。

## **预期效果**

审批通过后，可在知识库目录下查询附件文件。

![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3434735871/p887620.png)

## **步骤一：配置连接流**

1. 配置连接流之前，需要创建[我的连接流](https://open-dev.dingtalk.com/fe/connector?hash=%23%2FmyFlow#/myFlow)。
2. 设置触发事件为：

   1. 设置流程为：子流程。
   2. 设置入参

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0995134371/p888361.png)

   也可以使用《编码模式》导入如下配置：

   ```
   {
     "description": "入参",
     "properties": {
       "dentryUuid": {
         "description": "目录ID",
         "properties": {},
         "required": [],
         "sortedProps": [],
         "title": "目录ID",
         "type": "string",
         "version": 0
       },
       "fileInfo": {
         "description": "文件信息",
         "properties": {},
         "required": [],
         "sortedProps": [],
         "title": "文件信息",
         "type": "string",
         "version": 0
       },
       "userId": {
         "description": "用户ID",
         "properties": {},
         "required": [],
         "sortedProps": [],
         "title": "用户ID",
         "type": "string",
         "version": 0
       }
     },
     "required": [
       "fileInfo",
       "userId",
       "dentryUuid"
     ],
     "sortedProps": [
       "fileInfo",
       "userId",
       "dentryUuid"
     ],
     "title": "入参",
     "type": "object",
     "version": 0
   }
   ```
3. 添加临时变量节点。

   1. **选择连接器-流程变量：**

      ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3434735871/p887614.png)
   2. **选择执行动作-**创建基本类型变量**：**

      ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3434735871/p887623.png)
   3. 设置入参：

      | **参数** | **说明** |
      | --- | --- |
      | 变量1 | - 变量key：spaceId - 变量类型：文本 - 默认值：`JACKSONJSONPATHEVAL(JSONPARSE(​1. 入参.文件信息​),'$[0].spaceId')`。 image |
      | 变量2 | - 变量key：fileId - 变量类型：文本 - 默认值：`JACKSONJSONPATHEVAL(JSONPARSE(1. 入参.文件信息),'$[0].fileId')`。 image |
      | 变量3 | - 变量key：fileName - 变量类型：文本 - 默认值：`JACKSONJSONPATHEVAL(JSONPARSE(1. 入参.文件信息),'$[0].fileName')`。 image |
4. **添加权限**：官方 > 存储管理 > 添加权限。

   | **参数** | **说明** |
   | --- | --- |
   | 空间 ID | 选择：节点2：流程变量.spaceId |
   | 操作用户的userId | 选择：节点1：入参.用户ID |
   | 文件或者文件夹Id | 选择：节点2：流程变量.fileId |
   | 权限角色Id | 填写：拥有 |
   | 权限成员信息 | - 权限成员类型："USER" - 权限成员id：节点1：入参.用户ID |

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3434735871/p887611.png)
5. **获取文件上传信息**：官方 > 存储管理 > 获取文件上传信息。

   | **参数** | **说明** |
   | --- | --- |
   | 操作者userId | 选择：节点1：入参.用户ID |
   | 父节点dentryUuid | 选择：节点1：入参.目录ID |

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3434735871/p887626.png)
6. **获取文件下载信息**：官方 > 存储管理 > 获取文件下载信息。

   | **参数** | **说明** |
   | --- | --- |
   | 空间Id | 选择：节点2：流程变量.spaceId |
   | 文件Id | 选择：节点2：流程变量.fileId |
   | 操作者userId | 选择：节点1：入参.用户ID |

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3434735871/p887625.png)
7. **上传文件**：官方 > 存储管理 > 文件上传。

   | **参数** | **说明** |
   | --- | --- |
   | 文件下载URL地址 | 选择：节点5：出参.业务结果.Header加签信息.下载URL[\*] |
   | 文件上传URL地址 | 选择：节点4：出参.响应体.业务结果.Header加签上传信息.传输地址[\*] |
   | 文件下载Header信息 | 选择：节点5：出参.业务结果.Header加签信息.请求头信息 |
   | 文件上传Header信息 | 选择：节点4：出参.响应体.业务结果.Header加签上传信息.请求头 |

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3434735871/p887613.png)
8. **提交文件**：官方 > 存储管理 > 提交文件。

   | **参数** | **说明** |
   | --- | --- |
   | 操作用户userId | 选择：节点1：入参.用户ID |
   | 添加文件唯一标识 | 选择：节点4：出参.响应体.业务结果.上传唯一标识 |
   | 名称（文件名+后缀） | 选择：节点2：流程变量.fileName |
   | 父节点dentryUuid | 选择：节点1：入参.目录ID |

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3434735871/p887618.png)
9. 发布连接流。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4924134371/p887617.png)

## **步骤二：创建OA附件审批表单**

1. 流程表单设计

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4924134371/p887616.png)
2. 流程设计

   1. 设置审批人，本示例使用**自动通过**：

      ![image.gif](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3434735871/p887612.gif)
   2. 添加连接器：

      ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3434735871/p887609.png)
   3. 选择连接器。

      ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3434735871/p887615.png)

## **恭喜，你已完成全部配置！**

你已完成本教程的全部内容，可以开始测试。

1. 需提前创建[知识库和知识库目录](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0553-knowledge-base-overview.md)。
2. 附件大小建议在3MB以内。

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3434735871/p887603.png)

   ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3434735871/p887608.png)
