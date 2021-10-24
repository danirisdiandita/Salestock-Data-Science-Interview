def Prob(n, k):
    if k == 1 and n == 1:
        return 1
    elif k == 0:
        return 0
    elif k > n:
        return 0
    if n == 0:
        return 0
    else:
        return Prob(n-1,k)*k/6 + Prob(n-1,k-1)*(7-k)/6

expectation = 0
for i in range(1,6+1):
    expectation += i * Prob(6,i)
    
print("The expectation value is {}".format(expectation))