---
title: "培训任务督办：让企业学习的跟踪督办更高效"
source_url: "https://open.dingtalk.com/document/development/supervision-tasks-tracking-supervision"
namespace: "development"
slug: "supervision-tasks-tracking-supervision"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "待办任务 > 集成方案 > 培训任务督办：让企业学习的跟踪督办更高效"
doc_id: "doc_2b04f5bebd694176"
updated_at: "2026-11-17 17:52:53"
---

> Source: https://open.dingtalk.com/document/development/supervision-tasks-tracking-supervision
> Path: 应用开发 / 服务端 API / 待办任务 > 集成方案 > 培训任务督办：让企业学习的跟踪督办更高效
> Updated: 2026-11-17 17:52:53

# 培训任务督办：让企业学习的跟踪督办更高效

## **概述**

本方案通过集成钉钉通讯录与待办能力，实现企业培训学习任务的按角色自动指派、待办提醒、进度跟踪与一键催办，帮助培训管理员高效推动员工完成学习任务，提升培训覆盖率和完成率。

### **方案背景**

在数字化时代，企业培训已成为提高企业竞争力的重要措施，人才粗放式管理已无法满足未来企业的发展要求。传统的企业培训管理常常面临指派效率低、督学困难、新员工培训覆盖不足、学习沟通不畅等核心问题。

企业在日常运营中常面临以下痛点：

- **学习指派难**：不同岗位和职级的员工有不同的技能和知识要求，分配难度大；没有按岗位和职级指派学习，选人非常麻烦，低效。
- **培训督学难**：制造业用工密度大、流动率大，新员工培训学习管理困难。
- **新员工培训难**：新员工培训有统一的学习任务，无法保证所有新员工都完成学习任务；系统无法识别新员工，培训组织者工作机械繁重。
- **学习沟通难**：对于同一学习任务的学员，人员多区域分散，无法进行及时沟通；沟通讨论的入口步骤多，降低了学习交流兴趣。

### **核心价值**

本方案通过钉钉通讯录接口获取角色和部门人员信息，结合钉钉待办接口实现学习任务的自动指派与状态跟踪，帮助企业构建完整的培训任务管理体系。

- **按角色自动指派**：通过通讯录接口获取角色列表和指定角色的员工列表，自动为不同岗位和职级的员工匹配对应的学习任务。
- **待办任务直达**：调用钉钉待办接口为学员创建学习待办任务，任务直接出现在钉钉客户端待办页面，与审批事项并列展示，确保学员不遗漏。
- **进度跟踪与催办**：通过更新待办任务状态接口实时跟踪学员学习进度，结合Ding消息实现一键催办，提升培训完成率。

### **适用场景**

本方案适用于以下典型业务场景：

- **新员工入职培训学习任务指派与跟踪**：面向连锁酒店、零售门店等人员流动性大的行业，自动为新入职员工按岗位指派标准化培训课程，并通过待办任务跟踪完成情况。
- **专项技能职称考试学习任务督办**：面向需要定期组织技能认证或职称考试的企业，按不同角色和职级自动分发学习任务，确保全员按时完成。
- **跨区域多门店员工培训学习任务管理**：面向拥有多个分支机构或门店的企业，通过统一平台为分散在各地的员工创建和跟踪学习任务。

## **典型业务场景**

### **场景一：新员工入职培训学习任务指派与跟踪**

#### **痛点分析**

以连锁酒店行业为例，旗下多个品牌在全国拥有上百家门店，员工人数众多且流动性大。新员工入职后需要完成标准化的岗位培训，但传统方式下培训组织者需要手动为每位新员工逐一分配学习任务，工作量大且容易遗漏。

- 新员工入职后无法自动识别和匹配对应岗位的学习任务。
- 培训组织者需要手动逐个选人指派，效率低下且容易出错。
- 缺乏有效的跟踪手段，无法确认新员工是否按时完成学习任务。
- 培训完成情况无法量化统计，管理层难以评估培训效果。

#### **价值验证**

- **自动化流程**

  ![培训任务督办_场景一_新员工入职培训](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3719094971/p1112752.png)
- **核心优势**

  - **按角色自动指派学习任务**：通过获取角色列表和指定角色员工列表，自动识别新员工所属岗位并匹配对应的培训课程，无需手动选人指派。
  - **待办任务直达学员**：学习任务以钉钉待办形式推送到学员待办页面，学员可在钉钉移动端直接查看和完成，入口统一且不易遗漏。
  - **进度实时跟踪与统计**：管理员可实时查看每位学员的待办完成状态，超70%的核心岗位员工在线完成资质认证课程培训。

### **场景二：跨区域多门店员工培训学习任务督办**

#### **痛点分析**

面向拥有多个分支机构的集团型企业，员工分布在不同的城市和门店，培训组织者难以对分散在各地的学员进行统一管理和督学。培训任务的传达和跟进依赖层层通知，信息传递效率低且容易失真。

- 员工分布在不同区域，培训通知难以统一触达。
- 缺乏有效的督学手段，无法对未完成学员进行针对性提醒。
- 培训管理者无法实时掌握各区域的学习进度和完成率。
- 传统沟通方式入口步骤多，学员参与度低。

#### **价值验证**

- **自动化流程**

  ![培训任务督办_场景二_自动化流程](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3719094971/p1112753.png)
- **核心优势**

  - **跨区域统一任务分发**：通过通讯录接口获取全企业角色和人员信息，不受地域限制，统一为各地学员创建学习待办任务。
  - **待办状态实时更新**：学员完成学习后自动更新待办任务状态，管理员可实时查看各区域完成情况，实现数字化督学。
  - **一键催办提升完成率**：结合钉钉Ding消息能力，对未完成学员发起一键催办，确保培训任务按时完成。

## **实施指南**

### **技术架构**

- **接口调用层**：调用钉钉通讯录服务端API实现角色列表获取、指定角色员工列表获取，调用待办API实现待办任务新增与状态更新等操作。
- **应用认证层**：通过Client ID和Client Secret获取accessToken，鉴权调用者身份。
- **通讯录管理层**：调用通讯录相关API获取企业角色信息和角色下员工列表，获取userid等关键标识符。
- **待办任务管理层**：调用待办相关API创建学习待办任务和更新任务状态，查询任务详情。
- **错误处理层**：完善的错误码体系，便于快速定位和解决问题。

### **前置条件**

在实施方案前，需满足以下条件：

- **应用准备**：完成企业内部应用的创建与配置，参考[应用创建与配置](../01-XOnnmGCTbn-开发指南/0007-create-application.md)。
- **权限要求**：拥有钉钉企业管理员或子管理员权限，并申请以下接口权限：

  - `qyapi_get_department_list` （通讯录部门信息读权限）
  - `qyapi_get_department_member` （通讯录部门成员读权限）
  - `Todo.Todo.Write` （待办应用中待办写权限）
- **开发环境**：已安装Java开发环境（JDK1.6及以上）及Maven构建工具。
- **SDK准备**：下载钉钉服务端SDK，详情参见[服务端SDK下载](0002-download-the-server-side-sdk.md)，支持Java/Python/Go等多语言。

### **代码实现**

步骤一：完成[添加网页应用](../01-XOnnmGCTbn-开发指南/0007-create-application.md)流程，并接入[企业内部网页应用免登](0017-enterprise-internal-application-logon-free.md)。

步骤二：获取应用凭证信息，获取应用 Client ID 和 Client Secret。

步骤三：申请接口权限，申请待办相关接口的权限。

步骤四：获取应用访问凭证[获取企业内部应用的accessToken](0032-obtain-the-access-token-of-an-internal-app.md)，调用接口时，通过accessToken鉴权调用者身份。

步骤五：调用服务端待办相关API。

> **[!NOTE]**
>
> 若是第三方企业应用，则需要接入[统一授权套件](0008-applications-authorization.md)；若需要创建个人待办，请使用[创建钉钉个人待办任务](0794-api-createpersonaltodotask.md)。

1. 接入免登后，通过accessToken和免登码调用[通过免登码获取用户信息](0023-obtain-the-userid-of-a-user-by-using-the-log-free.md)接口，获取当前登录用户的`userid`、`unionid`和`name`。
2. 通过accessToken，调用[获取角色列表](0088-obtains-a-list-of-enterprise-roles.md)接口获取企业内角色列表信息。
3. 通过accessToken和角色id，调用[获取指定角色的员工列表](0095-obtain-the-list-of-employees-of-a-role.md)接口获取指定角色员工列表信息。
4. 服务端生成学习任务信息（任务标题/执行时间/跳转链接等），发送任务信息和执行用户id，调用[创建钉钉待办任务](0793-add-dingtalk-to-do-task.md)接口创建待办任务。
5. 任务执行人登录钉钉移动端，点击“消息”-->“待办”中查看任务。
6. 点击任务进入任务执行页面，执行任务并提交，调用[更新钉钉待办任务](0796-updates-dingtalk-to-do-tasks.md)接口更新钉钉待办任务。

## 实施步骤

### **步骤一：接入免登**

1. 创建应用，并完成[添加网页应用](../01-XOnnmGCTbn-开发指南/0007-create-application.md)流程。
2. 接入[企业内部网页应用免登](0017-enterprise-internal-application-logon-free.md)。

   ```
   import * as dd from 'dingtalk-jsapi';

   dd.requestAuthCode({
     corpId: 'corpid',
     clientId: 'clientid',
     onSuccess: function (result) {
       /*{
           code: 'hYLK98jkf0m' //string authCode
       }*/
     },
     onFail: function (err) {},
   });
   ```

### **步骤二：****获取应用凭证**

1. 登录[钉钉开发者后台](https://open-dev.dingtalk.com/)。
2. 选择目标应用，进入应用详情页。
3. 单击**基础信息** > **凭证与基础信息**。
4. 记录应用的`Client ID`和`Client Secret`。

   > **[!NOTE]**
   >
   > 请妥善保管 `Client Secret`，不要泄露给第三方。建议将其存储在环境变量或密钥管理系统中，避免硬编码在代码里。

### **步骤三：添加接口权限**

1. 在应用详情页，单击**权限管理**。
2. 在权限搜索框中输入以下权限标识并申请：

   - `qyapi_get_department_list` （通讯录部门信息读权限）—— 用于获取企业通讯录部门列表信息，为后续按部门筛选学员提供基础数据。
   - `qyapi_get_department_member` （通讯录部门成员读权限）—— 用于获取指定部门下的成员列表，确定培训任务的目标学员范围。
   - `Todo.Todo.Write` （待办应用中待办写权限）—— 用于创建和更新待办任务状态，标记学习任务为已完成。

> **[!NOTE]**
>
> 不同业务场景可能需要不同的权限组合，请根据实际需求申请。例如批量导入场景还需申请批量操作用户的相关权限。

### 步骤四：获取访问凭证（accessToken）

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

### **步骤五：核心API调用**

1. **获取登录用户信息**：通过accessToken和免登码调用[通过免登码获取用户信息](0023-obtain-the-userid-of-a-user-by-using-the-log-free.md)接口，获取当前登录用户的`userid`、`unionid`和`name`。

   ```
   public void getOapiV2UserGetuserinfo() throws Exception{
     DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/v2/user/getuserinfo");
     OapiV2UserGetuserinfoRequest req = new OapiV2UserGetuserinfoRequest();
     req.setCode("bab02f63c1e030fbbxxxx");
     OapiV2UserGetuserinfoResponse rsp = client.execute(req, access_token);
     System.out.println(rsp.getBody());
   }
   ```

   **参数说明**：

   - `access_token`：调用接口凭证。
   - `code`：免登授权码。

   **返回字段**：

   - `userid`：用户userid。
   - `unionid`：用户unionid。
   - `name`：用户姓名。
2. **获取角色列表**：通过accessToken，调用[获取角色列表](0088-obtains-a-list-of-enterprise-roles.md)接口获取企业内角色列表信息，为按角色指派学习任务提供基础数据。

   ```
   public void getRoleList(String accessToken) throws Exception {
     DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/role/list");
     OapiRoleListRequest request = new OapiRoleListRequest();
     request.setSize(200L);
     request.setOffset(0L);
     OapiRoleListResponse response = client.execute(request, accessToken);
     System.out.println(response.getResult().getList());
   }
   ```

   **参数说明**

   - `size`：分页大小，默认值20，最大值200。
   - `offset`：偏移量，从0开始。

   **返回字段**

   - `groupId`：角色组ID。
   - `name`：角色组名称。
   - `roles[].id`：角色ID。
   - `roles[].name`：角色名称。
3. **获取指定角色的员工列表**：通过accessToken和角色id，调用[获取指定角色的员工列表](0095-obtain-the-list-of-employees-of-a-role.md)接口获取指定角色员工列表信息，确定需要指派学习任务的目标学员。

   ```
   public void getRoleSimpleList(String accessToken, Long roleId) throws Exception {
     DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/role/simplelist");
     OapiRoleSimplelistRequest req = new OapiRoleSimplelistRequest();
     req.setRoleId(roleId);
     req.setSize(20L);
     req.setOffset(0L);
     OapiRoleSimplelistResponse rsp = client.execute(req, accessToken);
     System.out.println(rsp.getResult().getList());
   }
   ```

   **参数说明**

   - `role_id`：角色ID。
   - `size`：分页大小，默认值20，最大100。
   - `offset`：偏移量，从0开始。

   **返回字段**

   - `list[].userid`：员工的userid。
   - `list[].name`：员工姓名。
4. **新增钉钉待办任务**：调用[创建钉钉待办任务](0793-add-dingtalk-to-do-task.md)接口，为指定员工创建学习待办任务，任务将出现在钉钉客户端待办页面。

   ```
   public void createTodoTask() throws Exception {
     Config config = new Config();
     config.protocol = "https";
     config.regionId = "central";
     com.aliyun.dingtalktodo_1_0.Client client = new com.aliyun.dingtalktodo_1_0.Client(config);
     CreateTodoTaskHeaders createTodoTaskHeaders = new CreateTodoTaskHeaders();
     createTodoTaskHeaders.xAcsDingtalkAccessToken = "<your access token>";
     CreateTodoTaskRequest createTodoTaskRequest = new CreateTodoTaskRequest()
       .setOperatorId("PUoiinWIpxxx")
       .setSubject("接入钉钉待办")
       .setCreatorId("PUoiiP6g")
       .setDescription("应用可以调用该接口发起一个钉钉待办任务，该待办事项会出现在钉钉客户端“待办”页面")
       .setExecutorIds(java.util.Arrays.asList("PUoiixxxxhiiGiP6g"))
       .setParticipantIds(java.util.Arrays.asList("PUoxxxxiGiP6g"))
       .setPriority(20)
       .setTodoType("TODO");
     try {
       client.createTodoTaskWithOptions("PUoixxxxGiP6g", createTodoTaskRequest, createTodoTaskHeaders, new com.aliyun.teautil.models.RuntimeOptions());
     } catch (TeaException err) {
       if (!com.aliyun.teautil.Common.empty(err.code) && !com.aliyun.teautil.Common.empty(err.message)) {
         // err 中含有 code 和 message 属性，可帮助开发定位问题
         System.out.println(err.code);
         System.out.println(err.message);
       }
     } catch (Exception _err) {
       TeaException err = new TeaException(_err.getMessage(), _err);
       if (!com.aliyun.teautil.Common.empty(err.code) && !com.aliyun.teautil.Common.empty(err.message)) {
         // err 中含有 code 和 message 属性，可帮助开发定位问题
         System.out.println(err.code);
         System.out.println(err.message);
       }
     }
   }
   ```

   - `unionId`：（路径参数）当前访问资源所归属用户的unionId，和创建者的unionId保持一致。
   - `operatorId`：当前操作者用户的unionId。
   - `subject`：待办标题，最大长度1024。
   - `creatorId`：创建者的unionId。
   - `description`：待办备注描述，最大长度4096。。
   - `executorIds`：执行者的unionId。
   - `participantIds`：参与者的unionId。
   - `priority`：优先级。
   - `todoType`：待办的业务类型。

   **返回字段**

   - `id`：待办任务唯一ID。
   - `subject`：待办的标题。
   - `description`：待办描述。
   - `executorIds`：执行者的unionId。
   - `participantIds`：参与者的unionId。
   - `source`：业务来源。
   - `sourceId`：业务系统侧的唯一标识ID，即业务ID。
5. 创建成功后，任务执行人登录钉钉移动端，点击“消息”-->“待办”中查看任务。
6. **更新钉钉待办任务**：调用调用[更新钉钉待办任务](0796-updates-dingtalk-to-do-tasks.md)接口更新待办任务状态，标记学习任务为已完成。

   ```
   public void updateTodoTask() throws Exception {
     Config config = new Config();
     config.protocol = "https";
     config.regionId = "central";
     com.aliyun.dingtalktodo_1_0.Client client = new com.aliyun.dingtalktodo_1_0.Client(config);
     UpdateTodoTaskHeaders updateTodoTaskHeaders = new UpdateTodoTaskHeaders();
     updateTodoTaskHeaders.xAcsDingtalkAccessToken = "<your access token>";
     UpdateTodoTaskRequest updateTodoTaskRequest = new UpdateTodoTaskRequest()
       .setSubject("更新钉钉待办")
       .setDueTime(1617675000000L)
       .setDone(true);
     try {
       client.updateTodoTaskWithOptions("PUoiinxxx", "OPJpwtxxx", updateTodoTaskRequest, updateTodoTaskHeaders, new com.aliyun.teautil.models.RuntimeOptions());
     } catch (TeaException err) {
       if (!com.aliyun.teautil.Common.empty(err.code) && !com.aliyun.teautil.Common.empty(err.message)) {
         // err 中含有 code 和 message 属性，可帮助开发定位问题
         System.out.println(err.code);
         System.out.println(err.message);
       }
     } catch (Exception _err) {
       TeaException err = new TeaException(_err.getMessage(), _err);
       if (!com.aliyun.teautil.Common.empty(err.code) && !com.aliyun.teautil.Common.empty(err.message)) {
         // err 中含有 code 和 message 属性，可帮助开发定位问题
         System.out.println(err.code);
         System.out.println(err.message);
       }
     }
   }
   ```

   **参数说明**

   - `unionId`：（路径参数）当前访问资源所归属用户的unionId，需要操作者的unionId保持一致。
   - `taskId`：（路径参数）待办ID。
   - `subject`：待办标题，最大长度1024。
   - `dueTime`：截止时间，Unix时间戳，单位毫秒。
   - `done`：完成状态。

   **返回字段**

   - `result`：更新结果。

**实施完成检查清单**：

- ✅ 应用凭证已安全获取并妥善保管。
- ✅ 接口权限已正确添加，确保通讯录读权限和待办写权限均已授权。
- ✅ accessToken获取逻辑已实现并验证，缓存机制已正确配置。
- ✅ 角色列表接口调用成功，能正确获取企业所有角色信息。
- ✅ 指定角色员工列表接口调用成功，能正确获取角色下的员工userid和姓名。
- ✅ 新增待办任务接口调用成功，学员能在钉钉待办页面看到学习任务。
- ✅ 更新待办任务接口调用成功，学员完成学习后待办状态正确更新。
- ✅ 错误码处理逻辑已完善，能正确处理userid无效、参数不合法、待办重复等异常情况。

## **常见问题（FAQ）**

- **Q1：待办任务创建后多久会逾期？**

  待办创建后，若两个小时内未处理，则两小时后会被计入已逾期。
- **Q2：为什么创建待办任务时返回854001错误码？**

  该错误码表示待办任务重复。每人每天最多收到一条表单内容相同的待办（包括title和formItemList参数）。另外，当传了biz\_id参数时，每个用户的biz\_id也不能重复。
- **Q3：为什么调用待办接口时返回400002错误码？**

  每人每天最多收到100条待办任务，超过此限额会返回该错误码。请检查是否对同一用户频繁创建待办任务。
- **Q4：如何实现分页获取角色列表和员工列表？**

  通过size和offset参数实现分页查询。获取角色列表时，size最大为200；获取员工列表时，size最大为100。通过hasMore字段判断是否还有下一页数据。
- **Q5：accessToken过期了怎么办？**

  accessToken有效期为7200秒（2小时），有效期内重复获取会返回相同结果并自动续期。建议在代码中实现缓存机制，在accessToken过期前主动刷新。
