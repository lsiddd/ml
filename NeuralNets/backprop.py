import matplotlib as mpl
#mpl.use("agg")
import matplotlib.pyplot as plt
import numpy as np
np.random.seed(0)

# Backpropagation in two layers
e = []

#função sigmoide
sigmoid = lambda z:np.tanh(z)
Dsigmoid = lambda z: (1/ np.cosh(z)) ** 2

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
	w1 = np.random.rand(5,3) 

	# 2 perceptrons na camada de saída
	w2 = np.random.rand(2,6)
	
	#listas de entradas e saídas
	x = [[0, 0], [0, 1], [1, 0], [1, 1]]
	d = [[0, 0], [1, 0], [1, 0], [0, 1]]
	

	h1 = layer (x, w1)
	y  = layer (h1, w2)

	mi = 0.1
	nEpocas = 5000
	e = [0]
	w1t = []
	w2t = []

	for Epc in range(nEpocas):
		h1 = layer (x, w1)
		y  = layer (h1, w2)

		for n in range(len(d)):
			delta1 = []
			delta2 = []


			for i in range(len(w2)):
				delta2.append(Dsigmoid(y[n][i]) * (y[n][i] - d[n][i]))
			for i in range(len(w1)):
				soma = 0
				for j in range(len(w2)):
					soma = soma + delta2[j] * w2[j][i]
				delta1.append(Dsigmoid(h1[n][i]) * soma)

			for i in range(len(w2)):
				for j in range(len(w2[i]) - 1):
					w2[i][j] = w2[i][j] - mi * delta2[i] * h1[n][j]
				w2[i][j+1] = w2[i][j+1] - mi * delta2[i]
			for i in range(len(w1)):
				for j in range(len(w1[i]) - 1):
					w1[i][j] = w1[i][j] - mi * delta1[i] * x[n][j]
				w1[i][j+1] = w1[i][j+1] - mi * delta1[i]

		e.append(erro(y, d))
	
	mpl.style.use("ggplot")
	plt.figure()
	plt.plot(e, linewidth=2, color='orange')
	plt.xlim(1, nEpocas)
	plt.ylim(0, max(e))
	plt.xlabel("Epoch")
	plt.ylabel("MSE")
	plt.grid(True, color="#9467bd")
	plt.show()

if __name__ == "__main__":
	main()