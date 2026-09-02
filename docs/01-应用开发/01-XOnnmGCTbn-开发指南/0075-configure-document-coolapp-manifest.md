---
title: "配置文档酷应用Manifest"
source_url: "https://open.dingtalk.com/document/dingstart/configure-document-coolapp-manifest"
namespace: "dingstart"
slug: "configure-document-coolapp-manifest"
group: "应用开发"
tab: "开发指南"
breadcrumb: "开发酷应用 > 开发文档酷应用 > 配置文档酷应用Manifest"
doc_id: "QAJLK0v5V7"
updated_at: "2026-01-29 14:38:23"
---

> Source: https://open.dingtalk.com/document/dingstart/configure-document-coolapp-manifest
> Path: 应用开发 / 开发指南 / 开发酷应用 > 开发文档酷应用 > 配置文档酷应用Manifest
> Updated: 2026-01-29 14:38:23

# 配置文档酷应用Manifest

如果您需要了解文档酷应用Manifest，请参考本文档。

## **什么是文档酷应用Manifest**

文档酷应用的Manifest文件是用于描述一个文档酷应用的基本信息的JSON文件，通过配置manifest可以定义文档酷应用的以下几类信息：

1. 定义调试模式下文档酷应用的酷应用ID、酷应用名称，支持应用类型。
2. 指定酷应用在文档中如何进行渲染，包括自定义功能项名称，启动自定义功能后如何渲染UI界面。
3. 声明文档酷应用与文档模型进行何种交互，指定脚本服务。

## **配置属性**

下表定义了一个Manifest所需属性：

| **属性** | **使用场景** | **含义** |
| --- | --- | --- |
| dev | 调试模式下的文档酷应用 | 定义调试模式下文档酷应用的酷应用ID及名称。 |
| workbook | 钉钉表格酷应用 | 定义钉钉表格酷应用的基本信息。 |

### **dev**

dev属性定义了调试模式下文档酷应用的应用ID及名称等信息。在酷应用发布阶段，无需在manifest中定义dev属性。

| **属性** | **是否必填** | **类型** | **含义** |
| --- | --- | --- | --- |
| id | 是 | String | 文档酷应用的唯一标识。  **[!IMPORTANT]**  建议使用GUID生成工具生成ID，以避免和其它调试酷应用冲突，要求唯一。 |
| name | 是 | String | 文档酷应用名称。 |
| description | 否 | String | 文档酷应用描述。 |
| icon | 否 | String | 文档酷应用图标地址。 |

### **workbook**

workbook属性定义了钉钉表格酷应用的相关信息。

#### **参数示例：**

```
{
  "workbook": {
    "scriptService": {
      "url": "https://www.example.com/script.html"
    },
    "menus": [
      {
        "name": "启动",
        "action": {
          "type": "open-side-bar",
          "url": "https://www.example.com/sidebar.html"
        }
      }
    ]
  }
}
```

#### **参数说明：**

| 名称 | 是否必填 | 类型 | 含义 |
| --- | --- | --- | --- |
| scriptService | 否 | Object | 定义文档酷应用使用的脚本服务。 |
| url | 是 | String | 注册文档酷应用脚本服务的地址，由酷应用开发者提供。 |
| menus | 是 | Array | 定义文档酷应用提供的功能列表，及启用对应功能后如何渲染。 |
| name | 是 | String | 文档酷应用提供的功能名称。 |
| action | 是 | Object | 启用功能后如何进行渲染。 |
| type | 是 | String | 固定值`open-side-bar`，启用功能后打开钉钉表格右侧面板。 |
| url | 是 | String | 酷应用自定义UI面板地址，由酷应用开发者提供。 |
| onClose | 否 | Object | 关闭功能时是否进行提示。   - 类似一：     ```   {     type: 'default';   }   ``` - 类型二：     ```   {     type: 'confirm';     message: string;   }   ``` |

## **后续步骤**

如果你已经了解了文档酷应用Manifest，需要[接入文档酷应用](0074-access-document-coolapp.md)。

> **[!NOTE]**
>
> 如果你需要开发文档酷应用，详情参考[脚本服务和 UI 页面](0076-develop-document-coolapp-script-services-and-ui-pages.md)。
