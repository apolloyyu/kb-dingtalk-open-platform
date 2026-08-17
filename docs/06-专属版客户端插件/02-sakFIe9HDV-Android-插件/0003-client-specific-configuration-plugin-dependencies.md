---
title: "配置插件依赖项"
source_url: "https://open.dingtalk.com/document/development/client-specific-configuration-plugin-dependencies"
namespace: "development"
slug: "client-specific-configuration-plugin-dependencies"
group: "专属版客户端插件"
tab: "Android 插件"
breadcrumb: "Android 插件 > 配置插件依赖项"
doc_id: "94rVrAsr8v"
updated_at: "2026-08-12 09:20:46"
---

> Source: https://open.dingtalk.com/document/development/client-specific-configuration-plugin-dependencies
> Path: 专属版客户端插件 / Android 插件 / Android 插件 > 配置插件依赖项
> Updated: 2026-08-12 09:20:46

# 配置插件依赖项

本文重点用于指导开发者如何正确配置钉钉扩展插件（\*.deb）的依赖项，确保插件在发布后能够正常运行。

## 为什么配置依赖

钉钉插件以 DEB 格式发布，要求**所有运行时依赖必须内嵌或显式声明**，否则可能导致类缺失、方法找不到等运行时异常（Crash）。主要依赖包括：

> **[!NOTE]**
>
> 任何依赖信息的缺少都会造成插件功能异常。

- 依赖的功能 SDK （\*.aar/\*.jar文件）。
- 依赖的三方开源库 Maven 坐标地址信息。
- 额外的 Gradle 配置，比如 DataBinding 、 ButterKnife 的 Plugin 、注解处理器信息等。

## 插件文件介绍

钉钉平台定义了客户端插件的标准发布格式— **DEB 文件**。该文件本质是一个压缩文件，解压后内部关键结构：

| 文件 | 描述 |
| --- | --- |
| BundleManifest.xml | 描述了额外的三方 mvn 依赖列表、gradle 相关配置等。 |
| \*.aar | 依赖的 AAR 格式 SDK 文件。 |
| \*.jar | 依赖的 JAR 格式 SDK 文件。 |

因此，当插件出现功能异常时（比如类找不到的 Crash ），可先自行解压查看插件文件中是否缺少相关的依赖信息。

## **插件依赖配置**

以下配置均通过 `bundle.xml` 完成，并在编译阶段自动映射为标准的 `build.gradle` 脚本代码。

### **依赖的功能 SDK**

请将所需 SDK 打包为 AAR 或 JAR 文件，放置于 Bundle 工程的 `./libs` 目录下，插件打包时会将文件合并打包。

> **[!NOTE]**
>
> 不支持工程源码依赖、或自定义SDK本地目录。

### **其他 Gradle 相关依赖配置项**

#### **设置最小 SDK 版本： minSDKVersion**

bundle.xml 中添加如下：

```
  <minSdkVersion>21</minSdkVersion>
```

对应生成的 build.gradle 配置：

```
android {
  defaultConfig {
    minSdkVersion 21
  }
}
```

#### **添加自定义依赖：dependencies**

当你的 SDK 依赖了开源的三方库，或者自研的其他基础库已经发布到了公共仓库中，为了使用需要添加对应依赖，bundle.xml 中配置如下：

```
<dependencies>
    <implementation path="com.xiaomi:mipush_client:3.7.2@aar"/>
</dependencies>

<!-- 假如期望引入三方库后，能够排除部分依赖，请参数如下配置 -->
<dependencies>
    <implementation path="com.example:test_sdk:1.0.0@aar">
        <exclude path="com.demo.groupname:artifact_name"/>
    </implementation>
</dependencies>
```

对于引入特有的 mvn 仓库配置：

```
  <repositories>
    <maven>http://developer.huawei.com/repo/</maven>
  </repositories>
```

对应的 build.gradle 中的配置如下：

```
repositories {
    maven {
        url "http://developer.huawei.com/repo/"
    }
}
dependencies {
  implementation "com.xiaomi:mipush_client:3.7.2"
}
```

#### 添加注解解析器：kapt

同样，假如引入了特有的注解编译器，bundle.xml 添加如下，其中 argument 代表配置的可选参数：

```
  <dependencies>
    <kapt path="com.github.bumptech.glide:compiler:4.8.0">
      <argument name="test-arg">"test-value"</argument>
    </kapt>
  </dependencies>
```

#### 添加自己的 gradle 插件：apply-plugin

假如我们使用了类似 ButterKnife 的工具，需要在钉钉编译环境中添加 gralde 的插件，bundle.xml 可以如下

引入 classpath。

```
<classpaths>
    <classpath path="com.xxx.xxx:mygradlelib:1.1.0"/>
</classpaths>
```

bundle.xml 添加使用 plugin。

```
  <apply-plugins>
    <plugin id="my-plugin"/>
  </apply-plugins>
```

#### 添加自定义的packageOptions

假如你的 SDK 引入时会出现打包冲突时，可能需要配置 packageOptions ，主要支持 exclude 和 pickFirst 两种，可以在 bundle.xml 中添加如下片段：

```
<packaging-options>
    <exclude>META-INF/INDEX.LIST</exclude>
    <pickFirst>lib/arm64-v8a/libRSSupport.so</pickFirst>
</packaging-options
```

以上片段会被映射成如下 build.gradle 的脚本代码：

```
android {
    packagingOptions {
        exclude 'META-INF/INDEX.LIST'
        pickFirst 'lib/arm64-v8a/libRSSupport.so'
    }
}
```

#### 使用内置插件

bundle.xml 中的添加示例：

```
<used-plugins>
	<plugin id="插件ID" />
  <plugin id="插件ID" 参数1="参数值"  参数2="参数值"/>
</used-plugins>
```

钉钉支持的内置插件清单：

| **插件id** | **功能说明** | **示例** |
| --- | --- | --- |
| dataBinding | 开启DataBinding | ``` <used-plugins> 	<plugin id="dataBinding"/> </used-plugins> ``` |
| renderScript | 开启RenderScript | ``` <used-plugins>     <plugin id="renderScript"              targetApi="24"              supportModeEnabled="true" /> </used-plugins> ``` |
