width = int(input())  # Number of cells on the X-axis
height = int(input())  # Number of cells on the Y-axis
arr = [list(input()) for _ in range(height)]
answer_arr = []
#pos (x,y)=width x height y
def closest_bottom_neighbor(x, y):
    for l in range(y + 1, height):  # Iterating through rows
        if arr[l][x] == "0":  # Column remains constant, checking below
            return [x, l]  
    return [-1, -1]
def closest_right_neighbor(x, y):
    for j in range(x + 1, width):  # Iterating through columns
        if arr[y][j] == "0":  # No need for extra bounds check
            return [j, y]  
    return [-1, -1]
for l in range(height):
    for j in range(width):
        if arr[l][j] == "0":  # Assuming '0' represents nodes
            right_neighbor = closest_right_neighbor(j, l)  # Corrected
            bottom_neighbor = closest_bottom_neighbor(j, l)  # Corrected
            answer_arr.append([[j, l], right_neighbor, bottom_neighbor])

for t in answer_arr:
    for j in range(len(t)):
        if j < 2:
            print(*t[j], end=" ")
        else:
            print(*t[j])