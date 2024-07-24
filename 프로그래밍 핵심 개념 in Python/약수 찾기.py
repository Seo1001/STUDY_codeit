i = 1
total = 0

while i <= 120:
    if 120 % i == 0:
        print(i)
        total += 1
    i += 1
    
print("120의 약수는 총 {}개입니다." .format (total))
