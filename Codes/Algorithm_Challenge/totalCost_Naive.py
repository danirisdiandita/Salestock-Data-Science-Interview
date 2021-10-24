def totalCost(scores):
    answer = 10*len(scores)
    for i in range(len(scores)):
        for j in range(0,i):
            if scores[i] > scores[j]:
                answer += 1
    return answer

scores = [1874, 1339, 5617, 8331, 5424, 9667]

print(totalCost(scores))

scores = [1675, 4660, 7028, 8022, 2529, 3270, 2472, 420, 3024, 5501,
4647, 313, 3568, 4105, 7372, 8680, 1966, 3952, 5320, 7663,
2828, 5868, 286, 9149, 7979, 6050, 1070, 5388]

print(totalCost(scores))