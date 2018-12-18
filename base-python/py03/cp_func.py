import sys
import os

def copy(src_dir = '/etc/passwd', dst_dir = '/tmp/pass'):
    log = True
    with open(src_dir, 'rb') as src_fobj:
            with open(dst_dir, 'wb') as dst_fobj:
                while log:
                    data = src_fobj.read(4096)
                    if not data:
                        log = False
                        continue
                    dst_fobj.write(data)
                else:
                    os.chmod(dst_dir, 755)
# copy(sys.argv[1], sys.argv[2])

def qq(n = 2):
    print('*' * n)
qq(sys.argv[1])