t=int(input())
for _ in range(t):
    n=int(input())
    if n%2==0:
        for l in range(1,n,2):
            print(l,end=" ")
        for t in range(n,0,-2):
            print(t,end=" ")
    else:
        for t in range(2,n,2):
            print(t,end=" ")
        for l in range(n,-1,-2):
            print(l,end=" ")