s = input()
k = int(input())
high=len(s)+1
low=1
def check_kgood(string,k):
    return(len(set(string))<=k)
while high>low:
    mid=low + (high-low)//2
    good=False
    for i in range(len(s)-mid + 1):
        if check_kgood((s[i:i+mid]),k):
            good=True
            break
    if good:
        low=mid+1
    else:
        high=mid
print(low - 1)
    