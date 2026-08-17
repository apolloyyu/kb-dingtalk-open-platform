---
title: "批量预览钉盘图片"
source_url: "https://open.dingtalk.com/document/development/batch-preview-of-nail-plate-pictures"
namespace: "development"
slug: "batch-preview-of-nail-plate-pictures"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > H5微应用 > JSAPI参考 > 钉盘 > 批量预览钉盘图片"
doc_id: "2Me95jSRzO"
updated_at: "2025-09-17 20:56:51"
---

> Source: https://open.dingtalk.com/document/development/batch-preview-of-nail-plate-pictures
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > H5微应用 > JSAPI参考 > 钉盘 > 批量预览钉盘图片
> Updated: 2025-09-17 20:56:51

# 批量预览钉盘图片

调用**biz.cspace.previewDentryImages**，实现批量预览钉盘图片。

## **效果示例**

![iShot2022-11-07 09](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6317877661/p512977.png)

## 使用说明

调用本接口前，请先引入钉钉js，参考[准备工作](https://open.dingtalk.com/document/orgapp/read-before-development)。

| **客户端** | **是否需要鉴权** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- | --- |
| 支持说明 | 不需要 | 支持(钉钉版本≥6.3.30) | 支持(钉钉版本≥6.3.30) | 不支持 |

```
 dd.biz.cspace.previewDentryImages({
                images:[
                  {
                    spaceId:"9590xxxxx",
                    dentryId:"7280xxxxx"
                  },
                  {
                    spaceId:"9590xxxxx",
                    dentryId:"7280xxxxx"
                  }
                ],
                index:1,
                onSuccess: function(result) {
                    console.log(JSON.stringify(result))

                },
                onFail : function(err) {
                    console.log(JSON.stringify(err))
                }
            })
```

## 参数说明

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| images | Array<Object> | 是 | 钉盘图片列表。目前无数量限制。 |
| spaceId | String | 是 | 图片所在的钉盘空间ID，调用[获取文件或文件夹列表](https://open.dingtalk.com/document/orgapp/obtain-the-file-list-storage)接口获取spaceId参数值。 |
| dentryId | String | 是 | 图片在钉盘空间内的节点ID，可调用[获取文件或文件夹列表](https://open.dingtalk.com/document/orgapp/obtain-the-file-list-storage)接口获取id参数值。 |
| index | Number | 否 | 从第几张开始预览。第一张index等于0，依次类推。  **[!NOTE]**  如果index超出images中图片的数量，默认从第一张开始预览。 |
| onSuccess | Function | 否 | 调用成功的回调函数。 |
| onFail | Function | 否 | 调用失败的回调函数。 |

## 返回结果

本接口只触发onSuccess回调，回调信息是空字符串。

调用本接口只预览参数无误的图片，图片参数spaceId和dentryId错误时，会出现以下情况：

- index对应的图片元素参数无误，但images内其他图片元素参数错误，该错误元素对应的图片不会被预览。
- index对应的图片元素参数错误，调用本接口会出现强提示“文件不存在或已删除”。

![iShot2022-11-07 09](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5317877661/p512976.png)
