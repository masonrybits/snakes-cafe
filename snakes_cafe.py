menu = {
  'Appetizers': ['Wings', 'Cookies', 'Spring Rolls'],
  'Entrees': ['Salmon', 'Steak', 'Meat Tornado', 'A Literal Garden'],
  'Desserts': ['Ice Cream', 'Cake', 'Pie'],
  'Drinks': ['Coffee', 'Tea', 'Unicorn Tears'],
}

def print_welcome():
  print('*' * 38 + '\n' + '*' * 2 + ' ' * 4 + 'Welcome to the Snakes Cafe!' + ' ' * 3 + '*' * 2 + '\n' + '*' * 2 + ' ' * 4 + 'Please see our menu below.' + ' ' * 4 + '*' * 2 + '\n' + '*' * 2 + ' ' * 36 + '\n' + '*' * 2 + ' ' * 1 + 'To quit at any time, type "quit"' + ' ' * 1 + '*' * 2 + '\n' + '*' * 38 + '\n') 

def print_order():
  print('*' * 35 + '\n' + '*' * 2 + ' ' * 1 + 'What would you like to order?' + ' ' * 1 + '*' * 2 + '\n' + '*' * 35)

def print_menu():
  for x, y in menu.items():
    print (x)
    print ('-' * 8)
    for i in y:
      print(i)
    print ('\n')

def take_order():
  orders = {}
  order = input()
  while order != 'quit':
    if order in orders:
      orders[order] += 1
    else:
      orders[order] = 1
    print(f'** {orders[order]} of {order} have been added to your meal **'
    )
    order = input()

print_welcome()
print_menu()
print_order()
take_order()