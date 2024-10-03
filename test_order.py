import pytest
from dessert import Order, Candy, Cookie, IceCream, Sundae

# Test valid payment types
def test_cash_payment_type():
    order = Order()

    order.set_pay_type('1')
    assert order.get_pay_type() == 'CASH'

def test_card_payment_type():
    order = Order()

    order.set_pay_type('2')
    assert order.get_pay_type() == 'CARD'
    
def test_phone_payment_type():
    order = Order()

    order.set_pay_type('3')
    assert order.get_pay_type() == 'PHONE'

# Test invalid payment type
def test_invalid_payment_type():
    order = Order()

    with pytest.raises(ValueError, match='Invalid Payment Type'):
        order.set_pay_type('4')

# Test getting an invalid payment type
def test_get_invalid_payment_type():
    order = Order()

    # Trying to get an invalid payment type
    with pytest.raises(ValueError, match='Invalid Payment Type'):
        order.get_pay_type()

# Test setting payment type with an empty string
def test_set_payment_type_empty_string():
    order = Order()

    order.set_pay_type('')
    assert order.get_pay_type() == 'CASH'

def test_order_sort_method():
    order = Order()
    candy1 = Candy('Chocolate Bar', 0.2, 1.99)
    candy2 = Candy('Gummy Bears', 0.25, 2.49)
    candy3 = Candy('Lollipop', 0.1, 0.99)

    order.add(candy2)
    order.add(candy1)
    order.add(candy3)

    # Sort the order
    order.sort()

    # The order should be sorted in ascending order of prices
    assert order.order[0] == candy3
    assert order.order[1] == candy1
    assert order.order[2] == candy2