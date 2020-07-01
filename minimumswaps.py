def minimumSwaps(arr):
    i, swap = -1, 0
    while i <len(arr)-1:
        i += 1
        if arr[i] == i+1:
            continue
        j = arr[i]-1
        arr[j], arr[i] = arr[i], arr[j]
        swap += 1
        i -= 1
    return swap


n = int(input())
arr = list(map(int, input().rstrip().split()))
res = minimumSwaps(arr)
print(res)