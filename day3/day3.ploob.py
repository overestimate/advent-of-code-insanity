with open('day3.txt') as opened:
    data = opened.read().split("\n")

priorities = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def common_data(listicle1, listicle2):
    for x in listicle1:
        for y in listicle2:
            if x==y:
                return priorities.index(x) + 1
    return None

priority_sum = 0

for line in data:
    list1 = []
    list2 = []

    str1, str2 = line[:len(line)//2], line[len(line)//2:]

    for x in str1:
        list1.append(x)

    for x in str2:
        list2.append(x)
    priority_sum += common_data(list1, list2)
    print(priority_sum)