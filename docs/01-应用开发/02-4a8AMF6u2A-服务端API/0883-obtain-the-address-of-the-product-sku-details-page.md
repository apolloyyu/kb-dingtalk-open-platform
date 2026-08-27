---
title: "获取内购商品SKU页面地址"
source_url: "https://open.dingtalk.com/document/development/obtain-the-address-of-the-product-sku-details-page"
namespace: "development"
slug: "obtain-the-address-of-the-product-sku-details-page"
group: "应用开发"
tab: "服务端API"
breadcrumb: "应用市场 > 应用内购 > 获取内购商品SKU页面地址"
doc_id: "BgwBOGE2Wa"
updated_at: "2026-06-08 09:43:52"
---

> Source: https://open.dingtalk.com/document/development/obtain-the-address-of-the-product-sku-details-page
> Path: 应用开发 / 服务端API / 应用市场 > 应用内购 > 获取内购商品SKU页面地址
> Updated: 2026-06-08 09:43:52

# 获取内购商品SKU页面地址

通过此接口获取内购商品的SKU选择页面地址，用于在应用中跳转至指定商品的规格选择页。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/appstore/internal/skupage/get |
| HTTP Method | POST |
| 支持的应用类型 | appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_appstore\_internal-开通应用在应用市场的内购订单的数据管理权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用本接口的访问凭证，通过调用获[服务商获取第三方应用授权企业的access\_token](1448-obtain-isvapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| goods\_code | String | 是 | FW\_GOODS\_1111 | 内购商品码。iShot2022-09-20 11 |
| callback\_page | String | 否 | http%3A//dingtalk.com%3Fa%3Db | 回调页面地址（需经过URL编码），微应用填写页面URL，E应用填写页面路径地址。  **[!IMPORTANT]**  http模式下，页面地址必须与应用的主域名一致，否则无法正常跳转。 |
| extend\_param | String | 否 | %7B%22outDefinedPrice%22%3A19999%7D | 调用方扩展参数。   - 若为**非固定规格**内购商品，该参数必填，且必须进行 **UrlEncode** 处理，用于指定商品价格。  参数格式为{"outDefinedPrice":199}，表示该商品价格为1.99元。 - 如果是**固定规格**内购商品，该参数可不填写。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/appstore/internal/skupage/get" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=fa1306c4-9c88-4ecf-bc76-bb3622a27c7b' \
-d 'callback_page=http%253A%2F%2Fdingtalk.com%253Fa%253Db' \
-d 'extend_param=11111111' \
-d 'goods_code=FW_GOODS_1111'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/appstore/internal/skupage/get");
OapiAppstoreInternalSkupageGetRequest req = new OapiAppstoreInternalSkupageGetRequest();
req.setGoodsCode("FW_GOODS_1111");
req.setCallbackPage("http%3A//dingtalk.com%3Fa%3Db");
req.setExtendParam("%7B%22outDefinedPrice%22%3A19999%7D");
OapiAppstoreInternalSkupageGetResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiAppstoreInternalSkupageGetRequest("https://oapi.dingtalk.com/topapi/appstore/internal/skupage/get")

req.goods_code="FW_GOODS_1111"
req.callback_page="http%3A//dingtalk.com%3Fa%3Db"
req.extend_param="11111111"
try:
  resp= req.getResponse(access_token)
  print(resp)
except Exception,e:
  print(e)
```

PHP

```
include "TopSdk.php";
date_default_timezone_set('Asia/Shanghai');

$c = new DingTalkClient(DingTalkConstant::$CALL_TYPE_OAPI, DingTalkConstant::$METHOD_POST , DingTalkConstant::$FORMAT_JSON);
$req = new OapiAppstoreInternalSkupageGetRequest;
$req->setGoodsCode("FW_GOODS_1111");
$req->setCallbackPage("http%3A//dingtalk.com%3Fa%3Db");
$req->setExtendParam("11111111");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/appstore/internal/skupage/get");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/appstore/internal/skupage/get");
OapiAppstoreInternalSkupageGetRequest req = new OapiAppstoreInternalSkupageGetRequest();
req.GoodsCode = "FW_GOODS_1111";
req.CallbackPage = "http%3A//dingtalk.com%3Fa%3Db";
req.ExtendParam = "11111111";
OapiAppstoreInternalSkupageGetResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | String | https://dingtalk.com | 内购商品SKU页面地址。 |
| errmsg | String | ok | 返回码描述。 |
| errcode | Number | 0 | 返回码。 |

### **响应体示例**

```
{
  "result":"https://dingtalk.com",
  "errcode":"0",
  "errmsg":"ok"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

## 应用链接跳转到SKU页面地址

### **移动端**

| **应用类型** | **打开方法** |
| --- | --- |
| H5微应用 | 调用前端JSAPI-[打开目标页面](https://open.dingtalk.com/document/isvapp/open-the-target-page)。 |
| 小程序 | 1. 目标页面引入dingtalk-jsapi。      ```    import 'dingtalk-jsapi/entry/mobile';    import openLink from 'dingtalk-jsapi/api/biz/util/openLink';    ``` 2. 在当前页面调用openLink跳转sku页面。      ```     openLink(){        openLink({          url:"https:\/\/h5.dingtalk.com\/open-mxxxxx"        })      },    ``` |

### **PC端**

PC端应用打开侧边栏，可以使用JSAPI-[打开侧边面板](https://open.dingtalk.com/document/isvapp/open-side-panel)。
