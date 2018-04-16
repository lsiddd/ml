import matplotlib as mpl
mpl.use("agg")
import matplotlib.pyplot as plt
import numpy as np
font = {'size'   : 14}
mpl.rc('font', **font)

def sigmoid(z):
	return (np.exp(z) - np.exp(-1 * z)) / (np.exp(z) + np.exp(-1 * z))

def main():
	#pesos da primeira camada
	u =[[0, 0.5, 1],
		[0, 0.5, 1]]
	#pesos da segunda camada
	v =[[0.5, 1, 2],
		[0.5, 2, 1]]
	#listas de entradas e saídas
	x = [[0, 0], [0, 1], [1, 0], [1, 1]]
	d = [[0, 0], [1, 0], [1, 0], [0, 1]]



	h1 = []
	y = []

		


if __name__ == "__main__":
	main()