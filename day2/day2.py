with open('day2.txt','r') as f:g = [(a.split(' ')[0],a.split(' ')[1]) for a in f.read().split('\n')]
def c1(s,o):return (ord(s)-ord(o)-1)%3*3+ord(s)-87
def c2(r,o):return (ord(r)-88)%3*3+(((ord(r)-88)%3)+ord(o)-63)%3+1
print(f"first half, score is {sum([c1(t[1],t[0]) for t in g])}", f"second half, score is {sum([c2(t[1],t[0]) for t in g])}", sep="\n")