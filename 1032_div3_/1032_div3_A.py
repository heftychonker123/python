t=int(input())
for _ in range(t):
    n,s=(int(i) for i in input().split())
    arr=[int(i) for i in input().split()]
    if n==1:
        print(abs(arr[0]-s))
    else:
        print(min(abs(arr[n-1]-s),abs(arr[0]-s))+arr[n-1]-arr[0])