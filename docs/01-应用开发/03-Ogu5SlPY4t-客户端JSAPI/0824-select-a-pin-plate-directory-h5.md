---
title: "选取钉盘目录"
source_url: "https://open.dingtalk.com/document/development/select-a-pin-plate-directory-h5"
namespace: "development"
slug: "select-a-pin-plate-directory-h5"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > H5微应用 > JSAPI参考 > 钉盘 > 选取钉盘目录"
doc_id: "peven1dIJX"
updated_at: "2025-09-17 20:56:52"
---

> Source: https://open.dingtalk.com/document/development/select-a-pin-plate-directory-h5
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > H5微应用 > JSAPI参考 > 钉盘 > 选取钉盘目录
> Updated: 2025-09-17 20:56:52

# 选取钉盘目录

调用**biz.cspace.chooseSpaceDir**选取钉盘目录。

## 调试

访问[JSAPI Explorer](https://open-dev.dingtalk.com/apiExplorer#/jsapi?api=biz.cspace.chooseSpaceDir)在线调试该接口。

## 使用说明

唤起钉盘选择器，从用户当前的企业空间或个人空间选择一个目录，用以保存文件等操作。

| **客户端** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 支持 | 支持 | 不支持 |

```
dd.biz.cspace.chooseSpaceDir({
                corpId:"dingf8b3508f3073b265",
                onSuccess: function(data) {
                 /* data结构
                 {"data":
                    [
                    {
                    "spaceId": "" //被选中的空间id
                    "path": "", // 被选中的文件夹路径
                    "dirId": "", //被选中的文件夹id
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
| corpId | String | 企业id，必填，只能选择该企业下的企业空间。 |

## 返回结果

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| spaceId | String | 被选中文件夹所在的钉盘空间id。 |
| path | String | 被选中的文件夹路径， 例如“/测试/测试子目录/”。 |
| dirId | String | 被选中的文件夹id。 |
