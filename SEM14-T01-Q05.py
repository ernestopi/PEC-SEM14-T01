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

mes_niver = int(input())
populacao_lida = int(input())
meses = ('janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro')
meses_2 = ('JANEIRO','FEVEREIRO','MARÇO','ABRIL','MAIO','JUNHO','JULHO','AGOSTO','SETEMBRO','OUTUBRO','NOVEMBRO','DEZEMBRO')

ch = carrega_cidades()

print(f'CIDADES COM MAIS DE {populacao_lida} HABITANTES E ANIVERSÁRIO EM {meses_2[mes_niver-1]}:')
for c in ch:
    if mes_niver == c[4] and c[5] > populacao_lida:
        print(f'{c[2]}({c[0]}) tem {c[5]} habitantes e faz aniversário em {c[3]} de {meses[mes_niver-1]}.')
