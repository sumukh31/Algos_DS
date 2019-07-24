import collections
def missing_element(arr1,arr2):
    count = collections.defaultdict(int)

    for num in arr2:
        count[num] += 1
    for num in arr1:
        if count[num] == 0:
            return num
        else:
            count[num] -= 1

arr1 = [1,2,3,3]
arr2 = [1,2,3]

missing = missing_element(arr1,arr2)
print (missing)
