import random


def gcd(a, b):
    if a < b:
        a, b = b, a
    while b:
        a, b = b, a % b
    return a


def Is_Prime(n):
    d = n - 1
    r = 0
    while not (d & 1):
        r += 1
        d >>= 1

    for _ in range(5):
        a = random.randint(2, n - 2)

        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue

        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == 1:
                return False
            if x == n - 1:
                break
        else:
            return False

    return True


def Extended_Eulid(a: int, m: int) -> int:
    x = 0
    lx = 1
    om = m
    while m != 0:
        q = a // m
        (a, m) = (m, a % m)
        (x, lx) = ((lx - (q * x)), x)
    if lx < 0:
        lx += om
    return lx


def Prime_Generate(num_size: int) -> int:
    key_min = pow(2, num_size - 1)
    key_max = pow(2, num_size)
    while True:
        num = random.randrange(key_min, key_max)
        num = num | 1
        if Is_Prime(num):
            return num


def Key_Generate(p: int, q: int):
    e = random.randint(1, (p - 1) * (q - 1))
    while gcd(e, (p - 1) * (q - 1)) != 1:
        e = random.randint(1, (p - 1) * (q - 1))
    n = p * q
    d = Extended_Eulid(e, (p - 1) * (q - 1))
    return n, e, d


def Encrypt(message: int, e: int, n: int) -> int:
    ciphertext = pow(message, e, n)
    return ciphertext


def Decrypt(ciphertext: int, d: int, n: int) -> int:
    plaintext = pow(ciphertext, d, n)
    return plaintext
