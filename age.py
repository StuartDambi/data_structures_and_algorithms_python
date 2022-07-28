def get_my_age():
  year_of_birth = input('Enter your year of birth: ')
  current_year = input('What is the year today: ')
  try:
    age = int(current_year) - int(year_of_birth)
    print(age)
  except:
    print("Please enter a valid year")

get_my_age()