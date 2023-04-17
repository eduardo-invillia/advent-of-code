from collections import defaultdict
from itertools import chain

entrada = list(chain.from_iterable(open(0)))
tamanho = 4

d = defaultdict(int)
for i, c in enumerate(entrada):
    d[c] += 1
    if i - tamanho >= 0:
        d[entrada[i - tamanho]] -= 1
    print(d)
    if len([s for s in d.values() if s == 1]) == tamanho:
        print(i + 1)
        break
