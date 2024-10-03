from dessert import Order, Candy, Cookie, IceCream, Sundae
import receipt

class DessertShop:
    customer_db={}
    def __init__(self):
        self.order = Order()
        
    def user_prompt_candy(self):
        name = input('Enter candy name:\n')
        weight = float(input('Enter weight:\n'))
        if weight < 0:
            raise ValueError('Invalid weight input.')
        price = float(input('Enter price:\n'))
        if price < 0:
            raise ValueError('Invalid price.')        
        return Candy(name.title(), weight, price)
    
    def user_prompt_cookie(self):
        name = input('Enter the cookie name:\n')
        quantity = int(input('Enter the quantity:\n'))
        if quantity < 0:
            raise ValueError('Invalid quantity input.')
        price = float(input('Enter the price per dozen:\n'))
        if price < 0:
            raise ValueError('Invalid price.')
        return Cookie(name.title(), quantity, price)

    def user_prompt_icecream(self):
        name = input('Enter the ice cream flavor:\n')
        quantity = int(input('Enter the scoop quantity:\n'))
        if quantity < 0:
            raise ValueError('Invalid quantity input.')        
        price = float(input('Enter the price per scoop:\n'))
        if price < 0:
            raise ValueError('Invalid price.')
        return IceCream(name.title(), quantity, price)

    def user_prompt_sundae(self):
        name = input('Enter the ice cream flavor:\n')
        quantity = int(input('Enter the scoops quantity:\n'))
        if quantity < 0:
            raise ValueError('Invalid quantity input.')
        price = float(input('Enter the price per scoop:\n'))
        if price < 0:
            raise ValueError('Invalid price.')
        topping = input('Enter the sundae topping:\n')
        topping_price = float(input('Enter the topping price:\n'))
        if topping_price < 0:
            raise ValueError('Invalid price.')
        return Sundae(name.title(), quantity, price, topping.title(), topping_price)
    
    def user_prompt_payment(self):
        payment_type = input('1: Cash\n2: Card\n3: Phone\nEnter payment method: ')
        if payment_type in ['1', '2', '3']:
            self.order._pay_type = self.order.PAYTYPES[int(payment_type) - 1]  # Convert to index
        else:
            print('Invalid payment method. Defaulting to Cash.')
            self.order._pay_type = self.order.PAYTYPES[0]  # Default to Cash
        return self.order._pay_type
    
    def user_prompt_customer(self):
        prompt_name = input('\nEnter customer name: ').title()
        if prompt_name not in self.customer_db.keys():
            customer = Customer(prompt_name)
            self.customer_db[prompt_name] = customer
        else:
            customer = self.customer_db[prompt_name]
        customer.add2history(self.order)
        return customer
    
    def admin(self):
        while True:
            print("\nAdmin Module Options:")
            print("1: Shop Customer List")
            print("2: Customer Order History")
            print("3: Best Customer")
            print("4: Exit Admin Module")

            choice = input("Enter your choice: ")

            if choice == '1':
                cust_list=[cust for cust in self.customer_db.keys()]
                for cust in cust_list:
                    print(cust)
            elif choice == '2':
                prompt_name=input('Enter customer name: ')
                if prompt_name.title() in self.customer_db.keys():
                    print(self.customer_db.get(prompt_name.title()))
                else:
                    print('Customer does not exist.')
            elif choice =='3':
                max_cost=0
                for customer_name, customer in self.customer_db.items():
                    if customer.cost_history>max_cost:
                        max_cost=customer.cost_history
                        best_customer_name=customer_name
                print(best_customer_name)
            elif choice =='4':
                return False
                    
            
class Customer:
    id=1000
    def __init__(self, customer_name=''):
        self.customer_name = customer_name
        self.order_history = []
        self.cost_history = 0
        self.customer_id = self.id
        Customer.id+=1
    
    def add2history(self, order: Order) -> 'Customer':
        self.order_history.append(order)
        self.cost_history+=order.order_cost()
        return self.order_history
    
    def __repr__(self):
        return repr([self.customer_id,[self.order_history]])

def main():
    while True:
        shop = DessertShop() 
        
        done = False
        prompt = '\n'.join([
            '\n',
            '1: Candy',
            '2: Cookie',            
            '3: Ice Cream',
            '4: Sundae',
            '\nWhat would you like to add to the order? (1-4, Enter for done): '
        ])

        while not done:
            choice = input(prompt)
            if choice == '':
                customer=shop.user_prompt_customer()
                shop.user_prompt_payment()
                print(shop.order)
                print(f'Customer: {customer.customer_name}\nCustomer ID: {customer.customer_id}\nTotal Orders: {len(customer.order_history)}')
                done=True
            elif choice == '1':            
                item = shop.user_prompt_candy()
                shop.order.add(item)
                print(f'{item.name} has been added to your order.')
            elif choice == '2':            
                item = shop.user_prompt_cookie()
                shop.order.add(item)
                print(f'{item.name} has been added to your order.')
            elif choice == '3':            
                item = shop.user_prompt_icecream()
                shop.order.add(item)
                print(f'{item.name} has been added to your order.')
            elif choice == '4':            
                item = shop.user_prompt_sundae()
                shop.order.add(item)
                print(f'{item.name} has been added to your order.')
            else:            
                print('Invalid response: Please enter a choice from the menu (1-4) or Enter')

        print()
      
        shop.order.sort()
    
        data = [['Name', '', 'Item Cost', 'Tax']]
    
        for item in shop.order:
            data.append([f'{item.name} ({item.packaging})', '', f'${item.calculate_cost():.2f}', f'${item.calculate_tax():.2f}'])

        data.append(['-------------------------------'])
        data.append(['Total items in your order', '', shop.order.__len__(), ''])
        data.append(['Order Subtotal', '', f'${shop.order.order_cost():.2f}', f'${shop.order.order_tax():.2f}'])
        data.append(['Order Total', '', '', f'${shop.order.order_tax() + shop.order.order_cost():.2f}'])
        data.append(['-------------------------------'])
        data.append([f'Paid with {shop.order.pay_type}'])
        data.append(['-------------------------------'])
        data.append([f'Customer: {customer.customer_name}','',f'Customer ID: {customer.customer_id}', f'Total Orders: {len(customer.order_history)}'])
    
        receipt.make_receipt(data, 'receipt.pdf')

        start_again=input("Would you like to start another order? (y/n): ").strip().lower()
        if start_again != 'y':
            break

    shop.admin()      

if __name__ == '__main__':
    main()
