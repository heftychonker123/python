import operator



#Checking if a point is in a diamond with diagonal length n
def check_in_diamond(x,y,n):
    return(n/2>=abs(x)+abs(y))
#Checking if a point is in a circle with diameter n
def check_in_circle(x,y,n):
    return(x**2+y**2<=(n**2)/4)
#Checking if a point is in a square with side length n
def check_in_square(x,y,n):
    return(abs(x)<=n/2 and abs(y)<=n/2)
size = int(input())
n = int(input())
answer={}
for i in range(n):
    name = input()
    answer[name]=0
t = int(input())
for i in range(t):
    j=0
    inputs = input().split()
    throw_name = inputs[0]
    throw_x = int(inputs[1])
    throw_y = int(inputs[2])
    if check_in_diamond(throw_x,throw_y,size):
        j=15
    elif check_in_circle(throw_x,throw_y,size):
        j=10    
    elif check_in_square(throw_x,throw_y,size):
        j=5
    else:
        j=0
    answer[throw_name]+=j
arr_1=list(answer)
index=n-1
while index>0:
    for i in range(index):
        if answer[arr_1[i]]<answer[arr_1[i+1]]:
            arr_1[i],arr_1[i+1]=arr_1[i+1],arr_1[i]
    index-=1
for z in arr_1:
    print(z,end=" ")
    print(answer[z])