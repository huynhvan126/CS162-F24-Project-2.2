# Author: Van Huynh
# GitHub username: huynhvan126
# Date: 10/09/2024
# Description: Writing code for recording the menu items and daily sales of a lemonade stand.
class InvalidSalesItemError(Exception):
    """
    Custom exception raised when an attempt is made to record sales for an item not in the menu.
    """
    pass

class MenuItem:
    """
    Represents a menu item with a name, wholesale cost, and selling price.
    """
    def __init__(self, name, wholesale_cost, selling_price):
        """
        Initializes a MenuItem with the provided name, wholesale cost, and selling price.
        """
        self._name = name
        self._wholesale_cost = wholesale_cost
        self._selling_price = selling_price

    def get_name(self):
        """
        Returns the name of the menu item.
        """
        return self._name

    def get_wholesale_cost(self):
        """
        Returns the wholesale cost of the menu item.
        """
        return self._wholesale_cost

    def get_selling_price(self):
        """
        Returns the selling price of the menu item.
        """
        return self._selling_price

class SalesForDay:
    """
    Represents the sales data for a specific day.
    """
    def __init__(self, day, sales_dict):
        """
        Initializes a SalesForDay object for the given day with the sales data.
        """
        self._day = day
        self._sales_dict = sales_dict

    def get_day(self):
        """
        Returns the day number.
        """
        return self._day

    def get_sales_dict(self):
        """
        Returns the sales dictionary for the day.
        """
        return self._sales_dict

class LemonadeStand:
    """
    Represents a lemonade stand that tracks menu items and daily sales.
    """
    def __init__(self, name):
        """
        Initializes a LemonadeStand with the provided name and empty menu and sales record.
        """
        self._name = name
        self._current_day = 0
        self._menu = {}  # dictionary of MenuItem objects
        self._sales_record = []  # list of SalesForDay objects

    def get_name(self):
        """
        Returns the name of the lemonade stand.
        """
        return self._name

    def add_menu_item(self, menu_item):
        """
        Adds a menu item to the lemonade stand.
        """
        self._menu[menu_item.get_name()] = menu_item

    def enter_sales_for_today(self, sales_dict):
        """
        Records the sales for the current day. Raises an InvalidSalesItemError if an item in the sales
        is not found in the menu.
        """
        for item in sales_dict:
            if item not in self._menu:
                raise InvalidSalesItemError(f"'{item}' not in the menu")

        self._sales_record.append(SalesForDay(self._current_day, sales_dict.copy()))
        self._current_day += 1

    def sales_of_menu_item_for_day(self, day, item_name):
        """
        Returns the quantity of a specific menu item sold on a specific day.
        """
        for record in self._sales_record:
            if record.get_day() == day:
                sales_dict = record.get_sales_dict()
                return sales_dict.get(item_name, 0)
        return 0

    def total_sales_for_menu_item(self, item_name):
        """
        Returns the total quantity of a specific menu item sold across all days.
        """
        total_sales = 0
        for record in self._sales_record:
            sales_dict = record.get_sales_dict()
            total_sales += sales_dict.get(item_name, 0)
        return total_sales

    def total_profit_for_menu_item(self, item_name):
        """
        Calculates the total profit for a specific menu item based on its wholesale cost and selling price.
        """
        menu_item = self._menu.get(item_name)
        if not menu_item:
            return 0
        total_sales = self.total_sales_for_menu_item(item_name)
        profit_per_item = menu_item.get_selling_price() - menu_item.get_wholesale_cost()
        return total_sales * profit_per_item


    def total_profit_for_stand(self):
        """
        Calculates the total profit for the lemonade stand by summing the profits of all menu items.
        """
        total_profit = 0
        for item_name in self._menu:
            total_profit += self.total_profit_for_menu_item(item_name)
        return total_profit

# Main function
def main ():
    """
    Main function that runs the lemonade stand, add menu items, and record daily sales.
    """
    stand = LemonadeStand('Lemons R Us') # Create a new LemonadeStand called 'Lemons R Us'

# add menu items
    item1 = MenuItem('lemonade', 0.5, 1.5) # Create lemonade as a menu item (wholesale cost 50 cents, selling price $1.50)
    item2 = MenuItem('nori', 0.6, 0.8) # Create nori as a menu item (wholesale cost 60 cents, selling price 80 cents)
    item3 = MenuItem('cookie', 0.2, 1) # Create cookie as a menu item (wholesale cost 20 cents, selling price $1.00)
    stand.add_menu_item(item1) # Add lemonade to the menu for 'Lemons R Us'
    stand.add_menu_item(item2) # Add nori to the menu for 'Lemons R Us'
    stand.add_menu_item(item3) # Add cookie to the menu for 'Lemons R Us'

# Sales dictionary
    day_0_sales = {'lemonade': 5, 'cookie': 2, 'not_in_the_menu': 1}

# Try/except block for invalid sales
    try:
        stand.enter_sales_for_today(day_0_sales)
    except InvalidSalesItemError as e:
        print(f'Error: {e}')

if __name__ == '__main__':
    main()