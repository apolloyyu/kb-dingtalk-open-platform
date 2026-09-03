# 产品信息

doc_id: rn6mj1gnwd
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/jzcrm/goods
api_version: v2-new
app_types: 第三方企业应用
permissions: Jzcrm.Common.ReadWrite

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- datatype (Long, required): 数据类型，固定值**154**。
- stamp (Long, required): 时间戳。
- data_userid (String, required): 创建人。
- cpname (String, required): 产品名称。
- cpunit (String, required): 产品单位。
- unitrate (String, required): 单位换算。
- optional: msgid(Long), data(Object), cp_parentid(String), cptype(String), cpguige(String), typeid(String), cpno(String), isstop(String), addedtime(String), cparea(String), cpbrand(String), cbprice(String), issnmanage(String), ispicimanage(String), gysid(String), cpimg(String), cpbarcode(String), cpweight(String), preprice1(String), preprice2(String), preprice3(String), preprice4(String), isstock(String), stockup(String), stockdown(String), cpcontent(String), cpremark(String)

## Returns
- optional: time(String), msgid(Long)

## Limits
- 库存上限。

source_url: https://open.dingtalk.com/document/development/add-or-edit-product-information
updated_at: 2026-06-02 20:01:03
