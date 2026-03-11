def calculate_totals(sales):

    products = {}
    total = 0

    for sale in sales:
        product = sale["product"]
        quantity = sale["quantity"]
        price = sale["price"]

        total += price * quantity

        if product in products:
            products[product] += quantity
        else:
            products[product] = quantity

    return products, total