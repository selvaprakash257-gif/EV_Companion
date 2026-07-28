def charging_cost():

    
    units = int(input("Enter Units Consumed: "))

    price_per_unit = float(input("Enter Price Per Unit: "))

    total_cost = units * price_per_unit

    print("Charging Cost: ₹", total_cost)
