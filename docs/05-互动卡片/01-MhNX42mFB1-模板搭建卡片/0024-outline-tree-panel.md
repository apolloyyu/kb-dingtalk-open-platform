---
title: "面板介绍"
source_url: "https://open.dingtalk.com/document/development/outline-tree-panel"
namespace: "development"
slug: "outline-tree-panel"
group: "互动卡片"
tab: "模板搭建卡片"
breadcrumb: "模板搭建器 > 面板介绍"
doc_id: "FvezLxBVdD"
updated_at: "2026-08-05 09:10:12"
---

> Source: https://open.dingtalk.com/document/development/outline-tree-panel
> Path: 互动卡片 / 模板搭建卡片 / 模板搭建器 > 面板介绍
> Updated: 2026-08-05 09:10:12

# 面板介绍

## **大纲树面板**

通过大纲树面板，可以清晰查看当前卡片模板中所有组件的**层级结构**，同时支持快速选中组件并拖拽进行**布局调整或重命名**等操作。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6046989661/p514982.png)

- **组件层级结构**：大纲树与模拟器中的组件一一对应，选中时互相高亮。例如「图片」组件的层级为：**卡片 > 布局容器 > 布局 > 图片**

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6046989661/p513847.png)
- **调整布局**：单击组件可在模拟器中高亮对应区域；长按组件可拖拽调整布局。

  ![drag_component_tree](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6262293761/p536847.gif)
- **组件重命名**：双击组件名称即可进入编辑状态进行重命名，便于在复杂大纲树中快速定位组件。

  ![com_name_edit](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7262293761/p536813.gif)

## 组件库面板

卡片模板由各种组件构成。组件库面板罗列了搭建器提供的所有组件。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7556989661/p514974.png)

### **组件分类**

以组件的用途作为区分，组件库中的组件共分为以下几类：

- **头部内容**：用来修饰卡片头部的组件
- **内容元素**：用来展示卡片中的基础信息，如文本、公告栏等
- **图片、视频**：用来展示图片、视频相关的组件
- **容器**：用于高级功能如循环渲染等功能的容器组件
- **计时组件**：与计时相关的组件，如计时与倒计时
- **进度条组件**：用来展示进度的组件，如条状、块状进度条等
- **操作区组件**：与用户操作相关的组件，如选择框、按钮等
- **布局**：普通的布局组件，如 1:1、1:2、固定宽度布局等
- **堆叠布局**：与普通布局不同，堆叠布局的子内容可以堆叠，常见的有左上、坐下等方位的堆叠布局

### **使用组件**

通过长按**拖拽**的方式将组件拖入模拟器画布的目标位置。

![drag_comopnent](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1882293761/p530430.gif)

### **组件文档**

鼠标悬浮在组件上时会出现「帮助」图标，点击后打开该组件的介绍文档，包含**使用说明**及**演示**等信息。

> **[!NOTE]**
>
> 组件文档通过弹窗方式打开，该弹窗没有遮罩且支持**长按弹窗标题**进行拖拽，实现边看文档边搭建。

![drag_doc](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0882293761/p530429.gif)

在组件文档的演示示例中停留时，会出现「添加到卡片」按钮，点击后可在当前模板中添加示例组件，帮助快速上手。除卡片头部等特殊组件添加在模板顶部外，大部分组件默认添加在模板底部。

> **[!NOTE]**
>
> 除少部分特殊组件如卡片头部等是添加在卡片模板顶部外，大部分组件都是直接添加在卡片模板底部。

![add_demo](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1882293761/p530431.gif)

鼠标停留在属性标题上时，会以气泡提示显示该属性的描述。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2122985871/p523364.png)

### **基础与区块组件的区别**

- 基础组件：原子化组件，可自由配置样式和内容。
- 区块组件：由基础组件组合而成，样式固定，仅可修改内容，更多信息可查看[区块组件库面板](#86b199e091orw)介绍。

> **[!NOTE]**
>
> 两者可混合使用，但区块组件不能嵌套在布局组件中（循环渲染容器除外）。

| **对比项** | **基础组件** | **区块组件** |
| --- | --- | --- |
| **配置性** | 可配置内容和样式 | 统一 UI 规范，仅可配置内容 |
| **是否原子化** | 是 | 否，包含复合组件 |
| **响应式布局** | 不支持 | 复合区块组件支持 |
| **布局嵌套** | 可与其他布局嵌套 | 只能作为卡片顶层的组件 |

## 区块组件库面板

区块组件库面板罗列了所有区块组件，同样支持拖拽到模拟器画布中使用。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3882293761/p515000.png)

### **基础与区块组件的区别**

- 基础组件：原子化组件，可自由配置样式和内容，更多信息可查看[组件库面板](#80c83c00913on)介绍。
- 区块组件：由基础组件组合而成，样式固定，仅可修改内容。

> **[!NOTE]**
>
> 两者可混合使用，但区块组件不能嵌套在布局组件中（循环渲染容器除外）。

| **对比项** | **基础组件** | **区块组件** |
| --- | --- | --- |
| **配置性** | 可配置内容和样式 | 统一 UI 规范，仅可配置内容 |
| **是否原子化** | 是 | 否，包含复合组件 |
| **响应式布局** | 不支持 | 复合区块组件支持 |
| **布局嵌套** | 可与其他布局嵌套 | 只能作为卡片顶层的组件 |

### **复合组件的响应式功能**

复合组件由文本和另一部分组合而成，排列方式可能是左右或上下，在特定条件下，排列方式会自动切换，即响应式布局。

以「双列文本」组件为例，帮助你更轻松地理解响应式。

| **条件（满足其一）** | **PC 端且卡片宽度 > 440px** | **移动端，或 PC 端且卡片宽度 < 440px** |
| --- | --- | --- |
| **排列方式** | 左右排列 | 上下排列 |
| **示例** | image | image |

开启响应式需在创建卡片时为公有数据添加 `config` 对象，并设置 `config.autoLayout` 为 `true`。下面分别介绍[卡片平台创建卡片实例](0003-create-a-card-instance-from-the-card-platform.md)和[开放接口创建卡片实例](0004-open-the-interface-to-create-a-card-instance.md)两种方式如何配置：

- **方式一：通过卡片平台创建时**

  1. 为了在创建实例时能为`autoLayout`配置值，我们需要定义该变量，如图，需要作为`config`对象的一个字段。

     ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3882293761/p549913.png)
  2. 搭建完成后「发布」卡片，进入卡片实例管理页面。![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2122985871/p538065.png)
  3. 为`config`配置静态数据，如图所示，其中`autoLayout`为`true`。![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3882293761/p538066.png)
  4. 实现[卡片平台投放卡片实例](0005-card-delivery-instance-for-card-platform.md)即可。
- **方式二：通过开放接口创建时**

  由于 `config` 的值是非字符串类型，需在 `cardParamMap.sys_full_json_obj` 字段中添加相关变量：

  ```
  {
    "cardData" : {
      "cardParamMap" : {
        "sys_full_json_obj" : "{\"config\":{\"autoLayout\":true}}"
      }
    },
  }
  ```

  [开放接口投放卡片实例](0006-open-interface-card-delivery-instance.md)后即可看到响应式效果。

  > **[!NOTE]**
  >
  > 此处使用了「文本+下拉框」和「文本+按钮」复合组件进行演示。

  ![autolayout](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3882293761/p538071.gif)

## **预设模板面板**

针对不同场域（如消息卡片）下的常见场景，搭建器提供了开箱即用的预设模板，如审批模板、日志模板、表单模板等。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3096989661/p515185.png)

将鼠标移至想要使用的模板上，即可看见「使用」和「预览」按钮。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2096989661/p515186.png)

点击「使用」即可使用当前预设模板的所有内容

> **[!IMPORTANT]**
>
> 使用预设模板将会**覆盖您当前的卡片模板**，请知晓后使用（点击「使用」时会有弹窗提示）

## **数据源面板**

数据源面板用于管理卡片模板的变量及变量的模拟数据，数据源包含了多种变量，这些变量对于卡片而言即是一个个的占位符，通过占位符即可让卡片实现内容的动态变化。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2122985871/p515205.png)

### **新增变量**

1. 如图所示，点击「新增」并在下拉框中选择新增的变量类型（此处以大部分场景下使用的**普通变量**为例，关于普通变量、表达式变量、新增本地变量的区别，参见文档[变量类型](0027-variable-type.md)）。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4018797661/p515293.png)
2. 在弹出的变量管理面板中，点击「新增变量」按钮新增变量。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2122985871/p515319.png)
3. 完善新增变量的**变量名**、[变量类型](0027-variable-type.md)、**变量描述、是否是私有变量**等信息后点击保存即可添加。

   > **[!NOTE]**
   >
   > 变量勾选了私有之后，表示当前变量支持私有变量模式，此时卡片在渲染时将优先从卡片的私有数据上获取对应的变量数据来进行展示。如果私有数据没有值，则使用公有数据进行展示。通过私有数据的模式，可以做到卡片内容千人千面。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2122985871/p516105.png)

### **查看变量**

在数据源面板中会展示所有的变量列表。鼠标单击某一个变量即可打开变量的基础信息，如变量名、变量类型、是否私有是私有变量、描述等信息：

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5286989661/p517453.png)

### **编辑变量**

变量的编辑包含变量的排序、复制、删除等功能，点击数据源面板中对应数据源的「编辑」按钮即可打开变量编辑面板。

打开的变量编辑面板与上文添加变量时打开的变量编辑面板是一样的，因此与「信息完善」和「新增变量」相关的功能不再进行赘述。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2122985871/p516100.png)

> **[!NOTE]**
>
> 不同的变量类型（普通变量、表达式变量等）有属于自己的「编辑」按钮以及变量编辑面板，不会互相影响。如图所示，这是表达式变量的编辑面板：
>
> ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2122985871/p516101.png)

下面将一一介绍变量编辑的相关功能。

#### **变量排序**

通过长按对应变量前面的拖动图标，即可对变量进行上、下顺序的调整。

![drag_variable](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8882293761/p532232.gif)

#### **变量复制**

变量的复制可以**快速地在同级目录下创建一个与目标配置相同的变量**，用好变量的复制有助于提高你的开发效率。

如图所示，高亮区域的图标即为变量复制的按钮，点击后即可在同级目录下对变量进行复制。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2122985871/p516106.png)

如下图所示，对名为`appNamePage`的变量进行了复制后可以看到同级目录下有新的变量名为`appNamePage_copy` 的变量。

![copy_variable](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8882293761/p532236.gif)

#### **变量删除**

如图所示，高亮区域的图标即为变量删除的按钮，点击确认后即可对变量进行删除。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2122985871/p516102.png)

### **模拟数据编辑**

模拟数据即 Mock 数据，是对卡片变量值的模拟。

发送卡片需要结合真实的卡片数据，而我们可以在搭建器中通过变量数据的模拟来预览卡片在不同环境下的样子，有助你对卡片的布局等内容及时进行调整。

模拟数据的编辑，在数据源面板中共有两种方式：

1. 单个变量 Mock 数据编辑
2. 卡片整体 Mock 数据编辑

#### **单个变量 Mock 数据编辑**

如图所示，高亮区域的图标即为变量模拟数据编辑入口，点击后即可进入该变量的模拟数据编辑页面。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2122985871/p516114.png)

**示例**：

1. 点击`title`变量的编辑 Mock 数据图标，进入 Mock 数据编辑面板。![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2122985871/p516138.png)
2. 进入 Mock 数据编辑面板后，并填写数据为「钉钉，让进步发生」，点击「保存」对模拟数据的修改进行暂存。![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2122985871/p516117.png)
3. 此时回到变量编辑面板，还需要点击「保存」更新暂存的 Mock 数据修改。![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2122985871/p516139.png)
4. 此时可以看到模拟器中的卡片标题已经进行了修改。![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2122985871/p516140.png)

   > **[!NOTE]**
   >
   > 这里修改了模拟数据后，卡片内容之所以能响应是因为卡片的标题中绑定了相关的变量，关于如何通过变量展示动态化的内容，参见[绑定变量](0026-binding-variables.md)。

#### **卡片整体 Mock 数据编辑**

卡片整体 Mock 数据的编辑可以一次性对多种变量的多个变量进行 Mock 数据的编辑，提升 Mock 数据编辑的效率。

如图，在数据源面板中点击「Mock」按钮即可打开 Mock 数据编辑面板：

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5286989661/p516141.png)

在此面板中你可以直接通过编辑`JSON`的形式去编辑卡片的[公有、私有和本地数据](0030-public-private-and-local-data.md)。

## **模拟器**

模拟器用于预览卡片在不同客户端环境下的渲染效果，支持编辑和布局调整。结合模拟数据和预览模式，可提前感知卡片的实际渲染效果。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7143318661/p516144.png)

### 编辑模式

在**编辑模式**下，我们可以对组件快速的进行拖拽调整、祖先组件快速选择、组件复制、删除等操作，能够有效地提高你编辑卡片的效率。

- **组件拖拽排序**：长按组件可拖拽调整位置，大纲树面板会同步更新组件位置信息。

  ![simulator_drag_component](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3982293761/p537997.gif)
- **组件快速选择**：选中组件后出现操作栏（组件名、复制按钮、删除按钮）。鼠标悬浮到组件名上可查看祖先组件列表，点击即可选中并操作。

  1. **选中目标组件**，当你在模拟器中点击**选中**某个组件时，你就可以发现组件在高亮的同时还出现了一个组件的操作栏，如图所示，操作栏从左到右分别是：**组件名**、**组件复制按钮**与**组件删除按钮**。![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6147989661/p516203.png)
  2. 鼠标悬浮到**组件名**上，即可查看当前组件的所有祖先组件列表：![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6147989661/p516207.png)
  3. 在组件名下方出现的祖先组件列表，点击其中一个组件后即可对其进行选中高亮并做相关的操作。

     ![simulator_select_parent](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3982293761/p537998.gif)
- **组件复制**：选中组件后点击复制按钮，即可将该组件复制到同级兄弟节点处。

  ![simulator_com_copy](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3982293761/p537999.gif)
- **组件删除**：选中组件后点击删除按钮即可删除。

  ![simulator_com_del](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3982293761/p538000.gif)

  误删可通过撤销操作回退：点击「撤销」按钮或使用快捷键 Windows `Ctrl + Z` / Mac `Command + Z`。

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6147989661/p516219.png)

### **预览模式**

模拟器支持编辑模式与预览模式的切换。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6147989661/p516190.png)

当卡片处于**预览模式**时，搭建器将会做以下处理：

- 卡片模板不可编辑
- 依据当前 Mock 的数据对卡片进行渲染
- 激活组件的**条件渲染**
- 激活组件的**循环渲染生效**
- 激活组件的**点击事件**

> **[!NOTE]**
>
> 对于条件渲染、循环渲染以及点击事件，详情参见[组件属性设置面板](https://open.dingtalk.com/document/development/component-property-settings-panel)。

### **模拟器配置**

模拟器上半部分为配置区域，支持渲染环境、黑夜模式、客户端版本号及国际化等配置。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7143318661/p516158.png)

- **渲染环境**：支持模拟**桌面端、iOS、Android**下的渲染效果，默认为 iOS。

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6143318661/p516164.png)

  桌面端环境下还支持宽屏/窄屏模式切换。

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6143318661/p516166.png)

  以下是宽屏、窄屏的区别：

  | **窄屏** | **宽屏** |
  | --- | --- |
  | image | image |
- **黑夜模式**：点击「黑夜」按钮可查看卡片在钉钉黑夜模式下的效果。

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6143318661/p516171.png)
- **版本号与国际化**：点击「更多」可打开版本号及国际化配置面板。如需支持国际化，需在组件属性中填写国际化相关配置，组件属性的配置参见[组件属性设置面板](#41817b64b84wa)。

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6143318661/p516172.png)

## **组件属性设置面板**

选中模拟器中的组件后，属性设置面板会同步展示该组件的所有属性，供开发者配置。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1427989661/p516248.png)

### **属性分类**

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6982293761/p549932.png)

如上图所示，属性设置面板中的属性被分为四类：

- 内容：与组件内容相关的属性，如内容、图片地址、最大行数、是否显示等
- 样式：与组件样式相关的属性，常见的有文字颜色、文字大小、边距等
- 事件：与组件点击事件相关的属性，如链接跳转、回传请求、复制内容、弹窗提示等
- 高级：不隶属于前三类的高级属性，具体请查看组件的详细属性

### **文本内容设置**

文本内容设置被多个组件广泛使用，用于输入文本内容。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6982293761/p549941.png)

- **使用变量**

  除基础文本外，还可在文本中插入变量。

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6982293761/p549965.png)

  在文本内容属性设置中通过`${变量名}`格式使用变量。如果使用变量是对象变量的属性，可以通过`${object.property}`方式进行引用。

  **注意**：在循环渲染容器里引用循环项字段时，需要使用 `${loop.变量名}` 格式来引用变量。

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6982293761/p550031.png)

  > **[!NOTE]**
  >
  > 使用变量之前，请确保已经创建了对应的变量。创建变量的方法请参考[数据源面板](#aa650d08c1k6k)文档。
- **启用多语言支持**

  开启"国际化"配置后，可为每种语言配置独立文案，各语言文案中同样支持引用变量。

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6982293761/p549971.png)

  配置完成后可通过模拟器预览不同语言的效果。

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6982293761/p549975.png)

### **组件“条件显示”设置**

大多数组件可通过"是否显示"属性控制显隐，对应的设置面板为"条件显示"。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6982293761/p549980.png)

- **固定值**

  组件始终按配置的"显示"或"隐藏"状态展示，不会进行动态展示。
- **条件计算**

  满足指定条件时才显示组件，否则不显示。目前有两种条件类型：运行环境和变量。

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6982293761/p549982.png)

  | **条件类型** | **解释** |
  | --- | --- |
  | 运行环境 | 当客户端版本号满足条件时显示。可选择多个客户端（桌面端、安卓等），版本号必须合法，否则功能不生效。  image |
  | 变量 | 当卡片变量值满足条件时显示。不同变量类型对应不同的条件选项（如布尔值只能选"为 true"或"为 false"）。  image |

  支持创建多个条件，并选择"且"（所有条件都满足才显示）或"或"（任一条件满足即显示）。

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6982293761/p550000.png)

## **顶部操作栏**

顶部操作栏提供卡片模板级别的操作，同时显示模板名称、保存状态及帮助入口。

卡片搭建器顶部的操作栏提供卡片模板级别的操作，如模板的导入、导出、复制以及保存和发布等功能，同时在操作栏上显示卡片模板的名称、内容更新的保存情况以及帮助入口相关的信息。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7982293761/p516388.png)

以下是顶部操作栏的功能介绍：

| 功能 | 说明 |
| --- | --- |
| 复制模板 | 填写新模板名称后确认，即可创建当前模板的副本。 |
| 导出 | 导出当前模板的 JSON 描述文件，可导入到其他模板中使用。 |
| 导入 | 导入通过"导出"功能获取的 JSON 描述文件，在当前卡片模板中使用。 |
| 保存 | 保存当前卡片模板的所有修改。 |
| 发布 | 发布并锁定当前模板，防止意外修改导致业务异常。  **[!IMPORTANT]**  模板一旦发布则无法再次编辑，请谨慎操作。 |
