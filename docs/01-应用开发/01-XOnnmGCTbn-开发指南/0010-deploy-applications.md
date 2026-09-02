---
title: "应用部署"
source_url: "https://open.dingtalk.com/document/development/deploy-applications"
namespace: "development"
slug: "deploy-applications"
group: "应用开发"
tab: "开发指南"
breadcrumb: "开发指南 > 三方应用部署 > 应用部署"
doc_id: "PW14rvoywc"
updated_at: "2026-09-02 18:14:24"
---

> Source: https://open.dingtalk.com/document/development/deploy-applications
> Path: 应用开发 / 开发指南 / 开发指南 > 三方应用部署 > 应用部署
> Updated: 2026-09-02 18:14:24

# 应用部署

计算巢为服务商提供了一套环境管理应用，一键云资源与应用诊断，一体化监控事件收集和预警体系 ，保障应用稳定运行的方案。

## 部署流程

1. 钉钉组织绑定阿里云账号

   1. 在开发者后台点击进入[阿里云](https://open-dev.dingtalk.com/fe/alicloud#/)，将上架应用部署的阿里云主账号绑定到上架应用所属的钉钉组织。

      1. 通过阿里云主账号绑定功能把阿里云主账号绑定到钉钉组织的某个管理员身份。
      2. 一个钉钉组织下的管理员身份账号只能绑定一个阿里云主账号，但支持不通过管理员身份账号绑定不同的阿里云主账号。
      3. 把管理员绑定的阿里云主账号当做该组织的应用部署账号。
   2. 进入阿里云页面后点击“添加关联账号”，点击“去绑定”。

      **注意**：若**没有“添加关联账号”**，说明此账号已经绑定了阿里云主账号，不能再添加关联主账号，需要更换其他子管理员角色的钉钉账号。

      ![iShot_2023-02-03_15](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7138465761/p555673.png)
   3. 跳转到阿里云的主账号登录，输入主账号名（例如原钉钉云主账号一般为dingclou-xxxx）和密码，成功登录阿里云主账号，回跳刷新钉钉开发者后台，此时需要访问阿里云“[三方账号绑定](https://account.console.aliyun.com/v2/#/bind)”页面，选择钉钉账号进行扫码绑定：https://account.console.aliyun.com/v2/#/bind。

      ![111](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7138465761/p555675.png)

      **注意**：若在操作钉钉绑定过程中，提示“已绑定”，如下图，则说明该钉钉账号在已经有阿里云主账号绑定过，需要更换其他子管理员角色的钉钉账号或者找到已经绑定的阿里云账号进行解绑。

      ![iShot_2023-02-03_15](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7138465761/p555685.png)
   4. 要求阿里云主账号的维护者必须是企业的子管理员，并且不能解除该绑定关系。

      ![钉钉组织绑定 ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1737987361/p358562.png)
2. 在应用部署页选择上架应用的部署方式，部署方式包括：

   - 部署方式一：阿里云+计算巢+通讯录加密，缺点是需要接入通讯录加密，存在接入改造成本。
   - 部署方式二：阿里云+计算巢+数据安全中心云产品，缺点是需要购买数据安全中心产品，对RDS数据进行额外的防泄漏保护。
   - 部署方式三：阿里云+计算巢，缺点是应用只可以通过自有渠道进行推广。

   部署方式的差异请参考文档[部署方式介绍](0009-introduction-to-deployment-methods.md)。

   ![设置应用部署方式](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4604438871/p409613.png)
3. 第一次设置计算巢部署方式时，需要授权计算巢获取阿里云资源权限。

   ![计算巢授权](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4604438871/p409627.png)
4. 计算巢授权完成后的应用部署详情页，页面内容包括

   | **内容** | **说明** | **校验通过的标准** |
   | --- | --- | --- |
   | RDS | 用户配置rds推送的rds数据源。 | 1、将rds导入到计算巢的应用分组下。  2、设置rds的账号密码，连接测试成功。 |
   | 安全域名 | 用于检查当前应用的安全域名是否已申请完成。 | 1、申请钉钉安全域名。  2、按照激活标准配置使用安全域名，具体参考《[钉钉安全域名](0017-config-domain-name.md)》。 |
   | 数据安全中心 | 用于检查当前应用的数据安全中心配置是否完成。 | 1、rds导入到计算巢的应用分组下。  2、购买数据安全中心，在数据安全中心的控制台授权&绑定导入计算巢的rds实例，数据安全中心配置具体参考[启用数据安全中心（推荐）](0015-enable-data-security-center.md)。 |
   | 出口IP配置 | 用于检查当前应用出口IP配置是否计算巢应用上的eip资源。 | 1、将eip资源导入到计算巢的应用分组下。  2、在“**开发管理**”的“**出口IP**”，将eip添加到出口IP列表中。 |
   | 资源管理 | 用于跳转到关联计算巢应用的链接，通过该链接到计算巢上导入应用部署依赖的云资源。 | 注：应用绑定的云账号必须是部署上了钉应用云资源的账号，否则进入到计算巢控制台后无法找到云资源。 |

   ![应用部署详情页](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9968306461/p409643.png)
5. 点击"资源管理"跳转到关联计算巢应用详情页，通过导入资源按钮把应用部署依赖的资源关联到计算巢应用上

   > **[!NOTE]**
   >
   > - 必须关联上架应用依赖的SLB、RDS、ECS、EIP，参考文档[导入资源到计算巢](0012-import-resources-compute-nest.md)。
   > - 应用部署架构建议满足[架构最佳实践](0011-architecture-best-practices.md)。

   ![关联资源](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1737987361/p358671.png)
6. 申请安全域名，登录钉钉开发者后台，在上架应用中进行钉钉安全域名的绑定，依赖第5点关联的私网SLB资源，并配置HTTP协议的监听端口。

   > **[!NOTE]**
   >
   > - 上架应用的服务端接口必须通过安全域名进行访问。
   > - 三方应用的推送类型是HTTP或者SyncHttp也需要使用安全域名进行访问。

   ![安全域名1](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1737987361/p359095.png)
7. 数据安全中心购买云产品保护数据库RDS：

   登录[数据安全中心](https://yundun.console.aliyun.com/?spm=5176.2020520101.categories-n-products.dsddp.6ecb4df5CNlfVg&p=sddp#/sddp/authorization)，进行购买操作，详情请参考文档[启用数据安全中心（推荐）](0015-enable-data-security-center.md)。
8. 配置RDS数据源，如果要使用RDS推送，需要在计算巢应用上导入华东1或华北3区域的rds，然后在应用部署的rds页配置推送数据源。

   ![RDS推送配置](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9968306461/p409649.png)
9. 通过应用自检校验部署方式（已上架应用可选），通过应用自检校验部署方式应用自检流程中校验计算巢部署方式，或者找钉钉技术人工验证部署方式。

   ![应用自检1 ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2737987361/p359096.png)
10. 上架应用广场：

    应用自检流程通过计算巢部署方式后，推广方式可以选择上广场推广，详情请参考[提交应用商品上架](../07-TjCzIgfQs3-平台服务/0030-submit-your-product-to-the-shelves.md)。
