
class Product:
    def __init__(self, name:str, weight:float, category:str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r', encoding='utf-8')
        products_ = file.read()
        file.close()
        return products_

    def add(self, *products):
        for i in products:
            for i_product in self.get_products().split('\n'):
                if i.name in i_product.split(', ')[0]:
                   i.weight += float(i_product.split(', ')[1])
                   print(f'Продукт {i.name} уже был в магазине, его общий вес теперь равен {i.weight}')
            file_products = open(self.__file_name, 'a', encoding='utf-8')
            file_products.write(f'{i.name}, {i.weight}, {i.category}\n')
            file_products.close()


if __name__ == '__main__':
    s1 = Shop()
    p1 = Product('Potato', 50.5, 'Vegetables')
    p2 = Product('Spaghetti', 3.4, 'Groceries')
    p3 = Product('Potato', 5.5, 'Vegetables')
    s1.add(p1, p2, p3)
    print(s1.get_products())
