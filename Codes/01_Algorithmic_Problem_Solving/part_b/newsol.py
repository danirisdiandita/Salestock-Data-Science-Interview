def mergeSort(A):
    def merge(left, right): # [1,2,9,8] and [3,6,5]
        result = []
        i, j = 0, 0
        while i< len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result += left[i:]
        result += right[j:]
        return result
    if len(A) <= 1:
        return A
    mid = len(A) // 2
    lefthalf = mergeSort(A[:mid])
    righthalf = mergeSort(A[mid:])
    return merge(lefthalf, righthalf)
def solutionNotSoNaive(input):
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
            # Adding the 
            A.append(int(val))
            A_low = min(A_low,int(val))
            A_high = max(A_high,int(val))
            
    # sorting A using mergesort
    A = mergeSort(A)
    # initialize B
    B = A.copy()
    
    # the middle between minB and maxB is the average of A
    
    minB = sum(A) // len(A)
    maxB = minB + MAX_DIFF
    
    # first scan at the middle to determine the difference 
    # in the cost function
    
    cost = 0
    for A_index in range(len(A)):
        if A[A_index] < minB:
            B[A_index] = minB
            cost += (A[A_index] - B[A_index])*(A[A_index] - B[A_index])
        elif A[A_index] > maxB:
            B[A_index] = maxB
            cost += (A[A_index] - B[A_index])*(A[A_index] - B[A_index])
    
    # scanning by going down
    # initialize newcost as a temporary variable
    newcost = 0
    # initializing B
    B = A.copy()
    # initializing new minB and maxB as temporary variables
    minBnew = minB
    maxBnew = maxB
    while True:
        minBnew -= 1
        maxBnew -= 1
        for A_index in range(len(A)):
            if A[A_index] < minBnew:
                B[A_index] = minBnew
                newcost += (A[A_index] - B[A_index])*(A[A_index] - B[A_index])
            elif A[A_index] > maxBnew:
                B[A_index] = maxBnew
                newcost += (A[A_index] - B[A_index])*(A[A_index] - B[A_index])
        # updating the cost, if the newcost is smaller
        if newcost < cost:
            cost = min(cost, newcost)
            newcost = 0
        elif newcost > cost:
            break
        elif minBnew == A_low:
            break
            
    # scanning by going up
    # initialize newcost as a temporary variable
    newcost = 0
    # initializing B
    B = A.copy()
    # initializing new minB and maxB as temporary variables
    minBnew = minB
    maxBnew = maxB
    while True:
        minBnew += 1
        maxBnew += 1
        for A_index in range(len(A)):
            if A[A_index] < minBnew:
                B[A_index] = minBnew
                newcost += (A[A_index] - B[A_index])*(A[A_index] - B[A_index])
            elif A[A_index] > maxBnew:
                B[A_index] = maxBnew
                newcost += (A[A_index] - B[A_index])*(A[A_index] - B[A_index])
        # updating the cost, if the newcost is smaller
        if newcost < cost:
            cost = min(cost, newcost)
            newcost = 0
        elif newcost > cost:
            break
        elif minBnew == A_low:
            break
    return cost

print("The minimum cost for the 'input.txt' is {}".format(solutionNotSoNaive("input.txt")))
print("The minimum cost for the 'input_extended.txt' is {}".format(solutionNotSoNaive("input_extended.txt")))
