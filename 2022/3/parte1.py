from string import ascii_lowercase, ascii_uppercase


def parser(entrada):
    for line in entrada:
        line = line.strip()
        tamanho = len(line) // 2
        yield line[:tamanho], line[tamanho:]


# def encontrar_duplicado(a, b):  # O(n²)
#     for c_a in a:
#         for c_b in b:
#             if c_a == c_b:
#                 return c_a


# def encontrar_duplicado(a, b):  # O(n²)
#     for c_a in a:
#         if c_a in b:
#             return c_a


def encontrar_duplicado(a, b):  # O(n*log2n)
    b = set(b)
    for c_a in a:
        if c_a in b:
            return c_a


valores = {c: i for i, c in enumerate(ascii_lowercase + ascii_uppercase, start=1)}


total = 0
for a, b in parser(open(0)):
    c = encontrar_duplicado(a, b)
    total += valores[c]
print(total)
