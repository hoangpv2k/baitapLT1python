import math
def factoril(n):
    if n==0: return 1
    return n*factoril(n-1)

def prob(n,p,N):
    ssumprob=(factoril(N) / (factoril(n)*factoril(N-n) ))*math.pow(p,n)*math.pow(1-p,N-n)
    return ssumprob

def infoMeasure(n,p,N):
    tong=prob(n,p,N)
    return -math.log2(tong)

def sumprob(N,p):
#trả về giá trị là tổng các xác suất của symlol sum=p(1)+..p(N) xấp xỉ 1
    tong2=0
    for i in range(0,N):
        tong2+=prob(i,p,N)
    return tong2

def approEntropy(N, p):
    app=0
    for i in range(0,N):
        app+=prob(i,p,N) * infoMeasure(i,p,N)
    return app
print(prob(3,1/2,50))
#print(infoMeasure(n,p,N))
#print(sumprob(N,p))
#print(appoxEntropy(N,p))
