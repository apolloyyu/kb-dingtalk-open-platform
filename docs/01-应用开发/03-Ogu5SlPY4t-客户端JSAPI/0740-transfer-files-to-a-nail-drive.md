---
title: "转存文件到钉盘"
source_url: "https://open.dingtalk.com/document/development/transfer-files-to-a-nail-drive"
namespace: "development"
slug: "transfer-files-to-a-nail-drive"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 开放接口 > 钉盘 > 转存文件到钉盘"
doc_id: "gueqo34d9s"
updated_at: "2025-09-17 21:01:16"
---

> Source: https://open.dingtalk.com/document/development/transfer-files-to-a-nail-drive
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 开放接口 > 钉盘 > 转存文件到钉盘
> Updated: 2025-09-17 21:01:16

# 转存文件到钉盘

调用**dd.saveFileToDingTalk**转存文件到钉盘。

## 示例代码

```
dd.saveFileToDingTalk({
    url:"https://ringnerippca.files.wordpress.com/20.pdf",  // 文件在第三方服务器地址
    name:"文件名",
    success: (res) => {
        /* data结构
         {"data":
            [
            {
            "spaceId": "" //空间id
            "fileId": "", //文件id
            "fileName": "", //文件名
            "fileSize": 111111, //文件大小
            "fileType": "", //文件类型
            }
            ]
         }
         */
    },
    fail: (err) =>{
        dd.alert({
            content:JSON.stringify(err)
        })
    }
})
```

## **入参**

| **参数** | **类型** | **说明** |
| --- | --- | --- |
| url | String | 文件在第三方服务器上的url地址或通过[单步文件上传](https://open.dingtalk.com/document/orgapp/single-step-file-upload)获取到的media\_id。  **[!NOTE]**  如果是url地址，要求资源请求返回消息头中需要包含Content-Length字段，且>0。 |
| name | String | 文件保存的名字。 |
