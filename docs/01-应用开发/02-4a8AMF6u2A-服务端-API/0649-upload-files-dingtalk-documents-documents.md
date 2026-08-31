---
title: "上传本地文件到钉钉文档（我的文档）"
source_url: "https://open.dingtalk.com/document/development/upload-files-dingtalk-documents-documents"
namespace: "development"
slug: "upload-files-dingtalk-documents-documents"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "文档/文件 > 存储管理 > 使用教程 > 上传本地文件到钉钉文档（我的文档）"
doc_id: "Ms4Fj0JynI"
updated_at: "2026-05-15 12:27:36"
---

> Source: https://open.dingtalk.com/document/development/upload-files-dingtalk-documents-documents
> Path: 应用开发 / 服务端 API / 文档/文件 > 存储管理 > 使用教程 > 上传本地文件到钉钉文档（我的文档）
> Updated: 2026-05-15 12:27:36

# 上传本地文件到钉钉文档（我的文档）

本文档将指引你如何将本地文件上传到钉钉文档（我的文档）目录下。

## **简介**

### **教学内容**

本教程介绍开发者如何将本地文件上传到钉钉文档（我的文档）目录中。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1287161571/p981575.png)

### **教学目标**

帮助开发者快速掌握本地文件上传至钉钉文档（我的文档）目录中的能力。

### **教学范围**

面向钉钉所有开发者

## **前提条件**

- 已经获取开发者权限。
- 已经安装了 IDE 或其他开发工具。
- 已经安装了 [node.js](https://nodejs.org/en/download)，并完成了相关[环境的配置](https://m.runoob.com/nodejs/nodejs-install-setup.html)。
- 已经安装了 [maven](https://maven.apache.org/)，并完成了相关[环境的配置](https://maven.apache.org/install.html)。
- 已经安装了 [JDK](https://www.oracle.com/java/technologies/downloads/?er=221886)，并完成了相关[环境的配置](https://docs.oracle.com/en/java/javase/24/install/overview-jdk-installation.html)。

## **开发流程**

1. 调用[获取我的文档知识库信息](0563-get-my-documents.md)接口，获取“我的文档”根节点 ID，即返回参数`rootNodeId`（parentDentryUuid）。
2. 调用[获取文件上传信息](0674-obtain-file-upload-informations.md)接口，获取上传文件所需的`resourceUrls`和`headers`参数值。
3. 使用 OSS 的 header 加签方式上传文件：

   Java

   ```
   import java.io.*;
   import java.net.HttpURLConnection;
   import java.net.URL;
   public void test(){
                  // 从接口返回信息中拿到resourceUrls
                   String resourceUrl = "上述接口返回的resourceUrls";
                 // 从接口返回信息中拿到headers
                   Map<String, String> headers = "上述接口返回的headers";
                   URL url = new URL(resourceUrl);
                   HttpURLConnection connection = (HttpURLConnection)url.openConnection();
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
                   OutputStream out = connection.getOutputStream();
                   InputStream is = new FileInputStream(new File("/Users/xxxxx/Desktop/测试文件.xls"));
                   byte[] b =new byte[1024];
                   int temp;
                   while ((temp=is.read(b))!=-1){
                          out.write(b,0,temp);
                   }
                   out.flush();
                   out.close();
                   int responseCode = connection.getResponseCode();
                   connection.disconnect();
                   if (responseCode == 200) {
                       System.out.println("上传成功");
                    } else {
                       System.out.println("上传失败");
                    }
   }
   ```

   Python

   ```
   #!/usr/bin/env python

   import requests

   url = '<第一步接口获取的resourceUrl>'
   headers = <第一步接口返回的headers>
   result = requests.put(url, data=open('<path_to_file>', 'rb'), headers=headers)
   print(result)
   ```

   C#

   ```
   public static string HttpRequest(string url, string filePath, Dictionary<string, string> headers) {

       FileStream fileStream = new FileStream(filePath, FileMode.Open, FileAccess.Read, FileShare.Read);
       BinaryReader reader = new BinaryReader(fileStream);
       reader.BaseStream.Seek(0, SeekOrigin.Begin);
       byte[] datas = reader.ReadBytes((int)reader.BaseStream.Length);
       HttpWebRequest request = (HttpWebRequest)WebRequest.Create(url);
       request.Method = "PUT";
       request.Timeout = 150000;
       foreach (var header in headers) {
           request.Headers.Add($"{header.Key}", $"{header.Value}");
       }
       Stream requestStream = null;
       string responseStr = null;
       try {
           if (datas != null) {
               request.ContentLength = datas.Length;
               requestStream = request.GetRequestStream();
               requestStream.Write(datas, 0, datas.Length);
               requestStream.Close();
           } else {
               request.ContentLength = 0;
           }
           HttpWebResponse response = request.GetResponse() as HttpWebResponse;
           responseStr = response.Headers.GetValues("x-oss-request-id")[0];
       } catch (Exception ex) {
           Console.WriteLine("error");
       } finally {
           request = null;
           requestStream = null;
       }
       return responseStr;
   }
   ```

   PHP

   ```
   $url = $result->body->headerSignatureInfo->resourceUrls[0];
   $headersSource = $result->body->headerSignatureInfo->headers;
   foreach ($headersSource as $key => $value) {
   $headers[] = $key . ': ' . $value;
   }
   // 需要主动指定content-type为空
   $headers['Content-Type'] = '';

   $file = '/Users/dengxian.ldx/Desktop/test.txt';

   $ch = curl_init();
   curl_setopt_array($ch, array(
   CURLOPT_URL => $url,
   CURLOPT_RETURNTRANSFER => true,
   CURLOPT_HEADER => true,
   CURLOPT_TIMEOUT => 100,
   CURLOPT_CONNECTTIMEOUT => 100,
   CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
   CURLOPT_PUT => true,
   CURLOPT_HTTPHEADER => $headers,
   CURLOPT_SSL_VERIFYPEER => false,
   CURLOPT_SSL_VERIFYHOST => false,
   ));
   curl_setopt($ch, CURLOPT_INFILE, fopen($file , 'rb'));
   curl_setopt($ch, CURLOPT_INFILESIZE, filesize($file) );
   curl_setopt($ch, CURLOPT_UPLOAD, true);

   $response = curl_exec($ch);
   curl_close($ch);

   echo $response .PHP_EOL;
   ```

   Node.js

   ```
   const fs = require('fs');
   const request = require('request-promise');

   url = <url>;
   header = <headers>;

   // 注意: 需要主动指定content-type为空
   headers['content-type']='';

   var options = {
     method: 'PUT',
     url: url,
     headers: headers
   };

   fs.createReadStream('/Users/dengxian.ldx/temp/test/a.txt').pipe(request(options)).then(body =>{
     console.log(body);
   }).catch(err => {
     console.log(err);
   });
   ```
4. 调用[提交文件](0675-submittal-file.md)接口，上传文件到钉钉文档（我的文档）目录中。

## **步骤一：创建应用**

1. 登录[开发者后台](https://open-dev.dingtalk.com/#/)。
2. 单击**应用开发** > **企业内部应用** > **钉钉应用** > **创建应用**。
3. 填写应用信息。

   | **配置项** | **是否必选** | **配置说明** |
   | --- | --- | --- |
   | **应用名称** | 是 | 输入应用名称，应用名称最小长度为 2 个字符。 |
   | **应用描述** | 是 | 简要描述应用提供的产品或服务，应用描述最小长度为 4 个字符。 |
   | **应用图标** | 否 | 上传应用图标，图标要求 JPG/PNG 格式、240 px \* 240 px 以上、1:1 、2 MB 以内的无圆角图标。 |
4. 单击**保存**，进入应用详情页。

创建完成后，即可单击**基础信息** > **凭证与基础信息**，查看应用 Client ID 和 Client Secret。

> *注意：保存 Client ID 和 Client Secret，后续需要使用。*

## **步骤二：配置网页应用**

1. 在应用详情页，单击**应用能力** > **添加应用能力**。
2. 选择添加网页应用。
3. 配置网页应用（H5）信息：

   | **配置项** | **说明** |
   | --- | --- |
   | 应用首页地址 | 填写首页地址，本示例使用：`http://localhost:5173?corpid=$CORPID$`用于后续测试。  本示例仅用于本地测试。  image |
   | PC端首页地址 |

   配置完成后，单击保存。

## **步骤三：申请接口权限**

1. 在应用详情页，单击**开发配置** > **权限管理**，进入权限申请页面。
2. 在权限搜索框中分别输入`Wiki.Workspace.Read`、`Storage.UploadInfo.Read`和`Storage.File.Write`，并申请接口权限。

   > 如果你不是企业管理员/没有应用开发权限，申请权限时需要企业管理员审批。

## **步骤四：发布应用**

1. 应用配置完成后，你需要发布应用，在应用详情页，单击**应用发布** > **版本管理与发布**。
2. 单击**创建新版本**，进入版本详情页面。
3. 配置版本信息：

   | **配置项** | **说明** |
   | --- | --- |
   | 应用版本号 | 填写应用版本号，使用默认版本即可。 |
   | 版本描述 | 填写版本描述信息，自定义即可。 |
   | 待发布内容 | 工作台显示的应用能力：  - 选择网页应用 |

   配置完成后，单击下方保存。
4. 在保存成功的弹框页面，单击直接发布。

   > *如果你不是企业管理员，发布应用时需要企业管理员审批，发布仅我可见则无需管理员审批。*

## **步骤五：构建服务**

1. 确保已经完成上述步骤，获取下方 Demo 运行的参数信息。
2. 你可以下载 [doc-demo.zip](https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20250704/bpihcw/doc-demo.zip) Demo。
3. 打开 IDE，并导入已下载的 Demo。

   > 示例代码分为 backend（后端代码目录）和frontend（前端代码目录）。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6369733671/p1026995.png)
4. 打开后端代码目录，在 resources 目录中修改`application.properties`文件，填写`clientId（应用Client ID）`、`clientSecret（应用Client Secret）`。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6369733671/p1026996.png)
5. 点击启动后端服务。

   > **[!NOTE]**
   >
   > - 在启动后端服务前，请确保已经正确安装Maven 和 JDK，并配置了相关环境；如果是初次安装 IDE，需要在 IDE 中修改相关配置文件。
   > - 确保 5173 和 8080 端口没有被占用。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6369733671/p1026998.png)
6. 打开前端代码目录，修改 `vite.config.ts`,并填写正确的`clientId（应用Client ID）`。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6369733671/p1026997.png)
7. 点击前端项目文件，鼠标右键并选择**终端**打开。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6369733671/p1026999.png)
8. 在终端窗口中，输出以下命令：

   1. `npm install`
   2. `npm run dev`

      > 注意：windows 在启动时候，请使用`npm run dev:raw`。
9. 至此，前端和后端服务已经启动成功。

## **步骤六：测试应用**

1. 登录钉钉客户端，选择应用所在的组织。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1287161571/p981635.png)
2. 单击**工作台** > **添加**，搜索上方你创建的企业应用并完成添加操作。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1287161571/p981637.png)
3. 在工作台访问应用，并单击**选择本地文件**上传。

   > 要求上传文件小于 50M。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1287161571/p981647.png)
4. 选择文件后，单击**提交**，完成上传操作。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1287161571/p981651.png)
5. 上传完成后，即可打开文件查看上传内容。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1287161571/p981786.png)
