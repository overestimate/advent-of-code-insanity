with open('day4.txt') as f: data = [[[int(z) for z in y.split('-')] for y in x.strip().split(',')] for x in f.readlines()]
running_subset_total = 0
running_overlap_total = 0
for i, pairing_group in enumerate(data):
    idx = 0
    idx_other = 1
    if pairing_group[idx_other][0] in range(pairing_group[idx][0], pairing_group[idx][1]+1):
        if pairing_group[idx_other][1] in range(pairing_group[idx][0], pairing_group[idx][1]+1):
            print(range(pairing_group[0][0], pairing_group[0][1]+1), pairing_group[1], end='+\n')
            running_subset_total += 1
            continue
    idx = 1
    idx_other = 0
    if pairing_group[idx_other][0] in range(pairing_group[idx][0], pairing_group[idx][1]+1):
        if pairing_group[idx_other][1] in range(pairing_group[idx][0], pairing_group[idx][1]+1):
            print(range(pairing_group[1][0], pairing_group[1][1]+1), pairing_group[0], end='-\n')
            running_subset_total += 1
def rot():
    global running_overlap_total
    print(f"iter={i} groups are subset, added")
    running_overlap_total +=1     
for i, pairing_group in enumerate(data):
    idx = 0
    idx_other = 1
    if pairing_group[idx_other][0] in range(pairing_group[idx][0], pairing_group[idx][1]+1):
        rot()
        continue
    elif pairing_group[idx_other][1] in range(pairing_group[idx][0], pairing_group[idx][1]+1):
        rot()
        continue
    idx = 1
    idx_other = 0
    if pairing_group[idx_other][0] in range(pairing_group[idx][0], pairing_group[idx][1]+1):
        rot()
        continue
    elif pairing_group[idx_other][1] in range(pairing_group[idx][0], pairing_group[idx][1]+1):
        rot()
        continue
print(running_subset_total, running_overlap_total)