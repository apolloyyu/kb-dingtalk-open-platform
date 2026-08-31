---
title: "常见问题"
source_url: "https://open.dingtalk.com/document/development/common-problems-with-tables"
namespace: "development"
slug: "common-problems-with-tables"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "文档/文件 > 表格 > 常见问题"
doc_id: "O01QaatZ3U"
updated_at: "2026-07-14 09:21:51"
---

> Source: https://open.dingtalk.com/document/development/common-problems-with-tables
> Path: 应用开发 / 服务端 API / 文档/文件 > 表格 > 常见问题
> Updated: 2026-07-14 09:21:51

# 常见问题

## 接入相关

- **如何获取表格的 workbookId**

  每个钉钉表格都有一个 `workbookId` 作为唯一标识，有以下几种获取方式：

  - **从表格 URL 中获取**：打开钉钉表格，URL 中包含的文档 ID 即为 `workbookId`。

    ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7254684771/p1063528.png)
  - **从文档信息中获取**：点击表格左上角「菜单」→「表格」→「文档信息」，其中的文档 ID 即为 `workbookId`。

    ![从文档信息获取workbookId](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7254684771/p1063526.png)
  - **通过知识库 API 获取**：调用[获取节点](0570-get-knowledge-base-acquisition-node.md)接口，返回的`nodeId`（`dentryUuid`）即为`workbookId`。
- **如何获取 operatorId**

  `operatorId`是操作人的`unionId`，获取步骤如下：

  1. **通过手机号获取 userId**：调用[根据手机号查询用户](0063-query-users-by-phone-number.md)接口。
  2. **通过 userId 获取 unionId**：调用[查询用户详情](0056-query-user-details.md)接口，返回的`unionId`即为`operatorId`。

     > **[!IMPORTANT]**
     >
     > 首次调用可能需要在应用中申请「通讯录」相关权限。获取到 `operatorId` 后建议将其保存下来（如配置为环境变量），避免每次都通过接口获取。
- **AccessToken 过期了怎么办**

  AccessToken 的有效期为 **7200 秒（2 小时）**。过期后需要重新调用 [获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取新的 Token。

  建议在应用中实现 Token 缓存和自动刷新机制：

  - 缓存 Token 及其过期时间；
  - 在 Token 过期前 5 分钟主动刷新；
  - 当接口返回 Token 无效错误时，立即刷新并重试。
- **调用接口报错 The operator has no permission，如何解决**

  该错误表示`operatorId`对应的用户没有目标表格的操作权限。请检查：

  - **用户是否有表格的访问权限**：确保该用户已被添加为表格的协作者，或表格所在的知识库对该用户开放了权限。
  - **权限类型是否匹配**：

    - 读操作：如`GetAllSheets`、`GetSheet`、`GetRange`需要`Document.Workbook.Read` 权限。
    - 写操作：如`AppendRows`、`UpdateRange`、`CreateSheet`）需要 `Document.Workbook.Write`权限。
  - **应用是否申请了对应权限**：在[钉钉开放平台](https://open-dev.dingtalk.com/)的应用管理中，检查是否已申请并获批了相应的权限点。

## API 使用相关

- **sheetId 参数可以传工作表名称吗？**

  可以，`sheetId`参数支持传入工作表的 **ID** 或 **名称（标题）**。例如：

  - 传 ID：`Sheet1`，系统生成的 ID；
  - 传名称：`销售数据`，用户自定义的工作表标题。
  > **建议**：优先使用工作表 ID，因为名称可能被用户修改。可通过`GetAllSheets`接口获取所有工作表的 ID 和名称。
- **AppendRows 追加数据时，数据会写到哪里？**

  `AppendRows`会自动定位工作表中**最后一行有数据的位置**，在其下方追加新行。

  - 如果工作表为空，数据从第一行开始写入。
  - 追加的列数应与已有数据的列数保持一致，以确保数据对齐。
- **UpdateRange 更新单元格时，rangeAddress 的格式是什么？**

  `rangeAddress`使用 **A1 表示法**，常见格式如下：

  | **格式** | **含义** | **示例** |
  | --- | --- | --- |
  | A1 | 单个单元格 | 第 1 行第 1 列。 |
  | A1:C3 | 矩形区域 | 从 A1 到 C3 的 9 个单元格。 |
  | A:A | 整列 | A 列所有单元格。 |
  | 1:1 | 整行 | 第 1 行所有单元格。 |
  | A1:ZZ99999 | 大范围区域 | 用于全表操作。 |
- `GetRange` **和** `UpdateRange` **有什么区别？**

  | **对比项** | **GetRange** | **UpdateRange** |
  | --- | --- | --- |
  | HTTP 方法 | GET | PUT |
  | 功能 | 读取单元格区域的值、样式等属性 | 更新单元格区域的值、样式等属性 |
  | 权限要求 | `Document.Workbook.Read` | `Document.Workbook.Write` |
  | 说明文档 | [获取单元格区域](0609-get-cell-properties.md) | [更新单元格区域](0610-update-cell-properties.md) |

  `GetRange`适合在写入数据后验证结果，或在自动化流程中读取表格数据进行后续处理。两者使用相同的`rangeAddress`参数（A1 表示法）来指定操作的单元格范围。
- **调用接口返回 invalidRequest.resource.notFound，如何排查**

  该错误表示请求的资源不存在，常见原因：

  | **场景** | **可能原因** | **解决方案** |
  | --- | --- | --- |
  | workbookId 无效 | 表格已被删除或 ID 拼写错误 | 重新获取 workbookId。 |
  | sheetId 无效 | 工作表已被删除或名称已修改 | 调用 `GetAllSheets` 获取最新的工作表列表。 |
  | rangeAddress 无效 | 单元格地址格式错误或超出范围 | 检查 A1 表示法格式，确保在表格范围内。 |
- **钉钉表格 API 有哪些使用限制**

  | **限制项** | **限制值** | **说明** |
  | --- | --- | --- |
  | 调用频率 | 建议 ≤ 100 次/分钟 | 单个应用对同一表格的调用频率。 |
  | AppendRows 单次追加 | 建议 ≤ 5000 行 | 超过可能导致超时。 |
  | 单元格内容长度 | 取决于表格限制 | 过长的文本可能被截断。 |
  | AccessToken 有效期 | 7200 秒（2 小时） | 过期需重新获取。 |
- 如何在代码中处理 API 调用失败的情况

  建议实现以下错误处理策略：

  - **Token 过期自动刷新**：捕获 Token 无效错误，自动刷新后重试。
  - **频率限制重试**：收到 429 错误时，等待一段时间后重试（建议使用指数退避策略）。
  - **幂等性处理**：对于写操作（如 `AppendRows`），需注意重试可能导致数据重复写入。建议在数据中加入唯一标识，写入后通过 `GetRange` 验证。
  - **超时处理**：网络请求设置合理的超时时间（建议 30 秒），超时后进行重试。

    ```
    import time

    def call_api_with_retry(func, max_retries=3):
      for attempt in range(max_retries):
        try:
          return func()
        except TokenExpiredError:
          refresh_token()
        except RateLimitError:
          time.sleep(2 ** attempt)
        except TimeoutError:
          time.sleep(1)
      raise Exception("API 调用失败，已达最大重试次数")
    ```
