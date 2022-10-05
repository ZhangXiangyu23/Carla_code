# coding:utf-8

# 不是抽象类,是一个普通父类
class Parent(object):
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

    # 未实现的普通方法
    def hobby(self):
        pass

# 子类
class Son(Parent):
    # 重写
    def is_adult(self):
        print("False")


# 实例化
s = Son(sex="male", surname="Zhang", job="student")
s.is_adult()
s.hobby()












