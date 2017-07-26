import classes

print "\n\n\n 		*** 	Bem-vindo ao construtor de decks de Magic: The Gathering! 	***\n\n\n"

resposta = 0
resposta2 = 3
resposta3 = 0
s = 0
n = 1
cor = 0
cor2 = 0
pergunta = 0
nome = 'None'
usu_teste = False
opcao_exclui = 0
edita_deck = 0
tipo_edicao = 0

while(resposta3 != 1):
	nick = raw_input("Digite o nick de usuario (SEM ESPACOS):\n")
	senha = raw_input("Entre com uma senha. Lembre-se de NAO usar ESPACOS e letras MAIUSCULAS!\n")
	usuario = classes.Usuario(nick, nome, senha)
	usuario.criar_usuario()
	usu_teste = usuario.procura_usuario()
	if usu_teste == False:
		resposta3 = input("Deseja criar um novo usuario?(RESPONDA COM 's' ou 'n'):\n")
		if resposta3 == s:
			print "Entao, vamos criar um novo usuario:\n"
			usuario.nome = raw_input("Por favor, digite o seu nome de usuario:\n")
			print "Pronto, " + usuario.nome + ", seu usuario foi criado!\n"
			usuario.alterando_nome()
			break
		elif resposta3 == n:
			pass
		
		else:
			print "\n   *** Resposta Invalida!   ***\n"
			pass
		pass
	else:
		resposta3 = 1
		break

while (resposta != 6 or resposta2 != 0):
	while (resposta != 2 or resposta != 6) :
		print "O que deseja fazer dentro do usuario '" + nick + "' ?\n"
		resposta = input("1) Criar novo deck\n2) Editar deck\n3) Excluir deck\n4) Mostrar todos os decks do usuario\n5) Excluir usuario\n6) Sair do programa\n")
		if resposta == 1:
			deck_name = raw_input("Digite o nome do deck que deseja criar:\n")
			nome_deck = deck_name.replace(' ', '').lower()
			formato = 0
			while(formato > 6 or formato < 1):
				formato = input("Qual o formato do deck?\n1) STANDART(T2);\n2) MODERN;\n3) COMMANDER;\n4) PAUPER;\n5) LEGACY;\n6) VINTAGE.\n")
				if formato == 1:
					formato_deck = 'STANDART(T2)'
					break
				elif formato == 2:
					formato_deck = 'MODERN'
					break
				elif formato == 3:
					formato_deck = 'COMMANDER'
					break
				elif formato == 4:
					formato_deck = 'PAUPER'
					break
				elif formato == 5:
					formato_deck = 'LEGACY'
					break
				elif formato == 6:
					formato_deck = 'VINTAGE'
					break
				else:
					"Resposta invalida!\n"	
			
			deck = classes.Deck(nome_deck, formato_deck, nick)
			deck.novo_deck()
			opcao_exclui = 0
			pass

		elif resposta == 2:
			#edita_deck/////////////////
			nome_edita = raw_input("Qual o nome do deck que deseja editar:\n")
				
			while(edita_deck > 6 or edita_deck < 1):
				edita_deck = input("Qual o formato do deck que deseja editar:\n1) STANDART(T2);\n2) MODERN;\n3) COMMANDER;\n4) PAUPER;\n5) LEGACY;\n6) VINTAGE.\n")
				if edita_deck == 1:
					formato_edita = 'STANDART(T2)'
					break
				elif edita_deck == 2:
					formato_edita = 'MODERN'
					break
				elif edita_deck == 3:
					formato_edita = 'COMMANDER'
					break
				elif edita_deck == 4:
					formato_edita = 'PAUPER'
					break
				elif edita_deck == 5:
					formato_edita = 'LEGACY'
					break
				elif edita_deck == 6:
					formato_edita = 'VINTAGE'
					break
				else:
					print "Resposta invalida!\n"

			deck = classes.Deck(nome_edita, formato_edita, nick)
			break

		elif resposta == 3:
			nome_exclui = raw_input("Qual o nome do deck que deseja excluir:\n")
			while(opcao_exclui > 6 or opcao_exclui < 1):
				opcao_exclui = input("Qual o formato do deck que deseja excluir:\n1) STANDART(T2);\n2) MODERN;\n3) COMMANDER;\n4) PAUPER;\n5) LEGACY;\n6) VINTAGE.\n")
				if opcao_exclui == 1:
					formato_exclui = 'STANDART(T2)'
					break
				elif opcao_exclui == 2:
					formato_exclui = 'MODERN'
					break
				elif opcao_exclui == 3:
					formato_exclui = 'COMMANDER'
					break
				elif opcao_exclui == 4:
					formato_exclui = 'PAUPER'
					break
				elif opcao_exclui == 5:
					formato_exclui = 'LEGACY'
					break
				elif opcao_exclui == 6:
					formato_exclui = 'VINTAGE'
					break
				else:
					print "Resposta invalida!\n"
					pass
			deck = classes.Deck(nome_exclui, formato_exclui, nick)
			deck.exclui_deck(nick)
			pass

		elif resposta == 4:
			usuario.mostra_decks()
			pass
		elif resposta == 5:
			#exclui_usuario
			pass
		elif resposta == 6:
			#encerra_programa
			break
		else :
			print "Resposta invalida!!!\n"

	if(resposta == 2):
		while(resposta != 4 or resposta != 5):
			print "O que deseja fazer com o deck " + deck.nome_edita + "?\n1) Adicionar carta\n2) Remover carta\n3) Mostrar deck completo\n4) Sair do Deck\n5) Sair do programa\n"
			resposta = input()
			if resposta == 1:
				card_name = raw_input("Digite o nome da carta:\n")
				while(cor < 1 or cor > 5):
					cor = input("Qual a cor da carta?\n1) Preto\n2) Azul\n3) Branco\n4) Vermelho\n5) Verde\n")
					if cor == 1:
						cor_carta = 'PRETO'
						break
					elif cor == 2:
						cor_carta = 'AZUL'
						break
					elif cor == 3:
						cor_carta = 'BRANCO'
						break
					elif cor == 4:
						cor_carta = 'VERMELHO'
						break
					elif cor == 5:
						cor_carta = 'VERDE'
						break
					else:
						print "Resposta invalida!\n"

				while(pergunta == 's'):
					pergunta = input("A carta tem apenas esta cor?\ns) Sim\nn) Nao\n")
					if pergunta == 1:
						while(cor2 < 1 or cor2 > 5):
							cor2 = input("Qual outra cor tem a carta?\n1) Preto\n2) Azul\n3) Branco\n4) Vermelho\n5) Verde\n")
							if cor2 == 1:
								cor_carta = cor_carta + ', PRETO'
								break
							elif cor2 == 2:
								cor_carta = cor_carta + ', AZUL'
								break
							elif cor2 == 3:
								cor_carta = cor_carta + ', BRANCO'
								break
							elif cor2 == 4:
								cor_carta = cor_carta + ', VERMELHO'
								break
							elif cor2 == 5:
								cor_carta = cor_carta + ', VERDE'
							else:
								print "Resposta invalida!\n"
					pass

				custo_mana = input("Qual o custa de mana convertido da carta?\n")
				deck_contido = nome_deck
				dono_deck = nick
				carta = classes.Carta(card_name, cor_carta, custo_mana, dono_deck, deck_contido)
				print (carta.carda_name, carta.cor_carta, carta.custo_mana)
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

	if(resposta == 5 or resposta == 6):
		resposta2 = input("Voce gostaria realmente de sair do programa? (Responda com ('s' ou 'n'))\n")
		if(resposta2 == 0):
			print "\n\n 		*** 	Obrigado por utilizar o Contrutor de decks de Magic: The Gathering ! 	***\n"
		else:
			pass

	
		
	