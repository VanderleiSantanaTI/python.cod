from product import Product


def generate_products():
    list_products = []

    for x in range(10):
        p = Product(name=f"Produto {x + 3}", price=4.90 * x)
        list_products.append(p)
    return list_products


if __name__ == "__main__":
    generate_products()

