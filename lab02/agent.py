import matplotlib.pyplot as plt
import math


class InventoryAgent:
    def __init__(self, avg_price, discount_threshold=0.20, critical_stock=10, min_order=10, normal_order=15):
        self.avg_price = avg_price
        self.discount_threshold = discount_threshold
        self.critical_stock = critical_stock
        self.min_order = min_order
        self.normal_order = normal_order

    def should_order(self, price, stock_level):
        
        discounted_price = self.avg_price * (1 - self.discount_threshold)
        if price <= discounted_price and stock_level >= self.critical_stock:
            return self.normal_order  
        elif stock_level < self.critical_stock:
            return self.min_order  
        return 0  


avg_price = float(input("Enter the average price of the smartphone: "))
agent = InventoryAgent(avg_price=avg_price)


time_steps = []
prices = []
stock_levels = []
orders = []


num_steps = int(input("Enter the number of time steps: "))

for t in range(num_steps):
    print(f"\nTime Step {t + 1}")
    

    price = float(input("Enter the current price of the smartphone: "))
    stock_level = int(input("Enter the current stock level: "))
    order = agent.should_order(price, stock_level)
    

    time_steps.append(t)
    prices.append(price)
    stock_levels.append(stock_level)
    orders.append(order)
    
    print(f"Order placed: {order} units")

plt.figure(figsize=(10, 6))
plt.plot(time_steps, stock_levels, label="Stock Level", marker='o')
plt.plot(time_steps, prices, label="Price", marker='o')
plt.plot(time_steps, orders, label="Orders", linestyle='--', marker='o')
plt.xlabel("Time Step")
plt.ylabel("Value")
plt.legend()
plt.title("Smartphone Inventory Management")
plt.show()