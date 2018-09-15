test = 1794

def digital_root(n):
    while (n>9):
        n = sum(map(int,str(n)))
    return n

print(digital_root(test))