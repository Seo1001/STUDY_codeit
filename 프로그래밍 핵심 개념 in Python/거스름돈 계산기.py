def calculate_change(payment, cost):
    change = payment - cost
    
    
    fifty_thousand = change // 50000
    print("50000원 지폐: {}장". format(fifty_thousand))
    change = change % 50000
    
    ten_thousand = change // 10000
    print("10000원 지폐: {}장". format(ten_thousand))
    change = change % 10000
    
    five_thousand = change // 5000
    print("5000원 지폐: {}장". format(five_thousand))
    change = change % 5000
    
    one_thousand = change // 1000
    print("1000원 지폐: {}장". format(one_thousand))
    change = change % 1000

# 테스트 코드
calculate_change(100000, 33000)
print()
calculate_change(500000, 378000)
