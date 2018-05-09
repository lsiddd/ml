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
	#8 perceptrons na primeira camada oculta
	w1 =[[0.5, 0.5, 0.5],
		 [0.5, 0.5, 0.5]]
		
	#4 perceptrons na segunda camada oculta
	w2 =[[0.5, 0.5, 0.5],
		 [0.5, 0.5, 0.5],
		 [0.5, 0.5, 0.5],
		 [0.5, 0.5, 0.5],]

	# 2 perceptrons na camada de saída
	w3 = [[0.5, 0.5, 0.5, 0.5, 0.5],
		  [0.5, 0.5, 0.5, 0.5, 0.5]]

	#listas de entradas e saídas
	x = [[0, 0], [0, 1], [1, 0], [1, 1]]
	d = [[0, 0], [1, 0], [1, 0], [0, 1]]

	h1 = layer (x, w1)
	h2 = layer (h1, w2)
	y  = layer (h2, w3)

	mi = 0.1
	nEpocas = 400
	e = [0]
	w1t = []
	w2t = []

	for i in range(nEpocas):
		lastE = erro(y, d)
		h1 = layer (x, w1)
		h2 = layer (h1, w2)
		y  = layer (h2, w3)

		for n in range(len(d)):
			delta1 = []
			delta2 = []
			delta3 = []


			for i in range(len(w3)):
				delta3.append(y[n][i] * (1 - y[n][i]) * (y[n][i] - d[n][i]))
			for i in range(len(w2)):
				soma = 0
				for j in range(len(w3)):
					soma = soma + delta3[j] * w3[j][i]
				delta2.append(h2[n][i] * (1 - h2[n][i]) * soma)
			for i in range(len(w1)):
				soma = 0
				for j in range(len(w2)):
					soma = soma + delta2[j] * w2[j][i]
				delta1.append(h1[n][i] * (1 - h1[n][i]) * soma)


			for i in range(len(w3)):
				for j in range(len(w3[i]) - 1):
					w3[i][j] = w3[i][j] - mi * delta3[i] * h2[n][j]
				w3[i][j+1] = w3[i][j+1] - mi * delta3[i]
			for i in range(len(w2)):
				for j in range(len(w2[i]) - 1):
					w2[i][j] = w2[i][j] - mi * delta2[i] * h1[n][j]
				w2[i][j+1] = w2[i][j+1] - mi * delta2[i]
			for i in range(len(w1)):
				for j in range(len(w1[i]) - 1):
					w1[i][j] = w1[i][j] - mi * delta1[i] * x[n][j]
				w1[i][j+1] = w1[i][j+1] - mi * delta1[i]
				
			h1 = layer (x, w1)
			h2 = layer (h1, w2)
			y  = layer (h2, w3)
		
		print(erro(y, d))
		e.append(erro(y, d))
		

	plt.figure()
	plt.plot(e)
	plt.grid()
	plt.xlim(1, nEpocas)
	plt.ylim(0, max(e))
	plt.xlabel("Epoch")
	plt.ylabel("MSE")
	plt.show()
	
if __name__ == "__main__":
	main()