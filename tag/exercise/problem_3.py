    l = input().split(' ')
    n = int(l[0])
    m = int(l[1])

    result = []
    def josephus(n,m):
        people = list(range(1,n+1))
        index = 0
        for i in range(n):
            count = 0
            while count < m:
                if people[index] != 0:
                    count += 1
                if count == m:
                    result.append(people[index])
                    people[index] = 0
                index = (index+1) % n
        return result[-1]
    print(josephus(n,m))