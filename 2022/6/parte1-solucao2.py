from itertools import chain

entrada = list(chain.from_iterable(open(0)))
tamanho = 4

for i in range(len(entrada)):
    print(i, i + tamanho, entrada[i : i + tamanho])
    d = set(entrada[i : i + tamanho])
    if len(d) == tamanho:
        print(i + tamanho)
        break
