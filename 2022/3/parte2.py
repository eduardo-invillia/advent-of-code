from string import ascii_lowercase, ascii_uppercase


def parser(entrada):
    for line in zip(*[iter(entrada)] * 3):
        yield [l.strip() for l in line]


def encontrar_duplicado(a, b, c):
    b = set(b)
    c = set(c)
    for c_a in a:
        if c_a in b and c_a in c:
            return c_a


valores = {c: i for i, c in enumerate(ascii_lowercase + ascii_uppercase, start=1)}


total = 0
for mochilas in parser(open(0)):
    l = encontrar_duplicado(*mochilas)
    total += valores[l]
print(total)
