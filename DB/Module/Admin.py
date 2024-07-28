from . import RSA
from . import AES
from . import Hash
from . import File


# 注册管理员
def create(password):
    # 生成RSA密钥对
    p = RSA.Prime_Generate(512)
    q = RSA.Prime_Generate(512)
    n, e, d = RSA.Key_Generate(p, q)
    # RSA-1024
    n_b = n.to_bytes(1024, 'big')
    e_b = e.to_bytes(1024, 'big')
    d_b = d.to_bytes(1024, 'big')
    # 管理员密钥
    key = bytes.fromhex(Hash.sha(password))
    # 加密形式存储私钥
    pri = open('Admin/admin.pri', 'wb')
    pri.write(AES.encrypt(key, n_b + d_b))
    pri.close()
    # 明文存储公钥
    pub = open('Admin/admin.pub', 'wb')
    pub.write(n_b + e_b)
    pub.close()


# 导入公钥
def pub():
    # 导入公钥
    pub = open('Admin/admin.pub', 'rb')
    n = int.from_bytes(pub.read(1024), 'big')
    e = int.from_bytes(pub.read(1024), 'big')
    pub.close()
    return e, n


# 导入公钥
def pri(key):
    # 导入私钥
    pri = open('Admin/admin.pri', 'rb')
    file = AES.decrypt(key, pri.read())
    # 切片操作 左闭右开
    n = int.from_bytes(file[:1024], 'big')
    d = int.from_bytes(file[1024:], 'big')
    pri.close()
    return d, n


# 保存用户的密钥
def save_key(username, password):
    # 导入公钥
    e, n = pub()
    # 将用户密钥转换为整数
    message = int.from_bytes(password.encode('utf-8'), 'big')
    # 写公钥加密后的用户密钥
    key = open('Admin/key/' + username, 'w')
    key.write(hex(RSA.Encrypt(message, e, n)))
    key.close()


# 导入用户密钥
def load_key(username, password):
    # 管理员密钥
    key = bytes.fromhex(Hash.sha(password))
    # 导入私钥
    d, n = pri(key)
    # 导入加密后的用户密钥
    file = open('Admin/key/' + username, 'r')
    message = int(file.read(), 16)
    file.close()
    # 解密
    key = bytes.fromhex(hex(RSA.Decrypt(message, d, n))[2:])
    key = key.decode('utf-8')
    return key


# 在管理员文件夹内注册文件
def up(filename, key):
    # 导入公钥
    e, n = pub()
    # 将文件密钥转换为整数
    message = int.from_bytes(key.encode('utf-8'), 'big')
    # 将文件名与其密钥保存
    file = open('Admin/dat/' + filename, 'w')
    file.write(hex(RSA.Encrypt(message, e, n)))
    file.close()


# 在管理员文件夹内读取文件密钥
def down(filename, password):
    # 管理员密钥
    key = bytes.fromhex(Hash.sha(password))
    # 导入私钥
    d, n = pri(key)
    # 导入加密后的文件密钥
    file = open('Admin/dat/' + filename, 'r')
    message = int(file.read(), 16)
    file.close()
    # 解密
    key = bytes.fromhex(hex(RSA.Decrypt(message, d, n))[2:])
    key = key.decode('utf-8')
    return key


# 管理员访问所有文件
def load_list(password):
    data_list = File.get_all('Data')
    dat_list = File.get_all('Admin/dat')
    files = [file for file in data_list if file in dat_list]
    res = []
    for file in files:
        res.append([file, down(file, password)])
    return res
