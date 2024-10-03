import unittest
from dessertshop import Customer

class TestCustomer(unittest.TestCase):
    def test_unique_customer_ids(self):
        # Create three Customer instances
        customer1 = Customer("Alice")
        customer2 = Customer("Bob")
        customer3 = Customer("Charlie")

        # Check that their IDs are distinct
        self.assertNotEqual(customer1.customer_id, customer2.customer_id)
        self.assertNotEqual(customer1.customer_id, customer3.customer_id)
        self.assertNotEqual(customer2.customer_id, customer3.customer_id)

if __name__ == '__main__':
    unittest.main()
