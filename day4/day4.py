with open('day4.txt') as f: data = [[[int(z) for z in y.split('-')] for y in x.strip().split(',')] for x in f.readlines()]
range_groups = [sorted([range(pairing_group[0][0], pairing_group[0][1]+1), range(pairing_group[1][0], pairing_group[1][1]+1)], key=len, reverse=True) for pairing_group in data]
subset_groups = [g for g in range_groups if g[0][0] <= g[1][0] and g[0][-1] >= g[1][-1]]
overlap_groups = [g for g in range_groups if True in [True for x in g[1] if x in g[0]]]
print(len(subset_groups), len(overlap_groups))