---
title: "多选组件"
source_url: "https://open.dingtalk.com/document/development/multiple-select-components"
namespace: "development"
slug: "multiple-select-components"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > H5微应用 > JSAPI参考 > 弹窗 > 多选组件"
doc_id: "I5eoOmNxwv"
updated_at: "2025-09-17 20:56:30"
---

> Source: https://open.dingtalk.com/document/development/multiple-select-components
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > H5微应用 > JSAPI参考 > 弹窗 > 多选组件
> Updated: 2025-09-17 20:56:30

# 多选组件

调用**biz.util.multiSelect**多选组件。

## 调试

访问[JSAPI Explorer](https://open-dev.dingtalk.com/apiExplorer#/jsapi?api=biz.util.multiSelect)在线调试该接口。

## 使用说明

| **客户端** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 支持 | 支持 | 不支持 |

```
dd.biz.util.multiSelect({
    options:['选项1', '选项2', '选项3', '选项4'],
    selectOption:['选项3'],
    onSuccess : function(result) {
        /* 返回用户选中的index数组，从0开始。 例如
             [ 2, 3 ]
        */
    },
    onFail : function() {}
})
```

## 参数说明

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| options | Array | 待选选项列表。 |
| selectOption | String | 已选选项列表。 |

## 返回结果

返回结果为数组，包含用户选中的index列表，从0开始。
