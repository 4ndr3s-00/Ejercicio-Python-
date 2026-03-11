from calcular import calculate_totals
from mensaje import show_summary

sales = []

option = "y"

while option == "y":
    product = input("Product name: ")
    price = float(input("Unit price: "))
    quantity = int(input("Quantity: "))

    sales.append({
        "product": product,
        "price": price,
        "quantity": quantity
    })

    option = input("Add another sale? (y/n): ").lower()


products, total = calculate_totals(sales)

show_summary(products, total)