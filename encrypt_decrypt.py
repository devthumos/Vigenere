import re

class VigenereCypher():
    def mapping(self, alfabeto) -> list:
        mapping_matrix = [[chr((linha + i) % len(alfabeto) + ord("a"))
                            for i in range(len(alfabeto))]
                            for linha in range(len(alfabeto))]

        return mapping_matrix

    def encrypt(self, mensagem_original, chave, mapping_matrix, alfabeto):
        mensagem_cifrada = ""

        indice = 0
        indice_alfabeto = 0
        while indice < mensagem_original[1]:
            if mensagem_original[0][indice] in alfabeto:
                coluna = ord(mensagem_original[0][indice]) - ord("a")
                linha = ord(chave[0][indice_alfabeto % chave[1]]) - ord("a")

                mensagem_cifrada += mapping_matrix[linha][coluna]
                indice_alfabeto += 1
            else:
                mensagem_cifrada += mensagem_original[0][indice]
            indice += 1

        mensagem_cifrada = (mensagem_cifrada, len(mensagem_cifrada))
        return mensagem_cifrada

    def decrypt(self, mensagem_cifrada, chave, alfabeto):
        mensagem_decifrada = ""

        indice = 0
        indice_alfabeto = 0
        while indice < mensagem_cifrada[1]:
            if mensagem_cifrada[0][indice] in alfabeto:
                if ord(mensagem_cifrada[0][indice]) >= ord(chave[0][indice_alfabeto % chave[1]]):
                    coluna = ord(mensagem_cifrada[0][indice]) - ord(chave[0][indice_alfabeto % chave[1]])
                else:
                    antes_da_rotacao = ord("z") - ord(chave[0][indice_alfabeto % chave[1]]) + 1
                    depois_da_rotacao = ord(mensagem_cifrada[0][indice]) - ord("a")

                    coluna = antes_da_rotacao + depois_da_rotacao

                mensagem_decifrada += chr(coluna + ord("a"))
                indice_alfabeto += 1
            else:
                mensagem_decifrada += mensagem_cifrada[0][indice]
            indice += 1

        mensagem_decifrada = (mensagem_decifrada, len(mensagem_decifrada))
        return mensagem_decifrada
        