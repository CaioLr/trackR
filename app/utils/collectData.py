from . import cpuData
from . import gpuData

cpu = cpuData.CpuDataCollector()
def get_cpu_info():

    return {
        'cpu_percent_usage': cpu.get_cpu_usage(),
        'cpu_temp': cpu.get_cpu_temp(),
    }

gpu = gpuData.GpuDataCollector()
def get_gpu_info():

    return {
        'gpu_percent_usage': gpu.get_gpu_usage(),
        'gpu_temp': gpu.get_gpu_temp(),
        'gpu_memory_usage': gpu.get_gpu_memory(),
    }

def get_data():
    data = {
        'cpu': get_cpu_info(),
        'gpu': get_gpu_info(),
    }

    return data