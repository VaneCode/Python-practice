han = open('mbox-shor.txt')

for line in han:
    line = line.rstrip()
    if line == ' ' :
     print('Blank line')
     continue
    wds = line.split
    # Guardian in a compound statement
    if wds.len < 3 or wds[0] != 'From':
        continue
    print(wds[2])