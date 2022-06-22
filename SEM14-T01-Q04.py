def carrega_cidades():
    resultado = []
    with open('cidades.csv', 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            uf, ibge, nome, dia, mes, pop = linha.split(';')
            resultado.append(
                (uf, int(ibge), nome, int(dia), int(mes), int(pop))
            )
    arquivo.close()
    return resultado

populacao_lida = int(input())

ch = carrega_cidades()

print(f'CIDADES COM MAIS DE {populacao_lida} HABITANTES:')

for c in ch:
    if c[5] > populacao_lida:
        print(f'IBGE: {c[1]} - {c[2]}({c[0]}) - POPULAÇÃO: {c[5]}')