# coding:utf-8

# 父类
class Father(object):
    sex = "male"
    job = "teacher"
    age = 35
    surname = "Zhang"

    def run(self):
        print("running...")

    def hobby(self):
        print("basketball")

# 子类
class Son(Father):
    job = "student"
    age = 10

    def hobby(self):
        print("swimming...")



if __name__ == "__main__":
    s = Son()
    # 继承了父亲的性别和姓氏
    print(s.sex)
    print(s.surname)

