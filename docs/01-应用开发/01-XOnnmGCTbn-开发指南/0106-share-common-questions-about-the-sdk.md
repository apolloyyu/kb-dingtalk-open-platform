---
title: "常见问题"
source_url: "https://open.dingtalk.com/document/dingstart/share-common-questions-about-the-sdk"
namespace: "dingstart"
slug: "share-common-questions-about-the-sdk"
group: "应用开发"
tab: "开发指南"
breadcrumb: "接入移动客户端 > 接入钉钉分享 > 常见问题"
doc_id: "TiLZLCxRPF"
updated_at: "2026-05-13 09:00:15"
---

> Source: https://open.dingtalk.com/document/dingstart/share-common-questions-about-the-sdk
> Path: 应用开发 / 开发指南 / 接入移动客户端 > 接入钉钉分享 > 常见问题
> Updated: 2026-05-13 09:00:15

# 常见问题

## 外部分享到钉钉

**Q：手机安装了钉钉，点击分享到钉钉，钉钉没有响应**

A：可能原因：传递的context不正确，分享到钉钉，需要使用Activity的context。

**Q：手机安装了钉钉，点击分享到钉钉，钉钉的界面出来了，结果点击分享时，没有响应**

A：可能原因有以下3个：

- 没有配置钉钉的混淆消息
- 没有网络
- 申请的钉钉的签名信息不匹配

**Q：外部链接分享钉钉，在钉钉内打开，页面底部出现“赞”和“评论”**

A：在分享链接中拼接参数 “\_dt\_no\_comment=false” 即可解决。

**Q：没有配置钉钉的混淆消息问题发现及解决**

- **如何发现**：

  - 查看log日志发现相关信息Log.e("DDMediaMessage", "get media object from bundle failed: unknown ident " + className)。
- **如何解决**：

  - 钉钉分享sdk的相关反混淆配置在分享的demo工程中，参照配置即可。

**Q：没有网络问题发现及解决**

- **如何发现**：

  - 查看log日志发现相关信息Log.e("ShareDelegate", "check app auth error，the reason is: " + s1)。
  - 通过钉钉分享提供的回调的activity中，查看信息。

    errorCode = BaseResp.ErrCode.ERR\_AUTH\_DENIED

    errorMsg = "key check error"
- **如何解决**：

  - 打开手机wifi或者移动网络。
  - 在自己的app中，做分享前判断有没有网络，如果没有网络，直接提示用户没有网络。

**Q：申请的钉钉的签名信息不匹配问题发现及解决**

- **如何发现**：

  - **方式1（推荐）**

    在自己的app或者测试app中，在分享程序前校验自己的app\_id、packageName以及签名是否与自己申请的一致。

    > **[!NOTE]**
    >
    > 本方式是建议的操作方式，而且在debug和release的测试版本中都可以加入以下的示例代码。

    MainActivity中有分享到钉钉的按钮，在分享正式调用前调用如下的逻辑：

    ```
    private static final String ONLINE_PACKAGE_NAME = "package_name_holder";//将值替换为在钉钉开放平台上申请时的packageName
    private static final String ONLINE_APP_ID = "app_id_holder";//将值替换为在钉钉开放平台上申请时平台生成的appId
    private static final String ONLINE_SIGNATURE = "signature_holder";//将值替换为在钉钉开放平台上申请时的signature
    private static final String CURRENT_USING_APP_ID = "package_app_id_holder";//将值替换为您使用的APP_ID

    /**
     * 校验分享到钉钉的参数是否有效
     * @return
     */
    private boolean checkShareToDingDingValid() {
        if(!TextUtils.equals(ONLINE_PACKAGE_NAME, getPackageName())){
            Toast.makeText(this, "包名与线上申请的不匹配", Toast.LENGTH_SHORT).show();
            return false;
        }
        if(!TextUtils.equals(ONLINE_APP_ID, CURRENT_USING_APP_ID)){
            Toast.makeText(this, "APP_ID 与生成的不匹配", Toast.LENGTH_SHORT).show();
            return false;
        }
        if(!TextUtils.equals(ONLINE_SIGNATURE, SignatureCheck.getMD5Signature(this, getPackageName()))){
            Toast.makeText(this, "签名与线上生成的不符", Toast.LENGTH_SHORT).show();
            return false;
        }
        return true;
    }
    ```
  - **方式2：查看log日志**

    Log.e("ShareDelegate", "check app auth error，the reason is: " + s1);
  - **方式3：通过钉钉分享提供的回调的activity中，查看信息**

    ```
    目前的错误信息是通用的 
    errorCode = BaseResp.ErrCode.ERR_AUTH_DENIED 
    errorMsg = "key check error"
    ```
- **如何解决**：

  - 核对签名信息，如果不匹配，更新签名信息。
  - 如果确认签名信息没有问题，检查是否是debug和release版本的问题；如果debug和release版本的签名不一致，需要根据这两个版本，分别申请app\_id。

## 钉钉分享到外部

**Q：找不到微信/qq/新浪微博**

A：可能原因：

- 手机端没有安装这些应用。
- 手机屏蔽了钉钉读取应用安装列表。
- 钉钉当前页面H5的配置，屏蔽了这些平台的分享。
