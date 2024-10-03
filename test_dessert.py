import pytest
from dessert import DessertItem, Candy

#attributes
#calculate cost
#calculate tax

def test_dessertitem_attribute():
    dessertitem=Candy("Candy Corn", 1.5, .25, 'Bag')
    assert dessertitem.name=='Candy Corn'

def test_calculate_cost():
    dessertitem=Candy("Candy Corn", 1.5, .25, 'Bag')
    assert dessertitem.calculate_cost()==.38
    
def test_calculate_tax():
    dessertitem=Candy("Candy Corn", 1.5, .25, 'Bag')
    assert dessertitem.calculate_tax()==.03
    
def test_dessert_item_operators():
    candy1 = Candy('Chocolate Bar', 0.2, 1.99)
    candy2 = Candy('Gummy Bears', 0.25, 2.49)
    
    # Test equality
    assert candy1 == candy1
    assert not candy1 == candy2

    # Test inequality
    assert not candy1 != candy1
    assert candy1 != candy2

    # Test less than
    assert candy1 < candy2
    assert not candy2 < candy1

    # Test greater than
    assert candy2 > candy1
    assert not candy1 > candy2

    # Test less than or equal to
    assert candy1 <= candy1
    assert candy1 <= candy2
    assert not candy2 <= candy1

    # Test greater than or equal to
    assert candy2 >= candy2
    assert candy2 >= candy1
    assert not candy1 >= candy2