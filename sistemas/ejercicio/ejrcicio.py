def promedio(**values):
  """
    Calcula promedio de n valores
  """
  c = 0
  count = 0

  for k, value in values.items():
    c += value
    count += 1

  return c / count

print(promedio(a=1, b=2, c=5))