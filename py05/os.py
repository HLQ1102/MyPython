import os

print(os.getcwd())
# os.mkdir('/tmp/demo')
os.chdir('/tmp/demo')
print(os.getcwd())
# os.rename('1.txt', '2.txt')
os.chdir('/tmp/demo/')
print(os.getcwd())
