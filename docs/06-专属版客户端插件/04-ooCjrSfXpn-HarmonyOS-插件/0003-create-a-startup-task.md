---
title: "创建启动任务"
source_url: "https://open.dingtalk.com/document/development/create-a-startup-task"
namespace: "development"
slug: "create-a-startup-task"
group: "专属版客户端插件"
tab: "HarmonyOS 插件"
breadcrumb: "HarmonyOS 插件 > 创建启动任务"
doc_id: "XKB0qNqrEl"
updated_at: "2026-08-12 09:20:50"
---

> Source: https://open.dingtalk.com/document/development/create-a-startup-task
> Path: 专属版客户端插件 / HarmonyOS 插件 / HarmonyOS 插件 > 创建启动任务
> Updated: 2026-08-12 09:20:50

# 创建启动任务

## **功能描述**

当 App 冷启动时，框架允许插件插入自己的冷启动任务，该任务也是插件在钉钉平台中可执行的最早时机。开发者可以使用该类初始化自己的功能。

## **接口说明**

启动任务是基于扩展点开放，扩展点信息如下：

| **扩展点编码** | **接口类** |
| --- | --- |
| dingtalk\_bundles$startup\_tasks | EpStartupTask |

EpStartupTask关键接口：

| **名称** | **说明** |
| --- | --- |
| run() | 入参：   - context: **EpStartupContext**    - stage: AbilityStage   - context: common.ApplicationContext - callback: (success: boolean, msg?: string) => void    - 启动任务执行结束的回调。   - 启动任务会阻塞进入首页，因此**请务必在成功或失败后均调用 callback**，以此通知钉钉平台继续执行启动任务并释放相关资源。   返回值：无 |

> **[!NOTE]**
>
> - 启动任务会阻塞进入首页，因此**请务必在成功或失败后均调用 callback**，避免出现启动卡死现象。
> - 启动任务可能发生在账号未登录时（进入登录页面前触发调用），请做好登录态的逻辑处理。

## **示例代码**

```
export class ExampleStartupTask extends EpStartupTask {

  run(stContext: EpStartupContext, callback: (success: boolean, msg?: string) => void): void {
    console.info('testcase', 'init bundle sdk.')
    callback(true)
  }
}
```

添加扩展点实现配置：

- Index.ets 文件中添加导出类 ExampleStartupTask。
- dingtalk-bundle.json5 中添加扩展点配置

  ```
  "extensions": [
    {
      "class": "ExampleStartupTask",
      "bind": "dingtalk_bundles$startup_tasks"
    },
  ]
  ```
