# coding:utf-8

# 父类
class Father(object):
    def __init__(self, sex, job, age, surname):
        self.sex = sex
        self.job = job
        self.age = age
        self.surname = surname

    def run(self):
        print("running...")

    def hobby(self):
        print("basketball")

# 子类1
class Son(Father):
    def __init__(self, sex, job, age, surname, school_name):
        # 调用父类现有方法
        super().__init__(sex, job, age, surname)
        # 进行扩展
        self.school_name = school_name
    # 重写
    def hobby(self):
        print("swimming")


# 子类2
class Daughter(Father):
    def __init__(self, sex, job, age, surname, school_name):
        # 调用父类现有方法
        super().__init__(sex, job, age, surname)
        # 进行扩展
        self.school_name = school_name

    # 重写
    def hobby(self):
        print("drawing")

# 获取爱好
def get_hobby(obj):
    obj.hobby()

if __name__ == "__main__":
    s = Son(sex="male", job="student", age=10, surname="Zhang", school_name="CHD")
    d = Daughter(sex="female", job="student", age=12, surname="Zhang", school_name="CHD")
    # 将s、d两个对象传入相同的函数get_hobby
    get_hobby(s)
    get_hobby(d)