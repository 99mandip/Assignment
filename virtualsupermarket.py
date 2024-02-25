supermarket = { "wheat": {"quantity": 20, "price": 100},
               "biscuits":  {"quantity": 50, "price": 120},
               "cheese":  {"quantity": 20, "price": 300},
               "perfume":  {"quantity": 10, "price": 440},
               "apples":  {"quantity": 15, "price": 150},
               "butter":  {"quantity": 35, "price": 225},
               "creatine": {"quantity": 40, "price": 1015},
               "cornflakes":  {"quantity": 20, "price": 700}            
              }



customers = ["Ram", "Hari", "Sita"]
grocery_lists = { 
   "Ram" : [('biscuits', 10), ('cheese', 15), ('butter', 7), ('cornflakes', 10)],
   "Hari":  [('creatine', 15), ('apples', 10), ('perfume', 5), ('cheese', 12), 
             ('cornflakes', 5)],
   "Sita":  [('cornflakes', 5), ('creatine', 20), ('perfume', 5), ('apples', 5), 
             ('cheese', 30), ('biscuits', 20)]}

    
# filling the carts
carts = {}
for customer in customers:
    carts[customer] = []
    for item, quantity in grocery_lists[customer]:
        if item in supermarket:
            if supermarket[item]["quantity"] < quantity:
                quantity = supermarket[item]["quantity"]
            if quantity:
                supermarket[item]["quantity"] -= quantity
                carts[customer].append((item, quantity))
for customer in customers:                            
     print(carts[customer])
            
            
print("checkout")
for customer in customers:
    print("\ncheckout for " + customer + ":")
    total_sum = 0
    for name, quantity in carts[customer]:
        unit_price = supermarket[name]["price"]
        amount_sum = quantity * unit_price
        print(f"{quantity:3d} {name:12s} {unit_price:8.2f} {amount_sum:8.2f}")
        total_sum += amount_sum
    print(f"Total sum:             {total_sum:11.2f}")





    








