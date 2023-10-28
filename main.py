import json

try:
  with open('tudien.json', 'r', encoding='utf-8') as f:
    dictionary = json.load(f)
except FileNotFoundError:
  pass

def tim_tughep(t):
    dict = []
    for i in dictionary.keys():
        dict.append(i.lower())
    input = t.split()
    list_tughep = []
    l = 0
  
    while True:
        r = l + 3
        while r > l:
            tu_ghep = input[l:r]
            tu = ' '.join(tu_ghep)
            r -= 1
          
            if tu.lower() in dict:
                list_tughep.append(tu)
                break
              
            if r == l:
                list_tughep.append(tu)
                break

        if r >= len(input):
            break

        l = r + 1

    list_tughep.pop()
    return list_tughep
