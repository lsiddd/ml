#Loading Container Problem
import numpy as np
import random

from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure


# produto escalar de duas listas numéricas
dotp = lambda v1, v2: sum([x*y for x,y in zip(v1, v2)])

#iniciar população aleatóriamente
def startPop(size):
	pop = []
	for i in range(size):
		#nosso alfabeto será inteiros entre 4 e 188
		pop.append(list(np.random.random_integers(4,188,5)))

	#adicionar coluna de fitness
	for i in pop:
		i.append(fitness(i))

	#ordenar por fitness
	pop.sort(key=lambda x: x[5], reverse=True)
	return pop

#cálculo dafitness dado um indivíduo
def fitness(vec):
	pesos = [2, 4, 5, 8, 12] #pesos de cada tipo
	valores = [3, 6, 10, 18, 25] #valor de cada tipo

	# O peso e o valor de cada indivíduo
	# será o produto escalar entre o
	# vetor de pesos e valores e a quantidade 
	# de cada tipo no indivíduo
	pesoInd = dotp(vec, pesos)
	valorInd = dotp(vec, valores)

	if (pesoInd <= 500):
		return valorInd
	# Punição para o caso de o peso exceder o max
	else:
		return valorInd - 24 * (pesoInd - 500)

# Seleção de pais por torneio
def torneio(pop, tx, nCandidatos):
	popPais = []
	# Sempre seleciona um n par de pais
	nFilhos = 2 * int(len(pop) * tx / 2)

	for i in range(nFilhos):
		# Amostrar candidatos aleatóriamente
		candidatos = random.sample(pop, nCandidatos)
		popPais.append(candidatos[0])
		bestFitness = candidatos[0][5]
		#selecionar apenas o de maior fitness
		for j in candidatos:
			if(j[5] > bestFitness):
				popPais = popPais[:-1]
				popPais.append(j)
				bestFitness = j[5]
	return popPais

# Cruzamento por máscara binária dada a população de pais
def cruzamento(popPais):
	popFilhos = []
	# Cruzar população de pais dois a dois
	for i,k in zip(popPais[0::2], popPais[1::2]):
		filho1 = []
		filho2 = []
		# Máscara binária aleatória
		mask = np.random.randint(2, size=5)
		# Cruzamento de acordo com a máscara
		for j in range(len(mask)):
			if(mask[j]):
				filho1.append(i[j])
				filho2.append(k[j])
			else:
				filho1.append(k[j])
				filho2.append(i[j])
		# Cálcular a fitness dos filhos
		filho1.append(fitness(filho1))
		filho2.append(fitness(filho2))
		popFilhos.append(filho1)
		popFilhos.append(filho2)
	return popFilhos

#Adicionar filhos na população
def inserirFilhos(pop, popFilhos):
	# Eliminar piores indivíduos da população
	pop = pop[:-len(popFilhos)]
	#inserir indivíduos filhos
	for i in popFilhos:
		pop.append(i)
	#organizar a população por fitness
	pop.sort(key=lambda x: x[5], reverse=True)
	return pop

# Mutar n indivíduos aleatóriamente
def mutacao(pop, tx):
	nMutados = int(len(pop) * tx)
	elitismo = True

	for i in range(nMutados):
		# Se houver elitismo, nunca se muta o melhor indivíduo
		#index do indivíduo a ser mutado
		if (elitismo):
			index1 = np.random.random_integers(1, len(pop) - 1, 1)[0]
		else:
			index1 = np.random.random_integers(0, len(pop) - 1, 1)[0]
		#index do gene a ser mutado
		index2 = np.random.random_integers(0, 4, 1)[0]
		pop[index1][index2] = np.random.random_integers(4,188,1)[0]
		# Recálculo da fitness
		pop[index1][5] = fitness(pop[index1])
	# Reornganização da população
	pop.sort(key=lambda x: x[5], reverse=True)
	return pop

def main():
	bestIndFit = []
	mediumFit = []

	pop = startPop(100)

	nGerações = 100

	for i in range(nGerações):

		popPais = torneio(pop, 0.1, 3)
		
		popFilhos = cruzamento(popPais)

		pop = inserirFilhos(pop, popFilhos)

		pop = mutacao(pop, 0.2)

		print(f'Geração {i} -- Melhor Indivíduo: {pop[0]} -- Peso: {dotp([2, 4, 5 , 8, 12], pop[0])}')
		
		bestIndFit.append(pop[0][5])
		mediumFit.append(np.mean(pop, axis=0)[5])

	fig = Figure()
	FigureCanvas(fig)
	ax = fig.add_subplot(111)
	ax.plot(bestIndFit, label="Fitness do Melhor Indivíduo")
	ax.plot(mediumFit, "-.", label="Fitness Média da População")
	ax.set_title('Fitness ao Longo das Gerações')
	ax.set_xlabel('Geração')
	ax.set_ylabel('Fitness')
	ax.set_yscale('symlog')
	ax.set_xlim(0,99)
	fig.savefig("fit.pdf")

if (__name__=="__main__"):
    main()
