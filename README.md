# which-is-fastest
which model is fastest in ollama model

1
curl -X POST "http://localhost:11434/v1/completions" \
-H "Content-Type: application/json" \
-d '{"model":"qwen2.5", "prompt":"Once upon a time","max_tokens":50}'


2

docker exec -it jeecg-boot-ollama-1 bash

root@44e7bd5ada51:/# ollama list
NAME                                 ID              SIZE      MODIFIED       
qwen2:latest                         dd314f039b9d    4.4 GB    37 minutes ago    
mofanke/dmeta-embedding-zh:latest    55960d8a3a42    408 MB    37 minutes ago    
mistral:latest                       f974a74358d6    4.1 GB    37 minutes ago    
quentinz/bge-large-zh-v1.5:latest    bc8ca0995fcd    651 MB    37 minutes ago    
bge-large:latest                     b3d71c928059    670 MB    37 minutes ago    
bge-m3:latest                        790764642607    1.2 GB    37 minutes ago    
nomic-embed-text:latest              0a109f422b47    274 MB    37 minutes ago    
mxbai-embed-large:latest             468836162de7    669 MB    2 weeks ago       
root@44e7bd5ada51:/# 


3
API威胁检测装置

4
import requests
import time

# 定义变量
url = "http://localhost:11434/v1/completions"
model_name = "example_model"  # 替换为你的模型名称
prompt = "Once upon a time"

# 准备请求数据
data = {
    "model": model_name,
    "prompt": prompt,
    "max_tokens": 50
}

# 记录开始时间
start_time = time.time()

# 发送请求
response = requests.post(url, json=data)

# 记录结束时间
end_time = time.time()

# 输出结果
elapsed_time = end_time - start_time
print(f"Request took {elapsed_time:.6f} seconds")


validator.py

5

#1 
 qwen2 "Once upon a time" 39.657311 seconds
 
#2
 qwen2 "Once upon a time" 9.714003 seconds
 mistral "Once upon a time" 41.652619 seconds
 bge-m3 does not work since it's an embedded model
 
#3
 qwen2 "Once upon a time" 36.316671 seconds
 mistral "Once upon a time" 41.525311 seconds
 
#4
qwen2 'Once upon a time' took 42.944693 seconds
mistral 'Once upon a time' took 39.544331 seconds

6 

curl -X POST http://localhost:11434/api/pull -d '{
  "name": "wizardlm2"
}'

ollama list
NAME                                 ID              SIZE      MODIFIED          
wizardlm2:latest                     c9b1aff820f2    4.1 GB    55 seconds ago       
qwen2:latest                         dd314f039b9d    4.4 GB    About an hour ago    
mofanke/dmeta-embedding-zh:latest    55960d8a3a42    408 MB    About an hour ago    
mistral:latest                       f974a74358d6    4.1 GB    About an hour ago    
quentinz/bge-large-zh-v1.5:latest    bc8ca0995fcd    651 MB    About an hour ago    
bge-large:latest                     b3d71c928059    670 MB    About an hour ago    
bge-m3:latest                        790764642607    1.2 GB    About an hour ago    
nomic-embed-text:latest              0a109f422b47    274 MB    About an hour ago    
mxbai-embed-large:latest             468836162de7    669 MB    2 weeks ago 

7
#4.5
qwen2 'Once upon a time' took 40.189143 seconds
mistral 'Once upon a time' took 40.463915 seconds
wizardlm2 'Once upon a time' took 36.084257 seconds

8

CPU Usage: 8.6%
Number of logical CPUs: 4
Current CPU frequency: 2750.01 MHz
Min CPU frequency: 800.00 MHz
Max CPU frequency: 3800.00 MHz
Total Memory: 15.54 GB
Available Memory: 8.24 GB
Used Memory: 6.06 GB
Memory Usage: 46.9%

lscpu | grep "Model name"

Model name:                           Intel(R) Core(TM) i5-7500 CPU @ 3.40GHz

9


#5
 qwen2 'Once upon a time' took 41.006630 seconds
mistral 'Once upon a time' took 37.462838 seconds
wizardlm2 'Once upon a time' took 39.889695 seconds

#6

qwen2 'Once upon a time' took 40.804133 seconds
mistral 'Once upon a time' took 36.839904 seconds
wizardlm2 'Once upon a time' took 40.563017 seconds


10

API威胁检测装置是什么？

#1
qwen2 'API威胁检测装置是什么？' took 39.082330 seconds
mistral 'API威胁检测装置是什么？' took 40.254380 seconds
wizardlm2 'API威胁检测装置是什么？' took 41.148996 seconds

#2
qwen2 'API威胁检测装置是什么？' took 39.101374 seconds
mistral 'API威胁检测装置是什么？' took 40.524140 seconds
wizardlm2 'API威胁检测装置是什么？' took 41.884625 seconds

#3
qwen2 'API威胁检测装置是什么？' took 38.996265 seconds
mistral 'API威胁检测装置是什么？' took 41.745497 seconds
wizardlm2 'API威胁检测装置是什么？' took 41.822845 seconds
