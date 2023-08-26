word = 'WARNING'
with open(r'search_file\log.txt', 'r') as fp:
    # read all lines in a list
    lines = fp.readlines()
    n = 0
    for line in lines:
        n = n + 1
        if line.find(word) != -1:
            print(word, 'string exists in file')
            print('Line Number:', n)
            print('Line:', line)