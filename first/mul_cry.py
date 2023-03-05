# @author: Nev8r
# @date: 2023-03-05 20:28:45
from inverse import inverse,gcd

def encode(plaintext,key):
    cipher = ""
    for word in plaintext:
        if word.isalpha():
            if word.isupper():
                cipher += chr(((ord(word) - 65) * key) % 26 + 65)
            else:
                cipher += chr(((ord(word) - 97) * key) % 26 + 97)
        else:
            cipher += word
    return cipher
def decode(c,key):
    return encode(c,inverse(key,26))

if __name__=='__main__':
    # y=k*x%26
    k_ls = []
    for i in range(0,25):
        if gcd(i,26) == 1:
            k_ls.append(i)
    # print(k_ls)
    print('''
    1. 加密
    2. 解密
    ''')
    op = int(input('do your choice:'))
    if op == 1:
        plaintext = input("input your plantext:")
        print("key's list")
        print(k_ls)
        key = int(input("choose your key:"))
        if key not in k_ls:
            print("illegal key")
            exit()
        cipher = encode(plaintext,key)
        print("after encode:")
        print(cipher)
    else:
        cipher = input('input your cipher: ')
        key = int(input('input your key: '))
        plaintext = decode(cipher,key)
        print('after decrypt: ')
        print(plaintext)

