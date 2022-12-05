with open('day5.txt') as f: crates = f.read().split(' 1 ')
crates_list = [crates[0][i:i+3] for i in range(len(crates[0])) if i % 4 == 0]
crates_list_list = [crates_list[i:i+len(crates[0].split('\n')[0]+' ') // 4] for i in range(len(crates_list)) if i % (len(crates[0].split('\n')[0]+' ') // 4) == 0]
final_crates = [[elem[i][1] for elem in crates_list_list if elem[i] != '   '] for i in range(len(crates[0].split('\n')[0]+' ') // 4)]
commands_str = '\n'.join(' 1 '.join(crates[1:]).split('\n')[2:])
commands_list = [[int(x) for i, x in enumerate(elem.split(' ')) if i % 2 == 1] for elem in commands_str.split('\n')]
moved_crates_9000 = final_crates.copy()
moved_crates_9001 = final_crates.copy()
for command in commands_list:
    moved_items = (moved_crates_9000[command[1] - 1][0:command[0]])[::-1]
    print(moved_items)
    moved_crates_9000[command[1] - 1] = moved_crates_9000[command[1] - 1][command[0]:]
    moved_crates_9000[command[2] - 1] = moved_items + moved_crates_9000[command[2] - 1]
for command in commands_list:
    moved_items = moved_crates_9001[command[1] - 1][0:command[0]]
    print(moved_items)
    moved_crates_9001[command[1] - 1] = moved_crates_9001[command[1] - 1][command[0]:]
    moved_crates_9001[command[2] - 1] = moved_items + moved_crates_9001[command[2] - 1]
print(''.join([elem[0] for elem in moved_crates_9000]), ''.join([elem[0] for elem in moved_crates_9001]))