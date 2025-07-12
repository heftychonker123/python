t=int(input())
for i in range(t):
    a,x,y=[int(i) for i in input().split()]
    if (x>=a and a>=y) or ( x<=a and a<=y):
        print("NO")
    else:
        print("YES")