def merge_sort(list):
  '''
  Sort a list in ascending order
  Returns a new sorted list

  Divide: Find the mid point of list and divide into sublists
  Conquer: Recursively sort the sublists created in previous step
  Combine: Merge the sorted sublists created in the previous step
  '''

  if len(list) <= 1:
    return list

  left_half, right_half = split(list)
  left = merge_sort(left_half)
  right = merge_sort(right_half)

  return merge(left, right)


# Split Function
def split(list):
  '''
  Divide unsorted list at midpoint into sublists
  Returns two sublists - left and right
  '''

  mid = len(list)//2
  left = list[:mid]
  right = list[mid:]
  return left, right

# Merge function
def merge(left, right):
  '''
  Merges two lists sorting them in the process
  Returns new merged list
  '''
  l = []
  i = 0
  j = 0
  while i < len(left) and j < len(right):
    if left[i] < right[j]:
      l.append(left[i])
      i+=1
    else:
      l.append(right[j])
      j+=1

  while i < len(left):
    l.append(left[i])
    i+=1

  while j < len(right):
    l.append(right[j])
    j+=1
  return l


l = merge_sort([1, 5, 7,2,9])
print(l)