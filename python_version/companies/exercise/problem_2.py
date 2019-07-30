def helper(k, n):
    # write your code here
    result_Number = 0 if k > 0 else 1
    num = ['0'] + list(str(n))
    for i in range(1, len(num)):
        large_Number = int(''.join(num[:i]))
        residual_number = int(''.join(num[i + 1:])) if (i + 1) < len(num) else 0
        residual_number += 1
        if k != 0:
            large_Number += 1
        if k < int(num[i]):
            result_Number += large_Number * 10 ** (len(num) - i - 1)
        elif k == int(num[i]):
            result_Number += (large_Number - 1) * (10 ** (len(num) - i - 1)) + residual_number
        else:
            result_Number += (large_Number - 1) * (10 ** (len(num) - i - 1))
    return result_Number

n  = int(input())
if n <= 0 or n >= 1000000000:
    print(-1)
else:
    result = []
    for i in range(9,-1,-1):
        result.append(helper(i,n))
    result[-1] -= 1
    for i in result:
        print(i,end=" ")
