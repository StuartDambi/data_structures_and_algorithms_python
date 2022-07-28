# Notes
# Precondition to binary search algorithm
# is that the list has to be sorted

def binary_search(search_list, target):
  first = 0
  last = len(search_list) - 1

  while first <= last:
    midpoint = (first + last)//2
    if (search_list[midpoint] == target):
      return midpoint
    elif midpoint < target:
      first = midpoint + 1
    else:
      last = midpoint - 1

  return None

def verify(value):
  if value == None:
    print('Value does not exist in list')
  else:
    print(f'Item was found at position {value}')

result = binary_search([1,2 ,3,4 ,5], 3)

verify(result)