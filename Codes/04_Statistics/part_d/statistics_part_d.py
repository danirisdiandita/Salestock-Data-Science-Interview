import random 

sum_within_range = 0
sum_outside_range = 0
iterator = 0
probability = 1
while True:
    sum = 0
    for i in range(10000):
        sum += random.randint(1,6)
    if 34500 <= sum <= 35500:
        sum_within_range += 1
    else:
        sum_outside_range += 1
    probability = (sum_within_range / (sum_within_range + sum_outside_range))
    iterator += 1
    if iterator % 50 == 0:
        print("probability = {}, iteration = {}".format(probability, iterator))
    if iterator == 10000:
        break