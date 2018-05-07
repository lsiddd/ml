import numpy as np

# Straightforward propagation in multiple layers

verbose = True

e = []

#função sigmoide
def sigmoid(z):
	return (np.exp(z) - np.exp(-1 * z)) / (np.exp(z) + np.exp(-1 * z))

#Função que recebe o vetor de entradas e uma matriz de pesos
# e retorna um vetor de saídas em cada neurônio
def layer(x, u):
	r1 = []
	for N in x: #para cada conjunto de entradas N
		h1 =[]
		N.append(1)#adicionar a entrada bias
		for i in u: # para cada neurônio na camada considerada
			if (len(i) != len(N)):
				raise Exception("Número de arcos de entrada no neurônio deve ser igual ao número de entradas.")
			s = 0
			for j in range(len(i)): #para cada peso do neurônio
				s = s + i[j] * N[j]
			h1.append(sigmoid(s))
		r1.append(h1)
	return r1

def main():
	#última coluna dos pesos será sempre o bias
	#pesos da primeira camada
	w1 =[[1,   2, 0],
		[0.5, 1, 0]]
		
	#pesos da segunda camada
	w2 =[[1, 2, 0.5],
		[2, 1, 0.5]]

	#listas de entradas e saídas
	x = [[0, 0], [0, 1], [1, 0], [1, 1]]
	d = [[0, 0], [1, 0], [1, 0], [0, 1]]

	y = layer(layer(x, w1),w2)
	
if __name__ == "__main__":
	main()