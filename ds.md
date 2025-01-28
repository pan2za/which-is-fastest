1 ollama list
NAME                                 ID              SIZE      MODIFIED           
deepseek-r1:1.5b                     a42b25d8c10a    1.1 GB    About a minute ago    
qwen2:latest                         dd314f039b9d    4.4 GB    44 hours ago          
mofanke/dmeta-embedding-zh:latest    55960d8a3a42    408 MB    44 hours ago          
mistral:latest                       f974a74358d6    4.1 GB    44 hours ago          
quentinz/bge-large-zh-v1.5:latest    bc8ca0995fcd    651 MB    44 hours ago          
bge-large:latest                     b3d71c928059    670 MB    44 hours ago          
bge-m3:latest                        790764642607    1.2 GB    44 hours ago          
nomic-embed-text:latest              0a109f422b47    274 MB    44 hours ago          
wizardlm2:latest                     c9b1aff820f2    4.1 GB    2 days ago            
mxbai-embed-large:latest             468836162de7    669 MB    3 weeks ago 

2 

qwen2 'API威胁检测装置是什么？' took 41.718746 seconds
mistral 'API威胁检测装置是什么？' took 42.994939 seconds
wizardlm2 'API威胁检测装置是什么？' took 44.562419 seconds
deepseek-r1:1.5b 'API威胁检测装置是什么？' took 11.037689 seconds

but, deepseek answer is wierd. it answers, "对不起，我还没有学会回答这个问题。如果你有其他问题，我非常乐意为你提供帮助。"

3

qwen2 'API威胁检测装置是什么？' took 39.672386 seconds
mistral 'API威胁检测装置是什么？' took 41.712518 seconds
wizardlm2 'API威胁检测装置是什么？' took 41.669707 seconds
deepseek-r1:1.5b 'API威胁检测装置是什么？' took 9.864724 seconds

still deepseek answer is useless.

4

 ollama list
NAME                                 ID              SIZE      MODIFIED       
deepseek-r1:latest                   0a8c26691023    4.7 GB    30 seconds ago    
deepseek-r1:1.5b                     a42b25d8c10a    1.1 GB    17 minutes ago    
qwen2:latest                         dd314f039b9d    4.4 GB    44 hours ago      
mofanke/dmeta-embedding-zh:latest    55960d8a3a42    408 MB    44 hours ago      
mistral:latest                       f974a74358d6    4.1 GB    44 hours ago      
quentinz/bge-large-zh-v1.5:latest    bc8ca0995fcd    651 MB    44 hours ago      
bge-large:latest                     b3d71c928059    670 MB    44 hours ago      
bge-m3:latest                        790764642607    1.2 GB    44 hours ago      
nomic-embed-text:latest              0a109f422b47    274 MB    44 hours ago      
wizardlm2:latest                     c9b1aff820f2    4.1 GB    2 days ago        
mxbai-embed-large:latest             468836162de7    669 MB    3 weeks ago

5

qwen2 'API威胁检测装置是什么？' took 40.621979 seconds
mistral 'API威胁检测装置是什么？' took 42.178841 seconds
wizardlm2 'API威胁检测装置是什么？' took 41.381686 seconds
deepseek-r1 'API威胁检测装置是什么？' took 36.782832 seconds

but deepseek-r1 answer is not complete.
the result is 
"<think>\n\u597d\uff0c\u6211\u9700\u8981\u56de\u7b54\u5173\u4e8e\u201cAPI\u5a01\u80c1\u68c0\u6d4b\u88c5\u7f6e\u201d\u7684\u95ee\u9898\u3002\u9996\u5148\uff0c\u8fd9\u4e2a\u8bcd\u7ec4\u8ba9\u6211\u60f3\u5230\u5b83\u662f\u7528\u6765\u68c0\u6d4b\u53ef\u80fd\u5f71\u54cdAPI\u5b89\u5168\u7684\u8bbe\u5907\uff0c\u53ef\u80fd\u662f\u7f51\u7edc\u8bbe\u5907\u6216\u8005\u662f\u8f6f\u4ef6\u5de5\u5177\u3002\n\n\u63a5\u7740\uff0c\u6211\u5e94\u8be5\u62c6\u89e3\u4e00\u4e0b\u5173\u952e\u8bcd\u3002\u201c\u63a5\u53e3\u201d",

好，我需要回答关于“API威胁检测装置”的问题。首先，这个词组让我想到它是用来检测可能影响API安全的设备，可能是网络设备或者是软件工具。

接着，我应该拆解一下关键词。“接口”

6

qwen2 'API威胁检测装置是什么？' took 38.944212 seconds
mistral 'API威胁检测装置是什么？' took 40.614877 seconds
wizardlm2 'API威胁检测装置是什么？' took 41.780345 seconds
deepseek-r1 'API威胁检测装置是什么？' took 40.007925 seconds

7
qwen2 'API威胁检测装置是什么？' took 40.656196 seconds
mistral 'API威胁检测装置是什么？' took 40.664649 seconds
wizardlm2 'API威胁检测装置是什么？' took 41.217016 seconds
deepseek-r1 'API威胁检测装置是什么？' took 39.787528 seconds

All the deepseek-r1:latest is thinking without </think> end.


