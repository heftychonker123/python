t=int(input())
for _ in range(t):
    x=input()
    ans=10
    for l in x:
        ans=min(int(l),ans)
    print(ans)