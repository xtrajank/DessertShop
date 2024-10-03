#default
#nominal
#modify
import pytest
from dessert import DessertItem, Candy, Cookie, IceCream, Sundae

def test_dessertitem_default():
  dessertitem=DessertItem()
  assert dessertitem.name==''

def test_dessertitem_nominal():
  dessertitem=DessertItem('candy corn')
  assert dessertitem.name=='candy corn'

def test_dessertitem_modify():
  dessertitem=DessertItem()
  dessertitem.name='candy corn'
  assert dessertitem.name=='candy corn'

def test_candy_defualt():
    candy=Candy()
    assert candy.name==''
    assert candy.candy_weight==0.0
    assert candy.price_per_pound==0.0
    
def test_candy_nominal():
    candy=Candy('gum', 0.02, 5)
    assert candy.name=='gum'
    assert candy.candy_weight==0.02
    assert candy.price_per_pound==5
    
def test_candy_modify():
  candy=Candy()
  candy.name='snickerdoodle'
  assert candy.name=='snickerdoodle'
  candy.candy_weight=0.02
  assert candy.candy_weight==0.02
  candy.price_per_pound=5
  assert candy.price_per_pound==5

def test_cookie_defualt():
  cookie=Cookie()
  assert cookie.name==''
  assert cookie.cookie_quantity==0.0
  assert cookie.price_per_dozen==0.0
    
def test_cookie_nominal():
  cookie=Cookie('snickerdoodle', 2, 5)
  assert cookie.name=='snickerdoodle'
  assert cookie.cookie_quantity==2
  assert cookie.price_per_dozen==5
    
def test_cookie_modify():
  cookie=Cookie()
  cookie.name='snickerdoodle'
  assert cookie.name=='snickerdoodle'
  cookie.cookie_quantity=2
  assert cookie.cookie_quantity==2
  cookie.price_per_dozen=5
  assert cookie.price_per_dozen==5

def test_icecream_defualt():
  icecream=IceCream()
  assert icecream.name==''
  assert icecream.scoop_count==0
  assert icecream.price_per_scoop==0.0
    
def test_icecream_nominal():
  icecream=IceCream('mint', 2, 2.0)
  assert icecream.name=='mint'
  assert icecream.scoop_count==2
  assert icecream.price_per_scoop==2.0
    
def test_icecream_modify():
  icecream=IceCream()
  icecream.name='mint'
  assert icecream.name=='mint'
  icecream.scoop_count=2
  assert icecream.scoop_count==2
  icecream.price_per_scoop=2.0
  assert icecream.price_per_scoop==2.0

def test_sundae_defualt():
  sundae=Sundae()
  assert sundae.name==''
  assert sundae.scoop_count==0
  assert sundae.price_per_scoop==0.0
  assert sundae.topping_name==''
  assert sundae.topping_price==0.0
    
def test_sundae_nominal():
  sundae=Sundae('fudge', 2, 2.0, 'fudge', 4.0)
  assert sundae.name=='fudge'
  assert sundae.scoop_count==2
  assert sundae.price_per_scoop==2.0
  assert sundae.topping_name=='fudge'
  assert sundae.topping_price==4.0
    
def test_sundae_modify():
  sundae=Sundae()
  sundae.name='fudge'
  assert sundae.name=='fudge'
  sundae.scoop_count=2
  assert sundae.scoop_count==2
  sundae.price_per_scoop=2.0
  assert sundae.price_per_scoop==2.0
  sundae.topping_name='fudge'
  assert sundae.topping_name=='fudge'
  sundae.topping_price=4.0
  assert sundae.topping_price==4.0