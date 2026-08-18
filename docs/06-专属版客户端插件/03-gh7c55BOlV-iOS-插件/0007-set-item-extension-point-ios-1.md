---
title: "设置项扩展点"
source_url: "https://open.dingtalk.com/document/development/set-item-extension-point-ios-1"
namespace: "development"
slug: "set-item-extension-point-ios-1"
group: "专属版客户端插件"
tab: "iOS 插件"
breadcrumb: "使用扩展点 > 设置项扩展点"
doc_id: "wCq13DeQOS"
updated_at: "2026-08-18 09:07:56"
---

> Source: https://open.dingtalk.com/document/development/set-item-extension-point-ios-1
> Path: 专属版客户端插件 / iOS 插件 / 使用扩展点 > 设置项扩展点
> Updated: 2026-08-18 09:07:56

# 设置项扩展点

## **基础信息**

| **扩展点编码** | **接口类** | **支持的平台** |
| --- | --- | --- |
| exclusive\_settings | DTKExclusiveExtensionSettingItemProtocol  DTKExclusiveExtensionSettingProtocol | iOS |

## **功能说明**

设置项扩展点可用于在设置页面中新增插件设置项的场景，如下效果示例：

![image..png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6452055861/p676031.png)

## **参数说明**

DTKExclusiveExtensionSettingItemProtocol

| **名称** | **说明** |
| --- | --- |
| title | 主标题 |
| actionTitle | 右侧副标题 |
| unreadType | 红点类型，0:不显示，1:默认小红点 2:数字红点 |
| unreadCount | 若unreadType=2，则用于显示红点数字 |
| isHidden | 是否隐藏 |
| sortIndex | 排序优先级，数字越小优先级越高 |
| onclick | 点击事件，可配置设置项的点击跳转 |

DTKExclusiveExtensionSettingProtocol

| **名称** | **说明** |
| --- | --- |
| refreshCellsBlock | 刷新列表事件，钉钉侧赋值 |
| createSettingItemList | 返回设置项的列表 |

## **代码示例**

Object C

```
DTKExclusiveExtensionRegisterPlugin(exclusive_settings, DTKExternalDemoSettingExtension)

@implementation DTKExternalDemoSettingItem
@synthesize actionTitle;
@synthesize isHidden;
@synthesize onclick;
@synthesize sortIndex;
@synthesize unreadCount;
@synthesize unreadType;
@synthesize title;
@end

@implementation DTKExternalDemoSettingExtension
// 返回设置项的列表
- (NSArray<id<DTKExclusiveExtensionSettingItemProtocol>> *)createSettingItemList{
    NSArray<id<DTKExclusiveExtensionSettingItemProtocol>> *items = [self generateItems];
    return items;
}

- (NSArray<id<DTKExclusiveExtensionSettingItemProtocol>> *)generateItems{
    DTKExternalDemoSettingItem *item1 =  [DTKExternalDemoSettingItem new];
    item1.title = @"扩展测试1";
    item1.actionTitle = @"右侧扩展测试1";
    item1.unreadType = 2;
    item1.unreadCount = 4;
    item1.onclick = ^{
        NSLog(@"点击扩展测试1");
    };
    
    DTKExternalDemoSettingItem *item2 =  [DTKExternalDemoSettingItem new];
    item2.title = @"扩展测试2";
    item2.actionTitle = @"右侧扩展测试2";
    item2.unreadType = 2;
    item2.unreadCount = 14;
    item2.onclick = ^{
        NSLog(@"点击扩展测试2");
    };
    return @[item1,item2];
    
}
@synthesize refreshCellsBlock;
```
