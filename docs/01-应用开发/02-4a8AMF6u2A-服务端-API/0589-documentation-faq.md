---
title: "常见问题"
source_url: "https://open.dingtalk.com/document/development/documentation-faq"
namespace: "development"
slug: "documentation-faq"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "文档/文件 > 文档 > 常见问题"
doc_id: "XqDrSNSLeu"
updated_at: "2026-11-11 17:26:43"
---

> Source: https://open.dingtalk.com/document/development/documentation-faq
> Path: 应用开发 / 服务端 API / 文档/文件 > 文档 > 常见问题
> Updated: 2026-11-11 17:26:43

# 常见问题

## **文档**相关

### **内容写入**

- **如何将 Markdown 格式的内容写入钉钉文档？**

  有两种方式可以将 Markdown 内容写入文档：

  - **方式一：插入内容（追加，不影响已有内容）**

    调用[插入内容](0582-api-insertcontent.md)接口，将 Markdown 内容插入到文档指定位置：

    ```
    curl --location --request POST 'https://api.dingtalk.com/v1.0/doc/suites/documents/{documentId}/content?operatorId={operatorId}' \
    --header 'x-acs-dingtalk-access-token: {ACCESS_TOKEN}' \
    --header 'Content-Type: application/json' \
    --data '{
      "content": {
        "type": "markdown",
        "content": "# 一级标题\n\n这是一段正文内容。"
      }
    }'
    ```
  - **方式二：覆写文档（清空后重写）**

    调用[覆写文档（应用授权）](0580-api-doc-updatecontent.md)接口，以 Markdown 格式覆写文档全部内容：

    ```
    curl --location --request POST 'https://api.dingtalk.com/v1.0/doc/suites/documents/{docKey}/overwriteContent?operatorId={operatorId}' \
    --header 'x-acs-dingtalk-access-token: {ACCESS_TOKEN}' \
    --header 'Content-Type: application/json' \
    --data '{
      "content": "# 文档标题\n\n正文内容。",
      "dataType": "markdown"
    }'
    ```

    覆写文档会**清空**文档现有全部内容，属于破坏性操作，请谨慎使用。如果只需追加内容，请使用插入内容接口。

### **块元素操作**

- **如何插入带内容的段落**

  调用[插入块元素](0584-api-docinsertblocks.md)接口，在文档中插入一个段落块，并通过`children`字段指定段落内的行内元素：

  ```
  curl --location --request POST 'https://api.dingtalk.com/v1.0/doc/suites/documents/{dentryUuid}/blocks?operatorId={operatorId}' \
  --header 'x-acs-dingtalk-access-token: {ACCESS_TOKEN}' \
  --header 'Content-Type: application/json' \
  --data '{
    "element": {
      "blockType": "paragraph",
      "paragraph": {},
      "children": [
        {
          "text": "这是一段加粗的红色文字",
          "bold": true,
          "color": "#FF5733"
        },
        {
          "elementType": "sticker",
          "properties": { "code": "大笑" }
        }
      ]
    }
  }'
  ```

  如果调用成功，预计将返回以下格式数据：

  ```
  {
    "result": {
      "data": {
        "paragraph": { "text": "这是一段加粗的红色文字" },
        "blockType": "paragraph",
        "index": 0,
        "id": "......"
      }
    },
    "success": true
  }
  ```

  `paragraph`对象不能被省略，即使段落无特殊属性，也需要传入空对象`{}`。
- **如何在文档指定位置（而非末尾）插入块元素**

  调用[插入块元素](0584-api-docinsertblocks.md)接口时，通过`blockId`或`index`指定目标位置，并通过`where`参数控制插入到目标位置之前还是之后：

  ```
  curl --location --request POST 'https://api.dingtalk.com/v1.0/doc/suites/documents/{docKey}/blocks?operatorId={operatorId}' \
  --header 'x-acs-dingtalk-access-token: {ACCESS_TOKEN}' \
  --header 'Content-Type: application/json' \
  --data '{
    "element": {
      "blockType": "paragraph",
      "paragraph": {}
    },
    "blockId": "lc4si5p3n84zwqxxx",
    "where": "before"
  }'
  ```

  | 参数 | 说明 |
  | --- | --- |
  | `blockId` | 目标块的唯一标识，插入到该块之前或之后 |
  | `index` | 当`blockId`不存在时，使用文档第`index`个一级块作为目标位置（从 0 开始） |
  | `where` | `"before"`表示插入到目标位置之前，`"after"`表示之后（默认为`"after"`） |
- **如何插入标题**

  调用[插入块元素](0584-api-docinsertblocks.md)接口，将`blockType`设置为`heading`，并在`heading`对象中通过`level`指定标题级别（1~6）：

  ```
  curl --location --request POST 'https://api.dingtalk.com/v1.0/doc/suites/documents/{docKey}/blocks?operatorId={operatorId}' \
  --header 'x-acs-dingtalk-access-token: {ACCESS_TOKEN}' \
  --header 'Content-Type: application/json' \
  --data '{
    "element": {
      "blockType": "heading",
      "heading": {
        "level": 2,
        "text": "这是一个二级标题"
      }
    }
  }'
  ```

  如果调用成功，预计将返回以下格式数据：

  ```
  {
    "success": true
  }
  ```

  `heading.level` 与标题级别的对应关系：

  | level 值 | 对应标题 |
  | --- | --- |
  | `1` | 一级标题（H1） |
  | `2` | 二级标题（H2） |
  | `3` | 三级标题（H3） |
  | `4` | 四级标题（H4） |
  | `5` | 五级标题（H5） |
  | `6` | 六级标题（H6） |
- **如何插入引用块**

  调用[插入块元素](0584-api-docinsertblocks.md)接口，将`blockType`设置为`blockquote`，并在`blockquote`对象中传入引用内容：

  ```
  curl --location --request POST 'https://api.dingtalk.com/v1.0/doc/suites/documents/{docKey}/blocks?operatorId={operatorId}' \
  --header 'x-acs-dingtalk-access-token: {ACCESS_TOKEN}' \
  --header 'Content-Type: application/json' \
  --data '{
    "element": {
      "blockType": "blockquote",
      "blockquote": {
        "text": "这是一段引用内容"
      }
    }
  }'
  ```

  如果调用成功，预计将返回以下格式数据：

  ```
  {
    "result": {
      "data": {
        "blockType": "blockquote",
        "index": 4,
        "id": "......"
      }
    },
    "success": true
  }
  ```
- **如何插入高亮块并在其中嵌套段落**

  高亮块的`children`只能是`BlockElement`数组。调用[插入块元素](0584-api-docinsertblocks.md)接口时，在`children`中传入子段落：

  ```
  curl --location --request POST 'https://api.dingtalk.com/v1.0/doc/suites/documents/{docKey}/blocks?operatorId={operatorId}' \
  --header 'x-acs-dingtalk-access-token: {ACCESS_TOKEN}' \
  --header 'Content-Type: application/json' \
  --data '{
    "element": {
      "blockType": "callout",
      "callout": {
        "sticker": "灯泡",
        "showstk": true,
        "bgcolor": "#FFF9C4",
        "border": "#FFD700"
      },
      "children": [
        {
          "blockType": "paragraph",
          "paragraph": { "text": "这是高亮块内的段落内容" }
        }
      ]
    }
  }'
  ```

  不同类型块元素的`children`类型不同：段落块的`children`只能是行内元素；高亮块的`children`只能是块元素。
- **如何插入分栏**

  调用[插入块元素](0584-api-docinsertblocks.md)接口，将`blockType`设置为`columns`，通过`columns.size`指定分栏数量，并在`children`中传入各栏的块元素内容：

  ```
  curl --location --request POST 'https://api.dingtalk.com/v1.0/doc/suites/documents/{docKey}/blocks?operatorId={operatorId}' \
  --header 'x-acs-dingtalk-access-token: {ACCESS_TOKEN}' \
  --header 'Content-Type: application/json' \
  --data '{
    "element": {
      "blockType": "columns",
      "columns": {
        "size": 2,
        "noFill": false
      },
      "children": [
        {
          "blockType": "paragraph",
          "paragraph": { "text": "左栏内容" }
        },
        {
          "blockType": "paragraph",
          "paragraph": { "text": "右栏内容" }
        }
      ]
    }
  }'
  ```

  如果调用成功，预计将返回以下格式数据：

  ```
  {
    "result": {
      "data": {
        "columns": { "size": 2 },
        "blockType": "columns",
        "index": 7,
        "id": "......"
      }
    },
    "success": true
  }
  ```

  `columns` 对象的字段说明：

  | 字段 | 类型 | 说明 |
  | --- | --- | --- |
  | `size` | Number | 分栏数量 |
  | `noFill` | Boolean | 是否自动填充背景色，默认`false` |

  `columns`的`children`只能是 **BlockElement 数组**，不能是行内元素。
- **如何插入有序列表**

  调用[插入块元素](0584-api-docinsertblocks.md)接口，将`blockType`设置为`orderedList`，并在`orderedList`对象中传入列表属性，在`children`中传入列表项文本：

  ```
  curl --location --request POST 'https://api.dingtalk.com/v1.0/doc/suites/documents/{docKey}/blocks?operatorId={operatorId}' \
  --header 'x-acs-dingtalk-access-token: {ACCESS_TOKEN}' \
  --header 'Content-Type: application/json' \
  --data '{
    "element": {
      "blockType": "orderedList",
      "orderedList": {
        "list": {
          "listId": "my-ordered-list-001",
          "level": 0,
          "listStyleType": "decimal",
          "listStyle": {
            "format": "decimal",
            "text": "%1.",
            "align": "left"
          }
        }
      },
      "children": [
        { "text": "有序列表第一项" }
      ]
    }
  }'
  ```

  如果调用成功，预计将返回以下格式数据：

  ```
  {
    "result": {
      "data": {
        "blockType": "orderedList",
        "index": 6,
        "id": "......"
      }
    },
    "success": true
  }
  ```

  `list` 对象的常用字段说明：

  | 字段 | 类型 | 说明 |
  | --- | --- | --- |
  | `listId` | String | 列表的唯一标识，同一列表的多个列表项应使用相同的`listId` |
  | `level` | Number | 列表缩进层级，从`0`开始 |
  | `listStyleType` | String | 列表样式类型，有序列表使用`"decimal"` |
- **如何插入无序列表**

  调用[插入块元素](0584-api-docinsertblocks.md)接口，将`blockType`设置为`unorderedList`，并在`unorderedList`对象中传入列表属性，在`children`中传入列表项文本：

  ```
  curl --location --request POST 'https://api.dingtalk.com/v1.0/doc/suites/documents/{docKey}/blocks?operatorId={operatorId}' \
  --header 'x-acs-dingtalk-access-token: {ACCESS_TOKEN}' \
  --header 'Content-Type: application/json' \
  --data '{
    "element": {
      "blockType": "unorderedList",
      "unorderedList": {
        "list": {
          "listId": "my-unordered-list-001",
          "level": 0,
          "listStyleType": "disc",
          "listStyle": {
            "format": "disc",
            "text": "%1",
            "align": "left"
          }
        }
      },
      "children": [
        { "text": "无序列表第一项" }
      ]
    }
  }'
  ```

  如果调用成功，预计将返回以下格式数据：

  ```
  {
    "result": {
      "data": {
        "blockType": "unorderedList",
        "index": 8,
        "id": "......"
      }
    },
    "success": true
  }
  ```

  有序列表和无序列表的`listId`用于将多个列表项关联为同一个列表。若要插入同一列表的多个列表项，每个列表项应使用相同的`listId`，可通过 BatchOperate 批量接口一次性插入。

### **查询操作**

- **如何获取文档中所有块元素的 blockId？**

  调用[查询块元素](0583-api-docblocksquery.md)接口，获取文档根节点下的一级块元素列表，每个元素包含其`id`（即`blockId`）：

  ```
  curl --location --request GET 'https://api.dingtalk.com/v1.0/doc/suites/documents/{docKey}/blocks?operatorId={operatorId}' \
  --header 'x-acs-dingtalk-access-token: {ACCESS_TOKEN}'
  ```

  如果调用成功，预计将返回以下格式数据：

  ```
  {
    "success": true,
    "result": {
      "data": [
        {
          "heading": { "level": "heading-1", "text": "文档标题" },
          "blockType": "heading",
          "index": 0,
          "id": "......"
        },
        {
          "paragraph": { "text": "正文内容。" },
          "blockType": "paragraph",
          "index": 1,
          "id": "......"
        }
      ]
    }
  }
  ```

  目前查询块元素接口**仅支持查询文档根节点下的一级块元素**，不支持递归查询嵌套在高亮块等容器内的子块元素。

## **表格**

### **接入相关**

- **如何获取表格的 workbookId**

  每个钉钉表格都有一个 `workbookId` 作为唯一标识，有以下几种获取方式：

  - **从表格 URL 中获取**：打开钉钉表格，URL 中包含的文档 ID 即为 `workbookId`。

    ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7254684771/p1063528.png)
  - **从文档信息中获取**：点击表格左上角「菜单」→「表格」→「文档信息」，其中的文档 ID 即为 `workbookId`。

    ![从文档信息获取workbookId](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7254684771/p1063526.png)
  - **通过知识库 API 获取**：调用[获取节点](0570-get-knowledge-base-acquisition-node.md)接口，返回的`nodeId`（`dentryUuid`）即为`workbookId`。
- **如何获取 operatorId**

  `operatorId`是操作人的`unionId`，获取步骤如下：

  1. **通过手机号获取 userId**：调用[根据手机号查询用户](0062-query-users-by-phone-number.md)接口。
  2. **通过 userId 获取 unionId**：调用[查询用户详情](0055-query-user-details.md)接口，返回的`unionId`即为`operatorId`。

     > **[!IMPORTANT]**
     >
     > 首次调用可能需要在应用中申请「通讯录」相关权限。获取到 `operatorId` 后建议将其保存下来（如配置为环境变量），避免每次都通过接口获取。
- **AccessToken 过期了怎么办**

  AccessToken 的有效期为 **7200 秒（2 小时）**。过期后需要重新调用 [获取企业内部应用的accessToken](0032-obtain-the-access-token-of-an-internal-app.md)接口获取新的 Token。

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

### **API 使用相关**

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
