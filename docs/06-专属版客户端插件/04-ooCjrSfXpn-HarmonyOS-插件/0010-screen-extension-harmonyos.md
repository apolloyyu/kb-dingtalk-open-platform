---
title: "截录屏控制扩展点（HarmonyOS）"
source_url: "https://open.dingtalk.com/document/development/screen-extension-harmonyos"
namespace: "development"
slug: "screen-extension-harmonyos"
group: "专属版客户端插件"
tab: "HarmonyOS 插件"
breadcrumb: "使用扩展点 > 截录屏控制扩展点"
doc_id: "fJ3yTbRZzY"
updated_at: "2026-08-12 09:20:54"
---

> Source: https://open.dingtalk.com/document/development/screen-extension-harmonyos
> Path: 专属版客户端插件 / HarmonyOS 插件 / 使用扩展点 > 截录屏控制扩展点
> Updated: 2026-08-12 09:20:54

# 截录屏控制扩展点（HarmonyOS）

## **基础信息**

| **扩展点编码** | **接口类** | **支持的版本** |
| --- | --- | --- |
| dingtalk\_bundles$screenshot | DTExtension | 专属钉钉基线: >=7.6.40 |

## **功能说明**

当你的业务期望控制专属钉钉 App 的截录屏管控时，可以使用该扩展点。实现扩展点后，你的业务策略将会同钉钉平台策略合并仲裁，最终的仲裁结果定义当前页面是否可以截录屏。

## **接口说明**

| **名称** | **说明** |
| --- | --- |
| invokeSync() | 入参：   - API = 'onCreate'：    - 扩展点构建事件，可用于初始化业务。 - API = 'getAbilityPrivacyLevel'    - 获取指定 Ability 的截屏管控等级   - 入参 1：ApiData.get('ability')，正在仲裁的钉钉 UIAbility Name。      - 钉钉主 Ability 名称: 'dingtalk'；     - 钉钉会议 Ability 名称：'meeting'；     - 钉钉直播 Ability 名称：'live'；     - 其他：'normal'        - 备注：未来长远钉钉 Ability 名称可能会发生调整，当出现不适配时，请关注。   - 入参 2：ApiData.get('screenSharingStatus')      - 当前会议共享屏幕的状态   - 返回值：ApiData.put('level') = 0/1/2/3/4      - 0：代表本业务不处理     - 1：代表本业务期望禁止截屏（建议优先使用）     - 2：代表本业务由于特殊场景（比如屏幕共享）期望临时允许截屏     - 3：代表本业务认为是特殊私密数据（比如密聊），禁止截屏     - 其他值：无效，默认位为 0 - 钉钉根据各个业务的等级，合并取最高优先级。 |
| notifyDataChange() | 通知业务策略有变更，刷新 UIAbility 配置。  **[!NOTE]**  请避免在 `invokeSync(api='getAbilityPrivacyLevel')` 中调用 `notifyDataChange`，否则会出现死循环。 |
| getData() | 无效接口 |
| invoke() | 无效接口 |

## **示例代码**

请记得在 Index.ets 以及 dingtalk-bundle.json5 中配置插件。

```
import { ApiData, ApiParams, ApiRequest, DTExtension } from "@dingtalk/bundle_openapi";
import { myBundle } from "@dingtalk/bundle_testcase/src/main/ets/bundle/Bundle";

export class TCScreenshotExtension extends DTExtension {

  invokeSync(params: ApiParams): ApiData | undefined {
    switch (params.api) {
      case 'onCreate':
        console.warn('testcase', 'TCScreenshotExtension onCreate')
        return undefined

      case 'getAbilityPrivacyLevel':
        return this.getAbilityPrivacyLevel(params)

      default:
        return undefined
    }
  }

  getAbilityPrivacyLevel(params: ApiParams): ApiData {
    const status = params.data?.getBool('screenSharingStatus')
    const ability = params.data?.getString('ability')

    const res = new ApiData().put('level', 1)
    return res
  }
}
```

## **关联事件**

当你的插件使用了截屏控制扩展点时，可能还希望感知钉钉会议共享屏幕状态，方便做精细化管控，你可以使用如下事件。

事件名称：conference.screenshare.change

事件作用：当钉钉会议共享屏幕状态变更时会触发本事件，示例代码如下：

```
interface ScreenModel {
  isCasting?: boolean
}

myBundle.onEvent('conference.screenshare.change', (model: ScreenModel) => {
  console.error('open_bundle', `testcase receive event ${model.isCasting}`)
})
```
