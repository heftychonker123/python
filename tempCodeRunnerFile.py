import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

message = input().split()
t={}
for i in message:
    if i in t:
        t[i]+=1
    else:
        t[i]=0
for z in t:
    print(z+":"+str(t[z]))