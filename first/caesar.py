def encrypt(plaintext,key):
    cipher = ''
    for word in plaintext:
        if word.isalpha():
            if word.isupper():
                cipher += chr((ord(word) - 65 + key) % 26 + 65)
            else:
                cipher += chr((ord(word) - 97 + key) % 26 + 97)
        else:
            cipher += word
    return cipher
def decrypt(cipher,key):
    return encrypt(cipher,26-key)
if __name__ == '__main__':
    print('''
    1. 加密
    2. 解密
    ''')
    op = int(input('do your choice:'))
    if op == 1:
        plaintext = input('input your plaintext: ')
        key = int(input('input your key: '))
        cipher = encrypt(plaintext,key)
        print('after encrypt:')
        print(cipher)
    else:
        cipher = input('input your cipher: ')
        key = int(input('input your key: '))
        plaintext = decrypt(cipher,key)
        print('after decrypt: ')
        print(plaintext)