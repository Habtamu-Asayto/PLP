def  calculate_discount(price, discount_percent) :
    if discount_percent >= (20/100)* price:
        discount_percent = (20/100) * price
        new = price - discount_percent
        return new
    else:
        return price
price = float(input("Enter the price: "))
discount = float(input("Enter the discount percent: "))
new_price = calculate_discount(price, discount)
print(f"The new price after discount is: {new_price}")