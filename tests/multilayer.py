import matplotlib as mpl
mpl.use("agg")
import matplotlib.pyplot as plt
import numpy as np
font = {'size'   : 14}
mpl.rc('font', **font)

verbose = True

#função sigmoide
def sigmoid(z):
	return (np.exp(z) - np.exp(-1 * z)) / (np.exp(z) + np.exp(-1 * z))

#Função que recebe o vetor de entradas e uma matriz de pesos
# e retorna um vetor de saídas em cada neurônio
def layer(x, u):
	r1 = []
	for n in x:
		h1 =[]
		n.append(1)
		for i in u:
			if (len(i) != len(n)):
				raise Exception("Número de arcos de entrada no neurônio deve ser igual ao número de entradas.")

			s = 0
			for j in range(len(i)):
				# if (verbose):
				# 	if (j < (len(i) - 1)):
				# 		print (f'X{j}: {n[j]}')
				# 	else:
				# 		pass
				s = s + i[j] * n[j]
			h1 .append(sigmoid(s))
		r1.append(h1)
	return r1

def main():
	#pesos da primeira camada
	w1 =[[1,   2, 0],
		[0.5, 1, 0]]
	#pesos da terceira camada
	w2 =[[1, 2, 0.5],
		[2, 1, 0.5]]
	#listas de entradas e saídas
	x = [[0, 0], [0, 1], [1, 0], [1, 1]]
	d = [[0, 0], [1, 0], [1, 0], [0, 1]]
	print (layer(layer(x, w1),w2))

if __name__ == "__main__":
	main()