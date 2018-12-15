class Student:
    def __init__(self, name, stnum, gender, teacher):
        self.name   = name
        self.stnum  = stnum
        self.gender = gender
        self.teacher = Teacher(teacher) # 类的组合，调用Teacher类的,引入其他的类
    # @classmethod
    def __str__(self):
        return '  My name is %s.\n  Student number is %s. \n  My gender is %s.' % (self.name, self.stnum, self.gender)

    def sing(self):
        print('%s 在唱歌！！' % self.name)


    @staticmethod  # 静态方法，写在类的外面，可以独立成为一个函数，“愣”把它放到类中了
    def is_date_valid(dstr):
        y, m, d = map(int, dstr.split('-'))
        return 1 <= d <= 31 and 1 <= m <=12 and y < 4000  # 返回一个逻辑对象


class XueShengHui(Student):
    def __init__(self, name, stnum, gender, phone, teacher):
        super(XueShengHui, self).__init__(name, stnum, stnum, teacher)  # 初始化父类
        self.phone = phone  # 定义子类的属性
    def huizhang(self):
        print('  %s is 学生会会长  \n  %s 的电话是' % (self.name, self.phone)) # 子类父类混合调用

    def __call__(self, *args, **kwargs):   #
        print('aaa %s %s' % args)

    @classmethod  # 类方法，不用创建实例即可调用
    def create(cls, dstr):  # cls表示类本身, class的缩写
        y, m, d = map(int, dstr.split('-'))  # map(int, ['2000', '5', '4'])
        dt = cls(y, m, d)  # 即Date(y, m, d)
        return dt

class Teacher:    # 单独定义老师类，是学生类的附属类
    def __init__(self, name):
        self.name = name


if __name__ == '__main__':
    bb = XueShengHui('肖伍九', 201614301047, 'man', '15729885657', '刘')
    bb.huizhang()
    aa = bb.stnum
    print(bb.stnum)
    print(bb)   # 子类未定义"__str__"，默认调用父类的"__str__"方法
    print(bb.teacher.name)
    bb({aa:'123'},123)
    cc = Student.is_date_valid('2018-12-12')  # 测试挑勇类静态方法
    print(cc)
