# @author: Nev8r
# @date: 2023-03-05 20:28:45
from inverse import inverse,gcd

def encode(plaintext,a,b):
    cipher = ""
    for word in plaintext:
        if word.isalpha():
            if word.isupper():
                cipher += chr(((ord(word) - 65) * a + b) % 26 + 65)
            else:
                cipher += chr(((ord(word) - 97) * a + b) % 26 + 97)
        else:
            cipher += word
    return cipher
def decode(cipher,a,b):
    ani = inverse(a,26)
    plaintext = ""
    for word in cipher:
        if word.isalpha():
            if word.isupper():
                plaintext += chr(((ord(word)-65-b) * ani) % 26 + 65)
            else:
                plaintext += chr(((ord(word)-97-b) * ani) % 26 + 97)
        else:
            plaintext += word
    return plaintext
def init():
    for i in range(0,25):
        if gcd(i,26) == 1:
            k_ls.append(i)
if __name__=='__main__':
    global k_ls
    k_ls = []
    init()
    print('''
    1. 加密
    2. 解密
    ''')
    op = int(input('do your choice:'))
    if op == 1:
        plaintext = input("input your plantext:")
        print("key's list")
        print(k_ls)
        a,b = map(int,input("input your key:").split())
        if a not in k_ls:
            print("illegal key")
            exit()
        cipher = encode(plaintext,a,b)
        print("after encode:")
        print(cipher)
    else:
        cipher = input('input your cipher: ')
        a,b = map(int,input("input your key:").split())
        plaintext = decode(cipher,a,b)
        print('after decrypt: ')
        print(plaintext)

