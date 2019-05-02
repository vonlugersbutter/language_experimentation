# finding pair that give set sum within a list

# original way

import sys

arr = [8,7,2,5,3,1]
sums = 10

sum_found = False

while sum_found == False:
    for i in range(0, len(arr),1):
        add = arr[1] + arr[i]
        if add == sums:
            print(arr[1],arr[i])
            sum_found = True

# naive way

def find_pair(arr, n, sums):
    for i in range(0,n-1,1):
        for j in range(i+1,n,1):
            if (arr[i] + arr[j]) == sums:
                print("Pair found for " + str(arr[i]) + str(arr[j]))
                return
    print("Pair not found")
    return

n = sys.getsizeof(arr)/sys.getsizeof(arr[0])
find_pair(arr,int(n),sums)

# good way using sorting

def find_pair_sort(arr,sums):
    arr.sort()
    low = 0
    high = len(arr)-1

    while low < high:
        if arr[low] + arr[high] == sums:
            print("Pair found")
            return
        if arr[low] + arr[high] < sums:
            low += 1
        elif arr[low] + arr[high] > sums:
            high -= 1
    
    print("Pair not found.")

find_pair_sort(arr,sums)
        
