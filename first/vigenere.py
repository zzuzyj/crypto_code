def encrypt(plaintext,key):
    cipher = ''
    key_len = len(key)
    for i in range(len(plaintext)):
        if plaintext[i].isalpha():
            if plaintext[i].isupper():
                cipher += chr((ord(plaintext[i]) - 65 + ord(key[i%key_len])-65) % 26 + 65)
            else:
                cipher += chr((ord(plaintext[i]) - 97 + ord(key[i%key_len])-97) % 26 + 97)
        else:
            cipher += plaintext[i]
    return cipher
def decrypt(cipher,key):
    key_inv = ''
    for word in key:
        if word.isalpha():
            if word.isupper():
                key_inv += chr(26-(ord(word)-65)+65)
            else:
                key_inv += chr(26-(ord(word)-97)+97)
        else:
            key_inv +=word
    return encrypt(cipher,key_inv)
if __name__ == '__main__':
    print('''
    1. 加密
    2. 解密
    ''')
    op = int(input('do your choice:'))
    if op == 1:
        plaintext = input('input your plaintext: ')
        key = input('input your key: ')
        cipher = encrypt(plaintext,key)
        print('after encrypt:')
        print(cipher)
    else:
        cipher = input('input your cipher: ')
        key = input('input your key: ')
        plaintext = decrypt(cipher,key)
        print('after decrypt: ')
        print(plaintext)