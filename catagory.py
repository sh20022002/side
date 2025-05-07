class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = []

    def withdraw(self, amount, description=''):
        """ Withdraw amount if funds are available. """
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        return False

    def deposit(self, amount, description=''):
        """ Deposit amount into category ledger. """
        self.ledger.append({'amount': amount, 'description': description})

    @property
    def get_balance(self):
        """ Returns current balance of the category. """
        return sum(item['amount'] for item in self.ledger)

    def transfer(self, amount, category):
        """ Transfers amount from one category to another if funds are available. """
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {category.category}')
            category.deposit(amount, f'Transfer from {self.category}')
            return True
        return False

    def check_funds(self, amount):
        """ Checks if the amount can be withdrawn. """
        return amount <= self.get_balance

    def __str__(self) -> str:
        """ Returns a string representation of the category ledger. """
        head = self.category.center(30, '*') + '\n'
        total = 0

        for item in self.ledger:
            description = item['description'][:23].ljust(23)  # Limit to 23 chars
            amount = f"{item['amount']:.2f}".rjust(7)  # Right-align amount
            head += f"{description}{amount}\n"
            total += item['amount']

        head += f"Total: {total:.2f}"
        return head


def create_spend_chart(categories):
    """ Generates a spending chart showing percentage spent by category. """

    # Calculate total spending per category (only withdrawals)
    total_spent = 0
    spent_per_category = []

    for category in categories:
        spent = sum(item['amount'] for item in category.ledger if item['amount'] < 0)
        spent_per_category.append(abs(spent))  # Store positive values
        total_spent += abs(spent)

    # Convert spending to percentages
    percentages = [(spent / total_spent) * 100 for spent in spent_per_category]

    # Chart header
    chart = "Percentage spent by category\n"

    # Create y-axis with 100% down to 0% in increments of 10
    for i in range(100, -1, -10):
        chart += f"{str(i).rjust(3)}| "
        for percentage in percentages:
            chart += "o  " if percentage >= i else "   "
        chart += "\n"

    # Add the horizontal line
    chart += "    " + "-" * (3 * len(categories) + 1) + "\n"

    # Find the longest category name
    max_length = max(len(category.category) for category in categories)

    # Print category labels vertically
    for i in range(max_length):
        chart += "     "  # Left spacing
        for category in categories:
            chart += (category.category[i] + "  ") if i < len(category.category) else "   "
        if i < max_length - 1:
            chart += "\n"  # Add a newline if not the last row

    return chart


# Example Usage
food_category = Category("Food")
clothing_category = Category("Clothing")
auto_category = Category("Auto")

food_category.deposit(1000, "initial deposit")
food_category.withdraw(10.15, "groceries")
food_category.withdraw(15.89, "restaurant and more food")
clothing_category.deposit(100, "initial deposit")
clothing_category.withdraw(50, "clothes shopping")
auto_category.deposit(100, "initial deposit")
auto_category.transfer(50, clothing_category)

categories = [food_category, clothing_category, auto_category]

# Print category details
print(food_category)
print(clothing_category)
print(auto_category)

# Print the spending chart
print(create_spend_chart(categories))
