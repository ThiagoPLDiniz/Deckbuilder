import psycopg2
import pprint

try:
	conn = psycopg2.connect(dbname='deckbuilder', user='postgres', host='localhost', password='frumello1');
	conexao = conn.cursor()
except:
	print "Erro de Conexao...\n"
commit = ('COMMIT TRANSACTION;')

class Usuario() :
	def __init__(self, nome_usuario, user):
		self.nome = nome_usuario
		self.nick = user

	def procura_usuario(self):
		busca = ("SELECT * FROM usuarios where nick = '" + self.nick + "'")
		
		try:
			conexao.execute(busca)
			resultado_busca = conexao.fetchall()

		except:
			print "\n    ***  Usuario nao encontrado!   ***\n"
			criar = input("Deseja criar um novo usuario?\n")

	def criar_usuario(self):
		criando = ('INSERT INTO usuarios ("nick", "nome") VALUES (')
		criando2 = ("'" + self.nick + "', " + "'" + self.nome + "')")
		criando_tabela = ('CREATE TABLE ' + self.nick + ' ("nome_deck" varchar(35) not null, "formato_deck" varchar(15))')

		try:
			conexao.execute(criando + criando2)
			conexao.execute(criando_tabela)
			conexao.execute(commit)
			print "\n   ***   Usuario criado com sucesso!   ***\n"
		except:
			print "\n    ***   Usuario ja existe!   ***\n"





class Deck():
	def __init__(self, nome_deck, formato_deck, dono):
		self.nome = nome_deck
		self.formato = formato_deck
		self.dono = dono

	def procura_deck(self):
		procurando = ('SELECT * FROM ' + self.dono + ' where nome_deck = ')
		procurando2 = ("'" + self.nome + "'")
		procura = procurando + procurando2

		conexao.execute(procura)
		resultado = conexao.fetchall()
		pprint.pprint(resultado)
 
	def novo_deck(self):
		criando_deck = ('INSERT INTO ' + self.dono + '("nome_deck", "formato_deck") VALUES (')
		criando_deck2 = ("'" + self.nome + "', " + "'" + self.formato + "')")
		criacao = criando_deck + criando_deck2

		conexao.execute(criacao)
		conexao.execute(commit)



class Carta():
	def __init__(self, card_name, cor_carta, custo_carta, dono_deck, deck):
		self.nome = card_name
		self.cor = cor_carta
		self.manas = custo_carta
		self.dono = dono_deck
		self.deck = deck

