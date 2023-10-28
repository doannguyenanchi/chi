import json

try:
  with open('tudien_d.json', 'r', encoding='utf-8') as f:
    dictionary = json.load(f)
except FileNotFoundError:
  pass


def tim_tughep(t):
    dict = dictionary.keys()
    input = t.split()
    list_tughep = []
    l = 0
    while True:
        r = l + 3
        while r > l:
            tu_ghep = input[l:r]
            tu = ''
            for x in tu_ghep:
                tu += x + ' '
            tu = tu[:-1]
            r -= 1
            if tu in dict:
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

print(tim_tughep('địa chỉ trường Bùi Thị Xuân'))
