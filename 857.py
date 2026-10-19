expenses = [
    { "item" : "Lunch" , "amount" : 150},
    { "item" : "Bus" , "amount" : 40}
]

total = sum(exp["amount"] for exp in expenses)

print("Total :" , total )