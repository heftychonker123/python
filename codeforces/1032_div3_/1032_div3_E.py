t=int(input())
ans_arr=[]
for _ in range(t):
    ans=0
    l,r=(input().split())
    t=0
    for m in range(len(l)):
        t=min(10+int(r[m])-int(l[m]),abs(int(r[m])-int(l[m])))
        if int(l[m])==1 and int(r[m])==1:
            ans+=2
        if t==1:
            ans+=1
    ans_arr.append(ans)
print(*ans_arr)