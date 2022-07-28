def split_bill(bill, k, b):
  sum_of_items = 0
  anna_balance = 0
  if k < len(bill):
    bill.pop(k)
    for item in bill:
      sum_of_items = sum_of_items + item
    anna_balance = int(b - (sum_of_items/2))
    print(anna_balance)
  else:
    for item in bill:
      sum_of_items = sum_of_items + item
    print('Bon appetit')
  


split_bill([2, 4, 7], 7, 13)
# bal 