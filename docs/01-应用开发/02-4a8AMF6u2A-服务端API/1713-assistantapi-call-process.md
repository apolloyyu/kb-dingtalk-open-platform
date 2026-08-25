---
title: "Assistant API 调用流程"
source_url: "https://open.dingtalk.com/document/development/assistantapi-call-process"
namespace: "development"
slug: "assistantapi-call-process"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > AI 助理 > Assistant API 调用流程"
doc_id: "gybGAfgLmX"
updated_at: "2026-03-06 09:22:39"
---

> Source: https://open.dingtalk.com/document/development/assistantapi-call-process
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > AI 助理 > Assistant API 调用流程
> Updated: 2026-03-06 09:22:39

# Assistant API 调用流程

本文主要介绍了如何使用 Assistant API 的方式发起跟AI助理的聊天交互。

> **[!IMPORTANT]**
>
> 本文档已于 2026年 03 月 05 日迁移至历史文档（不推荐）目录，且本文档及相关接口仅保持现有功能，不再新增支持其他能力。

## **前提条件**

创建好了自定义 AI 助理。创建的方式有以下 2 种：

- 在客户端以下入口进行创建，按照正常引导流程操作即可。

  ![5eecdaf48460cde5c9a86e51a3e2f0bdca53d4e864534b5b58e70b814913bc360a414d3de9277d871abf3af1cbd75249977eb01c0408e66288d0d2d56b2efef41db8239340c94bc2d69c876fe0d59d8630db33177d325ce6fc653b69905bac42.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8807092271/p830813.png)
- 助理创建完成后，获取调用 Assistant API 的凭证信息，需要查询到助理关联应用的 Client ID 和 Client Secret 等信息。 操作路径是“进入到助理编辑页”>“选择集成开发”。

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2039331471/p925578.png)

## **功能简介**

- 开发者可以使用 Assistant API 给 AI 助理发送消息并发起交互，然后获取AI助理的回答。
- 适用于钉钉端外环境集成钉钉AI助理的能力，比如集成于微信公众号，把 AI 助理的回复作为公众号的响应，让公众号也能拥有钉钉 AI 助理同样的能力；也可以集成到企业内部的系统。

## **概览**

开发者需要完成以下三个步骤

1、创建一个线程（Thread），用于用户开启一段对话。

2、添加一个消息（Message）到线程（Thread）中，作为用户的提问（Query）。

3、运行（Run）Assistant在指定的线程（Thread）上，让Assistant生成回答。

### **步骤一:创建Thread**

Thread是一个用户跟AI助理的对话空间，相关的Message信息都存放在Thread中。

具体信息参考[创建线程](1716-api-createassistantthread.md)文档

### **步骤二:添加Message到Thread中**

- 用户的Query的信息可以通过Message传入，可以创建一个Message给到指定的线程（Thread）；

具体信息参考[创建消息](1719-api-createassistantmessage.md)文档

### **步骤三:创建Run，开始运行**

- 用户可以通过“Run”这个Thread来运行创建好的Assistant。
- AI助理会智能地选择并回答用户的问题最终生成的答案，并将过程中产生的内容以Message的形式添加进Thread中。
- 有2种运行Run的方式（二选一）

  - 非流式
  - 流式

#### **1、非流式Run**

创建非流式Run之后需要以轮询的方式检索Run，检索当前Run实例的状态（status）是否是一个结束状态，是则停止轮询；如果状态是“complete”时，再通过Message的list方法获取AI助理的回复内容列表。

**接入参考文档：**

- [创建AI助理的运行任务](1723-api-createassistantrun.md)文档
- [获取AI助理的运行任务](1724-api-retrieveassistantrun.md)文档
- [获取AI助理的消息列表](1721-api-listassistantmessage.md)文档

> **[!IMPORTANT]**
>
> **注意：**
>
> - 由于可能模型使用人数过多，可能需要花费一定时间等待运行结束，因此建议等待Run的状态为“complete”后再去取消息。

#### **2、流式Run**

创建流式Run之后，AI助理回复的消息就会出现在流式数据中，开发者需要根据不同消息的格式进行解析， 最后再输出到自己的业务系统中。 注意：流式Run无需轮询检索Run状态，也不需要读取Message列表

**接入参考文档：**[创建AI助理的运行任务](1723-api-createassistantrun.md)文档。

> **[!NOTE]**
>
> - 每一次流式推送的数据包含了一组 event 和 data，开发者需要根据 event 的类型，去解析 data 中的JSON数据。
> - event 类型中需要特殊说明的是：thread.message.delta，该 event 对应的 data 存放了AI助理的回复内容，开发者拿到data后需要先解析出 messageId 和 mode，根据 messageId 确定当前的流式消息内容归属于哪一条消息，然后再根据 mode 进行处理，存放到业务自己的内存缓存中，说明如下：
>
>   - 如果 mode 是“overwrite”，即是覆盖模式，那缓存中 message 内容就直接更新为当前的流式消息内容；
>   - 如果 mode 是“append”，即是增量模式，那就将当前的流式消息内容追加到缓存中；

流式数据格式：

```
event:thread.run.created
data:{"assistantId":"1039246b3f2249b38d9a69da2a2b0681","createAt":1722862859475,"expiredAt":1722863459475,"runId":"run_86c2f1428b494e6f9797cc5a6e2ed33f","startedAt":1722862859475,"statusEnum":"in_progress","threadId":"thread_message_e2c3bd6bbc074c56bde4371191af88d0"}
event:thread.message.created
data:{"createAt":1722862861124,"message":{"content":"","contentType":"text","role":"assistant"},"messageId":"message_75c25f6c8cd847d4b1971e5765b59486","threadId":"thread_message_e2c3bd6bbc074c56bde4371191af88d0"}
event:thread.message.delta
data:{"mode":"overwrite","delta":{"role":"assistant","text":{"value":"你好"},"type":"text"},"messageId":"message_75c25f6c8cd847d4b1971e5765b59486"}
event:thread.message.delta
data:{"mode":"overwrite","delta":{"role":"assistant","text":{"value":"你好！"},"type":"text"},"messageId":"message_75c25f6c8cd847d4b1971e5765b59486"}
event:thread.message.delta
data:{"mode":"overwrite","delta":{"role":"assistant","text":{"value":"你好！有什么"},"type":"text"},"messageId":"message_75c25f6c8cd847d4b1971e5765b59486"}
event:thread.message.delta
data:{"mode":"overwrite","delta":{"role":"assistant","text":{"value":"你好！有什么可以帮助你的吗？比如"},"type":"text"},"messageId":"message_75c25f6c8cd847d4b1971e5765b59486"}
event:thread.message.delta
data:{"mode":"overwrite","delta":{"role":"assistant","text":{"value":"你好！有什么可以帮助你的吗？比如查询某个地方的天气。&&Next"},"type":"text"},"messageId":"message_75c25f6c8cd847d4b1971e5765b59486"}
event:thread.message.delta
data:{"mode":"overwrite","delta":{"role":"assistant","text":{"value":"你好！有什么可以帮助你的吗？比如查询某个地方的天气。"},"type":"text"},"messageId":"message_75c25f6c8cd847d4b1971e5765b59486"}
event:thread.message.delta
data:{"mode":"overwrite","delta":{"role":"assistant","text":{"value":"你好！有什么可以帮助你的吗？比如查询某个地方的天气。"},"type":"text"},"messageId":"message_75c25f6c8cd847d4b1971e5765b59486"}
event:thread.message.delta
data:{"mode":"overwrite","delta":{"role":"assistant","text":{"value":"你好！有什么可以帮助你的吗？比如查询某个地方的天气。"},"type":"text"},"messageId":"message_75c25f6c8cd847d4b1971e5765b59486"}
event:thread.message.completed
data:{"createAt":1722862861124,"deleted":0,"message":{"content":"你好！有什么可以帮助你的吗？比如查询某个地方的天气。","role":"assistant"},"messageId":"message_75c25f6c8cd847d4b1971e5765b59486","runId":"run_86c2f1428b494e6f9797cc5a6e2ed33f","threadId":"thread_message_e2c3bd6bbc074c56bde4371191af88d0"}
event:thread.run.completed
data:{"assistantId":"1039246b3f2249b38d9a69da2a2b0681","createAt":1722862859487,"expiredAt":1722863459487,"runId":"run_86c2f1428b494e6f9797cc5a6e2ed33f","startedAt":1722862859487,"statusEnum":"completed","threadId":"thread_message_e2c3bd6bbc074c56bde4371191af88d0"}
event:done
data:[DONE]
```

## **最佳实践**

### **非流式调用示例**

```
public class AssistantRunService {
    private static final String APP_ACCESS_TOKEN = "${your_access_token}";
    private static final String ASSISTANT_ID = "${your_assistant_id}";

    public String createThread() {
        RestTemplate restTemplate = new RestTemplate();

        HttpHeaders httpHeaders = new HttpHeaders();
        httpHeaders.setContentType(MediaType.APPLICATION_JSON);
        httpHeaders.set("x-acs-dingtalk-access-token", APP_ACCESS_TOKEN);
        HttpEntity<Void> request = new HttpEntity<>(httpHeaders);
        ResponseEntity<JSONObject> response = restTemplate.postForEntity("https://api.dingtalk.com/v1.0/assistant/threads", request, JSONObject.class);
        if (!Objects.equals(response.getStatusCode(), HttpStatus.OK)) {
            // TODO 调用接口失败的场景处理，做对应的异常业务处理
            throw new RuntimeException("create thread http response status is not ok");
        }

        JSONObject body = response.getBody();
        if (body == null) {
            // TODO 接口未返回任何内容，做对应的异常业务处理
            throw new RuntimeException("create thread http response body is invalid");
        }
        // 返回创建的threadId
        return body.getString("id");
    }

    public String createMessage(String threadId, String content) {
        String url = String.format("https://api.dingtalk.com/v1.0/assistant/threads/%s/messages", threadId);
        RestTemplate restTemplate = new RestTemplate();

        JSONObject requestBody = new JSONObject();
        requestBody.put("role", "user");
        requestBody.put("content", content);
        HttpHeaders httpHeaders = new HttpHeaders();
        httpHeaders.setContentType(MediaType.APPLICATION_JSON);
        httpHeaders.set("x-acs-dingtalk-access-token", APP_ACCESS_TOKEN);
        HttpEntity<JSONObject> request = new HttpEntity<>(requestBody, httpHeaders);
        ResponseEntity<JSONObject> response = restTemplate.postForEntity(url, request, JSONObject.class);
        if (!Objects.equals(response.getStatusCode(), HttpStatus.OK)) {
            // TODO 调用接口失败的场景处理，做对应的异常业务处理
            throw new RuntimeException("create user message http response status is not ok");
        }

        JSONObject body = response.getBody();
        if (body == null) {
            // TODO 接口未返回任何内容，做对应的异常业务处理
            throw new RuntimeException("create user message http response body is null");
        }
        // 返回创建的messageId
        return body.getString("id");
    }

    public List<String> getReplyMessage(String threadId, String runId) throws Exception {
        // 如果传入runId
        String url = String.format("https://api.dingtalk.com/v1.0/assistant/threads/%s/messages?runId=%s", threadId, runId);
        RestTemplate restTemplate = new RestTemplate();

        HttpHeaders httpHeaders = new HttpHeaders();
        httpHeaders.setContentType(MediaType.APPLICATION_JSON);
        httpHeaders.set("x-acs-dingtalk-access-token", APP_ACCESS_TOKEN);
        HttpEntity<String> request = new HttpEntity<>(httpHeaders);
        ResponseEntity<JSONObject> response = restTemplate.exchange(url, HttpMethod.GET, request, JSONObject.class);
        if (!Objects.equals(response.getStatusCode(), HttpStatus.OK)) {
            // TODO 调用接口失败的场景处理，做对应的异常业务处理
            throw new RuntimeException("list message http response status is not ok");
        }
        JSONObject body = response.getBody();
        if (body == null) {
            // TODO 接口未返回任何内容，做对应的异常业务处理
            throw new RuntimeException("list message http response body is null");
        }
        System.out.println("[list message response]:\n" + body.toJSONString() + "\n");
        List<JSONObject> data = body.getJSONArray("data").toJavaList(JSONObject.class);
        return data.stream().filter(Objects::nonNull)
                .filter(item -> Objects.equals(item.getString("role"), "assistant") || Objects.equals(item.getString("role"), "tool"))
                .filter(item -> item.get("content") != null)
                .sorted(Comparator.comparing(item -> item.getLong("createdAt")))
                .map(item -> {
                    Object contents = item.get("content");
                    List<JSONObject> contentsList = JSON.parseArray(JSON.toJSONString(contents), JSONObject.class);
                    return contentsList.get(0).getJSONObject("text").getString("value");

                })
                .collect(Collectors.toList());
    }

    public String createRun(String threadId) {
        String url = String.format("https://api.dingtalk.com/v1.0/assistant/threads/%s/runs", threadId);
        RestTemplate restTemplate = new RestTemplate();

        JSONObject requestBody = new JSONObject();
        requestBody.put("assistantId", ASSISTANT_ID);

        HttpHeaders httpHeaders = new HttpHeaders();
        httpHeaders.setContentType(MediaType.APPLICATION_JSON);
        httpHeaders.set("x-acs-dingtalk-access-token", APP_ACCESS_TOKEN);
        HttpEntity<JSONObject> request = new HttpEntity<>(requestBody, httpHeaders);
        ResponseEntity<JSONObject> response = restTemplate.postForEntity(url, request, JSONObject.class);
        if (!Objects.equals(response.getStatusCode(), HttpStatus.OK)) {
            // TODO 调用接口失败的场景处理，做对应的异常业务处理
            throw new RuntimeException("create run http response status is not ok");
        }

        JSONObject body = response.getBody();
        if (body == null || body.get("id") == null) {
            // TODO 接口未返回任何内容，做对应的异常业务处理
            throw new RuntimeException("create run http response body is null");
        }

        return body.getString("id");
    }

    public JSONObject retrieveRun(String threadId, String runId) {
        String url = String.format("https://api.dingtalk.com/v1.0/assistant/threads/%s/runs/%s", threadId, runId);
        RestTemplate restTemplate = new RestTemplate();
        HttpHeaders httpHeaders = new HttpHeaders();
        httpHeaders.setContentType(MediaType.APPLICATION_JSON);
        httpHeaders.set("x-acs-dingtalk-access-token", APP_ACCESS_TOKEN);
        HttpEntity<Void> request = new HttpEntity<>(httpHeaders);
        ResponseEntity<JSONObject> response = restTemplate.exchange(url, HttpMethod.GET, request, JSONObject.class);
        if (!Objects.equals(response.getStatusCode(), HttpStatus.OK)) {
            // TODO 调用接口失败的场景处理，做对应的异常业务处理
            throw new RuntimeException("retrieve run http response status is not ok");
        }

        JSONObject body = response.getBody();
        if (body == null) {
            // TODO 接口未返回任何内容，做对应的异常业务处理
            throw new RuntimeException("retrieve run http response body is null");
        }
        return body;
    }

    public static void main(String[] args) {
        AssistantRunService assistantRunService = new AssistantRunService();
        try {
            String threadId = assistantRunService.createThread();
            System.out.println(threadId);

            String messageId = assistantRunService.createMessage(threadId, "你好");
            System.out.println(messageId);

            String runId = assistantRunService.createRun(threadId);
            System.out.println(runId);

            JSONObject run = assistantRunService.retrieveRun(threadId, runId);
            List<String> runningStatusList = Arrays.asList("in_progress", "requires_action", "queued");
            while (runningStatusList.contains(run.get("status"))) {
                Thread.sleep(5000);
                run = assistantRunService.retrieveRun(threadId, runId);
                // TODO 开发者需要添加超时处理
            }

            if (Objects.equals(run.get("status"), "completed")) {
                List<String> replyMessage = assistantRunService.getReplyMessage(threadId, runId);
                System.out.println(replyMessage);
            } else if (Objects.equals(run.get("status"), "failed")) {
                // TODO 执行失败的异常处理
            } else {
                // TODO 处理未知状态
                System.out.println(run.get("status"));
                System.out.println(run.toJSONString());
            }
        } catch (HttpStatusCodeException e) {
            // HTTP响应异常
            log.error("Error Response code: " + e.getStatusCode().value());
            log.error("Error Response Body: " + e.getResponseBodyAsString(StandardCharsets.UTF_8));
            // TODO 响应异常处理
        } catch (Exception e) {
            log.error("AI assistant run error" + e.getMessage());
        }
    }
}
```

### 流式调用示例

```
public class AssistantRunStreamService {
    private static final String APP_ACCESS_TOKEN = "${your_access_token}";
    private static final String ASSISTANT_ID = "${your_assistant_id}";

    public String createThread() {
        RestTemplate restTemplate = new RestTemplate();

        HttpHeaders httpHeaders = new HttpHeaders();
        httpHeaders.setContentType(MediaType.APPLICATION_JSON);
        httpHeaders.set("x-acs-dingtalk-access-token", APP_ACCESS_TOKEN);
        HttpEntity<Void> request = new HttpEntity<>(httpHeaders);
        ResponseEntity<JSONObject> response = restTemplate.postForEntity("https://api.dingtalk.com/v1.0/assistant/threads", request, JSONObject.class);
        if (!Objects.equals(response.getStatusCode(), HttpStatus.OK)) {
            // TODO 调用接口失败的场景处理，做对应的异常业务处理
            throw new RuntimeException("create thread http response status is not ok");
        }

        JSONObject body = response.getBody();
        if (body == null) {
            // TODO 接口未返回任何内容，做对应的异常业务处理
            throw new RuntimeException("create thread http response body is invalid");
        }
        return body.getString("id");
    }

    public String createMessage(String threadId, String content) {
        String url = String.format("https://api.dingtalk.com/v1.0/assistant/threads/%s/messages", threadId);
        RestTemplate restTemplate = new RestTemplate();

        JSONObject requestBody = new JSONObject();
        requestBody.put("role", "user");
        requestBody.put("content", content);
        HttpHeaders httpHeaders = new HttpHeaders();
        httpHeaders.setContentType(MediaType.APPLICATION_JSON);
        httpHeaders.set("x-acs-dingtalk-access-token", APP_ACCESS_TOKEN);
        HttpEntity<JSONObject> request = new HttpEntity<>(requestBody, httpHeaders);
        ResponseEntity<JSONObject> response = restTemplate.postForEntity(url, request, JSONObject.class);
        if (!Objects.equals(response.getStatusCode(), HttpStatus.OK)) {
            // TODO 调用接口失败的场景处理，做对应的异常业务处理
            throw new RuntimeException("create user message http response status is not ok");
        }

        JSONObject body = response.getBody();
        if (body == null) {
            // TODO 接口未返回任何内容，做对应的异常业务处理
            throw new RuntimeException("create user message http response body is null");
        }
        return body.getString("id");
    }

    public static void main(String[] args) {
        try {
            AssistantRunStreamService assistantRunStreamService = new AssistantRunStreamService();
            String threadId = assistantRunStreamService.createThread();
            System.out.println(threadId);
            String messageId = assistantRunStreamService.createMessage(threadId, "你好");
            System.out.println(messageId);

            String url = String.format("https://api.dingtalk.com/v1.0/assistant/threads/%s/runs", threadId);
            URL urlObj = new URL(url);
            HttpURLConnection urlConnection = (HttpURLConnection) urlObj.openConnection();
            urlConnection.setReadTimeout(60000);
            urlConnection.setConnectTimeout(60000);
            urlConnection.setRequestProperty("Content-Type", "application/json");
            urlConnection.setRequestProperty("x-acs-dingtalk-access-token", APP_ACCESS_TOKEN);
            urlConnection.setRequestMethod("POST");
            urlConnection.setDoOutput(true);
            urlConnection.setDoInput(true);
            BufferedOutputStream bos = new BufferedOutputStream(urlConnection.getOutputStream());

            String jsonStr = "{\"assistantId\":\"${your_assistant_id}\", \"stream\": true}";
            bos.write(jsonStr.getBytes("utf-8"));
            bos.flush();
            InputStreamReader inputStreamReader = new InputStreamReader(urlConnection.getInputStream());
            BufferedReader reader = new BufferedReader(inputStreamReader);
            String data ;
            while ((data = reader.readLine()) != null) {
                if (data.isEmpty()) {
                    continue;
                }
                System.out.println(data);
                // TODO 开发者自定义的业务逻辑
            }
            inputStreamReader.close();
            reader.close();
        } catch (HttpStatusCodeException e) {
            // HTTP响应异常
            log.error("Error Response code: " + e.getStatusCode().value());
            log.error("Error Response Body: " + e.getResponseBodyAsString(StandardCharsets.UTF_8));
            // TODO 响应异常处理
        } catch (Exception e) {
            log.error("AI assistant run error" + e.getMessage());
            // TODO 异常处理
        }
    }
}
```

## **所属商业化版本**

钉钉 AI 生产力平台高级版和定制版。
