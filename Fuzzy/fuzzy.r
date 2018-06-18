#install package FuzzyR if not already installed
if(!require(FuzzyR)){
  install.packages("FuzzyR")
  library(FuzzyR)
}
#criar objeto first
fis= newfis("study")

#adicionar as variaveis de entrada e saida
fis= addvar(fis, 'input', 'conhecimento previo', c(0,25))
fis= addvar(fis, 'input', 'dificuldade', c(0,25))
fis= addvar(fis, 'input', 'dificuldade para colar', c(0,25))
fis= addvar(fis, 'output', 'horas de antecedencia para estudar', c(0,25))

#adicionar as funcoes de pertinencia
fis= addmf(fis, 'input', 1, 'zerado', 'gaussmf', c(3,3))
fis= addmf(fis, 'input', 1, 'mais ou menos', 'gaussmf', c(3,13))
fis= addmf(fis, 'input', 1, 'expert', 'gaussmf', c(3,19)) 

fis= addmf(fis, 'input', 2, 'facil', 'trapmf', c(0,0,4,7))
fis= addmf(fis, 'input', 2, 'mais ou menos', 'trapmf', c(5, 7, 11, 15))
fis= addmf(fis, 'input', 2, 'dificil', 'trapmf', c(10,16,21,25))

fis= addmf(fis, 'input', 3, 'facil', 'trimf', c(0, 6, 9))
fis= addmf(fis, 'input', 3, 'mais ou menos', 'trimf', c(8, 13, 18))
fis= addmf(fis, 'input', 3, 'dificil', 'trimf', c(17, 20, 25))

fis= addmf(fis, 'output', 1, 'durante a prova', 'trapmf', c(0, 0, 6, 12))
fis= addmf(fis, 'output', 1, 'noite anterior', 'gaussmf', c(3, 12))
fis= addmf(fis, 'output', 1, 'cedo', 'trimf', c(15, 20, 25))

#columns:
# 1st -> first input variable
# 2nd -> second input variable
# 3rd -> thrid input variable
# 4th -> output variable
# 5th -> weigth of the rule
# 6th -> 1 for AND, 2 for OR

rules= rbind(c(3, 1, 0, 1, 1, 1),
             c(3, 2, 0, 2, 1, 1),
             c(3, 3, 0, 2, 1, 1),
             c(0, 1, 1, 1, 1, 1),
             c(0, 2, 1, 1, 1, 1),
             c(0, 3, 1, 2, 1, 1),
             c(1, 3, 0, 3, 1, 1),
             c(2, 3, 0, 3, 1, 1),
             c(0, 1, 3, 2, 1, 1),
             c(0, 3, 2, 3, 1, 1),
             c(0, 2, 2, 3, 1, 1),
             c(0, 1, 2, 2, 1, 1),
             c(0, 3, 1, 2, 1, 1),
             c(0, 2, 1, 2, 1, 1))

#adicionar regras ao objeto
fis= addrule(fis, rules)
showrule(fis)

#plot das funcoes de pertinencia
png('mf1.png')
plotmf(fis, 'input', 1)
dev.off()

png('mf2.png')
plotmf(fis, 'input', 2)
dev.off()

png('mf3.png')
plotmf(fis, 'input', 3)
dev.off()

png('out1.png')
plotmf(fis, 'output', 1)
dev.off()

#Interface grafica da biblioteca
showGUI(fis)
