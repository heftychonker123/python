n=int(input())
arr=[int(i) for i in input().split()]
x_high = arr[0]
x_low = arr[0]
max_loss = 0
for x in arr:
    if x > x_high:
        x_high = x
        x_low = x
    elif x < x_low:
        x_low = x
    loss = x_low-x_high
    if loss < max_loss:
        max_loss = loss
print(max_loss)