---
title: "控件库"
source_url: "https://open.dingtalk.com/document/connection/basic-controls"
namespace: "connection"
slug: "basic-controls"
group: "连接平台"
tab: "连接器中心"
breadcrumb: "官方连接器 > 使用教程 > OA审批 > 参考 > 控件库"
doc_id: "7zFmVwCdqA"
updated_at: "2026-11-19 11:40:21"
---

> Source: https://open.dingtalk.com/document/connection/basic-controls
> Path: 连接平台 / 连接器中心 / 官方连接器 > 使用教程 > OA审批 > 参考 > 控件库
> Updated: 2026-11-19 11:40:21

# 控件库

本文介绍了OA审批常用的基础控件和增强控件。

## **基础控件**

### **单行输入框**

填写以下控件的值获取数据，数据格式为：String类型。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2789546761/p561993.png)

获取的数据填充到以下控件，数据格式为：String类型。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1789546761/p561996.png)

### **多行输入框**

填写以下控件的值获取数据，数据格式为：String类型。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2789546761/p561999.png)

获取的数据填充到以下控件，数据格式为：String类型。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2789546761/p562000.png)

### **数字输入框**

填写以下控件的值获取数据，数据格式为：number类型。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2789546761/p562010.png)

获取的数据填充到以下控件，数据格式为：number类型或只包含数字的String类型，如（123或“123”）。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2789546761/p562015.png)

### **单选框**

> **[!IMPORTANT]**
>
> 选项最多200项，每项最多50个字。

#### **连接平台**

单选框作为输入到连接器时，填写以下控件的值获取数据中入参设置，例如：

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2789546761/p562072.png)

单选框作为连接器输出时，获取的数据填充到以下控件时出参设置，例如：

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2789546761/p562075.png)

#### **OA审批管理后台**

填写以下控件的值获取数据：

- 「单选框.值」数据格式为：String类型。
- 「单选框.选项列表.值列表」数据格式为：array类型。
- 「单选框.选项列表.ID列表」数据格式为：array类型。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1789546761/p562029.png)

> **[!NOTE]**
>
> - 「单选框.值」为展示值。
> - 「单选框.选项列表.值列表」为下拉框选项列表。
> - 「单选框.选项列表.ID列表」为对应选项的ID列表。
>
> 根据实际需求选择所需值获取，并不是所有值必填。

获取的数据填充到以下控件：

- 「单选框.值」数据格式为：String类型。
- 「单选框.选项列表.值列表」数据格式为：array类型。
- 「单选框.选项列表.ID列表」数据格式为：array类型。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2789546761/p562056.png)

> **[!NOTE]**
>
> 根据实际需求选择所需值填充，并不是所有值必填。

### **多选框**

> **[!IMPORTANT]**
>
> 选项最多200项，每项最多50个字。

#### **连接平台**

多选框内容作为输入到连接器时，填写以下控件的值获取数据中入参设置，例如：

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2789546761/p562107.png)

多选框内容作为连接器输出时，获取的数据填充到以下控件中出参设置，例如：

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1789546761/p562117.png)

#### **OA审批管理后台**

填写以下控件的值获取数据：

- 「多选框.值」数据格式为：Array<String>类型。
- 「多选框.选项列表.值列表」数据格式为：array类型。
- 「多选框.选项列表.ID列表」数据格式为：array类型。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1789546761/p562095.png)

> **[!NOTE]**
>
> - 「多选框.值」为展示值。
> - 「多选框.选项列表.值列表」为下拉框选项列表。
> - 「多选框.选项列表.ID列表」为对应选项的ID列表。
>
> 根据实际需求选择所需值获取，并不是所有值必填。

获取的数据填充到以下控件：

- 「多选框.值」数据格式为：Array<String>类型。
- 「多选框.选项列表.值列表」数据格式为：array类型。
- 「多选框.选项列表.ID列表」数据格式为：array类型。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1789546761/p562105.png)

> **[!NOTE]**
>
> 根据实际需求选择所需值填充，并不是所有值必填。

### **日期**

填写以下控件的值获取数据，数据格式为：String类型。

> **[!NOTE]**
>
> - 如果日期控件类型选择为：「年-月-日」则参数数据格式为「2023-02-02」。
> - 如果日期控件类型选择为「年-月-日 时：分」则参数为「2023-02-02 11:11」。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2789546761/p562142.png)

获取的数据填充到以下控件，数据格式为：String类型。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2789546761/p562153.png)

### **日期区间**

#### **连接平台**

日期区间作为输入到连接器时，填写以下控件的值获取数据中入参设置，例如：

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2789546761/p562190.png)

日期区间作为连接器输出时，获取的数据填充到以下控件中出参设置，例如：

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2789546761/p562191.png)

#### **OA审批管理后台**

填写以下控件的值获取数据，数据格式为：Array<String, String>或Array<String, String, number>类型。

> **[!NOTE]**
>
> - 如果日期区间控件类型设置为「年-月-日」，则参数数据格式为「2023-02-02」。
> - 如果日期控件类型选择为「年-月-日 时：分」，则参数为「2023-02-02 11:11」。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1789546761/p562172.png)

获取的数据填充到以下控件，数据格式为：Array<String, String>或Array<String, String, number>类型。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1467256761/p562639.png)

### **身份证**

填写以下控件的值获取数据，数据格式为：String类型。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1789546761/p562267.png)

获取的数据填充到以下控件，数据格式为：String类型。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2789546761/p562272.png)

### **电话**

填写以下控件的值获取数据，数据格式为：String类型。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1789546761/p562275.png)

获取的数据填充到以下控件，数据格式为：String类型。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2789546761/p562277.png)

## **增强控件**

### **图片**

填写以下控件的值获取数据，数据格式为：String类型（图片链接）。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1789546761/p562279.png)

获取的数据填充到以下控件，数据格式为：String类型（图片链接）。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2789546761/p562285.png)

### **明细/表格**

> **[!IMPORTANT]**
>
> 1. 明细内组件，不支持再嵌套明细 。
> 2. 明细中不支持多成员控件：如 多选项控件 / 图片控件(实际是图片列表), 放入明细中, 解析和展示都不支持。
> 3. 多个值变动, 触发更新/回填同一明细的不同字段，不支持，建议规避。

#### **连接平台**

**明细/表格中嵌套输入框**作为输入到连接器时，填写以下控件的值获取数据中入参设置，例如：

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2789546761/p562302.png)

**明细/表格中嵌套输入框**作为连接器输出时，获取的数据填充到以下控件中出参设置，例如：

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1789546761/p562304.png)

**明细/表格中嵌套单选框**作为连接器输出时，获取的数据填充到以下控件中出参设置，例如：

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2789546761/p562326.png)

#### **OA审批管理后台**

填写以下控件的值获取数据，数据格式为：array类型。

例如：明细/表格中嵌套输入框，作为填写以下控件的值获取数据。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2789546761/p562294.png)

获取的数据填充到以下控件，数据格式为：array类型。

例如：明细/表格中嵌套输入框，作为获取的数据填充到以下控件。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2789546761/p562299.png)

例如：明细/表格中嵌套单选框，作为获取的数据填充到以下控件。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2789546761/p562322.png)

### **金额**

填写以下控件的值获取数据，数据格式为：String类型（数字，例："100"）。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1789546761/p562334.png)

获取的数据填充到以下控件，数据格式为：String类型（数字，例："100"）。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2789546761/p562341.png)

### **附件**

填写以下控件的值获取数据，数据格式为：String类型（钉盘链接）。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2789546761/p562344.png)

> **[!NOTE]**
>
> 获取数据的内容包含spaceId、fileName、fileSize、fileType、fileId等信息，根据所得信息调用钉盘服务端API，详情参考[获取文件下载信息](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0674-obtains-the-download-information-about-a-file.md)。

获取的数据填充到控件，审批不支持解析。

### **外部联系人**

填写以下控件的值获取数据，数据格式为：String类型。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1789546761/p562352.png)

获取的数据填充到以下控件，数据格式为：String类型。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1789546761/p562368.png)

### **联系人**

填写以下控件的值获取数据，数据格式为：String类型。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1789546761/p562371.png)

获取的数据填充到以下控件，数据格式为：String类型。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2789546761/p562374.png)

### **部门**

填写以下控件的值获取数据：

- 部门值数据格式为：String类型。
- 部门ID数据格式为：number类型。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2789546761/p562379.png)

获取的数据填充到以下控件：

- 部门值数据格式为：String类型。
- 部门ID数据格式为：number类型。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2789546761/p562381.png)

### **地点**

填写以下控件的值获取数据：

- 定位位置为：String类型。
- 定位时间为：String类型。
- 经度为：number类型。
- 纬度为：number类型。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1789546761/p562385.png)

获取的数据填充到以下控件：

- 定位位置为：String类型。
- 定位时间为：String类型。
- 经度为：number类型。
- 纬度为：number类型。

> **[!NOTE]**
>
> 要同时填充定位时间、位置、经度和纬度才可以成功渲染地点控件。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2789546761/p562391.png)

### **省市区**

填写以下控件的值获取数据，地址、省、市、区的数据格式为：String类型。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2789546761/p562429.png)

获取的数据填充到以下控件，地址、省、市、区、省ID、市ID、区ID的数据格式为：String类型。

> **[!NOTE]**
>
> 要同时填充地址、省、市、区、省ID、市ID、区ID才可以成功渲染省市区控件。省ID、市ID、区ID参考中国省市县地区代码一览表，6位版编码表。例如：浙江省（330000）、杭州市（330100）、余杭区（330110）。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1789546761/p562431.png)

### **流水号**

> **[!NOTE]**
>
> 流水号是表单提交后自动生成的，因此只有在**流程设计**中可以获取到流水号值。

填写以下控件的值获取数据，数据格式为：String类型。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2789546761/p562442.png)
