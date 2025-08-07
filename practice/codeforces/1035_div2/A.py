t=int(input())
for _ in range(t):
    a,b,x,y=[int(i) for i in input().split()]
    if a==b:
        print(0)
    elif a>b:
        if a%2==0:
            print(-1)
        elif a%2!=0:
            if a==b+1:
                print(y)
            else:
                print(-1)
    elif a<b:
        if x<=y:
            print(x*(b-a))
        else:
            if a%2!=0:
                if (b-a)%2==0:
                    print((x+y)*(b-a)//2)
                else:
                    print(x +(x+y)*(b-a-1)//2)
            else:
                if (b-a)%2==0:
                    print((x+y)*(b-a)//2)
                else:
                    print(y +(x+y)*(b-a-1)//2)