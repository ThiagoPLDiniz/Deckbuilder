#!/usr/bin/env python
# -*- coding: utf-8 -*-
import classes


print "\n\n\n\n 		*** 	Bem-vindo ao construtor de decks de Magic: The Gathering! 	***\n\n\n\n"

resposta = 0
resposta2 = 3
s = 0
n = 1
nome = raw_input("Por favor, digite o seu nome de usuário:\n")
nick = nome.replace(' ', '').lower()
usuario = classes.Usuario(nome, nick)
usuario.procura_usuario()
usuario.criar_usuario()


while (resposta != 5 or resposta2 != 0):
	while (resposta != 2 or resposta != 5) :
		print "O que deseja fazer dentro do usuario '" + usuario.nome + "' ?\n"
		resposta = input("1) Criar novo deck\n2) Editar deck\n3) Excluir deck\n4) Mostrar todos os decks do usuario\n5) Sair do programa\n")
		if resposta == 1:
			deck_name = raw_input("Digite o nome do deck que deseja criar:\n")
			nome_deck = deck_name.lower()
			formato = raw_input("Qual o formato do deck?\n")
			formato_deck = formato.upper()
			dono = nick
			deck = classes.Deck(nome_deck, formato_deck, dono)
			deck.novo_deck()
			pass

		elif resposta == 2:
			#editar_deck
			break

		elif resposta == 3:
			#excluir_deck
			pass

		elif resposta == 4:
			#mostra_decks
			pass
		elif resposta == 5:
			#encerra_programa
			break
		else :
			print "Resposta invalida!!!\n"

	if(resposta == 2):
		while(resposta != 4 or resposta != 5):
			print "O que deseja fazer com o deck?\n1) Adicionar carta\n2) Remover carta\n3) Mostrar deck completo\n4) Sair do Deck\n5) Sair do programa\n"
			resposta = input()
			if resposta == 1:
				card_name = raw_input("Digite o nome da carta:\n")
				cor_carta = raw_input("Qual a cor da carta:\n")
				custo_mana = input("Qual o custa de mana convertido da carta?\n")
				deck_contido = nome_deck
				dono_deck = nick
				carta = classes.Carta(card_name, cor_carta, custo_mana, dono_deck, deck_contido)
				print(carta.card_name, carta.cor_carta, carta.custo_mana, carta.dono_deck, carta.deck_contido)
				pass

			elif resposta == 2:
				#remove_carta
				pass

			elif resposta == 3:
				#mostra_deck
				pass

			elif resposta == 4:
				print "\n\n 		*** 	Saindo do Deck ... 		***\n\n"
				break
		 
			elif resposta == 5:
				#encerra_programa
				break

			else :
				print "Resposta invalida!!!\n"

	if(resposta == 5):
		resposta2 = input("Voce gostaria realmente de sair do programa? (Responda com ('s' ou 'n'))\n")
		if(resposta2 == 0):
			print "\n\n 		*** 	Obrigado por utilizar o Contrutor de decks de Magic: The Gathering ! 	***\n"
		else:
			pass

	
		
	