---
title: "mixins"
source_url: "https://open.dingtalk.com/document/development/mini-app-mixins"
namespace: "development"
slug: "mini-app-mixins"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 自定义组件 > 开发自定义组件 > mixins"
doc_id: "vRc5aKU65T"
updated_at: "2025-09-17 20:58:11"
---

> Source: https://open.dingtalk.com/document/development/mini-app-mixins
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 自定义组件 > 开发自定义组件 > mixins
> Updated: 2025-09-17 20:58:11

# mixins

开发者有时候可能会实现多个自定义组件，而这些自定义组件可能会有些公共逻辑要处理，为此，小程序提供了mixins。

> **[!IMPORTANT]**
>
> - 每一个 mixin 只能包含 props、data、methods、didMount、didUpdate、didUnmount等属性。
> - 多个 mixin 中的属性 key 要确保不同，否则会报错。

```
// /mixins/lifecycle.js
export default {
  didMount(){},
  didUpdate(prevProps,prevData){},
  didUnmount(){},
};
```

```
// /pages/components/xx/index.js
import lifecycle from '../../mixins/lifecycle';

const initialState = {
  data: {
    y: 2
  },
};

const defaultProps = {
  props: {
    a: 3,
  },
};

const methods = {
  methods: {
    onTapHandler() {},
  },
}

Component({
  mixins: [
    lifecycle,
    initialState,
    defaultProps,
    methods
  ],
  data: {
    x: 1,
  },
});
```
