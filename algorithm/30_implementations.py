lis = [59,12,1,8,234, 10,100,34,56,7,23,456,234,-58]

def sortport():
    for i in range(len(lis)-1):
        for j in range(len(lis)-1-i):
            if lis[j] > lis[j+1]:
                lis[j], lis[j+1] = lis[j+1], lis[j]
    return lis


def hcf(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x
    
    for i in range(i, smaller +1):
        if (x % i ==0) and (y % i == 0):
            hcf = i
    return hcf

def lcm(x, y)
    if x > y:
        greater = x
    else:
        greater = y

    while(True):
        if (greater % x == 0) and (greator % y) == 0:
            lcm = greater
            break
        else
            greater += 1 
    return lcm