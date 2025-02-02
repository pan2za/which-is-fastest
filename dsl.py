import requests
import json

OLLAMA_HOST = 'http://localhost:11434'
MODEL_NAME = 'deepseek-r1'

def parse_response(buffer):
    """解析带<think>标记的响应内容"""
    think_start = buffer.find('<think>')
    think_end = buffer.find('</think>')
    
    think_content = ''
    response_content = buffer
    
    if think_start != -1 and think_end != -1:
        think_content = buffer[think_start+7:think_end]
        response_content = buffer[think_end+8:]
    elif think_start != -1:  # 检测到未闭合标签
        response_content = buffer[think_start:] + "[思考未完成]"
    
    return think_content.strip(), response_content.strip()

def chat_with_ollama():
    context = []
    print("Ollama 交互开始（输入 'exit' 退出）")
    
    while True:
        try:
            user_input = input("用户: ")
            if user_input.lower() in ['exit', 'quit']:
                break

            data = {
                "model": MODEL_NAME,
                "prompt": f"{user_input}，请在<think>标签中先进行思考，再用</think>结束思考后回复",
                "stream": True,
                "context": context,
                "options": {"temperature": 0.5}
            }

            buffer = ""  # 流式数据缓冲区
            think_content = ""
            response_content = ""
            
            with requests.post(
                f"{OLLAMA_HOST}/api/generate",
                json=data,
                stream=True,
                timeout=60
            ) as response:
                for line in response.iter_lines():
                    if line:
                        chunk = json.loads(line.decode('utf-8'))
                        
                        # 累积响应内容
                        buffer += chunk.get("response", "")
                        
                        # 实时解析内容
                        current_think, current_response = parse_response(buffer)
                        
                        # 更新有效内容
                        if current_think:
                            think_content = current_think
                        if current_response:
                            response_content = current_response
                            
                        # 检测生成是否完成
                        if chunk.get("done"):
                            # 最终清理缓冲区
                            final_think, final_response = parse_response(buffer)
                            think_content = final_think or think_content
                            response_content = final_response or response_content
                            context = chunk.get("context", [])
                            break

            # 输出结构化结果
            if think_content:
                print(f"\n<思考过程>\n{think_content}\n</思考过程>")
            if response_content:
                print(f"\n<最终回复>\n{response_content}\n</回复结束>")

        except Exception as e:
            print(f"\n发生错误: {str(e)}")

if __name__ == "__main__":
    chat_with_ollama()
