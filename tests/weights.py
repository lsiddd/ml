import matplotlib as mpl
import matplotlib.pyplot as plt
font = {'size'   : 15}
mpl.rc('font', **font)

#listas de entradas e saidas esperadas
x = [0, 1, 2, 3, 4]
d = [1, 1.75, 2.53, 3.34, 4.2]

if (len(x) != len(d)):
	raise Exception("inputs and outputs must have same lengths")

#taxa de aprendizagem
mi = 0.1
w0_start = 1.5
w1_start = 0.5

def adjust(w0_start, w1_start, filename, pltitle):
	#acessamos os valores globais de x e d para evitar passar como parâmetro a cada chamada
	global x
	global d

	#pesos iniciais do perceptron
	w0 = [w0_start]
	w1 = [w1_start]
	y0 = w1_start * x[0] + w0_start
	e0 = d[0] - y0
	e = [e0]
	y = [y0]
	n = 0
	print ("Iteração 1")
	print ("O erro nesta iteração é de " + str(e0))
	print ("O peso w1 é :" + str(w1_start))
	print ("O peso bias é:" + str(w0_start))
	print ("\n")

	for n in range(1, len(x) ):
		w0.append(w0[n-1] + mi * e[n-1])
		w1.append(w1[n-1] + mi * e[n-1] * x[n-1])
		y.append(w1[n] * x[n] + w0[n])
		e.append(d[n] - y[n])
		print ("Iteração " + str(n + 1))
		print ("O erro nesta iteração é de " + str(e[n]))
		print ("O peso w1 é: " + str(w1[n]))
		print ("O peso bias é: " + str(w0[n]))
		print ("\n")
	w0.append(w0[n] + mi * e[n])
	w1.append(w1[n] + mi * e[n] * x[n])

	plt.plot(x, d, label="dados")
	plt.plot(x, y, '--', label="predição")
	plt.legend()
	plt.xlabel("Entradas")
	plt.ylabel("Saídas")
	plt.title(pltitle)
	plt.show()
	plt.savefig("plots/" + filename)
	plt.close()
	return (w0[-1], w1[-1])

print ("---------------PRIMEIRA ÉPOCA---------------")
w0_start, w1_start = adjust(w0_start, w1_start, "a.png", "Primeira Época")
print("----------------SEGUNDA ÉPOCA----------------")
w0_start, w1_start = adjust(w0_start, w1_start, "b.png", "Segunda Época")
print("----------------TERCEIRA ÉPOCA----------------")
w0_start, w1_start = adjust(w0_start, w1_start, "c.png", "Terceira Época")
print("----------------QUARTA ÉPOCA----------------")
w0_start, w1_start = adjust(w0_start, w1_start, "d.png", "Quarta Época")
print("----------------QUINTA ÉPOCA----------------")
w0_start, w1_start = adjust(w0_start, w1_start, "e.png", "Quinta Época")
