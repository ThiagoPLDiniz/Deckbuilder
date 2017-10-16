import psycopg2
import pprint

try:
	conn = psycopg2.connect(dbname='deckbuilder', user='postgres', host='localhost', password='**********');
	conexao = conn.cursor()
	print "Conectado!\n"
except:
	print "Erro de Conexao...\n"
commit = ('COMMIT TRANSACTION;')

class Usuario() :
	def __init__(self, user, nome_usuario, senha):
		self.nome = nome_usuario
		self.nick = user
		self.senha = senha

	def procura_usuario(self):
		procura_usu = ("SELECT nome FROM usuarios WHERE nick = '" + self.nick + "' AND senha = '" + self.senha + "'")
		try:
			conexao.execute(procura_usu)
			busca = conexao.fetchall()
			procurando_usu = str(busca).strip('[]')
			procurando_usu2 = procurando_usu.strip("(',')")
			if procurando_usu2 == 'None':
				print "\n   ***   Usuario ainda nao foi criado!   ***\n"
				return(False)
			else:
				return(True)
		except:
			print "\n***\n"
	def autentica_senha(self):
		autentica_usu = ("SELECT nick FROM usuarios WHERE senha = '" + self.senha + "'")
		autentica_sen = ("SELECT senha FROM usuarios WHERE nick = '" + self.nick + "'")
		sen1 = "'" + self.senha + "'"
		usu1 = "'" + self.nick + "'"
 		try:
			conexao.execute(autentica_usu)
			autent_usu = conexao.fetchall()
			auten_usu = str(autent_usu).strip("[(',')]")
			if auten_usu != usu1:
				print "Erro no nome de usuario!\n"
				pprint.pprint(auten_usu)
				print usu1
				pass
			conexao.execute(autentica_sen)
			autent_sen = conexao.fetchall()
			auten_sen = str(autent_sen).strip("[(',')]")
			if auten_sen != sen1:
				print "Senha incorreta!\n"
				pprint.pprint(auten_sen)
				print sen1
				pass
		except:
			print "Erro ao executar Query!\n"

	def criar_usuario(self):
		criando = ('INSERT INTO usuarios ("nick", "nome", "senha") VALUES (')
		criando2 = ("'" + self.nick + "', '" + self.nome + "', '" + self.senha + "')")
		criando_tabela = ('CREATE TABLE ' + self.nick + ' ("nome_deck" varchar(35) not null, "formato_deck" varchar(15))')

		try:
			conexao.execute(criando + criando2)
			conexao.execute(criando_tabela)
			conexao.execute(commit)
		except:
			print "\n    ***   Usuario ja existe!   ***\n"

	def alterando_nome(self):
		alter = ("UPDATE usuarios SET nome = '" + self.nome + "' WHERE nick = '" + self.nick + "'")
		try:
			conexao.execute(alter)
			print "\n   ***   Nome de Usuario inserido com sucesso!   ***\n"
		except:
			print "\n   ***   Erro ao inserir nome de usuario!   ***\n"

	def exclui_usuario(self):
		deleta_usu = ("DELETE FROM usuarios where nick = '" + self.nick + "'")
		deleta_tabela = ("DROP TABLE " + self.nick)

	def mostra_decks(self):
		mostra = ("SELECT * FROM " + self.nick)

		conexao.execute(mostra)
		mostra1 = conexao.fetchall()
		pprint.pprint(mostra1)




class Deck():
	def __init__(self, nome_deck, formato_deck, dono):
		self.nome = nome_deck
		self.formato = formato_deck
		self.dono = dono

	def procura_deck(self):
		procurando = ('SELECT * FROM ' + self.dono + ' where nome_deck = ')
		procurando2 = ("'" + self.nome + "'")
		procurar = procurando + procurando2

		conexao.execute(procura)
		resultado = conexao.fetchall()
		pprint.pprint(resultado)
 
	def novo_deck(self):
		criando_deck = ('INSERT INTO ' + self.dono + '("nome_deck", "formato_deck") VALUES (')
		criando_deck2 = ("'" + self.nome + "', " + "'" + self.formato + "')")
		criando_table = ('CREATE TABLE ' + self.nome + '_' + self.dono + '("nome_carta" varchar(35) not null, "cor_da_carta" varchar(15) not null, "custo_de_mana" varchar(2) not null)')
		criacao = criando_deck + criando_deck2


		conexao.execute(criando_table)
		conexao.execute(criacao)
		conexao.execute(commit)

	def exclui_deck(self, nick):
		exclui = ("DROP TABLE " + self.nome + "_" + nick)
		exclui2 = ("DELETE FROM " + self.dono + " WHERE nome_deck = '" + self.nome + "' AND formato_deck = '" + self.formato)

		try:
			conexao.execute(exclui)
			conexao.execute(exclui2)
			conexao.execute(commit)
		except:
			print "Erro ao deletar deck!\n"



class Carta():
	def __init__(self, card_name, cor_carta, custo_carta, dono_deck, deck):
		self.nome = card_name
		self.cor = cor_carta
		self.manas = custo_carta
		self.dono = dono_deck
		self.deck = deck

	def insere_carta(self):
		insere = ('INSERT INTO ' + self.deck + '(')
		insere2 = ()
