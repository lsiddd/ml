import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

#função sigmoide
sigmoid = lambda z:(np.exp(z) - np.exp(-1 * z)) / (np.exp(z) + np.exp(-1 * z))

error = lambda Y, d: 1/2 * sum([np.sum (i **2) for i in np.nditer(Y -d)])

def layer(x, w):
	sh = list(x.shape)
	sh[1] = sh[1] + 1
	Xa = np.ones(sh)
	Xa[:,:-1] = x
	return sigmoid(np.matmul(Xa, w.transpose()))

def main():
	#última coluna dos pesos será sempre o bias
	w1 = np.random.rand(2,3)
	w2 = np.random.rand(2,3)
	#listas de entradas e saídas
	x = np.matrix('0 0; 0 1; 1 0; 1 1')
	d = np.matrix('0 0; 1 0; 1 0; 0 1')

	mi = 0.1

	H = layer(x, w1)
	Y = layer(H, w2)

	dY = Y * (np.ones(Y.shape) - Y)
	delta2 = np.multiply((Y - d), dY)
	dH = np.multiply(H, (np.ones(H.shape) - H))
	print(w2)
	print (np.matmul(w2.transpose(), delta2[0]))
	
if __name__ == "__main__":
	main()
