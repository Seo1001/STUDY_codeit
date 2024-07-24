val1 = 1
val2 = 1 
i = 1 

print(val1)
print(val2)
while i <= 48:
    if i % 2 == 0:
        val1 = val1 + val2
        print(val1)
    else:
        val2 = val1 + val2
        print(val2)
    i += 1
