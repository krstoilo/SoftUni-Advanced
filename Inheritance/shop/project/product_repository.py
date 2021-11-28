from project.product import Product


class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str):
        for product in self.products:
            if product_name == product.name:
                return product
        return None

    def remove(self, product_name: str):
        for product in self.products:
            if product_name == product.name:
                self.products.remove(product)
                break

    def __repr__(self):
        result = ''

        for product in self.products:
            result += f'{product.name}: {product.quantity}'
            result += '\n'

        return result.strip()
