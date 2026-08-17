---
title: "开发 Windows 插件"
source_url: "https://open.dingtalk.com/document/development/create-a-windows-lug-in-project"
namespace: "development"
slug: "create-a-windows-lug-in-project"
group: "专属版客户端插件"
tab: " Windows 插件"
breadcrumb: "开发 Windows 插件"
doc_id: "hxb7KqxSJw"
updated_at: "2026-08-12 09:20:43"
---

> Source: https://open.dingtalk.com/document/development/create-a-windows-lug-in-project
> Path: 专属版客户端插件 /  Windows 插件 / 开发 Windows 插件
> Updated: 2026-08-12 09:20:43

# 开发 Windows 插件

你可以参考本文档操作步骤，快速完成开发Windows插件过程中的创建工程操作。

## **前提条件**

已经下载并安装了Visual C++ 或其他 C/C++ 开发工具。

![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1922376671/p1038963.png)

## **创建插件工程**

1. 打开已经下好的开发工具，创建一个动态链接库项目，点击**下一步**。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1922376671/p1038964.png)
2. 给项目命名，例如："DingPlugin"，然后点击**创建**。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1922376671/p1038965.png)

   创建成功后，如下所示：

   > **[!NOTE]**
   >
   > 如果开发环境安装正确，能够正确生成一个 DLL 二进制文件。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1922376671/p1038966.png)

### **编辑插件配置**

钉钉开放插件包括两个重要的组成部分：

- **插件配置**：一个 JSON 格式的配置文件，定义了插件的基本属性，注册相关事件通知，声明通知回调。
- **插件 DLL**：可被钉钉加载执行的动态链接库，实现并导出了配置文件中声明的接口。

目前可被注册的事件通知如下：

- 登录（login/logout）
- 连接状态变更（connectionStatusChanged）
- 发送文件（checkFile）

每种事件触发时，钉钉客户端会通知已注册的插件，并调用 pluginHostEvent 下对应事件内的方法。

### **配置模板**

插件配置文件的模板定义如下：

```
{
  "plugins": [
    {
      "pluginName": "plugin",
      "pluginId": "{54Bxxxx34A9}",
      "arch": "x64",
      "type": "dll_outprocess",
      "subjectName": "DingTalk Technology Co.,Ltd.",
      "issuerName": "DigiCert Trusted G4 Code Signing RSA4096 SHA384 2021 CA1",
      "platforms": {
        "Win": {
          "bin": "plugins\\plugin-sample\\plugin.dll"
        }
      },
      "supportCondition": {
        "Win": {
          "supportOSVersion": "6.1"
        }
      },
      "pluginHostEvent": {
        "login": {
          "actionParam": "ew0KICAxxxxpbiINCn0="
        }
      }
    }
  ]
}
```

配置文件中参数说明如下：

| **属性名称** | **属性含义及可选项** |
| --- | --- |
| pluginName | 插件名称，遵循变量名定义规范，可包含：英文字母 a-zA-Z、数字 0-9、\_- 下划线中划线等字符。 |
| pluginId | 唯一的 GUID，可以使用 GUID 生成工具生成。 |
| arch | 系统架构：x64，由于当前主流系统架构为 64 位，因此仅支持配置为：**x64。** |
| type | 插件类型：**dll\_outprocess**，运行于钉钉主进程之外，以 dll 的形式被加载。 |
| subjectName | 签名证书主题，用于核验 dll 文件是否被篡改。 |
| issuerName | 签名证书的颁发机构，用于核验 dll 文件是否被篡改。 |
| platforms | 指定插件路径，相对路径，必须以"**plugins\\**"开头**。** |
| supportCondition | 支持的系统版本，目前仅支持：Windows 7、Windows 10、Windows 11 三个版本。 |
| **pluginHostEvent** | 声明插件关注的事件、以及事件回调。 |

**pluginHostEvent**参数说明： **pluginHostEvent** 字段用于注册插件关心的事件，以及对应事件环节需要调用的接口，如下所示：

```
{
  "login": {
    "actionParam": "ew0KICAxxxxCn0="
  }
}
```

在上述 **login** 事件中，其 **actionParam** 参数就是经过 base64 编码的方法名称：

```
{
    "funcName":"OnAfterLogin"
}
```

**actionParam** 中的方法名称没有约束，只需满足如下函数定义即可。钉钉开放框架初始化时，将动态加载相关插件，并按照插件配置的描述从 DLL 的导出方法中查询相关接口，在注册的事件发生时，调用该方法。

```
typedef void (*SPI_CommonEventResult)(const char* event_name,
                                      int32_t event_name_length,
                                      const char* result,
                                      int32_t result_length);

typedef void (*SPI_CommonEventNotify)(const char* event_name,
                                      int32_t event_name_length,
                                      const char* event_param,
                                      int32_t event_param_length,
                                      SPI_CommonEventResult callback);
```

### **实现插件功能**

### **开发插件**

以登录事件为例，当钉钉完成登录认证后，会异步调用已注册的`SPI_CommonEventNotify`类型方法：`OnAfterLogin`。

```
typedef void (*SPI_CommonEventResult)(const char* event_name,
                                      int32_t event_name_length,
                                      const char* result,
                                      int32_t result_length);

typedef void (*SPI_CommonEventNotify)(const char* event_name,
                                      int32_t event_name_length,
                                      const char* event_param,
                                      int32_t event_param_length,
                                      SPI_CommonEventResult callback);
```

`SPI_CommonEventNotify`类型方法，参数说明如下：

| **参数** | **说明** |
| --- | --- |
| event\_name | 事件名称：login/logout，connectionStatusChanged，checkFile 等。 |
| event\_param | 事件相关的参数，以 JSON 字符串的形式定义，具体的 JSON 字段以该 SPI 的说明文档为准。 |
| callback | 回调函数地址，`SPI_CommonEventResult`类型。 |

其中 SPI 的第三个参数用于传递插件所需的数据，例如，登录事件传递部分账号信息，文件扫描事件传递文件路径等信息。

参数类型是字符串，格式为 JSON，例如：

```
// parameter for login 
{
  "corpId": "dinxxxx890",
  "dllPath": "/path/to/plugin.dll",
  "staffId": "1122",
  "userId": "7788"
}

// parameter for checkFile
{
  "file_path": "/path/to/file.ext",
  "receiver_id": "67890",
  "receiver_name": "Bob",
  "receiver_type": "single",
  "sender_id": "12345",
  "sender_name": "Alice",
  "task_id": "C97xxxx9A87FA4"
}
```

### **参考示例**

```
extern "C" __declspec(dllexport) int OnAfterLogin(const char* event_name,
                                                  int32_t name_length,
                                                  const char* event_param,
                                                  int32_t param_length,
                                                  SPI_CommonEventResult cb) {
  if (event_name && name_length > 0 && event_param && param_length > 0 && cb) {
    std::string event_name_str(event_name, name_length);
    std::string event_param_str(event_param, param_length);
    if (event_name_str.compare("lockStatusChanged") == 0) {
      if (event_param_str.compare("true") == 0) {
        return -2;
      }
    }

    CDevInfo di;
    di.Initialize(event_name_str, event_param_str, cb);
    di.GetDeviceInfo();
    return 0;
  }

  return -1;
}

extern "C" __declspec(dllexport) int OnBeforeLogout(const char* event_name,
                                                    int32_t name_length,
                                                    const char* event_param,
                                                    int32_t param_length,
                                                    SPI_CommonEventResult cb) {
  if (event_name && name_length > 0 && event_param && param_length > 0 && cb) {
    std::string event_name_str(event_name, name_length);
    std::string event_param_str(event_param, param_length);
    if (event_name_str.compare("login") == 0) {
      // do what you want to do after login dingding
      CDevInfo di;
      di.Initialize(event_name_str, event_param_str, cb);
      di.GetDeviceInfo();
      return 0;
    }
  }
  return -1;
}

extern "C" __declspec(dllexport) int OnCheckFile(const char* event_name,
                                                 int32_t name_length,
                                                 const char* event_param,
                                                 int32_t param_length,
                                                 SPI_CommonEventResult cb) {
  if (event_name && name_length > 0 && event_param && param_length > 0 && cb) {
    std::string event_name_str(event_name, name_length);
    std::string event_param_str(event_param, param_length);
    if (event_name_str.compare("checkFile") == 0) {
      CFileChecker checker;
      std::string check_result =
      "{\"check_result\":\"check_pass\",\"task_id\":\"{DA670ACxxxxF}\",}";
      checker.Parse(event_param_str);
      checker.CheckFile();
      checker.GetResult(check_result);

      cb(event_name, name_length, check_result.c_str(), check_result.length());
      return 0;
    }
  }
  return -1;
}
```

以下是完整的示例代码，你可点击链接直接下载即可：

[open-plugin-demo.zip](https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20251230/phkmbf/open-plugin-demo.zip)

## **上传插件并打包验证**

1. 登录钉钉管理后台，创建新的插件。

   > **[!NOTE]**
   >
   > 插件**code**和**BundleId**只允许使用数字、字母和 \_，必须以字母为开头且在本组织内唯一。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3422376671/p1039007.png)
2. 点击创建好的插件卡片，进入插件详情页。

   > **[!NOTE]**
   >
   > 可以创建新版本，或者点击一个版本的详情，进入版本编辑页面。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3422376671/p1039008.png)
3. 上传插件包和配置清单文件，插件包包括 dll、exe 等格式的可执行文件和运行时所需的资源。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3422376671/p1039010.png)
4. 上传插件包和配置清单文件成功后，完成发布插件和打包验证，如下图所示：

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3422376671/p1039011.png)

   打包验证，如下图所示：

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3422376671/p1039014.png)
5. 点击正式发布按钮，实现插件的正式打包，并在弹窗中点击**确定**按钮。

   > **[!NOTE]**
   >
   > 发布插件时，如果勾选了“发布后默认更新至【APP 打包-专属 APP 配置】”，则正式打包默认会包含该插件，否则需要在【APP 打包-专属 APP 配置】处手工选择。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3422376671/p1039015.png)
6. 打包成功后，可以在**钉钉专属版** > **App定制** > **App打包**中找到**专属功能配置**，手动选择打包的版本，如下图所示：

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3422376671/p1039016.png)
