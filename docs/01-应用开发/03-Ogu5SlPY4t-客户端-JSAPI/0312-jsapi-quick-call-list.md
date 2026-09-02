---
title: "quickCallList"
source_url: "https://open.dingtalk.com/document/development/jsapi-quick-call-list"
namespace: "development"
slug: "jsapi-quick-call-list"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "办公电话 > quickCallList"
doc_id: "nKejTRvvUl"
updated_at: "2025-08-27 18:08:38"
---

> Source: https://open.dingtalk.com/document/development/jsapi-quick-call-list
> Path: 应用开发 / 客户端 JSAPI / 办公电话 > quickCallList
> Updated: 2025-08-27 18:08:38

# quickCallList

调用quickCallList，拨打单人电话选项。

## 支持说明

| 应用能力 | Android | iOS | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 6.0.0 | 不支持 | 6.0.0 | 6.0.0 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11652) |
| 小程序 | 6.0.0 | 不支持 | 6.0.0 | 6.0.0 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11652) |

## 支持应用类型

| 应用类型 | 是否支持调用 |
| --- | --- |
| 企业内部应用 | 是 |
| 第三方企业应用 | 是 |
| 第三方个人应用 | 是 |

## 鉴权规则

在H5应用中，调用[dd.config](https://open.dingtalk.com/document/orgapp/jsapi-authentication)完成鉴权后使用

在小程序应用中，无需鉴权即可直接调用

## **参数说明**

继承[通用输入对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性描述：

### 入参

- `title`（string，必填）：拨打电话时展示的标题。
- `corpId`（string，必填）：当前企业的corpId。
- `content`（string，必填）：拨打电话时展示的内容。
- `typeList`（array，必填）：定制拨打类型：  
    
  \* 1：VoIP  
  \* 2：国际电话，  
  \* 3：系统电话  
  \* 5：点对点视频通话  
  \* 7：办公电话
- `phoneNumber`（string）：被拨打的电话号码。  
    
    
  > staffId和phoneNumber中必须选择一个作为入参。
- `staffId`（string）：用户的userid。  
    
    
  > staffId和phoneNumber中必须选择一个作为入参。

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性描述：

### 出参

- `callTypeList`（array，必填）：展示的拨打类型，比如办公电话如果没开通则不显示，对方如果未激活钉钉，则VoIP不显示。这是返回的具备的list。  
    
  拨打类型：  
  \* 1：VoIP  
  \* 2：国际电话  
  \* 3：系统电话   
  \* 5：点对点视频通话  
  \* 7：办公电话
- `callType`（number，必填）：对应电话类型，如果是-1，说明点击了【取消】。
- `callId`（string，必填）：标识唯一一通通话。

## **示例****代码**

### 默认出入参

```
dd.quickCallList({
  title: '测试电话',
  corpId: 'ding1234xxxx',
  content: '推荐使用办公电话',
  staffId: '03432',
  typeList: [1, 2],
  phoneNumber: '155xxxxxxxx',
  success: (res) => {
    const { callId, callType, callTypeList } = res;
  },
  fail: () => {},
  complete: () => {},
});
```

`success`返回对象示例：

```
{ "callId": "xijdnxxxxx", "callType": -1, "callTypeList": [1, 2] }
```
