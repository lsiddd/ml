#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import sys
from datasets import fish

sigmoid = lambda z:np.tanh(z)
Dsigmoid = lambda z: (1/ np.cosh(z)) ** 2

def erro(y, d):
	error = 0
	for o, t in zip(y,d):
		for a, b in zip(o, t):
			error = error + (a - b)**2
	return error / 2

def main():
	x = fish.alaska + fish.canada

	d = []
	for i in fish.alaska:
		d.append([1, 0])
	for i in fish.canada:
		d.append([0, 1])
	
	P = 30
	M = len(x[0])
	C = len(d[0])

	w1 = np.random.rand(P, M + 1)
	w2 = np.random.rand(C, P + 1)


	nEpocas = 100
	mi = 0.1
	Erro = []
	for n in range(nEpocas):
		response = []
		for N in range(len(x)):

			h = []
			y = []
			e = []

			delta2 = []
			delta1 = []
			#forward pass
			#para cada neurônio na camada oculta
			for i in range(len(w1)):
				s = 0
				#para cada peso do neurônio
				for k in range(len(w1[0]) - 1):
					s = s + w1[i][k] * x[N][k]
				s = s + w1[i][k+1]
				h.append(sigmoid(s))

			#para cada neurônio na camada de saída
			for c in range(len(w2)):
				r = 0
				#para cada peso do neurônio
				for l in range(len(w2[0]) - 1):
					r = r + w2[c][l] * h[l]
				r = r + w2[c][l+1]
				y.append(sigmoid(r))
				e.append(y[c] - d[N][c])

			#cálculo dos deltas
			for c in range(len(w2)):
				delta2.append(e[c] * Dsigmoid(h[i]))
			for i in range(len(w1)):
				soma = 0
				for c in range(len(w2)):
					soma = soma + delta2[c] * w2[c][i]
				delta1.append(Dsigmoid(h[i])* soma)

			for c in range(len(w2)):
				for i in range(len(w1)):
					w2[c][i] = w2[c][i] - mi * h[i] * delta2[c]
				w2[c][i+1] = w2[c][i+1] - mi * delta2[c]
			for c in range(len(w1)):
				for i in range(len(x[0])):
					w1[c][i] = w1[c][i] - mi * h[i] * delta1[c]
				w1[c][i+1] = w1[c][i+1] - mi * delta1[c]
			response.append(y)
	acertos = 0
	for i, j in zip(response, d):
		if (np.argmax(i) == np.argmax(j)):
			acertos = acertos + 1
	print(f"taxa de acerto no conjunto de testes --> {acertos/len(d)}")
if (__name__ == "__main__"):
	main()

