# start input
n = int(input())
puzzle = []
for i in range(n):
    puzzle.append(list(map(int,input().split())))
#start coding using dp
position = dict()
for i in range(len(puzzle)):
    position[puzzle[i][0]] = i
puzzle.sort()
# hash to record position
dp = [0 for i in range(n + 1)]
dp[0] = 0
result_index_value = dict()
result = []

for i in range(n):
    original_value = puzzle[i][0]
    height = puzzle[i][1]
    base = puzzle[i][0]
    dp[i + 1] += 1
    for j in range(i + 1, n):
        compare_variable = base + height - 1
        if base + height - 1 >= base + 1:
            pass
        else:
            compare_variable = base + 1

        if compare_variable >= puzzle[j][0]:
            if compare_variable >= puzzle[j][0] + puzzle[j][1] - 1:
                pass
            else:
                base = puzzle[j][0]
                height = puzzle[j][1]
            dp[j + 1] += 1
            dp[j + 1] += dp[j]
    result_index_value[original_value] = max(dp)
    result.append(max(dp))
    dp = [0 for i in range(n + 1)]
    dp[0] = 0
true_result = [0 for i in range(n)]

#convert result ===> true result
for i in range(len(puzzle)):
    true_result[position[puzzle[i][0]]] = result_index_value[puzzle[i][0]]

for i in range(n):
    print(true_result[i])