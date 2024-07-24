a = 1
b = 1
value = 0

while a <= 9:
    while b <= 9:
        value = a * b
        print("{} * {} = {}" .format(a, b, value))
        b += 1
    a += 1
    b = 1
    
