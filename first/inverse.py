
# @author: Nev8r
# @date: 2023-03-05 12:48:00
from exgcd import exgcd
def gcd(a,b):
    return a if b==0 else gcd(b,a%b)
def quick_pow(a,b,mod):
    res = 1
    while b:
        if b&1:
            res = res*a%mod
        b>>=1
        a = a * a %mod
    return res
def small_fermat(a,p):
    return quick_pow(a,p-2,p)
def inverse(p,m):
    if gcd(p,m)!=1:
        # print("no inverse")
        return 0
    return exgcd(p,m,1,1)[1]
    # return small_fermat(p,m) 只能用于m是素数的情况
if __name__=='__main__':
    print(inverse(3,26))