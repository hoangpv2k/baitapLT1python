import math
def prob(n, p): 
  return (1-p)**(n-1)*p

def infoMeasure(n, p):
  info = prob(n, p)
  return - math.log2(info)
def sumProb(N, p):
'''
Trả về giá trị là tổng các xác xuất của symbol từ 1 đến N
sum = p(1)+ p(2) + .. + P(N) 
sum = (1-p)*[1 + p + p^2 + ...] = (1-p)*1/(1-p) = 1
khi N đủ lớn sum sẽ tiến gần đến 1
'''
  sum = 0
  for i in range(1, N):
    sum += prob(i, p)
  return sum

def approxEntropy(N, p):
  app = 0
  for i in range(1, N):
    app += prob(i, p) * infoMeasure(i, p)
  return app

if __name__ == "__main__":
  """
    Test function
  """
print(prob(3,1/2))
#print(infoMeasure(3,1/2))
#print(sumProb(3,1/2))
#print(approxEntropy(3,1/2))
