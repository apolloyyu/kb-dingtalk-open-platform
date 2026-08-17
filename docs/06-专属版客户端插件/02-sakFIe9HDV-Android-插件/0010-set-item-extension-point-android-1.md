---
title: "设置项扩展点（Android）"
source_url: "https://open.dingtalk.com/document/development/set-item-extension-point-android-1"
namespace: "development"
slug: "set-item-extension-point-android-1"
group: "专属版客户端插件"
tab: "Android 插件"
breadcrumb: "使用扩展点 > 设置项扩展点"
doc_id: "PQxnen23wp"
updated_at: "2026-08-12 09:20:50"
---

> Source: https://open.dingtalk.com/document/development/set-item-extension-point-android-1
> Path: 专属版客户端插件 / Android 插件 / 使用扩展点 > 设置项扩展点
> Updated: 2026-08-12 09:20:50

# 设置项扩展点（Android）

## **基础信息**

| **扩展点编码** | **接口类** | **支持的平台** |
| --- | --- | --- |
| setting\_items | EpSettingMenu | Android |

## **功能说明**

设置项扩展点可用于在设置页面中新增插件设置项的场景，如下效果示例：

![image_bb232600ccfj](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5628744861/p610718.png)

## **接口说明**

| **名称** | **说明** |
| --- | --- |
| getMenuObject() | 返回设置项描述信息，包括title、icon等。 |
| isVisible() | 设置项是否需要展示。true为展示，false为隐藏。 |
| isEnabled() | 暂不支持，请默认返回true。 |
| bindData() | 暂不支持 |
| getUnread() | 暂不支持 |
| setContext() | 设置页上下文，可获取对应的Activity |
| onClick() | 点击事件，可配置设置项的点击跳转 |

## **代码示例**

Java

```
@Extension(id = "example_setting", target = "setting_items")
  public class ExampleSetting extends EpSettingMenu {

    @Override
    public SettingMenuObject getMenuObject() {
      SettingMenuObject menu = new SettingMenuObject();
      menu.title = "示例设置项";
      return menu;
    }

    @Override
    public boolean isVisible() {
      return true;
    }

    @Override
    public boolean isEnabled() {
      return true;
    }

    @Override
    public void bindData(Object o) {}

    @Override
    public AdsViewObject getUnread() {
      return null;
    }

    @Override
    public void setContext(SettingContext context) {}

    @Override
    public void onClick(View v) {
        
    }
  }
```
