---
title: "登录认证扩展（认证多因子）"
source_url: "https://open.dingtalk.com/document/development/authentication-extension-android"
namespace: "development"
slug: "authentication-extension-android"
group: "专属版客户端插件"
tab: "Android 插件"
breadcrumb: "使用扩展点 > 登录认证扩展（认证多因子）"
doc_id: "Cat2wY9Ul0"
updated_at: "2026-08-18 09:07:56"
---

> Source: https://open.dingtalk.com/document/development/authentication-extension-android
> Path: 专属版客户端插件 / Android 插件 / 使用扩展点 > 登录认证扩展（认证多因子）
> Updated: 2026-08-18 09:07:56

# 登录认证扩展（认证多因子）

## **基础信息**

| **扩展点编码** | **接口类** | **支持的平台** |
| --- | --- | --- |
| loginAuth | LoginAuthPlugin | Android |

## **功能说明**

当钉钉登录成功后，开发者可使用该插件在之后的流程中插入自定义流程环节，比如二次验证等。

> **[!NOTE]**
>
> - 该扩展点必须经过钉钉授权方可使用，否则将无法生效，开发前如果需要请务必先同钉钉技术确认方案。
> - 只有经过钉钉后台配置的主组织才生效，测试前请确认加入正确的组织。

## **接口说明**

auth接口参数说明

| **参数** | **说明** |
| --- | --- |
| auth() | account：  type：用于标识账号是什么类型，0代表手机号，1代表邮箱账号；  params：自定义参数，比如IP、APPKEY等。该参数需要向钉钉方申请配置到服务端，参数会在登录时下发，参数按组织维度配置。当交付后不需要变更的参数，可自行把客户参数放在独立aar中，解耦集成。  callback：  备注说明：  （1）callback的onSuccess代表节点成功，继续回到钉钉登录流程中；  （2）callback的onException代表节点失败，中断登录流程回到登录页，第一个参数为code，第二个参数为msg，返回后钉钉会弹出Dialog，展示内容为msg（如果不为空）。  （3）当前期望直接返回中断登录（比如用户按了返回按钮），请返回code="11100"， 即：callback.onException("11100", "")； |
| account | 代表账号，如果是手机号格式为：+86-13221077194 |
| type | 用于标识账号是什么类型，0代表手机号，1代表邮箱账号； |
| params | 自定义参数，比如IP、APPKEY等。该参数需要向钉钉方申请配置到服务端，参数会在登录时下发，参数按组织维度配置。当交付后不需要变更的参数，可自行把客户参数放在独立aar中，解耦集成。 |
| callback | 节点执行完成的回调，回调后将会重新回到钉钉登录流程。   - onSuccess：Auth成功，将回到钉钉登录流程中； - onException: Auth失败，将中断登录流程回到登录页，第一个参数为code，第二个参数为msg。参钉钉会弹出Dialog，展示内容为msg（如果不为空）。   **[!NOTE]**  当期望直接中断登录（比如用户按了返回按钮），请返回code="11100"， 即：callback.onException("11100", "")；  **[!IMPORTANT]**  无论成功与否，请务确认所有分支均执行了回调，否则将导致钉钉登录流被卡住。 |

## **代码示例**

Java

```
@Extension(id="example_auth", target="loginAuth")
public class DemoLoginPlugin extends LoginAuthPlugin {

    @Override
    public void auth(String account, int type, 
			Map<String, String> map, ApiListener listener) {

        //执行验证逻辑，打开SMS验证页面
        Intent intent = new Intent(
						context, DemoSmsActivity.class);
        intent.putExtra("mobile", mobile);
        context.startActivity(intent);
    }

    @Override
    public String getBundleId() {
        return "demoid";
    }
}
```

另外，为了在登录流程中插入自定义activity，请在 activity 的 manifest 配置中追加 meta-data，meta-data 请保持一致，activity 在完成操作后请及时 finish 掉。示例如下：

XML

```
<activity android:name=".plugin.ExampleAuthActivity" android:exported="false">     
  <meta-data
         android:name="com.alibaba-inc.check.login.status.resume"
         android:value="0"/>
</activity>
```
