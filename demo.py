def findMaxOfArray(array): 
    maxnumber = array[0]
    for j in array: 
        if j > maxnumber:
            maxnumber = j

    return maxnumber



def findMinOfArray(array): 
    #TodDocl
    minnumber = array[0]
    for j in array: 
        if minnumber > j: 
            minnumber = j

    return minnumber
print(findMaxOfArray([1,2,10,4,6]))

print(findMinOfArray([1,2,10,4,6]))
