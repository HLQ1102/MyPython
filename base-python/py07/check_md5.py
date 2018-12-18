import sys
import hashlib

def check_md5(fnam):
    m = fnam
    x = hashlib.md5()
    with open(m, 'rb') as f:
        while True:
            data = f.read(4096)
            if not data:
                break
            x.update(data)
    return x.hexdigest()

if __name__ == '__main__':
    print(check_md5(sys.argv[1]))

