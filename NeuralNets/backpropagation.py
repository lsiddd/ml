import numpy as np
import matplotlib as mpl
#mpl.use("agg")
import matplotlib.style as style
import matplotlib.pyplot as plt

sigmoid = lambda z:np.tanh(z)
Dsigmoid = lambda z: (1/ np.cosh(z)) ** 2
gaussian = lambda x: np.exp(-1 * x**(2)) * 2 - 1
test = lambda x: 0.2 + 0.4 * x**2 + 0.3 * np.sin(15 * x) + 0.05 * np.cos(50 * x)

def erro(y, d):
    error = 0
    for o, t in zip(y, d):
        for a, b in zip(o, t):
            error = error + (a - b)**2
        return error / 2

x = []
d = []
linspace = np.arange(0, 10, 0.1)

#x = [[0,0], [0,1],[1,0],[1,1]]
#d = [[0], [1], [1], [0]]

for i in linspace:
	x.append([i])
	d.append([np.sin(i)])

P = 12
M = len(x[0])
C = len(d[0])

w1 = np.random.rand(P, M + 1)
w2 = np.random.rand(C, P + 1)


nEpocas = 500
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
            response.append(y)

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
        Erro.append(erro(response,d))

print (Erro[-1])

mpl.style.use("ggplot")
plt.figure()
plt.xlabel("Epoch")
plt.ylabel("MSE")
plt.grid(True, color="#9467bd")
plt.plot( np.arange(0, nEpocas, nEpocas / len(Erro)), Erro)
plt.savefig("mse.png")

plt.figure()
plt.xlabel("Entrada")
plt.ylabel("Saída")
plt.grid(True, color="#9467bd")
plt.plot(linspace,[i[0] for i in response], "--", label="Valor Previsto", linewidth=2)
plt.plot(linspace, np.sin(linspace), "-.", label="Valor Alvo", linewidth=2)
plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='center',
       ncol=2, borderaxespad=0)


plt.show()
'''
plt.figure()
plt.xlabel("Entrada")
plt.ylabel("Saída")
plt.grid(True, color="#9467bd")
plt.plot(linspace,[i[1] for i in response[::2]], "--", label="Valor Previsto", linewidth=2)
plt.plot(linspace, sigmoid(linspace), "-.", label="Valor Alvo", linewidth=2)
plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='center',
       ncol=2, borderaxespad=0)
       '''

