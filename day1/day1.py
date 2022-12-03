with open('day1.txt') as opened:data = [x.split('\n') for x in opened.read().split('\n\n')]
elves = sorted([sum([int(x) for x in item]) for item in[elf for elf in data]],reverse=True)
print(max(elves),sum(elves[0:3]),sep='\n')