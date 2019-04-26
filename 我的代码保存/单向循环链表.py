# 如果a+b+c=1000. 且a^2+b^2=c^2(a,b,c为自然数)， 如何求出所有a、b、c可能的组合？
 # coding:utf-8

class Node(object):
    # 初始化节点
    def __init__(self, item, next=None):
        self.element = item
        self.next = next
    
    # 输出节点数据
    def data(self):
        return self.element
 
class SingLink(object):
    # 初始化链表
    def __init__(self, node=None):
        self.__head = node
        if node:
            node.next = node
    

    # 判断链表是否为空
    def is_empty(self):
        return self.__head == None
    
    # 判断链表长度
    def lenth(self):
        count = 0
        cur = self.__head
        if self.is_empty():
            return 0
        elif cur.next.element == cur.element:
            print("---长度为{0}---".format(count + 1))
            return count + 1
        else:
            cur = self.__head
            while cur.next != self.__head:
                count += 1
                cur = cur.next
            print("---长度为{0}---".format(count + 1))
            return count + 1

    # 便利链表
    def travel(self):
        count = 0
        cur = self.__head
        while cur.next != self.__head:
            count += 1
            print(cur.element, end='-> ')
            cur = cur.next
        print(cur.element, end='-> \n')
        return count

    # 添加链表头部元素, 注意处理空链表的情况
    def app(self, item):
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = self.__head
        else:
            self.backed().next = node
            node.next = self.__head
            self.__head = node
            
            

    # 添加链表尾部元素, 注意处理空链表的情况
    def append(self, item):
        node = Node(item)
        if self.is_empty():
            self.__head = node
        elif self.one():
            self.__head.next = node
        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            cur.next = node
        node.next = self.__head
    
    # 指定位置添加元素, item为元素数据, place为添加的位置, 注意处理空链表的情况
    def insert(self, item, place):
        node = Node(item)
        # print(node.element)
        count = 0
        cur = self.__head
        if self.is_empty():
            self.__head = node
            node.next = self.__head
            self.__head = node
        elif place == 1:
            node.next = cur
            self.backed().next = node
            self.__head = node
        else:
            while cur:
                count += 1
                if count + 1 == place:
                    node.next = cur.next
                    cur.next = node
                    self.backed().next = self.__head
                    break
                cur = cur.next
        
    # 删除节点
    def remove(self, item):
        cur = self.__head
        print('---进入删除程序---')
        if self.is_empty():
            print('---链表为空---')
            return None
        else:
            # 判断此节点是否是头节点
            if cur.element == item:
                self.backed().next = cur.next
                self.__head = cur.next
                print('111')
            else:
                while cur.next != self.__head:
                    print('---正在判断---')
                    if cur.next.element == item:
                        print('---已删除元素"{0}"---'.format(item))
                        cur.next = cur.next.next
                        break
                    pre = cur
                    cur = cur.next
                if cur.element == item:
                    pre.next = self.__head
    
    # 查找结点是否存在
    def seach(self, item):
        cur = self.__head
        if self.is_empty():
            return False
        elif self.one() and cur.element == item:
            print('---"{0}"元素存在---'.format(item))
            return True
        while cur.next != self.__head:
            if cur.element == item or cur.next.element == item:
                print('---"{0}"元素存在---'.format(item))
                return True
            cur = cur.next
        print('---"{0}"元素不存在---'.format(item))
        return False

    def backed(self):
        cur = self.__head
        while cur.next != self.__head:
            cur = cur.next
        return cur

    def one(self):
        cur = self.__head
        if cur.next.element == cur.element:
            return True
        else:
            return False

if __name__ == "__main__":
    link = SingLink()
    print(link.is_empty())
    print(link.lenth())
    
    link.insert('haha', 1)
    # 在链表末尾添加元素
    link.travel()
    link.app('aa')
    link.travel()
    link.append('aaa')
    link.travel()

    link.append('aaaa')
    link.append('aaaaa')
    link.append('aaaaaa')
    # 在链表头添加元素
    link.app('bbbbbbb')
    link.travel()
    link.insert('insert', 1)
    link.travel()
    link.seach('aaa')
    link.remove('aaaaaa')
    
    # # 遍历链表
    link.travel()

