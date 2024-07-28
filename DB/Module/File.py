import os
from . import AES
from . import Hash


def get_all(folder):
    path = folder
    files = os.listdir(path)
    return files


def is_empty(folder):
    path = folder
    files = os.listdir(path)
    if len(files):
        return False
    else:
        return True


def is_exist(folder, file):
    path = folder
    files = os.listdir(path)
    if file in files:
        return True
    else:
        return False


# 给出密钥及文件名 上传文件
def up(file, key):
    path = 'Input/'
    files = os.listdir(path)
    if file not in files:
        return '文件不存在'
    if is_exist('Data', file):
        return '文件夹已有'
    else:
        # 生成密钥
        key = bytes.fromhex(Hash.sha(key))
        defile = open(path + file, 'rb')
        enfile = AES.encrypt(key, defile.read())
        defile.close()
        res = open('Data/' + file, 'wb')
        res.write(enfile)
        res.close()
        return '上传成功'


# 给出密钥及文件名 下载文件
def down(file, key):
    path = 'Data/'
    files = os.listdir(path)
    if file not in files:
        return '文件不存在'
    if is_exist('Output', file):
        return '输出区已有'
    else:
        # 生成密钥
        key = bytes.fromhex(Hash.sha(key))
        enfile = open(path + file, 'rb')
        defile = AES.decrypt(key, enfile.read())
        enfile.close()
        res = open('Output/' + file, 'wb')
        res.write(defile)
        res.close()
        return '下载成功'


# 过滤留下用户可见的文件
def filter(user_list):
    data_list = get_all('Data')
    # 输入的列表至少有一个元素
    if not user_list:
        return []
    else:
        return [file for file in user_list if file[0] in data_list]


if __name__ == '__main__':
    # print(is_empty('Users'))
    # print(is_exist('Users','123'))
    key = bytes.fromhex("000102030405060708090a0b0c0d0e0f")
    plaintext = bytes.fromhex("00112233445566778899aabbccddeeff")
    print(up('test', key))
    print(down('test', key))
    pass
