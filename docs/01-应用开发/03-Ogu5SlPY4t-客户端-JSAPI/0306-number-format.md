---
title: "数字格式"
source_url: "https://open.dingtalk.com/document/development/number-format"
namespace: "development"
slug: "number-format"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "酷应用 > 文档酷应用 > 数字格式"
doc_id: "doc_fecdd52b25d14e07"
updated_at: "2026-08-28 10:27:14"
---

> Source: https://open.dingtalk.com/document/development/number-format
> Path: 应用开发 / 客户端 JSAPI / 酷应用 > 文档酷应用 > 数字格式
> Updated: 2026-08-28 10:27:14

# 数字格式

## 自定义数字格式

range.setNumberFormat(string)

允许自定义一些数字格式，常用的

- **yy：**表示xx年。
- **yyyy：**表示xxxx年。
- **m：**表示x月。
- **mm：**表示xx月。
- **d：**表示x日。
- **dd：**表示xx日。
- **ddd：**表示周几。
- **dddd：**表示星期几。
- **h：**表示x时。
- **hh：**表示xx时
- **hm：**表示xx分。
- **"{string}"：**表示常量。

## 示例代码

```
const range = Workbook.getRange("A1");
range.setValue(45000);
range.setNumberFormat('yyyy-mm-dd');
```

上述代码会在A1单元格中输入内容，之后通过设置数字格式将其设为2023-03-15 。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4304887871/p1097854.png)

### 增加小数位

range.increaseDecimal()

此API功能和下图所示功能一致。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4304887871/p1097855.png)

### 减少小数位

range.decreaseDecimal()

此API功能和下图所示功能一致。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4304887871/p1097856.png)
