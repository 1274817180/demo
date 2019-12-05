li = [1, 2, 4, 8, 16]


def resolve(num):
    li.sort()
    li.reverse()
    li1 = []
    if num % 2 == 0:
        for i in li:
            if num >= i:
                li1.append(i)
                num = num - i
            elif num == 0:
                return li1
            else:
                pass
    elif num % 2 == 1:
        num = num - 1
        for i in li:
            if num >= i:
                li1.append(i)
                num = num - i
            elif num == 0:
                li1.append(1)
                return li1
            else:
                pass


print(resolve(18))