---
title: "数据源配置"
source_url: "https://open.dingtalk.com/document/aipass/data-source-configuration"
namespace: "aipass"
slug: "data-source-configuration"
group: "数据资产"
tab: "宜数（智能问数）"
breadcrumb: "互动大屏 > 数据源配置"
doc_id: "yFV62Bh4Wv"
updated_at: "2026-08-14 09:26:53"
---

> Source: https://open.dingtalk.com/document/aipass/data-source-configuration
> Path: 数据资产 / 宜数（智能问数） / 互动大屏 > 数据源配置
> Updated: 2026-08-14 09:26:53

# 数据源配置

## **概述**

互动大屏兼容多种数据源，包括静态数据、CSV文件、全局变量数据、API接口以及数据资产平台，旨在通过钉钉的数据可视化功能，为用户提供强大而灵活的数据展示支持。

> **[!NOTE]**
>
> 当前的版本属于**高级版**。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8973954371/p890866.png)

## **场景一：基于“钉钉官方数据”搭建大屏**

### **使用效果**

使用数据资产平台通道快速获取钉钉最近 30 天成功发起的语音会议平均参会人数。

![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3145754371/p889198.png)

### **搭建流程**

1. 在大屏中选中数据组件，此处以数字翻牌器为例。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9770954371/p890598.png)
2. 在右侧面板中选择数据源 tab，数据源类型选择数据资产平台。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9770954371/p890600.png)
3. 选择数据资产平台中想要查询的数据和指标。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9770954371/p890601.png)
4. 确认保存后即可创建对应数据服务，完成数据获取。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9770954371/p890602.png)
5. 配置好数据映射。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9770954371/p890603.png)
6. 即可在组件上展示对应的指标数值。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9770954371/p890604.png)

## **场景 2：基于“自有数据”搭建大屏**

### **使用效果**

使用资产平台自有数据，快速在智能大屏上展示。

![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3145754371/p889204.png)

### **搭建流程**

1. 通过Excel 方式上传地理位置数据。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1387946871/p890605.png)
2. 通过数据准备加工数据，详见[数据工厂](0014-overview-1.md)。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1387946871/p890608.png)
3. 在大屏中选择对应的地图组件。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9770954371/p890611.png)
4. 选择对应的子组件。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9770954371/p890613.png)
5. 配置资产平台的数据源。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9770954371/p890614.png)
6. 选择指标。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9770954371/p890615.png)
7. 配置映射。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9770954371/p890616.png)
8. 效果展示。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9770954371/p890617.png)
