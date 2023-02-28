def parse(entrada):
    for line in entrada:
        line = line.strip().split(' ')
        if len(line) >= 2:
            line[1] = int(line[1])
        yield line


def processador(instrucoes):
    X = 1
    for instrucao in instrucoes:
        if instrucao[0] == 'noop':
            yield X
        elif instrucao[0] == 'addx':
            yield X
            yield X
            X += instrucao[1]


sinal = 0
for i, x in enumerate(processador(parse(open(0))), start=1):
    if i in (20, 60, 100, 140, 180, 220):
        sinal += i * x
    if i == 220:
        break
print(sinal)
