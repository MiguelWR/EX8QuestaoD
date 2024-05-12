#Exercício 8

#d)

def Sd(p, q, n):
  if n == 0:
    return p
  elif n % 2 == 0:
    return Sd(p, q, n - 1) + q
  elif n % 2 != 0:
    return Sd(p, q, n - 1) - q


print(Sd(4, 6, 6))