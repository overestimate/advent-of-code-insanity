with open('day4.txt') as f: data = [[[int(z) for z in y.split('-')] for y in x.strip().split(',')] for x in f.readlines()]
running_subset_total = 0
running_overlap_total = 0
range_groups = []
for pairing_group in data:
    range_groups.append([range(pairing_group[0][0], pairing_group[0][1]+1), range(pairing_group[1][0], pairing_group[1][1]+1)])
for item in range_groups:
    item.sort(key=len, reverse=True)
for group in range_groups:
    if group[0] == group[1]:
        running_subset_total += 1
        continue
    subset_total_counter = len(group[1])
    for x in group[1]:
        if x in group[0]:
            subset_total_counter -= 1
    if subset_total_counter == 0: running_subset_total += 1
    print(group[0], group[1], len(group[1]), subset_total_counter)
for group in range_groups:
    for x in group[1]:
        if x in group[0]:
            running_overlap_total += 1
            break
print(running_subset_total, running_overlap_total)
