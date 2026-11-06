---
title: "模型微调"
source_url: "https://open.dingtalk.com/document/aipass/let-the-ai-assistant-play-a-better-role"
namespace: "aipass"
slug: "let-the-ai-assistant-play-a-better-role"
group: "AI PaaS"
tab: "DEAP·企业AI平台"
breadcrumb: "DEAP 开放API > 使用手册 > 模型微调"
doc_id: "P9gItFA7l6"
updated_at: "2026-11-03 14:57:15"
---

> Source: https://open.dingtalk.com/document/aipass/let-the-ai-assistant-play-a-better-role
> Path: AI PaaS / DEAP·企业AI平台 / DEAP 开放API > 使用手册 > 模型微调
> Updated: 2026-11-03 14:57:15

# 模型微调

## **核心优势**

- **免偏好数据**：无需人工标注的偏好数据集，直接通过编程式奖励函数优化模型。
- **双模型机制**：冻结的参考模型保持稳定性 + 可训练策略模型动态优化。
- **LoRA高效调优**：采用低秩LoRA适配器，仅训练0.1%参数实现全模型能力释放。
- **多任务兼容**：已验证支持Qwen3/Qwen2.5/QwQ等不同架构模型。

## **实战指南**

### **环境准备**

1. 进入 [DEAP后台](https://deap.dingtalk.com/#/sub-app/api-key) 创建一个API Key。

   > **[!NOTE]**
   >
   > 需要超管或者模型开发者权限。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5309863971/p1109832.png)
2. 选择对应的API Key，进入**权限设置**，添加模型微调的相关权限。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5309863971/p1109834.png)

   针对模型类别的所有权限组进行授权，使得API Key具备微调任务、训练集、模型部署等权限。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5309863971/p1109835.png)
3. 设置环境变量：

   - 将`API_KEY`设置为环境变量`export DINGTALK_API_KEY="sk-***"`。
   - 将`API_URL`设置为环境变量`export DINGTALK_BASE_URL=https://api-deap.dingtalk.com/v1`。
4. 安装Python SDK。

   ```
   pip install https://dingding-archive.oss-cn-shanghai.aliyuncs.com/maas/release/dingtalk-maas-pysdk/dingtalk_maas_pysdk-0.1.20-py3-none-any.whl
   ```

### **准备数据集**

数据集需包含训练集和测试集，训练集命名为`train.jsonl`，测试集命名为`test.jsonl`，每行一条数据。

> **[!NOTE]**
>
> `train.jsonl`及`test.jsonl`不能包含空行，且行数需大于 `num_gpu` \* `batch_size` \* `gradient_accumulation_steps` / (`epochs * num_generation`)，否则会报错。

- **SFT**

  `train.jsonl`及`test.json`兼容ChatML格式，需要包含messages列，具体示例如下：

  ```
  {
    "messages": [
      {
        "role": "user",
        "content": "写一个Python程序，找到给定列表中的最大数字。\n[3, 9, 2, 11, 5]"
      },
      {
        "role": "assistant",
        "content": "可以使用 Python 的内置函数 max 来找到给定列表中的最大数字。max()函数返回给定列表中的最大值。以下是使用max()函数的示例代码：\n```python\nmy_list = [3, 9, 2, 11, 5]\nmax_num = max(my_list)\nprint(\"最大数为:\", max_num)\n```\n输出结果：\n```\n最大数为: 11\n```\n首先，将给定的列表 [3, 9, 2, 11, 5] 存储在变量 my_list 中。然后，使用 max() 函数找到该列表中的最大数字，并将其存储在变量 max_num 中。最后，使用 print() 函数输出最大数字。\n注： 如果您的列表包含字符串则会引起错误，因为 max() 函数只能用于数字列表。"
      }
    ]
  }
  ```
- **GRPO**

  - `train.jsonl`中兼容ChatML格式，需要包含messages列，可添加其它任意所需字段。如果只要求模型输出正确的结论，不需要关注模型推理过程，则可使用"ground\_truth"或类似标签标记结论。
  - `test.jsonl`兼容ChatML格式，需要包含messages列，可以添加其它任意所需字段，用于GRPO阶段计算测试集奖励函数。

    ```
    {
      "messages": [
        {
          "role": "user",
          "content": "学校购买每张单价为140元的课桌，买了30张还多480元．如果用这笔钱买椅子，可以买40把．每把椅子的单价为多少元？"
        }
      ],
      "ground_truth": "117"
    }
    ```
- **CPT**

  `train.jsonl`中内容包含text的泛文本数据，可丰富预训练模型在特定领域的知识。

  ```
  {
    "text": "描述一下中国古代文学的典型特点。中国古代文学的典型特点包括：1. 以散文和诗歌为主要形式：中国古代文学中，散文和诗歌是最为常见和流行的文学形式。2. 强调意境：中国古代文学强调意境，而不仅仅关注情节的描述。作家致力于创造一种美感，通过文字表达出美好、深刻和含蓄的意境。3. 重视艺术性和审美价值：中国古代文学非常注重艺术性和审美价值，作家用精妙的文字表现出诗意和美感，增强作品的艺术性。4. 探究人性和社会问题：中国古代文学经常探究人性和社会问题，通过作品展示出人类在道德和伦理方面的深刻思考，及对社会现象和问题的探讨。5. 借物言志：中国古代文学中常借物言志，比如通过自然景观、动植物、传说和神话等形象，表达出人类的情感和内心世界。6. 注重传统文化的保护：中国古代文学注重传统文化的保护，作家在其作品中运用了许多古代文学的传统元素，生动展现出中国文化的独特魅力。"
  } {
    "text": "列举出五种古代建筑的设计特点。1. 希腊建筑的列式风格：希腊建筑以柱子为主要设计元素，通常采用遥望长廊和高大的柱子来营造开放、宏伟的氛围。 2. 古罗马建筑的弯曲线条：古罗马建筑特点是向外拓展，追求开放和自由的感觉。罗马主要使用大量的拱形和穹顶式建筑。 3. 中国古代建筑的斗拱和挑檐设计：古代中国建筑通常使用大量的楼台和门洞，以及高大的斗拱和挑檐，为建筑创造特有的中国风格。 4. 古埃及建筑的巨大石头：古埃及建筑通常使用巨大的石头、方石和石柱，以营造出庄重、神圣的气氛。 5. 日本古代建筑的轻松、简单风格：日本古代建筑通常简单、轻松，注重纵深感和自然感，以榻榻米、竹制墙壁等日本特有的设计元素为主。"
  } {
    "text": "描述一道健康的早餐菜谱，至少包含五种食材。材料：1个鸡蛋、1片火腿、1个小西红柿、少许碎芝士、1个全麦面包、半个牛油果。制作方法：1. 将鸡蛋打入碗中，加入少量盐和黑胡椒，搅匀。2. 将火腿切成小块，西红柿切成片状。3. 在不粘锅中，用少量油煎鸡蛋，煎至两面金黄。4. 将火腿块和西红柿片放在鸡蛋上，撒上少许碎芝士，再煮至芝士融化。5. 牛油果切成块状，将全麦面包切片，涂上牛油果，再放上煎好的蛋、火腿和西红柿，并撒上少许黑胡椒即可。此早餐菜谱富含蛋白质、维生素和纤维素，有助于增强体力、提高免疫力和保持健康体态。"
  }
  ```

### **上传数据集**

上传本地训练、验证数据集到钉钉的服务端。

```
import os
import openai

client = openai.OpenAI(
  base_url=os.environ.get("DINGTALK_BASE_URL"),
  api_key=os.environ.get("DINGTALK_API_KEY"),
)

training_file_name = '/your/dataset/directory/sft.jsonl'
training_response = client.files.create(
  file=open(training_file_name, "rb"),
  purpose="fine-tune",
  extra_query={
    "name": 'SFT测试例子',
    "mode": "sft"
  }
)
training_file_id = training_response.id
```

### **启动训练任务**

> **[!NOTE]**
>
> - base\_model目前支持三个模型，分别为：Qwen3-4B、Qwen3-14B、Qwen3-32B。
> - 建议先采用较低参数量的模型（如Qwen3-4B）验证训练流程，流程无明显问题后再切换到高参数量模型训练。
> - 每次提交新任务需等待上一个任务执行结束，再提交下一个任务。

- **SFT**

  训练SFT阶段，提交任务的示例如下：

  ```
  base_model = "Qwen3-4B"
  response = client.fine_tuning.jobs.create(
    model=base_model,
    training_file=training_file_id,
    validation_file=validation_file_id,
    method=job_create_params.Method(
      type= "supervised",
      supervised=SupervisedMethodParam(
        hyperparameters=SupervisedHyperparametersParam(
          num_train_epochs=1,
          per_device_train_batch_size=4,
          gradient_accumulation_steps=1,
        )
      ),
    ),
    extra_body={
      "name": 'sft-test',
    }
  )
  ```
- **GRPO**

  **定义奖励函数**：

  - 奖励函数所有输入字段均为List，completions字段为每个prompt生成的response，其数量应与num\_generations相等，在计算奖励函数时，可单独验证每个response的正确性，也可以计算每组response的相对优势。
  - 如果奖励函数需要额外的python库依赖，需要在奖励函数内部import。
  - **除模型输出的completions字段外，其余字段均为上传的jsonl文件中包含的字段，可以在奖励函数的入参中显式指定，也可以从\*\*kwargs中提取。**

  **示例1：格式验证函数**

  ```
  def format_reward(completions, ground_truth, **kwargs):
    def extract_answer(content: str):
      import re
      match = re.search(r'<answer>(.*?)</answer>', content, re.DOTALL)
      if match: return match.group(1)
      else: return None
    contents = [completion[0]["content"] for completion in completions]
    rewards = [1 if extract_answer(content) is not None else 0 for content in contents]
    return rewards
  ```

  **示例2：准确率验证函数**

  ```
  def accuracy_reward(completions, ground_truth, **kwargs):
    def extract_answer(content: str):
      import re
      match = re.search(r'<answer>(.*?)</answer>', content, re.DOTALL)
      if match: return match.group(1)
      else: return None
    contents = [completion[0]["content"] for completion in completions]
    rewards = [1 if extract_answer(content) == gt else 0 for content, gt in zip(contents, ground_truth)]
    return rewards
  ```

  训练GRPO时，可基于SFT训练结束的模型产物继续训练，也可以跳过SFT，直接训练GRPO。

  训练GRPO阶段，提交任务的示例如下：

  ```
  def accuracy_reward(completions, ground_truth, **kwargs):
    def extract_answer(content: str):
      import re
      match = re.search(r'<answer>(.*?)</answer>', content, re.DOTALL)
      if match:
        return match.group(1)
      else:
        return None

    contents = [completion[0]["content"] for completion in completions]
    rewards = [1 if extract_answer(content) == gt else 0 for content, gt in zip(contents, ground_truth)]
    return rewards

  def format_reward(completions, ground_truth, **kwargs):
    def extract_answer(content: str):
      import re
      match = re.search(r'<answer>(.*?)</answer>', content, re.DOTALL)
      if match:
        return match.group(1)
      else:
        return None

    contents = [completion[0]["content"] for completion in completions]
    rewards = [1 if extract_answer(content) is not None else 0 for content in contents]
    return rewards
    
  format_reward_source = inspect.getsource(format_reward).encode("utf-8")
  accuracy_reward_source = inspect.getsource(accuracy_reward).encode("utf-8")

  reward_fns = {
    "functions": {
      "format_reward": {
        "encodedFn": base64.b64encode(format_reward_source).decode("utf-8")
      },
      "accuracy_reward": {
        "encodedFn": base64.b64encode(accuracy_reward_source).decode("utf-8")
      }
    },
  }

  grpo_config = {
    "type": "reinforcement",
    "reinforcement": {
      "hyperparameters": {
        "rewardFns": reward_fns,
        "per_device_train_batch_size": 8,
        "per_device_eval_batch_size": 8
          "num_train_epochs": 1
          }
    }
  }

  response = client.fine_tuning.jobs.create(
    model=base_model,
    training_file=training_file_id,
    method=grpo_config,
    extra_body={
      "name": 'grpo-test',
    }
  )
  ```
- **CPT**

  训练CPT阶段，提交任务的示例如下：

  ```
  base_model = "Qwen3-4B"

  cpt_config = {
    "type": "cpt",
    "cpt": {
      "hyperparameters": {
        "num_train_epochs": 1,
        "per_device_train_batch_size": 4
      }
    }
  }

  response = client.fine_tuning.jobs.create(
    model=base_model,
    training_file=training_file_id,
    method=cpt_config,
    extra_body={
      "name": 'sft-test',
    }
  )
  ```

### **获取精调模型ID**

```
import os

import openai

client = openai.OpenAI(
  base_url=os.environ.get("DINGTALK_BASE_URL"),
  api_key=os.environ.get("DINGTALK_API_KEY"),
)

fine_tuning_job_id = "ftjob-d4mkml0b0qnd2s508t9g"
response = client.fine_tuning.jobs.retrieve(fine_tuning_job_id=fine_tuning_job_id)
print(response.model_dump_json(indent=2))
```

获得fine\_tuned\_model的内容作为模型ID。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5309863971/p1109843.png)

### **创建推理服务并获取服务状态**

> **[!IMPORTANT]**
>
> **在测试验证阶段，推理服务在启动达到2小时后将会被自动删除以保留平台资源。如需要生产环境部署推理服务，请提前钉钉联系预留资源。**

```
import os
import time

from dingtalk.client import DingTalkMaas

job_id = "ftjob-d4mkml0b0qnd2s508t9g"
model = "qwen1.5-0.5b-chat-20251125.ftjob-d4mkml0b0qnd2s508t9g"

# 当微调任务训练完成后，推理服务的checkpoints部署可用，可通过dmaasctl get checkpoints $adapterId 获取检查点列表。部署推理服务时传入需要部署的checkpointId

client = DingTalkMaas(api_key=os.environ.get("DINGTALK_API_KEY"))
deployment = client.deployments.create(
  adapter_id=job_id,
  model=model,
)

while True:
  deployment = client.deployments.get(
    code=deployment.maasCode,
    version=deployment.version,
  )

  print(deployment)
  if deployment.deployStatus == "SERVICE_AVAIABLE" or deployment.deployStatus == "SERVICE_AVAILABLE":
    break
  time.sleep(1.0)
```

输出的日志为：

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5309863971/p1109844.png)

如果需要持续测试，可传入`production` 标签。

```
import os
import time

from dingtalk.client import DingTalkMaas

job_id = "ftjob-d4mkml0b0qnd2s508t9g"
model = "qwen1.5-0.5b-chat-20251125.ftjob-d4mkml0b0qnd2s508t9g"

# 当微调任务训练完成后，推理服务的checkpoints部署可用，可通过dmaasctl get checkpoints $adapterId 获取检查点列表。部署推理服务时传入需要部署的checkpointId

client = DingTalkMaas(api_key=os.environ.get("DINGTALK_API_KEY"))
deployment = client.deployments.create(
  adapter_id=job_id,
  model=model,
  labels = {"env": "production"},
)
```

### **模型访问**

针对模型类别下的“大模型对话时权限”操作，选择 “授权” 操作 。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5309863971/p1109847.png)

对自训练模型进行授权，选择对应的模型进行授权，即 qwen3-4b-20251201.ftjob-d4mkml0b0qnd2s508t9g

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5309863971/p1109849.png)

**SDK访问示例如下：**

```
import openai

model = 'qwen3-4b-20251201.ftjob-d4mkml0b0qnd2s508t9g'

client = openai.OpenAI(
  base_url=os.environ.get("DINGTALK_BASE_URL"),
  api_key=os.environ.get("DINGTALK_API_KEY"),
)

response = client.chat.completions.create(
  model=model,
  messages=[
    {"role": "user", "content": "hello"}
  ],
  stream=False
)

print(response)
```

## **工具指南**

### **工具安装**

执行以下命令，安装工具：

```
pip install https://dingding-archive.oss-cn-shanghai.aliyuncs.com/maas/release/dingtalk-maas-pysdk/dingtalk_maas_pysdk-0.1.20-py3-none-any.whl
```

### **API Key权限设置**

API Key授权如下的权限：

- 微调任务的读取权限
- 微调任务的写入权限

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5309863971/p1109865.png)

### **查看日志**

执行以下代码，查看日志：

```
# dmaasctl logs adapter $job_id
dmaasctl logs adapter ftjob-xxajkjdkkdd
dmaasctl logs adapter ftjob-xxajkjdkkdd -f train.log -f tokens.log -o logs
dmaasctl logs adapter ftjob-xxajkjdkkdd -e '$export_id' -f quant.log
```

**支持参数**：

● `-o output` 输出日志，可以输出到某个目录`-o logs`，也可以将日志输入输出到某个文件 `-o train.log`。

● `-f` 指定下载文件，可单选 `-f train.log`，也可多选 `-f tokens.log -f tokens.log` 如果是量化任务 需指定下载文件为`quant.log`。

● `-e` 指定产物标识`export_id`，获取该量化任务的日志。

### **停止某训练任务**

执行以下命令，停止一个训练任务：

```
dmaasctl delete adapter ftjob-xxajkjdkkdd
```

### **获取adapter详情**

执行以下命令，获取一个adapter详情：

```
dmaasctl get adapter ftjob-xxajkjdkkdd -w --tensorboard
```

**支持参数**

- `-w/--watch` 可选，监控训练进度。
- `--tensorboard`，查看 Tensorboard。

### **下载adapter产物**

执行以下命令，下载adapter产物：

```
dmaasctl get artifact ftjob-xxajkjdkkdd [-o {dest_dir}]
```

**支持参数**

- `-o {dest_dir}`，下载到指定目录，可选，默认下载到当前目录
- `--merged`，获取lora合并产物，**SDK版本需要满足0.1.14**版本。

### **查询checkpoints**

执行以下命令，查询训练中所有的checkpoints：

```
dmaasctl get checkpoints ftjob-xxajkjdkkdd
```

### **创建产物合并**

执行以下命令，创建产物合并：

```
dmaasctl create merge ftjob-xxajkjdkkdd
```

### **创建量化任务**

执行以下命令，创建量化任务：

```
dmaasctl create quant repo-name-001/1
```

**支持参数**：

- `--quant_type/-qt {}` ：量化精度，`WxAyKVz`指对权重量化到x位、激活量化到y位，KV量化到z位，可选，默认为`W8A8-FP8`。可选精度参照如下：

  | **可选精度** | **说明** |
  | --- | --- |
  | W8A8-FP8 | 需要H系列、40xx系列及以上显卡，若用vllm推理，不需要提前量化，直接在启动server时增加`--quantization fp8`即可，模型质量几乎无损。 |
  | W8A8KV8-FP8 | 需要H系列、40xx系列及以上显卡，若用vllm推理，直接在启动server时增加`--quantization fp8 --kv-cache-dtype fp8`即可，kv量化会大幅影响模型质量。 |
  | W8A16-INT8 | 主流显卡均可以，模型质量略有损失。 |
  | W8A8-INT8 | 主流显卡均可以，模型质量损失较大。 |
  | W4A4-FP4 | 需要B系列、50xx系列显卡，模型质量损失较大。 |
  | W4A4KV4-FP4 | 需要B系列、50xx系列显卡，模型质量损失极大。 |
  | W4A16-INT4 | 主流显卡均可以，模型质量损失适中。 |
  | W4A4-INT4 | 主流显卡均可以，模型质量损失极大。 |
- `--quant_method/-qm {}`：量化方法，可选，默认为""，系统会自适应设置。可选方法参照如下：

  | **可选方法** | **说明** |
  | --- | --- |
  | AWQ | INT4优先选择AWQ。此方法只支持权重INT4位量化，精度较高，所需数据集较少，200条左右即可。 |
  | GPTQ | 其他INT量化优先选择GPTQ，此方法支持全部INT量化，精度上可能会低于AWQ，建议数据集1000条左右。 |
  | RTN | 此方法适用于所有量化，但用于INT量化时损失略大，FP量化效果较好，建议数据集1000条左右。 |

  精度上，FP8几乎无损，INT8略有损失，INT4损失较大。建议只使用权重量化，激活量化对模型质量影响较大，KV量化影响更严重。
- `--calib_dataset/-c {}`：校准数据集本地地址，部分量化方法需要上传校准数据集，数据集至少在100条以上。量化数据的数据和质量对量化结果也有一些影响。

  ```
  {
    "prompt": "学校购买每张单价为140元的课桌，买了30张还多480元．如果用这笔钱买椅子，可以买40把．每把椅子的单价为多少元？",
    "ground_truth": "117"
  }
  ```

### **查询产物状态**

执行以下命令，查询所有产物状态：

```
dmaasctl get artifacts repo--name-001/1
```

### **下载产物模型**

执行以下命令，下载指定产物模型：

```
dmaasctl get artifact repo-name-001/1 -e quant-xxxxxx
```

支持参数：

- `-e`/`--export-id {}`：产物标识，由8.中指令返回结果中的"code"字段得到，包括合并产物、量化产物。
- `-o`/`--output {dir}`：产物下载地址，可选，默认为""，产物模型存在工作目录下 。
