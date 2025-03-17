count = 0
result = -1

def merge_sort(arr, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(arr, p, q)
        merge_sort(arr, q+1, r)
        merge(arr, p, q, r)

def merge(arr, p, q, r):
    global count, result, k
    i = p
    j = q + 1
    tmp = []
    while i <= q and j <= r:
        if arr[i] <= arr[j]:
            tmp.append(arr[i])
            i += 1
        else:
            tmp.append(arr[j])
            j += 1

    while i <= q:
        tmp.append(arr[i])
        i += 1

    while j <= r:
        tmp.append(arr[j])
        j += 1

    for idx in range(len(tmp)):
        arr[p+idx] = tmp[idx]
        count += 1
        if count == k:
            result = arr[p+idx]

def main():
    global k, result
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    merge_sort(arr, 0, n-1)
    print(result)

if __name__ == "__main__":
    main()