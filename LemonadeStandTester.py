# Author: Van Huynh
# GitHub username: huynhvan126
# Date: 10/09/2024
# Description: writing unit tests for lemon stand classes

import unittest
from LemonadeStand import MenuItem, SalesForDay, LemonadeStand, InvalidSalesItemError

class TestLemonadeStand(unittest.TestCase):
    """
    Unit tests for the LemonadeStand class, testing various functionalities such as adding menu items,
    handling sales, and calculating total sales and profit.
    """

    def setUp(self):
        """
        Set up the test environment by creating a LemonadeStand object with two menu items: lemonade and cookie.
        """
        self.stand = LemonadeStand("Lemons R Us")
        self.item1 = MenuItem('lemonade', 0.5, 1.5)
        self.item2 = MenuItem('cookie', 0.2, 1)
        self.stand.add_menu_item(self.item1)
        self.stand.add_menu_item(self.item2)

    def test_add_menu_item(self):
        """
        Test adding items to the menu. Ensures that the items 'lemonade' and 'cookie' are correctly added
        to the menu and can be retrieved by their name.
        """
        self.assertEqual(self.stand._menu['lemonade'].get_name(), 'lemonade')
        self.assertEqual(self.stand._menu['cookie'].get_name(), 'cookie')

    def test_sales_for_today_invalid(self):
        """
        Test that entering sales for an item not on the menu raises an InvalidSalesItemError.
        Ensures the program properly validates sales input.
        """
        sales = {'invalid_item': 5}
        with self.assertRaises(InvalidSalesItemError):
            self.stand.enter_sales_for_today(sales)

    def test_sales_of_menu_item_for_day(self):
        """
        Test the sales of a menu item for a specific day. Simulate sales for 'lemonade' and 'cookie',
        and check that the sales data is correctly recorded for that day.
        """
        sales = {'lemonade': 5, 'cookie': 2}
        self.stand.enter_sales_for_today(sales)
        self.assertEqual(self.stand.sales_of_menu_item_for_day(0, 'lemonade'), 5)
        self.assertEqual(self.stand.sales_of_menu_item_for_day(0, 'cookie'), 2)

    def test_total_sales_for_menu_item(self):
        """
        Test the total sales of a menu item across all days. Simulate sales of 'lemonade' and 'cookie',
        and check that the total number of items sold is correctly calculated.
        """
        sales = {'lemonade': 5, 'cookie': 2}
        self.stand.enter_sales_for_today(sales)
        self.assertEqual(self.stand.total_sales_for_menu_item('lemonade'), 5)
        self.assertEqual(self.stand.total_sales_for_menu_item('cookie'), 2)

    def test_total_profit_for_menu_item(self):
        """
        Test the total profit for a specific menu item ('lemonade') based on its wholesale cost and
        selling price. Simulate sales and verify that the calculated profit is correct.
        """
        sales = {'lemonade': 5}
        self.stand.enter_sales_for_today(sales)
        profit = (1.5 - 0.5) * 5  # profit per lemonade is $1.00
        self.assertEqual(self.stand.total_profit_for_menu_item('lemonade'), profit)

if __name__ == "__main__":
    unittest.main()
