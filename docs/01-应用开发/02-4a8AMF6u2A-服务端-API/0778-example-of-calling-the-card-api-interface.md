---
title: "API 调用示例"
source_url: "https://open.dingtalk.com/document/development/example-of-calling-the-card-api-interface"
namespace: "development"
slug: "example-of-calling-the-card-api-interface"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "即时通信 > 互动卡片 > 示例与工具 > API 调用示例"
doc_id: "FtsWETyWUF"
updated_at: "2025-09-23 19:18:11"
---

> Source: https://open.dingtalk.com/document/development/example-of-calling-the-card-api-interface
> Path: 应用开发 / 服务端 API / 即时通信 > 互动卡片 > 示例与工具 > API 调用示例
> Updated: 2025-09-23 19:18:11

# API 调用示例

由于创建卡片、投放卡片接口参数比较复杂，本文档提供常见的参数组合和各语言调用示例以作参考。

## **创建并投放卡片（发送卡片）接口调用示例**

下面是三个常用场域的创建并投放卡片（发送卡片）接口调用传参示例，示例中花括号的内容需要替换成真实的数据，比如 access\_token、卡片模板 id、用户 userId、群聊 openConversationId 等。[创建卡片](0780-interface-for-creating-a-card-instance.md)和[投放卡片](0781-delivery-card-interface.md)接口的传参也可参考该示例。

### **场域类型：****IM机器人单聊**

HTTP

```
POST /v1.0/card/instances/createAndDeliver HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:String
Content-Type:application/json

{
  "cardTemplateId": "{卡片模板 id}",
  "outTrackId": "{唯一卡片实例 id}",
  "cardData": {
    "cardParamMap": {
      "string": "字符串",
      "boolean": "true",
      "number": "1",
      "markdown": "# markdown",
      "obj": "{\"key\": \"value\"}",
      "arr": "[{\"key\": \"value\"}]"
    }
  },
  "openSpaceId": "dtv1.card//IM_ROBOT.{用户 userId}",
  "imRobotOpenSpaceModel": { "supportForward": true },
  "imRobotOpenDeliverModel": { "spaceType": "IM_ROBOT" }
}
```

Java

```
import com.alibaba.fastjson.JSON;
import com.squareup.okhttp.*;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;
import java.util.UUID;

public class Main {
    
    public static Map<String, String> convertJsonValuesToString(Map<String, Object> obj) {
        Map<String, String> result = new HashMap<>();
        for (Map.Entry<String, Object> entry : obj.entrySet()) {
            String key = entry.getKey();
            Object value = entry.getValue();
            if (value instanceof String) {
                result.put(key, (String) value);
            } else {
                result.put(key, JSON.toJSONString(value));
            }
        }
        return result;
    }

    public static void main(String[] args) {
        String accessToken = "{access_token}";
        String url = "https://api.dingtalk.com/v1.0/card/instances/createAndDeliver";

        Map<String, Object> cardData = new HashMap<>();
        cardData.put("string", "字符串");
        cardData.put("boolean", true);
        cardData.put("number", 1);
        cardData.put("markdown", "# markdown");
        Map<String, String> obj = new HashMap<>();
        obj.put("key", "value");
        cardData.put("obj", obj);
        cardData.put("arr", new Object[]{obj});

        Map<String, Object> body = new HashMap<>();
        body.put("cardTemplateId", "{卡片模板 id}");
        body.put("outTrackId", UUID.randomUUID().toString());
        body.put("cardData", new HashMap<String, Object>() {{
            put("cardParamMap", convertJsonValuesToString(cardData));
        }});
        body.put("openSpaceId", "dtv1.card//IM_ROBOT.{用户 userId}");
        body.put("imRobotOpenSpaceModel", new HashMap<String, Object>() {{
            put("supportForward", true);
            put("lastMessageI18n", new HashMap<String, String>() {{
                put("ZH_CN", "您收到一条卡片消息");
            }});
        }});
        body.put("imRobotOpenDeliverModel", new HashMap<String, Object>() {{
            put("spaceType", "IM_ROBOT");
        }});

        OkHttpClient client = new OkHttpClient();
        MediaType JSON_MEDIA_TYPE = MediaType.parse("application/json; charset=utf-8");
        RequestBody requestBody = RequestBody.create(JSON_MEDIA_TYPE, JSON.toJSONString(body));
        Request request = new Request.Builder()
                .url(url)
                .post(requestBody)
                .addHeader("Content-Type", "application/json")
                .addHeader("Accept", "*/*")
                .addHeader("x-acs-dingtalk-access-token", accessToken)
                .build();

        try (Response response = client.newCall(request).execute()) {
            if (!response.isSuccessful()) throw new IOException("Unexpected code " + response);
            System.out.println(response.body().string());
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

Python

```
import uuid
import json
import requests

def convert_json_values_to_string(obj: dict) -> str:
    """
    Dump the attributes of a dictionary to a string.
    """
    result = {}
    for key, value in obj.items():
        if isinstance(value, str):
            result[key] = value
        else:
            result[key] = json.dumps(value)
    return result

access_token = "{access_token}"
headers = {
    "Content-Type": "application/json",
    "Accept": "*/*",
    "x-acs-dingtalk-access-token": access_token,
}
card_data = {
  "string": "字符串",
  "boolean": True,
  "number": 1,
  "markdown": "# markdown",
  "obj": {"key": "value"},
  "arr": [{"key": "value"}],
}
body = {
    "cardTemplateId": "{卡片模板 id}",
    "outTrackId": str(uuid.uuid1()),
    "cardData": {"cardParamMap": convert_json_values_to_string(card_data)},
    "openSpaceId": "dtv1.card//IM_ROBOT.{用户 userId}",
    "imRobotOpenSpaceModel": {
        "supportForward": True,
        "lastMessageI18n": {"ZH_CN": "您收到一条卡片消息"},
    },
    "imRobotOpenDeliverModel": {"spaceType": "IM_ROBOT"},
}

url = "https://api.dingtalk.com/v1.0/card/instances/createAndDeliver"

response = requests.post(url, headers=headers, json=body)
print(response.text)
```

Node.js

```
const axios = require('axios');
const uuid = require('uuid');

function convertJsonValuesToString(obj) {
    const result = {};
    for (const key in obj) {
        const value = obj[key];
        result[key] = (typeof value === 'string') ? value : JSON.stringify(value);
    }
    return result;
}

const accessToken = "{access_token}";
const headers = {
    "Content-Type": "application/json",
    "Accept": "*/*",
    "x-acs-dingtalk-access-token": accessToken,
};

const cardData = {
    "string": "字符串",
    "boolean": true,
    "number": 1,
    "markdown": "# markdown",
    "obj": {"key": "value"},
    "arr": [{"key": "value"}],
};

const body = {
    "cardTemplateId": "{卡片模板 id}",
    "outTrackId": uuid.v1(),
    "cardData": { "cardParamMap": convertJsonValuesToString(cardData) },
    "openSpaceId": "dtv1.card//IM_ROBOT.{用户 userId}",
    "imRobotOpenSpaceModel": {
        "supportForward": true,
        "lastMessageI18n": { "ZH_CN": "您收到一条卡片消息" },
    },
    "imRobotOpenDeliverModel": { "spaceType": "IM_ROBOT" },
};

const url = "https://api.dingtalk.com/v1.0/card/instances/createAndDeliver";

axios.post(url, body, { headers })
    .then(response => {
        console.log(response.data);
    })
    .catch(error => {
        console.error(error);
    });
```

Go

```
package main

import (
	"bytes"
	"encoding/json"
	"fmt"
	"net/http"

	"github.com/google/uuid"
)

func convertJsonValuesToString(obj map[string]interface{}) map[string]string {
	result := make(map[string]string)
	for key, value := range obj {
		if str, ok := value.(string); ok {
			result[key] = str
		} else {
			jsonValue, _ := json.Marshal(value)
			result[key] = string(jsonValue)
		}
	}
	return result
}

func main() {
	accessToken := "{access_token}"

	cardData := map[string]interface{}{
		"string":   "字符串",
		"boolean":  true,
		"number":   1,
		"markdown": "# markdown",
		"obj":      map[string]string{"key": "value"},
		"arr":      []map[string]string{{"key": "value"}},
	}

	body := map[string]interface{}{
		"cardTemplateId": "{卡片模板 id}",
		"outTrackId":     uuid.New().String(),
		"cardData": map[string]interface{}{
			"cardParamMap": convertJsonValuesToString(cardData),
		},
		"openSpaceId": "dtv1.card//IM_ROBOT.{用户 userId}",
		"imRobotOpenSpaceModel": map[string]interface{}{
			"supportForward":  true,
			"lastMessageI18n": map[string]string{"ZH_CN": "您收到一条卡片消息"},
		},
		"imRobotOpenDeliverModel": map[string]interface{}{
			"spaceType": "IM_ROBOT",
		},
	}

	jsonBody, _ := json.Marshal(body)

	req, err := http.NewRequest("POST", "https://api.dingtalk.com/v1.0/card/instances/createAndDeliver", bytes.NewBuffer(jsonBody))
	if err != nil {
		fmt.Println(err)
		return
	}
	req.Header.Set("Content-Type", "application/json")
	req.Header.Set("Accept", "*/*")
	req.Header.Set("x-acs-dingtalk-access-token", accessToken)

	client := &http.Client{}
	resp, err := client.Do(req)
	if err != nil {
		fmt.Println(err)
		return
	}
	defer resp.Body.Close()

	var resBody map[string]interface{}
	json.NewDecoder(resp.Body).Decode(&resBody)
	fmt.Println(resBody)
}
```

### **场域类型：IM机器人群聊**

HTTP

```
POST /v1.0/card/instances/createAndDeliver HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:String
Content-Type:application/json

{
  "cardTemplateId": "{卡片模板 id}",
  "outTrackId": "{唯一卡片实例 id}",
  "cardData": {
    "cardParamMap": {
      "string": "字符串",
      "boolean": "true",
      "number": "1",
      "markdown": "# markdown",
      "obj": "{\"key\": \"value\"}",
      "arr": "[{\"key\": \"value\"}]"
    }
  },
  "imGroupOpenSpaceModel": { "supportForward": true },
  "openSpaceId": "dtv1.card//IM_GROUP.{群聊 openConversationId}",
  "imGroupOpenDeliverModel": { "robotCode": "{应用 client-id}" }
}
```

Java

```
import com.alibaba.fastjson.JSON;
import com.squareup.okhttp.*;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;
import java.util.UUID;

public class Main {
    
    public static Map<String, String> convertJsonValuesToString(Map<String, Object> obj) {
        Map<String, String> result = new HashMap<>();
        for (Map.Entry<String, Object> entry : obj.entrySet()) {
            String key = entry.getKey();
            Object value = entry.getValue();
            if (value instanceof String) {
                result.put(key, (String) value);
            } else {
                result.put(key, JSON.toJSONString(value));
            }
        }
        return result;
    }

    public static void main(String[] args) {
        String accessToken = "{access_token}";
        String url = "https://api.dingtalk.com/v1.0/card/instances/createAndDeliver";

        Map<String, Object> cardData = new HashMap<>();
        cardData.put("string", "字符串");
        cardData.put("boolean", true);
        cardData.put("number", 1);
        cardData.put("markdown", "# markdown");
        Map<String, String> obj = new HashMap<>();
        obj.put("key", "value");
        cardData.put("obj", obj);
        cardData.put("arr", new Object[]{obj});

        Map<String, Object> body = new HashMap<>();
        body.put("cardTemplateId", "{卡片模板 id}");
        body.put("outTrackId", UUID.randomUUID().toString());
        body.put("cardData", new HashMap<String, Object>() {{
            put("cardParamMap", convertJsonValuesToString(cardData));
        }});
        body.put("openSpaceId", "dtv1.card//IM_GROUP.{群聊 openConversationId}");
        body.put("imGroupOpenSpaceModel", new HashMap<String, Object>() {{
            put("supportForward", true);
            put("lastMessageI18n", new HashMap<String, String>() {{
                put("ZH_CN", "您收到一条卡片消息");
            }});
        }});
        body.put("imGroupOpenDeliverModel", new HashMap<String, Object>() {{
            put("robotCode", "{应用 client-id}");
        }});

        OkHttpClient client = new OkHttpClient();
        MediaType JSON_MEDIA_TYPE = MediaType.parse("application/json; charset=utf-8");
        RequestBody requestBody = RequestBody.create(JSON_MEDIA_TYPE, JSON.toJSONString(body));
        Request request = new Request.Builder()
                .url(url)
                .post(requestBody)
                .addHeader("Content-Type", "application/json")
                .addHeader("Accept", "*/*")
                .addHeader("x-acs-dingtalk-access-token", accessToken)
                .build();

        try (Response response = client.newCall(request).execute()) {
            if (!response.isSuccessful()) throw new IOException("Unexpected code " + response);
            System.out.println(response.body().string());
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

Python

```
import uuid
import json
import requests

def convert_json_values_to_string(obj: dict) -> str:
    """
    Dump the attributes of a dictionary to a string.
    """
    result = {}
    for key, value in obj.items():
        if isinstance(value, str):
            result[key] = value
        else:
            result[key] = json.dumps(value)
    return result

access_token = "{access_token}"
headers = {
    "Content-Type": "application/json",
    "Accept": "*/*",
    "x-acs-dingtalk-access-token": access_token,
}
card_data = {
    "string": "字符串",
    "boolean": True,
    "number": 1,
    "markdown": "# markdown",
    "obj": {"key": "value"},
    "arr": [{"key": "value"}],
}

body = {
    "cardTemplateId": "{卡片模板 id}",
    "outTrackId": str(uuid.uuid1()),
    "cardData": {"cardParamMap": convert_json_values_to_string(card_data)},
    "openSpaceId": "dtv1.card//IM_GROUP.{群聊 openConversationId}",
    "imGroupOpenSpaceModel": {
        "supportForward": True,
        "lastMessageI18n": {"ZH_CN": "您收到一条卡片消息"},
    },
    "imGroupOpenDeliverModel": {"robotCode": "{应用 client-id}"},
}

url = "https://api.dingtalk.com/v1.0/card/instances/createAndDeliver"

response = requests.post(url, headers=headers, json=body)
print(response.text)
```

Node.js

```
const axios = require('axios');
const uuid = require('uuid');

function convertJsonValuesToString(obj) {
    const result = {};
    for (const key in obj) {
        const value = obj[key];
        result[key] = (typeof value === 'string') ? value : JSON.stringify(value);
    }
    return result;
}

const accessToken = "{access_token}";
const headers = {
    "Content-Type": "application/json",
    "Accept": "*/*",
    "x-acs-dingtalk-access-token": accessToken,
};

const cardData = {
    "string": "字符串",
    "boolean": true,
    "number": 1,
    "markdown": "# markdown",
    "obj": {"key": "value"},
    "arr": [{"key": "value"}],
};

const body = {
    "cardTemplateId": "{卡片模板 id}",
    "outTrackId": uuid.v1(),
    "cardData": { "cardParamMap": convertJsonValuesToString(cardData) },
    "openSpaceId": "dtv1.card//IM_GROUP.{群聊 openConversationId}",
    "imGroupOpenSpaceModel": {
        "supportForward": true,
        "lastMessageI18n": { "ZH_CN": "您收到一条卡片消息" },
    },
    "imGroupOpenDeliverModel": {"robotCode": "{应用 client-id}"},
};

const url = "https://api.dingtalk.com/v1.0/card/instances/createAndDeliver";

axios.post(url, body, { headers })
    .then(response => {
        console.log(response.data);
    })
    .catch(error => {
        console.error(error);
    });
```

Go

```
package main

import (
	"bytes"
	"encoding/json"
	"fmt"
	"net/http"

	"github.com/google/uuid"
)

func convertJsonValuesToString(obj map[string]interface{}) map[string]string {
	result := make(map[string]string)
	for key, value := range obj {
		if str, ok := value.(string); ok {
			result[key] = str
		} else {
			jsonValue, _ := json.Marshal(value)
			result[key] = string(jsonValue)
		}
	}
	return result
}

func main() {
	accessToken := "{access_token}"

	cardData := map[string]interface{}{
		"string":   "字符串",
		"boolean":  true,
		"number":   1,
		"markdown": "# markdown",
		"obj":      map[string]string{"key": "value"},
		"arr":      []interface{}{map[string]string{"key": "value"}},
	}

	body := map[string]interface{}{
		"cardTemplateId": "{卡片模板 id}",
		"outTrackId":     uuid.New().String(),
		"cardData": map[string]interface{}{
			"cardParamMap": convertJsonValuesToString(cardData),
		},
		"openSpaceId": "dtv1.card//IM_GROUP.{群聊 openConversationId}",
		"imGroupOpenSpaceModel": map[string]interface{}{
			"supportForward": true,
			"lastMessageI18n": map[string]string{
				"ZH_CN": "您收到一条卡片消息",
			},
		},
		"imGroupOpenDeliverModel": map[string]interface{}{
			"robotCode": "{应用 client-id}",
		},
	}

	jsonBody, _ := json.Marshal(body)

	req, err := http.NewRequest("POST", "https://api.dingtalk.com/v1.0/card/instances/createAndDeliver", bytes.NewBuffer(jsonBody))
	if err != nil {
		fmt.Println(err)
		return
	}
	req.Header.Set("Content-Type", "application/json")
	req.Header.Set("Accept", "*/*")
	req.Header.Set("x-acs-dingtalk-access-token", accessToken)

	client := &http.Client{}
	resp, err := client.Do(req)
	if err != nil {
		fmt.Println(err)
		return
	}
	defer resp.Body.Close()

	var resBody map[string]interface{}
	json.NewDecoder(resp.Body).Decode(&resBody)
	fmt.Println(resBody)
}
```

### **场域类型：吊顶**

HTTP

```
POST /v1.0/card/instances/createAndDeliver HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:String
Content-Type:application/json

{
  "cardTemplateId": "{卡片模板 id}",
  "outTrackId": "{唯一卡片实例 id}",
  "cardData": {
    "cardParamMap": {
      "string": "字符串",
      "boolean": "true",
      "number": "1",
      "markdown": "# markdown",
      "obj": "{\"key\": \"value\"}",
      "arr": "[{\"key\": \"value\"}]"
    }
  },
  "openSpaceId": "dtv1.card//ONE_BOX.{群聊 openConversationId}",
  "topOpenSpaceModel": { "spaceType": "ONE_BOX" },
  "topOpenDeliverModel": { "expiredTimeMillis": 1739795765042 }
}
```

Java

```
import com.alibaba.fastjson.JSON;
import com.squareup.okhttp.*;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;
import java.util.UUID;

public class Main {
    
    public static Map<String, String> convertJsonValuesToString(Map<String, Object> obj) {
        Map<String, String> result = new HashMap<>();
        for (Map.Entry<String, Object> entry : obj.entrySet()) {
            String key = entry.getKey();
            Object value = entry.getValue();
            if (value instanceof String) {
                result.put(key, (String) value);
            } else {
                result.put(key, JSON.toJSONString(value));
            }
        }
        return result;
    }

    public static void main(String[] args) {
        String accessToken = "{access_token}";
        String url = "https://api.dingtalk.com/v1.0/card/instances/createAndDeliver";

        Map<String, Object> cardData = new HashMap<>();
        cardData.put("string", "字符串");
        cardData.put("boolean", true);
        cardData.put("number", 1);
        cardData.put("markdown", "# markdown");
        Map<String, String> obj = new HashMap<>();
        obj.put("key", "value");
        cardData.put("obj", obj);
        cardData.put("arr", new Object[]{obj}); // Note: JSON array

        Map<String, Object> body = new HashMap<>();
        body.put("cardTemplateId", "{卡片模板 id}");
        body.put("outTrackId", UUID.randomUUID().toString());
        body.put("cardData", new HashMap<String, Object>() {{
            put("cardParamMap", convertJsonValuesToString(cardData));
        }});
        body.put("openSpaceId", "dtv1.card//ONE_BOX.{群聊 openConversationId}");
        body.put("topOpenSpaceModel", new HashMap<String, Object>() {{
            put("spaceType", "ONE_BOX");
        }});
        body.put("topOpenDeliverModel", new HashMap<String, Object>() {{
            put("expiredTimeMillis", 1739795765042);
        }});

        OkHttpClient client = new OkHttpClient();
        MediaType JSON_MEDIA_TYPE = MediaType.parse("application/json; charset=utf-8");
        RequestBody requestBody = RequestBody.create(JSON_MEDIA_TYPE, JSON.toJSONString(body));
        Request request = new Request.Builder()
                .url(url)
                .post(requestBody)
                .addHeader("Content-Type", "application/json")
                .addHeader("Accept", "*/*")
                .addHeader("x-acs-dingtalk-access-token", accessToken)
                .build();

        try (Response response = client.newCall(request).execute()) {
            if (!response.isSuccessful()) throw new IOException("Unexpected code " + response);
            System.out.println(response.body().string());
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

Python

```
import uuid
import json
import requests

def convert_json_values_to_string(obj: dict) -> str:
    """
    Dump the attributes of a dictionary to a string.
    """
    result = {}
    for key, value in obj.items():
        if isinstance(value, str):
            result[key] = value
        else:
            result[key] = json.dumps(value)
    return result

access_token = "{access_token}"
headers = {
    "Content-Type": "application/json",
    "Accept": "*/*",
    "x-acs-dingtalk-access-token": access_token,
}
card_data = {
    "string": "字符串",
    "boolean": True,
    "number": 1,
    "markdown": "# markdown",
    "obj": {"key": "value"},
    "arr": [{"key": "value"}],
}

body = {
    "cardTemplateId": "{卡片模板 id}",
    "outTrackId": str(uuid.uuid1()),
    "cardData": {"cardParamMap": convert_json_values_to_string(card_data)},
    "openSpaceId": "dtv1.card//ONE_BOX.{群聊 openConversationId}",
    "topOpenSpaceModel": { "spaceType": "ONE_BOX" },
    "topOpenDeliverModel": { "expiredTimeMillis": 1739795765042 }
}

url = "https://api.dingtalk.com/v1.0/card/instances/createAndDeliver"

response = requests.post(url, headers=headers, json=body)
print(response.text)
```

Node.js

```
const axios = require('axios');
const uuid = require('uuid');

function convertJsonValuesToString(obj) {
    const result = {};
    for (const key in obj) {
        const value = obj[key];
        result[key] = (typeof value === 'string') ? value : JSON.stringify(value);
    }
    return result;
}

const accessToken = "{access_token}";
const headers = {
    "Content-Type": "application/json",
    "Accept": "*/*",
    "x-acs-dingtalk-access-token": accessToken,
};

const cardData = {
    "string": "字符串",
    "boolean": true,
    "number": 1,
    "markdown": "# markdown",
    "obj": {"key": "value"},
    "arr": [{"key": "value"}],
};

const body = {
    "cardTemplateId": "{卡片模板 id}",
    "outTrackId": uuid.v1(),
    "cardData": { "cardParamMap": convertJsonValuesToString(cardData) },
    "openSpaceId": "dtv1.card//ONE_BOX.{群聊 openConversationId}",
    "topOpenSpaceModel": { "spaceType": "ONE_BOX" },
    "topOpenDeliverModel": { "expiredTimeMillis": 1739795765042 }
};

const url = "https://api.dingtalk.com/v1.0/card/instances/createAndDeliver";

axios.post(url, body, { headers })
    .then(response => {
        console.log(response.data);
    })
    .catch(error => {
        console.error(error);
    });
```

Go

```
package main

import (
	"bytes"
	"encoding/json"
	"fmt"
	"net/http"

	"github.com/google/uuid"
)

func convertJsonValuesToString(obj map[string]interface{}) map[string]string {
	result := make(map[string]string)
	for key, value := range obj {
		if str, ok := value.(string); ok {
			result[key] = str
		} else {
			jsonValue, _ := json.Marshal(value)
			result[key] = string(jsonValue)
		}
	}
	return result
}

func main() {
	accessToken := "{access_token}"

	cardData := map[string]interface{}{
		"string":   "字符串",
		"boolean":  true,
		"number":   1,
		"markdown": "# markdown",
		"obj":      map[string]string{"key": "value"},
		"arr":      []interface{}{map[string]string{"key": "value"}},
	}

	body := map[string]interface{}{
		"cardTemplateId": "{卡片模板 id}",
		"outTrackId":     uuid.New().String(),
		"cardData": map[string]interface{}{
			"cardParamMap": convertJsonValuesToString(cardData),
		},
		"openSpaceId": "dtv1.card//ONE_BOX.{群聊 openConversationId}",
		"topOpenSpaceModel": map[string]interface{}{
			"spaceType": "ONE_BOX",
		},
		"topOpenDeliverModel": map[string]interface{}{
			"expiredTimeMillis": 1739795765042,
		},
	}

	jsonBody, _ := json.Marshal(body)

	req, err := http.NewRequest("POST", "https://api.dingtalk.com/v1.0/card/instances/createAndDeliver", bytes.NewBuffer(jsonBody))
	if err != nil {
		fmt.Println(err)
		return
	}
	req.Header.Set("Content-Type", "application/json")
	req.Header.Set("Accept", "*/*")
	req.Header.Set("x-acs-dingtalk-access-token", accessToken)

	client := &http.Client{}
	resp, err := client.Do(req)
	if err != nil {
		fmt.Println(err)
		return
	}
	defer resp.Body.Close()

	var resBody map[string]interface{}
	json.NewDecoder(resp.Body).Decode(&resBody)
	fmt.Println(resBody)
}
```

## **相关文档**

- [创建并投放卡片](0783-create-and-deliver-cards.md)
