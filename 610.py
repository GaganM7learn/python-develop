sales = [1200, 450, 800, 1500, 300, 950]

large_sales_total = sum( sale for sale in sales if sale >= 800)
print(large_sales_total)