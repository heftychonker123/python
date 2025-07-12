arr=[int(i) for i in input().split()]
index=len(arr)-1
while index>0:
    for i in range(index):
        if arr[i]<arr[i+1]:
            arr[i],arr[i+1]=arr[i+1],arr[i]
    index-=1
print(arr)