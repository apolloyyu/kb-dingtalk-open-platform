---
title: "使用UI规范（OpenUI）"
source_url: "https://open.dingtalk.com/document/development/basic-specification-definition"
namespace: "development"
slug: "basic-specification-definition"
group: "专属版客户端插件"
tab: "Android 插件"
breadcrumb: "Android 插件 > 使用UI规范（OpenUI）"
doc_id: "6fObKA9a0Z"
updated_at: "2026-05-22 18:15:40"
---

> Source: https://open.dingtalk.com/document/development/basic-specification-definition
> Path: 专属版客户端插件 / Android 插件 / Android 插件 > 使用UI规范（OpenUI）
> Updated: 2026-05-22 18:15:40

# 使用UI规范（OpenUI）

本文重点描述了钉钉平台的基础UI规范，你可以引用钉钉定义的色值等，可以快速适配开发出符合钉钉规范的页面。

## **说明**

> **[!NOTE]**
>
> 钉钉定义的Color规范值均已适配钉钉的DarkMode样式，对于自定义的资源我们同样建议适配DarkMode，避免体验降级。

- 假如你期望参考钉钉的基础规范，请参考[基础规范定义](#602f7790371xz)。
- 假如你期望创建钉钉样式的Dialog，请参考[对话框服务（DialogService）](#a925ec2c346is)。
- 假如你期望展示钉钉样式的Toast，请参考[Toast服务（ToastService）](#8b43007c333f4)。
- 假如你期望使用图片加载器渲染图片，请参考[图片服务（ImageService）](#e5be1e78b3lxv)。

## **基础规范定义**

### **颜色规范（Color）**

| **颜色** | **用途** | **参考色** |
| --- | --- | --- |
| dingtalk\_line\_hard\_color | 线条，通常为list item的分割线 |  |
| dingtalk\_blue\_color | 钉钉蓝，常见于蓝色按钮、SwitchButton等 |  |
| dingtalk\_white\_color | 常规色值，白色 |  |
| dingtalk\_white\_level2\_color | 常规色值，带有透明度白色 |  |
| dingtalk\_background\_color | 页面背景色，常用于Activity背景色 |  |
| dingtalk\_foreground\_color | 页面前景色，常用于页面内整块元素的背景色，比如Toolbar、设置页面Item等 |  |
| dingtalk\_text\_level1\_color | 文本，一级文本颜色 |  |
| dingtalk\_text\_level2\_color | 文本，二级文本颜色 |  |
| dingtalk\_text\_level3\_color | 文本，三级文本颜色，常用于hint颜色 |  |
| dingtalk\_text\_level4\_color | 文本，四级文本颜色，常用于置灰文案 |  |

### **数值规范（Dimension）**

| **数值** | **描述** |
| --- | --- |
| dingtalk\_page\_padding\_left | 页面左侧缩进 |
| dingtalk\_page\_padding\_right | 页面右侧缩进 |
| dingtalk\_line\_height | 线条厚度，比如分割线 |

> **[!IMPORTANT]**
>
> - 本文中没有描述的ID请不要引用，尤其是“private\_”开头的资源ID。
> - 假如你的插件需要额外定义更多的资源ID，请追加自定义前缀，避免和钉钉平台资源命名冲突导致异常。

## **页面（DUIBaseActivity）**

> **[!NOTE]**
>
> DUIBaseActivity帮开发者封装好钉钉样式的Activity（主要是Toolbar），建议页面开发时使用该组件。

### **代码示例**

```
public class ExampleActivity extends DUIBaseActivity {
		@Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_demo);
        setTitle("测试DEMO");
    }
}
```

AndroidManifest.xml中不需要配置theme，直接定义即可：

```
<activity android:name="com.example.ExampleActivity" />
```

导航栏返回按钮默认为页面的finish()，假如期望自定义，可参考：

```
setNavigationOnClickListener(new OnClickListener {
		@Override
    public void onClick(View v) {
    		.....
    }
});
```

## **滑动开关（DUISwitchButton）**

### **组件说明**

| **组件名** | **功能说明** | **效果展示** |
| --- | --- | --- |
| DUISwitchButton | 实现了滑动开关的功能 | image |

### **接口说明**

| **接口** | **说明** |
| --- | --- |
| setChecked | 设置check状态 |
| isChecked | 判断开关当前check状态 |
| setOnCheckedChangeListener | 设置开关check监听者 |

### **代码示例**

View内置了默认宽度和高度，如果非必要的情况下，请直接使用wrap\_content。

```
<com.alibaba.android.dingtalk.openui.widget.DUISwitchButton
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"/>
```

## **Toast服务（ToastService）**

假如你的插件需要弹出Toast时，建议优先使用该服务，可用于弹出钉钉样式的Toast。

### **接口详情**

> **[!NOTE]**
>
> ToasService的所有接口均可在任意线程中使用，不需要切换到主线程。

| **接口** | **描述** |
| --- | --- |
| showToast | 弹出普通样式的Toast |
| showSuccessToast | 弹出附带成功（对勾）图标样式的Toast |
| showFailToast | 弹出失败（感叹号）图标样式的Toast |

### **代码示例**

```
ToastService service = 	MainBundle.getBundleContext().getService(ToastService.class);
service.showToast("执行完成");
```

## **对话框服务（DialogService）**

### **接口详情**

> **[!NOTE]**
>
> safeShow和safeHide接口均可在工作线程中调用，无需切换到主线程。

| **接口** | **描述** |
| --- | --- |
| createProgressDialog | 创建一个钉钉样式的加载进度的对话框 |
| createDialogBuilder | 创建一个钉钉样式的对话框构建器对象（请在UI线程中构建） |
| safeShow | 展示dialog |
| safeHide | 隐藏dialog |

### **代码示例**

```
DialogService service = MainBundle.getBundleContext().getService(DialogService.class);
ProgressDialog dialog = service.createProgressDialog(activity, true, "测试进度...");
service.safeShow(activity, dialog);
```

```
DialogService service = MainBundle.getBundleContext().getService(DialogService.class);
Dialog dialog = service.createDialogBuilder((Activity)jsRequest.context)
		.setTitle("演示标题")
		.setMessage("内容“)
		.setNegativeButton("我知道了", new DialogInterface.OnClickListener() {
        @Override
        public void onClick(DialogInterface dialogInterface, int i) {
           dialogInterface.dismiss();
        }
    })
    .create(jsRequest.context);
service.safeShow((Activity)jsRequest.context, dialog);
```

> **[!IMPORTANT]**
>
> 请务必在UI线程中创建Dialog，否则会出现Dialog无法关闭等异常现象。建议使用钉钉框架提供的ThreadService.runInUIExecutor或自定义UI线程实现。

## **图片服务（ImageService）**

### **接口详情**

| **接口** | **描述** |
| --- | --- |
| displayImage(imageView, url) | 将指定url的图片渲染到ImageView上，采用普通方式渲染 |
| displayAvatar(imageView, url) | 将指定url的图片渲染到imageView上，渲染方式是以钉钉会话头像的方式渲染（6.x钉钉版本是圆角矩形） |

> **[!NOTE]**
>
> 如下同样一张图片，左侧调用的displayAvatar的效果；右侧是 displayImage 的效果。
>
> ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7431753661/p490634.png)

### **代码示例**

```
ImageService service = MainBundle.getBundleContext().getService(ImageService.class);
if (service != null) {
    service.displayImage(imageView, url);
}
```
