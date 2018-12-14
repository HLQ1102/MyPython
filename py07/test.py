# import time


# print(time.time())



import tarfile
import os

# tar = tarfile.open('/tmp/security.tar.gz', 'w:gz')
# os.chdir('/etc')
# tar.add('security')
# os.mkdir('/tmp/demo')
# tar = tarfile.open('/tmp/security.tar.gz', 'r:gz')
# tar.extractall(path='/tmp/demo')
# tar.close()
# tar = tarfile.open('/tmp/www.tar.gz', 'w:gz')
# tar.add('/etc/passwd')
# tar.close()
#
# for path, folders, files in os.walk('/tmp/demo'):
#     for file in files:
#         print(os.path.join(path, file))
#

class Vendor:
    def __init__(self, phone):
        self.phone = phone

class BearToy:
    def __init__(self, size, color):
        self.size = size
        self.color = color
        self.vendor = Vendor('123-123-123')

class NewBearToy(BearToy):    # 括号中填入的是父类,基类
    def __init__(self, name, size, color):
        # BearToy.__init__(self, name, size, color)
        super(NewBearToy, self).__init__(size, color)
        self.name = name
    def walk(self):
        print('I can walk')
    def name(self0):
        print()

if __name__ == '__main__':
    bear_big = BearToy( 'LL', 'Brown')
    # print(bear_big.size)
    # print(bear_big.vendor.phone)
    bear2 = NewBearToy('dada2', 'Middle', 'Brown')
    print(bear2.vendor.phone)
    print(bear2.walk())
    print(' ')
