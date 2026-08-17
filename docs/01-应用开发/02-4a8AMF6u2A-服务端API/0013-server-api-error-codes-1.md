---
title: "全局错误码"
source_url: "https://open.dingtalk.com/document/development/server-api-error-codes-1"
namespace: "development"
slug: "server-api-error-codes-1"
group: "应用开发"
tab: "服务端API"
breadcrumb: "API 调用指南 > 全局错误码"
doc_id: "hwHUXIAmJL"
updated_at: "2026-05-06 10:20:52"
---

> Source: https://open.dingtalk.com/document/development/server-api-error-codes-1
> Path: 应用开发 / 服务端API / API 调用指南 > 全局错误码
> Updated: 2026-05-06 10:20:52

# 全局错误码

在调用钉钉开放平台接口时，开发者会收到对应的返回结果，包含成功或失败的错误码信息。通过分析错误码，可快速定位问题并进行调试。

> **[!NOTE]**
>
> 以下是服务端通用错误码列表，若某API接口的错误码未列入全局错误码中，请在对应 API 接口文档中查询。或通过右上角搜索功能，全局查找错误码说明和排查建议。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 200 | - | OK | 请求成功。 |
| 200 | content.dublication | update the same content | 更新了相同的备注 |
| 200 | integrationConfig.not.found | Data integration config not found. | 数据集成配置不存在 |
| 200 | integrationConfig.not.found | Tenant integration config not found. | 数据集成配置不存在 |
| 200/400 | invalidDept | INVALID DEPT | 非法的部门ID |
| 200/400/500 | param.openSpaceIdInvalid | param.openSpaceIdInvalid | openSpaceId不符合规范 |
| 200/400 | parameterInvalid | PARAMETER\_INVALID | 非法的业务编码；参数错误，请先完成学生信息转换；参数错误，请先完成家校通讯录转换；参数错误，请先完成家长信息转换；参数错误，请先完成高校通讯录转换 |
| 200/400/500/502/504 | processInstanceStartFailed | 创建审批实例失败 | 创建审批实例失败 |
| 200 | sizeTooLarge | Data size too large. | 数据量过大，单次限定50 |
| 200 | sizeTooLarge | Data size tool large. | 数据量多大，单次限定50；数据量过大，单次限定50 |
| 200 | staff.not.found | 钉钉员工不存在 | 钉钉员工不存在 |
| 200/400 | sysErrror | 创建审批实例系统异常 | 创建审批实例系统异常 |
| 200 | tenant.not.found | Tenant not found. | 租户不存在 |
| 201/400/502 | resource.not.found | %s | 机器人不存在；资源不存在，可能是机器人不存在；机器人不存在 |
| 400 | - | Bad Request | 请求参数错误，服务器无法理解。 |
| 400/500 | accessStorageFail | 调用存储异常 | 调用存储异常 |
| 400 | accesstoken.expired | 用户accessToken过期 | 用户accessToken过期 |
| 400 | accountNotRealname | 发起人账号在e签宝未实名发起人账号在e签宝未实名 | 发起人账号在e签宝未实名 |
| 400 | addSpace.forbiden | Add space is forbiden. | 你所在的组织的管理员已设置：禁止新建共享空间，已创建空间可正常使用 |
| 400 | aflowProcessCodeIsError | 获取审批模板失败或审批模板已被删除 | 获取审批模板失败或审批模板已被删除 |
| 400 | aflowProcessFormContentInvalid | 审批流的表单格式错误 | 审批流的表单格式错误 |
| 400 | aflowProcessFormDataIsNull | 流程表单数据为空 | 流程表单数据为空 |
| 400 | aflowProcessFormDatalsNull | 流程表单数据为空 | 流程表单数据为空 |
| 400 | aflowProcessGetFailed | 获取用户可见的审批模板失败 | 获取用户可见的审批模板失败 |
| 400 | aflowProcessInstCanNotBeExecuted | 审批状态异常，无法执行 | 审批状态异常，无法执行 |
| 400 | aflowProcessInstNotExist | 审批实例不存在 | 审批实例不存在；请检查processInstanceId参数是否正确 |
| 400 | aflowProcessInstStatusException | %s | 审批单状态异常，具体可能为：提交审批单后15秒内不能进行撤回、审批单已结束等；归档失败，审批单状态异常，具体可能为：仅支持对已完成的审批单操作归档、不能重复操作归档等 |
| 400 | aflowProcessInstStatusException | 审批单状态异常 | 审批单状态异常 |
| 400 | aflowProcessNotExist | 审批流不存在 | 审批流不存在 |
| 400 | aflowProcessSetupNoPermission | 无操作审批流的权限，请检查processCode是否正确 | 无操作审批流的权限，请检查processCode是否正确 |
| 400 | aim.nonexist | 您尚未开通钉钉客联服务，请联系钉钉官方客服咨询开通 | 您尚未开通钉钉客联服务，请联系钉钉官方客服咨询开通 |
| 400 | aim.nonexist | 租户不存在，请检查 | 租户不存在，请检查 |
| 400 | api.control.close | API CONTROL ClOSE | 会议室未开启中控能力 |
| 400 | apiPermissionDenied | 无权限访问此接口 | 无权限访问此接口 |
| 400 | app.not.exist | app不存在 | app不存在 |
| 400 | appender.contains.currentOperator | 加签任务，加签人不能包含当前操作人 | 请检查operatorId、appenderUserIds参数传值 |
| 400 | applicationNotExist.application.applicationNotExits | 应用不存在:%s | 应用不存在 |
| 400 | applicationNotExist.application.notExits | 应用不存在:%s | 应用不存在 |
| 400 | appQuotaInsufficient | %s | 应用容量不足 |
| 400 | appTypeNotSupport | 只支持企业自建小程序调用 | 只支持企业自建小程序调用 |
| 400 | assign.lack | 管理员未签署协议 | 管理员未签署协议 |
| 400/500 | assistant.not.exist | AI助理不存在 | AI助理不存在 |
| 400 | assistant.not.exsit | AI助理不存在 | AI助理不存在 |
| 400 | atMember.nonexist | at的人员不存在或者不在群中 | at的人员不存在或者不在群中 |
| 400 | auth.error | %s | 权限不足，不允许操作；权限校验不通过 |
| 400 | auth.failed | %s | 无权限，群内安装的群模板不属于当前token对应的应用名下；权限校验不通过 |
| 400 | autoflowLikeTriggerRateLimited | 该操作涉及自动化类业务(业务规则)并且触发限速, 请降速调用或取消相关自动化类业务配置 | 该操作涉及自动化类业务(业务规则)并且触发限速, 请降速调用或取消相关自动化类业务配置 |
| 400 | badRequest | %s | 参数错误，请确保 operationUserId、bid、nextToken 等参数合法。 |
| 400 | badRequest | badRequest | 参数错误，请确保 operationUserId、blackboardId 参数合法。 |
| 400 | batch.exceed | 每批获取量超最大值 | 每批获取量超最大值 |
| 400 | batch.toolarge | 每批接受人数超20 | 每批接受人数超20 |
| 400 | beginDateCannotAfterEndDate | 开始时间不能晚于结束时间 | 开始时间不能晚于结束时间 |
| 400 | benefit.query.error | 权益查询失败 | 权益系统查询失败 |
| 400 | benefit.query.error | 权益查询失败，请稍后重试 | 权益查询失败 |
| 400/500 | benefit.status.invalid | 权益校验失败，未开通或过期 | 权益校验；权益校验失败，未开通或过期 |
| 400 | benefit.status.invalid | 权益校验失败，未开通或过期，请开通/续费OA高级版 | 权益校验失败 |
| 400 | benefitStatusInvalid | 权益校验失败。指定bizDetailPageUrl为OA高级版专享功能，请开通高级版后再重试。 | 权益校验失败。指定bizDetailPageUrl为OA高级版专享功能，请开通高级版后再重试。 |
| 400 | bizDir.not.exist | 分组不存在或已删除 | 分组不存在或已删除，请检查入参。 |
| 400 | bizDir.number.exceed | 分组的数量到达上限，每个应用最多支持创建10个分组 | 分组的数量到达上限，每个应用最多支持创建10个分组，请先清理无效分组。 |
| 400 | bizTypeCannotModified | 假期业务类型不能修改 | 假期业务类型不能修改 |
| 400 | bizTypeIncorrect | 假期业务类型不正确 | 假期业务类型不正确 |
| 400 | bot.forbidden.sendMessage | %s | 账户被禁言 |
| 400 | bot.forbidden.sendMessage | 账户被禁言 | 账户被禁言 |
| 400 | bot.stopped | %s | 群机器人已经停用 |
| 400 | bot.stopped | 群机器人已经停用 | 群机器人已经停用 |
| 400 | businessError | %s | 业务错误 |
| 400 | businessError | businessError, %s | 业务错误 |
| 400 | cacheNotExists.cache.notExists | 缓存类型不存在:%s | 缓存类型不存在 |
| 400/500 | callAlipayFail | 调用支付宝异常 | 调用支付宝异常；无效的请求参数；调用支付宝异常 |
| 400 | callbackUrl.empty | 回调地址为空 | 回调地址为空 |
| 400/500 | callOrgFail | 调用内部通讯录异常 | 调用内部通讯录异常 |
| 400 | cancelCorpAuthError | 取消授权异常 | 取消授权异常 |
| 400 | cannot.ban.owner | 不允许禁言群主 | 不允许禁言群主 |
| 400 | cannot.find.user | 找不到该用户 | 找不到该用户 |
| 400 | canNotModifyOutLeadsId | can not modify outLeadsId | 不允许修改outLeadsId |
| 400 | card.content.checkFailed | 卡片内容违规 | 卡片内容违规 |
| 400 | card.outTraceIdEmpty | 业务标识outTrackId为空 | 业务标识outTrackId为空 |
| 400 | card.outTraceIdError | 卡片业务标识信息格式非法 | 卡片业务标识信息格式非法 |
| 400 | card.templateEmpty | 卡片模板ID为空 | 卡片模板ID为空 |
| 400 | cardInstance.notExist | 互动卡片实例不存在 | 互动卡片实例不存在 |
| 400 | cardInstance.notExist | 卡片实例不存在 | 卡片实例不存在 |
| 400 | cardInstance.wrong | 创建卡片实例失败，先检查卡片模板是否已发布 | 创建卡片实例失败，先检查卡片模板是否已发布 |
| 400 | cardMessage.sendFailed | 发送互动卡片消息失败 | 发送互动卡片消息失败 |
| 400 | cardTemplate.not.exist | 卡片模板不存在 | 卡片模板不存在 |
| 400 | cardTemplateInvalid | 卡片模板无效 | 卡片模板无效 |
| 400 | channel.nonexist | 渠道不存在，请检查 | 渠道不存在，请检查 |
| 400 | chat.coolApp.notInstalled | 酷应用未安装到会话内 | 酷应用未安装到会话内 |
| 400 | chat.notExist | 会话不存在 | 会话不存在 |
| 400 | chatbot.notFound | 机器人不存在 | 机器人不存在 |
| 400 | chatbotId.notAllow.sendOTO | %s | 不允许主动发单聊，请检查机器人状态是否已启用 |
| 400 | chatbotId.notAllow.sendOTO | 不允许主动发单聊 | 不允许主动发单聊 |
| 400 | chatbotNotFound | 不存在的机器人 | 不存在的机器人 |
| 400 | chatbotNotFound | 机器人不存在 | 机器人不存在 |
| 400 | chatbotNotInstall | 机器人未安装 | 机器人未安装 |
| 400 | checkParameter.param.error | %s | 参数校验失败；项目id不能为空；项目组id不能为空 |
| 400 | cidDecryptError | 群ID解析失败 | 群ID解析失败 |
| 400 | cidEncryptError | 群ID解析错误 | 群ID解析错误 |
| 400 | cidParse.wrong | 会话id解码失败 | 会话id解码失败 |
| 400 | cidParse.wrong | 单聊会话ID解码失败 | 单聊会话ID解码失败 |
| 400 | cidParse.wrong | 群ID解码失败 | 群ID解码失败 |
| 400 | client.add.error | 创建钉外账号及关联关系失败 | 创建钉外账号及关联关系失败 |
| 400 | client.nameIllegal | 用户名称中包含不合规内容，请检查 | 用户名称中包含不合规内容，请检查 |
| 400 | client.nonexist | 钉外账号不存在，请检查 | 钉外账号不存在，请检查 |
| 400 | clientOwner.nonexist | 群主不存在，群主为钉外账号 | 群主不存在，群主为钉外账号 |
| 400 | close.topbox.failed | 关闭吊顶失败 | 关闭吊顶失败 |
| 400 | closeTopbox.failed | 关闭吊顶失败 | 关闭吊顶失败 |
| 400 | cloudRecordNotFound | cloudRecordNotFound | 云录制记录未找到/未开启云录制 |
| 400 | codeNotExist | 用户码不存在 | 用户码不存在 |
| 400 | commandError | commandError | 指令错误 |
| 400 | commonParamIllegal | 网关入参非法 | 网关入参非法 |
| 400 | componentIsNull | 表单数据为空 | 表单数据为空 |
| 400 | concurrentError | CONCURRENT\_ERROR | 并发错误 |
| 400 | confClosed | confClosed | 会议已结束 |
| 400 | contain.notAllowed.content | %s | 含有不合适的内容 |
| 400 | contain.notAllowed.content | 含有不合适的内容 | 含有不合适的内容 |
| 400 | contain.notAllowed.picture | %s | 含有不合适的图片 |
| 400 | contain.notAllowed.picture | 含有不合适的图片 | 含有不合适的图片 |
| 400 | contain.notAllowed.text | %s | 含有不合适的文本 |
| 400 | contain.notAllowed.text | 含有不合适的文本 | 含有不合适的文本 |
| 400 | contain.unsafe.url | %s | 含有不安全的外链 |
| 400 | contain.unsafe.url | 含有不安全的外链 | 含有不安全的外链 |
| 400 | contentCheckError | 卡片内容校验失败 | 卡片内容校验失败 |
| 400 | contentNotCompliant | lippi\_live.validate.contentNotCompliant | 内容不合规 |
| 400 | contentSecurityChckFailed | 卡片内容不符合安全规范 | 卡片内容不符合安全规范 |
| 400 | conversation.org.dismatch | 会话不属于当前企业 | 会话不属于当前企业 |
| 400 | conversation.org.notMatch | 会话所属组织信息不匹配 | 请确认token是否有权限操作对于此会话进行操作 |
| 400 | conversationType.illegal | 会话类型值无效 | 会话类型值无效 |
| 400 | convertFail.jsonToBizStructureFail | %s | bizObjectJson转换为表单结构失败 |
| 400 | coolAppCode.empty | 酷应用编码为空 | 酷应用编码为空 |
| 400 | coolAppNotInstalled | 该酷应用未安装到目标会话内 | 该酷应用未安装到目标会话内 |
| 400 | coolAppNotInstalled | 该酷应用未安装到目标群内 | 该酷应用未安装到目标群内 |
| 400 | coolAppPermissionDenied | 无权限，指定的群扩展不属于当前token对应的应用名下 | 无权限，指定的群扩展不属于当前token对应的应用名下 |
| 400 | coolAppPermissionDenied | 无权限，指定的群聊酷应用不属于当前token对应的应用名下 | 无权限，指定的群聊酷应用不属于当前token对应的应用名下 |
| 400 | coolAppUnexist | 群聊酷应用不存在 | 群聊酷应用不存在；群聊酷应用不存在，请检查酷应用编码是否正确 |
| 400 | coolAppUninstalled | 无权限，该群没有安装群聊酷应用 | 无权限，该群没有安装群聊酷应用 |
| 400 | copy.template.error | Template copy error: %s | 复制模板失败 |
| 400 | corp.robot.nonexist | 该组织机器人不存在，请检查 | 该组织机器人不存在，请检查 |
| 400 | corpId.illegal | 所在组织没有对应插件的权限 | 所在组织没有对应插件的权限 |
| 400 | corpNotOpen | 企业未开通指定的码 | 企业未开通指定的码 |
| 400 | corpNotOpenHrm | 企业未开通通智能人事 | 企业未开通通智能人事 |
| 400 | corpNotRealName | 企业未实名 | 企业未实名 |
| 400 | corpNotRealname | 发起人企业在e签宝未实名 | 发起人企业在e签宝未实名 |
| 400 | count.exceeds.limit | count exceeds limit | 数量达到上限 |
| 400 | coupleGroup.memberError | 两人群需要指定两个钉外账号，请检查 | 两人群需要指定两个钉外账号，请检查 |
| 400 | couplegroup.notsupport | 二人群无法修改群信息 | 二人群无法修改群信息 |
| 400 | create.cardInstance.failed | 创建互动卡片实例失败 | 创建互动卡片实例失败 |
| 400 | createFlowError | 创建流程失败: %s | 创建流程失败 |
| 400 | createOrgAccountError | 创建企业账号异常 | 创建企业账号异常 |
| 400 | createUserAccountError | 创建用户账号异常 | 创建用户账号异常 |
| 400 | createUserError | 创建用户账号异常 | 创建用户账号异常 |
| 400 | creatorNotInOrg | 创建人已离职 | 创建人已离职 |
| 400 | creatorUidError | creatorUidError | 创建人错误 |
| 400 | creatorUserId.not.exists | creatorUserId not exists | creatorUserId不是企业员工 |
| 400 | crm.not.installed | crm.not.installed | 客户管理应用未安装。 |
| 400 | crmApp.not.installed | crm app is not installed | CRM应用未安装 |
| 400 | crmAppNotExisted | crmAppNotExisted | 客户管理应用不存在 |
| 400 | customerCountUnderPrincipal.exceeds.limit | customer count under principal exceeds limit | 负责人名下客户数量达到上限 |
| 400 | daily.call.limit | daily call limit | 单日调用数量已达上限，请择日再次调用 |
| 400 | data.format.error | %s | 表单数据格式错误 |
| 400 | data.not.exists | data not exists | 数据不存在 |
| 400 | dataModified.form.batchCreateBizObjectFail | 批量创建流程或业务对象全部失败 | 批量创建流程或业务对象全部失败 |
| 400 | dataModified.form.createBizObjectFail | %s | 创建业务对象失败 |
| 400 | dataModified.form.deleteBizObjectFail | %s | 删除实例失败 |
| 400 | dataModified.form.updateBizObjectFail | %s | 更新业务对象数据失败 |
| 400 | dataNotConsist | 数据不一致 | 数据不一致 |
| 400 | dataNotExist.app.appNotExist | 应用编码不存在 | 应用编码不存在 |
| 400 | dataNotExist.department.departmentNotExist | 部门无效或不存在 | 无效的departmentId参数 |
| 400 | dataNotExist.form.notExists | 表单不存在:%s | 表单不存在 |
| 400 | dataNotExist.form.schemaNotExist | 表单结构不存在 | 无效的schemaCode参数 |
| 400 | dataNotExist.process.instanceNotExist | 流程实例不存在 | 流程实例不存在 |
| 400 | dataNotExist.process.processDefineNotExist | 流程定义不存在 | schemaCode不是流程表单的架构编码 |
| 400 | dataNotExist.role.roleNotExist | 角色无效或不存在 | 无效的roleId参数 |
| 400 | dataNotExist.user.userNotExist | 操作用户不存在 | 操作用户不存在 |
| 400 | dateTooEarly | 时间不能在指定天数之前 | 时间不能在指定天数之前 |
| 400 | decryptOpenconversationIdFailed | 群ID解码失败 | 群ID解码失败 |
| 400 | delete.dir.error | 删除分组失败 | 删除分组失败，可能原因有：分组不存在，请检查入参dirId等。 |
| 400 | dentryAlreadyExist | %s | 同名文件已存在；文件已存在 |
| 400 | dentryAppPropertiesNumberExceedsLimit | %s | dentry上删除单App属性的数量超出限制, 最大数量 3；dentry上单App设置属性的数量超出限制, 最大数量 3 |
| 400 | dentryDownloadProtocolNotSupport | %s | 下载协议不支持 |
| 400 | dentryEditNotSupport | %s | 文件不支持编辑 |
| 400 | dentryExtensionNotSupport | %s | 文件后缀不支持 |
| 400 | dentryFormatNotSupport | %s | 不支持的文件格式；该格式不支持获取缩略图 |
| 400 | dentryNameConflict | %s | 文件名冲突 |
| 400 | dentryNameIllegal | %s | 文件名非法 |
| 400/404 | dentryNotExist | %s | 文件不存在；文件不存在；源文件(夹)或目标目录不存在；父目录不存在 |
| 400 | dentryPreviewNotSupport | %s | 文件不支持预览 |
| 400 | dentryStoreError | %s | 文件存储异常 |
| 400 | dentryUploadError | %s | 文件上传错误 |
| 400 | dentryUploadForbidden | %s | 禁止上传 |
| 400 | dentryUploadProtocolNotSupport | %s | 不支持的上传协议 |
| 400 | departmentAlreadyExist | 部门已存在 | 部门已存在 |
| 400 | departmentNotExist | 部门不存在 | 部门不存在 |
| 400 | departmentTypeError | 部门类型不对 | 部门类型不对 |
| 400 | deptCannotFind | DEPT\_CAN\_NOT\_FIND | 部门不存在 |
| 400 | deptCodeExist | DEPT\_CODE\_EXIST | 组织单元编码已存在 |
| 400 | depth.over.limit | Group Depth Over Limit | 分组深度超限 |
| 400 | deptMoveIllegal | DEPT\_MOVE\_ILLEGAL | 新的父组织单元设定异常 |
| 400 | deptMoveParamIllegal | DEPT\_MOVE\_PARAM\_ILLEGAL | 新的父组织单元参数异常 |
| 400 | deptNameExist | DEPT\_NAME\_EXIST | 组织单元名已存在 |
| 400 | deptNotExist | DEPT\_NOT\_EXIST | 组织单元不存在 |
| 400 | deptTypeInvalid | DEPT\_TYPE\_INVALID | 组织单元类型不合理 |
| 400 | device.not.found | device not found | 设备不存在 |
| 400 | deviceIdError | 30006，设备id异常 | 设备id异常 |
| 400 | devicekeyAlreadyExist | 300001，设备key已经存在 | 设备key已经存在 |
| 400 | devicekeyAlreadyExist | 30001，设备key已存在 | 设备key已存在 |
| 400 | devicekeyAlreadyExist | 设备key已存在 | 设备key已存在 |
| 400 | deviceKeyDuplicate | 设备key重复 | 设备key重复 |
| 400 | devicenameAlreadyExist | 30002，设备名称已存在 | 设备名称已存在 |
| 400 | devicenameAlreadyExist | 设备名称已存在 | 设备名称已存在 |
| 400 | deviceNotExist | 30000，找不到设备 | 找不到设备 |
| 400 | deviceNotExist | 30000，设备不存在 | 设备不存在 |
| 400 | deviceNotExist | 找不到设备 | 找不到设备 |
| 400 | deviceNotExist | 设备不存在 | 设备不存在 |
| 400 | deviceNumLimit | 300002，设备数量达到上限 | 设备数量达到上限 |
| 400 | deviceNumLimit | 30008，设备数量达到上限 | 设备数量达到上限 |
| 400 | deviceNumLimit | 设备数量达到上限 | 设备数量达到上限 |
| 400 | deviceTypeNotExist | 200001，设备类型不存在 | 设备类型不存在 |
| 400 | ding.receivercount.limit | ding receiver count limit | 钉消息接收人超出限制，应用内200，短信电话20 |
| 400 | ding.serverquota.insufficient | ding server quota insufficient | 发送钉消息权益不足，需充值 |
| 400 | dingAdminAuthError | 非钉钉管理员无法操作 | 非钉钉管理员无法操作 |
| 400 | directory.invalid | 规则directory不可用 | 规则directory不可用 |
| 400 | dirName.validation.failed | 目录名称校验失败 | 目录名称校验失败，不能重名，请检查入参。 |
| 400 | doRepeatOrderError | 请勿重复下单 | 请勿重复下单 |
| 400 | doResaleOrderError | 下转售订单失败 | 下转售订单失败 |
| 400 | duplicate.operation | duplicate operation | 重复操作 |
| 400 | duplicate.template.name | Duplicate Template Name | 模板名称重复 |
| 400 | duplicated.field | duplicated field | 存在重复模型字段key |
| 400 | duplicateKey | 卡片模板占位符有重复Key | 卡片模板占位符有重复Key |
| 400 | duplicateOperation | 重复操作 | 重复操作 |
| 400 | durationTooLong | 开始结束时间跨度过大 | 开始结束时间跨度过大 |
| 400 | emp.not.exist | 员工不存在 | 员工不存在 |
| 400 | employee.not.exist | 员工不存在 | 员工不存在 |
| 400 | employee.not.found | userId错误 | userId错误 |
| 400 | empNotDismission | 员工当前非离职状态 | 员工当前非离职状态 |
| 400 | empNotExists | 员工不存在 | 员工不存在 |
| 400 | empNotFound | 员工不存在 | 员工不存在 |
| 400 | empStatusError | 员工离职状态出错，请联系钉钉智能人事 | 员工离职状态出错，请联系钉钉智能人事 |
| 400 | emptyUserId | 用户ID为空 | 用户ID为空 |
| 400 | esignOpenPlatformCreateAppFail | E签宝开放平台开发者账号创建失败 | E签宝开放平台开发者账号创建失败 |
| 400 | exceedMaxReceiverSize | 日程人数超过上限 | 日程人数超过上限 |
| 400 | exceedSubscribeLimit | exceed subscribe limit | 订阅日历超过上限 |
| 400 | excludeNodeExceed | excludeUserIds、excludeDeptIds、excludeTagIds三个数组元素之和不能超过50 | excludeUserIds、excludeDeptIds、excludeTagIds三个数组元素之和不能超过50 |
| 400 | exclusive.account.limit | 只能操作归属该组织的专属账号 | 只能操作归属该组织的专属账号 |
| 400 | exclusive.account.only | 只能操作归属该组织的专属账号 | 只能操作归属该组织的专属账号 |
| 400 | executor.error | 执行错误 | 取数执行错误 |
| 400 | expiredPayCode | 码已过期 | 码已过期 |
| 400 | expiredTimeInvalid | 过期时间非法 | 过期时间非法 |
| 400 | extensionAppSettingError | extensionAppSettingCountError | 扩展应用设置数量错误 |
| 400 | failure.address.addressDoesNotExist | 请求地址不存在:%s | 请求地址不存在 |
| 400 | failure.batchOperation.batchDeletingSequenceIsPerforming | 当前表单有正在删除的批次，请等待完成后再重试:%s | 当前表单有正在删除的批次，请等待完成后再重试 |
| 400 | failure.batchOperation.batchUpdatingRuleNeedConditionComponent | 批量更新规则中未指定条件组件:%s | 批量更新规则中未指定条件组件 |
| 400 | failure.batchOperation.canNotFindImportSequence | 找不到导入序列记录:%s | 找不到导入序列记录 |
| 400 | failure.batchOperation.currentFormIsExecutingBatchDeleting | 当前表单正在执行批量删除操作，请稍后再试:%s | 当前表单正在执行批量删除操作，请稍后再试 |
| 400 | failure.batchOperation.dataAmountToStartProcessExceed | 批量发起流程的数据过多:%s | 批量发起流程的数据过多 |
| 400 | failure.batchOperation.excelDataIsEmpty | 批量发起的excel数据为空:%s | 批量发起的excel数据为空 |
| 400 | failure.batchOperation.noUpdatingComponentInBatchUpdatingRule | 批量更新规则中未指定更新组件:%s | 批量更新规则中未指定更新组件 |
| 400 | failure.batchOperation.sameComponentInConditionAndUpdateTarget | 同一个组件不能同时作为条件和更新值:%s | 同一个组件不能同时作为条件和更新值 |
| 400 | failure.connector.operateFailed | 操作失败:%s | 操作失败 |
| 400 | failure.data.failedToConstructData | 数据构建失败:%s | 数据构建失败 |
| 400 | failure.encrypt.encryptError | 加密失败:%s | 加密失败 |
| 400 | failure.expression.expressionEvaluateFail | 公式执行失败:%s | 公式执行失败 |
| 400 | failure.form.canNotPaasSubmissionRulesCheck | 不满足提交规则:%s | 不满足提交规则 |
| 400 | failure.form.dataAmountExceedFiveThousand | 数据量过大，不能超过5000条:%s | 数据量过大，不能超过5000条 |
| 400 | failure.form.instanceAssociationComponentNotSupportReceiptData | 单据数据不支持实例关联:%s | 单据数据不支持实例关联 |
| 400 | failure.form.pageChanged | 页面已变更，请更新后再修改并重新保存:%s | 页面已变更，请更新后再修改并重新保存 |
| 400 | failure.masterData.invokeMasterDataFailed | 主数据调用异常:%s | 主数据调用异常 |
| 400 | failure.message.dingTalkMessageError | 钉消息参数或返回结果处理异常:%s | 钉消息参数或返回结果处理异常 |
| 400 | failure.message.failedToSendMessage | 消息发送失败:%s | 消息发送失败 |
| 400 | failure.message.sendYidaInnerMessageError | 宜搭内部消息发送失败:%s | 宜搭内部消息发送失败 |
| 400 | failure.openSearch.preciseSearchNonsupportMultipleDistinctKey | 精确搜索不支持多个distinct字段:%s | 精确搜索不支持多个distinct字段 |
| 400 | failure.operation.appCopyFail | 应用复制失败:%s | 应用复制失败 |
| 400 | failure.operation.applicationContainsCrossApplicationDataSource | 操作异常，应用下包含跨应用数据源:%s | 操作异常，应用下包含跨应用数据源 |
| 400 | failure.operation.applicationKeyIsSensitiveInformation | 应用密钥为敏感信息, 请联系应用主管理员获取:%s | 应用密钥为敏感信息, 请联系应用主管理员获取；应用密钥为敏感信息， 请联系应用主管理员获取 |
| 400 | failure.operation.applicationKeyIsSensitiveInformation | 应用密钥为敏感信息, 请联系应用主管理员获取:%s | 应用密钥为敏感信息, 请联系应用主管理员获取；应用密钥为敏感信息， 请联系应用主管理员获取 |
| 400 | failure.operation.applicationNameNotCorrect | 应用名称不匹配，无法删除:%s | 应用名称不匹配，无法删除 |
| 400 | failure.operation.backAppNotAllowedToCreate | 轻应用不能创建:%s | 轻应用不能创建 |
| 400 | failure.operation.canNotModify | 封网期间，不允许执行该操作:%s | 封网期间，不允许执行该操作 |
| 400 | failure.operation.currentEditionCanOnlyCreateApp | 当前版本能创建的应用个数已达您企业内应用数量上限:%s | 当前版本能创建的应用个数已达您企业内应用数量上限 |
| 400 | failure.operation.dataAmountToBeClearExceedThreeHundred | 表单数据最多清空300条:%s | 表单数据最多清空300条 |
| 400 | failure.operation.environmentDoesNotSupport | 所在环境不支持当前操作:%s | 所在环境不支持当前操作 |
| 400 | failure.operation.exceptionOccurredInSearch | 搜索异常，请检查查询参数，有问题请通过宜搭官网首页右下角帮助链接联系我们:%s | 搜索异常，请检查查询参数，有问题请通过宜搭官网首页右下角帮助链接联系我们 |
| 400 | failure.operation.exceptionOccurredInSearch | 搜索异常，请检查查询参数，有问题请通过页面右下的vone联系我们:%s | 搜索异常，请检查查询参数，有问题请通过页面右下的vone联系我们 |
| 400 | failure.operation.failedToChangeEncryptionConfiguration | 表单下已存在数据，不允许变更加密配置:%s | 表单下已存在数据，不允许变更加密配置 |
| 400 | failure.operation.failedToRegister | 注册失败:%s | 注册失败 |
| 400 | failure.operation.failedToSearchEmployeeFieldValues | searchEmployeeFieldValues查不到人:%s | searchEmployeeFieldValues查不到人 |
| 400 | failure.operation.failedToSearchEmployeeFieldValues | 查不到人:%s | 查不到人 |
| 400 | failure.operation.failToSearchApp | 应用查询失败，请联系管理员:%s | 应用查询失败，请联系管理员 |
| 400 | failure.operation.fatalSystemError | 系统异常，请联系企业管理员:%s | 系统异常，请联系企业管理员 |
| 400 | failure.operation.fileSizeTooBig | 附件预览暂不支持大小超过20M的文件，请下载后查看:%s | 附件预览暂不支持大小超过20M的文件，请下载后查看 |
| 400 | failure.operation.forbidToDeleteEnabledProcess | 已启用的流程不允许删除:%s | 已启用的流程不允许删除 |
| 400 | failure.operation.forbidToReinitializeMappingRelationships | 固定的映射关系不允许重新初始化:%s | 固定的映射关系不允许重新初始化 |
| 400 | failure.operation.formDesignHistoryCanNotBeFound | 表单历史查询不到:%s | 表单历史查询不到 |
| 400 | failure.operation.incorrectMessageState | 消息状态异常下执行操作:%s | 消息状态异常下执行操作 |
| 400 | failure.operation.lightSystemError | 系统异常，请通过宜搭官网首页右下角帮助链接联系我们:%s | 系统异常，请通过宜搭官网首页右下角帮助链接联系我们 |
| 400 | failure.operation.lightSystemError | 系统异常，请通过页面右下的vone联系我们:%s | 系统异常，请通过页面右下的vone联系我们 |
| 400 | failure.operation.logicServiceFail | 调用逻辑编排服务处理失败:%s | 调用逻辑编排服务处理失败 |
| 400 | failure.operation.logicServiceInvokeFail | 调用逻辑编排服务失败:%s | 调用逻辑编排服务失败 |
| 400 | failure.operation.numberOfQueryDataExceed | 单次查询超过条数限制:%s | 单次查询超过条数限制 |
| 400 | failure.operation.onlyReceiptDataCanBeCleared | 只有单据表单才允许清空数据:%s | 只有单据表单才允许清空数据 |
| 400 | failure.operation.onlyReceiptDataCanBeDeletedInBatches | 只能批量删除单据数据:%s | 只能批量删除单据数据 |
| 400 | failure.operation.onlyTemplateAppCanBeCopied | 只能复制模板应用:%s | 只能复制模板应用 |
| 400 | failure.operation.operatingFrequencyTooFast | 操作频率过快，请稍后重试:%s | 操作频率过快，请稍后重试 |
| 400 | failure.operation.operationDeniedDuringThePublishPeriod | 表单发布中，不能进行其他操作:%s | 表单发布中，不能进行其他操作 |
| 400 | failure.operation.operationDeniedDuringTheRollbackPeriod | 数据回滚进行中，不能进行其他操作:%s | 数据回滚进行中，不能进行其他操作 |
| 400 | failure.operation.processFormCanNotSaveReceiptFormData | 流程表单不能保存单据数据:%s | 流程表单不能保存单据数据 |
| 400 | failure.operation.processingImportSequenceCanNotBeDeleted | 处理中的批次不允许删除:%s | 处理中的批次不允许删除 |
| 400 | failure.operation.processIsBeingRepaired | 正在修复流程，无需重复操作:%s | 正在修复流程，无需重复操作 |
| 400 | failure.operation.receiptFormCanNotStartInstance | 单据表单不能发起流程:%s | 单据表单不能发起流程 |
| 400 | failure.operation.registerError | 注册失败:%s | 注册失败 |
| 400 | failure.operation.registrationPasswordDoesNotMatchRules | 注册密码不符合规则:%s | 注册密码不符合规则 |
| 400 | failure.operation.requestTooFast | 请求过于频繁,请稍后重试:%s | 请求过于频繁,请稍后重试；请求过于频繁，请稍后重试 |
| 400 | failure.operation.saasApplicationNotFound | 无法找到应用，请核对应用信息:%s | 无法找到应用，请核对应用信息 |
| 400 | failure.operation.snapshotForAppPublishIsNotAllowedToDelete | 发布版本快照不允许删除:%s | 发布版本快照不允许删除 |
| 400 | failure.operation.theSubmissionRecordExceed | 提交记录已超额, 请在钉钉购买后继续提交:%s | 提交记录已超额, 请在钉钉购买后继续提交；提交记录已超额， 请在钉钉购买后继续提交 |
| 400/500 | failure.operation.tooManyVisitors | 平台当前访问人数过多，请稍后重试:%s | 平台当前访问人数过多，请稍后重试 |
| 400 | failure.operation.uploadAttachmentCapacityExceed | 上传附件容量超额, 请在钉钉购买后继续上传:%s | 上传附件容量超额, 请在钉钉购买后继续上传；上传附件容量超额， 请在钉钉购买后继续上传 |
| 400 | failure.operation.uploadFileFail | 文件上传失败:%s | 文件上传失败 |
| 400 | failure.operation.warn | 提醒:%s | 提醒 |
| 400 | failure.process.canOnlyRetryTheAbnormalProcess | 您只能对异常的流程进行重试:%s | 您只能对异常的流程进行重试 |
| 400 | failure.process.failedToCreateProcess | 创建流程失败:%s | 创建流程失败 |
| 400 | failure.process.failureOfProcessRetry | 流程重试失败:%s | 流程重试失败 |
| 400 | failure.process.oneTaskPermitOneBackAppend | 相同任务只能进行一次后加签:%s | 相同任务只能进行一次后加签 |
| 400 | failure.process.redirectProcessFailure | 流程实例跳转失败:%s | 流程实例跳转失败 |
| 400 | failure.resource.dataTypeAccessAmountReachLimit | 数据类型接入数量已满:%s | 数据类型接入数量已满 |
| 400 | failure.service.failedToInvokeFileService | 调用文件服务失败:%s | 调用文件服务失败 |
| 400 | failure.service.failedToInvokeHsf | 调用宜搭HSF接口失败:%s | 调用宜搭HSF接口失败 |
| 400 | failure.serviceCallBack.failedToExecuteService | 执行回调服务失败:%s | 执行回调服务失败 |
| 400 | failure.serviceCallBack.failedToInvokeService | 执行回调服务失败:%s | 执行回调服务失败 |
| 400 | failure.spi.spiLoadError | 系统SPI加载异常:%s | 系统SPI加载异常 |
| 400 | failure.task.failedToPerformApproval | 任务审批失败:%s | 任务审批失败 |
| 400/500 | failure.user.userNotExist | 用户不存在:%s | 用户不存在 |
| 400 | feedNotExist | feedNotExist | 课程不存在 |
| 400 | fieldId.not.exists | %s | 关系表结构字段缺失；联系人表结构字段缺失 |
| 400 | fieldIsNotSelect | 字段不是选项型 | 字段不是选项型 |
| 400 | fieldOptionsCannotModify | 字段选项不可修改 | 字段选项不可修改 |
| 400 | fieldTooMuch.field.exceed | 字段超过最大允许数量:%s | 字段超过最大允许数量 |
| 400 | fileArchived | %s | 文件处于归档状态, 会自动触发解归档, 请稍后重试 |
| 400 | fileMalicious | %s | 恶意文件 |
| 400 | filename.invalid | File name error. | 文件名非法 |
| 400 | fileType.unsupported | File type is not supported. | 该类型文件不支持下载 |
| 400 | fileViral | %s | 病毒文件 |
| 400 | flowLimit | current user can not create events exceed 100 per day | 每个用户每天限制创建100个日程 |
| 400 | flowNotExists | 流程信息不存在 | 流程信息不存在 |
| 400 | folder.exist | Folder already exist. | 目录已存在 |
| 400 | folder.exists | Folder exists | 目录已存在 |
| 400 | folderNotSupport | %s | 不支持发送文件夹 |
| 400 | forbid.add.rule | 当前企业可见性规则数量超限，禁止新增规则 | 禁止新增规则 |
| 400 | forecastError | 流程预测失败 | 流程预测失败 |
| 400 | formCode.error | formCode query error | 模板编码查询错误 |
| 400 | formCode.notExists | formCode not exists | formCode不存在 |
| 400 | formContent.error | 表单格式错误 | 表单格式错误 |
| 400 | formConverterError | 表单数据反向转换出错 | 表单数据反向转换出错 |
| 400 | formConverterError | 表单数据校验失败，失败控件：%s | 表单数据校验失败 |
| 400 | formName.error | 已有相同名称表单 | 表单名称错误 |
| 400 | formNotExist | 审批表单模板不存在 | 审批表单模板不存在 |
| 400 | formNotExist | 表单不存在 | 表单不存在 |
| 400 | formschema.error | %s | 表单schema不合法 |
| 400 | formschema.error | 流程条件分支中已使用的表单控件不可修改或删除 | 流程条件分支中使用的表单控件的类型不可修改或删除 |
| 400 | function.not.open | 企业未开通相应功能 | 企业未开通相应功能 |
| 400 | general.enumError | 入参枚举有误，请检查 | 入参枚举有误，请检查 |
| 400 | general.parameterError | 输入参数有误，请检查是否同时传了会话id和接收者id或都没传 | 输入参数有误，请检查是否同时传了会话id和接收者id或都没传 |
| 400 | general.parameterError | 输入参数有误，请检查是否缺少必要参数或内容不正确 | 输入参数有误，请检查是否缺少必要参数或内容不正确 |
| 400 | general.parameterError | 输入参数有误，请检查是否超出最大值或传参规则不正确 | 输入参数有误，请检查是否超出最大值或传参规则不正确 |
| 400 | general.signatureError | 参数签名失败，请检查 | 参数签名失败，请检查 |
| 400 | getCorpMarginError | 获取企业套餐余量异常 | 获取企业套餐余量异常 |
| 400 | getFileInfoError | 获取文件信息失败: %s | 获取文件信息失败 |
| 400 | getFileUploadUrlError | 获取文件上传地址异常 | 获取文件上传地址异常 |
| 400 | getFlowInfoError | 查询流程信息异常 | 查询流程信息异常 |
| 400 | getFlowInfoError | 获取流程信息失败 | 获取流程信息失败 |
| 400 | getInstFieldSettingError | 获取流程表单控件可见性失败 | 请记录异常日志，稍后再试 |
| 400 | getOpenAuthCorpError | 获取授权用户信息异常 | 获取授权用户信息异常 |
| 400 | getOpenIsvInfoError | 查询服务商信息异常 | 查询服务商信息异常 |
| 400 | getOpenIsvInfoError | 获取对接服务商信息异常 | 获取对接服务商信息异常 |
| 400 | getPictureFailed | 获取图片url失败 | 获取图片url失败 |
| 400 | getResaleOrderInfoError | 获取转售订单信息异常 | 获取转售订单信息异常 |
| 400 | getSignUrlError | 获取签署链接失败: %s | 获取签署链接失败 |
| 400 | getUserInfoError | 获取用户信息异常 | 获取用户信息异常 |
| 400 | getUserInfoFail | 获取用户信息失败,%s，%s | 获取用户信息失败 |
| 400 | goods.not.app | 非应用或内购商品 | 非应用或内购商品 |
| 400 | goodsItemNotExist | 商品规格不存在 | 商品规格不存在 |
| 400 | goodsNotExist | 内购商品不存在 | 内购商品不存在 |
| 400 | grayControlDenied | 接口灰度中暂时无法使用 | 接口灰度中暂时无法使用 |
| 400 | group.creating | 群会话仍在创建中，请稍后重试 | 群会话仍在创建中，请稍后重试 |
| 400 | group.diaband | 群已经解散 | 群已经解散 |
| 400 | group.disbanded | 群已经解散 | 群已经解散 |
| 400 | group.groupTemplate.notInstalled | 群模板未安装到群内 | 群模板未安装到群内 |
| 400 | group.memberIllegal | 两人群人数有误，请确保人数有且只有两人 | 两人群人数有误，请确保人数有且只有两人 |
| 400 | group.memberParamIllegal | 群成员参数设置有误，请检查 | 群成员参数设置有误，请检查 |
| 400 | group.nameIllegal | 群名称中包含不合规内容，请检查 | 群名称中包含不合规内容，请检查 |
| 400 | group.nonexist | 群不存在，请检查 | 群不存在，请检查 |
| 400 | group.not.found | Group Not Found | 分组不存在 |
| 400 | group.not.found | Parent Group Not Found | 父分组找不到 |
| 400 | group.notReady | 群会话仍在创建中，请稍后重试 | 群会话仍在创建中，请稍后重试 |
| 400 | group.num.overlimit | 查询群个群超出阈值，请检查 | 查询群个群超出阈值，请检查 |
| 400 | group.org.checkFailed | 无权限，群不属于当前企业 | 无权限，群不属于当前企业 |
| 400 | group.org.checkFailed | 群不属于当前企业 | 群不属于当前企业 |
| 400 | group.qrcode.nonexist | 群会话不存在，请检查 | 群会话不存在，请检查 |
| 400 | group.too.much | Group Too Much | 分组数量超出错误 |
| 400 | groupDisbang | 群已经解散 | 群已经解散 |
| 400 | groupNickForbid | 昵称内容非法 | 昵称内容非法 |
| 400 | groupNotExist | 200002，分组不存在 | 分组不存在 |
| 400 | groupPermissionDenied | 无权限 | 无权限,该群不是内部群，或者未安装群模板，或者未安装入参指定的群聊酷应用，或者入参指定的群聊酷应用不属于当前token所属应用名下 |
| 400 | groupPermissionDenied | 无权限访问此群数据 | 无权限访问此群数据 |
| 400 | groupPermissionDenied | 无权限，该群没有安装群模板 | 无权限，该群没有安装群模板 |
| 400 | groupQRCodeExpired | 对不起，由于群二维码配置失效，您的本次请求失败，请联系功能提供方 | 对不起，由于群二维码配置失效，您的本次请求失败，请联系功能提供方 |
| 400 | groupRelationSchemaNotExist | 群关系模板不存在 | 群关系模板不存在 |
| 400 | groupTemplatePermissionDenied | 无权限，该群安装的群模板不属于当前token对应的应用名下 | 无权限，该群安装的群模板不属于当前token对应的应用名下 |
| 400 | have.been.set | 你已经设置过钉钉号，无法修改 | 你已经设置过钉钉号，无法修改 |
| 400 | hidden.org.only | 必须以隐藏组织身份来调用接口 | 必须以隐藏组织身份来调用接口 |
| 400 | hsfIntegrationErrorCspace | 钉盘附件依赖三方错误 | 钉盘附件依赖三方错误 |
| 400 | hsfIntegrationErrorCspaceDentryServiceGenerateDownloadPresignedUrl | 产生文件下载的链接失败 | 产生文件下载的链接失败 |
| 400 | hsfIntegrationErrorCspaceDentryServiceGrant | 授权访问钉盘失败 | 授权访问钉盘失败 |
| 400 | hsfIntegrationErrorCspaceDentryServiceInfo | 查看具体文件信息失败 | 查看具体文件信息失败 |
| 400 | hsfIntegrationErrorCspaceGetCustomSpace | 获取钉盘space的信息失败 | 获取钉盘space的信息失败 |
| 400 | hsfIntegrationErrorCspaceGetSimpleMicroAppByRelatedAppId | 根据relatedAppId查询获取微应用信息失败 | 根据relatedAppId查询获取微应用信息失败 |
| 400 | idempotencyProcessing | Idempotency processing | 幂等请求处理中 |
| 400 | IdempotentParameterMismatch | The request uses the same client token as a previous, but non-identical request. Do not reuse a client token with different requests, unless the requests are identical. | client token不合法。 |
| 400 | idempotentParameterMismatch.uuid | illegal parameter %s | UUID 不存在 |
| 400 | idempotentParameterMismatch.uuid | uuid not found. | uuid参数非法。 |
| 400 | idInvalid | id对应的设置不存在 | id对应的设置不存在 |
| 400 | idInvalid | id对应的配置不存在 | id对应的配置不存在 |
| 400 | illegal.excludes | %s | 不接收者名单不合法 |
| 400 | illegal.excludes | 不接收者名单不合法 | 不接收者名单不合法 |
| 400 | illegal.migration.unionId | 非法的migrationUnionId | 非法的migrationUnionId |
| 400 | illegal.openconevrsation.id | %s | 无效的会话id |
| 400 | illegal.order.principle | 订单归属错误 | 非当前ISV所属订单无查询权限 |
| 400 | illegal.param | %s | 参数错误 |
| 400 | illegal.parameter | 参数错误 | 参数错误；参数错误，请检查入参。 |
| 400 | illegal.parameter | 非法参数 | 非法参数 |
| 400 | illegal.parameter.cid | openConverationId参数错误 | 参数漏填或者格式错误 |
| 400 | illegal.parameter.type | banWordsType参数错误 | 参数漏填或者格式错误 |
| 400 | illegal.receivers | %s | 接收者名单不合法 |
| 400 | illegal.receivers | 接收者名单不合法 | 接收者名单不合法 |
| 400 | illegalAlipayCode | 非法的支付宝码值 | 非法的支付宝码值 |
| 400 | illegalAppDesc | 应用描述含有不规范词语 | 应用描述含有不规范词语 |
| 400 | illegalAppIcon | 应用图标含有不规范词语 | 应用图标含有不规范词语 |
| 400 | illegalAppName | 应用名称含有不规范词语 | 应用名称含有不规范词语 |
| 400 | illegalApproveType | 不合法的审批类型 | 不合法的审批类型 |
| 400 | illegalArgument | 非法参数 %s | 非法参数 |
| 400 | illegalCalculateType | 不合法的时长计算模式 | 不合法的时长计算模式 |
| 400 | illegalComponent | 表单组件入参错误 | 表单组件入参错误 |
| 400 | illegalDateTypeForHalfDay | 不合法的开始结束时间格式forDURATION\_UNIT为半天 | 不合法的开始结束时间格式forDURATION\_UNIT为半天 |
| 400 | illegalDurationUnit | 不合法的时长单位 | 不合法的时长单位 |
| 400 | illegalIp | ip不合法 | ip不合法，可能是单个ip不合法，也可能是ip总长度超过了50 |
| 400 | illegalMobile | ILLEGAL\_MOBILE | 无效的手机号 |
| 400 | illegalOrg | ILLEGAL ORG | 未被组织授权 |
| 400 | illegalOrg | ILLEGAL\_ORG | 违法组织，不能使用 |
| 400 | illegalOvertimeDurationUnit | 不合法的加班时长单位（加班仅支持按小时） | 不合法的加班时长单位（加班仅支持按小时） |
| 400 | illegalPama | 参数非法 | 参数非法 |
| 400 | illegalParam | 参数错误 | 员工id或者最后工作日错误 |
| 400 | illegalParameter | Illegal parameter | 参数错误；请求参数不正确 |
| 400 | illegalParameter | illegal\_parameter | 必选参数错误 |
| 400 | illegalParameter | 参数错误：缺少必传参数 | 参数错误：缺少必传参数 |
| 400 | illegalParameter | 参数非法 | 参数非法，openTeamId不正确 |
| 400 | illegalParameter.account | illegal account | 服务窗账号不存在；服务窗账号异常。 |
| 400 | illegalParameter.accountOrg | illegal account org | 服务窗账号不存在 |
| 400 | illegalParameter.bindingClient | illegal binding client | 第三方应用与服务窗绑定关系不正确 |
| 400 | illegalParameter.bindingToken | illegal binding token | bindingToken参数不正确。 |
| 400 | illegalParameter.groupName | 参数错误：群名称 | 参数错误：群名称 |
| 400 | illegalParameter.maxResults | illegal maxResults. | maxResults参数不正确。 |
| 400 | illegalParameter.messageBody | illegal message body | 消息体不正确；消息体不合法。 |
| 400 | illegalParameter.messageContent | illegal message content | 消息内容不正确；消息内容不合法。 |
| 400 | illegalParameter.messageReceiver | illegal message receiver | 消息接收人不正确；消息接收人不正确。 |
| 400 | illegalParameter.messageType | illegal message type | 消息类型不正确；消息类型不合法。 |
| 400 | illegalParameter.nextToken | illegal nextToken. | nextToken不正确。 |
| 400 | illegalParameter.ownerUserId | 参数错误：群主id | 参数错误：群主id |
| 400 | illegalParameter.relationType | 参数错误：relationType非法 | 参数错误：relationType非法 |
| 400 | illegalParameter.unionId | illegal union id. | unionId不正确。 |
| 400 | illegalParameter.userId | illegal user id. | userId参数不正确。 |
| 400 | illegalParameter.uuid | illegal uuid | UUID 不合法；uuid参数非法。 |
| 400 | illegalRequest | illegal request | 请求异常。 |
| 400 | illegalRequest.account | illegal account. | 服务窗账号不正确。 |
| 400 | illegalRequest.followerNotExist | follower not existed. | 根据传入的unionId或userId未未询到对应的关注人信息。 |
| 400 | illegalRequest.overQuota | request over quota. | 请求超过配额。 |
| 400 | image.url.error | 上传图片失败，请检查图片url是否可用或者图片大小超过1M | 上传图片失败，请检查图片url是否可用或者图片大小超过1M |
| 400 | image.urlError | 上传图片失败，请检查图片url是否可用或者图片大小超过1M | 上传图片失败，请检查图片url是否可用或者图片大小超过1M |
| 400 | image.urlError | 上传群头像失败，请检查图片url是否可用或者图片大小超过1M | 上传群头像失败，请检查图片url是否可用或者图片大小超过1M |
| 400 | incorrect.format | 钉钉号格式不正确，请重新输入 | 钉钉号格式不正确，请重新输入 |
| 400 | incorrect.length | 钉钉号格式不正确，请重新输入 | 钉钉号格式不正确，请重新输入 |
| 400 | incorrect.reserved | 该钉钉号已被占用，请重新输入 | 该钉钉号已被占用，请重新输入 |
| 400 | incorrectOpenConversationId | %s | openConversionId不存在 |
| 400 | indicator.not.found | 当前指标不存在 | 当前指标不存在 |
| 400 | inProcessOfApproval | 已在转正审批流程中 | 已在转正审批流程中 |
| 400 | inputParams.accountId.empty | accountId不能为空 | accountId不能为空 |
| 400 | inputParams.agrs.empty | args不能为空 | args不能为空 |
| 400 | inputParams.corpId.empty | corpId不能为空 | corpId不能为空 |
| 400 | inputParams.date.invalid | startDate或endDate日期格式不正确,正确日期格式:20220801 | startDate或endDate日期格式不正确,正确日期格式:20220801 |
| 400 | inputParams.deptId.empty | 入参：deptId不能为空 | 入参：deptId不能为空 |
| 400 | inputParams.serviceId.empty | apiId不能为空 | apiId不能为空 |
| 400 | inputParams.staffId.empty | userId不能为空 | userId不能为空 |
| 400 | inputParams.startGraterEnd.date | 开始日期不能大于结束日期 | 开始日期不能大于结束日期 |
| 400 | inputParams.startOrEndDate.empty | startDate和endDate不能为空 | startDate和endDate不能为空 |
| 400 | inputParamsDate.over.timeScope | 查询时间超过最大时间范围 | 查询时间超过最大时间范围 |
| 400 | insert.repeat.error | 重复插入 | 重复插入 |
| 400 | insertOrUpdate.dir.error | 创建/更新分组失败 | 创建/更新分组失败，可能原因为分组数量达到上限等。 |
| 400 | instance.error | 发起审批实例失败 | 发起审批实例失败 |
| 400 | instance.query.error | %s | 表单实例查询失败 |
| 400 | instance.status.error | 当前流程实例状态不是运行中不支持加签操作 | 请检查processInstanceId参数，当前审批单状态是否为RUNNING |
| 400 | instance.status.error | 当前流程实例状态不是运行中不支持转交操作 | 当前流程实例状态不是运行中不支持转交操作 |
| 400 | instance.status.error | 当前流程实例状态不是运行中不支持退回操作 | 请检查processInstanceId参数，当前审批单状态是否为RUNNING |
| 400 | insufficient.capacity | Insufficient capacity | 剩余空间不足 |
| 400 | insufficient.capacity | The free capacity of the space is insufficient | 空间剩余容量不足 |
| 400 | integrated.concurrency.error | 不支持并发创建任务和实例，请稍后再试 | 不支持并发创建任务和实例，请稍后再试 |
| 400 | integrated.number.exceed | 流程任务的数量到达上限 | 流程任务的数量到达上限 |
| 400 | integrated.params.error | 参数非法，请检查分页参数跟起始时间 | 参数非法，请检查分页参数跟起始时间 |
| 400 | integrated.params.error | 用户ID不能为空，请检查 | 用户ID不能为空，请检查 |
| 400 | integrated.permission.error | 无操作审批流的权限，请检查审批实例或者模板是否正确 | 无操作审批流的权限，请检查审批实例或者模板是否正确 |
| 400 | integrated.permission.error | 无操作审批流的权限，请检查审批实例或者模板是否正确 | 无操作审批流的权限，请检查审批实例或者模板是否正确 |
| 400 | integrated.permission.error | 非流程中心集成审批流，无权操作 | 非流程中心集成审批流，无权操作 |
| 400 | integrated.qps.exceed | 本接口调用次数超过今日上限，请明日再试 | 本接口调用次数超过今日上限，请明日再试 |
| 400 | integrated.state.invalid | 参数错误，请检查流程实例ID是否正确 | 参数错误，请检查流程实例ID是否正确 |
| 400 | integrated.state.invalid | 流程实例不存在 | 流程实例不存在 |
| 400 | integrated.state.invalid | 流程实例已完结，不能继续创建任务 | 流程实例已完结，不能继续创建任务 |
| 400 | internalenterpriseaccount.limit | 仅限处理归属本企业的企业账号 | 仅限处理归属本企业的企业账号 |
| 400/500 | internalError | %s | 系统内部异常；系统内部异常，具体可能为：仅支持对已完成的审批单操作归档、不能重复操作归档等；系统内部异常，具体可能为：管理后台未设置允许提交人撤销审批中的审批单，导致您没有任务处理的权限；系统内部错误；系统内部异常 |
| 400 | invaild.parameter | invaildParameter | 参数非法 |
| 400 | invalid.appid | Invalid appId | 入参需要提供应用id字段，且应用id需要和当前token相匹配。 |
| 400 | invalid.authority | 参数userId有误 | 参数userId有误 |
| 400 | invalid.authority | 没有操作企业数据权限 | 没有操作企业数据权限 |
| 400 | invalid.bizId | 互动卡片BIZID无效 | 互动卡片BIZID无效 |
| 400 | invalid.chatbotId | invalid.chatbotId %s | 无效的机器人id |
| 400 | invalid.client | invalid.client | 无效的ClientID或ClientSecret |
| 400 | invalid.content | %s | 内容存在违禁词 |
| 400 | invalid.content | card streaming key invalid | 消息体内容不合法，流式组件的 Key 不合法。 |
| 400 | invalid.content | card template not exist | 消息体内容不合法，卡片模板不存在。 |
| 400 | invalid.content | emplateId cannot be null or empty | 消息体内容不合法，卡片模板不能为空。 |
| 400 | invalid.content | invalid componentTag | 消息体内容不合法，卡片组件类型不合法。 |
| 400 | invalid.content | templateId cannot be null or empty | 消息体内容不合法，卡片模板不能为空。 |
| 400 | invalid.content | templateId in content is not equal to templateId in context | 消息体内容不合法，卡片模板需要全流程一致。 |
| 400 | invalid.content.type | invalid content type | 消息体类型不合法。 |
| 400 | invalid.conversation.token | invalid conversation token | 不合法的会话凭证。 |
| 400 | invalid.data.action | Invalid data action | 无效的数据操作行为，只支持add、update和delete。 |
| 400 | invalid.media.id | media\_id非法 | media\_id非法 |
| 400 | invalid.objectType | invalid objectType | 不存在的objectType |
| 400 | invalid.openConversationId | %s | 无效的openConversationId，请检查openConversationId是否正确 |
| 400 | invalid.openConversationId | 无效的openConversationId | 无效的openConversationId |
| 400 | invalid.param | ai assistant not found | 无法找到 AI 助理。请使用 AI 助理的 ClientID/ClientSecret 获取访问凭证。 |
| 400 | invalid.param | invalid openConversationId | 会话 ID 不合法。 |
| 400 | invalid.param | invalid unionId | 用户 ID 不合法。 |
| 400 | invalid.param | 不合法的dingId | 不合法的dingId |
| 400 | invalid.param | 不合法的migrationDingId | 不合法的migrationDingId |
| 400 | invalid.param | 入参不能为空 | 入参不能为空 |
| 400 | invalid.param | 参数无效 | 无效参数 |
| 400 | invalid.param | 审批单已完成 | 审批单已完成 |
| 400 | invalid.param | 找不到超标审批单 | 找不到超标审批单 |
| 400 | invalid.param | 无效参数 | sourceUserId/targetUserId/effectCorpId不能为空，并且effectCorpId需要是真实存在的组织id；userId不能为空；无效参数 |
| 400 | invalid.param.actionCardTobtnOrientation | %s | 消息内容不合法，错误的actionCard-btnOrientation |
| 400 | invalid.param.actionCardTobtnOrientation | 错误的actionCard-btnOrientation | 错误的actionCard-btnOrientation |
| 400 | invalid.param.actionCardTocanForward | %s | 消息内容不合法，错误的actionCard-canForward |
| 400 | invalid.param.actionCardTocanForward | 错误的actionCard-canForward | 错误的actionCard-canForward |
| 400 | invalid.param.userId | 参数userId有误 | 参数userId有误 |
| 400 | invalid.parameter | invalidParameter | 参数非法 |
| 400 | invalid.parameter | parameter invalid | 参数错误 |
| 400 | invalid.parameter | 参数错误 | 参数错误 |
| 400/500 | invalid.parameter | 非法参数 | 非法参数 |
| 400 | invalid.processQueryKey | %s | 无效的processQueryKey，请检查processQueryKey是否正确 |
| 400 | invalid.processQueryKey | 无效的processQueryKey | 无效的processQueryKey |
| 400 | invalid.relationId | invalid parameter: relationId | relationId不存在 |
| 400 | invalid.relationType | invalid parameter: relationType | relationType不存在 |
| 400 | invalid.robotCode | 无效的robotCode | 无效的robotCode |
| 400 | invalid.robotCode | 无效的机器人标识 | 无效的机器人标识 |
| 400 | invalid.staffid | 无效的userId | 无效的userId |
| 400 | invalid.taskid | taskId非法 | taskId非法 |
| 400 | invalid.uk.parameter | invalid uk parameter | 查重字段为空 |
| 400 | invalid.unionId | invalid unionId | unionId非法 |
| 400 | invalid.unionid | unionid非法 | unionid非法 |
| 400 | invalid.unionId | 入参unionId不能为空 | 入参unionId不能为空 |
| 400 | invalid.user | 无效的用户ID | 无效的用户ID |
| 400 | invalid.userid | 找不到该用户 | 找不到该用户 |
| 400 | invalid.userid | 推送号非法 | 推送号非法 |
| 400 | invalid.userid.list | userId列表非法 | userId列表非法 |
| 400 | invalidAccessToken | 无权访问 | 无权访问 |
| 400 | invalidAgentId | agentId错误 | agentId错误 |
| 400 | invalidAgentId | 不合法的agentId | 不合法的agentId |
| 400 | invalidAgentId | 无效的agentId | 不合法的agentId |
| 400 | invalidAgentId | 无效的微应用ID | 无效的微应用ID |
| 400 | invalidAgentId | 获取审批钉盘空间信息，应用agentId不能为空 | 获取审批钉盘空间信息，应用agentId不能为空 |
| 400 | invalidAgentld | 无效的微应用ID | 无效的微应用ID |
| 400 | InvalidAuthentication | 不合法的access\_token | access\_token过期或者不存在，需要重新获取一下。 |
| 400 | invalidAuthInfo | 授权关系不存在 | 企业未开通对应的三方应用，无法获取该企业token |
| 400 | invalidAvailableTime | 有效时间非法 | 有效时间非法 |
| 400 | invalidClientIdOrSecret | clientId或者clientSecret错误 | clientId或者clientSecret错误 |
| 400 | invalidClientIdOrSecret | 无效的clientId或者clientSecret | 无效的clientId或者clientSecret |
| 400/409 | invalidCode | 无效的授权码 | 无效的授权码 |
| 400 | invalidCodeIdentity | 非法的码标识 | 非法的码标识 |
| 400 | invalidCorpId | 参数错误 | 参数错误 |
| 400 | invalidData.data.dataIsInvalid | 数据非法:%s | 数据非法 |
| 400 | invalidDepartmantId | INVALID\_DEPARTMENT\_ID | 错误的组织单元ID |
| 400 | invalidDepartmentId | INVALID\_DEPARTMENT\_ID | 不合理的组织单元ID；错误的组织单元ID |
| 400 | invalideChatId | 不合法的chatId | 不合法的chatId |
| 400 | invalidEcologicalCorpId | 不合法的合作空间corpId | 不合法的合作空间corpId |
| 400 | invalidEndTime | 获取审批实例ID列表，审批实例结束时间不能小于开始时间；且查询时间范围不能超过120天。 | 获取审批实例ID列表，审批实例结束时间不能小于开始时间；且查询时间范围不能超过120天。 |
| 400 | invalidFileId | 审批附件fileId不能为空 | 审批附件fileId不能为空 |
| 400 | invalidFileId | 授权预览审批附件，审批附件fileId不能为空 | 授权预览审批附件，审批附件fileId不能为空 |
| 400 | invalidFileInfos | 授权下载审批钉盘文件，授权的钉盘文件信息列表不能为空 | 授权下载审批钉盘文件，授权的钉盘文件信息列表不能为空 |
| 400 | invalidFileList | 授权预览审批附件，审批附件fileList不能为空 | 授权预览审批附件，审批附件fileList不能为空 |
| 400 | invalidGetTodoTaskSumUserId | 获取用户待审批数量，要查询的用户userId不能为空 | 获取用户待审批数量，要查询的用户userId不能为空 |
| 400 | invalidGroupParams | 群不存在或者群成员为空 | 群不存在或者群成员为空 |
| 400 | invalidInstanceArchiveIsSystem | 归档审批实例，是否通过系统操作参数不能为空 | 归档审批实例，是否通过系统操作参数不能为空 |
| 400 | invalidInstanceArchiveOpUserId | 归档审批实例，当isSystem为false时，操作人的userId不能为空 | 归档审批实例，当isSystem为false时，操作人的userId不能为空 |
| 400 | invalidInstanceArchiveOpUserIdNotOriginatorId | 归档审批实例，当isSystem为false时，操作人必须为OA审批管理员 | 归档审批实例，当isSystem为false时，操作人必须为OA审批管理员 |
| 400 | invalidInstanceCommentText | 审批实例评论内容不能为空 | 审批实例评论内容不能为空 |
| 400 | invalidInstanceCommentUserId | 审批实例评论人userId不能为空 | 审批实例评论人userId不能为空 |
| 400 | invalidInstanceExecuteActionerUserId | 同意拒绝审批任务，操作人的userId不能为空 | 同意拒绝审批任务，操作人的userId不能为空 |
| 400 | invalidInstanceExecuteActionerUserld | 同意拒绝审批任务，操作人的userld不能为空 | 同意拒绝审批任务，操作人的userld不能为空 |
| 400 | invalidInstanceExecuteResult | 同意拒绝审批任务，审批操作取值必填 且值必须为agree/refuse | 同意拒绝审批任务，审批操作取值必填 且值必须为agree/refuse |
| 400 | invalidInstanceExecuteResult | 同意拒绝审批任务，审批操作取值必填 且值必须为agree或refuse | 同意拒绝审批任务，审批操作取值必填 且值必须为agree或refuse |
| 400 | invalidInstanceExecuteTaskId | 同意拒绝审批任务，任务节点id不能为空 | 同意拒绝审批任务，任务节点id不能为空 |
| 400 | invalidInstanceId | 审批实例ID不能为空 | 审批实例ID不能为空；请检查processInstanceId参数是否正确 |
| 400 | invalidInstanceIdOrFieldId | 审批实例id或字段id不能为空 | 请检查processInstanceId、fieldId参数传值是否正确 |
| 400 | invalidInstanceIdOrFieldId | 审批实例id或当前审核人id不能为空 | 请检查processInstanceId、userId参数传值是否正确 |
| 400 | invalidInstanceListIdsStartTime | 获取审批实例ID列表，审批实例开始时间不能为空 | 获取审批实例ID列表，审批实例开始时间不能为空 |
| 400 | invalidInstanceTerminateIsSystem | 撤销审批实例，是否通过系统操作参数不能为空 | 撤销审批实例，是否通过系统操作参数不能为空 |
| 400 | invalidInstanceTerminateOperatingUserId | 撤销审批实例，当isSystem为false时，操作人的userId不能为空 | 撤销审批实例，当isSystem为false时，操作人的userId不能为空 |
| 400 | invalidIsvOrgId | INVALID\_ISV\_ORG\_ID | 无效的isv |
| 400 | invalidLang | INVALID\_LANG | 错误的通讯录语言 |
| 400 | invalidMaxResults | 获取审批实例ID列表，分页参数非法，每页大小，最多传20。 | 获取审批实例ID列表，分页参数非法，每页大小，最多传20。 |
| 400 | invalidMaxResults | 获取指定用户可见的审批表单列表，分页参数非法，每页大小，最多传100。 | 获取指定用户可见的审批表单列表，每页大小，最多传100。 |
| 400 | invalidMiniVersion | 不合法的versionId | 不合法的versionId |
| 400 | invalidMobileFormat | 手机号格式非法 | 手机号格式非法 |
| 400 | invalidMsgType | 无效的消息类型 | 无效的消息类型 |
| 400 | invalidNextToken | 获取审批实例ID列表，分页查询的游标不能为空 | 获取审批实例ID列表，分页查询的游标不能为空 |
| 400 | invalidNextToken | 获取指定用户可见的审批表单列表，分页查询的游标不能为空 | 获取指定用户可见的审批表单列表，分页查询的游标不能为空 |
| 400 | invalidOpenConversationId | 无效的群ID | 无效的群ID |
| 400 | invalidParam | %s | 参数为空或参数不合法；无效参数 |
| 400 | invalidParam | invalid param, %s | 应用id不能为空 |
| 400 | invalidParam | invalid params | 参数错误 |
| 400 | invalidParam | lippi\_live.room.preStartTimeCanNotEarlierThanNow | 预计开始时间不能早于当前时间 |
| 400 | invalidParam | lippi\_live.stream.paramError | 参数错误；参数错误，该直播不存在；参数错误，预计开播时间必须是未来时间并且小于预计结束时间。 |
| 400 | invalidParam | 参数错误 | 参数错误 |
| 400 | invalidParam | 参数错误: %s | 参数错误 |
| 400 | invalidParam.openConversationIdDecryptFailed | 会话ID解密失败 | 会话ID解密失败 |
| 400 | invalidParam.openConversationIdEmpry | 不合法的会话ID | 不合法的会话ID |
| 400 | invalidParam.openConversationIdEmpry | 会话ID为空 | 会话ID为空 |
| 400 | invalidParam.robotCodeEmpry | 机器人编码为空 | 机器人编码为空 |
| 400 | invalidParam.sceneGroupPermissionDenied | 无权限访问此群数据 | 无权限，该群未安装群模板，或者安装的群模板不属于当前token对应的应用名下 |
| 400/504 | invalidParameter | %s | 请求参数错误，请检查方法入参 |
| 400 | invalidParameter | CalendarId cannot be blank | 日历id不能为空；calendarId不能为空；日历id不能为空 |
| 400 | invalidParameter | Cannot get schedule information for more than limit. | 查询数目超出限制 |
| 400 | invalidParameter | Cannot query schedule for more than 90 days. | 查询天数超出限制 |
| 400 | invalidParameter | Event end time not set. | 日程结束时间未设置 |
| 400 | invalidParameter | Event id summary cannot be blank | 日程id不能为空 |
| 400 | invalidParameter | Event must be provided. | 日程不能为空 |
| 400 | invalidParameter | Event start time not set. | 日程开始时间未设置 |
| 400 | invalidParameter | Event summary cannot be blank | 日程标题不能为空 |
| 400 | invalidParameter | Meeting room invalid | 会议室不可用 |
| 400 | invalidParameter | Meeting rooms to remove must be provided. | 会议室不能为空 |
| 400 | invalidParameter | PARAMETER INVALID | 参数非法 |
| 400 | invalidParameter | Recurrence interval must between 1, 365 | interval需满足区间1,365 |
| 400 | invalidParameter | Recurrence range numberOfOccurrences must between 1, 99 | numberOfOccurrences需满足区间1,99 |
| 400 | invalidParameter | Subscribed calendar not support this method | 订阅日历不支持此方法 |
| 400 | invalidParameter | attendees batch size too large. Maximum allowed:5 | 会议室超过限制。最大5个。 |
| 400 | invalidParameter | calendar id cannot be blank | 日历id不能为空 |
| 400 | invalidParameter | calendar id cannot be null | 日历id不能为空 |
| 400 | invalidParameter | calendar name cannot be blank | 日历名不能为空 |
| 400 | invalidParameter | calendar name length must less than 128 | 日历名长度不能超过128个字 |
| 400 | invalidParameter | calendar type invalid | 日历类型异常 |
| 400 | invalidParameter | current user must in range | 当前用户必须在相应的群和企业内 |
| 400 | invalidParameter | eventId cannot be blank | 日程id不能为空 |
| 400 | invalidParameter | forwardErrorMessage | 参数异常 |
| 400 | invalidParameter | invalid parameter. | 参数错误；无效的参数 |
| 400 | invalidParameter | query ids cannot be empty | 查询id不能为空 |
| 400 | invalidParameter | roomId invalid | roomId不合法；会议室Id不合法 |
| 400 | invalidParameter | roomId must be provided. | roomId不能为空 |
| 400 | invalidParameter | shareExceedLimit | 共享人数超过上限 |
| 400 | invalidParameter | subscribe range cannot be null | 订阅范围不能为空 |
| 400 | invalidParameter | 下载审批附件参数错误 | 下载审批附件参数错误 |
| 400 | invalidParameter | 参数错误 | overtimeSettingIds参数异常；分页参数错误；参数异常；参数错误；未填最后工作日、离职人userId等；未填离职人userId；系统参数无效 |
| 400 | invalidParameter | 参数错误:%s | 参数异常 |
| 400 | invalidParameter | 参数错误:%s%s | 参数异常 |
| 400 | invalidParameter | 参数错误，具体可能为：企业ID、审批模板code等参数错误 | 参数错误，具体可能为：企业ID、审批模板code等参数错误 |
| 400 | invalidParameter | 发起审批参数错误。具体可能为：企业ID、审批模板code等参数错误，或发起人已离职 | 发起审批参数错误。具体可能为：企业ID、审批模板code等参数错误，或发起人已离职 |
| 400 | invalidParameter | 同意或拒绝审批任务参数错误 | 同意或拒绝审批任务参数错误 |
| 400 | invalidParameter | 员工 id列表大小不在1,50范围 | 员工 id列表大小不在1,50范围 |
| 400 | invalidParameter | 存在空参数 | 存在空参数 |
| 400 | invalidParameter | 归档审批实例参数错误 | 请按接口文档检查请求入参是否正确 |
| 400 | invalidParameter | 授权下载审批钉盘文件参数错误 | 授权下载审批钉盘文件参数错误 |
| 400 | invalidParameter | 授权预览审批附件参数错误 | 授权预览审批附件参数错误 |
| 400 | invalidParameter | 撤销审批实例参数错误 | 撤销审批实例参数错误 |
| 400 | invalidParameter | 无效的参数 | 无效的参数 |
| 400 | invalidParameter | 无效的请求参数 | 无效的请求参数 |
| 400 | invalidParameter | 无效请求参数 | 无效请求参数 |
| 400 | invalidParameter | 添加审批评论参数错误 | 添加审批评论参数错误 |
| 400 | invalidParameter | 用户ID或转正时间不能为空 | 用户ID或转正时间不能为空 |
| 400 | invalidParameter | 系统参数无效或者传入的微应用Id和员工userId有误 | 系统参数无效或者微应用Id和员工userId传入有误 |
| 400 | invalidParameter | 获取单个审批实例详情参数错误 | 获取单个审批实例详情参数错误 |
| 400 | invalidParameter | 获取审批钉盘空间信息参数错误 | 获取审批钉盘空间信息参数错误 |
| 400 | invalidParameter | 获取当前企业所有可管理的表单参数错误 | 获取当前企业所有可管理的表单参数错误 |
| 400 | invalidParameter | 获取指定用户可见的审批表单列表参数错误 | 获取指定用户可见的审批表单列表参数错误 |
| 400 | invalidParameter | 获取用户待审批数量参数错误 | 获取用户待审批数量参数错误 |
| 400 | invalidParameter | 请求参数列表长度过长，最大长度为100 | 请求参数列表长度过长，最大长度为100 |
| 400 | invalidParameter | 请求参数碳能量类型错误，请核对传递的数据类型 | 请求参数碳能量类型错误，请核对传递的数据类型 |
| 400 | invalidParameter | 请求参数缺失或无效！ | 请求参数缺失或无效！ |
| 400 | invalidParameter | 请求对象为空 | 请求对象为空 |
| 400 | invalidParameter | 非法的参数 | 非法的参数 |
| 400 | invalidParameter.appKey.blank | appKey为空 | 自建应用的appKey为空 |
| 400 | invalidParameter.appKey.targetAppKeyInvalid | 目标应用编码非法:%s | 目标应用编码非法 |
| 400 | invalidParameter.applicationName.applicationNameDuplicate | 应用名称已被占用:%s | 应用名称已被占用 |
| 400 | invalidParameter.applicationName.applicationNameTooLong | 名称不能超过150个字符(75个汉字):%s | 名称不能超过150个字符(75个汉字) |
| 400 | invalidParameter.argumentInvalid | %s | 参数非法，请查看具体错误信息 |
| 400 | invalidParameter.cardTemplate.notFound | 不存在的卡片模板 | 不存在的卡片模板 |
| 400 | invalidParameter.cid.empty | 单聊会话id为空 | 单聊会话id为空 |
| 400 | invalidParameter.cid.empty | 群id为空 | 群id为空 |
| 400/500 | invalidParameter.corp.corpNotExist | 企业不存在:%s | 企业不存在 |
| 400 | invalidParameter.corporation.invalidAuthorizationCorporationId | authCorpId非法:%s | authCorpId非法 |
| 400 | invalidParameter.corporation.invalidAuthorizationCorporationId | 不是合法的授权组织:%s | 不是合法的授权组织 |
| 400 | invalidParameter.cursor.invalid | 无效的nextToken | 无效的nextToken，请检查nextToken是否正确 |
| 400 | invalidParameter.event.calendarId | CalendarId cannot be blank | 日历id不能为空 |
| 400 | invalidParameter.event.eventId | eventId cannot be blank | 日程id不能为空 |
| 400 | invalidParameter.filterPraseFailed | %s | 入参：matcherJson无效或不正确 |
| 400 | invalidParameter.form.invalidArgumentsForSearchingEmployeeField | 搜人员组件值参数有误.:%s | 搜人员组件值参数有误. |
| 400 | invalidParameter.form.invalidArgumentsForSearchingEmployeeField | 搜人员组件值参数有误:%s | 搜人员组件值参数有误 |
| 400 | invalidParameter.input.invalid | %s | 入参校验失败 |
| 400 | invalidParameter.invalid | token对应机器人不存在 | token对应机器人不存在，请检查机器人是否在群内 |
| 400 | invalidParameter.invalidOrgId | crm has not been installed for this org | 服务窗的组织id非法 |
| 400 | invalidParameter.json.componentValuesEmptyInSearchFieldJson | searchFieldJson所有组件值都为空:%s | searchFieldJson所有组件值都为空 |
| 400 | invalidParameter.json.invalidJsonStringParamter | %s | bizObjectJson参数解析失败 |
| 400 | invalidParameter.maxResults | maxResults size must within range 0,500 | maxResults超过范围 |
| 400 | invalidParameter.metaKey.invalidMetaKey | 非法的meta key:%s | 非法的meta key |
| 400 | invalidParameter.metaKey.invalidMetaKey | 非法的元数据关键词:%s | 非法的元数据关键词 |
| 400 | invalidParameter.methodInputs.invalid | 入参校验失败:%s | 入参校验失败 |
| 400 | invalidParameter.methodInputs.invalidFormat | 数据格式错误:%s | 数据格式错误 |
| 400 | invalidParameter.msg.unsupport | %s | 不支持的消息类型 |
| 400 | invalidParameter.msg.unsupport | 不支持的消息类型 | 不支持的消息类型 |
| 400 | invalidParameter.msgBody.invalid | %s | 消息体必须是JSON格式 |
| 400 | invalidParameter.msgBody.invalid | body必须是JSON | body必须是JSON |
| 400 | invalidParameter.msgKey.empty | %s | msgKey为空 |
| 400 | invalidParameter.msgKey.empty | 缺少msgKey | 缺少msgKey |
| 400 | invalidParameter.msgKey.invalid | %s | msgKey无效，请传入正确的msgKey |
| 400 | invalidParameter.msgKey.invalid | msgKey无效 | msgKey无效 |
| 400 | invalidParameter.msgParam.invalid | %s | msgParam格式非法，必须是json格式 |
| 400 | invalidParameter.msgParam.invalid | msgParam必须是json格式 | msgParam必须是json格式 |
| 400 | invalidParameter.msgParam.tooLong | %s | 消息内容太长消息内容太长，请缩减内容长度 |
| 400 | invalidParameter.msgParam.tooLong | 消息内容太长 | 消息内容太长 |
| 400 | invalidParameter.muteStatusError | 不合法的的禁言状态 | 不合法的的禁言状态 |
| 400 | invalidParameter.name.invalid | 只允许数字,字母,下划线:%s | 只允许数字,字母,下划线；只允许数字，字母，下划线 |
| 400 | invalidParameter.number.exceed | 数字超过限制:%s | 数字超过限制 |
| 400 | invalidParameter.number.exceedMax | 超过限制:%s | 超过限制 |
| 400 | invalidParameter.openConversationId.invalid | 无效的会话id | 无效的会话id |
| 400 | invalidParameter.openConversationIdDecError | 会话ID解密失败 | 会话ID解密失败 |
| 400 | invalidParameter.openConversationIdError | 不合法的会话ID | 不合法的会话ID |
| 400 | invalidParameter.orgId.invalid | 无效的企业ID | 无效的企业ID |
| 400 | invalidParameter.pageSize.invalid | 无效的maxResults | maxResults超出上限200 |
| 400 | invalidParameter.param.empty | 入参为空 | 入参为空 |
| 400 | invalidParameter.param.empty | 参数为空 | 参数为空 |
| 400 | invalidParameter.param.invalid | %s | 参数不合法，请检查参数是否为空；参数不合法，请检查是否有参数为空 |
| 400 | invalidParameter.param.invalid | 入参错误：%s | 入参错误 |
| 400 | invalidParameter.param.invalid | 参数不合法 | 参数不合法；参数不合法，请检查参数是否为空 |
| 400 | invalidParameter.param.invalid | 参数不合法%s | 参数不合法 |
| 400 | invalidParameter.param.orgIdInvalid | 企业不存在或者已经解散 | 企业不存在或者已经解散 |
| 400 | invalidParameter.parameter.accessKeyNotMatch | 接入密钥不匹配:%s | 接入密钥不匹配 |
| 400 | invalidParameter.parameter.accessKeyNotMatch | 接入密钥不匹配:%s | 接入密钥不匹配 |
| 400 | invalidParameter.parameter.arrayLengthExceed | ARRAY类型超长:%s | ARRAY类型超长 |
| 400 | invalidParameter.parameter.attachmentsAmountExceedTwo | 不可以超过两个附件:%s | 不可以超过两个附件 |
| 400 | invalidParameter.parameter.blankDataTitle | 数据标题不能为空,请检查数据标题设置:%s | 数据标题不能为空,请检查数据标题设置；数据标题不能为空，请检查数据标题设置 |
| 400 | invalidParameter.parameter.doubleTypeLengthExceed | DOUBLE类型超长:%s | DOUBLE类型超长 |
| 400 | invalidParameter.parameter.error | 参数错误:%s | 参数错误 |
| 400 | invalidParameter.parameter.exceedLengthLimit | 参数超过了长度限制:%s | 参数超过了长度限制 |
| 400 | invalidParameter.parameter.expectDoubleButNonNumeric | DOUBLE类型非数字:%s | DOUBLE类型非数字 |
| 400 | invalidParameter.parameter.illegalParameterLength | 长度参数非法:%s | 长度参数非法 |
| 400 | invalidParameter.parameter.illegalSerialNumberFieldType | 流水号组件类型非法:%s | 流水号组件类型非法 |
| 400 | invalidParameter.parameter.illegalSerialNumberPrefix | 流水号前缀格式错误:%s | 流水号前缀格式错误 |
| 400 | invalidParameter.parameter.incorrectFormUuid | 指定的表单id有误:%s | 指定的表单id有误 |
| 400 | invalidParameter.parameter.invalidFileUrl | 文件地址参数非法:%s | 文件地址参数非法 |
| 400 | invalidParameter.parameter.invalidUrl | 请求地址非法:%s | 请求地址非法 |
| 400 | invalidParameter.parameter.optionValueOfRadioSelectFieldExceed | 单选/下拉单选组件选项值不能超过255.:%s | 单选/下拉单选组件选项值不能超过255. |
| 400 | invalidParameter.parameter.optionValueOfRadioSelectFieldExceed | 单选和下拉单选组件选项值不能超过255:%s | 单选和下拉单选组件选项值不能超过255 |
| 400 | invalidParameter.parameter.parameterIsEmpty | 不能为空:%s | 不能为空 |
| 400 | invalidParameter.parameter.tableFieldInTableField | 明细组件下不能含有明细组件:%s | 明细组件下不能含有明细组件 |
| 400 | invalidParameter.parameter.typeOfArrayItemCanNotBeString | ARRAY类型不允许为String:%s | ARRAY类型不允许为String |
| 400 | invalidParameter.phoneNumber.numberIsBlank | 手机号码不能为空:%s | 手机号码不能为空 |
| 400 | invalidParameter.process.emptyProcessInstanceIds | processInstanceIds不能为空:%s | processInstanceIds不能为空 |
| 400 | invalidParameter.processQueryKey.missing | %s | 缺少processQueryKey |
| 400 | invalidParameter.processQueryKey.missing | 缺少processQueryKey | 缺少processQueryKey |
| 400 | invalidParameter.processQueryKeys.overMax | %s | processQueryKeys超过数量上限20，请将processQueryKeys拆分成多个长度不超过20的数组，分批次调用此接口 |
| 400 | invalidParameter.publicAccount.publicAccountNotSupport | 暂不支持公共账号登录:%s | 暂不支持公共账号登录 |
| 400 | invalidParameter.robotCode | %s | 无效的robotCode，请检查机器人是否在群内；机器人不存在，请检查企业内是否安装了robotCode对应的机器人 |
| 400 | invalidParameter.robotCode.auth | 只有酷应用身份才可使用这个机器人 | 只有酷应用身份才可使用这个机器人 |
| 400 | invalidParameter.robotCode.auth | 此downloadCode和机器人robotCode不匹配，请使用接收此条消息机器人robotCode和对应的downloadCode | 此downloadCode和机器人robotCode不匹配，请使用接收此条消息机器人robotCode和对应的downloadCode |
| 400 | invalidParameter.robotCode.auth | 此应用appkey和机器人robotCode不匹配，请使用机器人应用的appkey | 此应用appkey和机器人robotCode不匹配，请使用机器人应用的appkey |
| 400 | invalidParameter.robotCode.auth | 此应用suiteKey和机器人不匹配，请使用机器人绑定的ISV应用的suiteKey发送消息 | 此应用suiteKey和机器人不匹配，请使用机器人绑定的ISV应用的suiteKey发送消息 |
| 400 | invalidParameter.robotCode.auth | 该接口仅支持企业自建应用或三方应用授权调用 | 该接口仅支持企业自建应用或三方应用授权调用 |
| 400 | invalidParameter.robotCode.auth | 调用该接口的企业和此downloadCode对应机器人企业所属不同 | 调用该接口的企业和此downloadCode对应机器人企业所属不同 |
| 400 | invalidParameter.robotCode.coolApp | 绑定这个机器人的酷应用没有在人与人单聊会话中被使用 | 绑定这个机器人的酷应用没有在人与人单聊会话中被使用 |
| 400 | invalidParameter.robotCode.coolApp | 绑定这个机器人的酷应用没有在群中被使用 | 绑定这个机器人的酷应用没有在群中被使用 |
| 400 | invalidParameter.robotCode.coolApp | 酷应用编码和机器人不匹配，请使用此酷应用绑定的机器人发送消息 | 酷应用编码和机器人不匹配，请使用此酷应用绑定的机器人发送消息 |
| 400 | invalidParameter.robotCode.coolApp | 酷应用编码无效 | 酷应用编码无效 |
| 400 | invalidParameter.robotCode.downloadCode | 下载码有误或者已经过期 | 下载码有误或者已经过期 |
| 400 | invalidParameter.robotCode.empty | %s | 机器人robotCode无效 |
| 400 | invalidParameter.robotCode.empty | 机器人downloadCode为空 | 机器人downloadCode为空 |
| 400 | invalidParameter.robotCode.empty | 机器人robotCode为空 | 机器人robotCode无效，请检查机器人是否在群内 |
| 400 | invalidParameter.robotCode.invalid | %s | 无效的robotCode；机器人不存在，请检查企业内是否安装了robotCode对应的机器人 |
| 400 | invalidParameter.robotCode.invalid | 无效的robotCode | 无效的robotCode |
| 400 | invalidParameter.robotCode.missing | %s | 缺少robotCode |
| 400 | invalidParameter.robotCode.missing | 缺少robotCode | 缺少robotCode |
| 400 | invalidParameter.robotCode.notExsit | %s | 机器人不存在；机器人不存在，请检查企业内是否安装了robotCode对应的机器人；机器人不存在，请检查会话内是否安装了robotCode对应的机器人 |
| 400 | invalidParameter.robotCode.notExsit | 机器人不存在 | 机器人不存在；机器人不存在，请检查机器人是否在群内 |
| 400 | invalidParameter.serviceCallBack.unsupportedServiceInvokeType | 不支持的服务注册类型:%s | 不支持的服务注册类型 |
| 400 | invalidParameter.subscribed.invalid | Subscribed calendar not support this method | 订阅日历不支持此方法 |
| 400 | invalidParameter.system.param | 无效的企业targetCorpId | 需要查询的企业不存在时抛错 |
| 400 | invalidParameter.system.param | 系统参数为空 | 系统参数为空的时候返回 |
| 400 | invalidParameter.task.onlyPlatformTaskCanBeExecuted | 只能执行宜搭平台任务:%s | 只能执行宜搭平台任务 |
| 400 | invalidParameter.task.unsupportedOutResultType | 不支持的任务执行动作.:%s | 不支持的任务执行动作. |
| 400 | invalidParameter.task.unsupportedOutResultType | 不支持的任务执行动作:%s | 不支持的任务执行动作 |
| 400 | invalidParameter.token.invalid | %s | 无授权的token |
| 400 | invalidParameter.token.invalid | 无授权的token | 无授权的token |
| 400 | invalidParameter.unionIdInvalid | %s | operatorId非法，请检查参数是否正确；unionId非法，请检查参数是否正确 |
| 400 | invalidParameter.userId.empty | %s | 缺少staffId |
| 400 | invalidParameter.userId.empty | 缺少staffId | 缺少staffId |
| 400 | invalidParameter.userIdList | 不合法的群成员列表 | 不合法的群成员列表 |
| 400 | invalidParameter.userIds.empty | %s | 用户userId列表为空 |
| 400 | invalidParameter.userIds.empty | 用户userId列表为空 | 用户userId列表为空 |
| 400 | invalidParameter.userIds.overMax | %s | 用户userId列表超过最大限制100,请将userId拆分成多个长度不超过100的数组，分批次调用此接口 |
| 400 | invalidParameter.userIds.overMax | 用户userId列表超过最大限制 | 用户userId列表超过最大限制 |
| 400/500 | invalidParameter.validation.parameterValidationFailed | 参数校验失败:%s | 参数校验失败 |
| 400 | invalidParameterCspace | 使用授权码方式认证时，isvOrgId不能为空 | 使用授权码方式认证时，isvOrgId不能为空 |
| 400 | invalidParams | 不合法的参数 | 不合法的参数 |
| 400 | invalidParamter.role | 无效的role | 无效的role |
| 400 | invalidPayCode | 无效payCode | 无效payCode |
| 400 | invalidPayCode | 无效的付款码 | 无效的付款码 |
| 400 | invalidPayCode | 非法的码值 | 非法的码值 |
| 400 | invalidProcessCode | 审批模板processCode不能为空 | 审批模板processCode不能为空 |
| 400 | invalidProcessCode | 审批模板processCode不能为空或超过最大数量限制 | 请检查processCode参数传值是否正确 |
| 400 | invalidProcessInstanceId | 实例id不能为空 | 实例id不能为空 |
| 400 | invalidProcessInstanceId | 授权预览审批附件，实例id不能为空 | 授权预览审批附件，实例id不能为空 |
| 400 | invalidRequest | %s | 请求非法 |
| 400 | invalidRequest.bizObjectNotExist | 业务对象不存在 | 无效的bizObjectId；无效的bizObjectId参数 |
| 400 | invalidRequest.dataNotReady | The requested data is not available yet. Please try again later. | 被请求的资源或数据还未准备完毕 |
| 400 | invalidRequest.document.broken | The document is broken and the server is unable to complete your request. | 文档已损坏 |
| 400 | invalidRequest.document.stillInitializing | The document is still initializing. Please try again later. | 文档初始化中，请稍后重试。 |
| 400 | invalidRequest.document.stillInitializing | The document is under initialization. Please try again later | 文档初始化中，请稍后重试 |
| 400 | invalidRequest.exceededMaximumLimit | 超过插件最大个数限制 | 超过插件最大个数限制 |
| 400 | invalidRequest.file.fileRecordNotExist | 文件记录不存在 | 文件记录不存在 |
| 400 | invalidRequest.file.getUploadUrlFile | 获取文件上传地址失败 | 获取文件上传地址失败 |
| 400 | invalidRequest.inputArgs.invalid | %s | 参数错误, 请查看错误信息。；请求参数不合法。可能的错误包含range地址不正确，输入参数数据维度不正确，颜色格式不正确等。具体错误请查看错误信息。；请求参数不合法，请查看错误信息。 |
| 400 | invalidRequest.inputArgs.invalid | 方法入参校验失败 | 方法入参校验失败，检查是否有必填参数未填，或者unionId是否合法等 |
| 400 | invalidRequest.inputArgs.operatorIdIllegal | The operatorId is illegal. | operatorId不合法。 |
| 400 | invalidRequest.inputArgs.overLimit | 批量操作数量超过限制 | 批量接口操作数量超限 |
| 400 | invalidRequest.inputArgs.unionIdIllegal | The operatorId is illegal. | operatorId不合法。 |
| 400 | invalidRequest.inputArgs.workbookIdIllegal | The workbookId is illegal. | workbookId不合法。 |
| 400 | invalidRequest.invalidAguemnts | invalid arguments | 参数错误 |
| 400 | invalidRequest.invalidAguemnts | 参数错误:%s | 参数错误 |
| 400 | invalidRequest.jsonFormatErroj | json格式错误 | json格式错误 |
| 400 | invalidRequest.opUserNotExist | 操作用户不存在 | 无效的opUserID或opUserID不存在 |
| 400 | invalidRequest.permission.operationIllegal | 权限操作非法 | 权限操作非法，不能移除自己的权限，也不能移除所有者 |
| 400 | invalidRequest.permission.overLimit | 权限信息数量超过限制 | 增加的权限信息数量超过限制 |
| 400 | invalidRequest.process.createInstanceFail | 创建流程实例失败 | 创建流程实例失败 |
| 400 | invalidRequest.resource.notWorkbook | %s | 不支持的文档类型，请检查workbookId。 |
| 400 | invalidRequest.robotCodeNotMatch | 应用与绑定的机器人robotCode不相符 | 应用与绑定的机器人robotCode不相符 |
| 400 | invalidRequest.robotIsStop | 机器人已经被组织停用 | 机器人已经被组织停用 |
| 400 | invalidRequest.robotNotExist | 机器人不存在，请核实后添加 | 机器人不存在，请核实后添加 |
| 400 | invalidRequest.template.notFound | 文档模板不存在 | 文档模板不存在 |
| 400 | invalidRequest.workspace.nameConflict | 知识库名称冲突 | 知识库名称冲突 |
| 400 | invalidRequest.workspace.notInOrg | 知识库不归属当前组织 | 知识库不归属当前组织 |
| 400 | invalidRequest.workspaceNode.nameConflict | 知识库文档名称冲突 | 知识库文档名称冲突 |
| 400 | invalidRequest.workspaceNode.notInWorkspace | 节点不在知识库内 | 节点不在知识库内 |
| 400 | invalidRequest.workspaceNode.parentNotFound | 父节点不存在 | 父节点不存在 |
| 400 | invalidRequestMethod | 请求方式错误，必须为post请求！ | 请求方式错误，必须为post请求！ |
| 400 | invalidRequestParams | INVALID\_REQUEST\_PARAMS | 不合法的参数 |
| 400 | invalidRequestParams | 参数错误（请根据文档检查对应参数） | 参数错误（请根据文档检查对应参数） |
| 400 | invalidRequestParams | 必填请求参数缺失 | 必填请求参数缺失 |
| 400 | invalidRoomCode | invalidRoomCode | 会议码无效 |
| 400 | invalidScheduleConferenceId | invalidScheduleConferenceId | 预约会议id无效 |
| 400 | invalidSeCretKey | 无效的SeCretKey | 无效的SeCretKey |
| 400 | invalidSign | 签名无效 | 签名无效 |
| 400 | invalidSize | 不合法的大小 | overtimeSettingIds不合法的大小 |
| 400 | invalidState.account.accountNotAuthorized | 您所使用的账号未被授权，请联系您所在企业的宜搭平台管理员进行账号授权后继续使用:%s | 您所使用的账号未被授权，请联系您所在企业的宜搭平台管理员进行账号授权后继续使用 |
| 400 | invalidState.account.trialAccountAttachmentCapacityExceed | 试用版宜搭账号上传附件容量已超额， 请在钉钉购买宜搭正式版本后继续使用:%s | 试用版宜搭账号上传附件容量已超额， 请在钉钉购买宜搭正式版本后继续使用 |
| 400 | invalidState.account.trialAccountAttachmentCapacityExceed | 试用账号上传附件容量已超额, 请在钉钉购买正式版本后继续使用:%s | 试用账号上传附件容量已超额, 请在钉钉购买正式版本后继续使用 |
| 400 | invalidState.account.trialAccountSubmissionRecordExceed | 试用版宜搭账号提交记录已超额， 请在钉钉购买宜搭正式版本后继续使用:%s | 试用版宜搭账号提交记录已超额， 请在钉钉购买宜搭正式版本后继续使用 |
| 400 | invalidState.account.trialAccountSubmissionRecordExceed | 试用账号提交记录已超额, 请在钉钉购买正式版本后继续使用:%s | 试用账号提交记录已超额, 请在钉钉购买正式版本后继续使用 |
| 400 | invalidState.administrator.tooManyAdministrators | 管理员过多:%s | 管理员过多 |
| 400 | invalidState.application.invalidApplicationSetting | 应用配置错误，请联系管理员:%s | 应用配置错误，请联系管理员 |
| 400 | invalidState.associationForm.incorrectAssociationDataSetting | 关联其他表单数据配置错误,数据来源字段未支持搜索,请在"数据管理"进行配置:%s | 关联其他表单数据配置错误,数据来源字段未支持搜索,请在"数据管理"进行配置；关联其他表单数据配置错误，数据来源字段未支持搜索，请在"数据管理"进行配置 |
| 400/500 | invalidState.authorization.invalidAuthorizationInformation | 无效的认证信息:%s | 无效的认证信息 |
| 400 | invalidState.batchOperation.batchUpdateRecordDoesNotExist | 批量更新记录查询不到:%s | 批量更新记录查询不到 |
| 400 | invalidState.batchOperation.dataNeedNotToBeUpdate | 没有符合条件的数据需要更新:%s | 没有符合条件的数据需要更新 |
| 400 | invalidState.batchOperation.duplicateConditionExist | 存在多行相同的过滤条件:%s | 存在多行相同的过滤条件 |
| 400 | invalidState.batchOperation.excelRowCountExceed | excel中行数超过限制:%s | excel中行数超过限制 |
| 400 | invalidState.batchOperation.illegalUpdateValue | 更新值不合法:%s | 更新值不合法 |
| 400 | invalidState.batchOperation.importSequenceDoesNotExist | 导入批次不存在或已删除:%s | 导入批次不存在或已删除 |
| 400 | invalidState.batchOperation.noDataInExcel | excel中没有数据:%s | excel中没有数据 |
| 400 | invalidState.batchOperation.onlyTheFrontPortionCanBeUpdated | 最多可按当前筛选条件更新前若干条数据，如有超过，请调整筛选条件:%s | 最多可按当前筛选条件更新前若干条数据，如有超过，请调整筛选条件 |
| 400 | invalidState.batchOperation.previousBatchUpdatingIsRunning | 存在正在运行的批量修改,请稍后再试:%s | 存在正在运行的批量修改,请稍后再试；存在正在运行的批量修改，请稍后再试 |
| 400 | invalidState.batchOperation.ruleIsInvalid | 批量更新规则中有不存在的组件:%s | 批量更新规则中有不存在的组件 |
| 400 | invalidState.batchOperation.runningImportTaskExceedLimit | 存在的运行中的导入任务超过上限:%s | 存在的运行中的导入任务超过上限 |
| 400 | invalidState.dataLinkage.dataSourceFieldNotSupportSearch | 数据联动配置错误,数据来源字段未支持搜索,请在"数据管理"进行配置:%s | 数据联动配置错误,数据来源字段未支持搜索,请在"数据管理"进行配置；数据联动配置错误，数据来源字段未支持搜索，请在"数据管理"进行配置 |
| 400 | invalidState.dataLinkage.filterFieldNotSupportSearch | 数据联动配置错误,过滤字段未支持搜索,请在"数据管理"进行配置:%s | 数据联动配置错误,过滤字段未支持搜索,请在"数据管理"进行配置；数据联动配置错误，过滤字段未支持搜索，请在"数据管理"进行配置 |
| 400 | invalidState.file.failedToUploadSchema | 上传CDN失败:%s | 上传CDN失败 |
| 400 | invalidState.file.failedToUploadSchema | 上传到内容分发服务器失败:%s | 上传到内容分发服务器失败 |
| 400 | invalidState.form.bindingOfFormAndOtherProcessesAlreadyExist | 页面与其他流程已有绑定关系:%s | 页面与其他流程已有绑定关系 |
| 400 | invalidState.form.componentActingAsApprovalConditionNotFilled | 已作为条件审批的组件必须必填(包含已失效条件):%s | 已作为条件审批的组件必须必填(包含已失效条件) |
| 400 | invalidState.form.componentIsDeleted | 组件已被删除:%s | 组件已被删除 |
| 400 | invalidState.form.correspondingFormIsDeleted | 对应表单已删除,请联系应用管理员:%s | 对应表单已删除,请联系应用管理员；对应表单已删除，请联系应用管理员 |
| 400 | invalidState.form.dataDoesNotExistOrIsDeleted | 数据不存在或已删除:%s | 数据不存在或已删除 |
| 400 | invalidState.form.duplicateComponentID | 组件ID不允许重复:%s | 组件ID不允许重复 |
| 400 | invalidState.form.duplicateSlug | Slug不允许重复:%s | Slug不允许重复 |
| 400 | invalidState.form.emptyPage | 页面内容不能为空:%s | 页面内容不能为空 |
| 400 | invalidState.form.failedToDeleteNavigationWithPage | 不允许删除包含有页面的导航:%s | 不允许删除包含有页面的导航 |
| 400 | invalidState.form.formDataIsBlank | 表单数据不能为空:%s | 表单数据不能为空 |
| 400 | invalidState.form.formNotExist | 表单不存在:%s | 表单不存在 |
| 400 | invalidState.form.formWasModified | 表单已变更，请刷新当前页面重新提交:%s | 表单已变更，请刷新当前页面重新提交 |
| 400 | invalidState.form.incorrectPageSetting | 前页面存在系统配置问题，请联系应用管理员:%s | 前页面存在系统配置问题，请联系应用管理员 |
| 400 | invalidState.form.instanceAssociationComponentDoesNotExist | 实例关联组件不存在:%s | 实例关联组件不存在 |
| 400 | invalidState.form.invalidComponentID | 组件ID不合法:%s | 组件ID不合法 |
| 400 | invalidState.form.invalidFormData | 表单校验失败:%s | 表单校验失败 |
| 400 | invalidState.form.invalidPageStatus | 表单状态错误:%s | 表单状态错误 |
| 400 | invalidState.form.pageInstanceNotFound | 未找到页面实例:%s | 未找到页面实例 |
| 400 | invalidState.form.pageNotFound | 页面不存在:%s | 页面不存在 |
| 400 | invalidState.form.processContainsRunningInstances | 流程存在运行中的实例不能删除:%s | 流程存在运行中的实例不能删除 |
| 400 | invalidState.form.publishedPageNotFound | 未找到已上线的页面:%s | 未找到已上线的页面 |
| 400 | invalidState.form.relationBetweenFormAndTheProcessDoesNotExist | 页面与流程的关联关系不存在:%s | 页面与流程的关联关系不存在 |
| 400 | invalidState.form.targetFormIsDeleted | 跳转的目标表单已删除:%s | 跳转的目标表单已删除 |
| 400 | invalidState.form.variablesExceedFive | 表单内置变量不能超过5个:%s | 表单内置变量不能超过5个 |
| 400 | invalidState.instance.formStatusChanged | 实例状态已变更，请刷新后再试:%s | 实例状态已变更，请刷新后再试 |
| 400 | invalidState.instance.instanceDataHasBeenModified | 实例数据已修改，请刷新当前页面:%s | 实例数据已修改，请刷新当前页面 |
| 400 | invalidState.instance.instanceStatusHasChanged | 实例状态已变更，请刷新当前页面:%s | 实例状态已变更，请刷新当前页面 |
| 400 | invalidState.key.keyCorrespondingToDataAlreadyExists | 数据对应的KEY已存在:%s | 数据对应的KEY已存在 |
| 400 | invalidState.mapping.mappingTypeNotMatchFieldType | 字段类型与映射类型不匹配:%s | 字段类型与映射类型不匹配 |
| 400 | invalidState.mapping.noMappingRelationship | 不存在映射关系:%s | 不存在映射关系 |
| 400 | invalidState.message.orderedMessageQueueWithoutShardingKey | 顺序消息未指定shardingKey:%s | 顺序消息未指定shardingKey |
| 400 | invalidState.mobileVerificationCode.codeExpired | 手机验证码已经失效, 请重新发送:%s | 手机验证码已经失效, 请重新发送；手机验证码已经失效， 请重新发送 |
| 400 | invalidState.mobileVerificationCode.codeIncorrect | 手机验证码有误, 请重新输入:%s | 手机验证码有误, 请重新输入；手机验证码有误， 请重新输入 |
| 400 | invalidState.mobileVerificationCode.codeIsAbnormal | 发送验证码异常, 请检查手机号码是否正确:%s | 发送验证码异常, 请检查手机号码是否正确；发送验证码异常， 请检查手机号码是否正确 |
| 400 | invalidState.openSearch.canNotFindKeyAccordingToComponentFieldId | 找不到OpenSearch上对应的key:%s | 找不到OpenSearch上对应的key |
| 400 | invalidState.openSearch.canNotFindKeyAccordingToComponentFieldId | 找不到高性能检索服务上对应的key:%s | 找不到高性能检索服务上对应的key |
| 400 | invalidState.openSearch.componentCanNotSupportThisOperatorType | 组件不支持该逻辑操作:%s | 组件不支持该逻辑操作 |
| 400 | invalidState.openSearch.currentFormIsRebuilding | 当前表单重构中,请稍后再试:%s | 当前表单重构中,请稍后再试；当前表单重构中，请稍后再试 |
| 400 | invalidState.openSearch.cursorExceedFiveThousand | 搜索接口翻页不能超过5000,请细化过滤条件缩小查询范围:%s | 搜索接口翻页不能超过5000,请细化过滤条件缩小查询范围；搜索接口翻页不能超过5000，请细化过滤条件缩小查询范围 |
| 400 | invalidState.openSearch.dataToUpdateNotFound | 更新的opensearch data数据不存在:%s | 更新的opensearch data数据不存在 |
| 400 | invalidState.openSearch.dataToUpdateNotFound | 更新的高性能检索服务 data数据不存在:%s | 更新的高性能检索服务 data数据不存在 |
| 400 | invalidState.openSearch.deficiencyOfMappingForFormField | 表单组件和索引的映射关系不存在:%s | 表单组件和索引的映射关系不存在 |
| 400 | invalidState.openSearch.failToSaveData | opensearch data数据保存失败, 组件映射关系找不到:%s | opensearch data数据保存失败, 组件映射关系找不到 |
| 400 | invalidState.openSearch.failToSaveData | 数据保存失败，组件映射关系找不到:%s | 数据保存失败，组件映射关系找不到 |
| 400 | invalidState.openSearch.invalidFormDataExist | 表单数据有误,请联系应用管理员:%s | 表单数据有误,请联系应用管理员；表单数据有误，请联系应用管理员 |
| 400 | invalidState.openSearch.notSupportDataLinkageAndAssociationForm | 数据联动/关联其他表单数据 不支持用OpenSearch替换mysql:%s | 数据联动/关联其他表单数据 不支持用OpenSearch替换mysql |
| 400 | invalidState.openSearch.notSupportDataLinkageAndAssociationForm | 数据联动和关联其他表单数据 不支持用高性能检索服务替换mysql:%s | 数据联动和关联其他表单数据 不支持用高性能检索服务替换mysql |
| 400 | invalidState.openSearch.numberComponentCanNotSupportNullQuery | 数字组件不支持null查询:%s | 数字组件不支持null查询 |
| 400 | invalidState.openSearch.openSearchQueryFail | openSearch查询失败:%s | openSearch查询失败 |
| 400 | invalidState.openSearch.openSearchQueryFail | 高性能检索服务查询失败:%s | 高性能检索服务查询失败 |
| 400 | invalidState.openSearch.searchFieldExceed | 该类型支持搜索的字段超过限制:%s | 该类型支持搜索的字段超过限制 |
| 400 | invalidState.openSearch.simultaneousFuzzySearchAndPreciseSearch | 精确搜索/模糊搜索无法同时支持:%s | 精确搜索/模糊搜索无法同时支持 |
| 400 | invalidState.openSearch.simultaneousFuzzySearchAndPreciseSearch | 精确搜索和模糊搜索无法同时支持:%s | 精确搜索和模糊搜索无法同时支持 |
| 400 | invalidState.permission.incorrectPermissionType | 权限类型不正确:%s | 权限类型不正确 |
| 400 | invalidState.permissionPackage.permissionPackageNotExist | 权限组不存在:%s | 权限组不存在 |
| 400 | invalidState.plugin.failedToExecute | 插件执行失败，请检查插件定义或联系管理员:%s | 插件执行失败，请检查插件定义或联系管理员 |
| 400 | invalidState.plugin.invalidFormat | 插件格式有误，请修正:%s | 插件格式有误，请修正 |
| 400 | invalidState.plugin.mutualDependencyInOutputField | 插件输出字段之间不能互相依赖:%s | 插件输出字段之间不能互相依赖 |
| 400 | invalidState.plugin.pluginOutputFieldShouldNotUseExpression | 表单中的某个插件输出字段不允许使用公式:%s | 表单中的某个插件输出字段不允许使用公式 |
| 400 | invalidState.process.circularProcessInvocationExist | 存在环路调用流程:%s | 存在环路调用流程 |
| 400 | invalidState.process.expectOnlyOneTask | 该实例下必须有且只有一个宜搭平台任务:%s | 该实例下必须有且只有一个宜搭平台任务 |
| 400 | invalidState.process.invalidFormEvent | 异常的流程事件绑定关系，请为流程正确配置触发事件:%s | 异常的流程事件绑定关系，请为流程正确配置触发事件 |
| 400 | invalidState.process.nameLengthExceed | 名称过长:%s | 名称过长 |
| 400 | invalidState.process.noAppropriateFormIsBoundToOriginalProcess | 原流程不存在表单绑定关系:%s | 原流程不存在表单绑定关系 |
| 400 | invalidState.process.processDefinitionNotExist | 原流程定义不存在:%s | 原流程定义不存在 |
| 400 | invalidState.process.processHasBeenEnabledOrDisabled | 流程已启用或者已禁用:%s | 流程已启用或者已禁用 |
| 400 | invalidState.process.processRequireAppropriateEvent | 流程未正确绑定触发事件:%s | 流程未正确绑定触发事件 |
| 400 | invalidState.process.targetActivityIsIllegal | 非法的跳转节点:%s | 非法的跳转节点 |
| 400 | invalidState.processConfig.processConfigIsWrong | 流程配置错误，请联系流程管理员:%s | 流程配置错误，请联系流程管理员 |
| 400 | invalidState.service.argumentsTypeNotFount | 找不到调用宜搭HSF接口的参数类型:%s | 找不到调用宜搭HSF接口的参数类型 |
| 400 | invalidState.service.improperServiceResultFormat | 服务返回结果格式不正确:%s | 服务返回结果格式不正确 |
| 400 | invalidState.serviceCallBack.serviceDataNotExist | 回调服务不存在:%s | 回调服务不存在 |
| 400 | invalidState.template.appTemplateNotExist | 应用模板不存在:%s | 应用模板不存在 |
| 400 | invalidState.template.templateDoesNotExist | 模板不存在:%s | 模板不存在 |
| 400 | invalidState.template.templateIsEmpty | 模板内容不能为空:%s | 模板内容不能为空 |
| 400 | invalidState.template.templateNameAlreadyExists | 模板名称已存在:%s | 模板名称已存在 |
| 400 | invalidSubDeptType | INVALID SUB DEPT TYPE | 部门下不能同时挂自定义部门和班级 |
| 400 | invalidSubDeptType | INVALID SUB\_DEPT TYPE | 部门下不能同时挂自定义部门和班级 |
| 400 | invalidSuiteKey | suitekey不合法 | suitekey不合法 |
| 400 | invalidSuiteKey | 无效的suiteKey | 无效的suiteKey |
| 400/500 | invalidSuiteTicket | suiteTicket无效 | suiteTicket无效 |
| 400 | invalidToken | 无效的token | 无效的token |
| 400 | invalidTriggerId | Invalid triggerId | 无效的触发器ID |
| 400 | invalidUser | INVALID\_USER | 无效用户 |
| 400 | invalidUser | 当前用户不在该组织下 | 当前用户不在该组织下 |
| 400 | invalidUser | 用户id不合法，不在对应企业中 | 用户id不合法，不在对应企业中 |
| 400 | invalidUserCorpRelation | 非法的用户和企业关系 | 非法的用户和企业关系 |
| 400 | invalidUserId | 授权预览审批附件，用户userId不能为空 | 授权预览审批附件，用户userId不能为空 |
| 400 | invalidUserId | 无效的userId | 无效的userId |
| 400 | invalidUserId | 无效的用户ID | 无效的用户ID；无效的用户id |
| 400 | invalidUserId | 无效的用户ID清单 | 无效的用户ID清单 |
| 400 | invalidUserId | 用户userId为空 | 用户userId为空 |
| 400 | invalidUserId | 获取审批钉盘空间信息，用户userId不能为空 | 获取审批钉盘空间信息，用户userId不能为空 |
| 400 | invalidUserId | 获取当前企业所有可管理的表单，要查询的用户userId不能为空 | 获取当前企业所有可管理的表单，要查询的用户userId不能为空 |
| 400 | invalidUserIds | 无效的用户ID清单 | 无效的用户ID清单 |
| 400 | invalidUserIds | 获取审批实例ID列表，发起userid列表参数非法，最大列表长度为10。 | 获取审批实例ID列表，发起userid列表参数非法，最大列表长度为10。 |
| 400 | invokeFrequency | 请求太频繁 | 请求太频繁 |
| 400 | invokeFrequentyly | 调用频繁 | 调用频繁 |
| 400 | ip.not.match | %s | IP不匹配，无权限使用此机器人发送消息 |
| 400 | ip.not.match | IP不匹配 | IP不匹配 |
| 400 | isDingAdminError | 判断钉钉管理员异常 | 判断钉钉管理员异常 |
| 400 | isNotWorkspace | %s | 不是知识库 |
| 400 | isvAppId.in.blackList | 当前isv应用appId已被加入黑名单，无法发起审批实例。 | 请确认该isv应用是否存在死循环等造成持续发起实例的情况。 |
| 400 | isvAuth.check.error | 当前isv没有该审批模板的操作权限，请检查企业是否授权了该审批模板给isv | 当前isv没有该审批模板的操作权限，请检查企业是否授权了该审批模板给isv |
| 400 | isvOrgId.in.blackList | 当前isv组织id已被加入黑名单，无法发起审批实例。 | 请确认该isv组织是否存在死循环等造成持续发起实例的情况。 |
| 400 | jsonData.empty | Invalid jsonData | 请求参数中的jsonData字段为空。 |
| 400 | keywords.not.match | %s | 机器人发送消息的关键词不匹配 |
| 400 | keywords.not.match | 关键词不匹配 | 关键词不匹配 |
| 400 | labelSizeBeyondLimit | 字段选项超过限制 | 字段选项超过限制 |
| 400 | leaveOpuserIdIsNotAdmin | 非管理员只能查询本人相关信息 | 非管理员只能查询本人相关信息 |
| 400 | leaveOrgIsUsed | 只允许企业接入使用 | 只允许企业接入使用 |
| 400 | leaveTypeNotFound | 未找到该假期类型 | 未找到该假期类型 |
| 400 | leaveUserIdListMax | 每次最多查询50条记录 | 每次最多查询50个员工userIds |
| 400 | lieuLeaveOnlyOne | 加班调休全局只能有一个 | 加班调休全局只能有一个 |
| 400 | lieuLeaveValidityIncorrect | 调休假有效期不正确 | 调休假有效期不正确 |
| 400 | link.params.missing | 链接消息参数缺失 | 链接消息参数缺失 |
| 400 | liveNotExist | this live not exist, please check liveId | 直播不存在，请检查直播ID |
| 400 | liveStatusNotMatch | this live status is not match, only forecast can update | 直播状态检查失败，预告态直播才允许修改 |
| 400 | lock.fail | 获取防并发锁失败 | 获取防并发锁失败 |
| 400 | mainApp.queryFailed | 主应用查询失败 | 主应用查询失败 |
| 400 | mainDeptIdInvalid | 传入主部门id有误 | 传入主部门id有误 |
| 400 | meetingRoomNotAvailable | forwardErrorMessage | 会议室已被占用 |
| 400 | meetingRoomNotAvailable | room busy | 会议室已被占用 |
| 400 | member.nonexist | 发送者不在群里，请检查 | 发送者不在群里，请检查 |
| 400 | member.nonexist | 找不到群成员，请检查 | 找不到群成员，请检查 |
| 400 | member.notEmpty | 添加的群成员列表不能为空，请检查 | 添加的群成员列表不能为空，请检查 |
| 400 | member.notEmpty | 移除的群成员列表不能为空，请检查 | 移除的群成员列表不能为空，请检查 |
| 400 | message.duplicate | 重复内容，发送失败 | 重复内容，发送失败 |
| 400 | message.not.empty | 指定消息内容不能为空 | 指定消息内容不能为空 |
| 400 | message.notSupportPhoto | 暂不支持发送图片 | 暂不支持发送图片 |
| 400 | miniAppId.illegal | appId对应插件不存在 | appId对应插件不存在 |
| 400 | miss.chatbotId | %s | 缺少robotCode |
| 400 | miss.openConversationId | %s | 缺少openConversationId |
| 400 | miss.openConversationId | 缺少openConversationId | 缺少openConversationId |
| 400 | miss.param.actionCard | %s | 消息内容不合法，需要actionCard属性 |
| 400 | miss.param.actionCard | 需要actionCard属性 | 需要actionCard属性 |
| 400 | miss.param.actionCardTobtns | %s | 消息内容不合法，需要actionCard-btns属性 |
| 400 | miss.param.actionCardTobtns | 需要actionCard-btns属性 | 需要actionCard-btns属性 |
| 400 | miss.param.actionCardTobtnsToactionUrl | %s | 消息内容不合法，需要actionCard-btns-actionURL属性 |
| 400 | miss.param.actionCardTobtnsToactionUrl | 需要actionCard-btns-actionURL属性 | 需要actionCard-btns-actionURL属性 |
| 400 | miss.param.actionCardTobtnsTotitle | %s | 消息内容不合法，需要actionCard-btns-title属性 |
| 400 | miss.param.actionCardTobtnsTotitle | 需要actionCard-btns-title属性 | 需要actionCard-btns-title属性 |
| 400 | miss.param.actionCardTosingleTitle | %s | 消息内容不合法，需要actionCard-singleTitle属性 |
| 400 | miss.param.actionCardTosingleTitle | 需要actionCard-singleTitle属性 | 需要actionCard-singleTitle属性 |
| 400 | miss.param.actionCardTosingleUrl | %s | 消息内容不合法，需要actionCard-singleURL属性 |
| 400 | miss.param.actionCardTosingleUrl | 需要actionCard-singleURL属性 | 需要actionCard-singleURL属性 |
| 400 | miss.param.actionCardTotext | %s | 消息内容不合法，需要actionCard-text属性 |
| 400 | miss.param.actionCardTotext | 需要actionCard-text属性 | 需要actionCard-text属性 |
| 400 | miss.param.actionCardTotitle | %s | 消息内容不合法，需要actionCard-title属性 |
| 400 | miss.param.actionCardTotitle | 需要actionCard-title属性 | 需要actionCard-title属性 |
| 400 | miss.param.audio | %s | 消息内容不合法，需要audio属性 |
| 400 | miss.param.beautifulCard | %s | 消息内容不合法，需要beautifulCard属性 |
| 400 | miss.param.beautifulCard | 需要beautifulCard属性 | 需要beautifulCard属性 |
| 400 | miss.param.beautifulCardToactionUrl | %s | 消息内容不合法，需要beautifulCard-actionUrl属性 |
| 400 | miss.param.beautifulCardToactionUrl | 需要beautifulCard-actionUrl属性 | 需要beautifulCard-actionUrl属性 |
| 400 | miss.param.beautifulCardToimage | %s | 消息内容不合法，需要beautifulCard-image属性 |
| 400 | miss.param.beautifulCardToimage | 需要beautifulCard-image属性 | 需要beautifulCard-image属性 |
| 400 | miss.param.beautifulCardTointroduction | %s | 消息内容不合法，需要beautifulCard-introduction属性 |
| 400 | miss.param.beautifulCardTointroduction | 需要beautifulCard-introduction属性 | 需要beautifulCard-introduction属性 |
| 400 | miss.param.beautifulCardTotitle | %s | 消息内容不合法，需要beautifulCard-title属性 |
| 400 | miss.param.beautifulCardTotitle | 需要beautifulCard-title属性 | 需要beautifulCard-title属性 |
| 400 | miss.param.contentOfText | %s | 消息内容不合法，需要text-content属性 |
| 400 | miss.param.contentOfText | 需要text-content属性 | 需要text-content属性 |
| 400 | miss.param.feedCard | %s | 消息内容不合法，需要feedCard属性 |
| 400 | miss.param.feedCard | 需要feedCard属性 | 需要feedCard属性 |
| 400 | miss.param.feedCardTolinks | %s | 消息内容不合法，需要feedCard-links属性 |
| 400 | miss.param.feedCardTolinks | 需要feedCard-links属性 | 需要feedCard-links属性 |
| 400 | miss.param.feedCardTolinksTomessageUrl | %s | 消息内容不合法，需要feedCard-links-messageURL属性 |
| 400 | miss.param.feedCardTolinksTomessageUrl | 需要feedCard-links-messageURL属性 | 需要feedCard-links-messageURL属性 |
| 400 | miss.param.feedCardTolinksTopicUrl | %s | 消息内容不合法，需要feedCard-links-picURL属性 |
| 400 | miss.param.feedCardTolinksTopicUrl | 需要feedCard-links-picURL属性 | 需要feedCard-links-picURL属性 |
| 400 | miss.param.feedCardTolinksTotitle | %s | 消息内容不合法，需要feedCard-links-title属性 |
| 400 | miss.param.feedCardTolinksTotitle | 需要feedCard-links-title属性 | 需要feedCard-links-title属性 |
| 400 | miss.param.file | %s | 消息内容不合法，需要file属性 |
| 400 | miss.param.image | %s | 消息内容不合法，需要image属性 |
| 400 | miss.param.image | 需要image属性 | 需要image属性 |
| 400 | miss.param.imageTopicUrl | %s | 消息内容不合法，需要image-picURL属性 |
| 400 | miss.param.imageTopicUrl | 需要image-picURL属性 | 需要image-picURL属性 |
| 400 | miss.param.link | %s | 消息内容不合法，需要link属性 |
| 400 | miss.param.link | 需要link属性 | 需要link属性 |
| 400 | miss.param.markdown | %s | 消息内容不合法，需要markdown属性 |
| 400 | miss.param.markdown | 需要markdown属性 | 需要markdown属性 |
| 400 | miss.param.markdownTotext | %s | 消息内容不合法，需要markdown-text属性 |
| 400 | miss.param.markdownTotext | 需要markdown-text属性 | 需要markdown-text属性 |
| 400 | miss.param.markdownTotitle | %s | 消息内容不合法，需要markdown-text属性 |
| 400 | miss.param.markdownTotitle | 需要markdown-text属性 | 需要markdown-text属性 |
| 400 | miss.param.messageUrlOfLink | %s | 消息内容不合法，需要link-messageUrl属性 |
| 400 | miss.param.messageUrlOfLink | 需要link-messageUrl属性 | 需要link-messageUrl属性 |
| 400 | miss.param.photo | %s | 消息内容不合法，需要photo属性 |
| 400 | miss.param.photo | 需要photo属性 | 需要photo属性 |
| 400 | miss.param.photoTophotoUrl | %s | 消息内容不合法，需要photo-photoURL属性 |
| 400 | miss.param.photoTophotoUrl | 需要photo-photoURL属性 | 需要photo-photoURL属性 |
| 400 | miss.param.text | %s | 消息内容不合法，需要text属性 |
| 400 | miss.param.text | 需要text属性 | 需要text属性 |
| 400 | miss.param.textOfLink | %s | 消息内容不合法，需要link-text属性 |
| 400 | miss.param.textOfLink | 需要link-text属性 | 需要link-text属性 |
| 400 | miss.param.titleOfLink | %s | 消息内容不合法，需要link-title属性 |
| 400 | miss.param.titleOfLink | 需要link-title属性 | 需要link-title属性 |
| 400 | miss.param.video | %s | 消息内容不合法，需要video-videoMediaId属性 |
| 400 | miss.staffId | miss.staffId %s | 无效的接收者id |
| 400 | missingParameter | 缺少必填参数 | 缺少必填参数 |
| 400 | missingParameter | 缺少必要参数 | 缺少必要参数 |
| 400 | missingParameter | 缺少必须参数 | 缺少必须参数 |
| 400 | missingRoomCode | missingRoomCode | 会议码缺失 |
| 400 | missingRoomId | MISSING ROOM ID | 会议id参数缺失 |
| 400 | mobileFormatError | mobileFormatError | 手机号格式错误 |
| 400 | model.exceed.error | 模型执行异常 | 大模型执行异常 |
| 400 | modifierUserId.not.exists | modifierUserId not exists | modifierUserId不是企业员工 |
| 400 | moneyNotConsist | 金额不一致 | 金额不一致 |
| 400 | moreThanMaxListSize | Exceeded the maximum number limit | 超出最大个数限制 |
| 400 | msgContent.error | 发送消息体参数错误 | 发送消息体参数错误 |
| 400 | name.invalid | Space name is invalid. | 空间名称非法 |
| 400 | nameAlreadyExists | 已存在相同假期名称 | 已存在相同假期名称 |
| 400 | nameTooLong | 假期名称过长 | 假期名称过长 |
| 400 | needAuth | NEED\_AUTH | 需要授权 |
| 400 | needAuth | 没有发起审批的权限 | 没有发起审批的权限 |
| 400 | needAuth | 没有同意拒绝审批的权限 | 没有同意拒绝审批的权限 |
| 400 | needAuth | 需要授权 | 需要授权 |
| 400 | needParameterNotPass | need parameter not pass. | 必传参数未传 |
| 400 | needParameterNotPass | need parameter, group name or owner or creator or template not pass. | 必传参数，群名称、群主、创建人或模板id参数未传 |
| 400 | needParameterNotPass | need parameter, groupset id not pass. | 必传参数，群组id未传 |
| 400 | no.application.authorization | 无应用间授权关系，无法进行该操作 | 无应用间授权关系，无法进行该操作 |
| 400 | no.field.permission | %s | 没有指定字段的编辑权限 |
| 400 | no.file | 抱歉，该对象不存在或已被删除，无法评论 | 抱歉，该对象不存在或已被删除，无法评论 |
| 400 | no.permission | %s | 无权限 |
| 400/403 | no.permission | No Permission | 无权限；无查询权限 |
| 400/500 | no.priviledge | You are not authorized to perform this operation. | 你没有权限进行此操作 |
| 400 | no.smart.permission | No Smart Room Permission | 未购买高级版无法使用 |
| 400 | no.valid.parameter | no valid parameter, can not update | 没有传入有效参数，禁止更新 |
| 400 | noAppManagePermission | 当前企业没有操作应用的权限 | 当前企业没有操作应用的权限 |
| 400 | noAppManagePermission | 没有操作应用的权限 | 没有操作应用的权限 |
| 400 | noAuthority | 无权限调用 | 无权限调用 |
| 400 | noAuthority | 未授权 | 未授权 |
| 400 | noFieldModifyPermission | 没有字段修改权限 | isv没有字段修改权限 |
| 400 | non.open.customer | draw or assign is not allowed for non-open-customer | 该实例非公海客户，不允许操作 |
| 400 | noPermission | NO\_PERMISSION | 没有创建权限；没有权限 |
| 400/404 | noPermission | lippi\_live.stream.noPermission | 鉴权失败，请检查publicType字段是否为全域公开,若全域公开需要升级直播权益；；鉴权失败 |
| 400/403 | noPermission | noPermission | 无操作权限；无操作权限；无权限 |
| 400 | noPermission | 无权访问，企业没有开通相应的微应用 | 无权访问，企业没有开通相应的微应用 |
| 400 | noPermission | 无权限访问 | 无权限访问 |
| 400 | noPermission | 无访问权限 | 无访问权限 |
| 400 | noPermission | 没有权限访问当前表单 | 权限校验失败 |
| 400 | noPermission.access.accessDeny | 暂无访问权限，应用管理员关闭了「家校通讯录」成员访问，如需访问请联系管理员开启。:%s | 暂无访问权限，应用管理员关闭了「家校通讯录」成员访问，如需访问请联系管理员开启。 |
| 400 | noPermission.access.illegalIp | 非法的IP地址访问:%s | 非法的IP地址访问 |
| 400 | noPermission.form.deleteApprovalConditionComponentsWasNotAllowed | 不允许删除作为条件审批的组件(包含已失效条件):%s | 不允许删除作为条件审批的组件(包含已失效条件) |
| 400 | noPermission.form.systemNavigationCanNotDelete | 系统导航不允许删除:%s | 系统导航不允许删除 |
| 400/500 | noPermission.permission.deny | 没有权限:%s | 没有权限 |
| 400 | noPermission.process.onlyCurrentApproverCanReturnProcessInstance | 不是流程当前审批人，不能执行退回:%s | 不是流程当前审批人，不能执行退回 |
| 400 | noPermission.process.onlyRunningTasksCanBeAppended | 非运行状态的流程无法加签:%s | 非运行状态的流程无法加签 |
| 400 | noPermission.process.onlyRunningTasksCanBeRedirected | 非运行状态的流程无法转交:%s | 非运行状态的流程无法转交 |
| 400 | noPermission.submit.deny | 您现在正在预览应用，无法操作提交动作。:%s | 您现在正在预览应用，无法操作提交动作。 |
| 400 | noPermission.to.setField | %s | 没有设置字段的权限 |
| 400 | noPermission.to.update | no permission to update this customer | 没有更新此数据的权限 |
| 400 | noRight | NO RIGHT | 当前用户没有操作权限 |
| 400 | noRight | NO\_RIGHT | 没有权限 |
| 400 | not.allowed.robotCode | %s | 待撤回的消息不是robotCode对应的机器人发出的，无权限撤回消息，请传入正确的robotCode；未被授权的robotCode |
| 400 | not.found | %s | 群聊不存在，请检查openConversationId是否正确 |
| 400 | not.inner.group | 当前群不是内部群 | 当前群不是内部群 |
| 400 | not.main.administrator | 不是主管理员(创建者) | 不是主管理员(创建者) |
| 400 | notCorpStaff | 非企业内部员工 | 非企业内部员工 |
| 400 | notCorpStaff | 非企业员工 | 非企业员工 |
| 400 | notEmptyParameter | 缺失必填的参数 | 缺失必填的参数 |
| 400 | notFixedItemExtendParamError | 非固定规格扩展参数异常 | 非固定规格扩展参数异常 |
| 400 | notFixedItemInvalidPrice | 内购商品非固定规格传入价格异常 | 内购商品非固定规格传入价格异常 |
| 400 | notFixedItemNoPrice | 内购商品非固定规格未传入价格 | 内购商品非固定规格未传入价格 |
| 400 | notFound | 未找到该假期类型 | 未找到该假期类型 |
| 400 | notFound | 未查询到指定数据%s | 未查询到指定数据%s |
| 400 | noticerOverLimit | 抄送人数量超过限制 | 抄送人数量超过限制 |
| 400 | notInEvent | 用户不在日程内 | 用户不在日程内 |
| 400 | notManage | 部门的管理员不存在 | 部门的管理员不存在 |
| 400 | notOaAdmin | 无权限操作，操作人必须为OA审批管理员 | 请检查opUserId，操作人必须为OA审批管理员 |
| 400 | notPermission | 无访问权限 | 无访问权限 |
| 400 | notRevoke.all.messages | %s | 消息未能全部撤回 |
| 400 | notSupportedFilterType | %s | 不支持的查询类型 |
| 400 | notUpdateType | 假期业务类型不能修改 | 假期业务类型不能修改 |
| 400 | noUserAuth | 当前用户无操作应用的权限 | 当前用户无操作应用的权限 |
| 400 | num.over.limit | Number Over Limit | 会议室权益可用额度不足 |
| 400 | oaplus.params.error | 参数校验不合法，请检查 | 参数校验不合法，请检查 |
| 400/500 | oaplus.query.limit | 请求过于频繁，稍后重试 | 企业访问并发超过限制；接口访问并发超过限制；请求过于频繁，稍后重试 |
| 400 | objective.rule.notExist | 考核规则不存在 | 考核规则不存在 |
| 400 | only.groupAdmin.canAtAll | 仅群主可@所有人 | 仅群主可@所有人 |
| 400 | open.topbox.failed | 开启吊顶失败 | 开启吊顶失败 |
| 400 | openConversationId.decryptFailed | openConversationId解密错误 | openConversationId解密错误 |
| 400 | openConversationId.empty | 会话id为空 | 会话id为空 |
| 400 | openConversationId.notExisted | openConversationId不能和token同时为空 | openConversationId不能和token同时为空 |
| 400 | openConversationId.notExisted | openConversationId为空 | openConversationId为空 |
| 400 | openConversationIdDecriptFailed | 群 ID 解码失败 | 群 ID 解码失败 |
| 400 | openConversationIds.error | openConversationIds中存在错误或失效群 | openConversationIds中存在错误或失效群 |
| 400 | openIsvExist | %s | 已初始化，请勿重复调用 |
| 400 | openIsvNotInit | 未初始化，请初始化后调用 | 未初始化，请初始化后调用 |
| 400 | openTopbox.failed | 开启吊顶失败 | 开启吊顶失败 |
| 400 | operationConcurrentControl | %s | 并发控制；稍后重试 |
| 400/403 | operationNotSupported | %s | 文件不支持下载；不支持删除到回收站 |
| 400 | operatorUserId.not.exist | operatorUserId not exist | 操作者不存在 |
| 400 | order.not.exist | 订单不存在 | 订单不存在 |
| 400 | org.no.function | 企业未开启相关功能 | 企业未开启相关功能 |
| 400 | org.not.exist | org not exist | 当前企业在Teambition中不存在；当前企业在Teambition中不存在。；当前企业在快办中不存在。 |
| 400 | org.not.exist | org.not.exist | 当前企业在Teambition中不存在 |
| 400 | org.not.exists | org not exists | 组织不存在或已解散 |
| 400 | org.not.found | Org Not Found | 企业找不到 |
| 400 | org.not.match | 群的归属组织与操作传入组织不匹配 | 群的归属组织与操作传入组织不匹配 |
| 400 | org.notOwn.group | 单聊会话不属于当前企业 | 单聊会话不属于当前企业 |
| 400 | org.notOwn.group | 群不属于当前企业 | 群不属于当前企业 |
| 400 | orgAccessForbidden | orgAccessForbidden | 组织访问受限 |
| 400 | organization.not.found | 当前组织不存在 | 当前组织不存在 |
| 400 | organization.not.found | 组织不存在 | 组织不存在 |
| 400 | orgInvalid.param.error | %s | 组织非百姓通组织 |
| 400 | orgNoAdmin | 数据异常,企业无管理员 | 数据异常,企业无管理员 |
| 400 | orgNotAuthApp | 企业未授权开通应用 | 企业未授权开通应用 |
| 400 | orgNotAuthed | 企业未完成高级认证 | 企业未完成高级认证 |
| 400 | orgNotExist | ORG\_NOT\_EXIST | 高校组织不存在 |
| 400 | orgNotExist | 企业已解散 | 企业已解散 |
| 400 | orgNotRealname | %s | 企业在e签宝未实名，请先在e签宝微应用内进行实名 |
| 400 | orgQuotaInsufficient | %s | 企业容量不足 |
| 400 | orgSuiteAuthNotExit | access forbidden | 组织无权限访问 |
| 400 | orgUpgradeNotSuccess | ORG\_UPGRADE\_NOT\_SUCCESS | 该组织未完成高校通讯录转换 |
| 400 | outTrackId.empty | 唯一标识一张卡片的外部ID(outTrackId)为空 | 唯一标识一张卡片的外部ID(outTrackId)为空 |
| 400 | outTrackId.exceed.limit | outTrackId长度超限 | outTrackId长度超限 |
| 400 | outTrackId.outOfLimit | outTrackId不要超过64个字符 | outTrackId不要超过64个字符 |
| 400 | outTrackIdLengthLimited | 超过卡片业务标识信息长度 | 超过卡片业务标识信息长度 |
| 400 | overMaxCount | 超过最大可创建应用数 | 超过最大可创建应用数 |
| 400 | overQuota | over quota. | 超过限制 |
| 400 | overtimeDurationTooLong | 加班时长过长 | 加班时长过长 |
| 400 | ownerCantBeManager | 群主不能是群管理员 | 群主不能是群管理员 |
| 400 | pageIndex.invalid | illegal nextToken | 游标错误 |
| 400 | pageIndex.invalid | illegal pageIndex | 游标错误 |
| 400 | pageIndexIllegal | 分页参数错误 | 分页参数从0开始非负整数 |
| 400 | pageSize.exceeds | pageSize must not exceeds 100 | 每页不能超过100条数据 |
| 400 | pageSize.invalid | illegal pageSize | 分页大小错误 |
| 400 | pageSizeIllegal | 分页大小超过限制 | 分页大小最大200条 |
| 400 | paging.parameter.error | 分页参数错误 | 分页参数错误 |
| 400 | param.blank | %s参数不能为空 | toUserId参数不能为空；请参照接口文档检查必填项taskId、processInstanceId、operateUserId、appenderUserIds、activateType、type；请参照接口文档检查必填项taskId、processInstanceId、operateUserId、targetActivityId、revertAction、targetActivityActioners等 |
| 400 | param.blank | 没有传递必传参数 | 没有传递必传参数 |
| 400 | param.callbackRouteKeyEmpty | param.callbackRouteKeyEmpty | 回调 RouteKey 为空 |
| 400 | param.callbackUrlEmpty | param.callbackUrlEmpty | 回调 Url 为空 |
| 400 | param.cardAlreadyExist | param.cardAlreadyExist | 卡片已经存在 |
| 400 | param.cardDataAndPrivateDataBothEmpty | param.cardDataAndPrivateDataBothEmpty | cardData 和 privateData 同时为空 |
| 400 | param.cardNotExist | param.cardNotExist | 卡片不存在 |
| 400 | param.cardPublicDataEmpty | param.cardPublicDataEmpty | 卡片公共数据为空 |
| 400 | param.cardTemplateIdEmpty | param.cardTemplateIdEmpty | 卡片模板 Id 为空；卡片模板Id为空 |
| 400 | param.code.error | %s | 表单模板查询错误 |
| 400 | param.contentUnsafe | param.contentUnsafe | 卡片数据不能通过安全审查 |
| 400 | param.conversationIdInvalid | param.openConversationIdInvalid | openConversationId不符合规范 |
| 400 | param.dynamicDataMappingEmpty | param.dynamicDataMappingEmpty | 动态数据源数据映射为空 |
| 400 | param.dynamicDataMappingPathEmpty | param.dynamicDataMappingPathEmpty | 动态数据源数据映射路径为空 |
| 400 | param.dynamicDataPullConfigEmpty | param.dynamicDataPullConfigEmpty | 动态数据源拉取配置为空 |
| 400 | param.dynamicDataPullIntervalInvalid | param.dynamicDataPullIntervalInvalid | 动态数据源拉取间隔时间为空或非法 |
| 400 | param.dynamicDataPullIntervalTimeUnitInvalid | param.dynamicDataPullIntervalTimeUnitInvalid | 动态数据源拉取间隔时间单位为空或非法 |
| 400 | param.dynamicDataSourcePullStrategyEmpty | param.dynamicDataSourcePullStrategyEmpty | 动态数据源拉取策略为空 |
| 400 | param.dynamicDataValueTypeEmpty | param.dynamicDataValueTypeEmpty | 动态数据源数据类型为空 |
| 400 | param.dynamicSourceIdEmpty | param.dynamicSourceIdEmpty | 动态数据源配置 ID 为空；动态数据源配置ID为空 |
| 400 | param.empty | param.empty | 入参为空；参数为空 |
| 400 | param.empty | 入参为空 | 入参为空 |
| 400 | param.empty | 请求参数为空 | 请求参数为空 |
| 400 | param.emptyAppendSpaces | param.emptyAppendSpaces | appendSpaces为空 |
| 400/500 | param.error | %s | 参数错误 |
| 400 | param.error | Error:%s | 请求参数错误。例如，Error:roomStatus invalid；请求参数错误。例如：Error:lack authorizedMembers |
| 400 | param.error | Invalid Param | 参数错误 |
| 400 | param.error | Param Error | 参数缺失错误；参数错误；operatorUnionId参数为空 |
| 400 | param.error | missing.user.info | 查询人缺失 |
| 400 | param.error | param.error | 参数错误；查询人unionId错误 |
| 400 | param.error | 参数无效 | 参数无效 |
| 400 | param.error | 参数错误 | 参数错误，请确认必填参数是否遗漏，nextGmtCreate与nextBizId必须配合使用 |
| 400 | param.error | 参数非法 | 参数非法 |
| 400 | param.error.maxresults | Too Large MaxResults | MaxResults过大 |
| 400 | param.format.error | 参数格式错误 | 参数格式错误 |
| 400 | param.format.error | 参数格式错误，请检查Mac地址 | 一般为mac地址格式问题 |
| 400 | param.illegal | %s | 参数不合法，如requestIds不合法、status不合法；参数不合法，请确认userId和platform是否正确 |
| 400 | param.illegal | 不合法的参数%s | 不合法的参数taskId |
| 400 | param.illegal | 参数不合法 | 参数不合法；参数不合法，请确认分页参数是否正确。 |
| 400 | param.illegal | 参数不合法，请确认parentId是否正确 | 参数不合法，请确认parentId是否正确 |
| 400 | param.illegal | 参数错误 | 参数错误；接口参数错误 |
| 400/500 | param.illegal | 参数错误：%s | 接口参数错误；参数错误，包含agentId、pushType、userIdList、pushValue |
| 400 | param.illegal | 请求参数无效 | 请求参数无效 |
| 400 | param.illegal.operator | 不合法的参数operateUserId | 不合法的参数operateUserId |
| 400 | param.illegal.operator | 操作人的userId必须为当前任务的审批人 | 请检查operateUserId参数；请检查operatorId参数 |
| 400/401 | param.invalid | %s | Mac地址有误，请确认地址格式，且不能重复添加；参数不合法；参数不合法，操作列表长度不能大于500；Mac地址有误，请确认地址格式，且不能重复添加 |
| 400 | param.invalid | param.invalid | 存在非法参数 |
| 400 | param.invalid | 参数不合法 | 参数不合法 |
| 400 | param.invalid | 参数错误:%s | 参数不合法,包含platform、type、pageSize、pageNumber... |
| 400 | param.invalid | 无效参数 | 无效参数 |
| 400 | param.invalid | 请求参数无效 | 请求参数无效 |
| 400 | param.isNotJson | 参数必须是json | 参数必须是json |
| 400 | param.length.exceed | %s | 参数requestIds长度超出限制 |
| 400 | param.manager.notexist | 查询的managerUserId不存在 | 查询的managerUserId无管理权限 |
| 400 | param.manager.notexist | 查询的mangerUserId不存在 | 查询的mangerUserId无管理权限 |
| 400 | param.missing | 参数不合法 | 参数不合法 |
| 400 | param.missing | 参数不合法，Mac地址和did必填一项 | Mac地址和did均缺失时报错 |
| 400 | param.missing | 参数不能为空 | 参数不能为空 |
| 400 | param.not.found | 参数不能为空 | 参数不能为空 |
| 400 | param.null | 参数不能为空 | 参数不能为空 |
| 400 | param.openDeliverModelEmpty | param.openDeliverModelEmpty | 场域投放模型为空 |
| 400 | param.openDeliverModelError | param.openDeliverModelError | 场域投放模型格式错误 |
| 400 | param.openSpaceIdEmpty | param.openSpaceIdEmpty | 投放openSpaceId为空 |
| 400 | param.openSpaceModelInvalid | param.openSpaceModelInvalid | 错误的场域属性模型 |
| 400 | param.openSpaceModelInvalid | param.openSpaceModellnvalid | 错误的场域属性模型 |
| 400 | param.outTrackIdEmpty | param.outTrackIdEmpty | 业务标识 outTrackId 为空；业务标识outTrackId为空 |
| 400 | param.spaceDeliverModelEmpty | param.spaceDeliverModelError | 场域投放模型格式错误 |
| 400 | param.stream.content | content is too large | 200092 |
| 400 | param.stream.contentEmpty | param.stream.contentEmpty | streaming更新content为空 |
| 400 | param.stream.guidEmpty | param.stream.guidEmpty | streaming更新guid为空 |
| 400 | param.stream.isFull | streaming update the parameter isFull is null | isFull字段为空 |
| 400 | param.stream.keyEmpty | param.stream.keyEmpty | streaming更新key为空 |
| 400 | param.stream.outTrackId | card is not exist | 卡片不存在 |
| 400 | param.templateNotExist | param.templateNotExist | 模板不存在 |
| 400 | param.templateUnpublished | param.templateUnpublished | 模板未发布 |
| 400 | param.user.notexist | 查询的staffId不存在 | 查询的userId在当前组织不存在 |
| 400 | param.user.notexist | 查询的userId不存在 | 查询的userId在当前组织不存在 |
| 400 | param.userIdEmpty | param.userIdEmpty | 用户 userId 为空；用户userId为空 |
| 400/500 | param.userIdNotExist | param.userIdNotExist | 用户 userId 不存在；用户user不存在；用户 userId 不存在 |
| 400 | paramBlank | 请求参数为空 | 请求参数为空 |
| 400 | paramError | %s | 参数错误 |
| 400 | paramError | PARAM ERROR | 参数错误 |
| 400 | paramError | paramError | 参数错误；参数错误，请检查入参 |
| 400 | paramError-keyword | %s | 参数错误-keyword |
| 400 | paramError.conflictStrategy | %s | 参数错误-conflictStrategy |
| 400 | paramError.contactId | 联系人员工编号填写错误 | 联系人员工编号填写错误 |
| 400 | paramError.contactsId | 当前联系人信息输入错误，请确认后再操作 | 当前联系人信息输入错误，请确认后再操作 |
| 400 | paramError.conversationId | %s | 参数错误-conversationId |
| 400 | paramError.corpId | 获取到的企业编号不能为空 | 获取到的企业编号不能为空 |
| 400 | paramError.createTimeRange | %s | 参数错误-createTimeRange |
| 400 | paramError.dentryCategories | %s | 参数错误-dentryCategories |
| 400 | paramError.dentryId | %s | 参数错误-dentryId |
| 400 | paramError.dentryIds | %s | 参数错误-dentryIds |
| 400 | paramError.dentryTypes | %s | 参数错误-dentryTypes |
| 400 | paramError.dentryUuid | %s | 参数错误-dentryUuid |
| 400 | paramError.description | %s | 参数错误-description |
| 400 | paramError.im | 审核的时候可见字段必须填写 | 审核的时候可见字段必须填写 |
| 400 | paramError.maxResults | %s | 参数错误-maxResults |
| 400 | paramError.modifiedTimeRange | %s | 参数错误-modifiedTimeRange |
| 400 | paramError.multipart | %s | 参数错误-multipart |
| 400 | paramError.name | %s | 参数错误-name |
| 400 | paramError.openType | %s | 参数错误-openType |
| 400 | paramError.orderBy | %s | 参数错误-orderBy |
| 400 | paramError.pageSize | 当前搜索pageSize数据大于默认值20 | 当前搜索pageSize数据大于默认值20 |
| 400 | paramError.pageSize | 搜索接口的分页数pageSize必须传递 | 搜索接口的分页数pageSize必须传递 |
| 400 | paramError.parentDentryUuid | %s | 参数错误-parentDentryUuid |
| 400 | paramError.parentId | %s | 参数错误-parentId |
| 400 | paramError.partNumbers | %s | 参数错误-partNumbers |
| 400 | paramError.permissionInheritance | %s | 参数错误-permissionInheritance |
| 400 | paramError.permissionMemberType | %s | 参数错误-permissionMemberType |
| 400 | paramError.protocol | %s | 参数错误-protocol |
| 400 | paramError.recycleBinId | %s | 参数错误-recycleBinId |
| 400 | paramError.recycleBinScope | %s | 参数错误-recycleBinScope |
| 400 | paramError.recycleItemId | %s | 参数错误-recycleItemId |
| 400 | paramError.recycleItemIds | %s | 参数错误-recycleItemIds |
| 400 | paramError.request | 请求的入参信息不能为空 | 请求的入参信息不能为空 |
| 400 | paramError.request | 请求的参数信息不能为空 | 请求的参数信息不能为空 |
| 400 | paramError.risk | 当前编辑内容安全审核未通过,存在风险词语 | 当前编辑内容安全审核未通过,存在风险词语 |
| 400 | paramError.roleId | %s | 参数错误-roleId |
| 400 | paramError.scene | %s | 参数错误-scene |
| 400 | paramError.sceneId | %s | 参数错误-sceneId |
| 400 | paramError.scope | %s | 参数错误-scope |
| 400 | paramError.scopeId | %s | 参数错误-scopeId |
| 400 | paramError.searchScopes | %s | 参数错误-searchScopes |
| 400 | paramError.searchTargets | %s | 参数错误-searchTargets |
| 400 | paramError.spaceId | %s | 参数错误-spaceId |
| 400 | paramError.status | 审核的状态必须填写 | 审核的状态必须填写 |
| 400 | paramError.status | 当前审核的词条不是待审核词条，请确认后再操作 | 当前审核的词条不是待审核词条，请确认后再操作 |
| 400 | paramError.storageDriver | %s | 参数错误-storageDriver |
| 400 | paramError.targetFolderId | %s | 参数错误-targetFolderId |
| 400 | paramError.targetSpaceId | %s | 参数错误-targetSpaceId |
| 400 | paramError.taskId | %s | 参数错误-taskId |
| 400 | paramError.uploadKey | %s | 参数错误-uploadKey |
| 400 | paramError.userId | 当前操作人员不是管理员,只有管理员可以进行该操作 | 当前操作人员不是管理员,只有管理员可以进行该操作 |
| 400 | paramError.userId | 操作员工编号userId不能为空 | 操作员工编号userId不能为空 |
| 400 | paramError.userId | 操作员工编号userId填写错误未找到对应员工信息 | 操作员工编号userId填写错误未找到对应员工信息 |
| 400 | paramError.userId | 操作员工编号useruserIdid不能为空 | 操作员工编号userId不能为空 |
| 400 | paramError.uuid | 当前词条不存在，请确认uuid后再操作 | 当前词条不存在，请确认uuid后再操作 |
| 400 | paramError.uuid | 当前词条不存在，请确认后uuid后再操作 | 当前词条不存在，请确认后uuid后再操作 |
| 400 | paramError.uuid | 查询操作主键uuid不能为空 | 查询操作主键uuid不能为空 |
| 400 | paramError.uuid | 词条操作主键uuid不能为空 | 词条操作主键uuid不能为空 |
| 400 | paramError.uuid | 词条操作主键不能为空 | 词条操作主键不能为空 |
| 400 | paramError.visitTimeRange | %s | 参数错误-visitTimeRange |
| 400 | paramError.wordParaphrase | 释义信息不能为空 | 释义信息不能为空 |
| 400 | parameter.blank | 参数为空 | 参数为空；非法的系统参数 |
| 400 | parameter.error | 单次操作不能超过10个 | 单次操作不能超过10个 |
| 400 | parameter.error | 参数不合法，请确认关联关系 | 参数不合法，请确认关联关系 |
| 400 | parameter.error | 参数错误 | settingId参数错误；参数错误 |
| 400 | parameter.error | 归属企业不存在 | 归属企业不存在 |
| 400 | parameter.error | 所传组织非上下游组织或者上下游组织不归属于所选组织 | 所传组织非上下游组织或者上下游组织不归属于所选组织 |
| 400 | parameter.error | 流程中心配置参数错误：%s | 流程中心配置参数错误 |
| 400 | parameter.invalid | PARAMETER\_INVALID | 参数异常 |
| 400 | parameter.invalid | 参数错误 | 参数漏填或者格式错误；参数错误 |
| 400 | parameterErrror | PARAMETER\_ERROR | 参数异常 |
| 400 | paramIllegal | PARAM ILLEGAL | 参数异常 |
| 400 | paramIllegal | paramIllegal | 参数错误，请检查 |
| 400 | paramIllegal | 参数错误 | 参数错误 |
| 400 | paramIllegal | 参数非法 | 参数非法 |
| 400 | paramIllegal | 请求参数非法 | 请求参数非法 |
| 400 | paramInvalid | 参数错误 | labels太多或者modifyType不对 |
| 400/500 | params.error | error:%s | 参数错误；未找到会议 |
| 400 | paramsError | error:%s | 参数错误；参数错误，用户unionId错误；参数错误，缺失会议id；参数错误，请检查入参 |
| 400 | paramsError | paramsError | 参数错误，请检查入参 |
| 400 | paramsTitleError | error:%s | 会议标题非法 |
| 400 | paramterInvalid | 参数错误 | opUserId和userId参数不能为空 |
| 400 | parentDeptInvalid | PARENT\_DEPT\_INVALID | 父组织单元不合理 |
| 400 | parentDeptNotExist | PARENT\_DEPT\_NOT\_EXIST | 父组织单元不存在 |
| 400 | permission.checkFailed | 发送动态卡片权限校验失败 | 发送动态卡片权限校验失败 |
| 400 | permission.coolApp.checkFailed | 无权限，酷应用不属于当前token对应的应用名下 | 无权限，酷应用不属于当前token对应的应用名下 |
| 400 | permission.denied | 没有权限获取企业认证信息 | 企业没有向自建应用授权时报错 |
| 400 | permission.error | %s | 没有访问权限 |
| 400 | permission.error | no permission | 没有权限；没有访问权限 |
| 400 | permission.error | 无操作审批流的权限，请检查审批实例或者模板是否正确 | 无操作审批流的权限，请检查审批实例或者模板是否正确 |
| 400 | permission.error | 没有审批流操作权限 | 没有审批流操作权限 |
| 400 | permission.error | 没有访问权限 | 没有访问权限 |
| 400 | permission.sceneGroup.checkFailed | 无权限，该群安装的群模板不属于当前token对应的应用名下 | 无权限，该群安装的群模板不属于当前token对应的应用名下 |
| 400/403/500/502 | permissionDenied | %s | 无权限；无权限获取缩略图；当前用户无此操作权限；无权限；用户缺少上传文件的权限；用户缺少下载文件的权限；用户缺少修改文件(夹)属性的权限；用户缺少创建空间的权限；用户缺少删除文件(夹)的权限；用户缺少对回收项原文件(夹)的查看权限；用户缺少对回收项原文件(夹)的管理权限；用户缺少待发送文件的拷贝权限或者用户缺少目标会话存储空间添加文件的权限；用户缺少拷贝文件(夹)的权限；用户缺少授权的权限；用户缺少添加文件夹的权限；用户缺少目标会话存储空间添加文件的权限；用户缺少移动文件(夹)的权限；用户缺少获取IM会话存储空间的权限；用户缺少获取企业信息的权限；用户缺少获取应用信息的权限；用户缺少获取文件(夹)信息的权限；用户缺少获取文件列表的权限；用户缺少获取权限列表的权限；用户缺少获取空间信息的权限；用户缺少订阅事件的权限；用户缺少读取文件的权限；用户缺少重命名文件(夹)的权限；无复制权限；无权限 |
| 400 | permissionDenied | Request user has no permission to launch check in | 当前用户无操作权限 |
| 400 | permissionDenied | Request user has no permission to launch sign out | 当前用户无操作权限 |
| 400 | permissionDenied | 用户不在订阅范围 | 用户不在订阅范围 |
| 400 | permissionDeny | permissionDeny | 用户不在授权范围内 |
| 400/404 | permissionError | permissionError:%s | 无权操作该会议；群权限限制 |
| 400 | permissionInheritanceUnsupportedForRootDentry | %s | 根目录不支持权限继承 |
| 400 | phoneding.reachlimit | 电话DING发送已达上限 | 电话DING发送已达上限 |
| 400 | picture.format.error | Picture Format Error | 图片格式错误 |
| 400 | point.system.error | 积分服务请求失败 %s | 积分服务请求失败 |
| 400 | positioinAgainstConstraint | 职位和主部门违反绑定约束 | 职位和主部门违反绑定约束 |
| 400 | positionIdInvalid | 职位id不合法 | 职位id不合法 |
| 400 | preCheckError | 前置校验失败: %s | 前置校验失败 |
| 400 | privatefile.not.exist | 专属存储文件不存在 | 专属存储文件不存在 |
| 400 | process.code.error | 获取审批模板失败或审批模板已被删除 | 获取审批模板失败或审批模板已被删除 |
| 400 | process.error | 审批流不存在 | 审批流不存在 |
| 400 | process.error | 模板不存在 | 模板不存在 |
| 400 | process.inst.notExist | 审批单不存在或已删除 | 审批单不存在或已删除 |
| 400 | process.not.exist | 审批流不存在 | 审批流不存在 |
| 400 | process.status.error | 审批单状态异常为非启用状态，不允许更新审批 | 审批单状态异常为非启用状态，不允许更新审批 |
| 400 | processCode.error | processCode query error | 模板编码查询错误 |
| 400 | processcode.error | processCode对应的审批流程不存在 | processCode对应的审批流程不存在 |
| 400 | processcode.error | processCode对应的表单不存在 | processCode对应的表单不存在 |
| 400 | processCode.in.blackList | 当前模板code已被加入黑名单，无法发起审批实例。 | 请确认该模板是否存在死循环等造成持续发起实例的情况。 |
| 400 | processCodeError | 获取审批模板失败或模板已删除 | 获取审批模板失败或模板已删除 |
| 400 | processCodeError | 获取审批模板失败或者模板已被删除 | 获取审批模板失败或者模板已被删除 |
| 400 | processes.error | 审批流已超过最大数量 | 审批流已超过最大数量 |
| 400 | processes.error | 获取模板列表失败 | 获取模板列表失败 |
| 400 | processFormDataIsNull | 流程表单数据为空 | 流程表单数据为空 |
| 400 | processGetFailed | 获取审批流失败 | 获取审批流失败 |
| 400 | processGetFailed | 获取审批流失败或审批单状态为非启用状态 | 获取审批流失败或审批单状态为非启用状态 |
| 400 | processGetFailedByParameter | 无操作审批流的权限，请检查审批实例或者模板是否正确 | 无操作审批流的权限，请检查审批实例或者模板是否正确 |
| 400 | processGroupGetFailed | 获取审批流分组失败 | 获取审批流分组失败 |
| 400 | processInstanceIdError | processInstanceId参数无效 | processInstanceId参数无效 |
| 400 | processInstanceInvalidParameter | 审批实例参数错误 | 审批实例参数错误 |
| 400 | processInstanceInvalidParameter | 审批实例参数错误，具体可能为:发起人、审批人、抄送人的userid错误，发起部门id错误，发起人不在发起部门中 | 审批实例参数错误，具体可能为:发起人、审批人、抄送人的userid错误，发起部门id错误，发起人不在发起部门中 |
| 400 | processInstanceNotExist | 审批实例不存在 | 审批实例不存在；请检查processInstanceId参数传值是否正确 |
| 400 | processInstNotExist | 审批实例不存在 | 审批实例不存在 |
| 400 | processNotExist | 审批模板不存在 | 请检查processCode参数传值是否正确 |
| 400 | processNotExist | 审批流不存在 | 审批流不存在 |
| 400/503 | processQueryKey.expireTime | %s | processQueryKey还未生成消息查询数据或已过期，无法查询消息 |
| 400 | processQueryKey.expireTime | processQueryKey还未生成消息查询数据或已过期 | processQueryKey还未生成消息查询数据或已过期，无法查询消息 |
| 400 | processSetupNoPermission | 无操作审批流的权限 | 无操作审批流的权限 |
| 400 | profile.not.exist | 账号不存在 | 账号不存在 |
| 400 | publisher.not.exist | 推送号不存在 | 推送号不存在 |
| 400 | publisher.notexist | 服务号不存在 | 服务号不存在 |
| 400 | qps.exceed.limit | 请求过于频繁 | 超过调用并发上限 |
| 400 | queryCard.failed | 查询卡片失败 | 查询卡片失败 |
| 400 | queryChatbot.wrong | 查询机器人失败 | 查询机器人失败 |
| 400 | queryDsl.invalid.json | queryDsl is not json format | queryDsl不是有效的JSON字符串 |
| 400 | queryDsl.json.error | queryDsl is not valid json | queryDsl格式不正确 |
| 400 | queryEmployInfoFailed | 查询企业员工信息失败 | 查询企业员工信息失败 |
| 400 | queryFlowDetailError | 查询流程详情异常 | 查询流程详情异常 |
| 400 | queryFlowDocInfoError | 查询流程文档信息详情异常 | 查询流程文档信息详情异常 |
| 400 | queryFlowError | 查询流程详情异常 | 查询流程详情异常 |
| 400 | queryFlowSignersError | 查询流程签署人信息异常 | 查询流程签署人信息异常 |
| 400 | quota.insufficient | Remain quota is insufficient. | 剩余容量不足 |
| 400 | ranIdInvalid | 职级id不合法 | 职级id不合法 |
| 400 | rankIdAgainstConstraint | 职位和职级违法绑定约束 | 职位和职级违法绑定约束 |
| 400 | recall.ding.exception | recall.ding.exception %s | 撤回DING消息异常 |
| 400 | receiver.id.parseFailed | 吊顶可见者id解析失败 | 吊顶可见者id解析失败 |
| 400 | receivers.exceed | %s | 接收者名单超限 |
| 400 | receivers.exceed | 接收者名单超限 | 接收者名单超限 |
| 400 | receivers.list.empty | 接收人列表为空 | 接收人列表为空 |
| 400 | recordNotExist | record not exist. | 记录不存在 |
| 400 | recordStopError | record stop error, please try again | 录制停止失败 |
| 400 | recordStopPermissionError | you can't operator, please contact meeting manager | 录制因权限问题停止失败 |
| 400 | recycleBinNotSupportForSpace | %s | 空间不支持回收站 |
| 400 | reject | %s | 群中机器人数量太多，无法查询 |
| 400 | related.customer.required | related customer required | 关联客户字段必填 |
| 400 | relationType.not.exists | relationType not exists | relationType不存在 |
| 400 | remoteServiceError | 远程服务错误 | 远程服务错误 |
| 400 | repeatApprovesOverLimit | 时间存在重复的审批单写入超过限制 | 时间存在重复的审批单写入超过限制 |
| 400 | request.duplicate | 重复请求，请稍后重试 | 重复请求，请稍后重试 |
| 400 | request.illegal | 本接口调用次数超过今日上限，请明日再试 | 调用次数超过限制 |
| 400 | request.isNull | request请求参数为空 | request请求参数为空；request请求参数未传递空 |
| 400 | request.limit | 模型限流 | 模型请求限流，请求稍后重试 |
| 400/500 | request.overlimit | You have sent too many requests. | 请求过于频繁 |
| 400 | request.too.fast | request too fast. | 请求过快被限流。 |
| 400 | request.too.frequent | request too frequent | 请求过于频繁 |
| 400 | request.too.frequent | 请求太频繁 | 请求过于频繁。 |
| 400 | request.too.tast | request too fast. | 请求过快被限流。 |
| 400 | requestError | 当前传递过来的词条信息不能为空 | 当前传递过来的词条信息不能为空 |
| 400 | requestError | 待处理的信息不能为空 | 待处理的信息不能为空 |
| 400 | requestError.wordName | 当前传递过来的词条名称信息不能为空 | 当前传递过来的词条名称信息不能为空 |
| 400 | requestIdNotConsist | RequestId不一致 | 两次解码传入的requestId不一致 |
| 400 | requestParamError | %s | 请求参数错误 |
| 400 | requestTooMuch | 请求太频繁了，稍后再试 | 请求太频繁了，稍后再试 |
| 400 | required.error | %s | 必填项校验错误 |
| 400 | resource.unavailable | %s | 资源不可用，可能是机器人已停用或会话未安装酷应用 |
| 400 | resourceCancel | Schedule conference has canceled | 预约会议已被取消 |
| 400 | resourceCapacity.resource.resourceReachedLimit | 宜搭资源校验失败:%s | 宜搭资源校验失败 |
| 400 | resourceClose | The meeting has ended | 该会议已被关闭 |
| 400 | robot.not.found | 机器人不存在 | 机器人不存在 |
| 400 | robot.oto.notExist | %s | 没有有效的机器人单聊会话 |
| 400 | robot.oto.notExist | 没有有效的机器人单聊会话 | 没有有效的机器人单聊会话 |
| 400 | robot.processQueryKey.expired | %s | processQueryKey已过期，无法撤回消息 |
| 400 | robot.queryFalied | 机器人查询失败 | 机器人查询失败 |
| 400 | robotCode.empty | 机器人编码为空 | 机器人编码为空 |
| 400 | robotDisabled | 机器人已停用 | 机器人已停用 |
| 400 | robotNotFound | 机器人不存在 | 机器人不存在 |
| 400 | room.exist | Room Exsit | 同名会议室已存在 |
| 400 | room.name.unsafe | Room Name Unsafe | 会议室名称不允许 |
| 400 | room.not.found | Room Not Found | 会议室不存在 |
| 400 | roomClosed | the meeting has ended | 房间已关闭 |
| 400 | rootDeptCanNotUpdate | ROOT\_DEPT\_CAN\_NOT\_UPDATE | 根组织单元不允许更新 |
| 400 | ruleNum.exceed.limit | 该类型可见性规则数量已达上限 | 规则数量已达上限 |
| 400 | same.data.exists | same data exists | 已存在相同数据 |
| 400 | sameMobileCount.exceeds.limit | same mobile count exceeds limit | 同一个手机号不能被添加超过10次 |
| 400 | saveFail | 保存数据发生错误 | 保存数据发生错误 |
| 400 | saveFailed | SAVE\_EMPLOYEE\_INFO\_FAILED | 创建用户信息失败 |
| 400 | saveIsvInfoError | 保存服务商信息异常 | 保存服务商信息异常 |
| 400 | saveOrgTaskError | 保存任务信息异常,盖企业印章,请传入企业名称 | 保存任务信息异常盖企业印章,请传入企业名称 |
| 400 | saveTaskError | 保存任务信息异常 | 保存任务信息异常 |
| 400 | sceneGroup.checkFailed | 场景群权限校验失败 | 场景群权限校验失败 |
| 400 | sceneGroupNotFound | 非场景群 | 非场景群 |
| 400 | sceneQuotaInsufficient | %s | 场景容量不足 |
| 400 | scheduleConferenceIdError | scheduleConferenceIdError | 预约会议id错误 |
| 400 | schema.sysAttrs.error | 表单扩展信息添加错误 | 添加process扩展属性错误 |
| 400 | send.byToken.tooFast | %s | 用TOKEN发送限流错误，请稍后再试 |
| 400 | send.byToken.tooFast | 用TOKEN发送限流错误 | 用TOKEN发送限流错误 |
| 400 | send.cardMsg.failed | 发送互动卡片消息失败 | 发送互动卡片消息失败 |
| 400 | send.ding.exception | send.ding.exception %s | 发送DING消息异常 |
| 400 | send.forbidden | %s | 此机器人禁止发送消息 |
| 400 | send.forbidden | 禁止发送 | 禁止发送 |
| 400 | send.oa.failed | 发工作通知失败，请稍后重试 | 发工作通知失败，请稍后重试 |
| 400 | send.oa.timeout | 发工作通知超时，请稍后重试 | 发工作通知超时，请稍后重试 |
| 400 | send.too.fast | %s | 发送消息频率过快，请稍后再试 |
| 400 | send.too.fast | 限流错误 | 限流错误 |
| 400 | send.toofast | 发送频繁，请稍后再试 | 发送频繁，请稍后再试 |
| 400 | sendCardMessageFailed | 发送卡片失败 | 发送卡片失败 |
| 400 | sendDingFail | 机器人发送ding消息失败 | 机器人发送ding消息失败 |
| 400 | sendMessage.model.notMatch | %s | 无匹配的消息模型 |
| 400 | sendMessage.model.notMatch | 无匹配的消息模型 | 无匹配的消息模型 |
| 400 | sendMessageMessageContentInvalid | 群发消息内容无效 | 群发消息内容无效 |
| 400 | sendMessageMessageContentTitleInvalid | 群发消息标题无效 | 群发消息标题无效 |
| 400 | sendMessageMessageInvalid | 群发消息参数无效 | 群发消息参数无效 |
| 400 | sendMessageQueryGroupInvalid | 群发消息圈群条件无效 | 群发消息圈群条件无效 |
| 400 | sendMessageSendConfigInvalid | 群发消息圈群条件圈群类型无效 | 群发消息圈群条件圈群类型无效 |
| 400 | sendMessageSendConfigSendTypeInvalid | 群发消息发送配置发送类型无效 | 群发消息发送配置发送类型无效 |
| 400 | sendMessageTaskNameInvalid | 群发任务名不正确，为空或者超过128字符 | 群发任务名不正确，为空或者超过128字符 |
| 400 | service.error | 服务错误 | 服务错误 |
| 400 | service.invalidParam | 入参错误 | 入参错误 |
| 400 | service.nonexist | 钉内账号不存在，请检查 | 钉内账号不存在，请检查 |
| 400 | serviceError | service error. %s | 执行异常 |
| 400 | serviceError | 服务错误 | 服务错误 |
| 400 | serviceId.error | 模型id设置错误 | 模型信息不正确，请在炼丹炉上确认模型是否正确 |
| 400 | serviceOwner.nonexist | 群主不存在，群主为钉内账号 | 群主不存在，群主为钉内账号 |
| 400 | session.expired | %s | session已过期 |
| 400 | session.expired | session已过期 | session已过期 |
| 400 | session.notExisted | %s | session不存在 |
| 400 | session.notExisted | session不存在 | session不存在 |
| 400 | setup.no.permission | 没有操作审批流的权限，请检查审批实例是否正确 | 没有操作审批流的权限，请检查审批实例是否正确 |
| 400 | sign.not.match | %s | 签名不匹配，无权限发送消息 |
| 400 | sign.not.match | 签名不匹配 | 签名不匹配 |
| 400 | singlegroup.notsupport | 二人群无法修改群信息 | 二人群无法修改群信息 |
| 400/404 | spaceNotExist | %s | 空间不存在；源文件(夹)或目标目录所在空间不存在；知识库不存在；空间不存在 |
| 400 | spaceQuotaInsufficient | %s | 空间容量不足 |
| 400 | sql.format.error | sql格式错误 | sql格式错误 |
| 400 | staff.not.found | userId错误 | userId错误 |
| 400 | staff.not.found | 员工不存在 | 员工不存在 |
| 400 | staffChangeError | staffChangeError | staffId转化失败 |
| 400 | staffId.notExisted | %s | staffId不存在 |
| 400 | staffId.notExisted | staffId不存在 | staffId不存在 |
| 400 | standardStruNotExist | STANDARD\_STRU\_NOT\_EXIST | 行政组织架构不存在 |
| 400 | struDeptCanNotUpdateStandardParam | STRU\_DEPT\_CAN\_NOT\_UPDATE\_STANDARD\_PARAM | 架构组织单元不允许更新标准字段(dept\_type/dept\_code/parent\_id/name) |
| 400 | struDeptNotExist | STRU\_DEPT\_NOT\_EXIST | 架构不存在 |
| 400 | subadmin.exceed | 管理员超限 | 管理员超限 |
| 400 | subAdminNumberExcessive | 管理员数量超过最大限制 | 管理员数量超过最大限制 |
| 400 | subjectNodeEmpty | subjectUserIds、subjectDeptIds、subjectTagIds不能都为空 | subjectUserIds、subjectDeptIds、subjectTagIds不能都为空 |
| 400 | subjectNodeExceed | subjectUserIds、subjectDeptIds、subjectTagIds三个数组元素之和不能超过50 | subjectUserIds、subjectDeptIds、subjectTagIds三个数组元素之和不能超过50 |
| 400 | suiteCallInvalid | 企业没有开通微应用 | 企业没有开通微应用 |
| 400 | swform.getFormInstance.bizError | getInstance fail | 获取表单详情失败 |
| 400 | swform.getFormInstance.paramError | app has been stoped | 应用已停用 |
| 400 | swform.getFormInstance.paramError | app not exist | 应用不存在 |
| 400 | swform.getFormInstance.paramError | can't find form app | 找不到应用（不存在或已停用） |
| 400 | swform.getFormInstance.paramError | invalid biz\_type | 填表类型参数非法，当前仅支持0：通用智能填表 1：教育版填表 |
| 400 | swform.getFormInstance.paramError | invalid formInstanceId | formInstanceId请求参数不能为空 |
| 400 | swform.getFormInstance.paramError | param invalid | 获取填表实例详情参数异常 |
| 400 | swform.listFormInstances.paramError | app has been stoped | 应用已停用 |
| 400 | swform.listFormInstances.paramError | app not exist | 应用不存在 |
| 400 | swform.listFormInstances.paramError | can't find form app | 企业下没有对应该appId的微应用 |
| 400 | swform.listFormInstances.paramError | getFormInstanceListByFormType fail | 获取表单实例列表失败 |
| 400 | swform.listFormInstances.paramError | invalid action\_date | 循环表单action\_date参数不合法 |
| 400 | swform.listFormInstances.paramError | invalid biz\_type | 填表类型参数非法，当前仅支持0：通用智能填表 1：教育版填表 |
| 400 | swform.listFormInstances.paramError | invalid form\_code | 找不到表单form\_code（不存在或已删除） |
| 400 | swform.listFormInstances.paramError | invalid offset | 无效的偏移量，需从0开始 |
| 400 | swform.listFormInstances.paramError | invalid size | 无效的分页大小，最大100。 |
| 400 | swform.listFormInstances.paramError | param invalid | 获取填表实例列表参数异常 |
| 400 | swform.listFormSchemasByCreator.paramError | app has been stoped | 应用已停用 |
| 400 | swform.listFormSchemasByCreator.paramError | app not exist | 应用不存在 |
| 400 | swform.listFormSchemasByCreator.paramError | getFormListByCreator fail | 获取用户创建的表单模板列表失败 |
| 400 | swform.listFormSchemasByCreator.paramError | invalid biz\_type | 填表类型参数非法，当前仅支持0：通用智能填表 1：教育版填表 |
| 400 | swform.listFormSchemasByCreator.paramError | invalid offset | nextToken请求参数不合法 |
| 400 | swform.listFormSchemasByCreator.paramError | invalid size | maxResults请求参数不合法，最大支持200 |
| 400 | swform.listFormSchemasByCreator.paramError | param invalid | 获取用户创建的填表模板列表参数异常 |
| 400/500 | system.busy | system busy | 请求过于频繁 |
| 400/500 | system.error | %s | 系统错误；未知的系统错误；系统繁忙，请稍后再试；系统错误；系统错误%s |
| 400/500/503 | system.error | system error | 系统错误；未知的系统内部错误。；系统错误 |
| 400/500 | system.error | system.error | 系统错误；系统异常；系统繁忙，请稍后重试；系统错误 |
| 400/500 | system.error | 未知的系统错误 | 未知的系统错误 |
| 400/500 | system.error | 系统异常 | 系统异常 |
| 400/500 | system.error | 系统错误 | 系统错误；内部服务发生的异常情况；系统错误 |
| 400 | system.error | 表单扩展信息添加错误 | 添加process扩展属性错误 |
| 400 | system.updateCallbackFailed | system.updateCallbackFailed | 更新回调 RouteKey 失败 |
| 400/500 | systemError | %s | 系统错误；服务繁忙，请稍后重试；未知的系统错误；系统异常；系统错误 |
| 400 | systemError | SYSTEM\_ERROR | 系统异常；系统异常，请重试；系统错误 |
| 400 | systemError | system error, %s | 获取模板归属应用失败 |
| 400/500 | systemError | 系统异常 | 系统内部异常；系统内部异常，请稍后再试；系统异常；出现未知的系统异常；出现未知的系统错误；系统异常；系统异常，内部群只能更新到内部服务群组，外部群只能更新到外部服务群组；系统异常，请稍后重试 |
| 400/500 | systemError | 系统错误 | 系统错误 |
| 400 | systemError | 系统错误，请稍后重试 | 系统错误，请稍后重试 |
| 400 | systemError.appNotExists | %s | 应用不存在 |
| 400 | systemError.appNotExists | system error app not exists, %s | 应用不存在 |
| 400 | systemError.appNotExists | system error, app not exists, %s | 应用不存在 |
| 400 | systemError.notPermittedAccess | %s | 无权限操作 |
| 400 | systemError.notPermittedAccess | system error not permitted access, %s | 无操作权限 |
| 400 | systemError.notPermittedAccess | system error, %s | 无权限操作 |
| 400 | systemError.notPermittedAccess | system error, not permitted access, %s | 无权限操作 |
| 400 | systemRuntimeException.exception.platformKnownException | 宜搭平台发生了异常:%s | 宜搭平台发生了异常 |
| 400 | systemRuntimeException.exception.platformKnownException | 平台已知异常:%s | 平台已知异常 |
| 400 | systemRuntimeException.exception.platformUnknownException | 宜搭平台发生了未知的异常:%s | 宜搭平台发生了未知的异常 |
| 400 | systemRuntimeException.exception.platformUnknownException | 平台未知异常:%s | 平台未知异常 |
| 400 | systemRuntimeException.exception.systemException | 系统运行异常:%s | 系统运行异常 |
| 400 | targetSelectApproverMissing | 自选审批人缺失 | 自选审批人缺失 |
| 400 | targetSelectApproverScopeError | 自选审批人不在规定范围内 | 自选审批人不在规定范围内 |
| 400 | task.dueTime.error | 任务列表tasks中截止时间dueTimestamp不能小于当前任务创建时间 | 任务列表tasks中截止时间dueTimestamp不能小于当前任务创建时间 |
| 400 | task.status.error | 当前任务状态不是运行中不支持加签操作 | 请检查taskId，任务状态是否为RUNNING |
| 400 | task.status.error | 当前任务状态不是运行中不支持转交操作 | 当前任务状态不是运行中不支持转交操作 |
| 400 | task.status.error | 当前任务状态不是运行中不支持退回操作 | 请检查taskId，任务状态是否为RUNNING |
| 400 | task.url.error | 任务列表tasks中url长度不能超过1024字符 | 任务列表tasks中url长度不能超过1024字符 |
| 400 | taskInfoSizeOverLimit | 任务信息队列超出上限 | 任务信息队列超出上限 |
| 400 | tasks.is.null | 参数错误，任务列表tasks不能为空 | 参数错误，任务列表tasks不能为空 |
| 400 | teacherNotExist | TEACHER NOT EXIST | 老师不存在 |
| 400 | template.isNotExist | 模板不存在 | 模板不存在 |
| 400 | template.mismatch | 群模板类型不匹配 | 群模板类型不匹配 |
| 400 | template.nonexist | 群模板不存在，请检查 | 群模板不存在，请检查 |
| 400 | template.not.exist | Target template don't exist | 模板不存在 |
| 400 | template.not.existed | %s | 机器人模板不存在；机器人模板不存在，请检查robotCode是否正确 |
| 400 | template.not.existed | 机器人模板不存在 | 机器人模板不存在 |
| 400 | template.not.found | Template Not Found | 模板找不到 |
| 400 | template.stopped | %s | 机器人模板已经停用；机器人模板已经停用，请检查机器人状态 |
| 400 | template.stopped | 机器人模板已经停用 | 机器人模板已经停用 |
| 400 | time.should.close | 时间段需要闭合(fromTime和toTime需都传或都不传) | 时间段需要闭合(fromTime和toTime需都传或都不传) |
| 400 | timeStamp.invalid | illegal timestamp | 查询时间错误 |
| 400 | todo.bizcategory.error | 同步待办分组失败 | 同步待办分组失败，请稍后重试。 |
| 400 | todo.orgTaskQuery.paramError | nextToken is invalid | 分页游标参数非法 |
| 400 | todo.orgTaskQuery.paramError | todo.orgTaskQuery.paramError | 查询企业待办列表系统参数错误 |
| 400 | todo.taskCreate.flowControlError | flowControl because of executorId or orgId | 创建待办针对执行者或者企业进行了限流处理 |
| 400 | todo.taskCreate.lockError | todo.taskCreate.lockError | 创建待办根据sourceId加锁失败 |
| 400/500 | todo.taskCreate.paramError | description is oversize | 待办描述长度超出限制 |
| 400 | todo.taskCreate.paramError | dueTime is invalid | 待办截止时间非法 |
| 400 | todo.taskCreate.paramError | executors is oversize | 待办执行人超出限制 |
| 400 | todo.taskCreate.paramError | participants is oversize | 待办参与人超出限制 |
| 400 | todo.taskCreate.paramError | subject is oversize | 待办标题长度超出限制 |
| 400 | todo.taskCreate.paramError | task exist | 待办任务已存在 |
| 400 | todo.taskCreate.paramError | todo.taskCreate.paramError | 创建待办参数异常 |
| 400/500 | todo.taskCreate.systemError | todo.taskCreate.systemError | 创建待办系统内部异常 |
| 400 | todo.taskCreate.tokenTypeError | token type is not match | 授权类型错误，本接口需要使用个人身份访问凭证 |
| 400 | todo.taskDelete.paramError | task not exist | 待办任务不存在 |
| 400 | todo.taskDelete.paramError | todo.taskDelete.paramError | 删除待办参数异常 |
| 400 | todo.taskExecutorStatusUpdate.paramError | executors is oversize | 待办执行人超出限制 |
| 400 | todo.taskExecutorStatusUpdate.paramError | task not belong to bizTag | 待办任务不属于该应用 |
| 400 | todo.taskExecutorStatusUpdate.paramError | task not exist | 待办任务不存在 |
| 400 | todo.taskExecutorStatusUpdate.paramError | todo.taskExecutorStatusUpdate.paramError | 更新待办执行者状态参数异常 |
| 400 | todo.taskUpdate.paramError | description is oversize | 待办描述长度超出限制 |
| 400 | todo.taskUpdate.paramError | dueTime is invalid | 待办截止时间非法 |
| 400 | todo.taskUpdate.paramError | executors is oversize | 待办执行人超出限制 |
| 400 | todo.taskUpdate.paramError | participants is oversize | 待办参与人超出限制 |
| 400 | todo.taskUpdate.paramError | subject is oversize | 待办标题长度超出限制 |
| 400 | todo.taskUpdate.paramError | task not belong to bizTag | 待办任务不属于该应用 |
| 400 | todo.taskUpdate.paramError | task not exist | 待办任务不存在 |
| 400 | todo.taskUpdate.paramError | todo.taskUpdate.paramError | 更新待办参数异常 |
| 400 | token.notExisted | %s | TOKEN不存在 |
| 400 | token.notExisted | TOKEN不存在 | TOKEN不存在 |
| 400 | too.many.group | %s | 发送频繁限流 |
| 400 | too.many.group | 发送频繁限流 | 发送频繁限流 |
| 400 | too.many.people | %s | 发送频繁限流 |
| 400 | too.many.people | 发送频繁限流 | 发送频繁限流 |
| 400 | toomuch.msg | send too fast | 消息发送太快，每分钟每机器人发送消息6000 |
| 400 | topbox.auth.checkFailed | 酷应用或场景群权限校验失败 | 酷应用或场景群权限校验失败 |
| 400 | tryAgainLater | 更新失败，请稍后重试 | 更新失败，请稍后重试 |
| 400 | typeInvalid | type只能是excludeNode、onlySelf、onlySelfDeptAndChild中的一个 | type只能是excludeNode、onlySelf、onlySelfDeptAndChild中的一个 |
| 400 | uidDecryptError | 消息接收者UID解码错误 | 消息接收者UID解码错误 |
| 400/401/500 | unauthorized | %s | 未授权；未授权，不允许操作；权限不足，群聊所属企业不匹配；调用权限不足；服务未授权,前往授权链接；未授权 |
| 400 | unavailable | %s | 群内未安装群模板 |
| 400 | unchange | taskflowStatusId not change | taskflowStatusId未改变 |
| 400 | unitIncorrect | 假期单位不正确 | 假期单位不正确 |
| 400 | unknown.send.result | %s | 未知的发送结果 |
| 400 | unknown.send.result | 未知的发送结果 | 未知的发送结果 |
| 400 | unknownUserError | unknownUserError | 无法识别的用户 |
| 400 | unsupported.grant.type | unsupported.grant.type | 不支持此授权类型，请检查授权类型参数 |
| 400/500 | unsupported.operation | Does not support the operation | 暂不支持该操作 |
| 400 | updateOverSize | 更新审批单数量超出限制 | 更新审批单数量超出限制 |
| 400 | updateSpeedfast | 亲，该操作速度过快，请5分钟后再试 | 亲，该操作速度过快，请5分钟后再试 |
| 400 | updateSubDeptGroupFailed | UPDATE\_SUB\_DEPT\_GROUP\_FAILED | 更新组织单元群包含子组织单元异常 |
| 400 | url.parameter.error | 参数错误:%s | 参数错误 |
| 400 | user.error | 用户信息缺失 | 请设置正确的用户信息 |
| 400 | user.not.admin | User Not Admin | 用户不是管理员 |
| 400 | user.not.employee | User Not Employee | 用户不在企业；用户不是员工 |
| 400 | user.not.exist | user not exist | 用户在当前企业中不存在；用户在当前企业中不存在。；用户或者操作者在当前企业中不存在 |
| 400 | user.not.exist | user.not.exist | 用户在当前企业中不存在 |
| 400 | user.not.exist | 用户ID不存在，请检查operateUserId、targetActivityActioners中的用户ID是否正确 | 用户ID不存在，请检查operateUserId、targetActivityActioners中的用户ID是否正确 |
| 400 | user.not.exist | 用户ID不存在，请检查operatorId、appenderUserIds中的用户ID是否正确 | 用户ID不存在，请检查operatorId、appenderUserIds中的用户ID是否正确 |
| 400 | user.not.exist | 用户不存在 | 用户不存在；用户不存在，请检查operateUserId参数是否正确。；用户不存在，请检查参数operateUserId是否正确。 |
| 400 | user.not.found | 用户不存在 | 用户不存在 |
| 400 | user.not.org | User Not In Org | 用户不在组织内 |
| 400 | user.over.limit | User Over Limit | 黑名单用户id超过限制 |
| 400 | userCodeExist | 用户码已存在 | 用户码已存在 |
| 400 | userId.not.exists | userId not exists | 用户不存在或该用户未关注服务窗 |
| 400 | userIdExist | USERID\_EXIST\_IN\_ORG | userId已存在 |
| 400 | userIdInvalid | userId不存在 | userId不存在 |
| 400 | userIdList.error | illegal userIdList | 查询userId列表错误 |
| 400 | userIdNotExists | %s | 用户不存在 |
| 400 | userIdOrUnionId.empty | 用户id为空 | 用户id为空 |
| 400 | userIds.missing | 请求中不含userIds字段 | 请求中不含userIds字段 |
| 400 | userInfo.convertError | 消息接收者UID解码错误 | 消息接收者UID解码错误 |
| 400 | userInfoError | 用户信息异常 | 用户信息异常 |
| 400 | userNoLivePermission | lippi\_live.exception.userNoLivePermission | 用户在当前组织没有直播权限 |
| 400 | userNotExist | USER\_NOT\_EXIST | 用户不存在 |
| 400 | userNotExist | 用户不存在 | 用户不存在；请检查opUserId参数是否正确，必须为组织内用户；请检查operatingUserId参数是否正确；请检查当前用户是否归属于当前组织 |
| 400 | userNotExisted | %s | 用户信息不存在 |
| 400 | userNotExists | 用户不存在 | 用户不存在 |
| 400 | userNotFound | USER\_NOT\_FOUND | 用户不存在 |
| 400 | userNotifyExist | 通知消息已经存在 | 通知消息已经存在 |
| 400 | userNotInExtContact | 用户不在外部联系人 | 用户不在外部联系人 |
| 400 | userNotInGroup | 用户不在群中 | 用户不在群中 |
| 400 | userNotInGroup | 用户不在群内 | 用户不在群内 |
| 400 | userNotInOrg | userNotInOrg | 用户不在组织内 |
| 400 | userNotInOrg | 用户不在此组织中 | 用户不在此组织中 |
| 400 | userOpenAccountProtect | USER\_OPEN\_ACCOUNT\_PROTECT | 用户开启了账号保护 |
| 400 | uuid.repeat | uuid重复 | uuid重复 |
| 400 | volume.lack | 电话DING额度不足 | 电话DING额度不足 |
| 400 | volume.lack | 额度不足 | 额度不足 |
| 401 | - | Unauthorized | 未授权，access\_token缺失或无效。 |
| 401 | businessError | 业务异常 | 例如不允许给自己办离职，员工不是正常在职状态等；例如员工不是待离职状态、所填离职原因不存在等异常；例如员工不是待离职状态等异常 |
| 401 | corp.not.bind | 组织未绑定 | 钉钉组织未绑定该系统 |
| 401 | illegal.argument | 参数有误 %s | 参数有误 %s |
| 401 | paramIllegal | param illagal. %s | 入参错误 |
| 401 | paramIllegal | param illegal. %s | 入参错误 |
| 401 | sys.error | 系统错误 | 系统错误 |
| 401 | system.not.exist | 系统未注册 | 系统未在钉钉物联平台注册 |
| 401 | unauthorized.client | unauthorized.client | 应用未被授权 |
| 402 | params.isNull | corpId或者viewUserId为空 | corpId或者viewUserId为空 |
| 403 | - | Forbidden | 请求被拒绝，通常由于权限不足或触发限流。 |
| 403 | accessDenied | %s | 请求被拒绝，请确认企业开通了公告微应用，并且用户id正确。；请求被拒绝，请确认操作人是企业主管理员或者是公告的发送人，并且公告归属于当前组织。 |
| 403 | accessDenied | accessDenied | 请求被拒绝，请确认操作人是企业主管理员或者是公告的发送人，并且公告归属于当前组织。 |
| 403 | acrossOrgAccessForbidden | %s | 禁止跨企业访问 |
| 403 | crm.not.created | crm应用未安装 | crm应用未安装 |
| 403 | crossOrgAccess.forbiden | Cross org access is forbiden. | 禁止跨企业访问 |
| 403 | forbidden.accessDenied | %s | 无当前节点的查看权限；无当前节点的查询权限，或者无当前节点的下级节点列表查询权限；无权限 |
| 403 | forbidden.accessDenied | The operator has no permission. | 当前用户无此操作权限。 |
| 403 | forbidden.accessDenied | 当前用户无此操作权限 | 当前用户无此操作权限 |
| 403 | forbidden.accessDenied | 用户无操作权限 | 当前用户无此操作权限；用户无操作权限 |
| 403 | Forbidden.AccessDenied.AccessTokenPermissionDenied | 没有调用该接口的权限 | 需要申请下接口权限，请参考[添加接口调用权限](0003-add-api-permission.md)。 |
| 403 | Forbidden.AccessDenied.IpNotInWhiteList | 访问ip不在白名单之中 | \* 企业应用：检查配置的服务器出口IP地址是否和请求IP地址一致。 \* ISV应用：检查套IP白名单和请求是否一致。 |
| 403 | forbidden.accessDenied.notInOrg | %s | 组织外成员无权限 |
| 403 | Forbidden.AccessDenied.QpmLimitForAppkeyAndApi | 您的企业应用调用钉钉开放平台当前接口的所有请求都被暂时禁用了 | 当前企业应用调用开放接口触发了QPM限流。 |
| 403 | Forbidden.AccessDenied.QpmLimitForSuitekeyAndOrgAndApi | 您的ISV应用调用钉钉开放平台当前接口的所有请求都被暂时禁用了 | 当前ISV应用调用开放接口触发了QPM限流，仅针对一个客户企业。 |
| 403 | Forbidden.AccessDenied.QpsLimitForApi | 您的服务器调用钉钉开放平台当前接口的所有请求都被暂时禁用了 | 触发了当前开放接口的全局QPS限流。 |
| 403 | Forbidden.AccessDenied.QpsLimitForAppkeyAndApi | 您的企业应用调用钉钉开放平台当前接口的所有请求都被暂时禁用了 | 当前企业应用调用开放接口触发了QPS限流。 |
| 403 | Forbidden.AccessDenied.QpsLimitForSuitekeyAndOrgAndApi | 您的ISV应用调用钉钉开放平台当前接口的所有请求都被暂时禁用了 | 当前ISV应用调用开放接口触发了QPS限流，仅针对一个客户企业。 |
| 403 | forbidden.accessDenied.realmControl | %s | 企业开启了专属安全管控，操作被禁止 |
| 403 | forbidden.acrossOrg | %s | 请求不合法，请检查要访问的文档是否归属于accessToken指定的组织。；请求操作不合法，请查看错误信息。 |
| 403 | forbidden.document.sizeOverLimit | The document size is over limit and the server is unable to complete your request. Retry is unlikely to work unless the document size is decreased. | 表格内容过大，请尝试缩减表格内容。 |
| 403/500 | forbidden.operationIllegal | %s | 无权限；请求操作不合法。可能的错误包含没有权限访问被锁定的单元格，修改数据透视表、待办相关的单元格等。具体错误请查看错误信息。；请求操作不合法，请查看错误信息。；请求操作不合法 |
| 403 | forbidden.user.notInOrg | 操作用户不在组织内 | 操作用户不在组织内 |
| 403 | forbidden.user.notInOrg | 用户不在组织内 | 操作用户不在组织内 |
| 403 | invalidRequest.document.typeIllegal | %s | 不支持的文档类型，请检查baseId |
| 403 | no.priviledge | Org has not obtained DingTalk certification | 企业不具有钉钉认证 |
| 403 | no.priviledge | You are not on the allowlist | 您未在允许名单中 |
| 403 | noPermission | NO PERMISSION | 无权查询会议 |
| 403 | orgAuthLevelNotEnough | auth level of org is not enough | 企业认证等级过低 |
| 403 | permission.deny | need user auth | 用户未授权 |
| 403 | permission.wrong | 无权限 %s | 无权限 %s |
| 403 | permissionDenied | The operator has no permission. | 当前用户无此操作权限 |
| 403 | permissionDenied | permission denied | 鉴权失败 |
| 403 | permissions.error | 没有调用该接口的权限 | 没有调用该接口的权限 |
| 403 | spaceNotAccessible | %s | 空间不可访问 |
| 403 | systenError | 服务器内部错误 | 服务器内部错误 |
| 403 | thumbnailNotExist | %s | 缩略图不存在 |
| 403 | unsupported.operation | Does not support cross-org access | 不支持跨企业访问 |
| 403 | workspaceNotAccessible | %s | 知识库不可访问 |
| 403 | workspaceTeamNotAccessible | %s | 知识小组不可访问 |
| 404 | - | Not Found | 请求的资源不存在。 |
| 404 | appNotExist | %s | 对应应用不存在 |
| 404 | candidate.notExists | 候选人不存在 | 候选人不存在 |
| 404 | conversationNotExist | %s | 目标会话不存在 |
| 404 | docNotExist | %s | 文档不存在 |
| 404/500 | documentNotExist | %s | 文档不存在；文档不存在或格式不支持；文档不存在或格式不支持 |
| 404 | error.notFound | 接口路径错误 %s | 接口路径错误 %s |
| 404 | instanceNotExist | instance not exist | 循环日程实例不存在 |
| 404 | invalidParameter.item.notFound | %s | 当前节点不存在或已被删除 |
| 404 | invalidParameter.space.notFound | %s | 当前知识库不存在或已被删除 |
| 404 | invalidParameter.user.notFound | 找不到该用户 | 用户不存在时返回这个错误码 |
| 404 | invalidRequest.document.deleted | 知识库文档已被删除 | 知识库文档已被删除 |
| 404 | invalidRequest.document.deleted | 知识库文档被删除 | 知识库文档被删除 |
| 404 | invalidRequest.document.deleted | 知识库节点已被删除 | 知识库节点已被删除 |
| 404 | invalidRequest.document.notFound | Fail to find the requested resource by the given baseId. Please make sure the given baseId is valid, and the operatorId has permission to access it. | 文档不存在 |
| 404 | invalidRequest.resource.notFound | %s | 无法找到要访问的资源；请求失败，无法找到要访问的资源。；资源不存在，数据不存在或被彻底删除 |
| 404 | invalidRequest.resource.notFound | 资源找不到 | 知识库、节点等资源找不到；资源找不到 |
| 404 | invalidRequest.workspace.deleted | 知识库已被删除 | 知识库已被删除 |
| 404 | invalidRequest.workspace.deleted | 知识库被删除 | 知识库被删除 |
| 404 | itemNotFound | forwardErrorMessage | 无法找到指定日程 |
| 404 | nodeNotExist | %s | 节点不存在 |
| 404 | object.not.exist | File does not exist or has been deleted. | 文件不存在或已删除 |
| 404 | parent.not.exist | Parent folder is not exist. | 父目录不存在 |
| 404 | parentNodeNotExist | %s | 父节点不存在 |
| 404 | recordStartError | recordStartError:%s | 开启录制失败 |
| 404 | recordStartPermissionError | permissionError:%s | 录制因权限问题开启失败 |
| 404 | recycleBinNotExist | %s | 回收站不存在 |
| 404 | recycleItemNotExist | %s | 回收项不存在 |
| 404 | rights.notExists | 权益不存在 | 权益不存在（可能已被删除） |
| 404 | roomNotFound | ROOM NOT FOUND | 查不到该会议 |
| 404 | taskNotExist | %s | 任务不存在 |
| 404 | teamNotExist | %s | 知识小组不存在 |
| 404 | waterLimitError | waterLimitError:%s | 人数水位限流 |
| 404 | workspaceNotExist | %s | 知识库不存在 |
| 405 | - | Method Not Allowed | 请求方法不被允许。 |
| 405 | params.invalid | 无效的分页请求参数nextToken和maxResults | 无效的分页请求参数nextToken和maxResults |
| 409 | invalidRequest.duplicateClientToken | Duplicate ClientToken detected. Please generate a new client token and retry. | 幂等键重复，请生成新的幂等键后重试。 |
| 429 | system.busy | system busy, request too frequest | 请求太频繁，系统限流 |
| 429 | systemBusy | 请求太频繁 | 系统繁忙，请求被限流 |
| 500 | - | Internal Server Error | 服务器内部错误。 |
| 500 | accessStorageFail | 访问存储异常 | 访问存储异常 |
| 500 | action.already.exist | 技能已发布到组织技能库，请勿重复发布 | 技能已发布到组织技能库，请勿重复发布 |
| 500 | agent.not.allow | 未授权该微应用红点推送权限 | 未授权该微应用红点推送权限 |
| 500 | api.fields.notAllAuth | 服务配置字段未被全部授权 | 服务配置字段未被全部授权 |
| 500 | apiDataConnect.dataFields.overMaxLimit | 数据项字段超过限制 | 数据项字段超过限制 |
| 500 | apiDataConnect.dataset.notFound | 数据集未找到 | 数据集未找到 |
| 500 | apiDataConnect.dataset.overLimit | 查询超过跨数据集个数限制 | 查询超过跨数据集个数限制 |
| 500 | apiDataConnect.datasource.notFound | 数据源未找到 | 数据源未找到 |
| 500 | apiDataConnect.datasource.overLimit | 暂不支持跨数据源查询 | 暂不支持跨数据源查询 |
| 500 | apiDataConnect.detailDataset.overLimit | 明细类型数据服务暂不支持跨数据集查询 | 明细类型数据服务暂不支持跨数据集查询 |
| 500 | approval.not.completed | 该数据服务审批未完成 | 该数据服务审批未完成 |
| 500 | approval.result.refused | 该数据服务审批被拒绝 | 该数据服务审批被拒绝 |
| 500 | assistant.basicInfo.error | %s | 获取AI助理基础信息失败(E000037) |
| 500 | assistant.decs.block | AI助理描述包含敏感字，请更换其他描述 | AI助理描述包含敏感字，请更换其他描述 |
| 500 | assistant.desc.block | AI助理描述包含敏感字，请更换其他描述 | AI助理描述包含敏感字，请更换其他描述 |
| 500 | assistant.desc.invalid | AI助理描述不合法，请确保只包含中文、英文大写字母、小写字母、阿拉伯数字，以及冒号、逗号和句号 | AI助理描述不合法，请确保只包含中文、英文大写字母、小写字母、阿拉伯数字，以及冒号、逗号和句号 |
| 500 | assistant.fallbackmsg.block | AI助理固定回复包含敏感字，请更换其他内容 | AI助理固定回复包含敏感字，请更换其他内容 |
| 500 | assistant.icon.block | AI助理头像包含敏感信息，请更换其他头像 | AI助理头像包含敏感信息，请更换其他头像 |
| 500 | assistant.instructions.block | AI助理角色设定包含敏感字，请更换其他角色设定 | AI助理角色设定包含敏感字，请更换其他角色设定 |
| 500 | assistant.name.block | AI助理名称包含敏感字，请更换其他名称 | AI助理名称包含敏感字，请更换其他名称 |
| 500 | assistant.name.invalid | AI助理名称不合法，请确保只包含中文、英文大写字母、小写字母、阿拉伯数字 | AI助理名称不合法，请确保只包含中文、英文大写字母、小写字母、阿拉伯数字 |
| 500 | assistant.recommendprompts.block | AI助理开场推荐语包含敏感字，请更换其他内容 | AI助理开场推荐语包含敏感字，请更换其他内容 |
| 500 | assistant.welcomecontent.block | AI助理欢迎语内容包含敏感字，请更换其他内容 | AI助理欢迎语内容包含敏感字，请更换其他内容 |
| 500 | auth.error | 没有权限操作 | 权限错误；没有权限操作 |
| 500 | bind.orgauth.inapproval | 组织开放正在审批中，不支持更改，请在审批完成后再进行修改操作 | 组织开放正在审批中，不支持更改，请在审批完成后再进行修改操作 |
| 500 | check.appauthrule.fail | 暂无权限删除该助理(E000079) | 暂无权限删除该助理(E000079) |
| 500 | check.appauthrule.fail | 暂无权限更新该助理(E000079) | 暂无权限更新该助理(E000079) |
| 500 | checkParam.invalid.notCampusTenantOrg | %s | 当前组织非园区租户组织 |
| 500 | conference.not.found | error:%s | 视频发起者不属于当前组织 |
| 500 | conversation.limit | 最大颁发通知到群的数量为5 | 最大颁发通知到群的数量为5 |
| 500 | conversation.wrong | 群不存在或者发送人不是群成员 | 群不存在或者发送人不是群成员 |
| 500 | create.permission.denied | 当前组织下你没有创建AI助理的权限，请联系管理员申请开通助理创建权限 | 当前组织下你没有创建AI助理的权限，请联系管理员申请开通助理创建权限 |
| 500 | create.security.denied | 不允许当前用户创建AI助理 | 安全管控不允许该用户创建AI助理 |
| 500 | createClassFail | CREATE CLASS FAIL | 创建自定义班级失败 |
| 500 | createDeptFail | CREATE\_DEPT\_FAIL | 创建部门失败 |
| 500 | createRobotException | 机器人创建异常 | 机器人创建异常 |
| 500 | createRobotFail | 机器人创建失败 | 机器人创建失败 |
| 500 | crop.not.install | 企业未安装钉钉物联应用，请联系我们(<https://open.dingtalk.com/document/orgapp-server/dingtalk-iot-overview>) | 企业未安装钉钉物联应用；未安装钉钉物联应用 |
| 500 | dashboard.quota.notEnough | 自定义仪表盘额度不足 | 自定义仪表盘额度不足 |
| 500 | dataItem.quota.notEnough | 调用数据项次数额度不足 | 调用数据项次数额度不足 |
| 500 | dataModified.form.formAlreadyModified | 实例数据已修改, 请刷新当前页面:%s | 实例数据已经修改 |
| 500 | dataNotFound | 数据不存在 | 数据不存在 |
| 500 | delete.error | 删除实例失败 | 删除实例失败 |
| 500 | deleteDeptFail | DELETE DEPT FAIL | 删除部门失败 |
| 500 | deleteGuardianFail | DELETE GUARDIAN FAIL | 删除家长失败 |
| 500 | deleteStudentFail | DELETE\_STUDENT\_FAIL | 删除学生失败 |
| 500 | deleteTeacherFail | DELETE TEACHER FAIL | 老师删除失败 |
| 500 | error.dingTeamIdInvalid | 无效的部门 id | 无效的部门 id |
| 500 | error.emptyScoreCard | 部门下没有计分卡 | 部门下没有计分卡 |
| 500 | error.invalidObjectiveId | 无效的目标Id | 无效的目标Id |
| 500 | error.invalidObjectiveId | 无效的组织目标 id | 无效的组织目标 id |
| 500 | error.invalidObjectiveRuleId | 无效的目标规则Id | 无效的目标规则Id |
| 500 | error.noIndicator | indicator not found | 该指标不存在或已删除 |
| 500 | error.noPermission | 无权限 | 无权限 |
| 500 | error.systemError | 系统异常 | 系统异常 |
| 500 | error.unknownerror | 服务器内部错误 %s | 服务器内部错误 %s |
| 500 | fail.failToCreateCorpAccount | 创建企业账号异常 | 创建企业账号异常 |
| 500 | failure.businessError.businessException | 宜搭未分类的业务异常信息:%s | 宜搭未分类的业务异常信息 |
| 500 | failure.businessError.businessException | 异常:%s | 宜搭未分类的业务异常信息 |
| 500 | failure.businessError.unclassifiedError | 宜搭未分类的错误信息:%s | 宜搭未分类的错误信息 |
| 500 | failure.businessError.unclassifiedError | 异常:%s | 宜搭未分类的错误信息 |
| 500 | failure.businessError.unclassifiedException | 宜搭未分类的错误信息:%s | 宜搭未分类的错误信息 |
| 500 | failure.businessError.unclassifiedException | 异常:%s | 宜搭未分类的错误信息 |
| 500 | fields.not.mappingConfig | 自定义模型中，有字段未配置映射关系 | 自定义模型中，有字段未配置映射关系 |
| 500 | form.code.error | 表单详情查询失败 | 参数错误 |
| 500 | form.error | 参数错误，不是存表单 | 参数错误 |
| 500 | form.error | 表单被停用，请联系管理员 | 表单被停用，请联系管理员 |
| 500 | form.invalid | 模板被停用，联系管理员启用 | 模板被停用 |
| 500 | form.not.exist | 表单不存在 | 表单不存在 |
| 500 | formTypeError | 参数无效，不是纯表单 | 参数无效，不是纯表单 |
| 500 | get.uid.fail | unionId异常，请检查所属组织信息是否正确 | unionId异常，请检查所属组织信息是否正确 |
| 500 | group.create.error | 创建群失败 | 创建群失败 |
| 500 | group.dismissError | 解散群失败 | 解散群失败 |
| 500 | group.query.error | Group Query Error | 分组查询错误 |
| 500 | group.updatefail | 更新群信息失败 | 更新群信息失败 |
| 500 | hava.no.auth | 该员工无企业权限 | 该员工无企业权限 |
| 500 | innerError | 宜搭服务内部异常信息:%s | 宜搭服务内部异常信息 |
| 500 | innerError | 异常:%s | 宜搭的依赖服务的异常信息 |
| 500 | innerSystemError | The system is busy, please try again later | 服务端内部错误 |
| 500 | installRobotFail | 机器人安装异常 | 机器人安装异常 |
| 500 | instance.error | 创建表单实例失败 | 创建表单实例失败 |
| 500 | instance.query.error | instance query error | 表单实例查询失败 |
| 500 | internalError | The server encountered an internal error and was unable to complete your request. Please try again later. | 服务内部错误，请稍后再试。；系统错误 |
| 500 | internalError | 系统内部错误 | 系统内部错误 |
| 500 | invalid.system.errror | 服务不可用 | 服务不可用 |
| 500 | invalid.system.errror | 系统错误 | 系统错误 |
| 500 | invalidParameter | 参数无效 | 参数无效，openConversationId不正确 |
| 500 | invalidRequest.pluginInstallFail | 插件安装失败 | 插件安装失败 |
| 500 | invalidState.matrix.matrixBeUsed | 该矩阵正在被使用，不能删除，请查看「使用详情」:%s | 该矩阵正在被使用，不能删除，请查看「使用详情」 |
| 500 | invalidState.matrix.matrixColumnsOverLimit | 超过矩阵列上限:%s | 超过矩阵列上限 |
| 500 | invalidState.matrix.matrixNotExist | 数据不存在:%s | 数据不存在 |
| 500 | invalidState.matrix.matrixRowsOverLimit | 超过矩阵行数上限:%s | 超过矩阵行数上限 |
| 500 | invalidState.matrix.matrixTableInfoInvalid | 矩阵表头校验异常，请检查表头设计:%s | 矩阵表头校验异常，请检查表头设计 |
| 500 | invalidState.role.roleNotExist | 角色不存在:%s | 角色不存在 |
| 500 | invalidVersion.unsupported | 当前组织未购买该权益，请联系管理员升级宜搭版本:%s | 当前组织未购买该权益，请联系管理员升级宜搭版本 |
| 500 | invoker.notIn.corp | 调用者不是本组织成员，请检查userId入参是否正确 | 调用者不是本组织成员，请检查userId入参是否正确 |
| 500 | listcursor.maxsize.limit | 每页的元素个数超出最大限制，请将元素个数减少至20，并尝试重新请求(E000060) | 每页的元素个数超出最大限制，请将元素个数减少至20，并尝试重新请求 |
| 500 | listsize.too.long | userId列表超过100 | userId列表超过100 |
| 500 | member.add.error | 添加群成员失败 | 添加群成员失败 |
| 500 | member.remove.error | 移除群成员失败 | 移除群成员失败 |
| 500 | message.contenttype.error | %s | 创建消息时，消息格式有误，请检查后重试（E000128） |
| 500 | message.create.error | %s | 系统异常，请稍后重试（E000029） |
| 500 | message.create.exception | %s | 系统异常，请稍后重试(E000184)；系统异常，请稍后重试（E000123） |
| 500 | message.create.throwable | %s | 系统异常，请稍后重试（E000123） |
| 500 | message.delete.error | %s | 系统异常，请稍后重试（E000035） |
| 500 | message.delete.exception | %s | 系统异常，请稍后重试(E000186) |
| 500 | message.delete.throwable | %s | 系统异常，请稍后重试（E000132） |
| 500 | message.invalid.param | %s | 传入的参数非法(E000036) |
| 500 | message.limit.invalid | %s | 查询Message实例数目的配置值不合法， 单次查询不允许超过100个（E000156） |
| 500 | message.list.error | %s | 系统异常，请稍后重试（E000032） |
| 500 | message.list.exception | %s | 系统异常，请稍后重试(E000208) |
| 500 | message.list.throwable | %s | 系统异常，请稍后重试（E000131） |
| 500 | message.not.exist | %s | 需要删除的消息不存在，无法删除，请检查后重试（E000162） |
| 500 | message.not.user | %s | 创建AI助理的运行任务前未创建角色为user的消息，请创建消息后再重试(E000034) |
| 500 | message.order.invalid | %s | 传入的order参数不合法，只允许"asc"和"desc"，请检查后重试(E000157) |
| 500 | message.param.error | %s | 传入的参数中ThreadId或者MessageId不存在，请检查后重试（E000161） |
| 500 | message.param.invalid | %s | 传入的参数中ThreadId或者MessageId不合法，请检查后重试（E000155） |
| 500 | message.retrieve.error | %s | 系统异常，请稍后重试（E000031） |
| 500 | message.retrieve.exception | %s | 系统异常，请稍后重试(E000188)；系统异常，请稍后重试(E000189) |
| 500 | message.retrieve.throwable | %s | 系统异常，请稍后重试(E000130) |
| 500 | message.role.error | %s | 创建消息时，消息角色有误，请检查后重试（E000127） |
| 500 | message.send.error | 发送消息失败 | 发送消息失败 |
| 500 | message.system.error | %s | 系统异常(E000023) |
| 500 | message.threadId.invalid | %s | 获取消息列表时，传入的ThreadId不合法或者该Thread实例不存在（E000159） |
| 500 | microInvisibleToUser | 用户不在应用可见范围内 | 用户不在应用可见范围内 |
| 500 | model.absent | 模型不存在 | 模型不存在，请确认模型是否部署 |
| 500 | model.timeout | 模型超时 | 模型服务超时，请稍后再试 |
| 500 | no.enterpriseauth | 您没有相关企业权限 | 您没有相关企业权限 |
| 500 | no.fileAuth | 抱歉，你没有权限发表评论 | 抱歉，你没有权限发表评论 |
| 500 | no.permission | 无权限，请联系管理员执行该操作 | 无权限，请联系管理员执行该操作 |
| 500 | noapp.manage.permission | 请先确保您拥有全局应用管理权限，或请相关权限管理员进行删除操作 | 请先确保您拥有全局应用管理权限，或请相关权限管理员进行删除操作 |
| 500 | not.have.permission | 当前组织没有红点推送权限 | 当前组织没有红点推送权限 |
| 500 | org.benefit.error | 当前组织无操作组织技能库权益，请联系管理员升级钉钉版本权益后进行使用（E000335） | 当前组织无操作组织技能库权益，请联系管理员升级钉钉版本权益后进行使用（E000335） |
| 500 | org.maxsize.limit | 企业AI助理数量已达到上限，请清理企业AI助理后再重试 | 企业AI助理数量已达到上限，请清理企业AI助理后再重试 |
| 500 | orgId.is.null | orgId请求参数为空 | orgId请求参数为空 |
| 500 | param.callbackRouteKeyExist | param.callbackRouteKeyExist | 回调 RouteKey 已存在 |
| 500 | parametar.color.wrong | 荣誉勋章背景色不符合要求 | 荣誉勋章背景色不符合要求 |
| 500 | parameter.expirationTimeWrong | 过期时间如果传值，需大于发放当天，且小于365天后 | 过期时间如果传值，则需大于发放当天，且小于365天后 |
| 500 | parameter.grantNameOverLength | 授予人名称需在50个字以内 | 授予人名称需在50个字以内 |
| 500 | parameter.grantOverSize | 最多可以颁发给10个人 | 最多可以颁发给10个人 |
| 500 | parameter.grantReasonOverSize | 颁奖词需在100个字以内 | 颁奖词需在100个字以内 |
| 500 | parameter.illeaglParam | 传入的参数为空 | 传入的参数为空 |
| 500 | parameter.illegalRequest | 传入的参数为空 | 传入的参数为空 |
| 500 | parameter.maxResultsIllegal | maxResults需小于100 | maxResults的取值范围为1～100 |
| 500 | parameter.maxResultsIllegal | 传入的参数中maxResults需小于100 | 传入的参数中maxResults需小于100 |
| 500 | parameter.media.wrong | 图片等多媒体素材非钉钉media\_id格式 | 图片等多媒体素材非钉钉media\_id格式，请检查图片尺寸是否满足文档要求 |
| 500 | parameter.nextTokenBlank | nextToken为空 | 传入的参数中nextToken为空 |
| 500 | parameter.nextTokenBlank | 传入的参数中nextToken为空 | 传入的参数中nextToken为空 |
| 500 | parameter.orgNotExists | 组织不存在 | 组织不存在 |
| 500 | parameter.requestNull | 传入的参数为空 | 传入的参数为空 |
| 500 | parameter.text.large | 荣誉勋章名称或描述长度不符合要求 | 荣誉勋章名称或描述长度不符合要求 |
| 500 | parameter.text.unsafe | 文案含有敏感词 | 文案含有敏感词 |
| 500 | parameter.userIdBlank | userId为空 | 传入的参数中userId为空 |
| 500 | parameter.userNotExist | 用户不在组织内 | 用户不在组织内 |
| 500 | parameter.userNotExist | 用户不存在 | 用户不存在 |
| 500 | parameter.userNotExists | 用户不存在 | 用户不存在 |
| 500 | parameter.wrong | 参数为空或不符合文档要求 | 参数为空或不符合文档要求 |
| 500 | parameter.wrong | 荣誉勋章Id或者员工userId错误 | 荣誉勋章Id或者员工userId错误 |
| 500 | plugin.not.exist | 插件不存在 | 插件不存在 |
| 500 | private.maxsize.limit | 个人AI助理数量已达到上限，请清理个人AI助理后再重试 | 个人AI助理数量已达到上限，请清理个人AI助理后再重试 |
| 500 | privatedelete.permission.denied | 个人AI助理需由创建者进行删除 | 个人AI助理需由创建者进行删除 |
| 500 | request.often | 请求太频繁 | 请求太频繁 |
| 500 | return.field.empty | 配置返回字段为空 | 配置返回字段为空 |
| 500 | revertTask.hsfIntegration.error | 退回任务系统执行失败，请稍后重试或联系钉钉客服处理 | 退回任务系统执行失败，请稍后重试或联系钉钉客服处理 |
| 500 | robot.sendMessage.error | 机器人发送消息失败 | 机器人发送消息失败 |
| 500 | run.accesstoken.error | %s | 校验AccessToken失败，请检查AccessToken是否有效，并检查"AI.Assistant.Run"该权限点已经授权；校验AccessToken失败，请检查AccessToken是否有效，并检查"AI.Assistant.Run.Me"该权限点已经授权 |
| 500 | run.assistant.error | %s | 系统繁忙，请稍后重试（E000150） |
| 500 | run.assistantparam.error | %s | 创建Run实例时 传入的assistantId不合法或者该助理本身不存在 |
| 500 | run.authuser.error | %s | 系统繁忙，请稍后重试（E000084） |
| 500 | run.create.error | %s | AI助理创建运行实例失败(E000019) |
| 500 | run.create.exception | %s | 系统繁忙，请稍后重试(E000119) |
| 500 | run.create.throwable | %s | 系统繁忙，请稍后重试（E000121） |
| 500 | run.lastmessage.invalid | %s | 创建运行实例失败，请确认当前Thread中有最新的用户输入。即Thread中最新的一条消息的角色是user，再进行重试 |
| 500 | run.limit.error | %s | 查询Run实例数目的配置值不合法， 单次查询不允许超过100个 |
| 500 | run.list.error | %s | 系统繁忙，请稍后重试(E000021) |
| 500 | run.list.exception | %s | 系统繁忙，请稍后重试(E000122) |
| 500 | run.message.exception | %s | 系统异常，请稍后重试(E000189) |
| 500 | run.order.error | %s | 传入的order参数不合法，只允许"asc"和"desc"，请检查后重试 |
| 500 | run.params.error | %s | 传入的参数中ThreadId或者RunId不存在，请检查后重试 |
| 500 | run.planning.error | %s | 系统繁忙，请稍后重试（E000022） |
| 500 | run.retrieve.error | %s | 系统繁忙，请稍后重试(E000004)；系统繁忙，请稍后重试（E000004） |
| 500 | run.retrieve.exception | %s | 系统繁忙，请稍后重试(E000114) |
| 500 | run.retrieve.throwable | %s | 系统异常，请稍后重试(E000130) |
| 500 | run.strategytype.invalid | %s | 创建Run时指定了无效的运行策略参数 |
| 500 | run.thread.exception | %s | 系统异常，请稍后重试(E000188) |
| 500 | run.token.error | %s | 校验AccessToken失败，请检查AccessToken是否有效，并检查"AI.Assistant.Run"该权限点已经授权 |
| 500 | send.ding.exception | 发送DING消息异常 | 发送DING消息异常 |
| 500 | server.error | %s | 请参考ErrorMessage中的errorMessage内容 |
| 500 | server.error | server.error | 服务器意外错误；系统内部服务错误 |
| 500 | server.error | system error | 系统内部服务错误；系统内部服务错误。 |
| 500 | service.code.invalid | 数据服务编码无效 | 数据服务编码无效 |
| 500 | service.code.invalid | 数据服务编码无效:serviceId不属于本组织 | 数据服务编码无效:serviceId不属于本组织 |
| 500 | service.common.error | %s | 系统错误 |
| 500 | service.error | 系统内部调用错误 | 一些内部意外错误，比如调用超时；系统内部调用错误 |
| 500 | service.error | 系统错误 | 系统错误 |
| 500 | service.meta.isNull | service meta信息为空 | service meta信息为空 |
| 500 | service.not.found | 数据服务未找到 | 数据服务未找到 |
| 500 | service.not.online | 该服务未上架 | 该服务未上架 |
| 500 | service.org.error | %s | 企业信息获取异常 |
| 500 | service.role.error | %s | 用户角色信息获取异常 |
| 500 | service.system.error | 系统错误 | 依赖服务调用失败时抛这个错误 |
| 500 | service.user.error | %s | 用户信息获取异常 |
| 500/503 | serviceBusy | The server is busy and unable to complete your request. Please try again later. | 服务繁忙，请稍后重试。 |
| 500 | serviceError | error:%s | 系统服务错误 |
| 500 | serviceError | systemError | 系统服务错误 |
| 500 | serviceId.is.null | serviceId为空 | serviceId为空 |
| 500 | size.error | 删除实例个数超出限制 | 参数错误 |
| 500 | size.error | 更新实例数超出限制 | 参数错误 |
| 500 | staffNotFound | 员工信息未找到 | 员工信息未找到 |
| 500 | statDate.format.iserror | statDate请求参数格式不正确，正确格式：yyyyMMdd | statDate请求参数格式不正确，正确格式：yyyyMMdd |
| 500 | statDate.is.null | statDate请求参数为空 | statDate请求参数为空 |
| 500 | swform.getFormInstance.sysError | swform.getFormInstance.sysError | 获取填表实例详情系统异常 |
| 500 | swform.listFormInstances.sysError | swform.listFormInstances.sysError | 获取填表实例列表系统异常 |
| 500 | swform.listFormSchemasByCreator.sysError | swform.listFormInstances.sysError | 获取用户创建的填表模板列表系统异常 |
| 500 | system.busy | system.busy | 系统繁忙 |
| 500 | system.busy | 系统内部错误 | 系统内部错误 |
| 500 | system.busy | 系统繁忙 | 内部服务发生的异常情况；系统异常错误；系统繁忙 |
| 500 | system.busy | 系统繁忙，请稍后再试 | 系统繁忙；系统繁忙，请稍后再试 |
| 500 | system.busy | 系统错误 | 系统错误 |
| 500 | system.check.limit | 剩余审核次数不足 | 剩余审核次数不足 |
| 500 | system.corp.noauth | 组织已认证且激活人数大于6人才可提交审核 | 组织已认证且激活人数大于6人才可提交审核 |
| 500 | system.error | SYSTEM\_ERROR | 系统异常 |
| 500 | system.error | system error %s | 系统错误 |
| 500 | system.error | systemError:%s | 系统错误 |
| 500 | system.error | 删除配置出错 | 删除配置出错 |
| 500 | system.error | 可见性更新失败 | 可见性更新失败 |
| 500 | system.error | 推送失败：%s | 系统错误导致推送失败 |
| 500 | system.error | 操作失败 | 操作失败 |
| 500 | system.error | 更新失败 | 更新失败 |
| 500 | system.error | 更新设置出错 | 更新设置出错 |
| 500 | system.error | 更新错误 | 更新错误 |
| 500 | system.error | 查询服务出错 | 查询服务出错 |
| 500 | system.error | 系统内部异常 | 系统内部异常 |
| 500 | system.error | 系统内部错误 | 系统内部错误 |
| 500 | system.error | 系统繁忙 | 系统繁忙 |
| 500 | system.error | 系统繁忙，请稍后再试 | 系统发生异常；系统繁忙，请稍后再试 |
| 500 | system.error | 系统错误:%s | 系统错误；问答系统错误 |
| 500 | system.error | 获取设置出错 | 获取设置出错；获取配置出错 |
| 500 | system.error | 获取配置出错 | 获取配置出错 |
| 500 | system.error.campusProjectContactNotInit | %s | 项目通讯录未初始化 |
| 500 | system.error.contact | %s | 创建项目失败；删除通讯录部门失败 |
| 500 | system.error.existProject | %s | 删除项目组失败，项目组下仍有园区项目 |
| 500 | system.freq.limit | 请求频繁，创建荣誉勋章不支持并发调用 | 请求频繁，创建荣誉勋章不支持并发调用 |
| 500 | system.image.large | 图片文件大小超过限制 | 图片文件大小超过限制 |
| 500 | system.userNotAdmin | 用户无权限新建荣誉勋章 | 用户无权限新建荣誉勋章 |
| 500 | system.userNotExist | 用户不在组织内 | 用户不在组织内 |
| 500 | systemBusy | SYSTEM BUSY | 系统繁忙 |
| 500 | systemBusy | 系统繁忙 | 系统异常错误；系统繁忙 |
| 500 | systemError | 100000，系统异常 | 系统异常 |
| 500 | systemError | SYSTEM ERROR | 系统内部错误；系统异常；系统错误；系统处理出错。；系统异常。；系统错误 |
| 500 | systemError | error:%s | 系统错误 |
| 500 | systemError | system error %s | 未知错误；系统错误 |
| 500 | systemError | system error %s %s | 系统错误 |
| 500 | systemError | system error, %s %s | 系统错误 |
| 500 | systemError | systemError | 系统错误 |
| 500 | systemError | systemError:%s | 服务端内部错误；系统错误 |
| 500 | systemError | 系统繁忙 | 系统繁忙 |
| 500 | systemError | 系统繁忙，请稍后再试 | 兜底错误码 |
| 500 | systemError.busy | 请求太频繁 | 请求被限流 |
| 500 | systemError.messageStatus | illegal message status | 消息状态异常 |
| 500 | systemInnerError | 系统繁忙 | 系统繁忙，请稍后再试 |
| 500 | systemInnerError | 系统繁忙，请稍后再试 | 系统繁忙，请稍后再试 |
| 500 | systerm.error | 系统错误 | 系统错误 |
| 500 | sytem.error | system error %s | 创建失败；系统错误 |
| 500 | teamNameDuplicate | 团队名称已存在 | 团队名称已存在 |
| 500 | teamNameInvalid | 团队名称非法 | 团队名称非法 |
| 500 | template.error | 表单模板已停用，联系管理员启用 | 表单模板已停用，联系管理员启用 |
| 500 | thread.create.error | %s | 系统异常，请稍后重试（E000014） |
| 500 | thread.create.exception | %s | 系统异常，请稍后重试（E000181） |
| 500 | thread.create.throwable | %s | 系统异常，请稍后重试（E000113） |
| 500 | thread.delete.error | %s | 系统异常，请稍后重试（E000018） |
| 500 | thread.delete.exception | %s | 系统异常，请稍后重试(E000183) |
| 500 | thread.delete.throwable | %s | 系统异常，请稍后重试（E000120） |
| 500 | thread.not.exist | %s | 传入ThreadId有误，未查询到相关信息，请检查线程信息后重试(E000015)；传入ThreadId有误，未查询到相关信息，请检查线程信息后重试（E000015） |
| 500 | thread.retrieve.error | %s | 系统异常，请稍后重试(E000116)；系统异常，请稍后重试(E000188)；系统异常，请稍后重试（E000016） |
| 500 | thread.retrieve.exception | %s | 系统异常，请稍后重试(E000188)；系统异常，请稍后重试（E000188） |
| 500 | todo.orgTaskQuery.systemError | todo.orgTaskQuery.systemError | 查询企业待办列表系统内部异常 |
| 500 | todo.taskDelete.systemError | todo.taskDelete.systemError | 删除待办系统异常 |
| 500 | todo.taskExecutorStatusUpdate.systemError | todo.taskExecutorStatusUpdate.systemError | 更新待办执行者状态系统异常 |
| 500 | todo.taskUpdate.systemError | todo.taskUpdate.systemError | 更新待办系统异常 |
| 500 | type.error | 表单类型错误 | 表单类型错误 |
| 500 | unclassifiedError | 宜搭未分类的异常信息:%s | 宜搭未分类的异常信息 |
| 500 | unclassifiedError | 异常:%s | 宜搭未分类的异常信息；通用异常信息 |
| 500 | unknown.error | Unknown Error | 未知错误 |
| 500 | unknown.error | unknownError | 未知错误 |
| 500/502/503 | unknownError | Unknown Error | 未知错误 |
| 500/503 | unknownError | 未知错误 | 未知错误 |
| 500 | update.error | 更新实例数据失败 | 更新实例数据失败 |
| 500 | user.not.found | 该员工不在企业中 | 该员工不在企业中 |
| 501 | campus.noRoot | 项目通讯录未初始化 | 项目通讯录未初始化 |
| 501 | department.notExist | 部门不存在 | 部门不存在 |
| 501 | illegal.field.notnull | 当前字段不能为空 %s | 当前字段不能为空 %s |
| 502 | - | Bad Gateway | 网关错误，上游服务异常。 |
| 502 | campus.notFit | 非园区租户组织 | 非园区租户组织 |
| 503 | - | Service Unavailable | 服务不可用，系统过载。 |
| 503 | operationTimeout | %s | 请求超时 |
| 503 | systemError.dingSpaceError | 钉盘服务不可用 | 钉盘服务不可用，可以稍后重试 |
| 504 | - | Gateway Timeout | 网关超时。 |
| 504 | service.timeout | The server is busy and unable to complete your request. Please try again later. | 请求超时 |
| 999 | error.unknownerror | %s | %s |
| -1 | 系统繁忙 | 系统繁忙。服务器暂不可用，建议稍后再重试1次，最多重试3次。 |  |
| 0 | 请求成功 | 请求成功。接口调用成功。 |  |
| 200001 | 表单不能为空 | 表单不能为空。无。 |  |
| 200002 | 分页参数index或offset不合法 | 分页参数index或offset不合法。检查一下对应接口的分页参数。 |  |
| 200003 | 分页大小不合法 | 分页大小不合法。检查一下对应接口的分页参数。 |  |
| 200004 | APP\_ID 不允许为空 | APP\_ID 不允许为空。app\_id为创建套件成功后，创建的ISV微应用的微应用ID。 可以登录开发者后台查看。 |  |
| 200005 | 表单名称不允许为空 | 表单名称不允许为空。无。 |  |
| 200006 | 表单内容不允许为空 | 表单内容不允许为空。无。 |  |
| 200007 | 表单值不允许为空 | 表单值不允许为空。无。 |  |
| 200008 | 表单uuid不存在 | 表单uuid不存在。无。 |  |
| 33001 | 无效的企业ID | 无效的企业ID。请确认access\_token是否正确。 |  |
| 33002 | 无效的微应用的名称 | 无效的微应用的名称。校验微应用的名称字段，不能为空且长度不能超过10个字符。 |  |
| 33003 | 无效的微应用的描述 | 无效的微应用的描述。校验微应用的描述字段，不能为空且长度不能超过20个字符。 |  |
| 33004 | 无效的微应用的ICON | 无效的微应用的ICON。校验微应用的icon字段，不能为空且确保图标存在。 |  |
| 33005 | 无效的微应用的移动端主页 | 无效的微应用的移动端主页。校验微应用的移动端主页，不能为空且必须以http开头或https开头 |  |
| 33006 | 无效的微应用的PC端主页 | 无效的微应用的PC端主页。校验微应用的PC端主页，必须以http开头或https开头。 |  |
| 33007 | 微应用的移动端的主页与PC端主页不同 | 微应用的移动端的主页与PC端主页不同。校验微应用的PC端主页，确保它和移动端主页的域名保持一致。 |  |
| 33008 | 无效的微应用OA后台的主页 | 无效的微应用OA后台的主页。校验下微应用的后台管理的主页失败，必须以http开头或https开头。 |  |
| 33012 | 无效的USERID | 无效的USERID。请检查userid是否正确，可通过[获取部门用户userid列表](0065-query-the-list-of-department-userids.md)接口获取。 |  |
| 33013 | 企业自建微应用的个数过多，通过接口创建微应用受限 | 企业自建微应用的个数过多，通过接口创建微应用受限。此限制只针对企业自建微应用，对ISV应用没有限制。 |  |
| 34001 | 无效的会话id | 无效的会话id。检查下所传的chatId字段是否为空。可通过[创建群](1481-session-management-creates-groups.md)接口获取chatId。 |  |
| 34002 | 无效的会话消息的发送者 | 无效的会话消息的发送者。检查下sender字段是否为空。 |  |
| 34003 | 无效的会话消息的发送者的企业Id | 无效的会话消息的发送者的企业Id。检查下发送者的企业Id。可在[开发者后台](https://open-dev.dingtalk.com/#/index)首页获取。 |  |
| 34004 | 无效的会话消息的类型 | 无效的会话消息的类型。检查下msgtype字段，是否为空，是否是定义的类型。msgtype请参考[消息通知类型](0775-message-types-and-data-format.md)。 |  |
| 34006 | 发送者不在企业中 | 发送者不在企业中。检查下发送者是否在企业中。可通过[获取部门用户基础信息](0066-queries-the-simple-information-of-a-department-user.md)查看。 |  |
| 34007 | 发送者不在会话中 | 发送者不在会话中。检查下发送者是否在会话id中。可通过[查询群成员](0751-query-group-members.md)接口查看。 |  |
| 34008 | 图片不能为空 | 图片不能为空。如果发的是图片消息，检查下图片是否为空。 |  |
| 34009 | 链接内容不能为空 | 链接内容不能为空。检查下messageUrl字段是否为空。 |  |
| 34010 | 文件不能为空 | 文件不能为空。检查下media\_id字段是否为空。可通过[上传媒体文件](0646-upload-media-files.md)接口获取。 |  |
| 34011 | 音频文件不能为空 | 音频文件不能为空。检查下media\_id字段是否为空。可通过[上传媒体文件](0646-upload-media-files.md)接口获取。 |  |
| 34012 | 找不到发送者的企业 | 找不到发送者的企业。检查下发送者是否是真实的。可通过[获取部门用户userid列表](0065-query-the-list-of-department-userids.md)接口获取。 |  |
| 34013 | 找不到群会话对象 | 找不到群会话对象。检查下chatid是否真实存在。可通过[查询群信息](0740-obtain-a-group-session.md)接口查看。 |  |
| 34014 | 会话消息的json结构无效或不完整 | 会话消息的json结构无效或不完整。检查下消息的json格式是否正确，json的key对应msgtype的value值。 |  |
| 34015 | 发送群会话消息失败 | 发送群会话消息失败。消息发送失败，建议稍后再重试下。 |  |
| 34016 | 会话消息的内容超长 | 会话消息的内容超长。检查下消息的content字段长度是否超过5000，title字段长度是否超过64，markdown字段长度是否超过5000，single\_title字段长度是否超过20，single\_url字段长度是否超过500，btn\_json\_list字段长度是否超过1000。 |  |
| 34018 | 角色信息不能为空 | 角色信息不能为空。检查参数roleName、groupId是否正确。 |  |
| 40000 | 参数错误 | 参数错误。请检查接口入参是否正确。 |  |
| 400001 | 系统错误 | 系统错误。无。 |  |
| 400002 | 参数错误 | 参数错误。检查参数是否符合规格。具体请参考当前接口的文档的参数说明和参数示例。 |  |
| 400003 | 时间戳无效 | 时间戳无效。检查随机时间戳是否符合规格。具体请参考当前接口的文档的参数说明和参数示例 |  |
| 400004 | 随机数无效 | 随机数无效。检查随机随机数是否符合规格。具体请参考当前接口的文档的参数说明和参数示例。 |  |
| 40001 | 获取access\_token时Secret错误，或者access\_token无效 | 获取access\_token时Secret错误，或者access\_token无效。检查下access\_token是否正确。 |  |
| 400010 | 激活的设备不存在（未绑定） | 激活的设备不存在（未绑定）。无。 |  |
| 400011 | 设备已经激活 | 设备已经激活。无。 |  |
| 40002 | 不合法的凭证类型 | 不合法的凭证类型。无。 |  |
| 400020 | 无访问权限 | 无访问权限。无。 |  |
| 400021 | 密钥错误 | 密钥错误。无。 |  |
| 400022 | 设备不存在 | 设备不存在。无。 |  |
| 400023 | 用户不存在 | 用户不存在。无。 |  |
| 40003 | 不合法的UserID | 不合法的UserID。确保该id在通讯录中存在，且是在你所传access\_token对应的企业里。可通过[获取部门用户userid列表](0065-query-the-list-of-department-userids.md)接口获取。 |  |
| 40004 | 不合法的媒体文件类型 | 不合法的媒体文件类型。检查下type字段，只支持image、voice、file。 |  |
| 400040 | 回调不存在 | 回调不存在。检查是否注册回调事件。可通过[查询订阅事件](../04-LFcRvVD08N-事件订阅/0236-query-subscribed-events.md)接口获取。 |  |
| 400041 | 回调已经存在 | 回调已经存在。检查该回调事件是否已注册过。可通过[查询订阅事件](../04-LFcRvVD08N-事件订阅/0236-query-subscribed-events.md)接口获取。 |  |
| 400042 | 企业不存在 | 企业不存在。无。 |  |
| 400043 | 企业不合法 | 企业不合法。无。 |  |
| 40005 | 不合法的文件类型 | 不合法的文件类型。如果是文件类型，检查下是否是支持。目前只支持doc、docx、xls、xlsx、ppt、pptx、zip、pdf、rar。 |  |
| 400050 | 回调地址无效 | 回调地址无效。检查回调地址是否正确或者符合地址格式。 |  |
| 400051 | 回调地址访问异常 | 回调地址访问异常。回调地址必须部署到外网以便开发平台通过回调地址推送回调信息。 |  |
| 400052 | 回调地址访返回数据错误 | 回调地址访返回数据错误。无。 |  |
| 400053 | 回调地址在黑名单中无法注册 | 回调地址在黑名单中无法注册。回调地址已添加黑名单，无法注册。 |  |
| 400054 | 回调URL访问超时 | 回调URL访问超时。无。 |  |
| 400055 | 回调设备不在线 | 回调设备不在线。无。 |  |
| 400056 | 回调访问设备失败 | 回调访问设备失败。无。 |  |
| 400057 | 回调访问设备不存在 | 回调访问设备不存在。无。 |  |
| 40006 | 不合法的文件大小 | 不合法的文件大小。检查下文件大小，image类型最大1MB，file类型最大10MB，voice类型最大2MB。 |  |
| 40007 | 不合法的媒体文件id | 不合法的媒体文件id。检查下mediaId是否为空，是否真实存在。可通过[上传媒体文件](0646-upload-media-files.md)接口获取。 |  |
| 40008 | 不合法的消息类型 | 不合法的消息类型。检查下msgtype是否为空，确保它在开放平台定义的几种类型里，msgtype请参考[消息通知类型](0775-message-types-and-data-format.md)。 |  |
| 40009 | 不合法的部门id | 不合法的部门id。检查下部门id是否为空，是否为数字且大于0。可通过[获取部门列表](0082-user-management-acquires-the-list-departments.md)接口查看。 |  |
| 40010 | 不合法的父部门id | 不合法的父部门id。检查父部门id是否为一个数字。可通过[获取指定用户的所有父部门列表](0085-queries-the-list-of-all-parent-departments-of-a-user.md)或[获取指定部门的所有父部门列表](0084-query-the-list-of-all-parent-departments-of-a-department.md)接口获取。 |  |
| 40011 | 不合法的排序order | 不合法的排序order。检查下order字段是否为空，是否为数字且大于0。 |  |
| 40012 | 不合法的发送者 | 不合法的发送者。检查下sender字段是否为空，是否真实存在。 |  |
| 40013 | 不合法的corpid | 不合法的corpid。检查下corpid是否有效。corpid参数可在[开发者后台](https://open-dev.dingtalk.com/#/index)首页获取。 |  |
| 40014 | 不合法的access\_token | 不合法的access\_token。检查下access\_token是否正确。 **重要** access\_token这个参数应该是带在url后面的。 |  |
| 40015 | 发送者不在会话中 | 发送者不在会话中。检查下sender字段和cid字段是否能对应上。 |  |
| 40016 | 不合法的会话ID | 不合法的会话ID。检查下cid字段是否为空，是否有效。 |  |
| 40017 | 在会话中没有找到与发送者在同一企业的人 | 在会话中没有找到与发送者在同一企业的人。cid对应的消息接收者为空，检查下cid字段。 |  |
| 40018 | 不允许以递归方式查询部门用户列表 | 不允许以递归方式查询部门用户列表。检查下fetchChild字段，目前不支持递归查询。 |  |
| 40019 | 该手机号码对应的用户最多可以加入5个非认证企业 | 该手机号码对应的用户最多可以加入5个非认证企业。更换手机号码后重试。 |  |
| 40020 | 当前团队人数已经达到上限，用电脑登录钉钉企业管理后台，升级成为认证企业 | 当前团队人数已经达到上限，用电脑登录钉钉企业管理后台，升级成为认证企业。用电脑登录钉钉企业管理后台，升级成为认证企业。 |  |
| 40021 | 更换的号码已注册过钉钉，无法使用该号码 | 更换的号码已注册过钉钉，无法使用该号码。使用未注册钉钉的手机号。 |  |
| 40022 | 企业中的手机号码和登录钉钉的手机号码不一致，暂时不支持修改用户信息，可以删除后重新添加 | 企业中的手机号码和登录钉钉的手机号码不一致，暂时不支持修改用户信息，可以删除后重新添加。暂时不支持修改用户信息，可以删除后重新添加。 |  |
| 40023 | 部门人数达到上限 | 部门人数达到上限。部门人数不能超过1000。 |  |
| 40024 | (安全校验不通过)保存失败，团队人数超限。请在手机钉钉绑定支付宝完成实名认证，或者申请企业认证，人数上限自动扩充 | (安全校验不通过)保存失败，团队人数超限。请在手机钉钉绑定支付宝完成实名认证，或者申请企业认证，人数上限自动扩充。手机绑定支付宝完成实名认证或者申请企业认证，人数上限自动扩充。 |  |
| 40025 | 无效的部门JSONArray对象，合法格式需要用中括号括起来，且如果属于多部门，部门id需要用逗号分隔 | 无效的部门JSONArray对象，合法格式需要用中括号括起来，且如果属于多部门，部门id需要用逗号分隔。合法格式需要用中括号括起来，且如果属于多部门，部门id需要用逗号分隔。 |  |
| 40029 | 不合法的oauth\_code | 不合法的oauth\_code。无。 |  |
| 40031 | 不合法的UserID列表 | 不合法的UserID列表。指定的UserID列表，至少存在一个UserID不在通讯录中。 |  |
| 40032 | 不合法的UserID列表长度 | 不合法的UserID列表长度。检查下列表是否为空，且长度合适。创建部门接口的userPerimits最多接收10000个。 |  |
| 40033 | 不合法的请求字符，不能包含\uxxxx格式的字符 | 不合法的请求字符，不能包含\uxxxx格式的字符。检查请求字符是否正确，不能包含\uxxxx格式的字符。 |  |
| 40035 | 不合法的参数 | 不合法的参数。检查下有没有传请求参数，一般发生在http post形式的接口里，没有传参数。 |  |
| 40038 | 不合法的请求格式 | 不合法的请求格式。检查下参数中是不是少了某个字段，具体参考各个文档的参数介绍。 |  |
| 40039 | 不合法的URL长度 | 不合法的URL长度。无。 |  |
| 40048 | url中包含不合法domain | url中包含不合法domain。发消息接口中消息url链接不安全。 |  |
| 40056 | 不合法的agentid | 不合法的agentid。检查下agentid字段是否为空，是否真实存在。 |  |
| 40057 | 不合法的callbackurl | 不合法的callbackurl。无。 |  |
| 40061 | 设置应用头像失败 | 设置应用头像失败。无。 |  |
| 40062 | 不合法的应用模式 | 不合法的应用模式。无。 |  |
| 40063 | 不合法的分机号 | 不合法的分机号。tel字段长度超长，长度不能超过50。 |  |
| 40064 | 不合法的工作地址 | 不合法的工作地址。workPlace长度超长，长度不能超过50个字符。 |  |
| 40065 | 不合法的备注 | 不合法的备注。remark长度超长，长度不能超过1024个字符。 |  |
| 40066 | 不合法的部门列表 | 不合法的部门列表。部门id列表长度太长，不能超过10000，并且每个id必须是数字。 |  |
| 40067 | 标题长度不合法 | 标题长度不合法。检查下标题长度。 |  |
| 40068 | 不合法的偏移量 | 不合法的偏移量。偏移量必须大于0。 |  |
| 40069 | 不合法的分页大小 | 不合法的分页大小。分页大小不合法，具体参考每个接口的参数定义。 |  |
| 40070 | 不合法的排序参数 | 不合法的排序参数。具体参考获取部门成员接口里面对order字段的定义。 |  |
| 40073 | 不存在的openid | 不存在的openid。openid不能为空。可通过[根据sns临时授权码获取用户信息](https://open.dingtalk.com/document/orgapp/obtain-the-user-information-based-on-the-sns-temporary-authorization)接口获取。 |  |
| 40077 | 不存在的预授权码 | 不存在的预授权码。无。 |  |
| 40078 | 不存在的临时授权码 | 不存在的临时授权码。临时授权码不能为空，且只能被使用一次，可参见以下接口： \* 小程序：[免登授权码](https://open.dingtalk.com/document/orgapp/mini-program-free-login) \* H5微应用：[免登流程](https://open.dingtalk.com/document/orgapp/logon-free-process) |  |
| 40079 | 不存在的授权信息 | 不存在的授权信息。检查下企业是否授权，授权方法参考[应用授权](0041-overview-of-application-licensing.md)。 |  |
| 40080 | 不合法的suitesecret | 不合法的suitesecret。无。 |  |
| 40082 | 不合法的suitetoken | 不合法的suitetoken。检查下token。 |  |
| 40083 | 不合法的suiteid | 不合法的suiteid。suiteKey字段不合法。 |  |
| 40084 | 不合法的永久授权码 | 不合法的永久授权码。检查下永久授权码是否正确。可通过[获取授权企业的永久授权码](https://open.dingtalk.com/document/isvapp/obtain-a-permanent-authorization-code)接口获取。 |  |
| 40085 | 不存在的suiteticket | 不存在的suiteticket。检查下suiteticket是否正确，确保是由回调接口正确来接收suiteticket。 |  |
| 40086 | 不合法的第三方应用appid | 不合法的第三方应用appid。appid字段不能为空。 |  |
| 40087 | 创建永久授权码失败 | 创建永久授权码失败。稍后再重试下，确保参数都传对。 |  |
| 40088 | 不合法的套件key或secret | 不合法的套件key或secret。稍后再重试下，确保suiteKey和suiteSecret都传对且一一对应。 |  |
| 40089 | 不合法的corpId或corpSecret | 不合法的corpid或corpsecret。如果你使用的是corpsecret，请稍后再重试下，确保corpid和corpsecret字段传对且一一对应。 |  |
| 40090 | 套件已经不存在 | 套件已经不存在。检查下suiteKey字段是否正确。 |  |
| 40091 | 用户授权码创建失败，需要用户重新授权 | 用户授权码创建失败，需要用户重新授权。创建永久授权码失败，需要用户重新授权产生临时授权码。 |  |
| 40100 | 分机号已经存在 | 分机号已经存在。无。 |  |
| 40101 | 邮箱已经存在 | 邮箱已经存在。无。 |  |
| 40102 | 过期的临时授权码 | 过期的临时授权码。临时授权只能使用一次后就不能在使用。 需要重新执行授权操作有开放平台推送新的临时授权码。 |  |
| 40103 | 该用户需要其同意才可添加，已向对方发送邀请 | 用户开启了账号保护，无法被加入到您的团队。由于通讯录添加新用户的保护机制导致。如一个员工已经存在于一个A企业，且A为认证企业，B企业再添加该员工的时候会提示。可以让该员工在钉钉客户端搜索"成员邀请"查看邀请信息，并点击加入。 |  |
| 40104 | 电话号码无效 | 无效手机号。检查手机号格式是否正确。 |  |
| 404 | 请求的URI地址不存在 | 请求的URI地址不存在。地址不存在，检查下url是否和文档里写的一致。 |  |
| 41001 | 缺少access\_token参数 | 缺少access\_token参数。检查下access\_token是否传了，注意该参数必须跟在请求url中。 |  |
| 41002 | 缺少corpid参数 | 缺少corpid参数。检查下corpid是否为空。corpid参数可在[开发者后台](https://open-dev.dingtalk.com/#/index)首页获取。 |  |
| 41003 | 缺少refresh\_token参数 | 缺少refresh\_token参数。检查下refresh\_token是否为空。 |  |
| 41004 | 缺少secret参数 | 检查下secret参数是否为空。检查下secret参数是否为空。 |  |
| 41005 | 缺少多媒体文件数据 | 缺少多媒体文件数据。无。 |  |
| 41006 | 缺少media\_id参数 | 缺少media\_id参数。检查下media\_id参数是否为空。可通过[上传媒体文件](0646-upload-media-files.md)接口获取。 |  |
| 41007 | 无效的ssocode | 无效的ssocode。sso的永久授权code无效，检查下是否为空，可参见[获取微应用后台免登的access\_token](https://open.dingtalk.com/document/orgapp/obtain-the-ssotoken-for-micro-application-background-logon-free)。 |  |
| 41008 | 缺少oauth | 缺少oauth。无。 |  |
| 41009 | 缺少UserID | 缺少UserID。检查下UserID是否为空。 |  |
| 41010 | 缺少url | 缺少url。检查下url是否为空。 |  |
| 41011 | 缺少agentid | 缺少agentid。检查下agentid是否为空。 |  |
| 41012 | 缺少应用头像mediaid | 缺少应用头像mediaid。检查下mediaid是否为空。可通过[上传媒体文件](0646-upload-media-files.md)接口获取。 |  |
| 41013 | 缺少应用名字 | 缺少应用名字。检查应用名字是否为空。 |  |
| 41014 | 缺少应用描述 | 缺少应用描述。检查应用描述是否为空。 |  |
| 41015 | 缺少JSON参数 | 缺少JSON参数。检查JSON参数是否为空。 |  |
| 41021 | 缺少suitekey | 缺少suitekey。检查suitekey参数是否为空。 |  |
| 41022 | 缺少suitetoken | 缺少suitetoken。检查suitetoken参数是否为空。 |  |
| 41023 | 缺少suiteticket | 缺少suiteticket。检查suiteticket参数是否为空。 |  |
| 41024 | 缺少suitesecret | 缺少suitesecret。检查suitesecret参数是否为空。 |  |
| 41025 | 缺少permanent\_code | 缺少permanent\_code。检查permanent\_code永久授权码参数是否为空。可通过[获取授权企业的永久授权码](https://open.dingtalk.com/document/isvapp/obtain-a-permanent-authorization-code)接口获取。 |  |
| 41026 | 缺少tmp\_auth\_code | 缺少tmp\_auth\_code。检查tmp\_auth\_code临时授权码参数是否为空。可参见[企业授权开通应用事件](https://open.dingtalk.com/document/isvapp/enterprise-authorized-application-activation-event-1)。 **说明** 临时授权码只能使用一次。 |  |
| 41027 | 需要授权企业的corpid参数 | 需要授权企业的corpid参数。检查corpid参数是否为空。corpid参数可在[开发者后台](https://open-dev.dingtalk.com/#/index)首页获取。 |  |
| 41028 | 禁止给全员发送消息 | 禁止给全员发送消息。检查是否有全员发送消息的权限，ISV没有该权限。 |  |
| 41029 | 超过消息接收者人数上限，企业接入为5000，ISV接入为1000 | 超过消息接收者人数上限。发送OA消息人数超上限。 \* **企业消息人数上限**：5000 \* **ISV消息人数上限**：1000 |  |
| 41030 | 企业未对该套件授权 | 企业未对该套件授权。检查该企业是否已经对该套件进行授权。 |  |
| 41031 | auth\_corpid和permanent\_code不匹配 | auth\_corpid和permanent\_code不匹配。激活套件时使用的auth\_corpid和permanent\_code不匹配。授权企业的auth\_corpid可在[开发者后台](https://open-dev.dingtalk.com/#/index)首页获取。 |  |
| 41041 | 时间跨度太大 | 查询间隔时间太长。考勤打卡数据查询间隔时间超过7天。 |  |
| 41042 | 加密失败 | 加密失败。无。 |  |
| 41043 | 解密失败 | 解密失败。无。 |  |
| 41044 | 禁止发送消息 | 禁止发送消息。检查是否有权限发送消息。 |  |
| 41045 | 单应用全员消息/每天总量超限 | 超过发送全员消息的次数上限。发送全员消息的次数，每天最多3次。 |  |
| 41046 | 超过发送全员消息的每分钟次数上限 | 超过发送全员消息的每分钟次数上限。企业OA消息全员发送每天不能超过3次，ISV不能发送全员消息。 |  |
| 41047 | 超过给该企业发消息的每分钟人次上限 | 超过给该企业发消息的每分钟人次上限。企业OA消息每分钟不能超过1500次，ISV OA消息每分钟不能超过200次。 |  |
| 41048 | 超过给企业发消息的每分钟次数总上限 | 超过给企业发消息的每分钟次数总上限。无。 |  |
| 41049 | 包含违禁内容 | 包含违禁内容。检查消息文本中是否有黄色、反动等词语。 |  |
| 41050 | 无效的活动编码 | 无效的活动编码。无。 |  |
| 41051 | 活动权益的校验失败 | 活动权益的校验失败。无。 |  |
| 41054 | 暂时无法更换手机号，如需修改请删除用户后重试 | 暂时无法更换手机号，如需修改请删除用户后重试。暂不支持修改手机号，请先将员工删除后再进行修改操作。 |  |
| 41100 | 时间参数不合法 | 时间参数不合法。时间参数不能为空，且格式为："yyyy-MM-dd hh:mm:ss"。 |  |
| 41101 | 数据内容过长 | 数据内容过长。请求体字符长度不能大于4096。 |  |
| 41102 | 参数值过大 | 参数值过大。上传文件或者idlist等参数过大。 |  |
| 420001 | 客户不存在 | 客户不存在。无。 |  |
| 4200010 | 客户联系人id非法 | 客户联系人id非法。无。 |  |
| 4200011 | 客户描述表单不存在 | 客户描述表单不存在。无。 |  |
| 4200012 | 客户描述表单查询失败 | 户描述表单查询失败。无。 |  |
| 4200013 | 联系人描述表单不存在 | 联系人描述表单不存在。无。 |  |
| 4200014 | 联系人描述表单查询失败 | 联系人描述表单查询失败。无。 |  |
| 4200015 | 客户描述表单格式校验错误 | 客户描述表单格式校验错误。无。 |  |
| 4200016 | 客户描述表单格缺少固定字段 | 客户描述表单格缺少固定字段。无。 |  |
| 4200017 | 客户联系人描述表单格式校验错误 | 客户联系人描述表单格式校验错误。无。 |  |
| 4200018 | 客户联系人描述表单格缺少固定字段 | 客户联系人描述表单格缺少固定字段。无。 |  |
| 4200019 | 客户描述表单数据格式校验错误 | 客户描述表单数据格式校验错误。无。 |  |
| 420002 | 客户查询失败 | 客户查询失败。无。 |  |
| 4200020 | 客户描述表单数据缺少固定字段 | 客户描述表单数据缺少固定字段。无。 |  |
| 4200021 | 客户联系人描述表单数据格式校验错误 | 客户联系人描述表单数据格式校验错误。无。 |  |
| 4200022 | 客户联系人描述表单数据缺少固定字段 | 客户联系人描述表单数据缺少固定字段。无。 |  |
| 420003 | 联系人不存在 | 联系人不存在。无。 |  |
| 420004 | 联系人查询失败 | 联系人查询失败。无。 |  |
| 420005 | 客户删除失败 | 客户删除失败。无。 |  |
| 420006 | 联系人删除失败 | 联系人删除失败。无。 |  |
| 420007 | 跟进人绑定失败 | 跟进人绑定失败。无。 |  |
| 420008 | 客户id非法 | 客户id非法。无。 |  |
| 420009 | 跟进人id非法 | 跟进人id非法。无。 |  |
| 42001 | access\_token超时 | access\_token超时。请检查网络状态。 |  |
| 42002 | refresh\_token超时 | refresh\_token超时。请检查网络状态。 |  |
| 42003 | oauth\_code超时 | oauth\_code超时。请检查网络状态。 |  |
| 42007 | 预授权码失效 | 预授权码失效。请检查该预授权码是否已经使用过。 |  |
| 42008 | 临时授权码失效 | 临时授权码失效。请检查该临时授权码是否已经使用过或者是否不正确。 |  |
| 42009 | suitetoken失效 | suitetoken失效。请检查该suitetoken是否已经过期。 |  |
| 43001 | 需要GET请求 | 需要GET请求。请检查http请求方式是否正确。 |  |
| 43002 | 需要POST请求 | 需要POST请求。请检查http请求方式是否正确。 |  |
| 43003 | 需要HTTPS | 需要HTTPS。请检查调用接口协议是否是https。 |  |
| 43004 | 无效的HTTP HEADER Content-Type | 无效的HTTP HEADER Content-Type。请检查请求头中的content-type是否正确。 |  |
| 43005 | 需要Content-Type为application/json;charset=UTF-8 | 需要Content-Type为application/json;charset=UTF-8。请检查请求头中的content-type是否是"application/json;charset=UTF-8"。 |  |
| 43007 | 需要授权 | 需要授权。该接口需要access\_token才能调用。 |  |
| 43008 | 参数需要multipart类型 | 参数需要multipart类型。检查提交参数中的ENCTYPE是否是multipart类型。 |  |
| 43009 | post参数需要json类型 | post参数需要json类型。请检查post参数数据是否是json类型。 |  |
| 44001 | 多媒体文件为空 | 多媒体文件为空。请检查多媒体文件数据是否为空。可通过[上传媒体文件](0646-upload-media-files.md)接口获取。 |  |
| 44002 | POST的数据包为空 | POST的数据包为空。请检查POST的数据包是否为空。 |  |
| 44003 | 图文消息内容为空 | 图文消息内容为空。请检查图文消息参数是否为空。 |  |
| 44004 | 文本消息内容为空 | 文本消息内容为空。请检查文本消息参数是否为空 |  |
| 45001 | 多媒体文件大小超过限制 | 多媒体文件大小超过限制。无。 |  |
| 45002 | 消息内容超过限制 | 消息内容超过限制。无。 |  |
| 45003 | 标题字段超过限制 | 标题字段超过限制。无。 |  |
| 45004 | 描述字段超过限制 | 描述字段超过限制。无。 |  |
| 45005 | 链接字段超过限制 | 链接字段超过限制。无。 |  |
| 45006 | 图片链接字段超过限制 | 图片链接字段超过限制。无。 |  |
| 45007 | 语音播放时间超过限制 | 语音播放时间超过限制。无。 |  |
| 45008 | 图文消息超过限制 | 图文消息超过限制。无。 |  |
| 45009 | 接口调用超过限制 | 接口调用超过限制。无。 |  |
| 45016 | 系统分组，不允许修改 | 系统分组，不允许修改。无。 |  |
| 45017 | 分组名字过长 | 分组名字过长。无。 |  |
| 45018 | 分组数量超过上限 | 分组数量超过上限。无。 |  |
| 45024 | 账号数量超过上限 | 账号数量超过上限。无。 |  |
| 46001 | 不存在媒体数据 | 不存在媒体数据。无。 |  |
| 46004 | 不存在的员工 | 不存在的员工。无。 |  |
| 47001 | 解析JSON/XML内容错误 | 解析JSON/XML内容错误。无。 |  |
| 48002 | Api禁用 | Api禁用。无。 |  |
| 48003 | suitetoken无效 | suitetoken无效。请检查该suitetoken是否已经过期或不正确。 |  |
| 48004 | 授权关系无效 | 授权关系无效。无。 |  |
| 49000 | 缺少chatid | 缺少chatid。请检查参数中是否有chatid。可通过[创建群](1481-session-management-creates-groups.md)接口获取chatId。 |  |
| 49001 | 绑定的微应用超过个数限制 | 绑定的微应用超过个数限制。绑定群会话和微应用超过5个。 |  |
| 49002 | 一个群只能被一个ISV套件绑定一次 | 一个群只能被一个ISV套件绑定一次。无。 |  |
| 49003 | 操作者必须为群主 | 操作者必须为群主。无。 |  |
| 49004 | 添加成员列表和删除成员列表不能有交集 | 添加成员列表和删除成员列表不能有交集。无。 |  |
| 49005 | 群人数超过人数限制 | 群人数超过人数限制。无。 |  |
| 49006 | 群成员列表必须包含群主 | 群成员列表必须包含群主。无。 |  |
| 49007 | 超过创建群的个数上限 | 超过创建群的个数上限。无。 |  |
| 49008 | 不合法的群类型，只能传入0或2限 | 不合法的群类型，只能传入0或2。无。 |  |
| 49009 | 企业群不能添加外部联系人，群主只能为企业员工 | 企业群不能添加外部联系人，群主只能为企业员工。无。 |  |
| 49010 | 群成员不能为空 | 群成员不能为空。无。 |  |
| 49011 | 群员工列表超长 | 群员工列表超长。无。 |  |
| 49012 | 群外部联系人列表超长 | 群外部联系人列表超长。无。 |  |
| 49013 | 群主不能为空 | 群主不能为空。无。 |  |
| 49014 | 非法的群主类型，只能为emp或者ext | 非法的群主类型，只能为emp或者ext。无。 |  |
| 49015 | 不合法的群名称 | 不合法的群名称。无。 |  |
| 49016 | 查询企业员工不存在 | 查询企业员工不存在。无。 |  |
| 49017 | 查询企业外部联系人不存在 | 查询企业外部联系人不存在。可通过[获取外部联系人列表](0100-obtain-the-external-contact-list.md)接口获取。 |  |
| 49018 | 群主非企业员工 | 群主非企业员工。无。 |  |
| 49019 | 群主非企业外部通讯录人员 | 群主非企业外部通讯录人员。可通过[获取外部联系人列表](0100-obtain-the-external-contact-list.md)接口获取。 |  |
| 49020 | 某人处于勿扰模式，拒绝加入群聊；请先与TA建立好友关系 | 某人处于勿扰模式，拒绝加入群聊；请先与TA建立好友关系。无。 |  |
| 49021 | 非好友建立群聊，认证用户一天只能拉50个人，非认证用户一天只能拉10个人 | 非好友建立群聊，认证用户一天只能拉50个人，非认证用户一天只能拉10个人。无。 |  |
| 49022 | 某人拒绝加入群聊 | 某人拒绝加入群聊。无。 |  |
| 49023 | 某人处于勿扰模式，拒绝加入群聊；请先与TA建立好友关系 | 某人处于勿扰模式，拒绝加入群聊；请先与TA建立好友关系。无。 |  |
| 50001 | redirect\_uri未授权 | redirect\_uri未授权。无。 |  |
| 50002 | 企业员工不在授权范围 | 企业员工不在授权范围。1. 检查是否不在可见范围（登录[钉钉开发者后台](https://open-dev.dingtalk.com/)>**企业内部应用** -**应用详情** -**版本管理与发布** -**可使用范围设置**） 2. 检查是否在授权范围内（登录[钉钉开发者后台](https://open-dev.dingtalk.com/)> **企业内部应用 > 应用详情** > **权限管理** >**添加接口权限** > **通讯录权限** >**授权范围）** |  |
| 50003 | 应用已停用 | 应用已停用。无。 |  |
| 50004 | 企业部门不在授权范围 | 企业部门不在授权范围。1. 检查是否不在可见范围（登录[钉钉开发者后台](https://open-dev.dingtalk.com/)>**企业内部应用** -**应用详情** -**版本管理与发布** -**可使用范围设置**） 2. 检查是否在授权范围内（登录[钉钉开发者后台](https://open-dev.dingtalk.com/)> **企业内部应用 > 应用详情** > **权限管理** >**添加接口权限** > **通讯录权限** >**授权范围**） |  |
| 50005 | 企业已禁用 | 企业已禁用。无。 |  |
| 52010 | 无效的corpid | 无效的corpid。请检查corpid参数是否正确。corpid可在[开发者后台](https://open-dev.dingtalk.com/#/index)首页获取。 |  |
| 52011 | jsapi ticket 读取失败 | jsapi ticket 读取失败。请检查ticket参数是否正确。 |  |
| 52012 | jsapi 签名生成失败 | jsapi 签名生成失败。请检查url、nonceStr、timestamp、ticket等参数是否正确。 |  |
| 52013 | 签名校验失败 | 签名校验失败。请检查url、nonceStr、timestamp、ticket等参数是否正确。 |  |
| 52014 | 无效的url参数 | 无效的url参数。请检查url参数是否正确。 |  |
| 52015 | 无效的随机字符串参数 | 无效的随机字符串参数。请检查nonceStr参数是否正确。 |  |
| 52016 | 请检查 | 无效的签名参数。请检查url、nonceStr、timestamp、ticket等参数是否正确。 |  |
| 52017 | 无效的jsapi列表参数 | 无效的jsapi列表参数。请检查dd.config中的jsApiList参数是否正确。 |  |
| 52018 | 无效的时间戳 | 无效的时间戳。请检查timestamp参数是否正确。 |  |
| 52019 | 无效的agentid | 无效的agentid。请检查agentid参数是否正确。 |  |
| 52020 | 未找到服务窗授权 | 未找到服务窗授权。无。 |  |
| 52021 | 未找到微应用授权 | 未找到微应用授权。无。 |  |
| 52022 | 无效的jsapi类型 | 无效的jsapi类型。无。 |  |
| 52023 | 无效的服务窗agentid | 无效的服务窗agentid。检查服务窗微应用是否停用或者删除，可通过 [查询服务号列表](0812-query-service-number-list.md)接口查询。 |  |
| 52024 | 无效的jsapi tag | 无效的jsapi tag。无。 |  |
| 52025 | 无效的安全微应用 | 无效的安全微应用。无。 |  |
| 52026 | 无效的安全微应用URL | 无效的安全微应用URL。无。 |  |
| 60001 | 不合法的部门名称 | 不合法的部门名称。请检查部门名称是否正确，长度不能超过64个字符。 |  |
| 60002 | 部门层级深度超过限制 | 部门层级深度超过限制。无。 |  |
| 60003 | 部门不存在 | 部门不存在。可通过[获取部门列表](0082-user-management-acquires-the-list-departments.md)接口获取。 |  |
| 60004 | 父亲部门不存在 | 父亲部门不存在。可通过[获取指定用户的所有父部门列表](0085-queries-the-list-of-all-parent-departments-of-a-user.md)接口获取。 |  |
| 60005 | 不允许删除有成员的部门 | 不允许删除有成员的部门。可通过[获取部门用户userid列表](0065-query-the-list-of-department-userids.md)接口查看。 |  |
| 60006 | 不允许删除有子部门的部门 | 不允许删除有子部门的部门。可通过[获取子部门ID列表](0083-obtain-the-list-of-sub-department-ids.md)接口查看。 |  |
| 60007 | 不允许删除根部门 | 不允许删除根部门。无。 |  |
| 60009 | 部门名称含有非法字符 | 部门名称含有非法字符。无。 |  |
| 60010 | 部门存在循环关系 | 部门存在循环关系。无。 |  |
| 60011 | 没有调用该接口的权限 | 没有调用该接口的权限。需要修改appkey对应的权限点。请在[钉钉开放平台](https://open-dev.dingtalk.com/#/index)**> 应用详情页 > 权限管理 > 添加接口权限 > 接口权限**勾选对应的权限点。 |  |
| 60012 | 不允许删除默认应用 | 不允许删除默认应用。无。 |  |
| 60013 | 不允许关闭应用 | 不允许关闭应用。无。 |  |
| 60014 | 不允许开启应用 | 不允许开启应用。无。 |  |
| 60015 | 不允许修改默认应用可见范围 | 不允许修改默认应用可见范围。无。 |  |
| 60016 | 部门id已经存在 | 部门id已经存在。可通过[获取部门详情](0081-query-department-details0-v2.md)接口查看详情。 |  |
| 60017 | 不允许设置企业 | 不允许设置企业。无。 |  |
| 60018 | 不允许更新根部门 | 不允许更新根部门。无。 |  |
| 60019 | 从部门查询人员失败 | 从部门查询人员失败。请检查该成员是否在该部门中。可通过[获取部门用户userid列表](0065-query-the-list-of-department-userids.md)接口获取。 |  |
| 60020 | 访问ip不在白名单之中 | 访问ip不在白名单之中。企业应用：检查配置的服务器出口ip地址是否和请求ip地址一致。 isv应用：检查套件ip白名单和请求ip是否一致。 |  |
| 60021 | 父部门下该部门名称已存在 | 父部门下该部门名称已存在。可通过[获取部门列表](0082-user-management-acquires-the-list-departments.md)接口查看。 |  |
| 60022 | 包含敏感内容，请检查修改后重试！ | 包含敏感内容，请检查修改后重试！。无。 |  |
| 60067 | 部门的企业群群主不存在 | 部门的企业群群主不存在。无。 |  |
| 60068 | 部门的管理员不存在 | 部门的管理员不存在。无。 |  |
| 60102 | UserID在公司中已存在 | UserID在公司中已存在。无。 |  |
| 60103 | 手机号码不合法 | 手机号码不合法。无。 |  |
| 60104 | 手机号码在公司中已存在 | 手机号码在公司中已存在。删除手机号重新添加或更换未添加过的手机号。 |  |
| 60105 | 邮箱不合法 | 邮箱不合法。无。 |  |
| 60106 | 邮箱已存在 | 邮箱已存在。无。 |  |
| 60107 | 使用该手机登录钉钉的用户已经在企业中 | 使用该手机登录钉钉的用户已经在企业中。无。 |  |
| 60110 | 部门个数超出限制 | 部门个数超出限制。无。 |  |
| 60111 | UserID不存在 | UserID不存在。无。 |  |
| 60112 | 用户name不合法 | 用户name不合法。无。 |  |
| 60113 | 身份认证信息（手机/邮箱）不能同时为空 | 身份认证信息（手机/邮箱）不能同时为空。无。 |  |
| 60114 | 性别不合法 | 性别不合法。无。 |  |
| 60118 | 用户无有效邀请字段（邮箱，手机号） | 用户无有效邀请字段（邮箱，手机号）。无。 |  |
| 60119 | 不合法的position | 不合法的position。无。 |  |
| 60120 | 用户已禁用 | 用户已禁用。无。 |  |
| 60121 | 找不到该用户 | 找不到该用户。检查该企业下该员工是否存在。 |  |
| 60122 | 不合法的extattr | 不合法的extattr。无。 |  |
| 60123 | 不合法的jobnumber | 不合法的jobnumber。无。 |  |
| 60124 | 用户不在此群中 | 用户不在此群中。无。 |  |
| 60125 | CRM配置信息创建失败 | CRM配置信息创建失败。无。 |  |
| 60126 | CRM配置信息更新失败 | CRM配置信息更新失败。无。 |  |
| 60127 | CRM人员配置信息删除失败 | CRM人员配置信息删除失败。无。 |  |
| 60128 | 无效的主管id | 无效的主管id。无。 |  |
| 70001 | 企业不存在或者已经被解散 | 企业不存在或者已经被解散。无。 |  |
| 70002 | 获取套件下的微应用失败 | 获取套件下的微应用失败。无。 |  |
| 70003 | agentid对应微应用不存在 | agentid对应微应用不存在。无。 |  |
| 70004 | 企业下没有对应该agentid的微应用 | 企业下没有对应该agentid的微应用。代表应用和企业映射关系的ID (appId的实例化ID)，同一个ISV应用在不同企业的agentId不一致。 |  |
| 70005 | ISV激活套件失败 | ISV激活套件失败。请检查激活套件使用的参数是否正确。 |  |
| 71006 | 回调地址已经存在 | 回调地址已经存在。无。 |  |
| 71007 | 回调地址已不存在 | 回调地址已不存在。无。 |  |
| 71008 | 回调call\_back\_tag必须在指定的call\_back\_tag列表中 | 回调call\_back\_tag必须在指定的call\_back\_tag列表中。无。 |  |
| 71009 | 返回文本非success | 返回文本非success。回调地址返回的内容必须是**success**文本经过加密后的结果。 |  |
| 71010 | POST的JSON数据不包含所需要的参数字段或包含的参数格式非法 | POST的JSON数据不包含所需要的参数字段或包含的参数格式非法。无。 |  |
| 71011 | 传入的url参数不是合法的url格式 | 传入的url参数不是合法的url格式。合法的URL地址是**协议** +**域名** +**端口** +**路径path** +**参数**组成。 |  |
| 71012 | url地址访问异常 | url地址访问异常。无。 |  |
| 71013 | 此域名或IP不能注册或者接收回调事件 | 此域名或IP不能注册或者接收回调事件。回调地址的域名或者IP必须在套件的ip白名单中，并且该ip必须为外网ip。 |  |
| 71014 | 获取套件下的服务窗应用失败 | 获取套件下的服务窗应用失败。无。 |  |
| 72001 | 获取钉盘空间失败 | 获取钉盘空间失败。检查domain、agent\_id、access\_token参数是否正确有效。 |  |
| 72002 | 授权钉盘空间访问权限失败 | 授权钉盘空间访问权限失败。无。 |  |
| 72003 | 钉盘空间添加文件失败 | 钉盘空间添加文件失败。无。 |  |
| 800001 | 仅限ISV调用 | 仅限ISV调用。只有ISV微应用才能调用 |  |
| 80001 | 可信域名没有IPC备案，后续将不能在该域名下正常使用jssdk | 可信域名没有IPC备案，后续将不能在该域名下正常使用jssdk。无。 |  |
| 810002 | 复制的审批流已超过最大数量 | 复制的审批流已超过最大数量。一个企业最多可创建100个模板，超过最大数量后调用接口会报错。 |  |
| 810003 | 审批流表单格式错误 | 审批流表单格式错误。检查下审批表单，去除不支持的控件。 |  |
| 810008 | 获取审批流失败 | 获取审批流失败。检查审批模板是否被停用。 |  |
| 81001 | 两个用户没有任何关系，请先相互成为好友 | 两个用户没有任何关系，请先相互成为好友。无。 |  |
| 81002 | 用户拒收消息 | 用户拒收消息。无。 |  |
| 820001 | 发起审批实例失败，错误原因为【系统错误:Could not convert xml to bpmnModel.】 | 发起审批实例失败，错误原因为【系统错误:Could not convert xml to bpmnModel.】。processCode值不正确，请检查processCode。 |  |
| 820005 | 审批单状态异常 | 审批单状态异常。检查审批实例Id是否正确。 |  |
| 820006 | 审批状态异常，无法执行 | 审批状态异常，无法执行。检查审批节点是否异常。 |  |
| 830001 | 无错误信息 | 无错误信息。审批模板不存在，或者是processCode值不正确导致，请检查processCode。 |  |
| 850012 | 无错误信息 | 无错误信息。from\_time和to\_time时间差超过了31天，请检查参数。 |  |
| 853001 | timestamp参数格式不正确，必须是当前时间的毫秒数 | timestamp参数格式不正确，必须是当前时间的毫秒数。检查timestamp参数格式。 |  |
| 853002 | timestamp参数不合法，该参数值与钉钉服务器当前时间相差超过1分钟 | timestamp参数不合法，该参数值与钉钉服务器当前时间相差超过1分钟。检查服务器的时间。 |  |
| 853003 | accessKey参数不合法，必须是钉钉开放平台存在的appId | accessKey参数不合法，必须是钉钉开放平台存在的appId。检查accessKey参数。 |  |
| 853004 | signature参数不正确，与钉钉服务端计算出来的签名不一致，注意该参数传递时必须urlEncode | signature参数不正确，与钉钉服务端计算出来的签名不一致，注意该参数传递时必须urlEncode。检查signature参数 |  |
| 88 | 鉴权异常 | 鉴权异常。关注返回结果里的subCode和subMsg。 |  |
| 88005 | 管理日历个人日历操作失败 | 管理日历个人日历操作失败。无。 |  |
| 89001 | 管理日历启动导出任务失败 | 管理日历启动导出任务失败。无。 |  |
| 89011 | 管理日历写入数据失败 | 管理日历写入数据失败。无。 |  |
| 89012 | 管理日历更新数据失败 | 管理日历更新数据失败。无。 |  |
| 900001 | 加密明文文本非法 | 加密明文文本非法。加密明文不能为空。 |  |
| 900002 | 加密时间戳参数非法 | 加密时间戳参数非法。加密时间戳不能为空。 |  |
| 900003 | 加密随机字符串参数非法 | 加密随机字符串参数非法。加密随机字符串不能为空。 |  |
| 900004 | 不合法的aeskey | 不合法的aeskey。检查aeskey是否符合规格，长度固定为43个字符，从a-z, A-Z, 0-9共62个字符中选取，是AESKey的Base64编码。解码后即为32字节长的AESKey。 |  |
| 900005 | 签名不匹配 | 签名不匹配。检查签名计算的参数是否正确。 \* 个人免登：[个人免登场景的签名计算方法](1427-signature-personal-registration.md) \* 第三方企业：[第三方访问接口的签名计算方法](1428-the-signature-calculation-method-of-the-third-party-access-interface.md) |  |
| 900006 | 计算签名错误 | 计算签名错误。检查签名计算的参数是否正确。 \* 个人免登：[个人免登场景的签名计算方法](1427-signature-personal-registration.md) \* 第三方企业：[第三方访问接口的签名计算方法](1428-the-signature-calculation-method-of-the-third-party-access-interface.md) |  |
| 900007 | 计算加密文字错误 | 计算加密文字错误。检查是否安装JRE补丁或者对应的JRE版本是否正常。 |  |
| 900008 | 计算解密文字错误 | 计算解密文字错误。检查是否安装JRE补丁或者对应的JRE版本是否正常。 |  |
| 900009 | 计算解密文字长度不匹配 | 计算解密文字长度不匹配。检查aeskey是否符合规格。长度固定为43个字符，从a-z, A-Z, 0-9共62个字符中选取，是AESKey的Base64编码。 |  |
| 90001 | 您的服务器调用钉钉开放平台所有接口的请求都被暂时禁用了 | 您的服务器调用钉钉开放平台所有接口的请求都被暂时禁用了。无。 |  |
| 900010 | 计算解密文字corpid不匹配 | 计算解密文字corpid不匹配。检查corpid是否正确或者是否为当前企业的corpid。 **企业内部应用**：检查corpid是否正确或者是否为当前企业的corpid； **产品方案商开发应用**：检查customKey是否正确； **第三方企业应用**：检查suiteKey是否正确； |  |
| 90002 | 您的服务器调用钉钉开放平台当前接口的所有请求都被暂时禁用了 | 您的服务器调用钉钉开放平台当前接口的所有请求都被暂时禁用了。无。 |  |
| 90003 | 您的企业调用钉钉开放平台所有接口的请求都被暂时禁用了，仅对企业自己的Accesstoken有效 | 您的企业调用钉钉开放平台所有接口的请求都被暂时禁用了，仅对企业自己的Accesstoken有效。无。 |  |
| 90004 | 您当前使用的CorpId及CorpSecret被暂时禁用了，仅对企业自己的Accesstoken有效 | 您当前使用的CorpId及CorpSecret被暂时禁用了，仅对企业自己的Accesstoken有效。无。 |  |
| 90005 | 您的企业调用当前接口次数过多，请求被暂时禁用了，仅对企业自己的Accesstoken有效 | 您的企业调用当前接口次数过多，请求被暂时禁用了，仅对企业自己的Accesstoken有效。无。 |  |
| 90006 | 您当前使用的CorpId及CorpSecret调用当前接口次数过多，请求被暂时禁用了，仅对企业自己的Accesstoken有效 | 您当前使用的CorpId及CorpSecret调用当前接口次数过多，请求被暂时禁用了，仅对企业自己的Accesstoken有效。无。 |  |
| 90007 | 您当前要调用的企业的接口次数过多，对该企业的所有请求都被暂时禁用了，仅对企业授权给ISV的Accesstoken有效 | 您当前要调用的企业的接口次数过多，对该企业的所有请求都被暂时禁用了，仅对企业授权给ISV的Accesstoken有效。无。 |  |
| 90008 | 您当前要调用的企业的当前接口次数过多，对此企业下该接口的所有请求都被暂时禁用了，仅对企业授权给ISV的Accesstoken有效 | 您当前要调用的企业的当前接口次数过多，对此企业下该接口的所有请求都被暂时禁用了，仅对企业授权给ISV的Accesstoken有效。无。 |  |
| 90009 | 您调用企业接口超过了限制，对所有企业的所有接口的请求都被暂时禁用了，仅对企业授权给ISV的Accesstoken有效 | 您调用企业接口超过了限制，对所有企业的所有接口的请求都被暂时禁用了，仅对企业授权给ISV的Accesstoken有效。无。 |  |
| 90010 | 您调用企业当前接口超过了限制，对所有企业的该接口的请求都被暂时禁用了，仅对企业授权给ISV的Accesstoken有效 | 您调用企业当前接口超过了限制，对所有企业的该接口的请求都被暂时禁用了，仅对企业授权给ISV的Accesstoken有效。无。 |  |
| 90011 | 您的套件调用企业接口超过了限制，该套件的所有请求都被暂时禁用了，仅对企业授权给ISV的Accesstoken有效 | 您的套件调用企业接口超过了限制，该套件的所有请求都被暂时禁用了，仅对企业授权给ISV的Accesstoken有效。无。 |  |
| 90012 | 您的套件调用企业当前接口超过了限制，该套件对此接口的所有请求都被暂时禁用了，仅对企业授权给ISV的Accesstoken有效 | 您的套件调用企业当前接口超过了限制，该套件对此接口的所有请求都被暂时禁用了，仅对企业授权给ISV的Accesstoken有效。无。 |  |
| 90013 | 您的套件调用当前企业的接口超过了限制，该套件对此企业的所有请求都被暂时禁用了，仅对企业授权给ISV的Accesstoken有效 | 您的套件调用当前企业的接口超过了限制，该套件对此企业的所有请求都被暂时禁用了，仅对企业授权给ISV的Accesstoken有效。无。 |  |
| 90014 | 您的套件调用企业当前接口超过了限制，该套件对此企业该接口的所有请求都被暂时禁用了，仅对企业授权给ISV的Accesstoken有效 | 您的套件调用企业当前接口超过了限制，该套件对此企业该接口的所有请求都被暂时禁用了，仅对企业授权给ISV的Accesstoken有效。无。 |  |
| 90017 | 此IP使用CorpId及CorpSecret调用接口的CorpId个数超过限制 | 此IP使用CorpId及CorpSecret调用接口的CorpId个数超过限制。从该ip发起超过XX个corpid的请求被限制。 |  |
