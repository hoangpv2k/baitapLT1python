import math
def fatorial(n):
    if n==0 : return 1
    return n * fatorial(n-1)
def prob(n p,r):
    ssumprob = fatorial(n) / (fatorial(n - r + 1) * fatorial(r - 1) * math.pow(2, n))
    return ssumprob
def infoMeasure(n, p, r):
    tong = prob(n,p,r)
    suminfo = - (math.log10(tong) / math.log10(2))
    return suminfo
def sumProb(N, p, r):
'''
trả về giá trị là tổng xác suất các symbol khi n đủ lớn sẽ tiến đến 1
'''
    sum = 0
    for i in range(1,N+1):
        sum += prob(i, p, r)
    return sum
def approxEntropy(N, p, r):
'''
trả về giá trị trung bình lượng tin các symbol
sum=-p(1).log(p1)...-p(N).log(p(N)) khi N đủ lớn sum sẽ tiến gần entropy nguồn tin

'''
    sum = 0
    for i in range(0, N):
        sum += prob(i, p, r) * infoMeasure(i,p,r)
    return sum

print(prob(3, 1/2, 50))
#print(infoMeasure(n, p, r))
#print(sumProb(N, p, r))
#print(approxEntropy(N, p, r))
