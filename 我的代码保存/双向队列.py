# 定义双向列表的类
class Dequeue(object):
    
    # 初始化空队列，使用列表数据类型
    def __init__(self):
        self.__list = []
    
    # 从头增加元素
    def app(self, item):
        self.__list.insert(0, item)
    
    # 从尾增加元素
    def append(self, item):
        self.__list.append(item)
    
    # 从尾部弹出元素
    def pop(self):
        if self.is_empty():
            return False
        return self.__list.pop()
    
    # 从头部弹出元素
    def headPop(self):
        if self.is_empty():
            return False
        return self.__list.pop(0)
    
    # 判断列表是否为空
    def is_empty(self):
        if self.__list is None:
            return True
        return False
    
    # 检查列表长度
    def size(self):
        print("---队列长度为{0}---".format(len(self.__list)))
        return len(self.__list)
    
    # 遍历列表
    def travel(self):
        for i in self.__list:
            print(i, end='-> ')
        print()

if __name__ == "__main__":
    ps = Dequeue()
    ps.append('haha1')  # 从尾部插入元素
    ps.app('haha2')     # 从头增加元素
    ps.append('haha3')  # 从尾增加元素
    ps.append('haha4')  # 从尾增加元素
    ps.pop()            # 从尾部弹出元素
    ps.size()           # 检查列表长度
    ps.travel()         # 遍历列表