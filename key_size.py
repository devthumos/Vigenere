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


if __name__ == "__main__":
    mensagem_cifrada = """tpsja kexis ttgztpb wq ssmil tfdxf vsetw ytafrttw btzf pcbroxdzo zn tqac wix, bwfd s, je ahvup sd pcbqqxff lfzed d avu ytwoxavneh sg p aznst qaghv. sfiseic f udh zgaurr dxnm rcdentv btzf nllgubsetz, wymh qfndbhqgotopl qq asmactq m prftlk huusieymi ythfdz: t tdxavict i cjs vu yts edi grzivupavnex yy pikoc wirjbko, xtw gb rvffgxa pikoc, iedp elex t gmbdr fzb sgiff bpkga; p gvgfghm t ele z xwogwko qbgmgwr adlmy bozs rtpmchv e xtme ccmo. xhmetg, hup meyqsd czgxaj o jul fsdis, eaz t tah bf iymvaxhf, mll ra roso: objqgsecl kepxqrl pgxdt sjtp emhgc v o axrfphvunh. huic zseh, ijewiet tw pjoj hzkee so kacwi pt ida dxbfp-tvict ha bsj dp tkahhf dp 1869, ge yxbya mxpm rvrclke pt qrtfffu. iwehl nre hsjspgxm t elaeks mccj, rtcse t diodiiddg, vrl lsxiszrz, isehiza nxvop rv tcxdqchfs nhrfdg v ffb eodagayaepd of cpfmftfzo ahv acnv axbkah. cezp tquvcj! vpkhmss v qfx rmd vfugx gmghrs yxq mciecthw. mrfvsnx ugt qyogbe — btbvictzm jar csnzucvr mtnhm, ifzsex i odbjtlgxq, iof czgwfpbke p mea ifzsex, ugt zvvzn yy sohupeie uwvid we gahzml asdp o znexvopzrr plxm tbxeyasep wuett ra swjcfkwa fiv pchjqgwl a mxmdp rv mtglm rcma: — “ghw, cjs f czglqrsjtpl, qqjg jeyasdtg, mod isptwj dtsid rcdirh ugt o eaenvqoo gacxgq tgkac vlagoedz t tqgrr ickibpfrvpe hq ja uod feuh pvlzl gmgottpkie fiv tpf lacfrdz t lgboeiothq. tgke lk wabpiiz, xwfpg xoetw pd qvu, ljyqaoj nfoizh sjcfkee fiv czuvqb c rzfe gabc lm nkibt tlnpkia, iiuo tlwa t o uoc vvgp s da bni xws iot t rmiiiekt ee bozs tgxuboj eymvmcvrs; enha xgjo p nq ejpcixx pajjfr lh rahgf iwnwfgs wiytha.” qcd e qbix pazgz! gea, cof mp tvdtdvnoh hmh jznex ebdzzcpl ugt zye oxmjtw. v fzb eehwd qfx gttulet t gxpijuwt hah avud wmmh; tfi llwub ele xx izrodiyaiu eoia z nrpxgtogxvqs qfuymvk ss yaxeif, hsd ad âgwupg eex tw pjjzdll ha bcto akmzrwge, xtw bpijaoh i fgcgerh gabc hupf wq gskict xmgrv dz xwbthrcfes. fpfue p tfagfvctws. hxfrmxx md jars yhzq di uek iiehcrs, pgxdt scad mvqh gvnshvmh, aznst mdbo jambrm, rojaot gab c toekmy, p tzlst, — yy awiiz ws hpzv, — e... exrtpa ganbizrwr! dljyu p dfunh pttg uicxm cjsd ect e ftftetke etbyoct. gachvnexq-et rv sluid fiv edle mcceixt, eucrr qfx rmd drrpgxm, eouenxy ypwj dz jyq pg gacxrfpg. v vpkhmss, gaoxgqj arid. gea swxo bni et qrrabwet, bro obka fiv sp wiumojsp ksxpf gewh gtpc, toyoyxho. eex h qqj csieh idp qfidt exiodeymi pgodaebgm... ja jowmiugof qfx ijewia lhw etgjeyme q firtch ezdg, eaz iedtqv qfx vqjbr ex lm fdrfs zl ixtavnehw pt ida ekestrza. p wepd ele dbq, a fiv mpgse rcevtglm p sjsl tracwda pke meoieyme-xd. rv pp, t gmqstetke pp qrml, vsy dg flshw qhhlptwse, p pfcl xrfgsrbpkxm, p hiidmi etbyoct qma dfdtt gdtf ea xbrtp sottggmd."""
    mensagem_cifrada_tratada = tratamento(mensagem_cifrada)

    filtro_ocorrencias = 2

    histograma_trigrama = histograma_trigrama(trigrama_busca(mensagem_cifrada_tratada))
    histograma_trigrama = sorted(histograma_trigrama.items(), key=lambda x: x[1]["freq"], reverse=True)
    histograma_trigrama_filtrado = {trigrama: {"freq": dicionario["freq"], "ocurr": dicionario["ocurr"]} for
                                    trigrama, dicionario in histograma_trigrama if
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
