import pytest
from dessert import DessertItem, Candy, Cookie, IceCream, Sundae

def test_candy_attribute():
    candy=Candy("Candy Corn", 1.5, .25)
    assert candy.name=='Candy Corn'
    assert candy.candy_weight==1.5
    assert candy.price_per_pound==.25

def test_calculate_cost():
    candy=Candy("Candy Corn", 1.5, .25)
    assert candy.calculate_cost()==.38
    
def test_calculate_tax():
    candy=Candy("Candy Corn", 1.5, .25)
    assert candy.calculate_tax()==.03
    
def test_can_combine_both_candies():
    candy1 = Candy("Candy Corn", 1.5, 0.25)
    candy2 = Candy("Chocolate Bar", 2.0, 0.50)
    assert candy1.can_combine(candy2) == True

def test_can_combine_other_not_candy():
    candy = Candy("Candy Corn", 1.5, 0.25)
    cookie = Cookie("Chocolate Chip", 12, 0.10)
    assert candy.can_combine(cookie) == False

def test_combine_two_candies():
    candy1 = Candy("Candy Corn", 1.5, 0.25)
    candy2 = Candy("Chocolate Bar", 2.0, 0.50)
    combined_item = candy1.combine(candy2)
    assert isinstance(combined_item, Candy)
    assert combined_item.name == "Candy Corn & Chocolate Bar"
    assert combined_item.candy_weight == 3.5
    assert combined_item.price_per_pound == 0.375

def test_combine_candy_and_not_candy():
    candy = Candy("Candy Corn", 1.5, 0.25)
    cookie = Cookie("Chocolate Chip", 12, 0.10)
    combined_item = candy.combine(cookie)
    assert combined_item == None
