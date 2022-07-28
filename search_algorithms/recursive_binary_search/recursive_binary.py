def recursive_binary_search(search_list, target):
  if len(search_list) == 0:
    return False
  else:
    midpoint = (len(search_list))//2
    if search_list[midpoint] == target:
      return True
    else:
      if search_list[midpoint] < target:
        return recursive_binary_search(search_list[midpoint+1:], target)
      else:
        return recursive_binary_search(list[:midpoint], target)

print(recursive_binary_search([1,2,3,4,5,6], 4))