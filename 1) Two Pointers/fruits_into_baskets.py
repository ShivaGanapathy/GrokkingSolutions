def fruits_into_baskets(fruits):
  lp = rp = 0
  storage = {}
  output = 0
  for rp in range(len(fruits)):
    if fruits[rp] not in storage:
      storage[fruits[rp]] = 0
    storage[fruits[rp]] +=1

    while len(storage.keys()) > 2:
      storage[fruits[lp]] -=1
      if storage[fruits[lp]]==0:
        del storage[fruits[lp]]
      
      lp+=1

    output = max(output, rp-lp+1)

  return output
      


