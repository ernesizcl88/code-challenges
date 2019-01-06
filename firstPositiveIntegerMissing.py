def firstPositiveIntegerMissing(arr):
    for i in range(len(arr)):
        while 0 < arr[i] <= len(arr) and arr[i] != i + 1 and arr[arr[i] - 1] != arr[i]:
            current = arr[i]
            arr[i], arr[current - 1] = arr[current - 1], arr[i]

    for i in range(len(arr)):
        if arr[i] != i +1:
            return i + 1
    return len(arr) + 1



tests = [([7,6,4,2,1,3,5],5)]


for case, expected in tests:
    print(case, expected, firstPositiveIntegerMissing(case))