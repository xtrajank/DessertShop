import pytest
from dessert import DessertItem, Candy, Cookie, IceCream, Sundae

def test_cookie_attribute():
    cookie=Cookie("Chocolate Chip", 6, 3.99)
    assert cookie.name=='Chocolate Chip'
    assert cookie.cookie_quantity==6
    assert cookie.price_per_dozen==3.99

def test_calculate_cost():
    cookie=Cookie("Chocolate Chip", 6, 3.99)
    assert cookie.calculate_cost()==2.00
    
def test_calculate_tax():
    cookie=Cookie("Chocolate Chip", 6, 3.99)
    assert cookie.calculate_tax()==0.14

def test_can_combine_both_cookies():
    cookie1 = Cookie("Chocolate Chip", 6, 3.99)
    cookie2 = Cookie("Oatmeal Raisin", 12, 4.99)
    assert cookie1.can_combine(cookie2) == True

def test_can_combine_other_not_cookie():
    cookie = Cookie("Chocolate Chip", 6, 3.99)
    ice_cream = IceCream("Vanilla", 2, 2.50)
    assert cookie.can_combine(ice_cream) == False

def test_combine_two_cookies():
    cookie1 = Cookie("Chocolate Chip", 6, 3.99)
    cookie2 = Cookie("Oatmeal Raisin", 12, 4.99)
    combined_item = cookie1.combine(cookie2)
    assert isinstance(combined_item, Cookie)
    assert combined_item.name == "Chocolate Chip & Oatmeal Raisin"
    assert combined_item.cookie_quantity == 18
    assert combined_item.price_per_dozen == 4.49

def test_combine_cookie_and_not_cookie():
    cookie = Cookie("Chocolate Chip", 6, 3.99)
    ice_cream = IceCream("Vanilla", 2, 2.50)
    combined_item = cookie.combine(ice_cream)
    assert combined_item == None
