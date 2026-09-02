---
title: "成员资料页扩展互动卡片能力"
source_url: "https://open.dingtalk.com/document/dingstart/member-information-page-expands-interactive-card-capability-beta"
namespace: "dingstart"
slug: "member-information-page-expands-interactive-card-capability-beta"
group: "应用开发"
tab: "开发指南"
breadcrumb: "开发酷应用 > 开发成员资料页酷应用 > 成员资料页扩展互动卡片能力"
doc_id: "hQ7Yq6Dvmx"
updated_at: "2026-06-30 09:01:04"
---

> Source: https://open.dingtalk.com/document/dingstart/member-information-page-expands-interactive-card-capability-beta
> Path: 应用开发 / 开发指南 / 开发酷应用 > 开发成员资料页酷应用 > 成员资料页扩展互动卡片能力
> Updated: 2026-06-30 09:01:04

# 成员资料页扩展互动卡片能力

本文介绍如何在成员资料页中通过酷应用实现互动卡片的数据响应与动态交互功能。通过该能力，开发者可在用户查看成员资料时，动态渲染自定义业务数据卡片，并支持用户点击交互后的回调处理。

> **[!NOTE]**
>
> HTTP回调必须是POST方法，**path必须和功能设计设置的卡片回调path相同。**

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4621872871/p521278.png)

```
@RestController
@Slf4j
public class CardCallBackController {

    @Value("${card.callback.apiSecret:test}")
    private String apiSecret;

    @RequestMapping(value = "/profile/card/callback", method = RequestMethod.POST)
    public DynamicDataCallbackResponseDTO callBack(HttpServletRequest request, @RequestBody(required = false) DynamicDataCallbackRequestDTO cardCallBackVO) {
        String content = cardCallBackVO.getContent();
        log.info(JSON.toJSONString(cardCallBackVO));
        Long signatureTimestamp = Long.valueOf(request.getHeader("x-ddpaas-signature-timestamp"));
        String signature = request.getHeader("x-ddpaas-signature");
        String calcSignature = calcSignature(apiSecret, signatureTimestamp);
        log.info("signature==>" + signature + ",calcSignature==>" + calcSignature);
//        if (!calcSignature.equalsIgnoreCase(signature)) {
//            log.warn("signature==>" + signature + ",calcSignature==>" + calcSignature);
//            return null;
//        }

        DynamicDataSourceContextRequestDTO contextRequestDTO = JSON.parseObject(content, DynamicDataSourceContextRequestDTO.class);
        String profile = contextRequestDTO.getDynamicDataSourceQueryRequests().get(0).getDynamicParams().get("profile");
        JSONObject profileJsonObject = JSON.parseObject(profile);
        String targetUserId = (String) profileJsonObject.get("userId");
        JSONObject object = new JSONObject();
        JSONArray data1 = new JSONArray();
        data1.add(object);
        DynamicDataCallbackResponseDTO responseDTO = new DynamicDataCallbackResponseDTO();
        DynamicDataCallbackResponseDTO.DataSourceQueryResponseDTO sourceQueryResponseDTO = new DynamicDataCallbackResponseDTO.DataSourceQueryResponseDTO();
        sourceQueryResponseDTO.setDynamicDataSourceId("ds.profile");
        sourceQueryResponseDTO.setDynamicDataValueType(OpenDynamicDataValueTypeEnum.OBJECT);
        JSONObject data = new JSONObject();
        data.put("data1", data1);
        sourceQueryResponseDTO.setData(JSON.toJSONString(data));
        List<DynamicDataCallbackResponseDTO.DataSourceQueryResponseDTO> sourceQueryResponseDTOS = new ArrayList<>();
        sourceQueryResponseDTOS.add(sourceQueryResponseDTO);
        responseDTO.setDataSourceQueryResponses(sourceQueryResponseDTOS);
        log.info(JSON.toJSONString(responseDTO));
        return responseDTO;
    }

    public static String calcSignature(String apiSecret, long ts) {
        try {
            Mac mac = Mac.getInstance("HmacSHA256");
            SecretKeySpec key = new SecretKeySpec(apiSecret.getBytes(), "HmacSHA256");
            mac.init(key);
            return Base64.getEncoder()
                    .encodeToString(mac.doFinal(Long.toString(ts).getBytes()));
        } catch (NoSuchAlgorithmException | InvalidKeyException e) {
            throw new RuntimeException("sign api secret failed", e);
        }
    }
}
```

## **Http回调入参数据模型**

**浏览成员资料页页面：**

```
{
  "content": "{\"dynamicDataSourceQueryRequests\":[{\"dynamicDataSourceId\":\"ds.profile\",\"dynamicParams\":{\"profile\":\"{\\\"corpId\\\":\\\"dingxx\\\",\\\"userId\\\":\\\"0153534058xxxx\\\"}\"}}]}",
  "corpId": "dingxxx",
  "outTrackId": "COOLAPP-10-10******08213F1A0A0007.f3c286ca-****-****-****-5f250e051600",
  "type": "dynamicDataCallback",
  "userId": "016801115xxx"
}
```

**点击成员资料页卡片：**

```
{
  "content": "{\"cardPrivateData\":{\"actionIds\":[\"like\"],\"params\":{\"like\":\"1\",\"likeNum\":26}}}",
  "corpId": "ding241f3******b35c2f4657eb6378f",
  "outTrackId": "COOLAPP-10-10******08213F1A0A0007.f3c286ca-****-****-****-5f250e051600",
  "type": "actionCallback",
  "userId": "016801115xxx"
}
```

| **名称** | **类型** | **说明** |
| --- | --- | --- |
| userId | String | 操作人用户userId。 |
| type | String | 回调类型：   - dynamicDataCallback 获取数据源 - actionCallback 卡片点击数据回传 |
| outTrackId | String | 卡片实例唯一标识。 |
| corpId | String | 所属企业ID，从不同的入口进入成员资料页，企业ID不同。   - **内部群&外部群**查看成员资料页：返回该内部群&外部群所属的企业ID。  image - **单聊&普通群**查看成员资料页：返回被查看人的**主企业ID**。  image  **[!NOTE]**  个人主企业可以从以下路径查看 **移动端 > 左上角个人头像 > 点击个人头像 >企业/团队。** |
| content | String | profile操作上下文，包含：   - dynamicParams.profile    - **corpId**: 被查看人企业ID   - **userId**：被查看人所在企业的用户userId - cardPrivateData（卡片数据回传时才会有）    - **actionIds**：点击选中的前端控件ID，示例如下图：  image   - **params**：数据回传具体参数，示例如下图：  image |

## **响应数据模型**

```
{
  "dataSourceQueryResponses": [
    {
      "data": "{\"profileUrl\":\"www.dingtalk.com\",\"profilePcUrl\":\"www.dingtalk.com\",\"isProfileOwner\":false,\"okrs\":[{\"name\":\"这是小钉小号新的目标，(进度会刷新)\",\"progress\":40}]}",
      "dynamicDataSourceId": "ds.profile",
      "dynamicDataValueType": "OBJECT"
    }
  ]
}
```

业务方响应钉钉侧参数说明（出参）：

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| data | String | 渲染卡片的私有数据对象，适合于设置每个人看到的不一样的卡片内容。  **[!IMPORTANT]**  data必须是jsonString类型。 |
| dynamicDataSourceId | String | 数据源类型，目前钉钉平台要求必须返回固定值 `ds.profile`。 |
| dynamicDataValueType | String | 数据源data返回数据格式，目前钉钉平台要求必须返回固定值 `OBJECT`。 |
