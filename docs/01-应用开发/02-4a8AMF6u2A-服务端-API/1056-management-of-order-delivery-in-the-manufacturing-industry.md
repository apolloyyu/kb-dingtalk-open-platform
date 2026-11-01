---
title: "制造业订单交付管理：产供销全链路数据协同与实时追踪"
source_url: "https://open.dingtalk.com/document/development/management-of-order-delivery-in-the-manufacturing-industry"
namespace: "development"
slug: "management-of-order-delivery-in-the-manufacturing-industry"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "行业与生态 > 生态开放 > 金智CRM > 集成方案 > 制造业订单交付管理：产供销全链路数据协同与实时追踪"
doc_id: "tfPnxoWIdU"
updated_at: "2026-10-16 09:23:19"
---

> Source: https://open.dingtalk.com/document/development/management-of-order-delivery-in-the-manufacturing-industry
> Path: 应用开发 / 服务端 API / 行业与生态 > 生态开放 > 金智CRM > 集成方案 > 制造业订单交付管理：产供销全链路数据协同与实时追踪
> Updated: 2026-10-16 09:23:19

# 制造业订单交付管理：产供销全链路数据协同与实时追踪

## **概述**

本方案面向生产制造企业，通过集成钉钉开放平台与金智CRM系统，打通销售、生产、采购、仓库、财务等部门业务在线协同链路，实现从销售订单下达、生产排程、物料核对到库存出入库的全流程数字化管理，帮助企业降低用人成本、提升业务流程效率、减少订单出错率。

### **方案背景**

生产制造企业在获得销售订单机会后，需要销售和生产部门及时同步订单所需生产产品，以销定产。然而在实际运营中，企业普遍面临以下挑战：

- **企业内部沟通不畅，协同效率低**：销售与中后台同事之间缺少统一平台和系统，经常发生订单下错单或者漏单的情况，造成损失；订单下单后，生产和销售部门无法及时协同，需要经过纸质生产申请单或者表格等不同平台多次确认。
- **客户回款情况难统计，应收款统计麻烦**：客户存在分期回款、多笔订单定期结算等多种回款方式，对应收款无法进行统计及提醒，存在错收款、漏收款情况。
- **库存出入库后数量不能实时更新**：库管人员出库或入库后，再通过表格修改数量，无法追溯出入库源头，数量更新不及时有错漏造成库存凌乱。
- **生产用料与库存无法精准核对，造成物料紧缺**：生产人员在正式生产前，无法精准核对生产所需物料与现有库存进行对比，会造成物料紧缺无法及时生产，以及物料囤积浪费采购金额。

### **核心价值**

- **高效信息传递和无纸化办公**：极大节省人力及企业内部沟通成本，使得工作流程由繁入简。
- **以销定产、以产定采**：摒弃过多人工核对环节，大大降低错误概率，提高整体工作效率。
- **全流程在线协同**：销售、生产、采购、仓库、财务等部门业务可及时在线协同，缩短订单周期。

### **适用场景**

本方案适用于以下典型业务场景：

- **销售合同闭环管理**：从商机跟进、合同签订、订单下达到回款催收的全流程数字化留痕与自动提醒。
- **产供销协同联动**：销售订单驱动生产排程，生产需求触发采购计划，实现以销定产、以产定采的精准协同。
- **仓储物流透明化**：库存出入库实时同步、物流信息自动追踪、签收状态即时推送，保障供应链可视可控。

## **典型业务场景**

### **场景一：销售合同闭环管理（制造业）**

#### **痛点分析**

杭州辉能电力科技有限公司多领域多产品线发展，自主研制生产的开关柜无线测温系统、开关柜智能操控装置、开关柜温湿度控制等产品，适用于各种电力设备中，包含物联网微电子领域、节能传感、电网智能化等的研发生产推广，还致力于能量收集技术，利用环境中的磁能、光能、热能、振动能等微量能量给传感器供电，为物联网传感器提供高品质节能电源解决方案。企业在用钉之前用人成本高，业务流程效率低，订单易出错。在销售合同管理环节，具体存在以下痛点：

- **订单下错单或漏单频发**：销售与中后台同事之间缺少统一平台和系统，经常发生订单下错单或者漏单的情况，造成直接经济损失。
- **跨部门协同依赖纸质单据**：订单下单后，生产和销售部门无法及时协同，需要经过纸质生产申请单或者表格等不同平台多次确认，耗时耗力且容易遗漏。
- **应收款统计困难且易错漏**：客户存在分期回款、多笔订单定期结算等多种回款方式，对应收款无法进行统计及提醒，存在错收款、漏收款情况，影响资金回笼效率。

#### **价值验证**

- **自动化流程**

  ![销售合同闭环管理自动化流程场景图_20261015_163216](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9973112971/p1106370.png)
- **核心优势**

  - **订单全程留痕**：从商机到回款全流程数字化记录，每一步操作都有据可查，支持多维度数据分析与历史追溯，避免关键节点信息丢失。
  - **应收自动提醒**：账期到期自动推送钉钉消息给相关财务人员，确保不漏收不错收，大幅降低坏账风险与人工催收成本。
  - **跨部门实时协同**：销售下单联动钉钉OA审批流，驱动生产、采购、仓库等部门及时响应，消除信息传递延迟与人工转述误差。

### **场景二：产供销协同联动（制造业）**

#### **痛点分析**

某中型装备制造企业拥有8条自动化产线，日均处理200+销售订单，过去依赖人工传递纸质单据协调生产与采购，原有流程存在以下问题：

- **库存数量无法实时更新**：库管人员出库或入库后，再通过表格修改数量，无法追溯出入库源头，数量更新不及时有错漏造成库存凌乱，影响生产计划准确性。
- **生产用料与库存无法精准核对**：生产人员在正式生产前，无法精准核对生产所需物料与现有库存进行对比，会造成物料紧缺无法及时生产，以及物料囤积浪费采购金额。
- **以销定产执行不到位**：销售订单与生产计划脱节，导致货物囤积或不必要的采购成本增加，订单周期延长，影响客户满意度。

#### **价值验证**

- **自动化流程**

  ![产供销协同联动自动化流程场景图_20261015_163243](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9973112971/p1106368.png)
- **核心优势**

  - **库存实时同步**：出入库操作即时更新至系统，销售接单时可准确判断库存状态，消除信息滞后导致的超卖或缺货风险。
  - **物料精准核对**：生产前系统自动比对需求与库存，低于安全阈值时自动触发采购申请，避免紧缺停工或盲目囤积造成的资金占用。
  - **以销定产落地**：销售订单自动驱动生产排程与采购计划，各部门基于同一数据源协同作业，订单周期平均缩短40%以上。

## **实施指南**

### **技术架构**

- **接口调用层**：通过钉钉开放平台API实现与金智CRM系统的数据交互，包括通讯录管理、身份验证、消息推送等能力。
- **应用认证层**：基于OAuth2.0协议完成企业授权，获取`accessToken`用于后续API调用。
- **业务逻辑层**：封装销售合同管理、产供销协同、库存管理等核心业务流程，实现自动化触发与状态同步。
- **数据存储层**：金智CRM作为业务数据主存储，钉钉作为消息通知与协同入口，两者通过API保持数据一致性。
- **错误处理层**：对API调用失败、权限不足、数据异常等情况进行捕获与重试，保障系统稳定性。

### **前置条件**

在实施方案前，需满足以下条件：

- **应用准备**：已完成钉钉开发者账号注册并实现[应用创建与配置](../01-XOnnmGCTbn-开发指南/0007-create-application.md)。
- **权限要求：**已在钉钉开发者后台为应用添加以下接口权限：

  - `qyapi_get_department_member` （通讯录部门成员读权限）
  - `Jzcrm.Common.ReadWrite` （金智CRM数据管理权限）
- **开发环境**：已安装Java开发环境（JDK1.6及以上）及Maven构建工具。
- **SDK准备：** [服务端SDK下载](0002-download-the-server-side-sdk.md)，版本建议最新稳定版。
- **系统配置**：金智CRM系统已完成基础配置并与钉钉完成对接授权。

### **代码实现**

步骤一：获取应用凭证信息，获取应用 Client ID 和 Client Secret。

步骤二：申请接口权限。查找“金智CRM”、“通讯录管理”，申请相应的权限。

步骤三：获取应用访问凭证[获取企业内部应用的accessToken](0032-obtain-the-access-token-of-an-internal-app.md)。调用接口时，通过accessToken鉴权调用者身份。

步骤四：订单交付流程 API：

1. 调用服务端API-[获取部门用户基础信息](0065-queries-the-simple-information-of-a-department-user.md)接口，获取用户`userId`。
2. 根据用户`userId`，调用服务端API-[新增/更新客户资料](1057-add-or-edit-customer-profile.md)接口，进行客户信息的新增和编辑。
3. 调用服务端API-[新增或更新产品信息](1065-add-or-edit-product-information.md)接口，进行产品信息的新增和编辑。
4. 调用服务端API-[新增或更新合同订单](1060-add-or-edit-contract-orders.md)接口，进行合同订单的新增和编辑。
5. 调用服务端API-[新增或更新采购单](1063-edit-purchase-order.md)接口，进行采购单的新增和编辑。
6. 调用服务端API-[新增或更新入库单](1066-add-or-edit-a-shipment-record.md)接口，进行入库单的新增和编辑。
7. 调用服务端API-[新增或更新发货单](1061-add-or-edit-invoices.md)接口，进行发货单的新增和编辑。
8. 调用服务端API-[新增或更新出库单](1067-add-or-edit-an-issue-ticket.md)接口，进行出库单的新增和编辑。

步骤五：数据信息管理API：

1. 根据数据`msgid`和数据类型`datatype`，调用[获取数据详情](1068-queries-data-details.md)接口，获取订单、采购、入库、发货和出库一系列环节的数据详细信息。
2. 根据数据`msgid`和数据类型`datatype`，调用[获取数据列表](1069-obtain-the-data-list.md)接口，可得到某一单据的数据列表信息。

## **实施步骤**

### **步骤一：****获取应用凭证**

1. 登录[钉钉开发者后台](https://open-dev.dingtalk.com/)。
2. 选择目标应用，进入应用详情页。
3. 单击**基础信息** > **凭证与基础信息**。
4. 记录应用的`Client ID`和`Client Secret`。

   > **[!NOTE]**
   >
   > 请妥善保管 `Client Secret`，不要泄露给第三方。建议将其存储在环境变量或密钥管理系统中，避免硬编码在代码里。

### **步骤二：添加接口权限**

1. 在应用详情页，单击**权限管理**。
2. 在权限搜索框中输入以下权限标识并申请：

   - `qyapi_get_department_member` （通讯录部门成员读权限）— 用于读取企业组织架构与部门成员信息，支撑报修工单自动关联员工姓名和部门。
   - `Jzcrm.Common.ReadWrite` （金智CRM数据管理权限）— 用于读写金智CRM中的销售订单、生产计划、库存数据等业务信息。

> **[!NOTE]**
>
> 不同业务场景可能需要不同的权限组合，请根据实际需求申请。例如批量导入场景还需申请批量操作用户的相关权限。

### 步骤三：获取访问凭证（accessToken）

根据步骤一中 的 Client ID 和 Client Secret，获取应用访问凭证[获取企业内部应用的accessToken](0032-obtain-the-access-token-of-an-internal-app.md)。

```
public void getAccessToken() throws Exception {
  Config config = new Config();
  config.protocol = "https";
  config.regionId = "central";
  com.aliyun.dingtalkoauth2_1_0.Client client = new com.aliyun.dingtalkoauth2_1_0.Client(config);
  GetAccessTokenRequest accessTokenRequest = new GetAccessTokenRequest()
    .setAppKey("din*********hgn")
    .setAppSecret("9G_O************mBkhgGIO");
  GetAccessTokenResponse accessToken = client.getAccessToken(accessTokenRequest);
  System.out.println(JSON.toJSONString(accessToken.getBody()));
}
```

**最佳实践**：

- **缓存策略**：`accessToken`有效期为2小时，建议在内存或Redis中缓存，过期前5分钟主动刷新。
- **并发控制**：避免多个线程同时刷新token导致冲突，可使用分布式锁机制。
- **异常重试**：网络波动时自动重试，最多3次，间隔递增（1s → 2s → 4s）。

### **步骤四：订单交付流程 API**

> **[!NOTE]**
>
> - 调用的API新增的数据会返回msgid参数。
> - 每个数据表单的dataType为固定值，详情请参考具体API示例。

1. 调用服务端API-[获取部门用户基础信息](0065-queries-the-simple-information-of-a-department-user.md)接口，获取用户`userId`。

   ```
   public void  getUserListsimple() throws ApiException {
     DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/user/listsimple");
     OapiUserListsimpleRequest req = new OapiUserListsimpleRequest();
     req.setDeptId(10L);
     req.setCursor(0L);
     req.setSize(10L);
     OapiUserListsimpleResponse rsp = client.execute(req, "access_token");
     System.out.println(rsp.getBody());
   }
   ```

   **请求参数：**

   - `dept_id`：部门ID，如果是根部门，该参数传1。
   - `cursor`：分页查询的游标，最开始传0。
   - `size`：分页长度，最大值100。

   **返回字段：**

   - `userid`：用户的userid。
   - `name`：用户姓名。
2. 根据用户`userId`，调用服务端API-[新增或更新客户资料](1057-add-or-edit-customer-profile.md)接口，进行客户信息的新增和编辑。

   ```
   public void getEditCustomer() throws Exception {
       Config config = new Config();
       config.protocol = "https";
       config.regionId = "central";

       com.aliyun.dingtalkjzcrm_1_0.Client client = new com.aliyun.dingtalkjzcrm_1_0.Client(config);

       EditCustomerHeaders editCustomerHeaders = new EditCustomerHeaders();
       editCustomerHeaders.xAcsDingtalkAccessToken = "<your access token>";

       // 构建客户数据
       EditCustomerRequest.EditCustomerRequestData data = new EditCustomerRequest.EditCustomerRequestData()
               .setDataUserid("张三")
               .setKhPkhid("客户1")
               .setKhClass("企业客户")
               .setKhName("客户2")
               .setKhSex("男")
               .setKhShortname("客户2")
               .setKhIndustry("服务")
               .setKhEmployees("100")
               .setKhAddress("200-300人")
               .setKhCountry("中国")
               .setKhProvince("山东")
               .setKhCity("青岛")
               .setKhCoaddress("香港中立")
               .setKhHottype("是")
               .setKhHotlevel("无")
               .setKhHotfl("高热意向客户")
               .setKhHotmemo("说明")
               .setKhType("普通客户")
               .setKhStatus("售中跟单")
               .setKhSn("KH20210531001")
               .setKhHandset("18965698965")
               .setKhEmail("59867898@qq.com")
               .setKhDingtalk("钉钉号")
               .setKhTel("0533-4577963")
               .setKhWeixin("wx_qijdjfyudj")
               .setKhQq("93539566")
               .setKhSkype("Skype")
               .setKhWangwang("旺旺")
               .setKhWorktel("0533-4577963")
               .setKhFax("传真")
               .setKhPst("236996")
               .setKhDepartment("财务部")
               .setKhAppellation("销售经理")
               .setKhPreside("销售")
               .setKhHeadship("销售经理")
               .setKhWeb("https:://www.baidu.com")
               .setKhBefontof("篮球")
               .setKhFrom("线上")
               .setKhBillinfo("开票资料")
               .setKhInfo("公司简介")
               .setKhRalagrade("高")
               .setKhCreditgrade("高")
               .setKhValrating("高")
               .setKhCttype("身份证")
               .setKhCtnumber("22363656369896536")
               .setKhContype("联系人分类")
               .setKhRemark("备注")
               .setKhJibie("vip客户");

       // 组装请求
       EditCustomerRequest editCustomerRequest = new EditCustomerRequest()
               .setDatatype(148L)
               .setStamp(1621822122L)
               .setMsgid(1L)
               .setData(data);

       try {
           client.editCustomerWithOptions(editCustomerRequest, editCustomerHeaders, new RuntimeOptions());
       } catch (TeaException err) {
           if (!com.aliyun.teautil.Common.empty(err.code) && !com.aliyun.teautil.Common.empty(err.message)) {
               // err 中含有 code 和 message 属性，可帮助开发定位问题
           }
       } catch (Exception _err) {
           TeaException err = new TeaException(_err.getMessage(), _err);
           if (!com.aliyun.teautil.Common.empty(err.code) && !com.aliyun.teautil.Common.empty(err.message)) {
               // err 中含有 code 和 message 属性，可帮助开发定位问题
           }
       }
   }
   ```

   **请求参数：**

   - `datatype`：数据类型，固定值**148**。
   - `stamp`：时间戳，单位：秒。
   - `msgid`：数据ID，值为0或不填时，为新增数据。
   - `data`：编辑客户数据。

   **返回字段：**

   - `msgid`：编辑数据的ID。
3. 调用服务端API-[新增或更新产品信息](1065-add-or-edit-product-information.md)接口，进行产品信息的新增和编辑。

   ```
   public void getEditGoods() throws Exception {
       Config config = new Config();
       config.protocol = "https";
       config.regionId = "central";

       com.aliyun.dingtalkjzcrm_1_0.Client client = new com.aliyun.dingtalkjzcrm_1_0.Client(config);

       EditGoodsHeaders editGoodsHeaders = new EditGoodsHeaders();
       editGoodsHeaders.xAcsDingtalkAccessToken = "<your access token>";

       // 构建商品数据
       EditGoodsRequest.EditGoodsRequestData data = new EditGoodsRequest.EditGoodsRequestData()
               .setDataUserid("张三")
               .setCpname("笔记本电脑")
               .setCpunit("台")
               .setUnitrate("单位换算")
               .setCpParentid("基准产品")
               .setCptype("S200")
               .setCpguige("12.5kg/台")
               .setTypeid("电子")
               .setCpno("CP6877979689")
               .setIsstop("正常")
               .setAddedtime("2021-06-01")
               .setCparea("西北")
               .setCpbrand("华为")
               .setCbprice("109999")
               .setIssnmanage("是")
               .setIspicimanage("是")
               .setGysid("华为")
               .setCpimg("产品图片链接")
               .setCpbarcode("234234453452")
               .setCpweight("12.5kg")
               .setPreprice1("209999")
               .setPreprice2("209999")
               .setPreprice3("209999")
               .setPreprice4("209999")
               .setIsstock("计算(按基准规格)")
               .setStockup("100")
               .setStockdown("1")
               .setCpcontent("产品说明")
               .setCpremark("产品备注");

       // 组装请求
       EditGoodsRequest editGoodsRequest = new EditGoodsRequest()
               .setDatatype(154L)
               .setStamp(1621822122L)
               .setMsgid(1L)
               .setData(data);

       try {
           client.editGoodsWithOptions(editGoodsRequest, editGoodsHeaders, new RuntimeOptions());
       } catch (TeaException err) {
           if (!com.aliyun.teautil.Common.empty(err.code) && !com.aliyun.teautil.Common.empty(err.message)) {
               // err 中含有 code 和 message 属性，可帮助开发定位问题
           }
       } catch (Exception _err) {
           TeaException err = new TeaException(_err.getMessage(), _err);
           if (!com.aliyun.teautil.Common.empty(err.code) && !com.aliyun.teautil.Common.empty(err.message)) {
               // err 中含有 code 和 message 属性，可帮助开发定位问题
           }
       }
   }
   ```

   **请求参数：**

   - `datatype`：数据类型，固定值**154**。
   - `stamp`：时间戳，单位：秒。
   - `msgid`：数据ID，值为0或不填时，为新增数据。
   - `data`：编辑产品数据。

   **返回字段：**

   - `msgid`：编辑数据的ID。
4. 调用服务端API-[新增或更新合同订单](1060-add-or-edit-contract-orders.md)接口，进行合同订单的新增和编辑。

   ```
   public void getEditOrder() throws Exception {
       Config config = new Config();
       config.protocol = "https";
       config.regionId = "central";

       com.aliyun.dingtalkjzcrm_1_0.Client client = new com.aliyun.dingtalkjzcrm_1_0.Client(config);

       EditOrderHeaders editOrderHeaders = new EditOrderHeaders();
       editOrderHeaders.xAcsDingtalkAccessToken = "<your access token>";

       // 构建订单数据
       EditOrderRequest.EditOrderRequestData data = new EditOrderRequest.EditOrderRequestData()
               .setDataUserid("张三")
               .setHtCustomerid("客户1")
               .setHtDate("2021-6-1")
               .setHtPreside("李四")
               .setHtState("执行中")
               .setHtSummoney("10000")
               .setHtOrder("合同")
               .setHtTitle("主体")
               .setHtNumber("DD798686767")
               .setHtLxrid("王五")
               .setHtLxrinfo("13989568656")
               .setHtXshid("对应机会")
               .setHtType("主营产品销售")
               .setHtPaymode("微信")
               .setHtBegindate("2021-6-1")
               .setHtCusub("孙大力")
               .setHtWesub("张大山")
               .setHtMoneyzhekou("12")
               .setHtKjmoney("14")
               .setHtFjmoneylx("运费")
               .setHtFjmoney("10")
               .setHtSummemo("外币备注")
               .setHtDeliplace("交付地点")
               .setHtEnddate("2021-6-2")
               .setHtWuliutype("顺丰快递")
               .setHtYunfeimoney("10")
               .setFahuoaddressid("山西省大同市")
               .setHtContract("合同正文")
               .setHtRemark("备注")
               .setChildMx("\"child_mx\":[{\"产品ID\":\"1\",\"数量\":\"10\",\"单价\":\"58.5\",\"总价\":\"585\",\"明细备注\":\"包含的测试产品\"}]");

       // 组装请求
       EditOrderRequest editOrderRequest = new EditOrderRequest()
               .setDatatype(150L)
               .setStamp(1621822122L)
               .setMsgid(1L)
               .setData(data);

       try {
           client.editOrderWithOptions(editOrderRequest, editOrderHeaders, new RuntimeOptions());
       } catch (TeaException err) {
           if (!com.aliyun.teautil.Common.empty(err.code) && !com.aliyun.teautil.Common.empty(err.message)) {
               // err 中含有 code 和 message 属性，可帮助开发定位问题
           }
       } catch (Exception _err) {
           TeaException err = new TeaException(_err.getMessage(), _err);
           if (!com.aliyun.teautil.Common.empty(err.code) && !com.aliyun.teautil.Common.empty(err.message)) {
               // err 中含有 code 和 message 属性，可帮助开发定位问题
           }
       }
   }
   ```

   **请求参数：**

   - `datatype`：数据类型，固定值**150**。
   - `stamp`：时间戳，单位：秒。
   - `msgid`：数据ID，值为0或不填时，为新增数据。
   - `data`：编辑合同数据。

   **返回字段：**

   - `msgid`：编辑数据的ID。
5. 调用服务端API-[新增或更新采购单](1063-edit-purchase-order.md)接口，进行采购单的新增和编辑。

   ```
   public void  getEditPurchase() throws Exception {
     Config config = new Config();
     config.protocol = "https";
     config.regionId = "central";
     com.aliyun.dingtalkjzcrm_1_0.Client client = new com.aliyun.dingtalkjzcrm_1_0.Client(config);
     EditPurchaseHeaders editPurchaseHeaders = new EditPurchaseHeaders();
     editPurchaseHeaders.xAcsDingtalkAccessToken = "<your access token>";
     EditPurchaseRequest.EditPurchaseRequestData data = new EditPurchaseRequest.EditPurchaseRequestData()
       .setDataUserid("张三")
       .setGysid("供应商1")
       .setCgno("CG7768698678")
       .setSummoney("10000")
       .setCgdate("2021-06-01")
       .setCgZxstate("执行中")
       .setOrderKhid("客户1")
       .setCgname("采购主题")
       .setGysLxrid("王五")
       .setGysLxrinfo("19636989568")
       .setCgtype("经营主产品采购")
       .setGysjingban("代表1")
       .setEmpid("代表2")
       .setCgMoneyzhekou("12")
       .setCgKjmoney("190")
       .setCgFjmoneylx("运费")
       .setCgFjmoney("10")
       .setOrderHtid("订单1")
       .setCgremark("采购摘要")
       .setChildMx("\"child_mx\":[{\"产品ID\":\"1\",\"数量\":\"10\",\"单价\":\"58.5\",\"总价\":\"585\",\"明细备注\":\"包含的测试产品\"}]");
     EditPurchaseRequest editPurchaseRequest = new EditPurchaseRequest()
       .setDatatype(153L)
       .setStamp(1621822122L)
       .setMsgid(1L)
       .setData(data);
     try {
       client.editPurchaseWithOptions(editPurchaseRequest, editPurchaseHeaders, new RuntimeOptions());
     }  catch (TeaException err) {
       if (!com.aliyun.teautil.Common.empty(err.code) && !com.aliyun.teautil.Common.empty(err.message)) {
         // err 中含有 code 和 message 属性，可帮助开发定位问题
       }
     
     } catch (Exception _err) {
       TeaException err = new TeaException(_err.getMessage(), _err);
       if (!com.aliyun.teautil.Common.empty(err.code) && !com.aliyun.teautil.Common.empty(err.message)) {
         // err 中含有 code 和 message 属性，可帮助开发定位问题
       }
     }
   }
   ```

   **请求参数：**

   - `datatype`：数据类型，固定值**153**。
   - `stamp`：时间戳，单位：秒。
   - `msgid`：数据ID，值为0或不填时，为新增数据。
   - `data`：编辑采购单数据。

   **返回字段：**

   - `msgid`：编辑数据的ID。
6. 调用服务端API-[新增或更新入库单](1066-add-or-edit-a-shipment-record.md)接口，进行入库单的新增和编辑。

   ```
   public void  getEditIntostock() throws Exception {
     Config config = new Config();
     config.protocol = "https";
     config.regionId = "central";
     com.aliyun.dingtalkjzcrm_1_0.Client client = new com.aliyun.dingtalkjzcrm_1_0.Client(config);
     EditIntostockHeaders editIntostockHeaders = new EditIntostockHeaders();
     editIntostockHeaders.xAcsDingtalkAccessToken = "<your access token>";
     EditIntostockRequest.EditIntostockRequestData data = new EditIntostockRequest.EditIntostockRequestData()
       .setDataUserid("张三")
       .setLibiodate("2021-06-01")
       .setStocklibid("华东大仓")
       .setLibiostate("已入库")
       .setBillno("RK784668968")
       .setCustomerid("供应商1")
       .setEmpid("李四")
       .setInorout("入库")
       .setLibioname("生产入库")
       .setOrderid("1")
       .setAskempid("王五")
       .setRemark("申请备注")
       .setAuditreson("入库备注")
       .setChildMx("[{\"产品ID\":\"1\",\"数量\":\"10\",\"单价\":\"58.5\",\"总价\":\"585\",\"明细备注\":\"包含的测试产品\"}]");
     EditIntostockRequest editIntostockRequest = new EditIntostockRequest()
       .setDatatype(189L)
       .setStamp(1621822122L)
       .setMsgid(1L)
       .setData(data);
     try {
       client.editIntostockWithOptions(editIntostockRequest, editIntostockHeaders, new RuntimeOptions());
     }  catch (TeaException err) {
       if (!com.aliyun.teautil.Common.empty(err.code) && !com.aliyun.teautil.Common.empty(err.message)) {
         // err 中含有 code 和 message 属性，可帮助开发定位问题
       }
     
     } catch (Exception _err) {
       TeaException err = new TeaException(_err.getMessage(), _err);
       if (!com.aliyun.teautil.Common.empty(err.code) && !com.aliyun.teautil.Common.empty(err.message)) {
         // err 中含有 code 和 message 属性，可帮助开发定位问题
       }
     }
   }
   ```

   **请求参数：**

   - `datatype`：数据类型，固定值**189**。
   - `stamp`：时间戳，单位：秒。
   - `msgid`：数据ID，值为0或不填时，为新增数据。
   - `data`：编辑入库单数据。

   **返回字段：**

   - `msgid`：编辑数据的ID。
7. 调用服务端API-[新增或更新发货单](1061-add-or-edit-invoices.md)接口，进行发货单的新增和编辑。

   ```
   public void  getEditInvoice() throws Exception {
     Config config = new Config();
     config.protocol = "https";
     config.regionId = "central";
     com.aliyun.dingtalkjzcrm_1_0.Client client = new com.aliyun.dingtalkjzcrm_1_0.Client(config);
     EditInvoiceHeaders editInvoiceHeaders = new EditInvoiceHeaders();
     editInvoiceHeaders.xAcsDingtalkAccessToken = "<your access token>";
     EditInvoiceRequest.EditInvoiceRequestData data = new EditInvoiceRequest.EditInvoiceRequestData()
       .setDataUserid("张三")
       .setFhCustomerid("客户1")
       .setFhDate("2021-06-01")
       .setFhNumber("FH87997978687")
       .setFhMode("顺丰快递")
       .setFhHtorder("1")
       .setFhTitle("发货主题")
       .setFhYunfei("10")
       .setFhJianshu("1")
       .setFhKg("12.5")
       .setFhShipper("李四")
       .setFhPreside("王五")
       .setFhLxrid("朱六")
       .setFhLinkman("杨七")
       .setFhTel("0622-8985652")
       .setFhHandset("18965362369")
       .setFhPost("268996")
       .setFhAddress("山东省青岛市")
       .setFhEmail("5268685@qq.com")
       .setFhMsn("MSN")
       .setFhRemark("备注")
       .setFhState("已发货")
       .setChildMx("\"child_mx\":[{\"产品ID\":\"1\",\"数量\":\"10\",\"单价\":\"58.5\",\"总价\":\"585\",\"明细备注\":\"包含的测试产品\"}]");
     EditInvoiceRequest editInvoiceRequest = new EditInvoiceRequest()
       .setDatatype(169L)
       .setStamp(1621822122L)
       .setMsgid(1L)
       .setData(data);
     try {
       client.editInvoiceWithOptions(editInvoiceRequest, editInvoiceHeaders, new RuntimeOptions());
     }  catch (TeaException err) {
       if (!com.aliyun.teautil.Common.empty(err.code) && !com.aliyun.teautil.Common.empty(err.message)) {
         // err 中含有 code 和 message 属性，可帮助开发定位问题
       }
     
     } catch (Exception _err) {
       TeaException err = new TeaException(_err.getMessage(), _err);
       if (!com.aliyun.teautil.Common.empty(err.code) && !com.aliyun.teautil.Common.empty(err.message)) {
         // err 中含有 code 和 message 属性，可帮助开发定位问题
       }
     }
   }
   ```

   **请求参数：**

   - `datatype`：数据类型，固定值**169**。
   - `stamp`：时间戳，单位：秒。
   - `msgid`：数据ID，值为0或不填时，为新增数据。
   - `data`：编辑发货单数据。

   **返回字段：**

   - `msgid`：编辑数据的ID。
8. 调用服务端API-[新增或更新出库单](1067-add-or-edit-an-issue-ticket.md)接口，进行出库单的新增和编辑。

   ```
   public void  getEditOutstock() throws Exception {
     Config config = new Config();
     config.protocol = "https";
     config.regionId = "central";
     com.aliyun.dingtalkjzcrm_1_0.Client client = new com.aliyun.dingtalkjzcrm_1_0.Client(config);
     EditOutstockHeaders editOutstockHeaders = new EditOutstockHeaders();
     editOutstockHeaders.xAcsDingtalkAccessToken = "<your access token>";
     EditOutstockRequest.EditOutstockRequestData data = new EditOutstockRequest.EditOutstockRequestData()
       .setDataUserid("张三")
       .setLibiodate("2021-06-01")
       .setStocklibid("华东一仓")
       .setLibiostate("已出库")
       .setBillno("CK89865667")
       .setCustomerid("客户1")
       .setEmpid("李四")
       .setInorout("出库")
       .setLibioname("出库主题")
       .setOrderid("1")
       .setAskempid("王五")
       .setRemark("申请备注")
       .setAuditreson("出库备注")
       .setChildMx("[{\"产品ID\":\"1\",\"数量\":\"10\",\"单价\":\"58.5\",\"总价\":\"585\",\"明细备注\":\"包含的测试产品\"}]");
     EditOutstockRequest editOutstockRequest = new EditOutstockRequest()
       .setDatatype(191L)
       .setStamp(1621822122L)
       .setMsgid(1L)
       .setData(data);
     try {
       client.editOutstockWithOptions(editOutstockRequest, editOutstockHeaders, new RuntimeOptions());
     } catch (TeaException err) {
       if (!com.aliyun.teautil.Common.empty(err.code) && !com.aliyun.teautil.Common.empty(err.message)) {
         // err 中含有 code 和 message 属性，可帮助开发定位问题
       }
     
     } catch (Exception _err) {
       TeaException err = new TeaException(_err.getMessage(), _err);
       if (!com.aliyun.teautil.Common.empty(err.code) && !com.aliyun.teautil.Common.empty(err.message)) {
         // err 中含有 code 和 message 属性，可帮助开发定位问题
       }
     }
   }
   ```

   **请求参数：**

   - `datatype`：数据类型，固定值**191**。
   - `stamp`：时间戳，单位：秒。
   - `msgid`：数据ID，值为0或不填时，为新增数据。
   - `data`：编辑出库单数据。

   **返回字段：**

   - `msgid`：编辑数据的ID。

### **步骤五，数据信息管理API**

1. 根据数据`msgid`和数据类型`datatype`，调用[获取数据详情](1068-queries-data-details.md)接口，获取订单、采购、入库、发货和出库一系列环节的数据详细信息。

   ```
   public void  getGetDataView() throws Exception {
     Config config = new Config();
     config.protocol = "https";
     config.regionId = "central";
     com.aliyun.dingtalkjzcrm_1_0.Client client = new com.aliyun.dingtalkjzcrm_1_0.Client(config);
     GetDataViewHeaders getDataViewHeaders = new GetDataViewHeaders();
     getDataViewHeaders.xAcsDingtalkAccessToken = "<your access token>";
     GetDataViewRequest getDataViewRequest = new GetDataViewRequest()
       .setDatatype("150")
       .setMsgid(1L);
     try {
       client.getDataViewWithOptions(getDataViewRequest, getDataViewHeaders, new RuntimeOptions());
     } catch (TeaException err) {
       if (!com.aliyun.teautil.Common.empty(err.code) && !com.aliyun.teautil.Common.empty(err.message)) {
         // err 中含有 code 和 message 属性，可帮助开发定位问题
       }
     
     } catch (Exception _err) {
       TeaException err = new TeaException(_err.getMessage(), _err);
       if (!com.aliyun.teautil.Common.empty(err.code) && !com.aliyun.teautil.Common.empty(err.message)) {
         // err 中含有 code 和 message 属性，可帮助开发定位问题
       }
     }
   }
   ```

   **请求参数：**

   - `datatype`：数据类型。
   - `msgid`：数据ID。

   **返回字段：**

   - `detail`：数据详情。
   - `dataname`：字段明细。
2. 根据数据`msgid`和数据类型`datatype`，调用[获取数据列表](1069-obtain-the-data-list.md)接口，可得到某一单据的数据列表信息。

   ```
   public void  getGetDataList() throws Exception {
     Config config = new Config();
     config.protocol = "https";
     config.regionId = "central";
     com.aliyun.dingtalkjzcrm_1_0.Client client = new com.aliyun.dingtalkjzcrm_1_0.Client(config);
     GetDataListHeaders getDataListHeaders = new GetDataListHeaders();
     getDataListHeaders.xAcsDingtalkAccessToken = "<your access token>";
     GetDataListRequest getDataListRequest = new GetDataListRequest()
       .setDatatype("150")
       .setPage(1L)
       .setPagesize(10L);
     try {
       client.getDataListWithOptions(getDataListRequest, getDataListHeaders, new RuntimeOptions());
     } catch (TeaException err) {
       if (!com.aliyun.teautil.Common.empty(err.code) && !com.aliyun.teautil.Common.empty(err.message)) {
         // err 中含有 code 和 message 属性，可帮助开发定位问题
       }
     
     } catch (Exception _err) {
       TeaException err = new TeaException(_err.getMessage(), _err);
       if (!com.aliyun.teautil.Common.empty(err.code) && !com.aliyun.teautil.Common.empty(err.message)) {
         // err 中含有 code 和 message 属性，可帮助开发定位问题
       }
     }
   }
   ```

   **请求参数：**

   - `datatype`：数据类型。
   - `page`：页码。
   - `pagesize`：分页条数。

   **返回字段：**

   - `detail`：数据列表。
   - `dataname`：字段明细。

**实施完成检查清单**

- ✅ 应用凭证（`Client ID`和`Client Secret`）已安全获取并妥善保管。
- ✅ 接口权限（`qyapi_get_department_member`、`Jzcrm.Common.ReadWrite`）已成功添加并生效。
- ✅ `accessToken`获取与缓存机制已实现并通过测试。
- ✅ 部门成员列表API调用成功，返回数据格式符合预期。
- ✅ 金智CRM数据读写API调用成功，订单创建与查询功能正常。
- ✅ 销售合同闭环管理场景已验证：订单留痕、应收提醒、跨部门协同均正常工作。
- ✅ 产供销协同联动场景已验证：库存同步、物料核对、以销定产流程跑通。
- ✅ 错误处理机制已部署，异常情况可自动重试并告警。

## **常见问题（FAQ）**

- **Q1：**`accessToken`**过期后如何处理？**

  若**accessToken**过期，可重新调用获取`accessToken`接口并更新缓存。建议在缓存中设置7000秒过期时间（早于官方7200秒），提前刷新避免业务中断。
- **Q2：权限添加后为何API仍返回无权限错误？**

  权限添加后需等待1-2分钟生效；若仍报错，请检查是否使用了正确的`accessToken`（旧令牌不会自动继承新权限），重新获取令牌后再试。
- **Q3：金智CRM订单创建失败可能是什么原因？**

  常见原因包括：`productCode`在金智CRM产品库中不存在、`customerId`未关联有效客户档案、`quantity`为非正整数、`status`枚举值拼写错误。请逐一核对参数合法性。
