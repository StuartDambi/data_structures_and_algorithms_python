def linear_search(search_set, target):
  '''
  Returns the position of the target if found, else return None
  '''
  for i in range(0, len(search_set)):
    if search_set[i] == target:
      return i
  return None

get_value = linear_search([1, 2, 3, 4, 6], 9)

def verify(value):
  if value == None:
    print('Value does not exist in list')
  else:
    print(f'Item was found at position {value}')

verify(get_value)