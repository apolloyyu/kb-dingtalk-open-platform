---
title: "JSAPI鉴权"
source_url: "https://open.dingtalk.com/document/development/jsapi-authentication"
namespace: "development"
slug: "jsapi-authentication"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "JSAPI鉴权"
doc_id: "ViV3AiVTvR"
updated_at: "2026-07-22 16:25:11"
---

> Source: https://open.dingtalk.com/document/development/jsapi-authentication
> Path: 应用开发 / 客户端 JSAPI / JSAPI鉴权
> Updated: 2026-07-22 16:25:11

# JSAPI鉴权

钉钉提供的JSAPI有很多是手机的基础能力，对这些JSAPI的调用不需要进行鉴权（**不需要进行dd.config**），只需要在**dd.ready**里调用。对于一些钉钉业务、安全相关的JSAPI的调用，需要先鉴权，然后再调用。

了解JSAPI是否需要鉴权，请查看[H5微应用JSAPI总览](0745-jsapi-overview-1.md)。

## 接入必读

- 鉴权是针对微应用页面实现的。如果当前页面用到需要鉴权的JSAPI，此页面就需要执行鉴权流程。钉钉开放平台会获取当前页面中需要鉴权的JSAPI，然后执行鉴权。

  要求开发者的签名**signature**值必须与开放平台的保持一致。

  > **[!IMPORTANT]**
  >
  > 计算签名时用到的URL，**必须是使用了需要鉴权的JSAPI的页面。**
- 针对VUE单页面应用，鉴权需要对父页面实现，因为计算签名方法不支持路由页面地址。

  实现流程如下，当使用了需要鉴权的子页面加载时，需要刷新父页面，使父页面完成鉴权流程，然后该子页面上就可以调用需要鉴权的JSAPI。

## 步骤一：获取access\_token

- 企业内部应用可通过[获取企业内部应用的accessToken](../02-4a8AMF6u2A-服务端-API/0033-obtain-the-access-token-of-an-internal-app.md)接口获取。
- 第三方企业应用可通过[获取第三方应用授权企业的accessToken](../02-4a8AMF6u2A-服务端-API/0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。

> **[!IMPORTANT]**
>
> 必须使用**当前微应用的参数**获取access\_token，

## 步骤二：获取jsapi\_ticket

通过[获取jsapiTicket](../02-4a8AMF6u2A-服务端-API/0039-create-a-jsapi-ticket.md)接口获取jsapi\_ticket时，请注意：

- 企业内部应用和第三方企业应用获取 jsapiTicket 后，如果 jsapiTicket 尚未过期，再次调用[获取jsapiTicket](../02-4a8AMF6u2A-服务端-API/0039-create-a-jsapi-ticket.md)接口时，返回的 jsapiTicket 值与之前的相同，只是续期了 2 小时。需要注意的是，从 jsapiTicket 生成起，最大过期时间为 24 小时，即使续期后，最大过期时间仍从 jsapiTicket 生成起计算。

  > 例如：当你早上 9 点，生成一个 jsapiTicket 时，即使一直续期，第二天早上 9 点，jsapiTicket 也会过期，需要重新生成一个新的 jsapiTicket。
- 企业内部应用获取jsapi\_ticket，一个appKey对应一个jsapi\_ticket，所以在使用的时候需要将jsapi\_ticket以appKey为维度进行缓存下来（设置缓存过期时间2小时），**并不需要每次都通过接口拉取**。

## 步骤三：获取签名参数

在前端进行鉴权之前，需要获取以下签名所需的参数：

| **参数** | **说明** | 开发企业内部应用 | ISV开发第三方企业应用 |
| --- | --- | --- | --- |
| **url** | 当前网页的URL，不包含#及其后面部分。  **[!NOTE]**   - 如果是单页面应用，请参考本文的最上方[接入必读](#)。 - 必须是当前页面的 location.href 的原内容，请勿提前进行encode/urlencode处理，否则会引起编码不一致最终导致**签名校验失败**。 | — | — |
| **nonceStr** | 自定义固定字符串。 | — | — |
| **agentId** | 应用的标识 | 可以在[开发者后台](https://open-dev.dingtalk.com/#/isveapp)的应用详情页中获取。 | 可以从授权信息中获取到。 |
| **timeStamp** | 时间戳 | 当前时间，但是前端和服务端进行校验时候的值要一致。 | 当前时间，但是前端和服务端进行校验时候的值要一致。 |
| **corpId** | 企业ID | 企业的corpid，可以在[开发者后台](https://open-dev.dingtalk.com/#/isveapp)首页获取。 | 通过在页面地址上追加?`corpId=$CORPID$`进行获取。 |

## 步骤四：计算签名

在服务端通过**sign(**`ticket`**,** `nonceStr`**,** `timeStamp`**,** `url`**)**计算前端校验需要使用的签名信息。

示例代码：

```
import java.net.URL;
import java.net.URLDecoder;
import java.security.MessageDigest;
import java.util.Formatter;
import java.util.Random;

/**
 * 计算dd.config的签名参数
 **/
public class DdConfigSign {

    /**
     * 计算dd.config的签名参数
     *
     * @param jsticket  通过微应用appKey获取的jsticket
     * @param nonceStr  自定义固定字符串
     * @param timeStamp 当前时间戳
     * @param url       调用dd.config的当前页面URL
     * @return
     * @throws Exception
     */
    public static String sign(String jsticket, String nonceStr, long timeStamp, String url) throws Exception {
        String plain = "jsapi_ticket=" + jsticket + "&noncestr=" + nonceStr + "&timestamp=" + String.valueOf(timeStamp)
            + "&url=" + decodeUrl(url);
        try {
            MessageDigest sha1 = MessageDigest.getInstance("SHA-256");
            sha1.reset();
            sha1.update(plain.getBytes("UTF-8"));
            return byteToHex(sha1.digest());
        } catch (Exception e) {
            throw new Exception(e.getMessage());
        }
    }

    // 字节数组转化成十六进制字符串
    private static String byteToHex(final byte[] hash) {
        Formatter formatter = new Formatter();
        for (byte b : hash) {
            formatter.format("%02x", b);
        }
        String result = formatter.toString();
        formatter.close();
        return result;
    }

    /**
     * 因为ios端上传递的url是encode过的，android是原始的url。开发者使用的也是原始url,
     * 所以需要把参数进行一般urlDecode
     *
     * @param url
     * @return
     * @throws Exception
     */
    private static String decodeUrl(String url) throws Exception {
        URL urler = new URL(url);
        StringBuilder urlBuffer = new StringBuilder();
        urlBuffer.append(urler.getProtocol());
        urlBuffer.append(":");
        if (urler.getAuthority() != null && urler.getAuthority().length() > 0) {
            urlBuffer.append("//");
            urlBuffer.append(urler.getAuthority());
        }
        if (urler.getPath() != null) {
            urlBuffer.append(urler.getPath());
        }
        if (urler.getQuery() != null) {
            urlBuffer.append('?');
            urlBuffer.append(URLDecoder.decode(urler.getQuery(), "utf-8"));
        }
        return urlBuffer.toString();
    }

    public static String getRandomStr(int count) {
        String base = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
        Random random = new Random();
        StringBuffer sb = new StringBuffer();
        for (int i = 0; i < count; i++) {
            int number = random.nextInt(base.length());
            sb.append(base.charAt(number));
        }
        return sb.toString();
    }
}
```

## 步骤五：引入使用的JS

```
<script src="https://g.alicdn.com/dingding/dingtalk-jsapi/2.10.3/dingtalk.open.js"></script>
```

## 步骤六：JSAPI鉴权

**示例代码**：

> **[!IMPORTANT]**
>
> - **dd.config**中所有的参数必须直接来自服务端，不能直接在前端定义。
> - 一个页面只需要调用一次**dd.config**即可，重复调用会复用第一次调用的参数，单页应用（SPA）的**router**切换视为同一个页面。

```
dd.config({
    agentId: '', // 必填，微应用ID
    corpId: '',//必填，企业ID
    timeStamp: '', // 必填，生成签名的时间戳
    nonceStr: '', // 必填，自定义固定字符串。
    signature: '', // 必填，签名
    type:0/1,   //选填。0表示微应用的jsapi,1表示服务窗的jsapi；不填默认为0。该参数从dingtalk.js的0.8.3版本开始支持
    jsApiList : [
        'runtime.info',
        'biz.contact.choose',
        'device.notification.confirm',
        'device.notification.alert',
        'device.notification.prompt',
        'biz.ding.post',
        'biz.util.openLink',
    ] // 必填，需要使用的jsapi列表，注意：不要带dd。
});

dd.error(function (err) {
    alert('dd error: ' + JSON.stringify(err));
})//该方法必须带上，用来捕获鉴权出现的异常信息，否则不方便排查出现的问题
```

**参数说明**：

| **参数** | 类型 | 是否必填 | 说明 |
| --- | --- | --- | --- |
| agentId | String | 是 | 微应用ID。 |
| corpId | String | 是 | 企业的corpid。 |
| timeStamp | String | 是 | 生成签名的时间戳。 |
| nonceStr | String | 是 | 自定义固定字符串。 |
| signature | String | 是 | JSAPI签名，可以参考简易教程中的获取签名的示例代码。 |
| type | number | 否 | 如果是要调用服务窗的jsapi，请填1。 |
| jsApiList | Array | 是 | 需要调用的jsapi列表。 |

## 步骤七：调用JSAPI

完成鉴权后，便可以在dd.ready里调用JSAPI了。

代码示例：

```
dd.ready(function() {
  dd.biz.contact.choose({
    multiple: true, //是否多选：true多选 false单选； 默认true
    users: ['10001', '10002', ...], //默认选中的用户列表，员工userid；成功回调中应包含该信息
    corpId: 'dingb4ff1079f84f8d54', //企业id
    max: 10, //人数限制，当multiple为true才生效，可选范围1-1500
    onSuccess: function(data) {
    /* data结构
      [{
        "name": "张三", //姓名
        "avatar": "
http://g.alicdn.com/avatar/zhangsan.png
" //头像图片url，可能为空
        "emplId": '0573', //员工userid
       },
       ...
      ]
    */
    },
    onFail : function(err) {}
});
```

## 代码示例

- 企业内部应用：[JSAPI权限验证配置Demo-Java版本](https://github.com/open-dingtalk/openapi-demo-java)
- 第三方企业应用：[JSAPI权限验证配置Demo-PHP版本](https://github.com/open-dingtalk/isv_demo_php)
- 前端鉴权示例：[PHP版本Demo.js](https://github.com/open-dingtalk/isv_demo_php/blob/master/public/javascripts/demo.js)

## 常见问题

1. **dd.config错误说明，提示“jsapi ticket读取失败”**

   "jsapi ticket读取失败"， 这个错误是因为钉钉服务器没有成功读取到该企业的jsticket数据，原因可能为：

   1. corpid不一致：

      调用获取jsapi\_ticket接口，使用的access\_token对应的corpid和dd.config中传递的corpid不一致。
   2. 开发者缓存的jsticket时间过长导致jsticket已经过期。
2. **报错提示“无效的agent\_id”**

   需要检查appkey和agent\_id所对应的应用，是否为同一个应用，必须是同一个应用下的agent\_id和appkey才可以正常使用。

   查看以下两项的值是否属于同一个应用。例如appkey对应的应用的agent\_id为23456，b所对应的agent\_id为23457，agent\_id不同，可判断不是同一个应用，则会报错。

   1. 调用获取jsapi\_ticket接口，使用的access\_token，使用的appkey
   2. dd.config中传递的agent\_id
3. **免登报错52013，签名校验失败**

   1. 用户后端签名使用的url地址和前端访问地址需要严格一致，包括端口号。前端部分可以用alert显示出当前的location.href，后端部分请在签名的时候打印日志。
   2. 访问通过反向代理服务器、各种NAT等场景下容易出现这种问题，如http缺省的80端口，和显式增加80的不是同一个URL。
   3. 检查确认获取的jsapiticket是否正确或者过期。jsapiticket是否有效期内重复获取导致jsapiticket被覆盖。
