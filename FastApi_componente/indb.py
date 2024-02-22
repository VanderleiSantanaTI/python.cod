from product import Product


def generate_products():
    list_products = []

    for x in range(10):
        p = Product(name=f"Produto {x + 1}", price=5.5 * x)
        list_products.append(p)
    return list_products
