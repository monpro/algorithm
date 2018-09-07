N,K = [int(i) for i in input().split(" ")]
input_string = [int(i) for i in input().split(" ")]

#four position
left,count,window,leftIndex = 0,0,0,0

for right in range(len(input_string)):
    #current is 0, ---->
    if input_string[right] == 0:
        count += 1
    while count > K:
        #found 0 ---->
        if input_string[left] == 0:
            count -= 1
        left += 1
        if right - left + 1 > window:
            window = right - left + 1
            leftIndex = left
print(window)



