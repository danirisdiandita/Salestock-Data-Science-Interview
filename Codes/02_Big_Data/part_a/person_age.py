# initializing mergesort for sorting purpose
def mergeSort(A):
    def merge(left, right): # [1,2,9,8] and [3,6,5]
        result = []
        i, j = 0, 0
        while i< len(left) and j < len(right):
            if left[i].lower() < right[j].lower():
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

# initialize the input phone and age as a text
F = open("person_age.txt")

# creating temporary textfiles per age of the phone
for i in range(1,120+1):
    f = open("tempfile/person_age_{0:03}.txt".format(i), "a")
    f.close()

for row in F:
    row = row.split(" ")
    age = int(row[1].strip("\n"))
    name = row[0]
    G = open("tempfile/person_age_{0:03}.txt".format(age), "a")
    G.write(name + "\n")
G.close()

# sorting the names inside each textfile using mergesort
# and rewrite everything the sorted names into 
# new textfiles

for i in range(1,120+1):
    with open("tempfile/person_age_{0:03}.txt".format(i)) as f:
        with open("tempfile/sorted_person_age_{0:03}.txt".format(i), "w") as g:
            for row in mergeSort(f.read().split("\n")[:-1]):
                g.write("{}\n".format(row))


# combining all of the sorted textfile by age and name into one file
with open("sorted_person_age.txt", "w") as finalsorted:
    for i in range(1, 120+1):
        with open("tempfile/sorted_person_age_{0:03}.txt".format(i)) as f:
            names = f.read().split("\n")[:-1]
            for name in names:
                finalsorted.write("{} {}\n".format(name, i))

                
# delete all of temporary textfiles to save memory
import os
for i in range(1,120+1):
    os.remove("tempfile/person_age_{0:03}.txt".format(i))
    os.remove("tempfile/sorted_person_age_{0:03}.txt".format(i))