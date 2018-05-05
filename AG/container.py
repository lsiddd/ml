#Loading Container Problem

import numpy as np
import random

def startPop(size):
	pop = []
	for i in range(size):
		pop.append(list(np.random.random_integers(4,188,5)))
	return pop

def fitness(vec):
	pesos = [2, 4, 5, 8, 12]
	valores = [3, 6, 10, 18, 25]

	pesoInd = sum([x*y for x,y in zip(vec, pesos)])
	valorInd = sum([x*y for x,y in zip(vec, valores)])

	if (pesoInd <= 500):
		return valorInd
	else:
		return valorInd - 24 * (pesoInd - 500)

def torneio(pop, tx, nCandidatos):
	popPais = []
	nFilhos = 2 * int(len(pop) * tx / 2)

	for i in range(nFilhos):
		candidatos = random.sample(pop, nCandidatos)
		popPais.append(candidatos[0])
		bestFitness = candidatos[0][5]
		for j in candidatos:
			if(j[5] > bestFitness):
				popPais = popPais[:-1]
				popPais.append(j)
				bestFitness = j[5]
	return popPais

def cruzamento(popPais):
	popFilhos = []
	for i,k in zip(popPais[0::2], popPais[1::2]):
		filho1 = []
		filho2 = []
		mask = np.random.randint(2, size=5)
		for j in range(len(mask)):
			if(mask[j]):
				filho1.append(i[j])
				filho2.append(k[j])
			else:
				filho1.append(k[j])
				filho2.append(i[j])
		filho1.append(fitness(filho1))
		filho2.append(fitness(filho2))
		popFilhos.append(filho1)
		popFilhos.append(filho2)
	return popFilhos

def inserirFilhos(pop, popFilhos):
	pop = pop[:-len(popFilhos)]
	for i in popFilhos:
		pop.append(i)
	pop.sort(key=lambda x: x[5], reverse=True)
	return pop

def mutacao(pop, tx):
	nMutados = int(len(pop) * tx)
	
	for i in range(nMutados):
		index1 = np.random.random_integers(1, len(pop) - 1, 1)[0]
		index2 = np.random.random_integers(0, 4, 1)[0]
		pop[index1][index2] = np.random.random_integers(4,188,1)[0]
		pop[index1][5] = fitness(pop[index1])
	pop.sort(key=lambda x: x[5], reverse=True)
	return pop

def main():
	pop = startPop(100)
	for i in pop:
		i.append(fitness(i))

	nGerações = 100

	for i in range(nGerações):
		pop.sort(key=lambda x: x[5], reverse=True)

		popPais = torneio(pop, 0.1, 3)
		
		popFilhos = cruzamento(popPais)

		pop = inserirFilhos(pop, popFilhos)

		pop = mutacao(pop, 0.1)
	print(pop[0])


if (__name__=="__main__"):
    main()
