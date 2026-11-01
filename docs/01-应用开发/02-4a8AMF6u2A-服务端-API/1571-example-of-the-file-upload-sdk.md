---
title: "文件上传流程"
source_url: "https://open.dingtalk.com/document/development/example-of-the-file-upload-sdk"
namespace: "development"
slug: "example-of-the-file-upload-sdk"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "历史文档（不推荐） > 文档/文件 > 钉盘 > 文件传输 > 文件上传流程"
doc_id: "VaJmPLGflq"
updated_at: "2026-08-25 09:38:28"
---

> Source: https://open.dingtalk.com/document/development/example-of-the-file-upload-sdk
> Path: 应用开发 / 服务端 API / 历史文档（不推荐） > 文档/文件 > 钉盘 > 文件传输 > 文件上传流程
> Updated: 2026-08-25 09:38:28

# 文件上传流程

你可以通过以下步骤，完成文件上传。

> **[!IMPORTANT]**
>
> - 本接口已完成升级，后续将维持现有功能且不再新增能力。
> - 未接入的开发者建议使用新版[获取文件下载信息](0678-obtains-the-download-information-about-a-file.md)接口，已接入用户不受影响。

## 操作步骤

1. 调用[获取文件上传信息](0674-obtain-file-upload-informations.md)接口，获取文件上传临时凭证。
2. 根据返回的文件上传凭证，上传文件到钉盘空间。

   Java

   ```
   public static void main(String[] args) {
       
       // 以下参数为步骤1返回的上传凭证
       // 阿里云账号的临时accessKeyId。
       String accessKeyId = "<accessKeyId>";
       // 阿里云账号的临时accessKeySecret。
       String accessKeySecret = "<accessKeySecret>";
       // 临时访问密钥。
       String securityToken = "<accessToken>";
       // OSS访问域名。
       String endpoint = "<endpoint>";
       // OSS存储空间。
       String bucket = "<bucket>";
       // 对应OSS Object Key，可用于刷新token以及调用添加文件（夹）接口添加文件记录。
       String ossKey = "<mediaId>";
       
       CredentialsProvider credentialsProvider = new DefaultCredentialProvider(accessKeyId, accessKeySecret, securityToken);
       ClientConfiguration clientConfiguration = new ClientConfiguration();
       clientConfiguration.setProtocol(Protocol.HTTPS); // 注意, 需要是HTTPS
       OSSClient ossClient = new OSSClient(endpoint, credentialsProvider, clientConfiguration);
       PutObjectRequest putObjectRequest = new PutObjectRequest(bucket, ossKey, new File("<path_to_file>"));
       
       ossClient.putObject(putObjectRequest);
       // 关闭OSSClient。
       ossClient.shutdown();
   }
   ```

   Python

   ```
   import oss2
   # 以下参数为步骤1返回的上传凭证
   # 阿里云账号的临时accessKeyId。
   accessKeyId = "<accessKeyId>"
   # 阿里云账号的临时accessKeySecret。
   accessKeySecret = "<accessKeySecret>"
   # 临时访问密钥。
   stsToken = "<accessToken>"
   # OSS访问域名。
   endpoint= "https://<endpoint>"
   # SS存储空间。
   bucket = "<bucket>"
   # 对应OSS Object Key，可用于刷新token以及调用添加文件（夹）接口添加文件记录。
   objectKey = "<mediaId>"

   auth = oss2.StsAuth(accessKeyId, accessKeySecret, stsToken)
   bucket = oss2.Bucket(auth, endpoint, bucket)

   try:
       bucket.put_object_from_file(objectKey, <path_to_file>)
   except oss2.exceptions.ServerError as e:
       print(e)
   ```

   Go

   ```
   package main

   import (
       "fmt"
       "os"
       "github.com/aliyun/aliyun-oss-go-sdk/oss"
   )

   // 以下参数为步骤1返回的上传凭证
   // 阿里云账号的临时accessKeyId。
   const accessKeyId = "<accessKeyId>"
   // 阿里云账号的临时accessKeySecret。
   const accessKeySecret = "<accessKeySecret>"
   // 临时访问密钥。
   const stsToken = "<accessToken>"
   // OSS访问域名。
   const endpoint = "https://<endpoint>"
   // OSS存储空间。
   const bucket = "<bucket>"
   // 对应OSS Object Key，可用于刷新token以及调用添加文件（夹）接口添加文件记录。
   const objectKey = "<mediaId>"

   func main() {
       // 构建oss client
       client, err := oss.New(endpoint, accessKeyId, accessKeySecret, oss.SecurityToken(stsToken))
       if err != nil {
           fmt.Println("Error:", err)
           os.Exit(-1)
       }

       // 获取存储空间。
       bucket, err := client.Bucket(bucket)
       if err != nil {
           fmt.Println("Error:", err)
           os.Exit(-1)
       }

       // 上传本地文件。
       err = bucket.PutObjectFromFile(objectKey, "<path_to_file>")
       if err != nil {
           fmt.Println("Error:", err)
           os.Exit(-1)
       }
   }
   ```

   C#

   ```
   // 以下参数为步骤1返回的上传凭证
   public static Object UploadFile(string endpoint, // "https://<endpoint>"
                                   string accessKeyId, // <accessKeyId>
                                   string accessKeySecret, // <accessKeySecret>
                                   string securityToken, // <securityToken>
                                   string bucketName, // <bucketName>
                                   string key // <mediaId>
                                   ) {
       DefaultCredentialsProvider credentialsProvider = new DefaultCredentialsProvider(new DefaultCredentials(accessKeyId, accessKeySecret, securityToken));
       ClientConfiguration clientConfiguration = new ClientConfiguration();
       clientConfiguration.Protocol = Protocol.Https; // 注意, 需要是HTTPS
       var client = new OssClient(endpoint, credentialsProvider, clientConfiguration);
       try {
           WebClient mywebclient = new WebClient();
           byte[] buffer = mywebclient.DownloadData("https://xxx");
           using (MemoryStream ms = new MemoryStream(buffer)) {
               return client.PutObject(bucketName, key, ms);
           }
       } catch (Exception e) {
       }
       return null;
   }
   ```

   JavaScript

   ```
   const OSS = require('ali-oss')

   // 以下参数为步骤1返回的上传凭证
   // OSS访问域名。
   let region = "<endpoint>.split(".")[0]"
   // 阿里云账号的临时accessKeyId。
   let accessKeyId = "<accessKeyId>"
   // 阿里云账号的临时accessKeySecret
   let accessKeySecret = "<accessKeySecret>"
   // OSS存储空间。
   let bucket = "<bucket>"
   // 临时访问密钥。
   let stsToken = "<securityToken>"
   // 对应OSS Object Key，可用于刷新token以及调用添加文件（夹）接口添加文件记录。
   let objectKey = "<mediaId>"

   const client = new OSS({
     region,
     accessKeyId,
     accessKeySecret,
     bucket,
     stsToken
   })
   client.options.endpoint.protocol="https:"

   async function put () {
     try {
       let result = await client.put(objectKey, '<path_to_file>')
       console.log(result)
     } catch (e) {
       console.log(e)
     }
   }

   put()
   ```

   > **[!NOTE]**
   >
   > 此Demo示例为本地文件上传，更多文件上传方式请参考[简单上传](https://open.dingtalk.com/document/object/simple-upload)。
3. 调用[添加文件（夹）](1564-add-file-and-folder.md)接口添加钉盘文件源信息。
