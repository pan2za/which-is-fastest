import psutil

def print_system_info():
    # 获取 CPU 信息
    cpu_percent = psutil.cpu_percent(interval=1)
    cpu_count = psutil.cpu_count(logical=True)  # 包括逻辑 CPU 核心数
    cpu_freq = psutil.cpu_freq()

    print(f"CPU Usage: {cpu_percent}%")
    print(f"Number of logical CPUs: {cpu_count}")
    print(f"Current CPU frequency: {cpu_freq.current:.2f} MHz")
    
    # 如果支持最小和最大频率，也打印出来
    if cpu_freq.min and cpu_freq.max:
        print(f"Min CPU frequency: {cpu_freq.min:.2f} MHz")
        print(f"Max CPU frequency: {cpu_freq.max:.2f} MHz")

    # 获取内存信息
    memory_info = psutil.virtual_memory()
    total_memory = memory_info.total / (1024 ** 3)  # 转换为 GB
    available_memory = memory_info.available / (1024 ** 3)  # 转换为 GB
    used_memory = memory_info.used / (1024 ** 3)  # 转换为 GB
    memory_percent = memory_info.percent

    print(f"Total Memory: {total_memory:.2f} GB")
    print(f"Available Memory: {available_memory:.2f} GB")
    print(f"Used Memory: {used_memory:.2f} GB")
    print(f"Memory Usage: {memory_percent}%")

if __name__ == "__main__":
    print_system_info()
