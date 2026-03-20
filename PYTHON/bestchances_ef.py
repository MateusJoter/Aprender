import pandas as pd

def contar_probabilidade(giros):
    jogadores = 150
    n_epicos = 147
    prob_n = 1

    while giros != 0:
        if jogadores == 0:
            break

        prob_n = prob_n*(n_epicos/jogadores)

        giros += -1
        jogadores += -1
        n_epicos += -1
    
    return 1 - prob_n

def calcular_giros(moedas):
    giros = 10*(moedas//900) + (moedas%900)/100

    return giros

def calcular_90perc():
    moedas = 0
    giros = 0
    probabilidade = 0

    while probabilidade < 0.9:
        moedas += 100
        giros = calcular_giros(moedas)
        probabilidade = contar_probabilidade(giros)

    return(moedas)

def elabora_dados():
    moedas_max = calcular_90perc()
    moedas = 0

    dados = {'giros/vez': [], 'qntd_inteira': [], 'giros_resto': [], 'prob': []}

    print('Calculando tuas probabilidades de tirar um épico .   .   .')

    for i in range(int(moedas_max/100)):
        moedas += 100

        giros = calcular_giros(moedas)
        dados['giros/vez'].append(int(giros))

        qntd_inteira = moedas_max//moedas
        dados['qntd_inteira'].append(int(qntd_inteira))

        giros_resto = (moedas_max%moedas)/100
        dados['giros_resto'].append(int(giros_resto))

        if giros_resto == 0:
            prob = 1 - ((1 - contar_probabilidade(giros))**qntd_inteira)
        else:
            prob = 1 - ((1 - contar_probabilidade(giros))**qntd_inteira)*(1 - contar_probabilidade(giros_resto))
        dados['prob'].append(str(round(100*prob, 2)) + '%')

    return dados

def salva_planilha(dados):
    df = pd.DataFrame(dados)
    df.to_csv('probabilidades_giros_efootball.csv', sep = ';', index = False)
    print('Resultados salvos!!!')

dados = elabora_dados()

salva_planilha(dados)