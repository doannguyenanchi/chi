import json
from pathlib import Path

SH = Path(__file__).parent
dictionary = json.loads(Path(SH/'tudien_d.json').read_text())

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
            tu = ' '.join(input[l:r])

            r -= 1

            if tu.lower() in dict:
                list_tughep.append(tu)
                break

            if r == l:
                if tu: list_tughep.append(tu)
                break

        if r >= len(input):
            break

        l = r + 1

    return list_tughep

i='Địa chỉ trường';                  print(f'''{i=:<33} {','.join(tim_tughep(i))=:>}''')
i='Địa chỉ trường Bùi Thị Xuân';     print(f'''{i=:<33} {','.join(tim_tughep(i))=:>}''')
i='Địa chỉ trường học Bùi Thị Xuân'; print(f'''{i=:<33} {','.join(tim_tughep(i))=:>}''')
