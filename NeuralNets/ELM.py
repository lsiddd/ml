#!/usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

verbose = False
erro = lambda y, d: 1/2 * sum([np.sum (i **2) for i in np.nditer(y - d)])

def output(x, d, w1, w2=[]):
	sh = list(x.shape)
	sh[1] = sh[1] + 1
	Xa = np.ones(sh)
	Xa[:,:-1] = x
	#ativação sigmoidal
	S = np.tanh(np.matmul(Xa, w1.transpose()))

	sh = list(S.shape)
	sh[1] = sh[1] + 1
	Ha = np.ones(sh)
	Ha[:,:-1] = S

	#se os pesos de saída não forem fornecidos
	#calculamos eles aqui
	if(w2 == []):
		w2 = np.matmul(np.linalg.pinv(Ha), d).transpose()

	#caso contrário, se faz propagação direta
	Y = np.matmul(Ha, w2.transpose())

	if (verbose):
		print (f'pesos da camada oculta: \n{w1}')
		print (f'pesos da camada de saída: \n{w2}')
		print (f'resposta da camada oculta:\n {S}')
		print (f'resposta da camada de saída:\n {Y}')
		print (f' O erro RMS da rede é {erro(Y, d)}\n\n')

		plt.style.use("ggplot")
		plt.figure()
		plt.title(f"Sen(x), erro RMS = {erro(Y, d)}")
		plt.plot(x, Y, "+", color="green", label="resposta da Rede")
		plt.plot(x, d, "-.", color="red", label="Função Original")
		plt.ylabel("Saída")
		plt.xlabel("Entrada")
		plt.legend()
		plt.show()
	return w2, Y

def main():
	x = []
	d = []

	linspace = np.arange(0, 10, 0.01)

	for i in linspace:
		x.append([i])
		d.append([np.sin(i)])
	
	#O conjunto de testes 
	testx = np.array(x[1::20])
	testd = np.array(d[1::20])

	#conjunto de treinamento
	x = np.array(x[::30])
	d = np.array(d[::30])

	#número de neurônioa na camada oculta
	P = 12000
	M = 1
	C = 1

	#inicialiazação dos pesos
	w1 = (np.random.rand(P,M+1) - 0.5) / 2

	#obtenção dos pesos de saída
	w2, response = output(x, d, w1)

	#testes para valores não presentes no conjunto de treinamento
	global verbose
	verbose = True
	output(testx, testd, w1, w2)

if __name__ == "__main__":
	main()
