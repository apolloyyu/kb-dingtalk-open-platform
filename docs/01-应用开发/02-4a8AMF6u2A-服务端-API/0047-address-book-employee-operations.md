---
title: "企业通讯录员工管理自动化"
source_url: "https://open.dingtalk.com/document/development/address-book-employee-operations"
namespace: "development"
slug: "address-book-employee-operations"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "通讯录管理 > 使用教程 > 企业通讯录员工管理自动化"
doc_id: "58Wi4Lt3sV"
updated_at: "2026-09-15 09:36:19"
---

> Source: https://open.dingtalk.com/document/development/address-book-employee-operations
> Path: 应用开发 / 服务端 API / 通讯录管理 > 使用教程 > 企业通讯录员工管理自动化
> Updated: 2026-09-15 09:36:19

# 企业通讯录员工管理自动化

## **概述**

本方案提供一套完整的企业通讯录员工管理自动化解决方案，通过钉钉开放平台的通讯录管理API，实现HR系统、OA系统等业务平台与钉钉通讯录的无缝集成，解决传统人工维护通讯录效率低、易出错、实时性差等核心痛点。

### 方案背景

企业在数字化转型过程中，面临以下挑战：

- **多系统数据孤岛**：HR系统、OA系统、ERP系统等独立运行，员工信息需要在多个系统中重复维护，数据一致性难以保障。
- **人工运维成本高**：新员工入职需手动在钉钉后台添加账号，离职员工需逐个删除，千人级企业每月耗费数十小时人工操作。
- **组织架构变化响应慢**：部门调整、人员调动等业务变更无法及时同步到钉钉，影响审批流、权限管理等依赖通讯录的核心功能。
- **安全合规风险**：离职员工账号未及时禁用可能导致数据泄露，手工操作缺乏审计日志难以追溯。

### 核心价值

通过本方案，企业可以实现：

- **全流程自动化**：员工入职、离职、调岗等生命周期事件自动同步至钉钉通讯录，零人工干预。
- **数据实时一致**：确保各业务系统与钉钉通讯录数据保持同步，避免信息不一致导致的管理混乱。
- **安全合规可控**：离职员工账号自动禁用，所有操作留痕可追溯，满足企业审计要求。

### 适用场景

本方案适用于以下典型业务场景：

- HR**系统集成**：将企业人力资源管理系统与钉钉通讯录双向同步，实现员工信息自动增删改查。
- OA**流程自动化**：员工入职/离职审批流程结束后，自动创建或删除钉钉账号，释放License成本。
- **批量数据迁移**：企业并购、组织架构重组时，快速批量导入或调整数千名员工的通讯录信息。
- **跨系统身份统一**：确保ERP、CRM、财务系统等多平台使用统一的钉钉身份标识（userid），简化权限管理。

## 典型业务场景

### 场景一：HR系统自动同步（入职流程自动化）

#### **痛点分析**

传统模式下，HR在系统中录入新员工后，需手动登录钉钉后台逐条添加账号。千人级企业每月入职数十人，耗费大量人工时间且易出现数据录入错误。

#### **价值验证**

- **实施前**

  ![HR系统实施前流程_20260911_093601_20260911_093710](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9716349871/p1101868.png)
- **实施后**

  ![HR系统实施后流程_20260911_093658_20260911_093808](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9716349871/p1101869.png)
- **价值收益量化**

  | **指标** | **实施前** | **实施后** | **提升幅度** |
  | --- | --- | --- | --- |
  | 单人员工创建时间 | 8分钟 | 2秒 | 99.6% ↓ |
  | 人工错误率 | 5-10% | 0% | 100% ↓ |
  | 月度运维工时（千人企业） | 40小时 | <1小时 | 97.5% ↓ |

### 场景二：员工离职自动化处理（安全合规保障）

#### **痛点分析**

员工离职后，若未及时禁用钉钉账号，可能导致企业敏感数据泄露。手工操作依赖HR通知IT，存在时间差和遗漏风险。

#### **价值验证**

- **自动化流程**

  ![员工离职自动化流程_20260911_093755_20260911_093906](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9716349871/p1101870.png)
- **关键优势**

  - **安全风险消除**：离职员工账号即时禁用，避免数据泄露隐患。
  - **成本优化**：自动释放钉钉账号License，降低企业订阅成本。
  - **审计合规**：所有操作留痕可追溯，满足企业内控和外部审计要求。
  - **无缝集成**：与OA审批流程自动联动，无需人工介入。

## 实施指南

### **技术架构**

本方案基于钉钉开放平台的服务端API构建，核心技术组件包括：

- **身份鉴权层：**通过`Client ID`/`Client Secret`获取`access_token`，确保接口调用安全性。
- **通讯录管理层**：提供用户创建、查询、更新、删除等完整API能力。
- **权限控制层**：细粒度权限管理，支持申请特定接口权限（`qyapi_manage_addresslist`等）。
- **错误处理层**：完善的错误码体系，便于快速定位和解决问题。

**API版本说明**：服务端API存在新版与旧版差异，建议优先使用新版API以获得更好的性能和功能支持。详情参见[新版API VS 旧版API](0002-download-the-server-side-sdk.md#section-8lr-id4-rbz)。

### 前置条件

在实施方案前，需满足以下条件：

- **应用准备：**完成企业内部应用的创建与配置，参考[应用创建与配置](../01-XOnnmGCTbn-开发指南/0007-create-application.md)。
- **权限要求：**拥有钉钉企业管理员或子管理员权限。
- **开发环境：**已安装Java开发环境（JDK1.6及以上）及Maven构建工具。
- **SDK准备：**下载钉钉服务端SDK，详情参见[服务端SDK下载](0002-download-the-server-side-sdk.md)，支持Java/Python/Go等多语言。

### **代码实现**

创建一个企业内部应用，使用**通讯录管理**提供的**用户管理**相关API，实现创建、获取、更新和删除企业员工等。

步骤一：获取应用凭证信息，获取应用 Client ID 和 Client Secret。

步骤二：申请接口权限，申请通讯录管理相关接口权限。

步骤三：获取应用访问凭证[获取企业内部应用的access\_token](1443-obtain-orgapp-token.md)。调用接口时，通过accessToken鉴权调用者身份。

步骤四：调用通讯录相关API：

1. 调用服务端API-[创建用户](0054-user-information-creation.md)接口，实现用户创建。获取用户`userid`。

   - 如果员工添加到根部门，接口参数传1即可。本示例采用添加员工至根部门。
   - 如果员工添加到某个部门下，先调用[获取子部门ID列表](0082-obtain-the-list-of-sub-department-ids.md)接口获取部门ID，作为创建用户接口的部门参数。
2. 根据用户`userid`信息，调用服务端API-[查询用户详情](0055-query-user-details.md)接口，获取用户详细信息。
3. 根据用户`userid`信息，调用服务端API-[更新用户信息](0056-user-information-update.md)接口，实现更新用户信息。
4. 根据用户`userid`信息，调用服务端API-[删除用户](0057-delete-a-user.md)接口，实现删除用户信息。

## **实施步骤**

### **步骤一：获取应用凭证**

1. 登录[钉钉开发者后台](https://open-dev.dingtalk.com/)。
2. 选择目标应用，进入应用详情页。
3. 单击**基础信息** > **凭证与基础信息**。
4. 记录应用的`Client ID`和`Client Secret`。

   > **[!NOTE]**
   >
   > 请妥善保管`Client Secret`，不要泄露给第三方。建议将其存储在环境变量或密钥管理系统中，避免硬编码在代码里。

### **步骤二：申请接口权限**

1. 在应用详情页，单击**权限管理。**
2. 在权限搜索框中输入以下权限标识并申请：

   1. `qyapi_manage_addresslist`（通讯录数据管理权限） - 用于创建、更新、删除用户。
   2. `qyapi_get_department_list`（通讯录部门信息读权限） - 用于查询部门ID。

> **[!NOTE]**
>
> 不同业务场景可能需要不同的权限组合，请根据实际需求申请。例如批量导入场景还需申请批量操作用户的相关权限。

### **步骤三：获取访问凭证（access\_token）**

根据步骤一中的 `Client ID` 和 `Client Secret`，调用[获取企业内部应用的access\_token](1443-obtain-orgapp-token.md)接口，获取应用访问凭证。

```
public void getAccessToken() throws ApiException {
  DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/gettoken");
  OapiGettokenRequest req = new OapiGettokenRequest();
  req.setAppkey("dingxxxxxxxxxhgn");
  req.setAppsecret("9G_xxxxxxxxxxxxxxx1JDf0Qq3nexxxxxxxxGIO");
  req.setHttpMethod("GET");
  OapiGettokenResponse rsp = client.execute(req);
  System.out.println(rsp.getBody());
}
```

**最佳实践**：

- **缓存策略**：`access_token`有效期为2小时，建议在内存或Redis中缓存，过期前5分钟主动刷新。
- **并发控制**：避免多个线程同时刷新token导致冲突，可使用分布式锁机制。
- **异常重试**：网络波动时自动重试，最多3次，间隔递增（1s → 2s → 4s）。

### **步骤四：核心API调用**

#### **创建用户（入职自动化）**

**接口说明**：

调用服务端API-[创建用户](0054-user-information-creation.md)接口，实现用户创建并获取唯一标识`userid`：

```
public void createUser() throws ApiException {
    DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/v2/user/create");
    OapiV2UserCreateRequest req = new OapiV2UserCreateRequest();
    
    req.setUserid("manger7676");
    req.setName("1009测试用户");
    req.setSeniorMode(false);
    req.setMobile("152****3025");
    req.setTitle("技术总监");
    req.setEmail("test*****@xx.com");
    req.setOrgEmail("test***@xxx.com");
    req.setOrgEmailType("profession");
    
    ArrayList<OapiV2UserCreateRequest.DeptTitle> deptTitles = new ArrayList<>();
    OapiV2UserCreateRequest.DeptTitle deptTitle = new OapiV2UserCreateRequest.DeptTitle();
    deptTitle.setDeptId(724960197L);
    deptTitle.setTitle("资深技术总监");
    deptTitles.add(deptTitle);
    req.setDeptTitleList(deptTitles);
    
    req.setHideMobile(false);
    req.setTelephone("010-8xxxxx6-2345");
    req.setJobNumber("202210190001");
    req.setHiredDate(1666143772000L);
    req.setWorkPlace("阿里中心******");
    req.setRemark("备注信息");
    req.setDeptIdList("724960197");
    
    List<OapiV2UserCreateRequest.DeptOrder> deptOrderList = new ArrayList<>();
    OapiV2UserCreateRequest.DeptOrder deptOrder = new OapiV2UserCreateRequest.DeptOrder();
    deptOrder.setDeptId(724960197L);
    deptOrder.setOrder(1L);
    deptOrderList.add(deptOrder);
    req.setDeptOrderList(deptOrderList);
    
    req.setExtension("{\"爱好\":\"[爱好](http://test.com?userid=#userid#&corpid=#corpid#)\"}");
    req.setManagerUserid("manager7676");
    req.setLoginEmail("test****@xxx.com");
    
    OapiV2UserCreateResponse rsp = client.execute(req, "access_token");
    System.out.println(rsp.getBody());
}
```

**部门分配策略**：

- 根部门：固定传`1`，适用于暂不确定具体部门的场景
- 指定部门：先调用[获取子部门ID列表](0082-obtain-the-list-of-sub-department-ids.md)接口获取部门ID：

```
public void departmentListSubId() throws ApiException {
    DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/v2/department/listsubid");
    OapiV2DepartmentListsubidRequest req = new OapiV2DepartmentListsubidRequest();
    req.setDeptId(1L);
    OapiV2DepartmentListsubidResponse rsp = client.execute(req, "access_token");
    System.out.println(rsp.getBody());
}
```

#### 查询用户详情（数据校验）

**接口说明**：

根据用户`userid`[查询用户详情](0055-query-user-details.md)，用于数据同步后的校验或业务系统读取：

```
public void userInfo() throws ApiException {
  DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/v2/user/get");
  OapiV2UserGetRequest req = new OapiV2UserGetRequest();
  req.setUserid("manger7676");
  req.setLanguage("zh_CN");
  OapiV2UserGetResponse rsp = client.execute(req, "access_token");
  System.out.println(rsp.getBody());
}
```

> **[!NOTE]**
>
> 部分字段的返回受权限限制，请参考[查询用户详情](0055-query-user-details.md)的返回字段说明。

**典型应用**：

- HR系统同步后校验数据一致性。
- OA审批流中动态获取申请人部门信息。
- 权限系统根据用户所属部门授予相应资源访问权限。

#### **更新用户信息（调岗/晋升）**

**接口说明**：

根据用户`userid`，[更新用户信息](0056-user-information-update.md)：

```
public void userModify() throws ApiException {
    DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/v2/user/update");
    OapiV2UserUpdateRequest req = new OapiV2UserUpdateRequest();
    
    req.setUserid("manger7676");
    req.setName("小钉");
    req.setHideMobile(false);
    req.setTelephone("010-86*****6-2345");
    req.setJobNumber("202210190002");
    req.setTitle("技术总监");
    req.setEmail("test*****@xxx.com");
    req.setWorkPlace("未来park");
    req.setRemark("备注备注");
    req.setDeptIdList("1");
    
    List<OapiV2UserUpdateRequest.DeptOrder> list2 = new ArrayList<>();
    OapiV2UserUpdateRequest.DeptOrder obj3 = new OapiV2UserUpdateRequest.DeptOrder();
    obj3.setDeptId(1L);
    obj3.setOrder(1L);
    list2.add(obj3);
    req.setDeptOrderList(list2);
    
    req.setExtension("{\"爱好\":\"旅游\",\"年龄\":\"24\"}");
    req.setSeniorMode(false);
    req.setHiredDate(1633017600000L);
    req.setLanguage("zh_CN");
    
    OapiV2UserUpdateResponse rsp = client.execute(req, "access_token");
    System.out.println(rsp.getBody());
}
```

> **[!NOTE]**
>
> - 出于安全考虑的设计决策，更新用户信息接口不支持更新手机号。
> - 如需修改手机号，建议通过钉钉管理后台手动修改，引导员工本人在钉钉客户端中自行修改。
> - 极端情况下可删除原账号后重新创建（不推荐，会丢失历史数据）。

**典型场景**：

- **员工调岗**：更新`department_ids`字段。
- **晋升/降级**：更新`job_number`或自定义字段。
- **邮箱变更**：更新`email`字段。

#### **删除用户（离职处理）**

根据用户`userid`从企业通讯录中[删除用户](0057-delete-a-user.md)：

```
public void userDelete() throws ApiException {
    DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/v2/user/delete");
    OapiV2UserDeleteRequest req = new OapiV2UserDeleteRequest();
    req.setUserid("manager7676");
    OapiV2UserDeleteResponse rsp = client.execute(req, "access_token");
    System.out.println(rsp.getBody());
}
```

> **[!NOTE]**
>
> - 删除操作不可逆，请谨慎使用。
> - 建议在删除前： 备份该员工的历史数据（聊天记录、钉盘文件等）、确认相关业务流程已完成（如待办事项已转移）、通知相关部门（IT、财务、行政等）进行后续清理工作。

## **数据保障与监控**

### API调用监控

为确保方案稳定运行，建议建立以下监控指标：

**核心指标**：

- 接口成功率：重点关注创建用户、查询用户等核心接口的成功率（目标>99.9%）。
- 响应时间：P95响应时间应控制在500ms以内，超时需告警。
- 批量处理效率：千人级批量导入应在30分钟内完成，否则检查网络或分批策略。

**监控工具**：

- 钉钉开发者后台提供API调用统计，可查看调用次数、成功率、错误分布。

### 错误码排查指南

| **错误码** | **含义** | **解决方案** |
| --- | --- | --- |
| `errcode=40001` | access\_token无效 | 检查`Client ID`和`Client Secret`是否正确，或重新获取`access_token`。 |
| `errcode=60020` | 未授权接口权限 | 在开发者后台添加对应的接口调用权限并提交审核。 |
| `errcode=40035` | 参数错误 | 检查必填参数是否完整，数据格式是否符合要求（如手机号格式）。 |
| `errcode=400003` | 用户不存在 | 确认`userid`是否正确，或先调用创建接口。 |
| `errcode=400004` | 手机号已被使用 | 该手机号已绑定其他钉钉账号，需解绑后重试。 |

**排查流程：**

- 查看返回的`errcode`和`errmsg`，定位问题类型。
- 参考钉钉开放平台[全局错误码](0013-server-api-error-codes-1.md)文档，查找详细解释。
- 检查请求参数、权限配置、网络连通性。
- 若问题持续，联系钉钉技术支持并提供请求日志。

### 典型场景判断依据

**成功场景特征：**

- ✅ 创建用户后返回有效的`userid`（格式如"user001"）。
- ✅ 查询接口能正确返回员工详细信息（name、mobile、department\_ids等）。
- ✅ 批量操作时，失败率<1%，且失败原因可追溯。

**失败场景特征**：

- ❌ 提示"权限不足" → 检查是否在开发者后台申请了对应权限。
- ❌ 提示"参数错误" → 检查必填字段、数据格式（如手机号需11位数字）。
- ❌ 提示"网络超时" → 检查服务器网络连通性，或增加超时时间。
- ❌ 提示"access\_token过期" → 刷新token并重试。

## 常见问题（FAQ）

- **Q1：如何通过钉钉开放平台API创建员工?**

  答：参考本文"步骤四：核心API调用"中的"4.1 创建用户"部分。需要先获取`access_token`，然后调用创建用户接口，传入员工基本信息（姓名、手机号、部门ID等），接口会返回新创建员工的`userid`。

  关键要点：

  - 必填参数：`name`（姓名）、`mobile`（手机号）
  - 可选参数：`department_ids`（部门ID列表，默认为根部门`1`）、`email`、`job_number`（工号）
  - 返回结果：`userid`（后续所有操作的唯一标识）
- **Q2：调用创建/更新部门接口时，department\_id（部门ID）应如何获取和填写?**

  答：

  - 根部门ID：固定为`1`，所有企业都有且仅有一个根部门
  - 子部门ID：调用"[获取子部门ID列表](0082-obtain-the-list-of-sub-department-ids.md)"接口（`departmentListSubId`）获取指定父部门下的所有子部门ID
  - 多级部门：可通过递归调用获取深层子部门ID，或通过"[获取部门详情](0080-query-department-details0-v2.md)"接口查询特定部门的完整信息
- **Q3：是否可通过钉钉开放平台API更新员工手机号？需满足哪些条件和权限？**

  答：暂时不支持通过API更新手机号。这是出于安全考虑的限制设计。如需修改员工手机号，建议采用以下方案：

  - 方案一（推荐）：通过钉钉管理后台手动修改，由管理员操作并留痕
  - 方案二：引导员工本人在钉钉客户端中自行修改
  - 方案三（极端情况）：删除原账号后重新创建（不推荐，会丢失历史聊天记录、钉盘文件等数据）

  技术原因：手机号是钉钉账号的核心身份标识，涉及短信验证、安全登录等多重机制，直接修改可能引发安全风险。
- **Q4：如何获取企业根部门ID（即根部门的department\_id）?**

  答：企业根部门ID固定为`1`，无需额外获取。所有企业都有且仅有一个根部门，其ID恒定为`1`。
