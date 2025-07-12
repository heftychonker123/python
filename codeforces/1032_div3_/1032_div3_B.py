t=int(input())
answer_arr=[]
for i in range(t):
    n=int(input())
    s=input()
    state=False
    for l in range(n-2):
        a,b,c=s[:l+1],s[l+1],s[l+2:]
        if b in (a+c):
            state=True
            break
    if state==True:
        answer_arr.append("yes")
    else:
        answer_arr.append("no")
print(*answer_arr)