import matplotlib as mpl
mpl.use("agg")
import matplotlib.pyplot as plt
import numpy as np
font = {'size'   : 14}
mpl.rc('font', **font)

def sigmoid(z):
	return (np.exp(z) - np.exp(-1 * z)) / (np.exp(z) + np.exp(-1 * z))

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
				s = s + i[j] * n[j]
			h1 .append(sigmoid(s))
		r1.append(h1)
	return r1

def main():
	#pesos da primeira camada
	u =[[1,   2, 0],
		[0.5, 1, 0]]
	#pesos da segunda camada
	v =[[1, 2, 0.5],
		[2, 1, 0.5]]
	#listas de entradas e saídas
	x = [[0, 0], [0, 1], [1, 0], [1, 1]]
	d = [[0, 0], [1, 0], [1, 0], [0, 1]]

	r1 = []
	print(layer(layer(x, u), v))

if __name__ == "__main__":
	main()