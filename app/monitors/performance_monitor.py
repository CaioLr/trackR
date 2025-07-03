from enum import nonmember
import os
import clr
clr.AddReference(os.path.join(os.getcwd(), "app", "lib", "LibreHardwareMonitorLib.dll"))
from LibreHardwareMonitor import Hardware
from typing import Optional

import logging
log = logging.getLogger(__name__)

class PerformanceDataCollector:
    def __init__(self):
        self.computer = Hardware.Computer()
        self.computer.IsCpuEnabled = True
        self.computer.IsGpuEnabled = True
        self.computer.IsMemoryEnabled = True
        self.computer.IsStorageEnabled = True
        self.computer.Open()

    # CPU
    def get_cpu_temp(self) -> Optional[float]: #CPU Temperature
        for h in self.computer.Hardware:
            h.Update()
            if "cpu" in str(h.HardwareType).lower():
                for sensor in h.Sensors:
                    if "temperature" in str(sensor.SensorType).lower():
                        return sensor.Value
        log.warning(f"CPU temperature not found.")
        return None
    def get_cpu_usage(self) -> Optional[float]: #CPU Usage
        for h in self.computer.Hardware:
            h.Update()
            if "cpu" in str(h.HardwareType).lower():
                for sensor in h.Sensors:
                    if (
                        "load" in str(sensor.SensorType).lower() and
                        "cpu total" in str(sensor.Name).lower()
                    ):
                        return sensor.Value
        log.warning(f"CPU usage not found.")
        return None

    # GPU
    def get_gpu_temp(self) -> Optional[float]: #GPU Temperature
        for h in self.computer.Hardware:
            h.Update()
            if "gpu" in str(h.HardwareType).lower():
                for sensor in h.Sensors:
                    if "temperature" in str(sensor.SensorType).lower():
                        return sensor.Value
        log.warning(f"GPU temperature not found.")
        return None
    def get_gpu_memory(self) -> Optional[list[dict[str,float]]]: #GPU Memory Usage
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
        log.warning(f"GPU memory not found.")
        return None
    def get_gpu_usage(self) -> Optional[float]: #GPU Usage
        for h in self.computer.Hardware:
            h.Update()
            if "gpu" in str(h.HardwareType).lower():
                for sensor in h.Sensors:
                    if "load" in str(sensor.SensorType).lower():
                        return sensor.Value
        log.warning(f"GPU usage not found.")
        return None

    # RAM Memory
    def get_memory_sizes(self) -> Optional[list[dict[str,float]]]: #RAM Sizes
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
        log.warning(f"RAM sizes not found.")
        return None

    # Storage
    def get_storage_usage(self) -> Optional[float]: #Storage Usage
        for h in self.computer.Hardware:
            h.Update()
            if "storage" in str(h.HardwareType).lower():
                for sensor in h.Sensors:
                    if "used space" in str(sensor.Name).lower():
                        return sensor.Value
        log.warning(f"Storage sizes not found.")
        return None
    def get_storage_temp(self) -> Optional[float]: #Storage Temperature
        for h in self.computer.Hardware:
            h.Update()
            if "storage" in str(h.HardwareType).lower():
                for sensor in h.Sensors:
                    if "temperature" in str(sensor.Name).lower():
                        return sensor.Value
        log.warning(f"Storage temperature not found.")
        return None

