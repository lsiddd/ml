import matplotlib as mpl
import matplotlib.pyplot as plt
import sklearn.preprocessing as sk
import numpy as np

#função sigmoide
sigmoid = lambda z:(np.exp(z) - np.exp(-1 * z)) / (np.exp(z) + np.exp(-1 * z))
erro = lambda y, d: 1/2 * sum([np.sum (i **2) for i in np.nditer(y - d)])

def output(x, d, w1, w2=[]):
	#scaling das entradas entre -1 e 1
	scaler = sk.MinMaxScaler(feature_range=(-1, 1))
	scaler = scaler.fit(x)
	X_scaled = scaler.transform(x)

	#scaling do conjunto de treinamento entre -0.7 e 0.7
	scaler = sk.MinMaxScaler(feature_range=(-0.7, 0.7))
	scaler = scaler.fit(d)
	D_scaled = scaler.transform(d)

	sh = list(X_scaled.shape)
	sh[1] = sh[1] + 1
	Xa = np.ones(sh)
	Xa[:,:-1] = X_scaled
	S = sigmoid(np.matmul(Xa, w1.transpose()))

	sh = list(S.shape)
	sh[1] = sh[1] + 1
	Ha = np.ones(sh)
	Ha[:,:-1] = S
	if(w2 == []):
		w2 = np.matmul(np.matmul(np.linalg.inv(np.matmul(Ha.transpose(), Ha)), Ha.transpose()), D_scaled).transpose()

	Y = np.matmul(Ha, w2.transpose())

	#reversão do scaling para cálculo do erro
	d = scaler.inverse_transform(D_scaled)
	Y = scaler.inverse_transform(Y)
	print (f'pesos da camada oculta: \n{w1}')
	print (f'pesos da camada de saída: \n{w2}')
	print (f'resposta da camada oculta:\n {S}')
	print (f'resposta da camada de saída:\n {Y}')
	print (f' O erro RMS da rede é {erro(Y, d)}\n\n')
	return w2

def main():
	#última coluna dos pesos será sempre o bias
	w1 = np.matrix('0.53  0.86 -0.43;\
					1.83  0.31  0.34;\
					-2.25 -1.3  3.57')

	#listas de entradas e saídas
	x_training = np.matrix(' 0.35 -1.4;\
				    3.1   1.2;\
				   -2.5   2.4;\
				    1.7   0.8;\
				   -0.4   0.6;\
				    1.3   2.6')

	d_training = np.matrix(' 6.2  1.4;\
				   -3.5  1.8;\
				    5.1  2.3;\
				    2.6  1.3;\
				    0.5 -2.1;\
				    0.2  4.1')

	w2 = output(x_training, d_training, w1)

	x_test = np.matrix(' 0.4 -1.8; \
						 3.4  1.6; \
						-2.2  2.1')

	d_test = np.matrix(' 5.2 1.6; \
						-3.0 1.5; \
						 4.1 1.3')
	
	output(x_test, d_test, w1, w2)

if __name__ == "__main__":
	main()
