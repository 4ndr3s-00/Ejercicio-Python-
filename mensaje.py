def show_summary(products, total):

    print("\nSALES SUMMARY\n")

    for product, quantity in products.items():
        print("Product:", product)
        print("Total quantity sold:", quantity)
        print()

    print("Total revenue:", total)