han = open('mbox-shor.txt')

for line in han:
    line = line.rstrip()
    if line == ' ' :
     print('Blank line')
     continue
    wds = line.split
    if wds[0] != 'From':
        continue
    print(wds[2])