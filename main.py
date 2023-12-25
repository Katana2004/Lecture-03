class Discount:
    def discount(self, order_price):
        return order_price

class RegularDiscount(Discount):
    def discount(self, order_price):
        return order_price * 0.95

class SilverDiscount(Discount):
    def discount(self, order_price):
        return order_price * 0.90

class GoldDiscount(Discount):
    def discount(self, order_price):
        return order_price * 0.85

class Client:
    def __init__(self, name, discount):
        self.name = name
        self.discount = discount

    def get_total_price(self, order_price):
        discounted_price = self.discount.discount(order_price)
        return f"Итоговая стоимость для клиента {self.name}: {discounted_price}"

order_price = 100

regular_client = Client("Иван", RegularDiscount())
silver_client = Client("Мария", SilverDiscount())
gold_client = Client("Петр", GoldDiscount())

print(regular_client.get_total_price(order_price))
print(silver_client.get_total_price(order_price))
print(gold_client.get_total_price(order_price))
