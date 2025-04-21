"""
Membership Class

This class manages membership tiers for users in a fictional membership program called PacCommerce.
It provides functionalities to display benefits and requirements associated with different membership levels,
predict suitable memberships based on user financial data, and calculate total prices after applying discounts.

Attributes:
- users (dict): A dictionary mapping user names to their respective membership levels.
- membership_table (list): A list containing details about each membership level, including discount percentages 
  and additional benefits.
- requirements_membership_table (list): A list detailing the monthly expense and income requirements for each 
  type of membership.

Methods:
- __init__(self): Initializes the Membership object with predefined users, benefits, and requirements data.
- show_benefit(self): Displays the benefits associated with each type of membership in a formatted table.
- show_requirements(self): Displays the monthly expense and income requirements for each type of 
  membership in a formatted table.
- predict_membership(self, monthly_expense, monthly_income): Predicts which membership level is most suitable 
  based on provided monthly expense and income using Euclidean distance calculation from requirement points.
- calculate_price(self, membership, list_harga_barang): Calculates total price after applying discounts based 
  on selected member's tier. It sums up item prices from 'list_harga_barang', applies appropriate discount,
  then prints out final amount after discounting.

Usage Example:
To use this class:
1. Create an instance: `membership = Membership()`
2. Display benefits: `membership.show_benefit()`
3. Display requirements: `membership.show_requirements()`
4. Predict suitable membership: `predicted = membership.predict_membership(monthly_expense=7, monthly_income=12)`
5. Calculate discounted price: `membership.calculate_price(membership='Gold', list_harga_barang=[1000000, 2000000])`

This code is designed for educational purposes or as part of an application managing customer memberships
and their corresponding discounts at PacCommerce.

Author: [Fathur Imam M]
Date Created: [18 April 2025]
"""
