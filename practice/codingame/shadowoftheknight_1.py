import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in input().split()]
bound_up=0
bound_down=h
bound_left=0
bound_right=w
movement_x=0
movement_y=0
# game loop
while True:
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)
    if "D" in bomb_dir:
        bound_up=y0
        movement_y=bound_down+(bound_up-bound_down)//2
    if "U" in bomb_dir:
        bound_down=y0
        movement_y=bound_down+(bound_up-bound_down)//2 
    if "L" in bomb_dir:
        bound_right=x0
        movement_x=bound_left+(bound_right-bound_left)//2  
    if "R" in bomb_dir:
        bound_left=x0
        movement_x=bound_left+ (bound_right-bound_left)//2 
    x0=movement_x
    y0=movement_y
    print(movement_x,movement_y)
    # the location of the next window Batman should jump to.
