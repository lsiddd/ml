import matplotlib as mpl
mpl.use("agg")
import matplotlib.pyplot as plt
import numpy as np
font = {'size'   : 14}
mpl.rc('font', **font)

#listas de entradas e saidas esperadas
x = [0, 1, 2, 3, 4]
d = [1, 1.75, 2.53, 3.34, 4.2]


if (len(x) != len(d)):
	raise Exception("vetores de entradas e saídas devem ter o mesmo comprimento")

#taxa de aprendizagem e pesos iniciais
mi = 0.1
w0 = 1.5
w1 = 0.5

Eepc = []
w0_total = []
w1_total = []
grad = []

for k in range(31):
	Ek = 0
	y = []
	for n in range(len(x)):
		y.append(w0 + w1 * x[n])
		e = d[n] - y[n]
		w1 = w1 + mi * e * x[n]
		w0 = w0 + mi * e * 1
		Ek = Ek + 1/2 * e * e

		w0_total.append(w0)
		w1_total.append(w1)

	grad.append(-1 * e * x[n])
	Eepc.append(Ek)
	plt.figure(figsize=(6,6))
	plt.plot(x, d, label="dados")
	plt.plot(x, y, '-.', label="predição")
	plt.legend()
	plt.grid()
	plt.xlabel("Entradas")
	plt.ylabel("Saídas")
	plt.title(str(k+1) + "ª Época")
	plt.show()
	plt.savefig("plots/" + str(k) + ".png")

plt.figure(figsize=(9,6))
plt.plot(w0_total, label="bias")
plt.plot(w1_total, "-.", label="w1")
plt.legend()
plt.grid()
plt.xlabel("Iteração")
plt.ylabel("Pesos")
plt.xlim(0, 150)
plt.ylim(0, 2)
plt.title("Pesos de Entrada em Cada Iteração")
plt.savefig("pesos.pdf")

plt.figure(figsize=(9,6))
plt.plot(grad, label="Gradiente")
plt.legend()
plt.xlim(0, 30)
plt.grid()
plt.xlabel("Época")
plt.ylabel("Gradiente")
plt.title("Gradiente ao Final de Cada Época")
plt.savefig("grad.pdf")
print(w1)
print(w0)
