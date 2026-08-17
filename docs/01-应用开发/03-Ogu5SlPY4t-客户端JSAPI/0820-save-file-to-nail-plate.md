---
title: "保存文件到钉盘"
source_url: "https://open.dingtalk.com/document/development/save-file-to-nail-plate"
namespace: "development"
slug: "save-file-to-nail-plate"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > H5微应用 > JSAPI参考 > 钉盘 > 保存文件到钉盘"
doc_id: "OZlRLw4h9A"
updated_at: "2025-09-17 20:56:49"
---

> Source: https://open.dingtalk.com/document/development/save-file-to-nail-plate
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > H5微应用 > JSAPI参考 > 钉盘 > 保存文件到钉盘
> Updated: 2025-09-17 20:56:49

# 保存文件到钉盘

调用**biz.cspace.saveFile**保存文件到钉盘。

## 调试

访问[JSAPI Explorer](https://open-dev.dingtalk.com/apiExplorer#/jsapi?api=biz.cspace.saveFile)在线调试该接口。

## 使用说明

| **客户端** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 支持 | 支持 | 不支持 |

```
dd.biz.cspace.saveFile({
        corpId:"dingf8b3508f3073b265",
        url:"https://ringnerippca.files.wordpress.com/20.pdf",  // 文件在第三方服务器地址， 也可为通过服务端接口上传文件得到的media_id，详见参数说明
        name:"文件名",
        onSuccess: function(data) {
                 /* data结构
                 {"data":
                    [
                    {
                    "spaceId": "", //空间id
                    "fileId": "", //文件id
                    "fileName": "", //文件名
                    "fileSize": 111111, //文件大小
                    "fileType": "", //文件类型
                    }
                    ]
                 }
                 */
                },
        onFail: function(err) {
                    alert(JSON.stringify(err));
        }
    });
```

## 参数说明

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| corpId | String | 用户当前的corpid，只能存储到corpid对应企业的钉盘和个人钉盘。 |
| url | String | 文件在第三方服务器上的url地址或通过提交文件上传事务、单步文件上传获取到的media\_id。 |
| name | String | 文件保存的名字。 |
| onSuccess | Function | 调用成功的回调函数。 |
| onFail | Function | 调用失败的回调函数。 |
