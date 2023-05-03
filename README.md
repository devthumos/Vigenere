# Vigenere Devthumos Tool

Vigenere Devthumos Tool é uma aplicação Python para cifrar, decifrar e analisar mensagens usando a cifra de Vigenère. A ferramenta também oferece recursos para encontrar tamanhos de chave prováveis e visualizar a distribuição dos grupos de trigramas através do Power BI.

## Funcionalidades

1. Encriptar: cifra uma mensagem usando a cifra de Vigenère e uma chave fornecida.
2. Decriptar: decifra uma mensagem cifrada usando a cifra de Vigenère e uma chave fornecida.
3. Probabilidades de Tamanhos de Chave: analisa a mensagem cifrada para encontrar prováveis tamanhos de chave.
4. Distribuição dos Agrupamentos em Power BI: visualiza a distribuição dos grupos de trigramas em um arquivo CSV para análise no Power BI.

## Utilização

Ao executar o programa, você verá um menu principal com as seguintes opções:

1. Encriptar
2. Decriptar
3. Probabilidades de Tamanhos de Chave
4. Distribuição dos Agrupamentos em Power BI
5. Sair

Digite o número correspondente à opção desejada e siga as instruções na tela.

## Opções do Menu Principal

1. Encriptar
   - Função: Cifra uma mensagem usando a cifra de Vigenère e uma chave fornecida.
   - Parâmetros: Chave (uma palavra ou frase) para cifrar a mensagem.
   - Arquivo utilizado: "Mensagens/Mensagem_Original.txt"
   - Instruções: Digite a chave desejada quando solicitado e pressione Enter. A mensagem cifrada será gerada no arquivo "Mensagens/Mensagem_Cifrada.txt".

2. Decriptar
   - Função: Decifra uma mensagem cifrada usando a cifra de Vigenère e uma chave fornecida.
   - Parâmetros: Chave (uma palavra ou frase) para decifrar a mensagem.
   - Arquivo utilizado: "Mensagens/Mensagem_Cifrada.txt"
   - Instruções: Digite a chave desejada quando solicitado e pressione Enter. A mensagem decifrada será gerada no arquivo "Mensagens/Mensagem_Decifrada.txt".

3. Probabilidades de Tamanhos de Chave
   - Função: Analisa a mensagem cifrada para encontrar prováveis tamanhos de chave usando o teste de Kasiski.
   - Parâmetros: Número mínimo de ocorrências de trigramas para filtrar e melhorar ainda mais o teste de Kasiski.
   - Arquivo utilizado: "Mensagens/Mensagem_Cifrada.txt"
   - Instruções: Pressione Enter para iniciar a análise. Os prováveis tamanhos de chave serão exibidos na tela e também salvos no arquivo "KeySize/SizeScore.txt".

4. Distribuição dos Agrupamentos em Power BI
   - Função: Escreve a distribuição dos grupos de trigramas em um arquivo CSV para análise no Power BI.
   - Parâmetros: Tamanho da chave (um número inteiro) encontrado na análise do índice de coincidência.
   - Arquivo utilizado: "Mensagens/Mensagem_Cifrada.txt"
   - Instruções: Digite o tamanho da chave quando solicitado e pressione Enter. O arquivo "Distributions/distribution.csv" será gerado com os dados de distribuição dos grupos de trigramas.

5. Sair
   - Função: Encerra o programa.
   - Parâmetros: Nenhum.
   - Instruções: Digite 5 no menu principal e pressione Enter para sair do programa.


## Arquivos Gerados

A aplicação gera os seguintes arquivos de saída:

1. "Mensagens/Mensagem_Cifrada.txt": contém a mensagem cifrada.
2. "Mensagens/Mensagem_Decifrada.txt": contém a mensagem decifrada.
3. "KeySize/SizeScore.txt": contém as probabilidades dos tamanhos de chave.
4. "Distributions/distribution.csv": contém a distribuição dos grupos de trigramas para análise no Power BI.

## Análise no Power BI

Para analisar a distribuição dos grupos de trigramas no Power BI, siga os passos abaixo:

1. Abra o arquivo "Dashboards/dashboard_de_distribuicao.pbix" no Power BI.
2. Atualize a fonte de dados para incluir o arquivo "Distributions/distribution.csv" gerado pelo programa.