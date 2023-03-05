def exgcd(a,b,x,y):
    if b==0:
        return a,1,0
    # ax + by = bx1+(a%b)y1
    # ax + by = ay1+b(x1-a//b*y1)
    d,x1,y1=exgcd(b,a%b,x,y)
    return d,y1,x1-(a//b)*y1
if __name__ == '__main__':
    print(exgcd(77,2,1,1))