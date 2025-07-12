t=int(input())
import math
for _ in range(t):
    k=int(input())
    answer=10**18+10**9
    low=k
    high=10**18+10**9
    while high>low:
        mid=low +(high-low)//2
        if mid-int(math.sqrt(mid))<k:
            low=mid+1
        elif mid-int(math.sqrt(mid))>k:
            high=mid
        else:
            high=mid
            answer=min(answer,mid)
    print(answer)