import argparse
import time
from typing import List, Tuple, Hashable, Any, Dict

from encrypt_decrypt import VigenereCypher
from key_size import key_size_probabilities
from key_by_size import pbi_distributions

vigenere_obj = VigenereCypher()

def opcao_1(chave):
	global vigenere_obj

	chave = chave.lower(), len(chave)
	alfabeto = list("abcdefghijklmnopqrstuvwxyz")

	mapping_matrix = vigenere_obj.mapping(alfabeto)

	with open("Mensagens/Mensagem_Original.txt", "r", encoding="utf-8") as file:
		mensagem_original = file.read().lower()
		mensagem_original = mensagem_original, len(mensagem_original)

	mensagem_cifrada = vigenere_obj.encrypt(mensagem_original, chave, mapping_matrix, alfabeto)

	with open("Mensagens/Mensagem_Cifrada.txt", "w", encoding="utf-8") as file:
		file.write(mensagem_cifrada[0])


def opcao_2(chave):
	global vigenere_obj

	chave = chave.lower(), len(chave)
	alfabeto = list("abcdefghijklmnopqrstuvwxyz")

	with open("Mensagens/Mensagem_Cifrada.txt", "r", encoding="utf-8") as file:
		mensagem_cifrada = file.read().lower()
		mensagem_cifrada = mensagem_cifrada, len(mensagem_cifrada)

	mensagem_decifrada = vigenere_obj.decrypt(mensagem_cifrada, chave, alfabeto)

	with open("Mensagens/Mensagem_Decifrada.txt", "w", encoding="utf-8") as file:
		file.write(mensagem_decifrada[0])

def opcao_3(filtro_ocorrencias):
	with open("Mensagens/Mensagem_Cifrada.txt", "r", encoding="utf-8") as file:
		mensagem_cifrada = file.read().lower()
		mensagem_cifrada = mensagem_cifrada, len(mensagem_cifrada)

	key_size_probabilities(mensagem_cifrada[0], filtro_ocorrencias)

def opcao_4(key_size):
	with open("Mensagens/Mensagem_Cifrada.txt", "r", encoding="utf-8") as file:
		mensagem_cifrada = file.read().lower()
		mensagem_cifrada = mensagem_cifrada, len(mensagem_cifrada)

	pbi_distributions(mensagem_cifrada[0], key_size)

def opcao_5():
	pass

menu_principal = """______ Vigenere Devthumos Tool ______
\t1) Encriptar
\t2) Decriptar
\t3) Probabilidades de Tamanhos de Chave
\t4) Distribuicao dos Agrupamentos em Power BI
\t5) Sair\n"""

menu_1 = """______ Vigenere Devthumos Tool ______
______________ Menu 01 ______________"""

menu_2 = """______ Vigenere Devthumos Tool ______
______________ Menu 02 ______________"""

menu_3 = """______ Vigenere Devthumos Tool ______
______________ Menu 03 ______________"""

menu_4 = """______ Vigenere Devthumos Tool ______
______________ Menu 04 ______________"""

menu_5 = """______ Vigenere Devthumos Tool ______
_______________ By By _______________"""


if __name__ == "__main__":
	menu_principal_verificado = 0
	while not menu_principal_verificado:
		print(menu_principal)
		menu_num = input("\t\tEscolha uma Opcao: ")

		if menu_num.isdigit():
			menu_num = int(menu_num)
			menu_principal_verificado = 1

			print("\n\n")
		else:
			print("\t\tEscolha uma Opcao Valida!\n\n")
			time.sleep(5)

	if menu_num == 1:
		print(menu_1, "\n")
		print("Nao esqueca de inserir a mensagem a ser cifrada no arquivo \"Mensagens/Mensagem_Original.txt\"")
		chave = input("\tChave: ")

		opcao_1(chave)

		print("Mensagem Cifrada Com Sucesso!")
		print("Encontre a Mensagem Cifrada no Arquivo \"Mensagens/Mensagem_Cifrada.txt\"")

	elif menu_num == 2:
		print(menu_2, "\n")
		print("Nao Esqueca de Inserir a Mensagem Cifrada a Ser Decifrada no Arquivo \"Mensagens/Mensagem_Cifrada.txt\"")
		chave = input("\tChave: ")

		opcao_2(chave)

		print("Mensagem Decifrada Com Sucesso!")
		print("Encontre a Mensagem Decifrada no Arquivo \"Mensagens/Mensagem_Decifrada.txt\"")		
	elif menu_num == 3:
		print(menu_3, "\n")
		print("Nao Esqueca de Inserir a Mensagem Cifrada a Ser Analisada Pelo Algoritmo no Arquivo \"Mensagens/Mensagem_Cifrada.txt\"")
		filtro_ocorrencias = int(input("\tNumero Minimo de Ocorrencias de Trigramas: "))

		opcao_3(filtro_ocorrencias)

		print("Probabilidades Encontradas Com Sucesso!")
		print("Encontre as Probabilidades de Tamanhos de Chave no Arquivo \"KeySize/SizeScore.txt\"")

	elif menu_num == 4:
		print(menu_4, "\n")
		print("Nao Esqueca de Inserir a Mensagem Cifrada a Ser Analisada Pelo Algoritmo no Arquivo \"Mensagens/Mensagem_Cifrada.txt\"")
		tamanho = int(input("\tPossivel Tamanho de Chave: "))

		opcao_4(tamanho)

		print("Distribuicoes Encontradas Com Sucesso!")
		print("Analise as Distribuicoes Visualmente Atraves do PowerBI no Arquivo \"Dashboards/dashboard_de_distribuicao.pbix\"")
	else:
		print(menu_5)
		exit(1)

