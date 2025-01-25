import requests
import time
import json

# 定义变量
url_base = "http://localhost:11434/v1"
completion_url = f"{url_base}/completions"
prompt = "API威胁检测装置是什么？"
#prompt = "Once upon a time"

# 已知的模型列表
models = [
    "qwen2",
    "mistral",
    "wizardlm2"
#    "bge_m3"  # 替换为你的实际模型名称
]
results = []

# 测量每个模型的请求时间并打印响应内容
def measure_model_performance(models):
    for model_name in models:
        print(f"Testing model: {model_name}")
        
        # 准备请求数据
        data = {
            "model": model_name,
            "prompt": prompt,
            "max_tokens": 50
        }
        
        # 记录开始时间
        start_time = time.time()
        
        elapsed_time = 0.0
        try:
            # 发送请求并获取响应
            response = requests.post(completion_url, json=data)
            response.raise_for_status()  # 检查请求是否成功
            
            # 计算耗时
            elapsed_time = time.time() - start_time
            
            # 输出结果
            print(f"Request took {elapsed_time:.6f} seconds")
            print("Response:")
            print(json.dumps(response.json(), indent=2))
        except requests.exceptions.RequestException as e:
            print(f"Error with model {model_name}: {e}")
        print(f"{model_name} \'{prompt}\' took {elapsed_time:.6f} seconds")
        result_str = f"{model_name} '{prompt}' took {elapsed_time:.6f} seconds"
        results.append(result_str)
if __name__ == "__main__":
    try:
        if not models:
            print("No models found.")
        else:
            measure_model_performance(models)
            
        print("Summary of results:")
        for result in results:
            print(result)
    except Exception as e:
        print(f"An error occurred: {e}")
