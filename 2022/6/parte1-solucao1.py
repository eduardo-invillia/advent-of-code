from collections import defaultdict
from itertools import chain

entrada = list(chain.from_iterable(open(0)))
tamanho = 4

for i in range(len(entrada)):
    print(i, i + tamanho, entrada[i : i + tamanho])
    d = defaultdict(int)
    for c in entrada[i : i + tamanho]:
        d[c] += 1
    if len(d) == tamanho:
        print(i + tamanho)
        break
