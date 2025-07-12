t=int(input())
for _ in range(t):
    n=int(input())
    if n<3:
        print("alice")
    elif n%2==0:
        print("bob")
    else:
        print("alice")