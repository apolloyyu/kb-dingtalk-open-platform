---
title: "设置项扩展点（HarmonyOS）"
source_url: "https://open.dingtalk.com/document/development/set-item-extension-point-harmonyos"
namespace: "development"
slug: "set-item-extension-point-harmonyos"
group: "专属版客户端插件"
tab: "HarmonyOS 插件"
breadcrumb: "使用扩展点 > 设置项扩展点"
doc_id: "yOU8gDeb8a"
updated_at: "2026-08-12 09:20:51"
---

> Source: https://open.dingtalk.com/document/development/set-item-extension-point-harmonyos
> Path: 专属版客户端插件 / HarmonyOS 插件 / 使用扩展点 > 设置项扩展点
> Updated: 2026-08-12 09:20:51

# 设置项扩展点（HarmonyOS）

## **基础信息**

| **扩展点编码** | **接口类** | **支持的平台** |
| --- | --- | --- |
| settings$setting\_items | DTExtension | HarmonyOS |

## **功能说明**

设置项扩展点可用于在设置页面中新增插件设置项的场景，如下效果示例：

![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8716230671/p1010095.png)

## **接口说明**

| **名称** | **说明** |
| --- | --- |
| getData() | ApiData 可识别字段：   - title：设置项标题 - subtitle：设置项右侧展示的子标题信息 - group：期望归属的分组（支持的分组：information、common、safe）   **[!NOTE]**  我们建议扩展点实现类持有 ApiData 数据，避免频繁创建 ApiData 对象。可参考示例代码实现。 |
| isEnabled() | 插件是否可用，默认`true`。 |
| invoke() | 入参：   - API = 'click'：ApiParams.context 为 CustomComponent 。   返回值：无 |

## **代码示例**

```
export class TCSettingMenu extends DTExtension {

  private data = new ApiData()

  constructor() {
    super()
    this.data = new ApiData()
      .put('title', '演示插件')
      .put('subtitle', '未开启')
      .put('group', 'safe')
  }

  getData(): ApiData {
    return this.data
  }

  async invoke(params: ApiParams): Promise<ApiData> {
    if (params.api === 'click' && params.context) {
      myBundle.routePage({
        component: params.context as CustomComponent,
        path: 'settings'
      })
    }
    return new ApiData()
  }

}
```

请在模块的 Index.ets 文件中导出类，并关联 dingtalk-bundle.json5 配置：

```
"extensions": [
  {
    "class": "TCSettingMenu",
    "bind": "settings$setting_items"
  }
],
```
