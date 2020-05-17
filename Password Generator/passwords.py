import random
print('''\nPassword Generator\n==================\n''')
number = int(input('How many passwords do you want?\n'))
length = int(input('''What must be each password's length?\n'''))
print('\nHere are your passwords:')

for pwd in range(number):
  password = ''
  for c in range(length):
    password += chr(random.randint(33,125))
  print(password)
