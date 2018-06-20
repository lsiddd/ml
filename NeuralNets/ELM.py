#!/usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import sys
from datasets import fish
#função sigmoide
sigmoid = lambda z:(np.exp(z) - np.exp(-1 * z)) / (np.exp(z) + np.exp(-1 * z))
erro = lambda y, d: 1/2 * sum([np.sum (i **2) for i in np.nditer(y - d)])

def output(x, d, w1, w2=[]):
	sh = list(x.shape)
	sh[1] = sh[1] + 1
	Xa = np.ones(sh)
	Xa[:,:-1] = x
	S = sigmoid(np.matmul(Xa, w1.transpose()))

	sh = list(S.shape)
	sh[1] = sh[1] + 1
	Ha = np.ones(sh)
	Ha[:,:-1] = S

	if(w2 == []):
		w2 = np.matmul(np.matmul(np.linalg.inv(np.matmul(Ha.transpose(), Ha)), Ha.transpose()), d).transpose()

	Y = np.matmul(Ha, w2.transpose())

	print (f'pesos da camada oculta: \n{w1}')
	print (f'pesos da camada de saída: \n{w2}')
	print (f'resposta da camada oculta:\n {S}')
	print (f'resposta da camada de saída:\n {Y}')
	print (f' O erro RMS da rede é {erro(Y, d)}\n\n')
	return w2

def main():
	'''
	x_training = np.array(fish.alaska + fish.canada)
	d = []
	for i in fish.alaska:
		d.append([1, 0])
	for i in fish.canada:
		d.append([0, 1])
	d_training = np.array(d)
	'''
	x = [[0,0], [0,1],[1,0],[1,1]]
	d = [[0,0], [1,0],[1,0],[1,1]]
	x = np.array(x)
	d = np.array(d)
	P = 150
	M = 2
	C = 2

	#w1 = np.matrix('0.53  0.86 -0.43;\
	#			1.83  0.31  0.34;\
	#			-2.25 -1.3  3.57')
	w1 = np.random.rand(P,M+1)


	w2 = output(x, d, w1)

if __name__ == "__main__":
	main()
