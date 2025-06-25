from enum import nonmember
import os
import clr

clr.AddReference(os.path.join(os.getcwd(), "assets\lib\LibreHardwareMonitorLib.dll"))
from LibreHardwareMonitor import Hardware

class CpuDataCollector:
    def __init__(self):
        self.computer = Hardware.Computer()
        self.computer.IsCpuEnabled = True
        self.computer.Open()

    def get_cpu_temp(self):
        for h in self.computer.Hardware:
            h.Update()
            if h.HardwareType == Hardware.HardwareType.Cpu:
                for sensor in h.Sensors:
                    if "temperature" in str(sensor.SensorType).lower():
                        return sensor.Value
        return None

    def get_cpu_usage(self):
        for h in self.computer.Hardware:
            h.Update()
            if h.HardwareType == Hardware.HardwareType.Cpu:
                for sensor in h.Sensors:
                    if (
                        "load" in str(sensor.SensorType).lower() and
                        "cpu total" in str(sensor.Name).lower()
                    ):
                        return sensor.Value
        return None
