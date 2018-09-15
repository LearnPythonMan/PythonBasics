test = 1794

def digital_root(n):
    while (n>9):
        n = sum(map(int,str(n)))
    return n

print(digital_root(test))

#def digital_root(n):
 #   return n if n < 10 else digital_root(sum(map(int,str(n))))

#def digital_root(n):
  #return n%9 or n and 9