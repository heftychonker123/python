# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

m = int(input())  # the amount of motorbikes to control
v = int(input())  # the minimum amount of motorbikes that must survive
l0 = input()  # L0 to L3 are lanes of the road. A dot character . represents a safe space, a zero 0 represents a hole in the road.
l1 = input()
l2 = input()
l3 = input()

# game loop
while True:
    s = int(input())  # the motorbikes' speed
    for i in range(m):
        # x: x coordinate of the motorbike
        # y: y coordinate of the motorbike
        # a: indicates whether the motorbike is activated "1" or detroyed "0"
        x, y, a = [int(j) for j in input().split()]
    print("SPEED")
