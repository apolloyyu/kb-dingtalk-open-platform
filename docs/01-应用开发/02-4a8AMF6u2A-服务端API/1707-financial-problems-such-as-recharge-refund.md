---
title: "充值/退款等财务问题"
source_url: "https://open.dingtalk.com/document/development/financial-problems-such-as-recharge-refund"
namespace: "development"
slug: "financial-problems-such-as-recharge-refund"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 钉钉云 > 常见问题 > 充值/退款等财务问题"
doc_id: "JQ5W1tXI2r"
updated_at: "2025-10-16 14:31:29"
---

> Source: https://open.dingtalk.com/document/development/financial-problems-such-as-recharge-refund
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 钉钉云 > 常见问题 > 充值/退款等财务问题
> Updated: 2025-10-16 14:31:29

# 充值/退款等财务问题

本文档主要介绍开发者在使用钉钉云过程中可能遇到的财务问题以及相关的解决途径。

## 预算

在正式使用钉钉云之前，你可能需要向公司申请相关的费用，需要申请多少费用将是你首先要解决的问题。关于预算我们的解决方案将会提供一个比较好的评估途径。目前解决方案有四种版本，分别适用不同的情况，费用也不同。表格价格仅供参考，具体请以购买为准：

| **解决方案版本** | **按量付费的价格（折后）** | **建议的预算** |
| --- | --- | --- |
| 体验版 | 10.416/天 | 2,500/年 |
| 基础版 | 79.128/天 | 19,000/年 |
| 升级版 | 190.592/天 | 44,000/年 |
| 高级版 | 462.744/天 | 100,000/年 |

由于解决方案是先**按量**购买的，按量购买后可以再转为包年包月，所以在转为包年包月前需要一些额外的费用用于按量使用。因此我们的建议预算比包年后的价格略多，用于支付转包年包月前的费用。

上图只是针对解决方案给出的预算建议，如果你还需要购买其他的云产品，你需要根据自己的需要进行费用的评估，具体产品的价格可以在购买预览页获得。

## 充值

在购买解决方案前需要最少充值100元（最低消费金额的限制，否则无法购买云产品），你可以通过多种方式进行充值。

1. 充值入口见下图

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4875299951/p163416.png)

2. 三种充值方式，请按照各自的说明进行充值。

#### 支付宝充值

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4875299951/p163417.png)

#### 企业网银充值

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4875299951/p163418.png)

#### 线下汇款

1.开发者需要进行线下汇款，打款成功后获取汇款底单。汇款流程注意事项：

（1）需要走对公打款流程，汇款方必须是企业

（2）汇款前确认钉钉云账号已实名认证

（3）汇款账号如下，

| 主体 | 阿里云计算有限公司 |
| --- | --- |
| 纳税人识别号 | 91330106673959654P |
| 注册地址 | 浙江省杭州市西湖区转塘科技经济区块16号8幢 |
| 联系电话 | 0571-85022088 |
| 开户行 | 招商银行杭州高新支行 |
| **开户行账号** | **571905493610702** |
| 开户行地址 | 杭州市西湖区文三路478号 |
| 支行银行行号（或叫联行号） | 308331012079 |
| 支行联系电话 | 88915617 |
| Swift code | CMBCCNBS281 |

2. 获取到的汇款底单后，参考[《线下汇款认领》](https://help.aliyun.com/document_detail/112437.html)进行汇款认领。

3. 正常情况工作时间24个小时内，完成汇款认领审核；若超期未审核或审核失败，请登录[钉钉开发者后台提交工单](https://ding-doc.dingtalk.com/document/contactus)反馈。

## 支付

当你购买解决方案后进行【转包年包月】操作，或者直接购买单独的云产品，那么都会生成相应的订单，然后可以对这些订单进行支付。

1. 订单支付页面，支持支付宝、个人网银、企业网银及线下汇款充值多种方式。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5875299951/p163419.png)

2. 如果没有立即支付，那么从订单列表页面，可以再次进入支付页面。注意未支付订单是有有效期的，过期将会自动作废，当然你也可以手工作废订单。

![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5875299951/p163420.png "image.png")

## 退款到阿里云账户

如果你购买的云产品不想继续使用，希望退款，可以按照退款流程进行申请退款。**目前仅支持退款到阿里云账户**，退款流程如下：

1. 释放云产品资源，释放流程请参考[释放钉钉云产品](https://open.dingtalk.com/document/isvapp/release-dingtalk-cloud-products)。
2. 资源释放成功后，云产品预付费金额将自动转入账号余额。

## 提现

提现是指从阿里云账户余额，转到钉钉云账号主体关联的银行卡或者支付宝账号。提现操作需要银行卡户头信息或支付宝账号信息与钉钉云实名认证信息相符。**注意事项：**

**1.钉钉云目前仅支持线下提现，不支持线上提现。**

2.提现余额时，如果账号内还有按量付费的云产品在运行，一定要保留足够的余额用于退款审核期间的消费。如果一旦提现审核通过后，余额不满足提现时，提现失败。

线下退款的具体步骤如下：

1. 完成账号的实名认证（如果提示没有完成实名认证，请联系钉钉云支持人员，联系方式见退款部分），缺省是根据钉钉企业的认证信息自动完成钉钉云账号的实名认证。

2. 提交提现的工单。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5875299951/p163421.png)

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5875299951/p163422.png)

3. 联系钉钉云支持人员获得主账号信息，请通过[钉钉技术支持](https://ding-doc.dingtalk.com/document/contactus)，转人工联系

4. 通过工单提交线下提现相关的资料

5. 提现到相关的银行账号或者支付宝账号

## 发票

阿里云发票开取的前提是有实际的消费，如果仅仅充值是不算消费的，因为充值的余额是可以提现的。实际的消费是通过订单体现的。

1. 发票索取入口

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5875299951/p163423.png)

2. 发票索取页面

![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5875299951/p163424.png "image.png")

3. 添加发票抬头

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6875299951/p163425.png)

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6875299951/p163426.png)

4. 发票寄送地址管理

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6875299951/p163427.png)

## 合同

合同的申请是根据订单来申请的，可以多个订单一起申请合同。申请的合同的订单并不要求必须是支付完成的，如果你的公司需要先拿到合同才可以支付，那么可以先下单不支付，再申请合同，最后再完成支付。

![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6875299951/p163428.png "image.png")
