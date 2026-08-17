---
title: "发布自定义组件"
source_url: "https://open.dingtalk.com/document/development/publish-custom-components-1"
namespace: "development"
slug: "publish-custom-components-1"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 自定义组件 > 发布自定义组件"
doc_id: "SAqjsEPRmo"
updated_at: "2025-09-17 20:58:12"
---

> Source: https://open.dingtalk.com/document/development/publish-custom-components-1
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 自定义组件 > 发布自定义组件
> Updated: 2025-09-17 20:58:12

# 发布自定义组件

小程序原生支持引入第三方npm模块，因此，也就支持自定义组件发布到npm，方便开发者复用和分享。

## 文件结构

基于官方的小程序扩展组件库mini-ddui的目录结构，供开发者参考，更多信息请参考mini-ddui小程序扩展组件库。

以下是发布自定义组件的推荐文件结构，仅供参考 。

```
├── src // 用于单个自定义组件
│   ├── index.js
│   ├── index.json
│   ├── index.axml
│   └── index.acss
├── ├── demo //用于自定义组件的demo演示
│   ├── ├── index.js
│   ├── ├── index.json
│   ├── ├── index.axml
│   ├── └── index.acss
├── app.js // 用于自定义组件小程序demo
├── app.json
└── app.acss
```

## JSON示例

package.json示例代码：

```
// package.json
{
  "name": "your-custom-compnent",
  "version": "1.0.0",
  "description": "your-custom-compnent",
  "repository": {
    "type": "git",
    "url": "your-custom-compnent-repository-url"
  },
  "files": [
    "es"
  ],
  "keywords": [
    "custom-component",
    "mini-program"
  ],
  "devDependencies": {
    "rc-tools": "6.x"
  },
  "scripts": {
    "build": "rc-tools run compile && node scripts/cp.js && node scripts/rm.js",
    "pub": "git push origin && npm run build && npm publish"
  }
}
```

## JS示例

cp.js示例代码：

```
// scripts/cp.js
const fs = require('fs-extra');
const path = require('path');
// copy file
fs.copySync(path.join(__dirname, '../src'), path.join(__dirname, '../es'), {
  filter(src, des){
    return !src.endsWith('.js');
  }
});
```

rm.js示例代码：

```
// scripts/rm.js
const fs = require('fs-extra');
const path = require('path');

// remove unnecessary file
const dirs = fs.readdirSync(path.join(__dirname, '../es'));

dirs.forEach((item) => {
  if (item.includes('app.') || item.includes('DS_Store') || item.includes('demo')) {
    fs.removeSync(path.join(__dirname, '../es/', item));
  } else {
    const moduleDirs = fs.readdirSync(path.join(__dirname, '../es/', item));
    moduleDirs.forEach((item2) => {
      if (item2.includes('demo')) {
        fs.removeSync(path.join(__dirname, '../es/', item, item2));
      }
    });
  }
});

fs.removeSync(path.join(__dirname, '../lib/'));
```
