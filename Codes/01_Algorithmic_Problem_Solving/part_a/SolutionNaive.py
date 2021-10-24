def solutionNaive(input):
    """
    find the minimum cost function with textfile input
    consists of size_of_A, MAX_DIFF, list of A
    
    input: string of textfile name (example: 'input.txt')
    format:
    =======
    size_of_A MAX_DIFF
    A_1
    A_2
    A_3
    ...
    =======
    example:
    =======
    4 10
    1
    5
    10
    13
    =======
    output: minimum cost function
    """
    
    f = open(input)
    i = 0
    A = []
    A_low = float("inf")
    A_high = 0
    for val in f:
        if i == 0:
            # assigning the size_of_A and the MAX_DIFF
            read_1 = val.split(" ")
            size_of_A, MAX_DIFF = int(read_1[0]), int(read_1[1])
            i = 1
        else:
            # Adding the row in text file into array
            A.append(int(val.strip("\n")))
            A_low = min(A_low,int(val))
            A_high = max(A_high,int(val))
            

    # define a big number for initializing the cost function
    cost = float("inf")

    # minB runs from A_low to A_high - 1
    for minB in range(A_low, A_high):
        # maxB runs from minB + 1 to the upper bound
        # of A_high
        for maxB in range(minB + 1, min(A_high, minB + MAX_DIFF) + 1):
            #calculating cost function for given minB and maxB
            cost_temp = 0
            B = A.copy()

            # assigning the 
            for A_i in range(0, len(A)):
                if A[A_i] < minB:
                    B[A_i] = minB
                elif A[A_i] > maxB:
                    B[A_i] = maxB
                cost_temp += (A[A_i] - B[A_i])*(A[A_i] - B[A_i])
            cost = min(cost, cost_temp)
    return cost

print("the minimum cost of the 'input.txt' is {}".format(solutionNaive("input.txt")))
print("the minimum cost of the 'input_extended.txt' is {}".format(solutionNaive("input_extended.txt")))
