from itertools import count


def parse(entrada):
    for line in entrada:
        line = line.strip().split(' ')
        if len(line) >= 2:
            line[1] = int(line[1])
        yield line


def processador(instrucoes):
    x = 1
    for instrucao in instrucoes:
        if instrucao[0] == 'noop':
            yield x
        elif instrucao[0] == 'addx':
            yield x
            yield x
            x += instrucao[1]


def crt():
    for i in count(0):
        x = yield
        j = i % 40
        if x - 1 <= j <= x + 1:
            print('#', end='')
        else:
            print('.', end='')
        if j == 39:
            print()


tela = crt()
next(tela)
for x in processador(parse(open(0))):
    tela.send(x)
