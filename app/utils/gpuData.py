import clr
import os

clr.AddReference(os.path.join(os.getcwd(), "assets\lib\LibreHardwareMonitorLib.dll"))
from LibreHardwareMonitor import Hardware

class GpuDataCollector:
    def __init__(self):
        self.computer = Hardware.Computer()
        self.computer.IsGpuEnabled = True
        self.computer.Open()

    def get_gpu_temp(self):
        for h in self.computer.Hardware:
            h.Update()
            for sensor in h.Sensors:
                if "temperature" in str(sensor.SensorType).lower():
                    return sensor.Value
        return None

    def get_gpu_memory(self):
        mem = []
        for h in self.computer.Hardware:
            h.Update()
            for sensor in h.Sensors:
                if "gpu memory used" in str(sensor.Name).lower():
                    mem.append({sensor.Name: sensor.Value})
                if "gpu memory total" in str(sensor.Name).lower():
                    mem.append({sensor.Name: sensor.Value})
        if mem:
            return mem
        return None

    def get_gpu_usage(self):
        for h in self.computer.Hardware:
            h.Update()
            for sensor in h.Sensors:
                if "load" in str(sensor.SensorType).lower():
                    return sensor.Value
        return None

