---
title: "小程序"
source_url: "https://open.dingtalk.com/document/development/small-program"
namespace: "development"
slug: "small-program"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "常见问题 > 小程序"
doc_id: "yURcCE2oIc"
updated_at: "2026-07-22 16:25:12"
---

> Source: https://open.dingtalk.com/document/development/small-program
> Path: 应用开发 / 客户端JSAPI / 常见问题 > 小程序
> Updated: 2026-07-22 16:25:12

# 小程序

本文介绍了小程序的常见问题。

- **小程序调用客户端 API 出现** `"is not function"`**报错？**

  答：小程序IDE工具无法及时同步最新方法，若在小程序中使用客户端 API 出现`"is not function"`，则需完成以下操作步骤：

  1. 钉钉小程序项目内创建`node_modules`文件夹。
  2. 在创建的`node_modules`文件夹目录下，安装客户端 SDK 。

     ```
     npm install dingtalk-jsapi --save
     ```
  3. 初始化，在钉钉小程序app.js文件头部，添加以下代码。

     ```
     import 'dingtalk-jsapi/entry/mobile';
     ```
  4. 添加完成后，就可以在小程序js文件中定义并使用了，例如：

     1. 在小程序index.axml文件，定义按钮触发方法：

        ```
        <view>
          <button size="default" type="primary" onTap="Test">选择部门和人</button>
        </view>
        ```
     2. 小程序index.js文件，引入方法并使用：

        ```
        import complexPicker from 'dingtalk-jsapi/api/biz/contact/complexPicker';
        Page({
          data: {
          },
          onLoad(query) {
          },
          Test(){
            complexPicker({
              title:"测试标题",            //标题
              corpId:"ding027fxxxxx",              //企业的corpId
              multiple:true,            //是否多选
              maxUsers:1000,            //最大可选人数
              pickedUsers:[],            //已选用户
              pickedDepartments:[],          //已选部门
              disabledUsers:[],            //不可选用户
              disabledDepartments:[],        //不可选部门
              requiredUsers:[],            //必选用户（不可取消选中状态）
              requiredDepartments:[],        //必选部门（不可取消选中状态）
              permissionType:"GLOBAL",          //可添加权限校验，选人权限，目前只有GLOBAL这个参数
              responseUserOnly:false,        //返回人，或者返回人和部门
              startWithDepartmentId:0 ,   //仅支持0和-1
              onSuccess: function(result) {
                  console.log(JSON.stringify(result))
              },
             onFail : function(err) {
              console.log(JSON.stringify(err))
             }
            })
          },
        });
        ```
- **第三方企业应用在IDE模拟器运行正常，预览及真机调试时显示空白页面**

  答：出现上述问题的可能原因为企业未授权开通应用导致，需要确保对应企业授权开通企业三方应用来保证预览及真机调试正常。
- **小程序使用web-view组件内嵌H5页面打开白屏**

  答：[web-view](0507-mini-app-web-view.md)内嵌H5页面在手机端打开页面显示白屏，可尝试在web-view上添加 enhanced="{{true}}"，示例如下：<web-view enhanced="{{true}}" src="{{url}}" ></web-view>

  > **[!IMPORTANT]**
  >
  > 钉钉小程序web-view中内嵌H5页面的场景下，调用JsApi需添加enhanced="{{true}}"标记。
- **调用dd.httpRequest报错{ "error" : 12,"errorMsg": "socket is closed"}**

  答：调用[发网络请求](0517-send-network-requests.md)接口出现上述错误时，可尝试在入参中增加 impl: 'dt' 。
- **在使用播放组件时出现h5内容同层播放，未固定为最高层**

  答：使用[video 视频播放器](0504-mini-app-video-player-1.md)出现上述问题时，可尝试在video标签添加raw-controls="true"来解决层级问题。
- **获取免登授权码报错{error: 1002, errorMessage: 企业无此微应用}**

  答：[免登授权码](0515-mini-program-free-login.md)出现上述错误时，请确认选择的企业下是否已授权开通该第三方企业应用。
- **使用video视频播放器无法获取视频总时长**

  答：使用[video 视频播放器](0504-mini-app-video-player-1.md)时，若要获取视频总时长需要增加native video属性，如<video enableNative="{{true}}">
- **小程序在真机上运行报错“...无权跨域...”**

  答：可能原因为未设置安全域名，请前往[开发者后台](https://open-dev.dingtalk.com/#/) **> 找到应用 > 安全中心 > 设置安全域名**，设置安全域名后，需在IDE重新打包上传版本并发布。
- **调用dd.enableLeaveConfirm未弹窗**

  答：[离开二次确认配置](0561-dd-enableleaveconfirm.md)未弹窗时，请确认当前页面是否有返回按钮或者关闭按钮，若无则无法弹窗。

  > **[!IMPORTANT]**
  >
  > 当前页面指调用dd.enableLeaveConfirm时小程序栈顶页面，与该 JSAPI 在哪个 page 实例调用无关。
- **调用onShareAppMessage分享，打开分享链接提示‘无效参数’**

  答：请检查小程序有无发布线上版本，发布线上版本后才可以正常跳转。
- **小程序如何用类似于echarts的图表插件**

  答：可参考使用[支付宝图表](https://f2.antv.antgroup.com/)。
- **dd.setTabBarBadge提示‘dd.setTabBarBadge is not a function’**

  答：[添加tabBar文本](0547-dd-settabbarbadge.md)出现上述错误时，请确认入参中text字段的类型是否为字符串类型。
- **调用jsapi报错"Not in DingTalk PC webview"**

  答：jsapi需在钉钉客户端容器环境中运行，否则调用jsapi会报错“Not in DingTalk PC webview”。
