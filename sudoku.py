class Celula:

	'''
	Classe de cada celula do sudoku.

	Passar parametro linha como objeto de Linha
	Parametro coluna como objeto de Coluna
	E se já tiver valor atribuir com num
	'''

	def __init__(self,linha, coluna, quadrante, num=0):
		self.possibilidades = [x for x in range(1,10) if not num]
		self.linha = linha
		self.linha.adicionaCelula(self)
		self.coluna = coluna
		self.coluna.adicionaCelula(self)
		self.quadrante = quadrante
		self.quadrante.adicionaCelula(self)
		self.num = num

	def __str__(self):

		'''
		representação pos linha/coluna
		'''

		return 'linha='+str(self.linha)+' '+'coluna='+str(self.coluna)+' q='+str(self.quadrante)+' v='+str(self.num)

	def set_num(self, num):
		'''
		Escolhe qual o numero final da celula e zera as possibilidades
		'''
		self.num=int(num)
		self.possibilidades=[]

	def get_num(self):
		'''
		Retorna o número atribuido para a celula.
		Se não tem numero retorna 0
		'''
		return self.num

	def deleta_possibilidade(self, n):
		'''
		Deleta a possibilidade de um valor n da Celula.possibilidades.
		Se só tem uma possibilidade atribui a possibilidade ao valor da celula (Celula.num)
		'''
		del self.possibilidades[self.possibilidades.index(n)]
		if len(self.possibilidades)==1:
			self.set_num(self.possibilidades[0])

	def get_valores_existentes_em_conjuntos(self):
		'''
		Retorna todos os valores das celulas que estao nos mesmos conjuntos (Linha, Coluna e Quadrante)
		   da celula em um Set
		'''
		linha_valores = self.linha.get_numeros_existentes()
		coluna_valores = self.coluna.get_numeros_existentes()
		quadrante_valores = self.quadrante.get_numeros_existentes()
		return set(linha_valores+coluna_valores+quadrante_valores)

	def preencher_por_valores_existentes(self):
		'''
		Passa por cada elemento da lista do get_valores_existentes_em_conjuntos retirando de suas possibilidades 
		'''
		if self.num==0:
			for v in self.get_valores_existentes_em_conjuntos():
				if v in self.possibilidades:
					self.deleta_possibilidade(v)
				if not self.possibilidades: return self


#---------- CONJUNTOS DE CElULAS ---------------------------------------------------------------------

class Conjunto:
	'''
	Super Classe dos conjuntos com atributos e metodos que serão iguais para todos
	'''

	def __init__(self, valor):
		self.celulas=[]
		self.valor=valor

	def __str__(self):
		return str(self.valor)

	def adicionaCelula(self, celula):
		'''
		Adiciona celula à lista do conjunto
		'''
		self.celulas.append(celula)

	def get_numeros_existentes(self):
		'''
		retorna uma lista com todos os numeros existentes do conjunto
		'''
		return [celula.get_num() for celula in self.celulas if celula.get_num()!=0]


class Linha(Conjunto):

	def __init__(self,numero_da_linha):
		super().__init__(numero_da_linha)
		self.numero_da_linha=numero_da_linha #retorna o eixo y

	def get_numero_da_linha(self):
		'''
		retorna o numero da linha
		'''
		return self.numero_da_linha

	def representacao_linha(self):
		'''
		retorna uma representação para a exibição dentro de um terminal
		'''
		primeiro = ' '.join([str(celula.get_num()) for celula in self.celulas[:3]])
		segundo = ' '.join([str(celula.get_num()) for celula in self.celulas[3:6]])
		terceiro = ' '.join([str(celula.get_num()) for celula in self.celulas[6:]])
		return '|'.join([primeiro, segundo, terceiro])


class Coluna(Conjunto):

	def __init__(self,numero_da_coluna):
		super().__init__(numero_da_coluna)
		self.numero_da_coluna=numero_da_coluna #retorna o eixo x

	def get_numero_da_coluna(self):
		'''
		Retorna o numero da coluna
		'''
		return self.numero_da_coluna


class Quadrante(Conjunto):
	def __init__(self,numero_do_quadrante):
		super().__init__(numero_do_quadrante)
		self.numero_do_quadrante=numero_do_quadrante #retorna o quadrante

	def get_numero_do_quadrante(self):
		'''
		Retorna o número do quadrante
		'''
		return self.numero_do_quadrante

#---------------------------- TABELA -------------------------------------------------


class Tabela:
	def __init__(self):
		self.linhas = [Linha(x) for x in range(1,10)]
		self.colunas = [Coluna(x) for x in range(1,10)]
		self.quadrantes = [Quadrante(x) for x in range(1,10)]
		self.celulas = []
		for i_l, linha in enumerate(self.linhas):
			for i_c, coluna in enumerate(self.colunas):
				quadrante = (i_c//3)+((i_l//3)*3)
				self.celulas.append(Celula(linha, coluna,self.quadrantes[quadrante]))

	def encontrar_posicao(self, linha,coluna):
		'''
		Encontra a celula a partir da posição linha e coluna
		'''
		for celula in self.celulas:
			if celula.linha.valor==linha and celula.coluna.valor==coluna:
				return celula
		
	def atribuir_valor(self,linha,coluna,v):
		'''
		Atribui à uma celula[x][y] o valor v
		'''
		self.encontrar_posicao(linha+1,coluna+1).set_num(v)

	def passar_por_todas_celulas_preenchendo(self):
		'''
		Passa por todas as celulas da tabela preenchendo a partir da Cedula.num
		'''
		mudanca=[]
		for celula in self.celulas:
			mudanca_var = celula.preencher_por_valores_existentes()
			if mudanca_var: mudanca.append(mudanca_var)
		return mudanca

	def representacao_tabela(self):
		'''
		retorna uma representação para a exibição dentro de um terminal
		'''
		print('_'*18)
		for i, l in enumerate(self.linhas):
			if i==3 or i==6:
				print('-'*18)
			print(l.representacao_linha())

	def repeticao(self):
		'''
		Repete a função de passar_por_todas_celulas_preenchendo e retorna quantas vezes foi repetido
		'''
		contador=1
		while True:
			print('\n\n---Vez nº %s---\n'%(contador))
			self.representacao_tabela()
			repete = self.passar_por_todas_celulas_preenchendo()
			if not repete:
				print('\nTerminou em %s vezes'%contador)
				return contador
			contador+=1






