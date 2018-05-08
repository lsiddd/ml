import matplotlib as mpl
#mpl.use("agg")
import matplotlib.pyplot as plt
import numpy as np

# Backpropagation in two layers

verbose = True

e = []

#função sigmoide
sigmoid = lambda z:(np.exp(z) - np.exp(-1 * z)) / (np.exp(z) + np.exp(-1 * z))
def erro(y, d):
	error = 0
	for o, t in zip(y,d):
		for a, b in zip(o, t):
			error = error + (a - b)**2
	return error / 2


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
		del N[-1]
		r1.append(h1)
	return r1

def main():
	#última coluna dos pesos será sempre o bias
	#pesos da primeira camada
	w1 =[[0.5, 0.5, 0.5],
		 [0.5, 0.5, 0.5],
		 [0.5, 0.5, 0.5],
		 [0.5, 0.5, 0.5],
		 [0.5, 0.5, 0.5],
		 [0.5, 0.5, 0.5]]
		
	#pesos da segunda camada
	w2 =[[0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5],
		 [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5]]

	#listas de entradas e saídas
	x = [[0, 0], [0, 1], [1, 0], [1, 1]]
	d = [[0, 0], [1, 0], [1, 0], [0, 1]]

	h = layer (x, w1)
	y = layer (h, w2)

	mi = 0.1
	nEpocas = 300
	e = []
	w1t = []
	w2t = []

	for i in range(nEpocas):
		h = layer (x, w1)
		y = layer (h, w2)
		for n in range(len(d)):
			delta1 = []
			delta2 = []


			for i in range(len(w2)):
				delta2.append(y[n][i] * (1 - y[n][i]) * (y[n][i] - d[n][i]))

			for i in range(len(w1)):
				soma = 0
				for j in range(len(w2)):
					soma = soma + delta2[j] * w1[i][j]
				delta1.append(h[n][i] * (1 - h[n][i]) * soma)


			for i in range(len(w2)):
				for j in range(len(w2[i]) - 1):
					w2[i][j] = w2[i][j] - mi * delta2[i] * h[n][j]
					h = layer (x, w1)
					y = layer (h, w2)
				w2[i][j+1] = w2[i][j+1] - mi * delta2[i]

			for i in range(len(w1)):
				for j in range(len(w1[i]) - 1):
					w1[i][j] = w1[i][j] - mi * delta1[i] * x[n][j]
					h = layer (x, w1)
					y = layer (h, w2)
				w1[i][j+1] = w1[i][j+1] - mi * delta1[i]
		print(erro(y, d))
		e.append(erro(y, d))
		w1t.append(w1)
		w2t.append(w2)

	plt.figure()
	plt.plot(e)
	plt.grid()
	plt.xlim(0, nEpocas-1)
	plt.ylim(0.5, 4.5)
	plt.title("why tho??")
	plt.xlabel("Epoch")
	plt.ylabel("MSE")
	plt.show()
	
if __name__ == "__main__":
	main()