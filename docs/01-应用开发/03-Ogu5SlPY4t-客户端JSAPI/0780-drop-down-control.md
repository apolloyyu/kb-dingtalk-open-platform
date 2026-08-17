---
title: "下拉控件"
source_url: "https://open.dingtalk.com/document/development/drop-down-control"
namespace: "development"
slug: "drop-down-control"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > H5微应用 > JSAPI参考 > 业务 > 下拉控件"
doc_id: "Tng6p8m5kT"
updated_at: "2025-09-17 20:56:20"
---

> Source: https://open.dingtalk.com/document/development/drop-down-control
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > H5微应用 > JSAPI参考 > 业务 > 下拉控件
> Updated: 2025-09-17 20:56:20

# 下拉控件

调用**biz.util.chosen**下拉控件。

## 调试

访问[JSAPI Explorer](https://open-dev.dingtalk.com/apiExplorer#/jsapi?api=biz.util.chosen)在线调试该接口。

## 使用说明

| **客户端** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 支持 | 支持 | 不支持 |

```
dd.biz.util.chosen({
    source:[{
        key: '选项1', //显示文本
        value: '123' //值，
    },{
        key: '选项2',
        value: '234'
    }],
   selectedKey:'选项2' , // 默认选中的key
   onSuccess : function(result) {
    //onSuccess将在点击完成之后回调
        /*
        {
            key: '选项2',
            value: '234'
        }
        */
    },
   onFail : function(err) {}
})
```

## 参数说明

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| source | Array[String] | 下拉控件的内容。 |
| key | String | 显示文本。 |
| value | String | 文本对应的值。 |
| selectedKey | String | 默认选中的key值。 |

## 返回结果

| 参数 | 说明 |
| --- | --- |
| key | 返回选择的文本。 |
| value | 返回选择的值。 |

展示效果如下图所示：

> **[!IMPORTANT]**
>
>  Android端和iOS端不同系统展示结果可能会出现差别，请以最终的展示效果为准。

![下拉控件](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1605834061/p177833.png)
