dict = ['địa chỉ', 'trường học', 'bùi thị xuân']
def tim_tughep(t):
  input = t.split()
  list_tughep = []
  n = 0
  while True:
    i = len(input)
    while i > n:
      tu_ghep = input[n:i]
      tu = ''
      for x in tu_ghep:
        tu += x + ' '
      tu = tu[:-1]
      i -= 1
      if tu.lower() in dict:
        list_tughep.append(tu)
        break
      if i == n:
        list_tughep.append(tu)
        break
    
    if i >= len(input):
      break

    n = i + 1

  return list_tughep

print(tim_tughep('Địa chỉ trường học Bùi Thị Xuân'))
    