
def filterfunc(x):
    return x % 3 == 0
    
mult3 = filter(filterfunc, [1, 2, 3, 4, 5, 6, 7, 8, 9])
