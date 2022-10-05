#coding:utf-8
# 从abc库中导入ABC, abstractmethod模块
from abc import ABC, abstractmethod

# 抽象父类
class Parent(ABC):
    # 构造方法
    def __init__(self, sex, surname, job):
        self.sex = sex
        self.surname = surname
        self.job = job

    # 已经实现的普通方法
    def run(self):
        print("running...")

    def say(self):
        print("saying...")

    def is_adult(self):
        print("True")

    # 抽象方法
    @abstractmethod
    def hobby(self):
        pass

# 子类
class Son(Parent):
    # 重写
    def is_adult(self):
        print("False")
    # 实现抽象父类的抽象方法
    def hobby(self):
        print("basketball")


# 实例化
s = Son(sex="male", surname="Zhang", job="student")
s.is_adult()
s.hobby()






