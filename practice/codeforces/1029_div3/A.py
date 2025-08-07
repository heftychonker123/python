t=int(input())
ans=[]
for _ in range(t):
    n,t=[int(i) for i in input().split()]
    arr=[int(i) for i in input().split()]
    x=n
    y=0
    for i in range(n):
        if arr[i]==1:
            x=min(x,i)
            y=max(y,i)
    if (t>=y-x+1):
        print("YES")
    else:
        print("NO")