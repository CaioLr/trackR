from . import performance_monitor

import logging
log = logging.getLogger(__name__)

pData = performance_monitor.PerformanceDataCollector()

def get_cpu_info() -> dict[str,float]:
    return {
        'cpu_percent_usage': pData.get_cpu_usage(),
        'cpu_temp': pData.get_cpu_temp(),
    }

def get_gpu_info() -> dict[str,float]:
    return {
        'gpu_percent_usage': pData.get_gpu_usage(),
        'gpu_temp': pData.get_gpu_temp(),
        'gpu_memory_usage': pData.get_gpu_memory(),
    }

def get_memory_info() -> dict[str,float]:
    memory_usage = pData.get_memory_sizes()
    ram_total = memory_usage[1]['available'] + memory_usage[0]['used']
    memory_usage = (memory_usage[0]['used'] / ram_total) * 100
    return {
        'ram_percent_usage': memory_usage,
        'ram_used': pData.get_memory_sizes()[0]['used'],
        'ram_available': pData.get_memory_sizes()[1]['available'],
        'ram_total': ram_total,
    }

def get_storage_info() -> dict[str,float]:
    return {
        'storage_usage': pData.get_storage_usage(),
        'storage_temp': pData.get_storage_temp()
    }

def get_data() -> dict[str,dict]:
    data = {
        'cpu': get_cpu_info(),
        'gpu': get_gpu_info(),
        'ram': get_memory_info(),
        'storage': get_storage_info(),
    }
    return data