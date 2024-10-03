class Payable:
    PAYTYPES = ['CASH', 'CARD', 'PHONE']

    def __init__(self, pay_type='1'):
        self._pay_type = pay_type

    @staticmethod
    def get_pay_types():
        return Payable.PAYTYPES

    @property
    def pay_type(self):
        return self._pay_type
    
    @pay_type.setter
    def pay_type(self, paytype):
        paytype_map = {'1': 'CASH', '2': 'CARD', '3': 'PHONE'}
        if paytype in paytype_map:
            self._pay_type = paytype_map[paytype]
        elif paytype == '':
            self._pay_type = 'CASH'
        else:
            raise ValueError('Invalid Payment Type')
