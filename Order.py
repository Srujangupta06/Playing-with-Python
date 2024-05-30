class Product:
    def __init__(self,name,price,deal_price,ratings):
        self.name = name
        self.price = price
        self.deal_price = deal_price
        self.ratings = ratings
        self.you_save = price - deal_price

    def display_product_details(self):
        print(f"Product Name: {self.name}")
        print(f"Rating: {self.ratings}")
        print(f"Price: {self.price} INR/-")
        print(f"Deal Price: {self.deal_price} INR/-")
        print(f"You save: {self.you_save} INR/-")
    
    def get_deal_price(self):
        return self.deal_price
        
class ElectronicItem(Product):
    def __init__(self,name,price,deal_price,ratings,warranty):
        super().__init__(name,price,deal_price,ratings)
        self.warranty = warranty
    
    def display_product_details(self):
        super().display_product_details()
        if self.warranty <= 1:
            print(f"Warranty: {self.warranty} Year")
        else:
            print(f"Warranty: {self.warranty} Years")
        
class GroceryItem(Product):
    def __init__(self,name,price,deal_price,ratings,expiry_date):
        super().__init__(name,price,deal_price,ratings)
        self.expiry_date = expiry_date
   
    def display_product_details(self):
        super().display_product_details()
        print(f"Expiry Date: {self.expiry_date}")

class Laptop(ElectronicItem):
    def __init__(self,name,price,deal_price,ratings,warranty,ram,storage,mso,size):
        super().__init__(name,price,deal_price,ratings,warranty)
        self.ram = ram
        self.storage = storage
        self.mso = mso
        self.size = size
    def display_product_details(self):
        super().display_product_details()
        print(f"Ram : {self.ram}")
        print(f"Storage : {self.storage}")
        print(f"Microsoft-Office: {self.mso}")
        print(f"Screen (Inch) : {self.size}")
        
class Order:
    delivery_charges = {
        'Normal' : 40,
        'Prime' : 75
    }
    def __init__(self,delivery_method,delivery_address):
        self.items_in_cart = []
        self.delivery_method = delivery_method
        self.delivery_address = delivery_address
    
    def add_item_into_cart(self,product,quantity):
        item = (product,quantity)
        self.items_in_cart.append(item)
    
    def display_order_details(self):
        print(f"Delivery Method: {self.delivery_method}")
        print(f"Delivery Address: {self.delivery_address}")
        if self.delivery_method == "Prime":
            print(f"Prime-Delivery Charge: {Order.delivery_charges['Prime']}")
        else:
            print(f"Normal-Delivery Charge: {Order.delivery_charges['Normal']}")
        print("------------------------------------")
        for product,quantity in self.items_in_cart:
            product.display_product_details()
            print(f"Quantity: {quantity}")
            print("------------------------------------")
        total_bill = self.get_total_bill()
        order_deliver_charges = Order.delivery_charges[self.delivery_method]
        total_bill += order_deliver_charges
        print(f"Total Bill: {total_bill} INR/-")
        Order.greet()
        
    def get_total_bill(self):
        total = 0 
        for product,quantity in self.items_in_cart:
            total += product.get_deal_price() * quantity
        return total 
    
    @classmethod
    def update_delivery_charges(cls,method,charge):
        cls.delivery_charges[method] = charge
    
    @staticmethod
    def greet():
        print("")
        print("Have a Great Shopping !!!")
tv = ElectronicItem("TV",45000,43000,4.3,1)
#tv.display_product_details()
milk = GroceryItem("Milk",35,30,4.5,"31 May 2024")
#milk.display_product_details()
my_order = Order("Normal","Nizamabad")
my_order.add_item_into_cart(tv,1)
my_order.add_item_into_cart(milk,5)

hp = Laptop("HP Pavillion 15",75000,73000,4.3,1,"16 GB","512 GB SSD","Yes",15.6)
my_order.add_item_into_cart(hp,1)
my_order.display_order_details()
    