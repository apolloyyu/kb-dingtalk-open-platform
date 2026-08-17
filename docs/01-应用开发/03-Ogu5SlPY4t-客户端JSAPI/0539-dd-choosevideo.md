---
title: "选择视频"
source_url: "https://open.dingtalk.com/document/development/dd-choosevideo"
namespace: "development"
slug: "dd-choosevideo"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 多媒体 > 视频 > 选择视频"
doc_id: "ss386d5oW1"
updated_at: "2025-09-17 20:59:03"
---

> Source: https://open.dingtalk.com/document/development/dd-choosevideo
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 多媒体 > 视频 > 选择视频
> Updated: 2025-09-17 20:59:03

# 选择视频

调用**dd.chooseVideo**拍摄视频或从手机相册中选视频。

## 示例代码

```
dd.chooseVideo({
  sourceType: ['album','camera'],
  maxDuration: 60,
  success:(res)=> {
    console.log(res.filePath)
  },
  fail: (err)=> {
    console.log(err)
  }
})
```

## 入参

| **参数** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| sourceType | String[] | 否 | 视频来源。  **默认值**：['album','camera']。 |
| maxDuration | Number | 否 | 最长视频拍摄时间，单位为秒。  取值范围：   - Android：5-60 - iOS：15-60   **默认值**：60。 |
| success | Function | 否 | 接口调用成功回调函数。 |
| fail | Function | 否 | 接口调用失败回调函数。 |
| complete | Function | 否 | 接口调用结束回调函数 |

**success 返回值**

| **方法名** | **类型** | **说明** |
| --- | --- | --- |
| filePath | String | 视频临时文件路径。 |
| duration | Number | 视频时间长度。 |
| size | Number | 视频数据大小。 |
| height | Number | 视频高度。 |
| width | Number | 视频宽度。 |
