---
title: "注册小程序页面"
source_url: "https://open.dingtalk.com/document/development/register-a-mini-program-page-1"
namespace: "development"
slug: "register-a-mini-program-page-1"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 小程序页面配置 > 注册小程序页面"
doc_id: "q5HeVEQgBz"
updated_at: "2025-09-17 20:57:54"
---

> Source: https://open.dingtalk.com/document/development/register-a-mini-program-page-1
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 小程序页面配置 > 注册小程序页面
> Updated: 2025-09-17 20:57:54

# 注册小程序页面

## Page()

`Page()` 接受一个 `object` 作为参数，该参数用来指定页面的初始数据、生命周期函数、事件处理函数等。

```
//index.js
Page({
  data: {
    title: "Dingtalk"
  },
  onLoad(query) {
    // 页面加载
  },
  onReady() {
    // 页面加载完成
  },
  onShow() {
    // 页面显示
  },
  onHide() {
    // 页面隐藏
  },
  onUnload() {
    // 页面被关闭
  },
  onTitleClick() {
    // 标题被点击
  },
  onPullDownRefresh() {
    // 页面被下拉
  },
  onReachBottom() {
    // 页面被拉到底部
  },
  onShareAppMessage() {
   // 返回自定义分享信息
  },
  viewTap() {
    // 事件处理
    this.setData({
      text: 'Set data for update.'
    })
  },
  go() {
    // 带参数的跳转，从 page/index 的 onLoad 函数的 query 中读取 xx
    dd.navigateTo({url:'/page/index?xx=1'})
  },
  customData: {
    hi: 'Dingtalk'
  }
})
```

上面代码中，`Page()`方法的参数说明如下：

| **属性** | **类型** | **描述** |
| --- | --- | --- |
| data | Object or Function | 初始数据或返回初始化数据的函数。 |
| onTitleClick | Function | 点击标题触发。 |
| onPageScroll | Function({scrollTop}) | 页面滚动时触发。 |
| onLoad | Function(query: Object) | 页面加载时触发。 |
| onReady | Function | 页面初次渲染完成时触发。 |
| onShow | Function | 页面显示时触发。 |
| onHide | Function | 页面隐藏时触发。 |
| onUnload | Function | 页面卸载时触发。 |
| onPullDownRefresh | Function | 页面下拉时触发。 |
| onReachBottom | Function | 上拉触底时触发。 |
| onShareAppMessage | Function | 点击右上角分享时触发。 |
| 其他 | Any | 开发者可以添加任意的函数或属性到 `object`参数中，在页面的函数中可以用 `this`来访问。 |

## 页面数据data

`data`是页面第一次渲染使用的初始数据。

> **[!IMPORTANT]**
>
> data为对象时，如果在页面中修改 data 则会影响该页面的不同实例。

axml示例代码：

```
<view>{{text}}</view>
<view>{{array[0].msg}}</view>
```

js示例代码：

```
Page({
  data: {
    text: 'DingTalk',
    array: [{msg: '1'}, {msg: '2'}]
  }
})
```

- **生命周期方法的说明**

  | 属性 | 说明 |
  | --- | --- |
  | onLoad | 一个页面只会调用一次，query 参数为 dd.navigateTo 和 dd.redirectTo 中传递的 query 对象。 |
  | onShow | 页面显示。每次页面显示都会调用一次。 |
  | onReady | 页面初次渲染完成。一个页面只会调用一次，代表页面已经准备妥当，可以和视图层进行交互。对界面的设置，如 dd.setNavigationBar 请在 onReady 之后设置。 |
  | onHide | 页面隐藏。当 dd.navigateTo 到其他页面或底部 tab 切换时调用。 |
  | onUnload | 当 dd.redirectTo 或 dd.navigateBack 到其他页面的时候调用。 |
- **事件处理函数的说明**

  | 属性 | 说明 |
  | --- | --- |
  | onPullDownRefresh | 下拉刷新。监听用户下拉刷新事件，需要在 app.json 的 window 选项中开启pullRefresh，当处理完数据刷新后，dd.stopPullDownRefresh可以停止当前页面的下拉刷新。 |
  | onShareAppMessage | 用户分享，详见[分享](https://open.dingtalk.com/document/orgapp/mini-program-jsapi-share)。 |

## Page.prototype.setData()

`setData`函数用于将数据从逻辑层发送到视图层，同时改变对应的`this.data`的值。

`setData`接受一个对象作为参数。对象的键名`key`可以非常灵活，以数据路径的形式给出，如 `array[2].message`、`a.b.c.d`，并且不需要在`this.data`中预先定义。

> **[!IMPORTANT]**
>
> - 直接修改`this.data`无效，无法改变页面的状态，还会造成数据不一致。
> - 请尽量避免一次设置过多的数据。

代码示例：

```
<view>{{text}}</view>
<button onTap="changeTitle"> Change normal data </button>
<view>{{array[0].text}}</view>
<button onTap="changeArray"> Change Array data </button>
<view>{{object.text}}</view>
<button onTap="changePlanetColor"> Change Object data </button>
<view>{{newField.text}}</view>
<button onTap="addNewKey"> Add new data </button>
```

```
Page({
  data: {
    text: 'test',
    array: [{text: 'a'}],
    object: {
      text: 'blue'
    }
  },
  changeTitle() {
    // 错误！不要直接去修改 data 里的数据
    // this.data.text = 'changed data'  
    
    // 正确
    this.setData({
      text: 'ha'
    })
  },
  changeArray() {
    // 可以直接使用数据路径来修改数据
    this.setData({
      'array[0].text':'b'
    })
  },
  changePlanetColor(){
    this.setData({
      'object.text': 'red'
    });
  },
  addNewKey() {
    this.setData({
      'newField.text': 'c'
    })
  }
})
```

## Page.prototype.$spliceData()

`$spliceData`同样用于将数据从逻辑层发送到视图层，但是相比于`setData`，在处理长列表的时候，其具有更高的性能。`$spliceData`接受一个对象作为参数。

1. 对象的键名key可以非常灵活，以数据路径的形式给出，如 `array[2].message`、`a.b.c.d`，并且不需要在`this.data`中预先定义。
2. 对象的value为一个数组（格式：[start, deleteCount, ...items]）,数组的第一个元素为操作的起始位置，第二个元素为删除的元素的个数，剩余的元素均为插入的数据。对应`es5`中数组的`splice`方法。

示例代码：

```
<!-- page.axml -->
<view class="spliceData">
  <view a:for="{{a.b}}" key="{{item}}" style="border:1px solid red">
    {{item}}
  </view>
</view>
```

```
// page.js
Page({
  data: {
    a: {
      b: [1,2,3,4]
    }
  },
  onLoad(){
    this.$spliceData({ 'a.b': [1, 0, 5, 6] })
  },
})
```

页面输出：

```
1
5
6
2
3
4
```

## Page.prototype.$batchedUpdates(callback: Function)

> **[!NOTE]**
>
> `$batchedUpdates`自1.14.0之后才支持，可以使用`dd.canIUse('page.$batchedUpdates')`做兼容性处理，详情请参考[dd.canIUse](https://open.dingtalk.com/document/orgapp/dd-caniuse)。

### 参数说明

| **事件** | **类型** | **描述** |
| --- | --- | --- |
| callback | Function | 在此回调函数中的数据操作会被批量更新。 |

### 示例代码

```
// pages/index/index.js
Page({
  data: {
    counter: 0,
  },
  plus() {
    setTimeout(() => {
      this.$batchedUpdates(() => {
        this.setData({
          counter: this.data.counter + 1,
        });
        this.setData({
          counter: this.data.counter + 1,
        });
      });
    }, 200);
  },
});
```

```
<!-- pages/index/index.axml -->
<view>{{counter}}</view>
<button onTap="plus">+2</button>
```

- 本示例中每次点击按钮，页面的`counter` 会加 2。
- 将 `setData` 放在this.$batchedUpdates中，这样尽管有多次`setData`，但是却只有一次数据的传输。
