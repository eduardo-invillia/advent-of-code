from itertools import chain
from string import ascii_lowercase

tamanho = 4
posicao_das_letras = [-1 for _ in ascii_lowercase]
ultima_duplicidade = -1
for i, c in enumerate(ord(c) for c in chain.from_iterable(open(0))):
    j = c - ord('a')
    if posicao_das_letras[j] > ultima_duplicidade:
        ultima_duplicidade = posicao_das_letras[j]
    else:
        if i - ultima_duplicidade == tamanho:
            print(i + 1)
            break
    posicao_das_letras[j] = i
