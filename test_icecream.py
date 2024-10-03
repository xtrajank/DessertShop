import pytest
from dessert import DessertItem, Candy, Cookie, IceCream, Sundae

def test_icecream_attribute():
    icecream=IceCream("Pistachio", 2, .79)
    assert icecream.name=='Pistachio'
    assert icecream.scoop_count==2
    assert icecream.price_per_scoop==.79

def test_calculate_cost():
    icecream=IceCream("Pistachio", 2, .79)
    assert icecream.calculate_cost()==1.58
    
def test_calculate_tax():
    icecream=IceCream("Pistachio", 2, .79)
    assert icecream.calculate_tax()==.11

