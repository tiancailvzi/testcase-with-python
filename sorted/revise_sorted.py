#method 1
def revise_comp(x,y):
  if x > y :
    return -1
  elif x == y :
    return 0
  else :
    return 1
    
sorted([1,2,4,6,7],revise_comp)


# method 2

sorted([1,2,4,6,7])[::-1]
  
