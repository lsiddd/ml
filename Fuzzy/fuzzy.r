#install package FuzzyR if not already installed
if(!require(FuzzyR)){
  install.packages("FuzzyR")
  library(somepackage)
}

fis= newfis("study")

fis= addvar(fis, 'input', 'conhecimento prévio', c(0,10))
fis= addvar(fis, 'input', 'dificuldade', c(0,10))
fis= addvar(fis, 'input', 'dificuldade para colar', c(0,10))
fis= addvar(fis, 'output', 'horas de antecedência para estudar', c(0,24))

fis= addmf(fis, 'input', 1, 'zerado', 'gaussmf', c(1.5,0))
fis= addmf(fis, 'input', 1, 'mais ou menos', 'gaussmf', c(1.5,5))
fis= addmf(fis, 'input', 1, 'expert', 'gaussmf', c(1.5,10)) 

fis= addmf(fis, 'input', 2, 'fácil', 'trapmf', c(0,0,1,3))
fis= addmf(fis, 'input', 2, 'mais ou menos', 'trapmf', c(2, 3, 7, 8))
fis= addmf(fis, 'input', 2, 'difícil', 'trapmf', c(7,9,10,10))

fis= addmf(fis, 'input', 3, 'fácil', 'gaussmf', c(1, 0))
fis= addmf(fis, 'input', 3, 'mais ou menos', 'gaussmf', c(1, 5))
fis= addmf(fis, 'input', 3, 'difícil', 'gaussmf', c(1, 10))

fis= addmf(fis, 'output', 1, 'durante a prova', 'gaussmf', c(1.5,0))
fis= addmf(fis, 'output', 1, 'noite anterior', 'gaussmf', c(1.5,12))
fis= addmf(fis, 'output', 1, 'cedo', 'gaussmf', c(1.5,24))

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
fis= addrule(fis, rules)
showrule(fis)

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

showGUI(fis)
