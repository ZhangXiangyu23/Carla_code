# coding:utf-8

class Parents(object):
    __name = "kaka"
    __age = 35
    job = "teacher"

    def __hobby(self):
        print("pingpong")

    # 调用私有方法hobby
    def get_hobby(self):
        self.__hobby()

    # 获取年龄
    def get_age(self):
        return self.__age

    # 获取姓名
    def get_name(self):
        return self.__name


if __name__ == "__main__":
    # 实例化
    p = Parents()
    # 通过留出来的公有方法进行获取封装好的属性
    print(p.get_name())
    print(p.get_age())

    # 通过留出来的公有方法进行调用封装好的方法
    p.get_hobby()
