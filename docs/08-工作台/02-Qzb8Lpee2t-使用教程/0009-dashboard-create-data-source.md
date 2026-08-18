---
title: "数据源"
source_url: "https://open.dingtalk.com/document/dingstart/dashboard-create-data-source"
namespace: "dingstart"
slug: "dashboard-create-data-source"
group: "工作台"
tab: "使用教程"
breadcrumb: "组件教程 > 全码组件 > 数据源"
doc_id: "IAYNJtakWu"
updated_at: "2026-08-18 09:12:01"
---

> Source: https://open.dingtalk.com/document/dingstart/dashboard-create-data-source
> Path: 工作台 / 使用教程 / 组件教程 > 全码组件 > 数据源
> Updated: 2026-08-18 09:12:01

# 数据源

## **创建数据源**

1. 登录[开发者后台](https://open-dev.dingtalk.com/#/plugin)。
2. 然后依次单击**定制服务** > **数据源管理** > **新建数据源**。

   ![数据源](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3233658161/p262557.png)
3. 在弹出的**新建数据源**页面中填写数据源基本信息。

   ![填写注册信息](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1026432161/p232907.png)

   **字段说明：**

   - **apiKey**：apiKey 是这个数据源的唯一标识，可自定义，由英文大小写组成，作为系统中对数据源的唯一识别码。

     例如：组件中需要用到一个数据源，那么在`config.json`的配置信息中需要用到 apiKey。

     ```
     // config.json 中的片段
     {
         ...
         "dataSources": [{
             "apiKey": "getChartData",
             "propName": "getChartDataApi",
         }],
         ...
     }
     ```
   - **apiSecret**：apiSecret 可以填写你和服务端同学约定的任意值，作为签名密钥，在获取用户身份时，供服务端接口识别这是来自钉钉的请求。
   - **参数**：请输入接口的所有参数名，多个参数名以英文逗号分隔，例如 param1，param2。

     无需设置 userid 和 corpid 参数，接口可以自动解析得到。
4. 数据源注册完成后，单击**测试**，测试数据源。

   测试数据源时，不需要填写参数 corpId 和 userid。服务端可以接收到 corpId 和 userid，服务端接收到的 corpId 为**当前企业的 corpId**，userid 为当前企业中**当前用户的 userid**。

   ![测试数据源](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1026432161/p232928.png)
5. 注册后的数据源，可以在服务商视角的设计器的数据源选择器中选到。也可以在 config.json 中的 **dataSources** 字段中使用。

   ![使用实践？](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1026432161/p232934.png)

   > **[!NOTE]**
   >
   > 在组件中使用选中的数据源，详见本文[在组件内发送请求](#c16ed8f1b10dr)介绍。

## **在组件内发送请求**

### **使用dataSources指定的数据源**

可以在 **dataSources** 属性中为组件指定配套的数据源，配置方式如下：

在 config.json 中，添加如下内容。

```
{
    dataSources: [{
        apiKey: 'getDataApi1',
        propName: 'getData1',
    }],
}
```

在组件代码中，添加如下内容。

```
// this.props.componentProps.getData1 是个 object，里面包含了 apiKey 以及其他开发者不需要关心的信息，
// 只要将这个 object 作为sdk.request的第一个参数传入即可
const data = await getSdk().request(this.props.componentProps.getData1, { param1: 'test', param2: 3 });
```

data 就是从服务端获取到的数据。

一个组件可以使用多个数据源，同一个数据源也可以被多个组件使用。

### **前后端接口联调**

将注册数据源时填写的信息，填入到 getSdk().request 的第三个参数中，即可访问后端接口。请确保参数中的信息与注册数据源时填入的信息一致。

```
const data = await getSdk().request(this.props.componentProps.gateWayApi, {
    param1: 'test',
    param2: 3,
}, {
    // sdk.request的第三个参数，输入注册数据源的信息
    url: 'https://xxx.dingtalk.com/api/test',
    apiKey: 'myApiKey',
    httpMethod: 'GET',
    // 参数名以英文逗号分隔，第二个参数中发送的请求参数，必须在数据源注册界面的"参数"字段注册过才能生效
    params: 'param1,param2',
    apiSecret: 'mytoken',
    // 可以mock userid 和 corpId，请注意大小写。userid 的 i 小写，corpId 的 I 大写。
    // 请确保mock的 userid 和 corpId 是真实存在的，以防服务端出错
    system: {
        userid: 'xxxx',
        corpId: 'xxxxx',
    },
})
```

> **[!NOTE]**
>
> 第三个参数只会在 IDE 中生效，不会在实际的工作台环境中生效。集成到工作台中时会采用第一个参数中的数据源信息发送请求。在正式提交代码时，可以不必删除第三个参数。

### **使用Setter选择的数据源**

在 config.json 的 **setters** 中，配置数据源选择的`setter`。

```
setters: [{
    // 这里定义了setter对应的props中的key，为"gateWayApi"，也可以取成任何想要的名字
    // 在组件中通过 this.props.componentProps.gateWayApi可以取到这个setter选中的值
    propName: 'gateWayApi',
    setterName: 'SelectApiSetter',
    props: {
      label: '数据源',
    }
}]
```

选中的数据源，会通过 **props** 传递给组件。

在组件中使用数据源选择 **Setter** 选中的数据源请求数据。

```
Component({
    async didMount() {
        getLifecycleSdk().didMount(this.props.componentName);
        // this.props.componentProps.gateWay 是个object类型，内部包含了apiKey等属性，可以直接传递给发送请求的SDK
        const data = await getSdk().request(this.props.componentProps.gateWayApi, {
            param1: 'test',
            param2: 3,
        });
    }
});
```

## **调试数据源请求**

在IDE或设计器中预览时，如果你需要通过断点进行调试，可使用以下两种方式实现：

- 方式一：使用 **getSdk().alert** 调试。

  > **[!NOTE]**
  >
  > `getSdk().alert()`只会在IDE或设计器中预览时才会生效，在线上不生效。

  ```
  getSdk().alert('标题', '内容');
  ```
- 方式二：使用 **getSdk().logger** 调试。

  `getSdk().logger`提供了 **log** 和 **error** 方法，在开发调试过程中，可实现与 **console.log**、**console.error** 相同的效果。

  你还可以通过`getSdk().logger`打印的信息配合调试工具可以实现远程真机调试的效果，如下：

  [](https://cloud.video.taobao.com/play/u/3691671841/p/1/e/6/t/1/327664641545.mp4)
