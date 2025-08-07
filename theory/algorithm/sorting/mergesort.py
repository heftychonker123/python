def merge(a, b):
    answer = []
    i, j = 0, 0

    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            answer.append(a[i])
            i += 1
        else:
            answer.append(b[j])
            j += 1

    answer.extend(a[i:])
    answer.extend(b[j:])
    return answer

def mergesort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr) // 2
        left = mergesort(arr[:mid])   # sort the left half
        right = mergesort(arr[mid:])  # sort the right half
        return merge(left, right)     # merge the sorted halves
print(mergesort([5, 3, 8, 1, 4, 7]))