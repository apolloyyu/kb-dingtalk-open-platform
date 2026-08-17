---
title: "选择图片"
source_url: "https://open.dingtalk.com/document/development/select-picture"
namespace: "development"
slug: "select-picture"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > H5微应用 > JSAPI参考 > 图片 > 选择图片"
doc_id: "M1N6LQrRP9"
updated_at: "2025-09-17 20:56:53"
---

> Source: https://open.dingtalk.com/document/development/select-picture
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > H5微应用 > JSAPI参考 > 图片 > 选择图片
> Updated: 2025-09-17 20:56:53

# 选择图片

调用**biz.util.chooseImage**，实现拍照或者选择本地照片。

## 使用说明

| **客户端** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 支持(钉钉版本≥6.5.35) | 支持(钉钉版本≥6.5.35) | 不支持 |

```
 dd.biz.util.chooseImage({
        count:1,
        secret:false,
        sourceType:['camera'],
        position:'front',
        onSuccess: (res) => {
           console.log(JSON.stringify(res))
            },
        onFail:(err) =>{
           console.log(JSON.stringify(err))
            }
})
```

## 参数说明

| 参数 | 类型 | 是否必传 | 说明 |
| --- | --- | --- | --- |
| count | Number | 否 | 最大可选照片数，默认1张。  **[!NOTE]**  当sourceType参数内只有camera时，该参数只能传1。 |
| sourceType | String Array | 否 | 相册选取或者拍照，默认 ['camera','album']。 |
| secret | boolean | 否 | 相机拍照生成的图片，是否存储到私有目录。   - **true**：图片存储到本机的目录为`/data/user/0/com.alibaba.android.rimet/cache/lightapp/xxxxx.jpg` - **false**：图片存储到本机的目录为`/storage/emulated/0/Android/data/com.alibaba.android.rimet/cache/Pissarro/xxx.jpg`   **[!NOTE]**  仅Android端并且钉钉客户端是6.5.27及以上版本支持。 |
| position | String | 否 | 相机拍照使用的摄像头：   - front：前置摄像头 - back：后置摄像头   **[!NOTE]**   - 默认back。 - 仅Android端并且钉钉客户端是6.5.27及以上版本支持。 |
| onSuccess | Function | 否 | 调用成功的回调函数。 |
| onFail | Function | 否 | 调用失败的回调函数。 |

## 返回结果

### 成功

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| filePaths | String Array | 图片的虚拟路径列表。 |
| files | Object | 图片的信息。 |
| path | String | 图片的虚拟路径。 |
| size | Number | 文件大小，单位Byte。 |
| fileType | String | 文件类型。 |

### 失败

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| result | Object | 当sourceType参数内只有camera时，该参数只能传1。 |

## 错误码

| 参数 | 说明 |
| --- | --- |
| 11 | 取消操作。 |
