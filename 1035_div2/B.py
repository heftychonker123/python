t=int(input())
for _ in range(t):
    answer=True
    n=int(input())
    px,py,qx,qy=[int(i) for i in input().split()]
    #Euclidian distance^2 of 2 given point
    dis=(((px-qx)**2) +((py-qy)**2))**0.5
    arr=[int(i) for i in input().split()]
    if dis>sum(arr):
        answer=False
    for i in range(n):
        if dis+sum(arr)<2*arr[i]:
            answer=False
            break
    if answer:
        print("yes")
    else:
        print("no")