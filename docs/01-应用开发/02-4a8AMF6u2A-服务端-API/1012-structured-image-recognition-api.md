---
title: "OCR文字识别"
source_url: "https://open.dingtalk.com/document/development/structured-image-recognition-api"
namespace: "development"
slug: "structured-image-recognition-api"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "行业与生态 > 生态开放 > AI > OCR文字识别"
doc_id: "GmQYnoAIsl"
updated_at: "2026-06-03 09:51:00"
---

> Source: https://open.dingtalk.com/document/development/structured-image-recognition-api
> Path: 应用开发 / 服务端 API / 行业与生态 > 生态开放 > AI > OCR文字识别
> Updated: 2026-06-03 09:51:00

# OCR文字识别

通过本接口可实现对图片中文字的自动识别（OCR），支持身份证、发票、银行卡等多种常见证照和票据类型的结构化信息提取，适用于企业自动化办公、财务报销、人事管理等场景。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/ocr/structured/recognize |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用appType-第三方企业应用 |
| 权限要求 | permission-`qyapi_ocr_structured`-ocr结构化图片识别能力的权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6ed1bxxx | 调用该API的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 - 第三方企业应用，通过[获取第三方企业的access\_token](1448-obtain-isvapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| type | String | 是 | idcard | 识别图片类型。   - **idcard**：身份证 - **invoice**：营业执照增值税发票 - **blicense**：营业执照 - **bank\_card**：银行卡 - **car\_no**：车牌 - **car\_invoice**：机动车发票 - **driving\_license**：驾驶证 - **vehicle\_license**：行驶证 - **train\_ticket**：火车票 - **quota\_invoice**：定额发票 - **taxi\_ticket**：出租车发票 - **air\_itinerary**：机票行程单 - **approval\_table**：审批表单 - **roster**：花名册 |
| image\_url | String | 是 | https://img.alicdn.com/tfs/TB1d7H1NNjaK1Rxxxxx.png | 识别图片地址，最大长度1000。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/ocr/structured/recognize" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=76bd22xxxx8728a' \
-d 'type=idcard' \
-d 'image_url=https://img.alicdn.com/tfs/TB1d7H1NNjaK1Rxxxxx.png'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/ocr/structured/recognize");
OapiOcrStructuredRecognizeRequest req = new OapiOcrStructuredRecognizeRequest();
req.setType("idcard");
req.setImageUrl("https://img.alicdn.com/tfs/TB1d7H1NNjaK1Rxxxxx.png");
OapiOcrStructuredRecognizeResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiOcrStructuredRecognizeRequest("https://oapi.dingtalk.com/topapi/ocr/structured/recognize")

req.type="idcard"
req.image_url="https://img.alicdn.com/tfs/TB1d7H1NNjaK1Rxxxxx.png"
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
$req = new OapiOcrStructuredRecognizeRequest;
$req->setType("idcard");
$req->setImageUrl("https://img.alicdn.com/tfs/TB1d7H1NNjaK1Rxxxxx.png");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/ocr/structured/recognize");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/ocr/structured/recognize");
OapiOcrStructuredRecognizeRequest req = new OapiOcrStructuredRecognizeRequest();
req.setType("idcard");
req.setImageUrl("https://img.alicdn.com/tfs/TB1d7H1NNjaK1Rxxxxx.png");
OapiOcrStructuredRecognizeResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| request\_id | String | xbax90pszo2q | 请求ID。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| result | OcrStructuredResult | {} | 识别结果。 |
| height | Number | 100 | 旋转后图片高度。 |
| width | Number | 100 | 旋转后图片宽度。 |
| angle | Number | 100 | 旋转度。 |
| data | String | {} | 图片识别内容json字符串，不同的类型有不同的字段。  例如，身份证{"姓名":"王xx","性别":"男","民族":"汉","出生日期":"1986年1月9日","住址":"四川省攀枝xxxx","身份证号码":"5101241988xxxxx"}。 |
| original\_height | Number | 100 | 原始图片高度。 |
| original\_width | Number | 100 | 原始图片宽度。 |

### **响应体示例**

```
{
        "errcode":"0",
        "result":{
                "original_width":"100",
                "data":"{}",
                "width":"100",
                "angle":"100",
                "original_height":"100",
                "height":"100"
        },
        "errmsg":"success",
        "request_id":"xbax90pszo2q"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

## 图片类型返回数据示例

1. 身份证识别正面(包含字块，单字及坐标信息)：

   ```
   {
       "code": 200,
        "data": {
            "姓名": "潘xxx",
            "性别": "男",
            "民族": "汉",
            "出生日期": "1986年1月9日",
            "住址": "四川省xxxxx",
            "身份证号码": "510132xxxxx"
           },
          //原图高度
           "orgHeight": 416,
           //原图宽度
          "orgWidth": 629,
          //旋转后图片高度
           "height": 416,
           //旋转后图片宽度
           "width": 629,   
           "sid": "5f3c4afxxxxx3a75e9f440517f0",
           "angle": 359   
   }
   ```
2. 身份证识别反面：

   ```
   {
    //请求结果code，200为请求成功，非200为请求失败
    "code": 200,
    "data": {
      "签发机关": "建瓯市公安局",
      "有效期限": "2012.06.25-2022.06.25"
    },
     //原图高度
     "orgHeight": 416,
     //原图宽度
     "orgWidth": 629,
     //旋转后图片高度
     "height": 416,
     //旋转后图片宽度
     "width": 629,
     "sid": "81318ebf846d52086xxxxxxxxx9ef153a84b0e01",
     "angle": 359
   }
   ```
3. 增值税发票识别：

   ```
   {
      //请求结果code，200为请求成功，非200为请求失败
       "code": 200,
       "data": {
           "发票代码": "03100xxx",
           "发票号码": "675xxx",
           "开票日期": "2017年2月12日",
           "校验码": "628503xxxx",
           "发票金额": "88.00",
           "大写金额": "88",
           "发票税额": "12.79",
           "不含税金额": "75.21",
           "受票方名称": "*宏伟",
           "受票方税号": "123312",
           "受票方地址、电话": "",
           "受票方开户行、账号": "",
           "销售方名称": "上海电子商务有限公司",
           "销售方税号": "913101xxxxx",
           "销售方地址、电话": "上海市xxxx",
           "销售方开户行、账号": "中国银行股份有限公司",
           "发票详单": "[xxx]",
           发票代码解析": "{xxxx}",
           },
           //原图高度
          "orgHeight": 416,
          //原图宽度
          "orgWidth": 629,
          //旋转后图片高度
          "height": 416,
          //旋转后图片宽度
          "width": 629,
           "sid": "81318ebf846dxxxxx339ef153a84b0e01",
           "angle": 359
   }
   ```
4. 汽车发票识别：

   ```
   {
      //请求结果code，200为请求成功，非200为请求失败
       "code": 200,
       "data": {
           "发票代码": "03xxxx",
           "发票号码": "67516978",
           "开票日期": "2017年2月12日",
           "购买方名称": "顾爽",
           "购买方身份证号码/组织机构代码": "22xxxx",
           "购买方纳税人识别号": "88",
           "车辆类型": "轿车",
           "厂牌型号": "CAxxxxA",
           "产地": "长春市",
           "合格证号": "HAAxxxx",
           "进口证明书号": "",
           "商检单号": "",
           "发动机号码": "158070",
           "车辆识别代号/车架号码": "FPxxx",
           "价税合计（大写）": "",
           "价税合计（小写）": "69800.00",
           "销货单位名称": "长原公司",
           "销货单位电话": "0431-81336176",
           "销货单位纳税人识别号": "9122xxxx",
           "销货单位账号": "07306xxxx",
           "销货单位地址": "长春巾xxxx",
           "销货单位开户银行": "吉专城xxx",
           "增值税税率或征收率": "17%",
           "增值税税额": "10141.88",
           "主管税务机关及代码": "长市高xxxx",
           "不含税价": "59658.12",
           "完税凭证号码": "",
           "吨位": "1",
           "限乘人数": "5"
        },
       //原图高度
       "orgHeight": 416,
       //原图宽度
       "orgWidth": 629,
       //旋转后图片高度
       "height": 416,
       //旋转后图片宽度
       "width": 629,
       "sid": "11318exxxx3a84b0e01",
       "angle": 359
   }
   ```
5. 银行卡识别：

   ```
   {
      //请求结果code，200为请求成功，非200为请求失败
       "code": 200,
       "data": {
           "银行卡卡号": "631xxxx"
         },
      //原图高度
       "orgHeight": 416,
      //原图宽度
       "orgWidth": 629,
      //旋转后图片高度
       "height": 416,
      //旋转后图片宽度
       "width": 629,
       "sid": "22318ebf84xxxxb0e01",
       "angle": 359
   }
   ```
6. 行驶证识别：

   ```
   {
      //请求结果code，200为请求成功，非200为请求失败
       "code": 200,
       "data": {
          "号牌号码": "粤BW726N",
          "车辆类型": "小型轿车",
          "所有人": "魏军",
          "住址": "深圳市xxxx",
          "使用性质": "非营运",
          "品牌型号": "丰田牌xxxx",
          "车辆识别代号": "LFMxxx",
          "发动机号码": "E350316",
          "注册日期": "2009年4月30日",
          "发证日期": "2009-04-30"
         },
        //原图高度
        "orgHeight": 416,
        //原图宽度
        "orgWidth": 629,
        //旋转后图片高度
        "height": 416,
        //旋转后图片宽度
        "width": 629,
        "sid": "44318ebf846xxxxxxx9ef153a84b0e01",
        "angle": 359
   }
   ```
7. 驾驶证识别：

   ```
   {
      //请求结果code，200为请求成功，非200为请求失败
       "code": 200,
       "data": {
          "证号": "4209xxxx",
          "姓名": "徐xx",
          "性别": "男",
          "国籍": "中国",
          "住址": "湖北省xxx",
          "发证单位": "湖北省xxx",
          "出生日期": "1993年5月16日",
          "初次领证日期": "2015-02-12",
          "准驾车型": "C1",
          "有效起始日期": "2015-02-12",
          "有效期限": "2015-02-12至2021-02-12"
        },
        //原图高度
        "orgHeight": 416,
        //原图宽度
        "orgWidth": 629,
        //旋转后图片高度
        "height": 416,
        //旋转后图片宽度
        "width": 629,
         "sid": "55318ebf8xxxxxx3a84b0e01",
         "angle": 359
   }
   ```
8. 车牌识别：

   ```
   {
      //请求结果code，200为请求成功，非200为请求失败
       "code": 200,
       "data": {
            "汽车车牌": "粤BxxxN"
        },
       "sid": "6631xxxxx0e01",
       "angle": 359
   }
   ```
9. vin识别码：

   ```
   {
      //请求结果code，200为请求成功，非200为请求失败
       "code": 200,
       "data": {
          "汽车vin码": "LSVxxxx"
        },
      //原图高度
       "orgHeight": 416,
      //原图宽度
       "orgWidth": 629,
      //旋转后图片高度
       "height": 416,
      //旋转后图片宽度
       "width": 629,
       "sid": "77318ebf8xxxxxxb0e01",
       "angle": 359
   }
   ```
10. 图片自动分类识别：

    ```
    {
     "code": 200,
       "data": {
         "姓名": "潘xx",
         "民族": "汉",
         "出生日期": "1986年1月9日",
         "住址": "四川省xxx",
         "身份证号码": "510xxxx",
         "性别": "男"
       },
       //原图高度
       "orgHeight": 416,
       //原图宽度
       "orgWidth": 629,
       //旋转后图片高度
       "height": 416,
       //旋转后图片宽度
       "width": 629,
       "sid": "111111bf84xxxxxxxb0e01",
       "angle": 359,
       "type": "身份证正面"
    }
    ```
11. 标题分类识别：

    ```
    {
        "code": 200,
        "data": {
            "type": "本票",
            "sid": "6811eec7xxxxxx12b3f1b9b"
        }
    }
    ```
12. 转账支票识别：

    ```
    {
        "code": 200,
         "data": {
             "ID1": "30109227",
             "ID2": "00258226",
             "付款行名称": "杭州银行XX支行",
             "出票人账号": "748xxx"
            },
           //原图高度
           "orgHeight": 416,
           //原图宽度
           "orgWidth": 629,
           //旋转后图片高度
           "height": 416,
           //旋转后图片宽度
           "width": 629,
           "sid": "f097f3f7xxxxxda4",
           "angle": 359
    }
    ```
13. 火车票识别：

    ```
    {
        "code": 200,
        "data": {
           "出发站": "上海虹桥站",
           "到达站": "杭州东站",
           "车次": "D2283",
           "出发站拼音": "Shanghaihongqiao",
           "到达站拼音": "Hangzhoudong",
           "开车时间": "2016年12月09日11：24开",
           "座位号": "14车15D号",
           "票价": "49.0",
           "座位类型": "二等座",
           "旅客信息": "4209831984****0035曹xx",
           "票号": "254xxxx"
         },
         "orgHeight": 416,
         "orgWidth": 629,
         "height": 416,
         "width": 629,
         "sid": "44318ebxxxx8339ef153a84b0e01",
         "angle": 359
    }
    ```
14. 定额发票识别：

    ```
    {
        "code": 200,
        "angle": 2,
        "data": {
           "大写金额": "拾元整",
           "发票代码": "15xxxx",
           "发票号码": "03xxxx",
           "小写金额": "",
           "发票代码解析": {
               "批次号": "58",
               "年份": "2018",
               "税务局代码": "国税",
               "发票行业代码": "其他",
               "金额版": "电脑版",
               "行政区划代码": "云南省",
               "发票类别代码": "企业冠名电脑发票"
            }
         },
          "height": 633,
          "orgHeight": 604,
          "orgWidth": 870,
          "width": 890,
          "sid": "44318ebxxxxxa84b0e01",
          "angle": 359
    }
    ```
15. 出租车发票识别：

    ```
    {
        "code": 200,
        "angle": 2,
        "data": {
           "实收金额": "",
           "车号": "渝B-30T76",
           "日期": "2018-09-28",
           "发票代码": "1500xxxx",
           "发票号码": "22xxxx",
           "里程": "22.8",
           "金额": "¥57.00",
           "下车": "01：40",
           "上车": "01：19",
           "合计": ""
         },
        "height": 633,
        "orgHeight": 604,
        "orgWidth": 870,
        "width": 890,
        "sid": "44318ebf8xxxxxx01",
        "angle": 359
    }
    ```
16. 机票行程单识别：

    ```
    {
        "code": 200,
         "angle": 2,
         "data": {
            "旅客姓名": "",
            "日期": "2019-02-2中",
            "出发地": "",
            "目的地": "",
            "民航发展基金": "",
            "电子客票号码": "781xxxx",
            "航班号": "东航MU2271",
            "燃油附加费": "EXEMPT",
            "有效身份证号码": "410xxxxxx",
            "填开单位": "",
            "保险费": "XXX",
            "印刷序号": "5042xx",
            "销售单位代号": "SIA25608336893",
            "票价": "CNY1410.0",
            "合计": "CNY1460.00",
            "验证码": "9817"
          },
         "height": 633,
         "orgHeight": 604,
         "orgWidth": 870,
         "width": 890,
         "sid": "44318ebf8xxxxx339ef153a84b0e01",
         "angle": 359
    }
    ```
17. 花名册识别：

    ```
    {
        "code": 200,
         "data": {
               "信息":[{
        "name": "张三",
        "mobile_phones": ["133xxx", "138xxxx"]
    }, {
        "name": "赵四",
        "mobile_phones": ["133xxxx", "138xxxx"]
    }]     
        }}
    ```
18. 实体信息监测：

    ```
    {
     "code": 200,
       "figure": null,
       "wordsInfo": null,
       "data": {
         "中国民族": "[\"汉\"]",
         "地址": "[\"四川省xxx\"]",
         "姓名": "[\"潘xx\"]",
         "性别": "[\"男\"]",
         "日期": "[\"1986年1月9日\"]",
         "身份证号": "[\"5101xxxxx\"]"
       },
       "orgWidth": 629,
       "recquality": null,
       "width": 635,
       "angle": 359,
       "orgHeight": 416,
       "type": null,
       "class": "com.taobao.ocr.client.view.OcrStructuredHSFServiceView",
       "height": 425,
       "sid": "beef67a0xxxx"
       "message": null,
       "class": "com.taobao.ocr.client.Result",
       "successful": true
    }
    ```
19. 审批表单识别：

    ```
    {
      "code": 200,
      "data": {
        "tableInfo": {
             // 标题
        "title": "差旅费报销单",
        "items": [{
                    // 是否在表格内部
            "whether_in_form": false,
                    // 类型，object表示单个kv，list表示一组kv，
            "type": "object",
                    // select(选项框)/calculate（合计）/money（金额）/department（部门）/attachment（附件）/photo（照片）/date（日期）/text（文本）/title（明细列表）/position（职位）/number（数字）
            "attribute": "department",
            "key": "部门",
            "value": ""
          }, {
            "whether_in_form": false,
            "type": "object",
            "attribute": "date",
            "key": "日期",
            "value": ""
          }, {
            "whether_in_form": false,
            "type": "object",
            "key": "附单据",
            "attribute": "text",
            "value": ""
          }, {
            "whether_in_form": false,
            "type": "object",
            "attribute": "position",
            "key": "单位主管",
            "value": ""
          }, {
            "whether_in_form": false,
            "type": "object",
            "attribute": "position",
            "key": "分管领导",
            "value": ""
          }, {
            "whether_in_form": false,
            "type": "object",
            "attribute": "department",
            "key": "出差部门",
            "value": ""
          }, {
            "whether_in_form": false,
            "type": "object",
            "attribute": "position",
            "key": "部门主管",
            "value": ""
          }, {
            "whether_in_form": false,
            "type": "object",
            "attribute": "position",
            "key": "财务审核",
            "value": ""
          }, {
            "whether_in_form": true,
            "type": "object",
            "attribute": "text",
            "key": "姓名",
            "value": ""
          }, {
            "whether_in_form": true,
            "type": "object",
            "attribute": "text",
            "key": "事由",
            "value": ""
          }, {
            "whether_in_form": true,
            "type": "object",
            "attribute": "text",
            "key": "出差天数",
            "value": ""
          },
          {
            "type": "list",
            "attribute": "title",
            "whether_in_form": true,
            "value": [{
              "type": "list",
              "attribute": "date",
              "key": "出发时间",
              "value": [{
                "type": "object",
                "key": "月",
                "value": ""
              }, {
                "type": "object",
                "attribute": "date",
                "key": "日",
                "value": ""
              }, {
                "type": "object",
                "attribute": "date",
                "key": "时",
                "value": ""
              }]
            }, {
              "type": "list",
              "attribute": "date",
              "key": "到达时间",
              "value": [{
                "type": "object",
                "attribute": "date",
                "key": "月",
                "value": ""
              }, {
                "type": "object",
                "attribute": "date",
                "key": "日",
                "value": ""
              }, {
                "type": "object",
                "attribute": "date",
                "key": "时",
                "value": ""
              }]
            }, {
              "type": "object",
              "attribute": "text",
              "key": "起点",
              "value": ""
            }, {
              "type": "object",
              "attribute": "text",
              "key": "终点",
              "value": ""
            }, {
              "type": "list",
              "attribute": "money",
              "key": "交通费",
              "value": [{
                "type": "object",
                "attribute": "money",
                "key": "火车费",
                "value": ""
              }, {
                "type": "object",
                "attribute": "money",
                "key": "汽车费",
                "value": ""
              }, {
                "type": "object",
                "attribute": "money",
                "key": "飞机费",
                "value": ""
              }, {
                "type": "object",
                "attribute": "money",
                "key": "轮船费",
                "value": ""
              }, {
                "type": "object",
                "attribute": "money",
                "key": "城市交通费",
                "value": ""
              }, {
                "type": "object",
                "attribute": "money",
                "key": "车辆通行费",
                "value": ""
              }]
            }, {
              "type": "object",
              "attribute": "money",
              "key": "宿费",
              "value": ""
            }, {
              "type": "object",
              "attribute": "money",
              "key": "行李运杂费",
              "value": ""
            }, {
              "type": "object",
              "attribute": "money",
              "key": "差旅补助",
              "value": ""
            }]
          }, {
            "whether_in_form": true,
            "type": "object",
            "attribute": "calculate",
            "key": "合计金额",
            "value": ""
          }, {
            "whether_in_form": true,
            "type": "object",
            "attribute": "calculate",
            "key": "合计金额",
            "value": ""
          }
        ]
      },
        //原图高度
        "orgHeight": 416,
        //原图宽度
        "orgWidth": 629,
        //旋转后图片高度
        "height": 416,
        //旋转后图片宽度
        "width": 629,
        "sid": "f097f3f7e5f93xxxx544ba9b3f1da4",
        "angle": 359
      }
    }
    ```
