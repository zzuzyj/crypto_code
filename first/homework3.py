
# @author: Nev8r
# @date: 2023-03-07 23:10:02
from affine import decode

if __name__=='__main__':
    cipher = "gzyyf"
    text = "he"
    for a in range(26):
        for b in range(26):
            plaintext = decode(cipher,a,b)
            if(plaintext[:2]==text):
                print(plaintext)
                break
                
