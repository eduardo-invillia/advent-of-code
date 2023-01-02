def parser(entrada):
    grupo = []
    for line in entrada:
        line = line.strip()
        if line:
            grupo.append(int(line))
        else:
            yield grupo
            grupo = []
    if grupo:
        yield grupo


def soma(entrada):
    for lista in entrada:
        yield sum(lista)


print(max(soma(parser(open(0)))))
