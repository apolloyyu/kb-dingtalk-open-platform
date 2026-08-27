---
title: "接入流程"
source_url: "https://open.dingtalk.com/document/development/ding-card-interactive-card-operation-process"
namespace: "development"
slug: "ding-card-interactive-card-operation-process"
group: "互动卡片"
tab: "搭建平台"
breadcrumb: "普通版搭建平台 > 接入流程"
doc_id: "3Y8gWle2g5"
updated_at: "2026-08-07 14:53:22"
---

> Source: https://open.dingtalk.com/document/development/ding-card-interactive-card-operation-process
> Path: 互动卡片 / 搭建平台 / 普通版搭建平台 > 接入流程
> Updated: 2026-08-07 14:53:22

# 接入流程

本文将帮助您快速掌握互动卡片普通版的接入流程，涵盖从应用创建到卡片发送与更新的完整操作步骤。通过本文，您可了解如何在钉钉企业内部应用中集成并使用互动卡片功能，实现高效的消息交互。

## 预期效果

### 更新前订餐图片

### 更新后

![更新后](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5648614561/p446110.png)

## 准备工作

在开始前，请确认已完成以下准备：

- 已成为钉钉开发者，详情请参考[成为钉钉开发者](../../01-应用开发/02-4a8AMF6u2A-服务端API/0003-add-api-permission.md)。
- 明确关键参数获取方式：

  - **cardBizId**：开发者自定义的卡片业务标识 ID，需保证在同一会话中唯一。
  - **openConversationId**：群会话 ID，获取方式参考[机器人发送互动卡片（普通版）](../../01-应用开发/02-4a8AMF6u2A-服务端API/1476-robots-send-interactive-cards.md)。

## 接入流程简介

本流程适用于**企业内部应用**开发者，用于通过机器人能力在群聊或单聊中发送和更新互动卡片消息。整体流程如下：

步骤一：登录[开发者后台](https://open-dev.dingtalk.com/#/)，创建[企业内部应用](../../01-应用开发/01-XOnnmGCTbn-开发指南/0007-create-application.md)。

步骤二：获取AppKey和AppSecret。

步骤三：在权限管理中申请机器人相关接口权限。

步骤四：调用[获取企业内部应用的accessToken](../../01-应用开发/02-4a8AMF6u2A-服务端API/0033-obtain-the-access-token-of-an-internal-app.md)接口获取企业内部应用的`accessToken`。

步骤五：登录[互动卡片普通版搭建平台](https://card.dingtalk.com/card-builder)，搭建卡片模板。

步骤六：调用服务端 API 发送及更新互动卡片：

- 调用新版服务端API-[机器人发送互动卡片（普通版）](../../01-应用开发/02-4a8AMF6u2A-服务端API/1476-robots-send-interactive-cards.md)接口，实现发送卡片信息。
- 根据cardBizId卡片标识ID，调用新版服务端API-[更新机器人发送互动卡片（普通版）](../../01-应用开发/02-4a8AMF6u2A-服务端API/1477-update-the-robot-to-send-interactive-cards.md)接口，实现更新卡片内容。

## 步骤一：创建企业内部应用

> **[!NOTE]**
>
> 如果已有企业内部应用，可跳过此步骤。

1. 登录[开发者后台](https://open-dev.dingtalk.com/#/)，创建[企业内部应用](../../01-应用开发/01-XOnnmGCTbn-开发指南/0007-create-application.md)。![创建企业内部应用](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5648614561/p444437.png)
2. 填写应用的基本信息，然后单击**确定创建**。

   - 应用类型：选择H5微应用。
   - 应用名称：填写应用名称信息。
   - 应用描述：填写应用的基本描述。
   - 开发方式：选择企业自主开发。![配置企业内部应用基本信息](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5648614561/p444456.png)

## 步骤二：获取AppKey和AppSecret

获取应用的Appkey和AppSecret。![获取应用Appkey](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4648614561/p444462.png)

## 步骤三：添加接口权限

申请机器人接口权限，搜索“机器人”，选择机器人相关接口权限并申请。![添加权限](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5648614561/p444506.png)

## 步骤四：获取企业内部应用的accessToken

根据步骤二中的AppKey和AppSecret，根据[获取企业内部应用的accessToken](../../01-应用开发/02-4a8AMF6u2A-服务端API/0033-obtain-the-access-token-of-an-internal-app.md)接口获取应用访问凭证。

## 步骤五：选择Ding Card互动卡片

1. 登录[互动卡片普通版搭建平台](https://card.dingtalk.com/card-builder)。![ding card搭建平台](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5648614561/p444520.png)
2. 选择卡片组件并复制卡片数据，本文使用钉钉**官方模板**-**食堂订餐**。![食堂订餐模板](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4648614561/p444533.png)

## 步骤六：调用服务端API

1. 下载新版SDK，详情参考[服务端SDK下载](../../01-应用开发/02-4a8AMF6u2A-服务端API/0002-download-the-server-side-sdk.md)。
2. 调用新版服务端API-[机器人发送互动卡片（普通版）](../../01-应用开发/02-4a8AMF6u2A-服务端API/1476-robots-send-interactive-cards.md)接口，实现互动卡片发送。

   ```
   public void sendDingCard() throws Exception {
           Config config = new Config();
           config.protocol = "https";
           config.regionId = "central";
           com.aliyun.dingtalkim_1_0.Client client = new Client(config);
           SendRobotInteractiveCardHeaders sendRobotInteractiveCardHeaders = new SendRobotInteractiveCardHeaders();
           sendRobotInteractiveCardHeaders.xAcsDingtalkAccessToken = "<your access token>";
           SendRobotInteractiveCardRequest.SendRobotInteractiveCardRequestSendOptions sendOptions = new SendRobotInteractiveCardRequest.SendRobotInteractiveCardRequestSendOptions()
                   .setAtUserListJson("[{\"nickName\":\"小齐\",\"userId\":\"08521816421284272\"}]")
                   .setAtAll(false)
                   .setReceiverListJson("[{\"userId\":\"08521816421284272\"}]");
           SendRobotInteractiveCardRequest sendRobotInteractiveCardRequest = new SendRobotInteractiveCardRequest()
                   //固定填写： 
                   .setCardTemplateId("StandardCard")
                   //群会话id
                   .setOpenConversationId("cidxxxxxxx3Rn+Y6Yg==")
                   .setSingleChatReceiver("{\"userId\":\"08521816421284272\"}")
                   //发送不同卡片内容，需传入不同的cardBizId。
                   .setCardBizId("dingCard1001")
                   //机器人ID，当该机器人为企业内部开发-机器人时，填写机器人应用的appKey
                   //其他机器人填写机器人的robotCode值
                   .setRobotCode("xxxxxxxxxxxxx")
                   .setCardData("{\n" +
                           "  \"config\": {\n" +
                           "    \"autoLayout\": true,\n" +
                           "    \"enableForward\": true\n" +
                           "  },\n" +
                           "  \"header\": {\n" +
                           "    \"title\": {\n" +
                           "      \"type\": \"text\",\n" +
                           "      \"text\": \"订餐\",\n" +
                           "      \"color\": \"common_green1_color\"\n" +
                           "    },\n" +
                           "    \"logo\": \"@lALPDrz7jNRJdJE4OA\"\n" +
                           "  },\n" +
                           "  \"contents\": [\n" +
                           "    {\n" +
                           "      \"type\": \"image\",\n" +
                           "      \"image\": \"@lALPDfYH0aWc_a3NAljNAyA\",\n" +
                           "      \"ratio\": \"16:9\",\n" +
                           "      \"id\": \"image_1653901065785\"\n" +
                           "    },\n" +
                           "    {\n" +
                           "      \"type\": \"markdown\",\n" +
                           "      \"text\": \"套餐内容：*西兰花、胡萝卜、鸡蛋、荞麦面、玉米、莴笋、紫薯*\",\n" +
                           "      \"id\": \"markdown_1653901065785\"\n" +
                           "    },\n" +
                           "    {\n" +
                           "      \"type\": \"section\",\n" +
                           "      \"content\": {\n" +
                           "        \"type\": \"text\",\n" +
                           "        \"text\": \"主菜选择：\",\n" +
                           "        \"id\": \"text_1653901065785\"\n" +
                           "      },\n" +
                           "      \"extra\": {\n" +
                           "        \"type\": \"select\",\n" +
                           "        \"options\": [\n" +
                           "          {\n" +
                           "            \"label\": {\n" +
                           "              \"type\": \"text\",\n" +
                           "              \"text\": \"? 鸡肉\",\n" +
                           "              \"id\": \"text_1653901065786\"\n" +
                           "            },\n" +
                           "            \"value\": \"1\"\n" +
                           "          },\n" +
                           "          {\n" +
                           "            \"label\": {\n" +
                           "              \"type\": \"text\",\n" +
                           "              \"text\": \"? 牛肉\",\n" +
                           "              \"id\": \"text_1653901065870\"\n" +
                           "            },\n" +
                           "            \"value\": \"2\"\n" +
                           "          }\n" +
                           "        ],\n" +
                           "        \"placeholder\": {\n" +
                           "          \"type\": \"text\",\n" +
                           "          \"text\": \"请选择\",\n" +
                           "          \"id\": \"text_1653901065835\"\n" +
                           "        },\n" +
                           "        \"id\": \"select_1647330112516\"\n" +
                           "      },\n" +
                           "      \"id\": \"section_1653901065785\"\n" +
                           "    },\n" +
                           "    {\n" +
                           "      \"type\": \"section\",\n" +
                           "      \"content\": {\n" +
                           "        \"type\": \"text\",\n" +
                           "        \"text\": \"取餐地点：\",\n" +
                           "        \"id\": \"text_1653901065850\"\n" +
                           "      },\n" +
                           "      \"extra\": {\n" +
                           "        \"type\": \"select\",\n" +
                           "        \"options\": [\n" +
                           "          {\n" +
                           "            \"label\": {\n" +
                           "              \"type\": \"text\",\n" +
                           "              \"text\": \"5号楼取餐点\",\n" +
                           "              \"id\": \"text_1653901065847\"\n" +
                           "            },\n" +
                           "            \"value\": \"1\"\n" +
                           "          },\n" +
                           "          {\n" +
                           "            \"label\": {\n" +
                           "              \"type\": \"text\",\n" +
                           "              \"text\": \"10号楼取餐点\",\n" +
                           "              \"id\": \"text_1653901065912\"\n" +
                           "            },\n" +
                           "            \"value\": \"2\"\n" +
                           "          },\n" +
                           "          {\n" +
                           "            \"label\": {\n" +
                           "              \"type\": \"text\",\n" +
                           "              \"text\": \"餐厅服务台\",\n" +
                           "              \"id\": \"text_1653901065845\"\n" +
                           "            },\n" +
                           "            \"value\": \"3\"\n" +
                           "          }\n" +
                           "        ],\n" +
                           "        \"placeholder\": {\n" +
                           "          \"type\": \"text\",\n" +
                           "          \"text\": \"请选择\",\n" +
                           "          \"id\": \"text_1653901065892\"\n" +
                           "        },\n" +
                           "        \"id\": \"select_1647330167899\"\n" +
                           "      },\n" +
                           "      \"id\": \"section_1653901065862\"\n" +
                           "    },\n" +
                           "    {\n" +
                           "      \"type\": \"action\",\n" +
                           "      \"actions\": [\n" +
                           "        {\n" +
                           "          \"type\": \"button\",\n" +
                           "          \"label\": {\n" +
                           "            \"type\": \"text\",\n" +
                           "            \"text\": \"一键预定\",\n" +
                           "            \"id\": \"text_1653901065910\"\n" +
                           "          },\n" +
                           "          \"actionType\": \"request\",\n" +
                           "          \"status\": \"primary\",\n" +
                           "          \"id\": \"button_1647330333211\"\n" +
                           "        }\n" +
                           "      ],\n" +
                           "      \"id\": \"action_1653901065786\"\n" +
                           "    },\n" +
                           "    {\n" +
                           "      \"type\": \"divider\",\n" +
                           "      \"id\": \"divider_1653901065786\"\n" +
                           "    },\n" +
                           "    {\n" +
                           "      \"type\": \"markdown\",\n" +
                           "      \"text\": \"**3月15日健康餐已预定：24/40 份**\",\n" +
                           "      \"id\": \"markdown_1653901065786\"\n" +
                           "    },\n" +
                           "    {\n" +
                           "      \"type\": \"markdown\",\n" +
                           "      \"text\": \"<font color=common_level3_base_color>赫莎莎 牛肉套餐</font>\",\n" +
                           "      \"icon\": \"@lALPDsCJC3kB4IYwMA\",\n" +
                           "      \"id\": \"markdown_1653901065823\"\n" +
                           "    },\n" +
                           "    {\n" +
                           "      \"type\": \"markdown\",\n" +
                           "      \"text\": \"<font color=common_level3_base_color>周小丽 牛肉套餐</font>\",\n" +
                           "      \"icon\": \"@lALPDsekCMKd0tMwMA\",\n" +
                           "      \"id\": \"markdown_1653901065846\"\n" +
                           "    },\n" +
                           "    {\n" +
                           "      \"type\": \"markdown\",\n" +
                           "      \"text\": \"<font color=common_level3_base_color>黄敏敏 牛肉套餐</font>\",\n" +
                           "      \"icon\": \"@lALPEBkmB-g2_NIwMA\",\n" +
                           "      \"id\": \"markdown_1653901065886\"\n" +
                           "    },\n" +
                           "    {\n" +
                           "      \"type\": \"action\",\n" +
                           "      \"actions\": [\n" +
                           "        {\n" +
                           "          \"type\": \"button\",\n" +
                           "          \"label\": {\n" +
                           "            \"type\": \"text\",\n" +
                           "            \"text\": \"查看全部\",\n" +
                           "            \"id\": \"text_1653901065843\"\n" +
                           "          },\n" +
                           "          \"actionType\": \"openLink\",\n" +
                           "          \"url\": {\n" +
                           "            \"all\": \"https://www.dingtalk.com\"\n" +
                           "          },\n" +
                           "          \"status\": \"normal\",\n" +
                           "          \"id\": \"button_1647330728999\"\n" +
                           "        }\n" +
                           "      ],\n" +
                           "      \"id\": \"action_1653901065859\"\n" +
                           "    }\n" +
                           "  ]\n" +
                           "}")
                   .setSendOptions(sendOptions);
           try {
               SendRobotInteractiveCardResponse sendRobotInteractiveCardResponse = client.sendRobotInteractiveCardWithOptions(sendRobotInteractiveCardRequest, sendRobotInteractiveCardHeaders, new RuntimeOptions());
               System.out.println(JSON.toJSONString(sendRobotInteractiveCardResponse.getBody()));
           } catch (TeaException err) {
               if (!com.aliyun.teautil.Common.empty(err.code) && !com.aliyun.teautil.Common.empty(err.message)) {
                   // err 中含有 code 和 message 属性，可帮助开发定位问题
                   System.out.println(err.code);
                   System.out.println(err.message);
               }

           } catch (Exception _err) {
               TeaException err = new TeaException(_err.getMessage(), _err);
               if (!com.aliyun.teautil.Common.empty(err.code) && !com.aliyun.teautil.Common.empty(err.message)) {
                   // err 中含有 code 和 message 属性，可帮助开发定位问题
                   System.out.println(err.code);
                   System.out.println(err.message);
               }
           }
       }
   ```
3. 调用新版服务端API-[更新机器人发送互动卡片（普通版）](../../01-应用开发/02-4a8AMF6u2A-服务端API/1477-update-the-robot-to-send-interactive-cards.md)接口，实现互动卡片发送。

   ```
    public void interactiveCardsUpdate() throws Exception {
           Config config = new Config();
           config.protocol = "https";
           config.regionId = "central";
           com.aliyun.dingtalkim_1_0.Client client = new Client(config);
           UpdateRobotInteractiveCardHeaders updateRobotInteractiveCardHeaders = new UpdateRobotInteractiveCardHeaders();
           updateRobotInteractiveCardHeaders.xAcsDingtalkAccessToken = "<your access token>";
           UpdateRobotInteractiveCardRequest.UpdateRobotInteractiveCardRequestUpdateOptions updateOptions = new UpdateRobotInteractiveCardRequest.UpdateRobotInteractiveCardRequestUpdateOptions()
                   .setUpdateCardDataByKey(true);
           UpdateRobotInteractiveCardRequest updateRobotInteractiveCardRequest = new UpdateRobotInteractiveCardRequest()
                   .setCardBizId("dingCard1001")
                   .setCardData("{\"contents\": [\n" +
                           "    {\n" +
                           "      \"type\": \"image\",\n" +
                           "      \"image\": \"@lALPDfYH0aWc_a3NAljNAyA\",\n" +
                           "      \"ratio\": \"16:9\",\n" +
                           "      \"id\": \"image_1653901065785\"\n" +
                           "    },\n" +
                           "    {\n" +
                           "      \"type\": \"markdown\",\n" +
                           "      \"text\": \"套餐内容：*西兰花、胡萝卜、鸡蛋、荞麦面、玉米、莴笋、紫薯*\",\n" +
                           "      \"id\": \"markdown_1653901065785\"\n" +
                           "    },\n" +
                           "    {\n" +
                           "      \"type\": \"section\",\n" +
                           "      \"content\": {\n" +
                           "        \"type\": \"text\",\n" +
                           "        \"text\": \"主菜选择：\",\n" +
                           "        \"id\": \"text_1653901065785\"\n" +
                           "      },\n" +
                           "      \"extra\": {\n" +
                           "        \"type\": \"select\",\n" +
                           "        \"options\": [\n" +
                           "          {\n" +
                           "            \"label\": {\n" +
                           "              \"type\": \"text\",\n" +
                           "              \"text\": \"? 鸡肉\",\n" +
                           "              \"id\": \"text_1653901065786\"\n" +
                           "            },\n" +
                           "            \"value\": \"1\"\n" +
                           "          },\n" +
                           "          {\n" +
                           "            \"label\": {\n" +
                           "              \"type\": \"text\",\n" +
                           "              \"text\": \"? 牛肉\",\n" +
                           "              \"id\": \"text_1653901065870\"\n" +
                           "            },\n" +
                           "            \"value\": \"2\"\n" +
                           "          }\n" +
                           "        ],\n" +
                           "        \"placeholder\": {\n" +
                           "          \"type\": \"text\",\n" +
                           "          \"text\": \"请选择\",\n" +
                           "          \"id\": \"text_1653901065835\"\n" +
                           "        },\n" +
                           "        \"id\": \"select_1647330112516\"\n" +
                           "      },\n" +
                           "      \"id\": \"section_1653901065785\"\n" +
                           "    },\n" +
                           "    {\n" +
                           "      \"type\": \"section\",\n" +
                           "      \"content\": {\n" +
                           "        \"type\": \"text\",\n" +
                           "        \"text\": \"取餐地点：\",\n" +
                           "        \"id\": \"text_1653901065850\"\n" +
                           "      },\n" +
                           "      \"extra\": {\n" +
                           "        \"type\": \"select\",\n" +
                           "        \"options\": [\n" +
                           "          {\n" +
                           "            \"label\": {\n" +
                           "              \"type\": \"text\",\n" +
                           "              \"text\": \"5号楼取餐点\",\n" +
                           "              \"id\": \"text_1653901065847\"\n" +
                           "            },\n" +
                           "            \"value\": \"1\"\n" +
                           "          },\n" +
                           "          {\n" +
                           "            \"label\": {\n" +
                           "              \"type\": \"text\",\n" +
                           "              \"text\": \"10号楼取餐点\",\n" +
                           "              \"id\": \"text_1653901065912\"\n" +
                           "            },\n" +
                           "            \"value\": \"2\"\n" +
                           "          },\n" +
                           "          {\n" +
                           "            \"label\": {\n" +
                           "              \"type\": \"text\",\n" +
                           "              \"text\": \"餐厅服务台\",\n" +
                           "              \"id\": \"text_1653901065845\"\n" +
                           "            },\n" +
                           "            \"value\": \"3\"\n" +
                           "          }\n" +
                           "        ],\n" +
                           "        \"placeholder\": {\n" +
                           "          \"type\": \"text\",\n" +
                           "          \"text\": \"请选择\",\n" +
                           "          \"id\": \"text_1653901065892\"\n" +
                           "        },\n" +
                           "        \"id\": \"select_1647330167899\"\n" +
                           "      },\n" +
                           "      \"id\": \"section_1653901065862\"\n" +
                           "    },\n" +
                           "    {\n" +
                           "      \"type\": \"action\",\n" +
                           "      \"actions\": [\n" +
                           "        {\n" +
                           "          \"type\": \"button\",\n" +
                           "          \"label\": {\n" +
                           "            \"type\": \"text\",\n" +
                           "            \"text\": \"一键预定\",\n" +
                           "            \"id\": \"text_1653901065910\"\n" +
                           "          },\n" +
                           "          \"actionType\": \"request\",\n" +
                           "          \"status\": \"primary\",\n" +
                           "          \"id\": \"button_1647330333211\",\n" +
                           "          \"value\": \"1\"\n" +
                           "        }\n" +
                           "      ],\n" +
                           "      \"id\": \"action_1653901065786\"\n" +
                           "    },\n" +
                           "    {\n" +
                           "      \"type\": \"divider\",\n" +
                           "      \"id\": \"divider_1653901065786\"\n" +
                           "    },\n" +
                           "    {\n" +
                           "      \"type\": \"markdown\",\n" +
                           "      \"text\": \"**6月1日健康餐已预定：23/40 份**\",\n" +
                           "      \"id\": \"markdown_1653901065786\"\n" +
                           "    },\n" +
                           "    {\n" +
                           "      \"type\": \"markdown\",\n" +
                           "      \"text\": \"<font color=common_level3_base_color>小钉 牛肉套餐</font>\",\n" +
                           "      \"icon\": \"@lALPDsCJC3kB4IYwMA\",\n" +
                           "      \"id\": \"markdown_1653901065823\"\n" +
                           "    },\n" +
                           "    {\n" +
                           "      \"type\": \"markdown\",\n" +
                           "      \"text\": \"<font color=common_level3_base_color>赫莎莎 牛肉套餐</font>\",\n" +
                           "      \"icon\": \"@lALPDsekCMKd0tMwMA\",\n" +
                           "      \"id\": \"markdown_1653901065846\"\n" +
                           "    },\n" +
                           "    {\n" +
                           "      \"type\": \"markdown\",\n" +
                           "      \"text\": \"<font color=common_level3_base_color>周小丽 牛肉套餐</font>\",\n" +
                           "      \"icon\": \"@lALPEBkmB-g2_NIwMA\",\n" +
                           "      \"id\": \"markdown_1653901065886\"\n" +
                           "    },\n" +
                           "    {\n" +
                           "      \"type\": \"action\",\n" +
                           "      \"actions\": [\n" +
                           "        {\n" +
                           "          \"type\": \"button\",\n" +
                           "          \"label\": {\n" +
                           "            \"type\": \"text\",\n" +
                           "            \"text\": \"查看全部\",\n" +
                           "            \"id\": \"text_1653901065843\"\n" +
                           "          },\n" +
                           "          \"actionType\": \"openLink\",\n" +
                           "          \"url\": {\n" +
                           "            \"all\": \"https://www.dingtalk.com\"\n" +
                           "          },\n" +
                           "          \"status\": \"normal\",\n" +
                           "          \"id\": \"button_1647330728999\"\n" +
                           "        }\n" +
                           "      ],\n" +
                           "      \"id\": \"action_1653901065859\"\n" +
                           "    }\n" +
                           "  ]}")
                   .setUpdateOptions(updateOptions);
           try {
               UpdateRobotInteractiveCardResponse updateRobotInteractiveCardResponse = client.updateRobotInteractiveCardWithOptions(updateRobotInteractiveCardRequest, updateRobotInteractiveCardHeaders, new RuntimeOptions());
               System.out.println(JSON.toJSONString(updateRobotInteractiveCardResponse.getBody()));
           } catch (TeaException err) {
               if (!com.aliyun.teautil.Common.empty(err.code) && !com.aliyun.teautil.Common.empty(err.message)) {
                   // err 中含有 code 和 message 属性，可帮助开发定位问题
                   System.out.println(err.code);
                   System.out.println(err.message);
               }

           } catch (Exception _err) {
               TeaException err = new TeaException(_err.getMessage(), _err);
               if (!com.aliyun.teautil.Common.empty(err.code) && !com.aliyun.teautil.Common.empty(err.message)) {
                   // err 中含有 code 和 message 属性，可帮助开发定位问题
                   System.out.println(err.code);
                   System.out.println(err.message);
               }
           }
       }
   ```
