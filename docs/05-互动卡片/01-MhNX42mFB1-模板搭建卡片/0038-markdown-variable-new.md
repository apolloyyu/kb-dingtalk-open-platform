---
title: "Markdown 变量"
source_url: "https://open.dingtalk.com/document/development/markdown-variable-new"
namespace: "development"
slug: "markdown-variable-new"
group: "互动卡片"
tab: "模板搭建卡片"
breadcrumb: "模板搭建器 > 变量协议 > Markdown 变量"
doc_id: "n7IImbaUOd"
updated_at: "2026-08-07 14:50:42"
---

> Source: https://open.dingtalk.com/document/development/markdown-variable-new
> Path: 互动卡片 / 模板搭建卡片 / 模板搭建器 > 变量协议 > Markdown 变量
> Updated: 2026-08-07 14:50:42

# Markdown 变量

本文介绍了`markdown`变量的语法规范以及一个示例来帮助你快速掌握`markdown`变量的使用。

## **概述**

卡片模板搭建编辑器中的`markdown`变量，结合「Markdown 内容」组件支持展示以下富文本内容：

- 多级标题与正文
- 灵活的文字样式

  - 加粗与斜体
  - 字体大小
  - 字体颜色
- 钉钉表情
- 段落与换行
- 链接
- 图片
- 分隔线
- 引用
- 无序列表
- 有序列表
- 表格
- 围栏代码块

## **语法介绍**

| **功能** | **语法** |
| --- | --- |
| 多级标题与正文 | 在单词或短语前面添加`#`和一个空格，`#`的数量代表了标题的级别。   ``` # 一级标题 ## 二级标题 ### 三级标题 #### 四级标题 ##### 五级标题 正文 ``` |
| 加粗 | 在单词或短语的前后各添加两个星号`**`。   ``` **加粗文本** ``` |
| 斜体 | 在单词或短语的前后各添加一个星号`*`。   ``` *斜体文本* ``` |
| 字体大小 | 使用`<font>`标签，传入`sizeToken`属性，属性值不要添加双引号。   ``` <font sizeToken=common_h3_text_style__font_size>三级标题字号</font> ```   **[!NOTE]**  支持的字体尺寸 Key 请参考下表。 |
| 字体颜色 | 使用`<font>`标签，传入`colorTokenV2`属性，属性值不要添加双引号。   ``` <font colorTokenV2=common_blue1_color>蓝色</font> ```   **[!NOTE]**  支持的字体颜色 Key 请参考下表。 |
| 钉钉表情 | 使用中括号包括表情文案。   ``` [元气满满] ```   **[!NOTE]**  钉钉表情文案请参考[钉钉表情列表](0041-list-of-dingtalk-expressions.md)。 |
| 换行 | 使用`<br>`标签将文本分隔。   ``` 第一行<br>第二行 ``` |
| 段落 | 使用空白行将一行或多行文本进行分隔。   ``` 第一段  第二段 ``` |
| 链接 | 链接文本放在中括号内，链接地址放在后面的括号中。   ``` [钉钉官网](https://www.dingtalk.com/) ``` |
| 图片 | 使用感叹号，然后在方括号增加替代文本，图片链接放在圆括号里。   ``` ![](https://static.dingtalk.com/media/lADPDetfXH_Pn3HNAbrNBDg_1080_442.jpg) ``` |
| 分隔线 | 在单独一行上使用连续三个星号`***`。   ``` *** ``` |
| 引用 | 在段落前添加一个`>`符号和一个空格即可创建块级引用。  块引用可以包含多个段落，为段落之间的空白行添加一个`>`符号。  添加多个`>`符号即可实现嵌套引用。   ``` > 引用第一段 > >> 嵌套引用第二段 > > 引用第三段 ``` |
| 无序列表 | 在每个列表项前面添加星号`*` 和一个空格。  缩进一个或者多个列表项可以创建嵌套列表。   ``` * 第一个列表项 	* 第一个嵌套列表项 	* 第二个嵌套列表项 * 第二个列表项 ``` |
| 有序列表 | 在每个列表项前添加数字并紧跟一个英文句点和一个空格。  数字不必按数学顺序排列，但是列表应当以数字`1`起始。  有序列表不支持嵌套。   ``` 1. 第一个列表项 2. 第二个列表项 3. 第三个列表项 ``` |
| 表格 | 使用`|`分隔每列，`|`与内容间需要有至少一个空格 。  可以通过在标题行中的连字符的左侧，右侧或两侧添加冒号`:`，将列中的文本对齐到左侧，右侧或中心。   ``` | 标题1 | 标题2 | 标题3 | | :- | :-: | -: | | 左对齐内容1 | 剧中内容1 | 右对齐内容1 | | 左对齐内容2 | 剧中内容2 | 右对齐内容2 | ``` |
| 围栏代码块 | 在代码块之前和之后的行上使用三个反引号，可在代码块之前的反引号旁边指定具体的语言类型。   ``` ```json {   "firstName": "John",   "lastName": "Smith",   "age": 25 } ``` ``` |

## **示例展示**

### **示例数据**

```
# 一级标题
## 二级标题
### 三级标题
#### 四级标题
##### 五级标题

正文 **加粗文本** *斜体文本* [钉钉官网链接](https://www.dingtalk.com/) [元气满满]

<font sizeToken=common_h3_text_style__font_size colorTokenV2=common_blue1_color>蓝色三级标题</font>

第一段第一行<br>第一段第二行

第二段第一行<br>第二段第二行

***

> 引用第一段
>
>> 嵌套引用第二段
>
> 引用第三段

1. 第一个有序列表项
    * 第一个无序列表项
        * 第一个嵌套无序列表项
        * 第二个嵌套无序列表项
    * 第二个无序列表项
2. 第二个有序列表项
3. 第三个有序列表项

| 表格标题1 | 表格标题2 | 表格标题3 |
| :- | :-: | -: |
| 左对齐内容1 | 剧中内容1 | 右对齐内容1 |
| 左对齐内容2 | 剧中内容2 | 右对齐内容2 |

```json
{
  "firstName": "John",
  "lastName": "Smith",
  "age": 25
}
```
```

### **示例效果**

![Markdown效果示例](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4485591171/p787156.jpg)

## **字体尺寸表**

| **尺寸 Key** | **桌面端** | **移动端** |
| --- | --- | --- |
| common\_hypertitle\_text\_style\_\_font\_size | 64px | 28px |
| common\_largetitle\_text\_style\_\_font\_size | 32px | 24px |
| common\_h1\_text\_style\_\_font\_size | 24px | 20px |
| common\_h2\_text\_style\_\_font\_size | 20px | 18px |
| common\_h3\_text\_style\_\_font\_size | 18px | 18px |
| common\_h4\_text\_style\_\_font\_size | 16px | 16px |
| common\_h5\_text\_style\_\_font\_size | 15px | 15px |
| common\_body\_text\_style\_\_font\_size | 14px | 17px |
| common\_footnote\_text\_style\_\_font\_size | 12px | 12px |

## **字体色值表**

| **色值 Key** | **Light** | **Dark** | **色值 Key** | **Light** | **Dark** |
| --- | --- | --- | --- | --- | --- |
| common\_yellow1\_color | ding | ding | common\_orange1\_color | ding | ding |
| common\_red1\_color | ding | ding | common\_pink1\_color | ding | ding |
| common\_purple1\_color | ding | ding | common\_blue1\_color | ding | ding |
| common\_water1\_color | ding | ding | common\_olive1\_color | ding | ding |
| common\_green1\_color | ding | ding | common\_level1\_base\_color | ding | ding |
| common\_level2\_base\_color | ding | ding | common\_level3\_base\_color | ding | ding |
| common\_level4\_base\_color | ding | ding | common\_gray1\_color | ding | ding |
| common\_gray2\_color | ding | ding | common\_gray3\_color | ding | ding |
| common\_gray4\_color | ding | ding | common\_gray5\_color | ding | ding |
| common\_gray6\_color | ding | ding |  | | |
