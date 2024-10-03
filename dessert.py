from abc import ABC
from packaging import Packaging
from payable import Payable
from combine import Combinable

class DessertItem(Packaging,ABC):
    def __init__(self, name='', tax_percent=.0725, packaging=None):
        self.name=name
        self.tax_percent=tax_percent
        self.packaging=packaging
        
    def calculate_cost(self):
        pass
    
    def calculate_tax(self):
        return round(self.calculate_cost()*self.tax_percent,2)
        
    def __eq__(self, other):
        return self.calculate_cost() == other.calculate_cost()

    def __ne__(self, other):
        return self.calculate_cost() != other.calculate_cost()

    def __lt__(self, other):
        return self.calculate_cost() < other.calculate_cost()

    def __gt__(self, other):
        return self.calculate_cost() > other.calculate_cost()

    def __ge__(self, other):
        return self.calculate_cost() >= other.calculate_cost()

    def __le__(self, other):
        return self.calculate_cost() <= other.calculate_cost()
    
    def __str__(self):
        pass

class Candy(DessertItem, Combinable):
    def __init__(self, name='', candy_weight=0.0, price_per_pound=0.0, packaging='Bag'):
        super().__init__(name)
        self.candy_weight=candy_weight
        self.price_per_pound=price_per_pound
        self.packaging=packaging

    def can_combine(self, other: 'Candy') -> bool:
        if isinstance(other, Candy):
            return (self.name == other.name) and (self.price_per_pound == other.price_per_pound)
        else:
            return False

    def combine(self, other: 'Candy'):
        if self.can_combine(other):
            self.candy_weight += other.candy_weight
            return self.candy_weight
        else:
            raise ValueError("Candy cannot be combined")
    
    def calculate_cost(self):
        return round(self.candy_weight*self.price_per_pound,2)
    
    def __str__(self):
        return f'{self.name.title()}, {self.candy_weight} lb(s), ${self.price_per_pound:.2f}/lb, ${self.calculate_cost():.2f}, ${self.calculate_tax():.2f}, {self.packaging}'

class Cookie(DessertItem, Combinable):
    def __init__(self, name='', cookie_quantity=0.0, price_per_dozen=0.0, packaging='Box'):
        super().__init__(name)
        self.cookie_quantity=cookie_quantity
        self.price_per_dozen=price_per_dozen
        self.packaging=packaging
        
    def can_combine(self, other: 'Cookie') -> bool:
        if isinstance(other, Cookie):
            return (self.name == other.name) and (self.price_per_dozen == other.price_per_dozen)
        else:
            return False

    def combine(self, other: 'Cookie'):
        if self.can_combine(other):
            self.cookie_quantity += other.cookie_quantity
            return self.cookie_quantity
        else:
            raise ValueError("Cookies cannot be combined")
        
    def calculate_cost(self):
        return round((self.cookie_quantity/12)*self.price_per_dozen,2)
    
    def __str__(self):
        return f'{self.name.title()}, {self.cookie_quantity} cookies, ${self.price_per_dozen:.2f}/dozen, ${self.calculate_cost():.2f}, ${self.calculate_tax():.2f}, {self.packaging}'

class IceCream(DessertItem):
    def __init__(self, name='', scoop_count=0.0, price_per_scoop=0.0, packaging='Bowl'):
        super().__init__(name)
        self.scoop_count=scoop_count
        self.price_per_scoop=price_per_scoop
        self.packaging=packaging
        
    def __str__(self):
        return f'{self.name.title()}, {self.scoop_count}, ${self.price_per_scoop:.2f}, ${self.calculate_cost():.2f}, ${self.calculate_tax():.2f}, {self.packaging}'
        
    def calculate_cost(self):
        return round(self.price_per_scoop*self.scoop_count,2)

class Sundae(IceCream):
    def __init__(self, name='', scoop_count=0.0, price_per_scoop=0.0, topping_name='', topping_price=0.0, packaging='Boat'):
        super().__init__(name, scoop_count, price_per_scoop)
        self.topping_name=topping_name
        self.topping_price=topping_price
        self.packaging=packaging
        
    def calculate_cost(self):
        return round(self.price_per_scoop*self.scoop_count+self.topping_price,2)
    
    def __str__(self):
        return f'{self.name.title()}, {self.scoop_count}, ${self.price_per_scoop:.2f}, {self.topping_name.title()}, ${self.topping_price:.2f}, ${self.calculate_cost():.2f}, ${self.calculate_tax():.2f}, {self.packaging}'

class Order(Payable):
    def __init__(self):
        super().__init__(pay_type='1')
        self.order=[]
   
    def add(self,item):
        if not isinstance(item, Combinable) or not any(i.can_combine(item) for i in self.order):
            self.order.append(item)
        else:
            for i in self.order:
                if i.can_combine(item):
                    i.combine(item)
                    break

    def __len__(self):
        return len(self.order)
   
    def __iter__(self):
        self.index = 0
        return self
    
    def __next__(self):
        if self.index < len(self.order):
            result = self.order[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration
    
    def order_cost(self):
        cost=0
        for item in self.order:
            cost+=item.calculate_cost()
        return round(cost,2)
    
    def sort(self):
        self.order.sort()
    
    def order_tax(self):
        total=0
        for item in self.order:
            total+=item.calculate_tax()
        return round(total,2)
    
    def sort(self):
        self.order.sort()
    
    @property
    def pay_type(self):
        return self._pay_type
    
    def __repr__(self):
        return ', '.join([str(item) for item in self.order])
            