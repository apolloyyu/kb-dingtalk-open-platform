---
title: "监听WebSocket关闭"
source_url: "https://open.dingtalk.com/document/development/dd-onsocketclose"
namespace: "development"
slug: "dd-onsocketclose"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 网络 > WebSocket > 监听WebSocket关闭"
doc_id: "hbXnkstqkp"
updated_at: "2025-09-17 20:58:54"
---

> Source: https://open.dingtalk.com/document/development/dd-onsocketclose
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 网络 > WebSocket > 监听WebSocket关闭
> Updated: 2025-09-17 20:58:54

# 监听WebSocket关闭

调用**dd.onSocketClose**监听WebSocket关闭。

## **示例****代码**

```
onLoad() {
    // 注意： 回调方法的注册在整个小程序启动阶段只要做一次，调多次会有多次回调
    dd.onSocketClose((res) => {
      dd.alert({content: '连接已关闭！'});
      this.setData({
        sendMessageAbility: false,
        closeLinkAbility: false,
      });
    });
    // 注意： 回调方法的注册在整个小程序启动阶段只要做一次，调多次会有多次回调
    dd.onSocketOpen((res) => {
      dd.alert({content: '连接已打开！'});
      this.setData({
        sendMessageAbility: true,
        closeLinkAbility: true,
      });
    });

    dd.onSocketError(function(res){
      dd.alert('WebSocket 连接打开失败，请检查！' + res);
    });

    // 注意： 回调方法的注册在整个小程序启动阶段只要做一次，调多次会有多次回调
    dd.onSocketMessage((res) => {
      dd.alert({content: '收到数据！' + JSON.stringify(res)});
    });
  },

connect_start() {
    dd.connectSocket({
      url: '服务器地址', // 开发者服务器接口地址，必须是 wss 协议，且域名必须是后台配置的合法域名
      success: (res) => {
        dd.showToast({
          content: 'success', // 文字内容
        });
      },
      fail:()=>{
        dd.showToast({
          content: 'fail', // 文字内容
        });
      }
    });
  }
```
