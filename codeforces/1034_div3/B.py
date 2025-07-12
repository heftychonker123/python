t=int(input())
for _ in range(t):
    n,j,k=(int(i) for i in input().split())
    arr=[int(i) for i in input().split()]
    z=arr[j-1]
    state=True
    arr.sort(reverse=True)
    if k==1:
        state=(z==arr[0])
    if state:
        print("YES")
    else:
        print("NO")