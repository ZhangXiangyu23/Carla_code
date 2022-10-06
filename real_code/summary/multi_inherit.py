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

# 母亲类
class Mother(object):
    sex = "female"
    job = "doctor"
    age = 35
    surname = "Li"

    def run(self):
        print("running...")

    def hobby(self):
        print("pingpong")

    def test(self):
        print("hello")



# 多继承,先继承了Father类，然后继承了Mother类
class Son(Father, Mother):
    job = "student"
    age = 10



if __name__ == "__main__":
    s = Son()
    # 两个父类里面都有surname和sex
    # 因为先继承的Father类，所以表现的是Father类的属性
    print(s.surname, s.sex)

    # 因为先继承的Father类，所以表现的是Father类的方法
    s.hobby()
    # 继承了Mother类的test方法
    s.test()
