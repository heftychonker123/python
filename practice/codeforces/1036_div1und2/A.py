t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    if n == 1:
        print("no")
        continue
    
    sorted_arr = sorted(arr)
    mismatch = [arr[i] for i in range(n) if arr[i] != sorted_arr[i]]
    if len(mismatch)==0:
        print("no")
    else:
        print(len(mismatch))
        print(*mismatch)
