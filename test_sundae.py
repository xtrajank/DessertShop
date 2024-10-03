import pytest
from dessert import DessertItem, Candy, Cookie, IceCream, Sundae

def test_sundae_attribute():
    sundae=Sundae("Vanilla", 3, .69, "Hot Fudge", 1.29)
    assert sundae.name=='Vanilla'
    assert sundae.scoop_count==3
    assert sundae.price_per_scoop==.69
    assert sundae.topping_name=='Hot Fudge'
    assert sundae.topping_price==1.29

def test_calculate_cost():
    sundae=Sundae("Vanilla", 3, .69, "Hot Fudge", 1.29)
    assert sundae.calculate_cost()==3.36
    
def test_calculate_tax():
    sundae=Sundae("Vanilla", 3, .69, "Hot Fudge", 1.29)
    assert sundae.calculate_tax()==.24


