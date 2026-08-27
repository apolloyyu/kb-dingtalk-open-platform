---
title: "上传文件"
source_url: "https://open.dingtalk.com/document/development/upload-file-stream"
namespace: "development"
slug: "upload-file-stream"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > e签宝 1.0 > 文件 > 上传文件"
doc_id: "eV6cAKj4FU"
updated_at: "2026-06-23 18:10:40"
---

> Source: https://open.dingtalk.com/document/development/upload-file-stream
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > e签宝 1.0 > 文件 > 上传文件
> Updated: 2026-06-23 18:10:40

# 上传文件

本文介绍了如何通过文件流的方式向获取到的文件上传地址上传文件。

## 上传方式

- 使用HTTP PUT方式上传。
- 上传时在HTTP Header中增加字段Content-MD5和Content-Type，字段值与获取文件直传地址接口中contentMd5和contentType值保持一致，否则会出现错误码为403的错误。

  - **Content-MD5**：base64编码的文件MD5
  - **Content-Type**：文件MIME类型，支持以下格式：

    - application/octet-stream
    - application/pdf
    > **[!IMPORTANT]**
    >
    > Content-Type的格式要和获取文件上传地址接口的请求参数contentType格式一致，否则会出现错误码为403的错误。
  - HTTP BODY：待上传文件的二进制字节流。

## 示例

**请求示例**：

```
PUT /ObjectName HTTP/1.1
Content-Type:application/octet-stream
Content-MD5:eB5eJF1ptWaXm4bijSPyxw==
```

**响应示例**：

```
HTTP/1.1 200 OK
Server: AliyunOSS
Date: Tue, 04 Dec 2018 15:56:38 GMT
Content-Length: 0
Connection: keep-alive
x-oss-request-id: 5C06A3B67B8B5A3DA422299D
ETag: "D41D8CD98F00B204E9800998ECF8427E"
x-oss-hash-crc64ecma: 0
Content-MD5: 1B2M2Y8AsgTpgAmY7PhCfg==
x-oss-server-time: 7
```

## 如何计算Content-MD5

Content-MD5计算方式如下：

1. 计算MD5加密的二进制数组（128位）。
2. 对这个二进制数组进行base64编码（而不是对32位字符串编码）

**JAVA代码示例**：

```
public static void main(String[] args) {

        System.out.println("结果：" + getStringContentMD5("D:/无微信“轻流产品介绍”.pdf"));
    }

    /***
    * 计算字符串的Content-MD5
    * @param str 文件路径
    * @return
    */
    public static String getStringContentMD5(String str) {
        // 获取文件MD5的二进制数组（128位）
        byte[] bytes = getFileMD5Bytes1282(str);
        // 对文件MD5的二进制数组进行base64编码
        return new String(Base64.encodeBase64(bytes));
    }

    /***
     * 获取文件MD5-二进制数组（128位）
     * 
     * @param filePath
     * @return
     * @throws IOException
     */
    public static byte[] getFileMD5Bytes1282(String filePath) {
        FileInputStream fis = null;
        byte[] md5Bytes = null;
        try {
            File file = new File(filePath);
            fis = new FileInputStream(file);
            MessageDigest md5 = MessageDigest.getInstance("MD5");
            byte[] buffer = new byte[1024];
            int length = -1;
            while ((length = fis.read(buffer, 0, 1024)) != -1) {
                md5.update(buffer, 0, length);
            }
            md5Bytes = md5.digest();
            fis.close();
        } catch (FileNotFoundException e) {
            System.out.println(e.getMessage());
            e.printStackTrace();
        } catch (NoSuchAlgorithmException e) {
            System.out.println(e.getMessage());
            e.printStackTrace();
        } catch (IOException e) {
            System.out.println(e.getMessage());
            e.printStackTrace();
        }
        return md5Bytes;
    }
```

**PHP代码示例**：

```
$contentBase64Md5 = getContentBase64Md5($filePath);

function getContentBase64Md5($filePath){
    //获取文件MD5的128位二进制数组
    $md5file = md5_file($filePath,true);
    //计算文件的Content-MD5
    $contentBase64Md5 = base64_encode($md5file);
    echo ("contentBase64Md5=".$contentBase64Md5);
    return $contentBase64Md5;
}
```

**.NET请求示例**：

```
public static string GetContentMD5FromFile(string filePath)
        {
            string ContentMD5 = null;
            try
            {
                FileStream file = new FileStream(filePath, FileMode.Open, FileAccess.Read);
                System.Security.Cryptography.MD5 md5 = new System.Security.Cryptography.MD5CryptoServiceProvider();
                // 先计算出上传内容的MD5，其值是一个128位（128 bit）的二进制数组
                byte[] retVal = md5.ComputeHash(file);
                file.Close();
                // 再对这个二进制数组进行base64编码
                ContentMD5 = Convert.ToBase64String(retVal).ToString();
                MessageBox.Show("MD5:" + ContentMD5);
                return ContentMD5;
            }
            catch (Exception ex)
            {
                MessageBox.Show("错误信息", "计算文件的Content-MD5值时发生异常：" + ex.Message);
                return ContentMD5;
            }
        }
```
