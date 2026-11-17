---
title: "考勤数据抽查：跨部门考勤核查与异常预警"
source_url: "https://open.dingtalk.com/document/development/hidden-common-callback-events"
namespace: "development"
slug: "hidden-common-callback-events"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "考勤 > 集成方案 > 考勤数据抽查：跨部门考勤核查与异常预警"
doc_id: "u9i2MeTTzp"
updated_at: "2026-11-06 11:34:15"
---

> Source: https://open.dingtalk.com/document/development/hidden-common-callback-events
> Path: 应用开发 / 服务端 API / 考勤 > 集成方案 > 考勤数据抽查：跨部门考勤核查与异常预警
> Updated: 2026-11-06 11:34:15

# 考勤数据抽查：跨部门考勤核查与异常预警

## **概述**

本方案基于钉钉考勤开放API，实现考勤数据的自动化定时抽取与多维度抽查比对，帮助管理层按时间、机构、部门、人员等维度对考勤达成情况进行常态化核查，及时发现考勤异常并推送预警通知，逐步提升企业整体考勤达成率。

### **方案背景**

考勤数据是企业人力资源管理的重要依据。企业使用钉钉考勤后积累了大量的打卡数据，但钉钉考勤仅提供基础的数据查询统计功能，无法满足日常考勤抽查的需求。企业在考勤管理中常面临以下痛点：

- **缺少横向纵向抽查对比**：无法对考勤数据基于时间、分支机构、部门等维度进行横向纵向抽查比对，难以发现异常部门和个人。
- **缺少逐级钻取核查**：无法对考勤数据进行从机构到部门再到个人的层层下钻抽查，问题定位效率低。
- **异常消息通知不及时**：无法在考勤数据出现异常时通过预警和消息推送的方式及时通知到相关负责人。
- **手工抽查效率低成本高**：为了做类似的抽查需要每天将数据导入Excel手工比对或通过代码开发数据接口获取数据，效率低成本高。

### **核心价值**

本方案通过调用钉钉考勤智能报表API自动定时抽取考勤数据，实现考勤数据的常态化抽查：

- **多维度抽查比对**：支持按时间、部门、人员等维度横向纵向抽查出勤率、迟到率、早退率等核心指标，快速锁定异常部门和人员。
- **层层下钻定位**：从集团到分公司到部门再到个人，逐层下钻抽查考勤数据，精准定位考勤异常源头。
- **抽查结果可视化**：以趋势图、占比图、排名图等可视化图表展现抽查结果，管理层一目了然。
- **异常实时预警**：抽查发现考勤指标偏离阈值时自动推送钉钉消息通知相关负责人，及时干预改进。

### **适用场景**

本方案适用于以下典型业务场景：

- **制造业多工厂考勤定期抽查**：跨区域多工厂的考勤达成率定期横向抽查，总部及时掌握各生产基地人员出勤异常情况。
- **连锁零售门店考勤排名抽查**：各门店考勤率排名抽查，快速识别落后门店，表扬先进敦促落后。
- **集团企业跨区域考勤异常抽查**：按时间维度定期抽查考勤率变化趋势，及时发现异常波动并预警。

## **典型业务场景**

### **场景一：山鹰纸业多工厂考勤达成率定期抽查**

#### **痛点分析**

山鹰纸业是国内造纸和包装行业龙头企业，在全国多个省份城市开办了造纸和包装工厂。公司总部希望及时掌握各地区、各工厂、各部门的人员考勤情况，前期推广并使用了钉钉考勤，但面临以下挑战：

- 各工厂考勤数据分散在钉钉系统中，总部无法统一抽查和比对。
- 手工导出Excel再汇总抽查，每月耗时数天且容易出错。
- 因为没有很好的途径对考勤数据进行多维度多层级抽查，无法对各地考勤情况进行相应的决策调整。
- 缺少抽查排名工具，管理层难以直观了解各基地考勤表现差异。

#### **价值验证**

- **自动化流程**

  ![制造业多工厂考勤抽查场景图_20261105_162012](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5506393971/p1110496.png)
- **核心优势**

  - **跨工厂定期抽查**：将各工厂各生产部门的考勤达成率进行横向抽查对比，管理层在钉钉端随时随地直观了解考勤达成率变化趋势。
  - **层层下钻核查**：从集团到工厂到部门到个人，逐层下钻抽查，精准定位考勤异常部门和个人。
  - **抽查排名驱动改进**：通过表扬先进敦促落后的措施，进一步提升员工积极使用钉钉考勤的意愿并主动改善本部门的考勤达成率。

### **场景二：集团总部考勤异常定时抽查与预警**

#### **痛点分析**

某集团企业在推行新的考勤制度后，需要持续抽查制度落地的实际效果。但当前面临以下问题：

- 无法按时间维度定期抽查考勤率的变化趋势，难以评估新制度的实际效果。
- 考勤数据异常时缺乏自动抽查预警机制，管理层被动等待月底报表才发现问题。
- 不同分支机构的考勤数据口径不统一，汇总抽查困难。
- 历史考勤抽查数据未沉淀为可分析的资产，无法支撑管理决策。

#### **价值验证**

- **自动化流程**

  ![集团考勤异常抽查场景图_20261105_162012](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5506393971/p1110497.png)
- **核心优势**

  - **定时抽查趋势变化**：按日期定期抽查出勤率、早退率和迟到率的变化趋势，清楚了解实行某项措施后整体考勤率的变化情况。
  - **抽查异常实时预警**：抽查发现考勤指标偏离预设阈值时自动推送钉钉消息通知相关负责人，实现从被动等待到主动干预的转变。
  - **抽查数据驱动制度优化**：基于历史考勤抽查数据分析，为考勤制度调整提供量化依据，持续提升考勤达成率。

## **实施指南**

### **技术架构**

- **接口调用层**：调用钉钉考勤服务端API实现考勤报表列定义获取、列值数据抽取、部门与用户信息查询等操作，支撑定时抽查任务。
- **应用认证层**：通过AppKey和AppSecret获取accessToken，鉴权调用者身份。
- **考勤数据层**：调用考勤智能报表API获取报表列定义与列值数据，实现考勤数据的自动化定时抽取。
- **通讯录数据层**：调用通讯录API获取部门列表与用户基础信息，建立组织架构与考勤抽查数据的关联关系。
- **错误处理层**：完善的错误码体系，便于快速定位和解决问题。

### **前置条件**

在实施方案前，需满足以下条件：

- **应用准备**：完成企业内部应用的创建与配置，参考**应用创建与配置**。
- **权限要求**：拥有钉钉企业管理员或子管理员权限，并申请以下接口权限：

  - `qyapi_base`（调用企业API时需要具备的基本权限）
  - `qyapi_get_department_list`（通讯录部门信息读权限）
  - `qyapi_get_department_member`（通讯录部门成员读权限）
- **开发环境**：已安装Java开发环境（JDK1.6及以上）及Maven构建工具。
- **SDK准备**：下载钉钉服务端SDK，详情参见**服务端SDK下载**，支持Java/Python/Go等多语言。
- **智能统计报表**：确保企业已在钉钉管理后台启用智能统计报表功能。

### **代码实现**

步骤一：获取应用凭证信息，获取应用 Client ID 和 Client Secret。

步骤二：申请接口权限，申请考勤相关接口权限。

步骤三：获取应用访问凭证[获取企业内部应用的access\_token](1456-obtain-orgapp-token.md)。调用接口时，通过accessToken鉴权调用者身份。

步骤四：相关调用流程：

1. 调用服务端API-[查询是否启用智能统计报表](0223-determine-whether-to-enable-attendance-intelligent-report.md)接口，来校验当前企业是否开启了智能统计报表。
2. 调用服务端API-[获取通讯录权限范围](0052-obtain-corpsecret-authorization-scope.md)接口，获取授权通讯录信息。
3. 调用服务端API-[获取部门列表](0081-user-management-acquires-the-list-departments.md)接口，获取部门列表ID值。
4. 通过部门列表ID，调用服务端API-[获取部门用户基础信息](0065-queries-the-simple-information-of-a-department-user.md)接口，获取部门的用户userid。
5. 调用服务端API-[获取考勤报表列定义](0222-queries-the-enterprise-attendance-report-column.md)接口，获取考勤报表中的报表列名和报表列ID。
6. 通过报表列ID，调用服务端API-[获取考勤报表列值](0221-queries-the-column-value-of-the-attendance-report.md)接口，获取钉钉智能考勤报表的列值数据。
7. 将考勤报表列定义和列值插入到本地数据库相应的数据库表即可完成钉钉考勤数据的抽取。

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

   - `qyapi_base`（调用企业API时需要具备的基本权限）-用于获取**考勤报表列定义与报表列值。**
   - `qyapi_get_department_list`（通讯录部门信息读权限）-用于获取部门用户基本信息。
   - `qyapi_get_department_member`（通讯录部门成员读权限）-用于获取部门用户成员。

> **[!NOTE]**
>
> 不同业务场景可能需要不同的权限组合，请根据实际需求申请。例如批量导入场景还需申请批量操作用户的相关权限。

### 步骤三：获取访问凭证（access\_token）

根据步骤一中 的 Client ID 和 Client Secret，获取应用访问凭证[获取企业内部应用的access\_token](1456-obtain-orgapp-token.md)。

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

1. **查询是否启用智能统计报表**：调用服务端API-[查询是否启用智能统计报表](0223-determine-whether-to-enable-attendance-intelligent-report.md)接口，校验当前企业是否已开启智能统计报表功能。

   > **[!NOTE]**
   >
   > 若该接口`smart_report`返回false，则代表未开启智能统计报表。

   ```
   public void getIsOpenSmartReport() throws ApiException {
     DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/isopensmartreport");
     OapiAttendanceIsopensmartreportRequest req = new OapiAttendanceIsopensmartreportRequest();
     OapiAttendanceIsopensmartreportResponse rsp = client.execute(req, access_token);
     System.out.println(rsp.getBody());
   }
   ```

   **参数说明**

   - `accessToken`：调用服务端接口的授权凭证。

   **返回字段**

   - `smart_report`：智能统计报表的开通状态。
2. **获取通讯录权限范围**：调用服务端API-[获取通讯录权限范围](0052-obtain-corpsecret-authorization-scope.md)接口，获取当前应用的通讯录授权范围，确认可抽查的组织架构范围。

   ```
   public void getScopes() throws ApiException {
     DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/auth/scopes");
     OapiAuthScopesRequest req = new OapiAuthScopesRequest();
     req.setHttpMethod("GET");
     OapiAuthScopesResponse rsp = client.execute(req, access_token);
     System.out.println(rsp.getBody());
   }
   ```

   **参数说明**

   - `accessToken`：调用服务端接口的授权凭证。

   **返回字段**

   - `authed_user`：授权可获取通信录信息的员工userid列表。
   - `authed_dept`：授权可获取通信录信息的部门ID列表。
   - `auth_user_field`：授权可获取的企业用户字段。
3. **获取部门列表**：调用服务端API-[获取部门列表](0081-user-management-acquires-the-list-departments.md)接口，获取各部门的ID值，用于后续按部门抽查用户考勤信息。

   ```
   public void getListsub() throws ApiException {
     DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/v2/department/listsub");
     OapiV2DepartmentListsubRequest req = new OapiV2DepartmentListsubRequest();
     req.setDeptId(1L);
     req.setLanguage("zh_CN");
     OapiV2DepartmentListsubResponse rsp = client.execute(req, access_token);
     System.out.println(rsp.getBody());
   }
   ```

   **参数说明**

   - `deptId`：父部门ID，根部门为1。

   **返回字段**

   - `dept_id`：部门ID。
   - `name`：部门名称。
   - `parent_id`：父部门ID。
4. **获取部门用户基础信息**：调用服务端API-[获取部门用户基础信息](0065-queries-the-simple-information-of-a-department-user.md)接口，根据部门ID获取部门下的用户userid列表，用于后续按用户查询考勤数据。

   ```
   public void getListSimple() throws ApiException {
     DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/user/listsimple");
     OapiUserListsimpleRequest req = new OapiUserListsimpleRequest();
     req.setDeptId(10L);
     req.setCursor(0L);
     req.setSize(10L);
     req.setOrderField("modify_desc");
     req.setContainAccessLimit(false);
     req.setLanguage("zh_CN");
     OapiUserListsimpleResponse rsp = client.execute(req, access_token);
     System.out.println(rsp.getBody());
   }
   ```

   **参数说明**

   - `deptId`：部门ID。
   - `cursor`：分页游标，首次传0。
   - `size`：分页大小，最大100。

   **返回字段**

   - `userid`：用户的userid。
   - `name`：用户姓名。
5. **获取考勤报表列定义**：调用服务端API-[获取考勤报表列定义](0222-queries-the-enterprise-attendance-report-column.md)接口，获取企业智能考勤报表中的列信息，包含列ID、列名等。

   ```
   public void getAttcolumns() throws ApiException {
     DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/getattcolumns");
     OapiAttendanceGetattcolumnsRequest req = new OapiAttendanceGetattcolumnsRequest();
     OapiAttendanceGetattcolumnsResponse rsp = client.execute(req, access_token);
     System.out.println(rsp.getBody());
   }
   ```

   **参数说明**

   - `accessToken`：调用服务端接口的授权凭证。

   **返回字段**

   - `result.columns`：报表列信息列表。
   - `columns[].id`：报表列ID，用于查询列值。
   - `columns[].name`：报表列名，如"应出勤天数""补卡次数"。
6. **获取考勤报表列值**：调用服务端API-[获取考勤报表列值](0221-queries-the-column-value-of-the-attendance-report.md)接口，获取指定用户在一定时间段内的考勤报表列值数据，支持多列同时查询。

   ```
   public void getColumnval() throws ApiException {
    DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/getcolumnval");
     OapiAttendanceGetcolumnvalRequest req = new OapiAttendanceGetcolumnvalRequest();
     req.setUserid("manager4220");
     req.setColumnIdList("129339038");
     req.setFromDate(StringUtils.parseDateTime("2020-09-07 12:12:12"));
     req.setToDate(StringUtils.parseDateTime("2020-09-09 12:12:12"));
     OapiAttendanceGetcolumnvalResponse rsp = client.execute(req, access_token);
     System.out.println(rsp.getBody());
   }
   ```

   **参数说明**

   - `userid`：用户的userid。
   - `column_id_list`：报表列ID，多值用英文逗号分隔，每次最多传20个。
   - `from_date`：开始时间。
   - `to_date`：结束时间，与开始时间间隔不超过31天。

   **返回字段**

   - `result.column_vals`：列信息与列值数据。
   - `column_vals[].date`：日期。
   - `column_vals[].value`：列值。
   - `column_vo.id`：报表列ID。
7. 将考勤报表列定义和列值插入到相应的数据库表，即可完成钉钉考勤数据的抽取。

**实施完成检查清单：**

- ✅ 企业内部应用已创建并获取AppKey和AppSecret。
- ✅ 接口权限企业考勤数据权限已申请并通过审批。
- ✅ 企业已在钉钉管理后台启用智能统计报表功能。
- ✅ accessToken获取接口调用正常且缓存机制已实现。
- ✅ 查询是否启用智能统计报表接口返回正常。
- ✅ 获取通讯录权限范围接口返回正确的部门可见范围。
- ✅ 获取部门列表接口可正常获取组织架构。
- ✅ 获取部门用户基础信息接口可正常获取用户列表。
- ✅ 获取考勤报表列定义接口返回正确的列信息。
- ✅ 获取考勤报表列值接口可正常获取指定用户的列值数据。
- ✅ 考勤数据已成功抽取并存储到本地数据库。
- ✅ 可视化分析仪表盘正常展示考勤趋势图、占比图和排名图。

## **常见问题（FAQ）**

- **Q1：调用考勤报表接口前需要满足什么条件？**

  必须确保企业已在钉钉管理后台启用智能统计报表功能。可先调用"查询是否启用智能统计报表"接口进行校验，若未启用需联系企业管理员在后台开通。
- **Q2：获取考勤报表列值接口的时间范围有什么限制？**

  结束时间减去开始时间必须在31天以内。如需获取更长时间范围的数据，需分段多次调用，每次查询不超过31天。
- **Q3：如何获取离职人员的考勤数据？**

  考勤报表接口不支持获取离职人员的考勤信息。离职人员的考勤数据可在钉钉企业管理后台的考勤统计页面查询。
- **Q4：columnIdList参数最多支持多少个列ID？**

  每次最多传20个列ID，多个列ID用英文逗号分隔。如需查询超过20个列的数据，需分多次调用。
- **Q5：考勤报表列定义接口返回的列ID会变化吗？**

  列ID在考勤报表模板不变的情况下是稳定的。如果企业在管理后台修改了智能统计报表的模板配置，列ID可能会发生变化，建议定期重新获取列定义。
