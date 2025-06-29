from enum import nonmember
import os
import clr

clr.AddReference(os.path.join(os.getcwd(), "assets\lib\LibreHardwareMonitorLib.dll"))
from LibreHardwareMonitor import Hardware

class PerformanceDataCollector:
    def __init__(self):
        self.computer = Hardware.Computer()
        self.computer.IsCpuEnabled = True
        self.computer.IsGpuEnabled = True
        self.computer.IsMemoryEnabled = True
        self.computer.IsStorageEnabled = True
        self.computer.Open()


    # CPU
    def get_cpu_temp(self): #CPU Temperature
        for h in self.computer.Hardware:
            h.Update()
            if "cpu" in str(h.HardwareType).lower():
                for sensor in h.Sensors:
                    if "temperature" in str(sensor.SensorType).lower():
                        return sensor.Value
        return None
    def get_cpu_usage(self): #CPU Usage
        for h in self.computer.Hardware:
            h.Update()
            if "cpu" in str(h.HardwareType).lower():
                for sensor in h.Sensors:
                    if (
                        "load" in str(sensor.SensorType).lower() and
                        "cpu total" in str(sensor.Name).lower()
                    ):
                        return sensor.Value
        return None

    # GPU
    def get_gpu_temp(self): #GPU Temperature
        for h in self.computer.Hardware:
            h.Update()
            if "gpu" in str(h.HardwareType).lower():
                for sensor in h.Sensors:
                    if "temperature" in str(sensor.SensorType).lower():
                        return sensor.Value
        return None
    def get_gpu_memory(self): #GPU Memory Usage
        mem = []
        for h in self.computer.Hardware:
            h.Update()
            if "gpu" in str(h.HardwareType).lower():
                for sensor in h.Sensors:
                    if "gpu memory used" in str(sensor.Name).lower():
                        mem.append({sensor.Name: sensor.Value})
                    if "gpu memory total" in str(sensor.Name).lower():
                        mem.append({sensor.Name: sensor.Value})
        if mem:
            return mem
        return None
    def get_gpu_usage(self): #GPU Usage
        for h in self.computer.Hardware:
            h.Update()
            if "gpu" in str(h.HardwareType).lower():
                for sensor in h.Sensors:
                    if "load" in str(sensor.SensorType).lower():
                        return sensor.Value
        return None

    # RAM Memory
    def get_memory_sizes(self): #RAM Sizes
        ram = []
        for h in self.computer.Hardware:
            h.Update()
            if "memory" in str(h.HardwareType).lower():
                for sensor in h.Sensors:
                    if (
                            "data" in str(sensor.SensorType).lower() and
                            "used" in str(sensor.Name).lower() and
                            "virtual" not in str(sensor.Name).lower()
                    ):
                        ram.append({"used": sensor.Value})
                    if (
                            "data" in str(sensor.SensorType).lower() and
                            "available" in str(sensor.Name).lower() and
                            "virtual" not in str(sensor.Name).lower()
                    ):
                        ram.append({"available": sensor.Value})
        if ram:
            return ram
        return None

    # Storage
    def get_storage_usage(self): #Storage Usage
        for h in self.computer.Hardware:
            h.Update()
            if "storage" in str(h.HardwareType).lower():
                for sensor in h.Sensors:
                    if "used space" in str(sensor.Name).lower():
                        return sensor.Value
        return None
    def get_storage_temp(self): #Storage Temperature
        for h in self.computer.Hardware:
            h.Update()
            if "storage" in str(h.HardwareType).lower():
                for sensor in h.Sensors:
                    if "temperature" in str(sensor.Name).lower():
                        return sensor.Value
        return None

