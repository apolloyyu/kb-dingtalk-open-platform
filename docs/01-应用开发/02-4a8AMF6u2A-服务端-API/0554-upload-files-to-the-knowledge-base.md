---
title: "知识库上传文件"
source_url: "https://open.dingtalk.com/document/development/upload-files-to-the-knowledge-base"
namespace: "development"
slug: "upload-files-to-the-knowledge-base"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "文档/文件 > 知识库 > 使用教程 > 知识库上传文件"
doc_id: "QqxqIgFzw5"
updated_at: "2026-03-27 19:05:57"
---

> Source: https://open.dingtalk.com/document/development/upload-files-to-the-knowledge-base
> Path: 应用开发 / 服务端 API / 文档/文件 > 知识库 > 使用教程 > 知识库上传文件
> Updated: 2026-03-27 19:05:57

# 知识库上传文件

## 功能说明

在知识库（团队空间）目录下上传一个文件，需要按顺序完成以下 3 个步骤：

1. **获取文件上传信息**：向服务端申请上传凭证（OSS 地址 + 签名 Headers）。
2. **上传文件到 OSS**：使用第一步返回的地址和 Headers，将文件内容 PUT 到 OSS。
3. **提交文件**：通知服务端上传完成，完成文件的最终入库。

> **[!IMPORTANT]**
>
> 三个步骤必须按顺序执行，缺少任何一步都无法完成文件上传。

---

## 步骤一：获取文件上传信息

调用接口 `POST /v2.0/storage/spaces/files/{parentDentryUuid}/uploadInfos/query`，传入目标目录的`parentDentryUuid`（父目录唯一标识）和操作者`unionId`，获取本次上传所需的凭证信息。

> **[!NOTE]**
>
> 接口请参考[获取文件上传信息](0674-obtain-file-upload-informations.md)文档说明，如何调用请参考[如何调用服务端API](https://open.dingtalk.com/document/development/how-to-call-apis)文档介绍。

**关键入参：**

- `parentDentryUuid`（Path）：上传目标目录的 dentryUuid。若上传到知识库根目录，可通过以下两种方式获取根目录的dentryUuid：

  - 调用[获取我的文档知识库信息](0563-get-my-documents.md)接口，取返回结果`workspace`下的`rootNodeId`字段值；
  - 调用[获取知识库列表](0560-get-knowledge-base-list.md)接口，取返回结果`workspaces`下的`rootNodeId`字段值。
- `unionId`（Query）：操作者的 unionId，可调用[查询用户详情](0056-query-user-details.md)接口获取。
- `protocol`（Body）：固定填 `HEADER_SIGNATURE`。
- `option.preCheckParam.name`（Body）：文件名（含后缀），不能包含特殊字符（`*`、`"`、`<`、`>`、`|`），不能以`.` 结尾。

**返回参数：**

- `uploadKey`：本次上传的唯一标识，第三步使用**。**
- `headerSignatureInfo.resourceUrls`：OSS 上传地址，第二步使用。
- `headerSignatureInfo.headers`：OSS 请求头，第二步使用。
- `expirationSeconds`：凭证过期时间（秒），请在过期前完成后续步骤。

**HTTP示例**：

```
POST /v2.0/storage/spaces/files/{parentDentryUuid}/uploadInfos/query?unionId=union_id HTTP/1.1
Host: api.dingtalk.com
x-acs-dingtalk-access-token: access_token
Content-Type: application/json

{
  "protocol": "HEADER_SIGNATURE",
  "option": {
    "storageDriver": "DINGTALK",
    "preCheckParam": {
      "size": 512,
      "name": "测试文件.xlsx"
    }
  }
}
```

## 步骤二：上传文件到 OSS

使用第一步返回的 `resourceUrls[0]` 作为上传地址、`headers` 作为请求头，通过 HTTP `PUT` 方法将本地文件内容直接上传到 OSS。

> **[!NOTE]**
>
> `Content-Type` 必须主动设置为空字符串，否则会导致签名校验失败。

**示例代码**：

Java

```
import java.io.*;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.Map;

public void uploadToOss(String resourceUrl, Map<String, String> headers, String filePath) throws Exception {
  URL url = new URL(resourceUrl);
  HttpURLConnection connection = (HttpURLConnection) url.openConnection();

  // 设置第一步返回的 headers
  if (headers != null) {
    for (Map.Entry<String, String> entry : headers.entrySet()) {
      connection.setRequestProperty(entry.getKey(), entry.getValue());
    }
  }

  connection.setDoOutput(true);
  connection.setRequestMethod("PUT");
  connection.setUseCaches(false);
  connection.setReadTimeout(10000);
  connection.setConnectTimeout(10000);
  connection.connect();

  // 写入文件内容
  OutputStream out = connection.getOutputStream();
  InputStream is = new FileInputStream(new File(filePath));

  byte[ ] buffer = new byte[1024];

  int bytesRead;
  while ((bytesRead = is.read(buffer)) != -1) {
    out.write(buffer, 0, bytesRead);
  }
  out.flush();
  out.close();
  is.close();

  int responseCode = connection.getResponseCode();
  connection.disconnect();

  if (responseCode == 200) {
    System.out.println("OSS 上传成功");
  } else {
    System.out.println("OSS 上传失败，状态码：" + responseCode);
  }
}
```

Python

```
import requests

resource_url = '<第一步返回的 resourceUrls[0]>'
headers = <第一步返回的 headers>

  # 注意：content-type 必须设置为空
  headers['content-type'] = ''

result = requests.put(resource_url, data=open('<本地文件路径>', 'rb'), headers=headers)
print(result.status_code)  # 200 表示上传成功
```

Node.js

```
const fs = require('fs');
const request = require('request-promise');

const url = '<第一步返回的 resourceUrls[0]>';
const headers = <第一步返回的 headers>;

// 注意：content-type 必须主动设置为空
headers['content-type'] = '';

fs.createReadStream('/path/to/local/file.txt')
  .pipe(request({ method: 'PUT', url, headers }))
  .then(() => console.log('OSS 上传成功'))
  .catch(err => console.log('OSS 上传失败', err));
```

## 步骤三：提交文件

OSS 上传完成后，调用接口 `POST /v2.0/storage/spaces/files/{parentDentryUuid}/commit`，将文件正式写入知识库目录，完成整个上传流程。

> **[!NOTE]**
>
> - 接口成功后会返回文件信息（`dentry`），包含文件 ID、uuid、所在空间等，上传完成。
> - 接口请参考[提交文件](0675-submittal-file.md)文档说明，如何调用请参考[如何调用服务端API](https://open.dingtalk.com/document/development/how-to-call-apis)文档介绍。

**关键入参：**

- `parentDentryUuid`（Path）：与第一步保持一致。
- `unionId`（Query）：操作者的 unionId，可调用[查询用户详情](0056-query-user-details.md)接口获取。
- `uploadKey`（Body）：第一步返回的 uploadKey，用于关联本次上传。
- `name`（Body）：文件名称（含后缀）。
- `option.conflictStrategy`（Body）：文件名冲突策略，可选`AUTO_RENAME`（默认，自动重命名）/`OVERWRITE`（覆盖）

**HTTP示例：**

```
POST /v2.0/storage/spaces/files/{parentDentryUuid}/commit?unionId=union_id HTTP/1.1
Host: api.dingtalk.com
x-acs-dingtalk-access-token: access_token
Content-Type: application/json

{
  "uploadKey": "第一步返回的 uploadKey",
  "name": "测试文件.xlsx",
  "option": {
    "conflictStrategy": "AUTO_RENAME"
  }
}
```

## 完整流程总结

```
[步骤一] 调用「获取文件上传信息」接口
         → 返回 uploadKey + resourceUrls + headers（有过期时间，请尽快完成后续步骤）

[步骤二] 使用 resourceUrls[0] + headers，HTTP PUT 上传文件内容到 OSS
         → OSS 返回 200 表示上传成功

[步骤三] 调用「提交文件」接口，传入 uploadKey + 文件名
         → 返回文件信息（dentry），文件正式入库，上传完成
```

## 注意事项

- 步骤二上传时，`Content-Type`必须设置为空字符串，否则会导致 OSS 签名校验失败。
- 步骤一返回的上传凭证有过期时间（`expirationSeconds`），请在过期前完成步骤二和步骤三，否则需要重新调用步骤一。
- 存储空间类型为`USER`时，只有空间拥有者和管理者有操作权限，其他员工需要先通过「添加权限」接口授权。
- 存储空间类型为`APP`时，任何人操作都需要先通过「添加权限」接口授权。
