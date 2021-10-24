# defining the factorial function
def factorial(x):
    result = 1
    for i in range(1,x+1):
        result = result*i
    return result

# defining the function of probability as a function of x
def Prob(x):
    combination = (factorial(8)/(factorial(x)*factorial(8-x)))
    events_per_total = ((1/6)**x)*((5/6)**(8-x))
    return combination*events_per_total
    
# printing for each values
for i in range(4,8+1):
    print("P(x = {}) = ".format(i), end = "")
    print(Prob(i))
    
# sum over all possible x = 4 to x = 8
Probtotal = 0
print("The total Probability is ", end = "")
for i in range(4,8+1):
    Probtotal += Prob(i)
print(Probtotal)