class Invoice:
    def __init__(self, item_number, item_description, quantity, price_per_item):
        self.__item_number = item_number
        self.__item_description = item_description
        self.__quantity = max(0, quantity) 
        self.__price_per_item = max(0.0, price_per_item)

    def get_item_number(self):
        return self.__item_number

    def set_item_number(self, item_number):
        self.__item_number = item_number

    def get_item_description(self):
        return self.__item_description

    def set_item_description(self, item_description):
        self.__item_description = item_description

    def get_quantity(self):
        return self.__quantity

    def set_quantity(self, quantity):
        self.__quantity = max(0, quantity)

    def get_price_per_item(self):
        return self.__price_per_item

    def set_price_per_item(self, price_per_item):
        self.__price_per_item = max(0.0, price_per_item)

    def get_invoice_amount(self):
        return self.__quantity * self.__price_per_item

invoice1 = Invoice("001", "Teclado", 2, 50.0)
print("Número do Item:", invoice1.get_item_number())
print("Descrição do Item:", invoice1.get_item_description())
print("Quantidade:", invoice1.get_quantity())
print("Preço por Item:", invoice1.get_price_per_item())
print("Valor da Fatura:", invoice1.get_invoice_amount())

invoice1.set_quantity(3)
invoice1.set_price_per_item(55.0)

print("\nValores modificados:")
print("Quantidade:", invoice1.get_quantity())
print("Preço por Item:", invoice1.get_price_per_item())
print("Valor da Fatura:", invoice1.get_invoice_amount())
