def print1ToMaxOfDigits(n):
    if n <= 0:
        return
    string_presentation = ['0' for i in range(n)]
    for i in range(10):
        string_presentation[0] = str(i)
        helper(string_presentation,n,0)


def helper(number,length,index):
    if index == length - 1:
        printNumber(number)
        return
    for i in range(10):
        number[index + 1] = str(i)
        helper(number,length, index + 1)


def printNumber(number):
    # number = [i for i in number if i != '0']
    new_number = []
    for i in range(len(number)):
        if number[i] == '0':
            continue
        else:
            new_number = [j for j in number[i:]]
            break
    if len(new_number) > 0:
        print(''.join(new_number))

print1ToMaxOfDigits(2)