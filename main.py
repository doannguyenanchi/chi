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
                list_tughep.append(tu)
                break

        if r >= len(input):
            break

        l = r + 1

    list_tughep.pop()
    return list_tughep

print(tim_tughep('Địa chỉ trường'))
