def solve(digits, map, answer, answer_arr=None):
    if answer_arr is None:
        answer_arr = []
    if not digits:
        return []
    if len(answer) == len(digits):
        answer_arr.append("".join(answer))
        return answer_arr
    for letter in map.get(digits[len(answer)], []):
        answer.append(letter)
        solve(digits, map, answer, answer_arr)
        answer.pop()
    return answer_arr


d = input()
map = {
    "2": ["a", "b", "c"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j", "k", "l"],
    "6": ["m", "n", "o"],
    "7": ["p", "q", "r", "s"],
    "8": ["t", "u", "v"],
    "9": ["w", "x", "y", "z"],
}

print(solve(d, map, []))
