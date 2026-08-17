---
title: "获取专属安全配置"
source_url: "https://open.dingtalk.com/document/development/obtain-a-dedicated-security-configuration-1"
namespace: "development"
slug: "obtain-a-dedicated-security-configuration-1"
group: "专属版客户端插件"
tab: "功能介绍"
breadcrumb: "使用开放API > 获取专属安全配置"
doc_id: "PaGDDz57ti"
updated_at: "2025-10-15 17:02:30"
---

> Source: https://open.dingtalk.com/document/development/obtain-a-dedicated-security-configuration-1
> Path: 专属版客户端插件 / 功能介绍 / 使用开放API > 获取专属安全配置
> Updated: 2025-10-15 17:02:30

# 获取专属安全配置

## **基础信息**

获取钉钉开放的专属安全配置，基于此接口安全类插件可同钉钉专属安全业务实现深度融合。

| **API名称** | **调用方式** | **支持的平台** |
| --- | --- | --- |
| dd.exclusive.getOpenConfig | 异步调用 | Android、iOS、HarmonyOS |

如下图为安全沙箱相关的开放配置，用户在钉钉管理后台操作开关后，安全类插件可以使用接口获取到用户的配置。

![image_b0155a30cc0v](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6336314861/p610659.png)

## **入参**

| **参数** | **类型** | **描述** |
| --- | --- | --- |
| keys | List | 期望获取的开放配置key列表。 |

## **返回结果**

返回Map数据。

> **[!IMPORTANT]**
>
> - 如果Map中不存在指定的Key或为Null，代表用户未配置该值。
> - 接口必须在有登录态时调用。
> - 在首次登录时，由于服务端推送数据具有延迟性，返回结果可能为空，请参考配置更新监听配置的变更。

## **配置更新**

1. Android平台配置更新可使用EventReceiver注册监听“exclusive.config.update”事件，当收到配置变更事件时，可重新调用接口获取最新配置。
2. iOS平台可直接监听系统通知，通知名称为@"DTKExclusiveExternalOAOpenConfigUpdate"，从通知结果中获取更新的配置。
3. HarmonyOS可使用myBundle注册监听“exclusive.config.update”事件。

Android-Java

```
// 变更事件监听
@Event(event={"exclusive.config.update"})
public class ExclusiveReceiver implements EventReceiver {

    @Override
    public void onEvent(String event, Bundle bundle) {
        String screenCtrlValue = bundle.getString("open_screen_protect");
        ...
    }
}
```

Object C

```
//注册监听
  [[NSNotificationCenter defaultCenter] addObserver:self
                                           selector:@selector(onExclusiveConfigUpdate:)
                                               name:@"DTKExclusiveExternalOAOpenConfigUpdate"
                                             object:nil];
//监听处理
- (void)onExclusiveConfigUpdate:(NSNotification *)notify
{
   //变更的config
   NSDictionary *changedConfigs = [notify.userInfo objectForKey:@"changedConfigs"];
   //此次配置中被移除的key列表
   NSArray *removedKeys = [notify.userInfo objectForKey:@"removedKeys"];
}
```

arkts

```
myBundle.onEvent('exclusive.config.update', (keys: Array<string>) => {
  // Keys为变化的配置列表
})
```

## **示例代码**

Android-Java

```
ApiRequest request = new ApiRequest();
request.api = "dd.exclusive.getOpenConfig";

ArrayList<String> list = new ArrayList<>();
list.add("open_clipboard_paste");
list.add("open_screen_protect");
request.putListParam("keys", list);

ApiResponse response = bundleContext.invokeApi(request, new ApiCallback<ApiResponse> {
		@Override
		public void onSuccess(ApiResponse response) {
    		Map<String, String> resMap = response.getMapResult();
        String config = resMap.get("open_screen_protect");
        ...
    }
});
```

Object C

```
 id<DTKExternalNativeAPIServiceProtocol> handler = DTKExternalGetImpl(@"your_bundle_id", DTKExternalNativeAPIServiceProtocol);
    NSString *apiName = @"dd.exclusive.getOpenConfig";
    
    NSArray *keyList = @[@"open_clipboard_paste",@"open_screen_protect"];
    NSDictionary *queryList = @{@"keys":keyList};
    
    [handler invokeNativeAPI:apiName requestParam:^(id<DTKExternalAPIRequest>  _Nonnull param, id<DTKExternalAPIContext>  _Nonnull context) {
        param.requestParams = queryList;
        
     } callback:^(NSDictionary * _Nonnull response) {
         NSString *config1 = response[@"open_clipboard_paste"];
         NSString *config2 = response[@"open_screen_protect"];
            
    }];
```

arkts

```
const param = new Map<string, APIDataType>()
param.set('keys', ['open_share_control', 'open_root_detection'])

myBundle.invokeApi({ 
  api: 'dd.exclusive.getOpenConfig', 
  params: param})
.then((resp) => { 
  resp.getString('open_share_control')
})
.catch((e: Error) => { 
  myBundle.toast(`用例失败：${e.message}`) 
})
```
