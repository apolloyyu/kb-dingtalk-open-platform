---
title: "选取钉盘目录"
source_url: "https://open.dingtalk.com/document/development/select-a-pin-plate-directory"
namespace: "development"
slug: "select-a-pin-plate-directory"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 开放接口 > 钉盘 > 选取钉盘目录"
doc_id: "vlOQPIyLrT"
updated_at: "2025-09-17 21:01:18"
---

> Source: https://open.dingtalk.com/document/development/select-a-pin-plate-directory
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 开放接口 > 钉盘 > 选取钉盘目录
> Updated: 2025-09-17 21:01:18

# 选取钉盘目录

调用**dd.chooseDingTalkDir**唤起钉盘选择器， 从用户当前的企业空间或个人空间选择一个目录， 用以保存文件等操作。

## 示例代码

```
dd.chooseDingTalkDir({
    success: (res) => {
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
| spaceId | String | 被选中文件夹所在的钉盘空间id。 |
| path | String | 被选中的文件夹路径， 例如“/测试/测试子目录/”。 |
| dirId | String | 被选中的文件夹id。 |
