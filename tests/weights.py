#listas de entradas e saidas esperadas
x = [0, 1, 2, 3, 4]
d = [1, 1.75, 2.53, 3.34, 4.2]

if (len(x) != len(d)):
	raise Exception("inputs and outputs must have same lengths")

#taxa de aprendizagem
mi = 0.1
w0_start = 1.5
w1_start = 0.5

def adjust(x, d, w0_start, w1_start):
	#pesos iniciais do perceptron
	w0 = [w0_start]
	w1 = [w1_start]
	y0 = w1_start * x[0] + w0_start
	e0 = d[0] - y0
	e = [e0]
	n = 0
	print ("Iteração 0")
	print ("O erro nesta iteração é de " + str(e0))
	print ("O peso w1 é :" + str(w1_start))
	print ("O peso bias é:" + str(w0_start))
	print ("\n")

	for n in range(1, len(x) ):
		w0.append(w0[n-1] + mi * e[n-1])
		w1.append(w1[n-1] + mi * e[n-1] * x[n-1])
		y = w1[n] * x[n] + w0[n]
		e.append(d[n] - y)
		print ("Iteração " + str(n + 1))
		print ("O erro nesta iteração é de " + str(e[n]))
		print ("O peso w1 é: " + str(w1[n]))
		print ("O peso bias é: " + str(w0[n]))
		print ("\n")
	w0.append(w0[n] + mi * e[n])
	w1.append(w1[n] + mi * e[n] * x[n])
	return (w0[-1], w1[-1])
print ("---------------PRIMEIRA ÉPOCA---------------")
w0_start, w1_start = adjust(x, d, w0_start, w1_start)
print("----------------SEGUNDA ÉPOCA----------------")
adjust(x, d, w0_start, w1_start)


