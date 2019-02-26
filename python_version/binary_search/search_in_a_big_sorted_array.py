
def searchBigSortedArray(A, target):
    start, end = 0,1
    while A[end] < target:
        end *= 2
    mid = start + (end - start) // 2
    while start + 1 < end:
        if A[mid] < target:
            start = mid
        else:
            end = mid

    if A[start] == target:
        return start
    elif A[end] == target:
        return end
    else:
        return -1


if __name__ == "__main__":
    import random
    array = []
    for i in range(10000):
        array.append(int(random.random() * 10000))
        array.sort()
    target = 17
    print(searchBigSortedArray(array, target))
