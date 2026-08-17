---
title: "获取图片信息"
source_url: "https://open.dingtalk.com/document/development/dd-getimageinfo"
namespace: "development"
slug: "dd-getimageinfo"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 多媒体 > 图片 > 获取图片信息"
doc_id: "sBoR0rG8ta"
updated_at: "2025-09-17 20:58:59"
---

> Source: https://open.dingtalk.com/document/development/dd-getimageinfo
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 多媒体 > 图片 > 获取图片信息
> Updated: 2025-09-17 20:58:59

# 获取图片信息

调用**dd.getImageInfo**获取图片信息。

## 扫码体验

![1595557868714-2](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3579903061/p174117.png)

## **示例代码**

```
//网络图片路径
dd.getImageInfo({
      src:'https://img.alicdn.com/tps/TB1sXGYIFXXXXc5XpXXXXXXXXXX.jpg',
      success:(res)=>{
        console.log(JSON.stringify(res))
      }
    })
  
//filePaths
dd.chooseImage({
      success: (res) => {
        dd.getImageInfo({
          src:res.filePaths[0],
          success:(res)=>{
            console.log(JSON.stringify(res))
          }
        })
      },
    })

//相对路径
dd.getImageInfo({
      src:'image/api.png',
      success:(res)=>{
        console.log(JSON.stringify(res))
      }
    })
```

## **入参**

| **参数** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| src | String | 否 | 图片路径，目前支持：网络图片路径、相对路径。 |
| success | Function | 否 | 调用成功的回调函数。 |
| fail | Function | 否 | 调用失败的回调函数。 |
| complete | Function | 否 | 调用结束的回调函数（调用成功、失败都会执行）。 |

**success 返回值**

| **名称** | **类型** | **描述** |
| --- | --- | --- |
| width | Number | 图片宽度，单位px。 |
| height | Number | 图片高度，单位px。 |
| path | String | 图片本地路径。 |
