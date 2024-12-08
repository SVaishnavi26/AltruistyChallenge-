def max_profit(prices):
    
    min_price = float('inf')
    max_profit = 0
    
    
    for price in prices:
        
        if price < min_price:
            min_price = price
       
        elif price - min_price > max_profit:
            max_profit = price - min_price
    
    return max_profit
n = int(input("Enter the number of days: "))
print("Enter the property prices:")
prices = [int(input()) for _ in range(n)]
result = max_profit(prices)
print("Maximum Profit:", result)
