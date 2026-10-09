---
title: "使用示例"
source_url: "https://open.dingtalk.com/document/development/json-card-usage-examples"
namespace: "development"
slug: "json-card-usage-examples"
group: "互动卡片"
tab: "JSON 构建卡片（AI）"
breadcrumb: "构建卡片结构 > 使用示例"
doc_id: "DDsEo5xqO5"
updated_at: "2026-09-30 09:14:05"
---

> Source: https://open.dingtalk.com/document/development/json-card-usage-examples
> Path: 互动卡片 / JSON 构建卡片（AI） / 构建卡片结构 > 使用示例
> Updated: 2026-09-30 09:14:05

# 使用示例

## **完整卡片示例**

下面是四张可以直接发送的完整卡片，覆盖常见场景。每个示例都是一个**完整的消息数组**：创建画布、初始化数据、声明组件树，复制后替换 `surfaceId` 和业务数据即可使用。

- **表单交互**：文本、单选、复选、开关、数字与图片上传等输入控件，配合必填校验和提交按钮。
- **客户端动作**：调用钉钉单行输入面板（promptText），把用户输入写回数据模型并展示。
- **Agent 进度**：用折叠面板逐步展示执行过程，分批追加组件与数据，最后用 Markdown 输出结论。
- **数据报表**：用标签页切换表格与图表，展示结构化数据。

## 使用方式

保存为 `card.a2ui.json`，先离线校验，再发给自己确认渲染效果：

```
dws aicard lint --file card.a2ui.json --preflight new-card
dws aicard preview --file card.a2ui.json
```

发到群聊或单聊，详见 [DWS 发送与更新](0017-json-card-dws-send-and-update.md)。

## 表单交互

文本、单选、复选、开关、数字与图片上传等输入控件，配合必填校验和提交按钮。

**完整消息数组 · 3 条**

```
[
  {
    "version": "v1.0",
    "createSurface": {
      "surfaceId": "open-form",
      "catalogId": "https://dingtalk.com/card/a2ui/catalogs/public/catalog.json"
    }
  },
  {
    "version": "v1.0",
    "updateDataModel": {
      "surfaceId": "open-form",
      "path": "/",
      "value": {"form": {"name": "", "dept": [], "agreed": false, "notify": false, "count": 1, "images": []}}
    }
  },
  {
    "version": "v1.0",
    "updateComponents": {
      "surfaceId": "open-form",
      "components": [
        {
          "id": "root",
          "component": "Column",
          "children": [
            "name",
            "dept-title",
            "dept",
            "agreed",
            "notify-row",
            "count-title",
            "count",
            "images-title",
            "images",
            "submit"
          ]
        },
        {"id": "name", "component": "TextField", "label": "Name", "value": {"path": "/form/name"}},
        {"id": "dept-title", "component": "Text", "text": "Department"},
        {
          "id": "dept",
          "component": "ChoicePicker",
          "label": "Choose a department",
          "variant": "mutuallyExclusive",
          "options": [{"label": "Engineering", "value": "dev"}, {"label": "Design", "value": "design"}],
          "value": {"path": "/form/dept"}
        },
        {
          "id": "agreed",
          "component": "CheckBox",
          "label": "Agree to submit",
          "value": {"path": "/form/agreed"},
          "action": {"event": {"name": "agreement_changed", "context": {"agreed": {"path": "/form/agreed"}}}}
        },
        {
          "id": "notify-row",
          "component": "Row",
          "align": "center",
          "children": ["notify-label", "notify"]
        },
        {"id": "notify-label", "component": "Text", "text": "Receive progress updates", "weight": 1},
        {
          "id": "notify",
          "component": "Switch",
          "value": {"path": "/form/notify"},
          "action": {
            "event": {"name": "notification_changed", "context": {"notify": {"path": "/form/notify"}}}
          }
        },
        {"id": "count-title", "component": "Text", "text": "Quantity"},
        {
          "id": "count",
          "component": "NumberInput",
          "label": "Quantity",
          "placeholder": "Enter a number",
          "value": {"path": "/form/count"}
        },
        {"id": "images-title", "component": "Text", "text": "Attachments"},
        {
          "id": "images",
          "component": "ImageUpload",
          "label": "Upload images",
          "value": {"path": "/form/images"},
          "action": {"event": {"name": "image_uploaded", "context": {"images": {"path": "/form/images"}}}}
        },
        {
          "id": "submit",
          "component": "Button",
          "child": "submit-label",
          "variant": "primary",
          "checks": [
            {
              "condition": {"call": "required", "args": {"value": {"path": "/form/name"}}},
              "message": "Enter a name"
            },
            {"condition": {"path": "/form/agreed"}, "message": "Agree before submitting"}
          ],
          "action": {"event": {"name": "submit", "context": {"form": {"path": "/form"}}}}
        },
        {"id": "submit-label", "component": "Text", "text": "Submit"}
      ]
    }
  }
]
```

## 客户端动作

调用钉钉单行输入面板（promptText），把用户输入写回数据模型并展示。

**完整消息数组 · 3 条**

```
[
  {
    "version": "v1.0",
    "createSurface": {
      "surfaceId": "open-host-action",
      "catalogId": "https://dingtalk.com/card/a2ui/catalogs/public/catalog.json"
    }
  },
  {
    "version": "v1.0",
    "updateDataModel": {
      "surfaceId": "open-host-action",
      "path": "/",
      "value": {"preset": {"text": "Weekly progress"}, "ui": {}}
    }
  },
  {
    "version": "v1.0",
    "updateComponents": {
      "surfaceId": "open-host-action",
      "components": [
        {
          "id": "root",
          "component": "Column",
          "children": [
            "edit",
            "hint",
            "result",
            "actions",
            "title-label",
            "title-result",
            "note-label",
            "note-result"
          ]
        },
        {
          "id": "edit",
          "component": "Button",
          "child": "edit-label",
          "action": {
            "functionCall": {
              "catalogId": "urn:dingtalk:a2ui:host:v1",
              "call": "promptText",
              "args": {"initialValue": {"path": "/preset/text"}}
            }
          },
          "metadata": {"extensions": {"dt_actionBindingsV1": {"action": {"resultPath": "/ui/prompt"}}}}
        },
        {"id": "edit-label", "component": "Text", "text": "Edit content"},
        {
          "id": "hint",
          "component": "Text",
          "text": "After confirmation, the result appears below. Cancel keeps the previous result; a failed call clears it.",
          "maxLine": 3
        },
        {
          "id": "result",
          "component": "Text",
          "text": {"path": "/ui/prompt/data/text"},
          "maxLine": 3
        },
        {
          "id": "actions",
          "component": "ButtonGroup",
          "buttons": [
            {
              "label": "Edit title",
              "action": {
                "functionCall": {
                  "catalogId": "urn:dingtalk:a2ui:host:v1",
                  "call": "promptText",
                  "args": {"initialValue": {"path": "/preset/text"}}
                }
              },
              "metadata": {"extensions": {"dt_actionBindingsV1": {"action": {"resultPath": "/ui/title"}}}}
            },
            {
              "label": "Edit note",
              "action": {
                "functionCall": {
                  "catalogId": "urn:dingtalk:a2ui:host:v1",
                  "call": "promptText",
                  "args": {"initialValue": {"path": "/preset/text"}}
                }
              },
              "metadata": {"extensions": {"dt_actionBindingsV1": {"action": {"resultPath": "/ui/note"}}}}
            }
          ]
        },
        {"id": "title-label", "component": "Text", "text": "Title result"},
        {
          "id": "title-result",
          "component": "Text",
          "text": {"path": "/ui/title/data/text"},
          "maxLine": 2
        },
        {"id": "note-label", "component": "Text", "text": "Note result"},
        {
          "id": "note-result",
          "component": "Text",
          "text": {"path": "/ui/note/data/text"},
          "maxLine": 3
        }
      ]
    }
  }
]
```

## Agent 进度

用折叠面板逐步展示执行过程，分批追加组件与数据，最后用 Markdown 输出结论。

**完整消息数组 · 7 条**

```
[
  {
    "version": "v1.0",
    "createSurface": {
      "surfaceId": "open-progress",
      "catalogId": "https://dingtalk.com/card/a2ui/catalogs/public/catalog.json"
    }
  },
  {
    "version": "v1.0",
    "updateDataModel": {
      "surfaceId": "open-progress",
      "path": "/",
      "value": {"answer": {"text": "Generating a report."}, "tools": {"text": "Summarizing sample data"}}
    }
  },
  {
    "version": "v1.0",
    "updateComponents": {
      "surfaceId": "open-progress",
      "components": [
        {"id": "root", "component": "Column", "children": ["executionPanel", "answer"]},
        {
          "id": "executionPanel",
          "component": "CollapsiblePanel",
          "title": "Summarizing data",
          "variant": "reasoning",
          "defaultExpanded": false,
          "children": ["executionTimeline"],
          "fallbackMarkdown": "Execution steps",
          "textEffect": "shimmer"
        },
        {
          "id": "executionTimeline",
          "component": "Column",
          "children": ["step1", "toolGroup_summary"]
        },
        {"id": "step1", "component": "Text", "text": "Sample data loaded", "maxLine": 2},
        {
          "id": "toolGroup_summary",
          "component": "CollapsiblePanel",
          "title": "Summarizing",
          "defaultExpanded": false,
          "children": ["toolRow"],
          "fallbackMarkdown": "Tool call details"
        },
        {"id": "toolRow", "component": "Row", "children": ["toolIcon", "toolText"]},
        {
          "id": "toolIcon",
          "component": "Icon",
          "name": "CodeProgram_L_outlined",
          "colorToken": "common_level2_base_color"
        },
        {
          "id": "toolText",
          "component": "Text",
          "text": {"path": "/tools/text"},
          "maxLine": 2,
          "weight": 1
        },
        {"id": "answer", "component": "Markdown", "content": {"path": "/answer/text"}}
      ]
    }
  },
  {
    "version": "v1.0",
    "updateComponents": {
      "surfaceId": "open-progress",
      "components": [
        {
          "id": "executionTimeline",
          "component": "Column",
          "children": ["step1", "toolGroup_summary", "step2"]
        },
        {"id": "step2", "component": "Text", "text": "Category totals calculated", "maxLine": 2}
      ]
    }
  },
  {
    "version": "v1.0",
    "updateDataModel": {"surfaceId": "open-progress", "path": "/tools/text", "value": "Data summary complete"}
  },
  {
    "version": "v1.0",
    "updateDataModel": {
      "surfaceId": "open-progress",
      "path": "/answer/text",
      "value": "**Summary complete**: Engineering 8, Design 3, Testing 2; 13 items in total."
    }
  },
  {
    "version": "v1.0",
    "updateComponents": {
      "surfaceId": "open-progress",
      "components": [
        {
          "id": "executionPanel",
          "component": "CollapsiblePanel",
          "title": "Execution complete",
          "variant": "reasoning",
          "defaultExpanded": false,
          "children": ["executionTimeline"],
          "fallbackMarkdown": "Execution steps"
        },
        {
          "id": "toolGroup_summary",
          "component": "CollapsiblePanel",
          "title": "Summary complete",
          "defaultExpanded": false,
          "children": ["toolRow"],
          "fallbackMarkdown": "Tool call details"
        }
      ]
    }
  }
]
```

## 数据报表

用标签页切换表格与图表，展示结构化数据。

**完整消息数组 · 3 条**

```
[
  {
    "version": "v1.0",
    "createSurface": {
      "surfaceId": "open-report",
      "catalogId": "https://dingtalk.com/card/a2ui/catalogs/public/catalog.json"
    }
  },
  {
    "version": "v1.0",
    "updateDataModel": {
      "surfaceId": "open-report",
      "path": "/",
      "value": {
        "rows": [
          {"name": "Engineering", "count": 8},
          {"name": "Design", "count": 3},
          {"name": "Testing", "count": 2}
        ],
        "table": {
          "meta": [
            {"colKey": "name", "colName": "Department", "type": "text"},
            {"colKey": "count", "colName": "Completed", "type": "text"}
          ],
          "data": [
            {"name": "Engineering", "count": 8},
            {"name": "Design", "count": 3},
            {"name": "Testing", "count": 2}
          ]
        },
        "chart": {
          "type": "histogram",
          "data": [{"x": "Engineering", "y": 8}, {"x": "Design", "y": 3}, {"x": "Testing", "y": 2}]
        }
      }
    }
  },
  {
    "version": "v1.0",
    "updateComponents": {
      "surfaceId": "open-report",
      "components": [
        {"id": "root", "component": "Column", "children": ["tabs", "summary"]},
        {
          "id": "tabs",
          "component": "Tabs",
          "tabs": [{"title": "Data details", "child": "table"}, {"title": "Chart", "child": "chart-stack"}]
        },
        {
          "id": "table",
          "component": "Table",
          "data": {"path": "/table"},
          "pagination": true,
          "pageSize": 2
        },
        {
          "id": "chart-stack",
          "component": "Stack",
          "child": "chart",
          "overlays": [{"child": "badge", "position": "topEnd"}]
        },
        {"id": "chart", "component": "Chart", "data": {"path": "/chart"}},
        {"id": "badge", "component": "Text", "text": "This week"},
        {"id": "summary", "component": "Loop", "children": {"componentId": "row", "path": "/rows"}},
        {"id": "row", "component": "Text", "text": {"path": "name"}, "maxLine": 1}
      ]
    }
  }
]
```
