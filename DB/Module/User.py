from . import File
from . import Hash
from . import AES


# 注册用户
def registry(username, password):
    # 如果不注册管理员则拒绝注册其它用户
    if username != 'admin':
        if not File.is_exist('Users/sha', 'admin'):
            return '管理员不存在'
    if File.is_exist('Users/sha', username):
        return '用户已存在'
    # 使用哈希存储用户名和密码便于验证身份以及保护用户信息
    user = Hash.sha(username + password)
    # 将用户数据写入特定文件夹与其同名的文件
    path = 'Users/sha/' + username
    open(path, 'w').write(user)
    return '注册成功'


# 用户登录
def login(username, password):
    # 检测是否存在该用户
    if not File.is_exist('Users/sha', username):
        return '不存在该用户'
    # 打开文件并读取
    path = 'Users/sha/' + username
    f = open(path, 'r')
    user = f.read()
    f.close()
    # 校验哈希值是否相等
    if user == Hash.sha(username + password):
        return '登录成功'
    else:
        return '密码错误'


# 导入用户的可访问文件
def load(username, password):
    # 打开待读取文件
    path = 'Users/lis/' + username
    f = open(path, 'rb')
    # 创建密钥
    key = bytes.fromhex(Hash.sha(password))
    # 解密文件
    lis = AES.decrypt(key, f.read()).decode('utf-8')
    user_list = lis.split('\n')
    f.close()
    # 如果为空返回空
    if len(user_list) == 1:
        return []
    # 返回用户的可访问文件
    else:
        user_list.pop(-1)
        return [user_list[i:i + 2] for i in range(0, len(user_list), 2)]


# 存储用户的可访问文件
def save(username, password, user_list):
    # 打开待写入文件
    path = 'Users/lis/' + username
    f = open(path, 'wb')
    # 创建密钥
    key = bytes.fromhex(Hash.sha(password))
    # 将列表中的文件全合并
    lis = ''
    for file in user_list:
        for item in file:
            lis += item + '\n'
    # 加密后写入
    f.write(AES.encrypt(key, lis.encode('utf-8')))
    f.close()


if __name__ == '__main__':
    print(registry('admin', '123'))
    print(login('admin', '123'))
