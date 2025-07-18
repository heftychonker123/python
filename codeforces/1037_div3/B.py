t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    i = 0
    ans = 0
    while i < n:
        found = False
        for l in range(i, min(n, i + k)):
            if arr[l] == 1:
                found = True
                i = l + 1
                break
        if not found:
            ans += 1
            i += k+1
    print(ans)
