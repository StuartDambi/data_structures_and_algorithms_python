from hashlib import new


class Person():
  def __init__(self, salary, tax, age):
    self.salary = salary
    self.tax = tax
    self.age = age

  def increase_salary(self, salary_increment):
    self.salary = self.salary + salary_increment
    print(self.salary)

  def calculate_employee_tax(self):
    if self.salary > 6000:
      self.tax = 0.1 * self.salary
      print(f'Your tax is {self.tax}')
    elif self.salary > 10000:
      self.tax = 0.2 * self.salary
      print(f'Your tax is {self.tax}')
    else:
      print('You cant pay tax')

new_person = Person(5000, 0, 25)

new_person.increase_salary(7000)

new_person.calculate_employee_tax()

# Inheritance