class Category:
    def __init__(self, category):
        self.ledger = {'amount': [], 'description': []}
        self.category = category

    def check_amount(self, amount):
        if amount > sum(self.ledger['amount']):
            return False
        else: return True

    def deposit(self, amount, description=''):
        self.ledger['amount'].append(amount)
        self.ledger['description'].append(description)

    def withdraw(self, amount, description=''):
        if self.check_amount(amount):
            self.ledger['amount'].append(amount * -1)
            self.ledger['description'].append(description)

            return True

        else: return False

    def get_balance(self):
        return sum(self.ledger['amount'])

    def transfer(self, amount, to):
        if self.check_amount(amount):
            self.withdraw(amount, f'Transfer to {to.category}')
            to.deposit(amount)

    def __repr__(self):
        amt_list = []
        description_list = []
        string_list = [self.category.center(30, '*')]

        for i in self.ledger['amount']:
            amt_list.append(i)

        for i in self.ledger['description']:
            description_list.append(i)

        for i in range(len(amt_list)):
            string_list.append(f'{description_list[i][:22].ljust(23)}{str("{:.2f}".format(amt_list[i])).rjust(7)}')

        string_list.append(f'Total: {"{:.2f}".format(self.get_balance())}')

        return '\n'.join(string_list)


def create_spend_chart(categories):
    graph = f'''
    Percentage Spent per Category
    100 |
    90  |
    80  |
    70  |
    60  |
    50  |
    40  |
    30  |
    20  |
    10  |
    0   |
         -----------------
    '''

    return graph


food = Category('Food')
food.deposit(300, 'initial deposit')
food.withdraw(50, 'purchased food for the restaurant')
print(food.get_balance())

clothing = Category('Clothing')
clothing.deposit(100, 'initial deposit')
food.transfer(100, clothing)
print(food.get_balance())
print(clothing.get_balance())

print(food)
print(create_spend_chart())
