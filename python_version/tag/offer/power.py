def power(base,exponent):
    if exponent > 0:
        flag = True
    else:
        flag = False

    exponent = abs(exponent)
    if base == 0:
        return 1
    if exponent == 1:
        return base

    result = power(base, exponent >> 1)
    result *= result

    if exponent & 1 == 1:
        result *= base
    if flag:
        return result
    else:
        return 1 / result


