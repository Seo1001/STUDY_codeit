dongil_total = 50000000
miran_total = 1100000000
year = 1988
defference = 0

while year < 2016:
    dongil_total = dongil_total * 1.12
    year += 1
    
if dongil_total > miran_total:
    defference = int (dongil_total) - miran_total
    print("{}원 차이로 동일 아저씨 말씀이 맞습니다." .format(defference))
