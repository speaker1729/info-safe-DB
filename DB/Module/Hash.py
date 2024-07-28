import hashlib


# 给一个字符串以字符串形式返回其哈希值
def sha(str):
    hash_object = hashlib.sha256(str.encode('utf-8'))
    hash_hex = hash_object.hexdigest()
    return hash_hex


if __name__ == '__main__':
    res = sha('123')
    print(res)
    print(type(res))
    print(len(res))
