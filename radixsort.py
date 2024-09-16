def countingSortForRadix(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in range(n - 1, -1, -1):
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1

    for i in range(n):
        arr[i] = output[i]

def radixsort(arr):
    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:
        countingSortForRadix(arr, exp)
        exp *= 10
    return arr

arr = [170, 45, 75, 90, 802, 24, 2, 66]
print(radixsort(arr))