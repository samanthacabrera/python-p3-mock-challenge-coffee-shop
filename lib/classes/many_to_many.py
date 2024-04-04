class Coffee:
    all = []
    def __init__(self, name):
        self._name = name
        Coffee.all.append(self)
    
    def get_name(self):
        return self._name

    def set_name(self, value):
        if hasattr(self, "_name"):
            raise AttributeError("ae")
        elif type(value) == str and len(value)>= 3:
            self._name = value
            
    name = property(get_name, set_name)  
        
    def orders(self):
        orderList = []
        for order in Order.all:
            if order.coffee is self:
                orderList.append(order)
        return orderList

    def customers(self):
        customerList = set()
        for order in Order.all:
            if order.coffee is self:
                customerList.add(order.customer)
        return list(customerList)
    
    def num_orders(self):
        numorders = 0
        for order in Order.all:
            if order.coffee is self:
                numorders += 1
        return numorders
    
    def average_price(self):
        orders = self.orders()
        total_price = 0
        if len(orders) == 0:
            return 0
        for order in orders:
            total_price += order.price
        return total_price / len(orders)

class Customer:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_name(self,value):
        if type(value) == str and (1 < len(value) < 16):
            self._name = value
        # else:
        #     raise ValueError("value error")
    name = property(get_name,set_name)
    
    def orders(self):
        orderList = []
        for order in Order.all:
            if order.customer is self:
                orderList.append(order)
        return orderList
    
    def coffees(self):
        coffeeList = set()
        for order in Order.all:
            if order.customer is self:
                coffeeList.add(order.coffee)
        return list(coffeeList)
 
    def create_order(self, coffee, price):
        order = Order(self, coffee, price)
        return order
    
class Order:
    all = []
    def __init__(self, customer, coffee, price):
        self._customer = customer
        self._coffee = coffee
        self._price = price
        Order.all.append(self)
    
    # def get_price(self):
    #     return self._price

    # def set_price(self, value):
    #     if hasattr(self, "_price"):
    #         raise AttributeError("ae")
    #     elif type(price) == float and 1.0 <= price <= 10.0:
    #         self._price = value
    
    def get_price(self):
        return self._price

    def set_price(self, value):
        if type(value) is float:
            if 1 <= float(value) <= 10:
                if not hasattr(self, 'price'):
                    self._price = value
                else:
                    raise ValueError("Order has already been instantiated")
            else:
                raise ValueError("Price must be between 1.0 and 10.0")
        else:
            raise ValueError("Price must be a number")

    price = property(get_price, set_price)
    
    def get_customer(self):
        return self._customer
    customer = property(get_customer)  

    
    def get_coffee(self):
        return self._coffee
    coffee = property(get_coffee)  