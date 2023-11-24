def funk(n):
  if n<0:
    return 0
  elif n==0:
     return 2
  else:
     return funk(n-1) + 3*funk(n-2) + 2 

print(funk(6))