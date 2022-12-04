with open('day3.txt', 'r') as f:s=f.read().split('\n')
r=[s[i:i+3] for i in range(0,len(s),3)]
k=[(x[0:len(x)//2],x[len(x)//2:]) for x in s]
m='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
def j(v):return chr([x for x in sorted([[ord(x) for x in v[1]],[ord(x) for x in v[0]]])[0] if x in sorted([[ord(x) for x in v[1]],[ord(x) for x in v[0]]])[1]][0])
def z(e):return chr([x for x in sorted([[ord(x) for x in y] for y in e])[0] if x in sorted([[ord(x) for x in y] for y in e])[1] and x in sorted([[ord(x) for x in y] for y in e])[2]][0])
print(sum([m.index((j(p)))+1 for p in k]), sum([m.index((z(g)))+1 for g in r]), sep='\n')