import re

def trigrama_busca(mensagem_cifrada_tratada: str):
    trigramas = []

    for i in range(len(mensagem_cifrada_tratada)-2):
        trigrama = mensagem_cifrada_tratada[i:i+3]
        trigramas.append((trigrama, i))

    return trigramas

def histograma_trigrama(trigramas: list):
    histograma = {}

    for trigrama, ocurr in trigramas:
        if trigrama in histograma:
            histograma[trigrama]["freq"] += 1
            histograma[trigrama]["ocurr"].append(ocurr)
        else:
            histograma[trigrama] = {"freq": 1, "ocurr": [ocurr]}

    return histograma

def tratamento(mensagem_cifrada):
    mensagem_cifrada_tratada = re.sub(r"[^a-z]", r"", mensagem_cifrada)

    return mensagem_cifrada_tratada

def dvalue_calculate(histograma_trigrama_filtrado):
    dvalues = {}
    for trigrama in histograma_trigrama_filtrado:
        dvalues[trigrama] = []
        for i in range(len(histograma_trigrama_filtrado[trigrama]["ocurr"]) - 1):
            dvalues[trigrama].append(histograma_trigrama_filtrado[trigrama]["ocurr"][i+1] - histograma_trigrama_filtrado[trigrama]["ocurr"][i])
    return dvalues


def mdc(a, b):
    while b:
        a, b = b, a % b
    return a

def mdc_lista(lista):
    resultado = lista[0]
    for elemento in lista[1:]:
        resultado = mdc(resultado, elemento)
    return resultado

def key_size_probabilities(mensagem_cifrada, filtro_ocorrencias):
    mensagem_cifrada_tratada = tratamento(mensagem_cifrada)

    filtro_ocorrencias = 2

    histograma_trig = histograma_trigrama(trigrama_busca(mensagem_cifrada_tratada))
    histograma_trig = sorted(histograma_trig.items(), key=lambda x: x[1]["freq"], reverse=True)
    histograma_trigrama_filtrado = {trigrama: {"freq": dicionario["freq"], "ocurr": dicionario["ocurr"]} for
                                    trigrama, dicionario in histograma_trig if
                                    dicionario["freq"] > filtro_ocorrencias}

    dvalues = dvalue_calculate(histograma_trigrama_filtrado)

    size_score = {}
    divisor_list = [mdc_lista(dvalues[lista]) for lista in dvalues]

    for divisor in divisor_list:
        if divisor in size_score:
            size_score[divisor] += 1
        else:
            size_score[divisor] = 1

    size_score = sorted(size_score.items(), key=lambda x: x[1], reverse=True)

    with open("KeySize/SizeScore.txt", "w", encoding="utf-8") as file:
        for divisor in size_score:
            file.write(f"{divisor[0]}: {divisor[1] * 100 / len(divisor_list):.3f}%\n")
