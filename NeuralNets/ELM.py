import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

#função sigmoide
sigmoid = lambda z:(np.exp(z) - np.exp(-1 * z)) / (np.exp(z) + np.exp(-1 * z))

def main():
	#última coluna dos pesos será sempre o bias
	w1 = np.random.rand(2,3)

	#listas de entradas e saídas
	x = np.matrix('0 0;\
				   0 1;\
				   1 0;\
				   1 1')

	d = np.matrix('0 0;\
				   1 0;\
				   1 0;\
				   0 1')

	sh = list(x.shape)
	sh[1] = sh[1] + 1
	Xa = np.ones(sh)
	Xa[:,:-1] = x
	S = sigmoid(np.matmul(Xa, w1.transpose()))

	sh = list(S.shape)
	sh[1] = sh[1] + 1
	Ha = np.ones(sh)
	Ha[:,:-1] = S

	w2 = np.matmul(np.matmul(np.linalg.inv(np.matmul(Ha.transpose(), Ha)), Ha.transpose()), d).transpose()

	Y = np.matmul(Ha, w2.transpose())
	print (1/2 * sum([np.sum (i **2) for i in np.nditer(Y -d)]))	

if __name__ == "__main__":
	main()
