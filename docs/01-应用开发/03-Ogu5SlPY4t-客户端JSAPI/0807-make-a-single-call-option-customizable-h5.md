---
title: "拨打单人电话选项（可定制）"
source_url: "https://open.dingtalk.com/document/development/make-a-single-call-option-customizable-h5"
namespace: "development"
slug: "make-a-single-call-option-customizable-h5"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > H5微应用 > JSAPI参考 > 电话 > 拨打单人电话选项（可定制）"
doc_id: "HZqdJe1HgB"
updated_at: "2025-09-17 20:56:38"
---

> Source: https://open.dingtalk.com/document/development/make-a-single-call-option-customizable-h5
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > H5微应用 > JSAPI参考 > 电话 > 拨打单人电话选项（可定制）
> Updated: 2025-09-17 20:56:38

# 拨打单人电话选项（可定制）

调用**biz.telephone.quickCallList**拨打单人电话选项（可定制）。

## 调试

访问[JSAPI Explorer](https://open-dev.dingtalk.com/apiExplorer#/jsapi?api=biz.telephone.quickCallList)在线调试该接口。

## 使用说明

可以定制单人拨打选项，并能取到电话的唯一标识CallId。会根据实际情况展示，比如VoIP会根据对方是否激活钉钉展示，办公电话会根据是否开通具体显示。

| **客户端** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 支持 | 支持 | 支持 |

```
dd.biz.telephone.quickCallList({
       title  :  "呼叫 xxxx",
       content : "推荐使用办公电话，员工免费",
       corpId  :  "xxxxxxxxxx",
       phoneNumber : "176xxxxxxxx",
       typeList : [1,2,7],
       onSuccess  :  function(result)  {
                //callTypeList:[1,7]
                //callType:7 选择了办公电话
                //callId:"xxxxxxxxxxxxxxx"  全链路标识电话的唯一标识              
        },
       onFail  :  function(err)  {
                //  获取方式同上
                //"errorCode":2
                //"errorMessage":{"errorMessage":"没有传入电话号码或者工号"}
                //"errorCode":400072
                //"errorMessage":{"errorMessage":"办公电话余额不足"}
        }
})
```

## 参数说明

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| corpId | String | 企业的corpid。选择对应企业的办公电话拨打。 |
| staffId | String | 用户的userid。  **[!IMPORTANT]**     - 使用该参数时，corpId必填。 - staffId和phoneNumber中必须选择一个作为入参。 |
| phoneNumber | String | 电话号码。  **[!IMPORTANT]**  staffId和phoneNumber中必须选择一个作为入参。 |
| content | String | 展示内容。 |
| title | String | 展示标题。 |
| typeList | List | 定制拨打类型：   - TYPE\_VOIP = 1，VoIP - TYPE\_Global\_PSTN = 2，国际电话 - TYPE\_SYS = 3，系统电话 - TYPE\_VIDEO\_P2P = 5，点对点视频通话 - TYPE\_BIZ\_CALL = 7，办公电话 |

## 返回结果

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| callTypeList | List | 展示的拨打类型，比如办公电话如果没开通则不显示，对方如果未激活钉钉，则VoIP不显示。这是返回的具备的list。 |
| callType | Number | 对应电话类型，如果是-1，说明点击了【取消】。 |
| callId | String | 标识唯一一通通话。 |
