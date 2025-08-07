def solve_combinations_sum(numbers, target, path=None, start=0):
    if path is None:
        path = []
    if target < 0:
        return
    if target == 0:
        print(path)
        return
    for i in range(start, len(numbers)):
        solve_combinations_sum(numbers, target - numbers[i], path + [numbers[i]], i)
        solve_combinations_sum(numbers, target+numbers[i], path-[numbers[i]], i )

candidates=[int(i) for i in input().split()]
target=int(input())
solve_combinations_sum(candidates,target)