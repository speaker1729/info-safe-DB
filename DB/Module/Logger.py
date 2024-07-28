from . import Admin
from . import RSA
from . import File
from . import Hash
import datetime


def log_save(log):
    # 导入公钥
    e, n = Admin.pub()
    # 将文件日志转换为整数
    message = int.from_bytes(log.encode('utf-8'), 'big')
    # 将文件名与其密钥保存
    filename = date()
    file = open('Admin/log/' + filename, 'w')
    file.write(hex(RSA.Encrypt(message, e, n)))
    file.close()


def log_load(password):
    if File.is_empty('Admin/log'):
        return []
    else:
        res = []
        files = File.get_all('Admin/log')
        # 管理员密钥
        key = bytes.fromhex(Hash.sha(password))
        # 导入私钥
        d, n = Admin.pri(key)
        for filename in files:
            # 导入加密后的文件密钥
            file = open('Admin/log/' + filename, 'r')
            message = int(file.read(), 16)
            file.close()
            # 解密
            log = bytes.fromhex(hex(RSA.Decrypt(message, d, n))[2:])
            # 解密
            # num = RSA.Decrypt(message, d, n)
            # log = num.to_bytes(num.bit_length()//8+1,'big')
            log = log.decode('utf-8')
            res.append([filename, log])
        return res


def date():
    now_time = datetime.datetime.now()
    format_time = now_time.strftime('%Y-%m-%d %H-%M-%S')
    return format_time


if __name__ == '__main__':
    print(date())
