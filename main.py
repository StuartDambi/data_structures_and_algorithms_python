age = 70
name = 'Stuart'
is_mature = True
books = ['age of altron', 'Ways to kill a rat', 10, 'a']
dictionary = {'name': 'Stuart', 'age': 38, 'school': 'WPS'}

print(dictionary)
print(books)

def calculate_age(year_of_birth, current_year):
  age = current_year - year_of_birth
  print(age)

def get_my_age():
  year_of_birth = input('Enter your year of birth: ')
  current_year = input('What is the year today: ')
  age = int(current_year) - int(year_of_birth)
  print(age)

# Logic statements
if is_mature:
  print('This boy is old')
else:
  print('he is a young boy')

# Loops
# Print even numbers between 1 and 10
x = 0
for x in range(10, 20):
  if x%2 == 0:
    print(x)

while x < 20:
  print(x)

# calculate_age(1996, 2028)
# get_my_age()  