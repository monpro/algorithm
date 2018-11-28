digit = int(input())

if digit >=  256 * 256 * 256 * 256:
    print('0.0.0.0')
def helper(number):
    result = []
    for x in [24,16,8,0]:
        result.append(str(number >> x & 0xff))
    return ".".join(result)
if helper(digit) == '255.255.255.255':
    print('0.0.0.0')
else:
    print(helper(digit))