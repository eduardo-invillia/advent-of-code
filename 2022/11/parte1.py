from heapq import nlargest
from operator import mul

'''
macacos = [
    {
        'itens': [79, 98],
        'operacao': lambda x: x * 19,
        'test': 23,
        True: 2,
        False: 3,
        'inspecionados': 0,
    },
    {
        'itens': [54, 65, 75, 74],
        'operacao': lambda x: x + 6,
        'test': 19,
        True: 2,
        False: 0,
        'inspecionados': 0,
    },
    {
        'itens': [79, 60, 97],
        'operacao': lambda x: x * x,
        'test': 13,
        True: 1,
        False: 3,
        'inspecionados': 0,
    },
    {
        'itens': [74],
        'operacao': lambda x: x + 3,
        'test': 17,
        True: 0,
        False: 1,
        'inspecionados': 0,
    },
]
'''

macacos = [
    {
        'itens': [66, 59, 64, 51],
        'operacao': lambda x: x * 3,
        'test': 2,
        True: 1,
        False: 4,
        'inspecionados': 0,
    },
    {
        'itens': [67, 61],
        'operacao': lambda x: x * 19,
        'test': 7,
        True: 3,
        False: 5,
        'inspecionados': 0,
    },
    {
        'itens': [86, 93, 80, 70, 71, 81, 56],
        'operacao': lambda x: x + 2,
        'test': 11,
        True: 4,
        False: 0,
        'inspecionados': 0,
    },
    {
        'itens': [94],
        'operacao': lambda x: x * x,
        'test': 19,
        True: 7,
        False: 6,
        'inspecionados': 0,
    },
    {
        'itens': [71, 92, 64],
        'operacao': lambda x: x + 8,
        'test': 3,
        True: 5,
        False: 1,
        'inspecionados': 0,
    },
    {
        'itens': [58, 81, 92, 75, 56],
        'operacao': lambda x: x + 6,
        'test': 5,
        True: 3,
        False: 6,
        'inspecionados': 0,
    },
    {
        'itens': [82, 98, 77, 94, 86, 81],
        'operacao': lambda x: x + 7,
        'test': 17,
        True: 7,
        False: 2,
        'inspecionados': 0,
    },
    {
        'itens': [54, 95, 70, 93, 88, 93, 63, 50],
        'operacao': lambda x: x + 4,
        'test': 13,
        True: 2,
        False: 0,
        'inspecionados': 0,
    },
]

for _ in range(20):
    for macaco in macacos:
        for item in macaco['itens']:
            item = macaco['operacao'](item) // 3
            macacos[macaco[item % macaco['test'] == 0]]['itens'].append(item)
            macaco['inspecionados'] += 1
        macaco['itens'] = []

maiores = nlargest(2, (macaco['inspecionados'] for macaco in macacos))
print(mul(*maiores))
