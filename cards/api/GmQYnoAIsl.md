# OCR文字识别

doc_id: GmQYnoAIsl
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/ocr/structured/recognize
api_version: v1-oapi
app_types: 企业内部应用, 第三方企业应用
permissions: not_stated

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该API的应用凭证。 - 企业内部应用，通过获取企业内部应用的access_token接口获取。 - 第三方企业应用，通过获取第三方企业的access_token接口获取。

## Body
- type (String, required): 识别图片类型。 - **idcard**：身份证 - **invoice**：营业执照增值税发票 - **blicense**：营业执照 - **bank_card**：银行卡 - **car_no**：车牌 - **car_invoice**：机动车发票 - **driving_license**：驾驶证 - **vehicle_license**：行驶证 - **train_ticket**：火车票 - **quota_invoice**：定额发票 - **taxi_ticket**：出租车发票 - **air
- image_url (String, required): 识别图片地址，最大长度1000。

## Returns
- optional: request_id(String), errcode(Number), errmsg(String), result(OcrStructuredResult), height(Number), width(Number), angle(Number), data(String), original_height(Number), original_width(Number)

## Limits
- 识别图片地址，最大长度1000。

source_url: https://open.dingtalk.com/document/development/structured-image-recognition-api
updated_at: 2026-06-03 09:51:00
