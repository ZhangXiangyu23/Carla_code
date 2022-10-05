#coding:utf-8

from abc import ABC, abstractmethod



class raw_data(ABC):
    def __init__(self, timestamp, device_type, device_name, producter):
        self.timestamp = timestamp
        self.device_type = device_type
        self.device_name = device_name
        self.producter = producter



class Sensor(ABC):
    def __init__(self, sample_ratio, meta_data):
        self.sample_ratio = sample_ratio
        self.meta_data = meta_data

    @abstractmethod
    def GetAttribute(self):
        pass


class VehicleIntegratedSensor(ABC):
    def __init__(self, x, y, z, horizontal_angle, vertical_angle):
        self.x = x
        self.y = y
        self.z = z
        self.horizontal_angle = horizontal_angle
        self.vertical_angle = vertical_angle


    @abstractmethod
    def GetPosition(self):
        pass
