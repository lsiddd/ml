#install package FuzzyR if not already installed
if(!require(FuzzyR)){
  install.packages("FuzzyR")
  library(somepackage)
}

fis= newfis("study")

fis= addvar(fis, 'input', 'previous knowledge', c(0,10))
fis= addvar(fis, 'input', 'dificulty', c(0,10))
fis= addvar(fis, 'input', 'how difficult it is to cheat', c(0,10))
fis= addvar(fis, 'output', 'how many hours before the test I should study', c(0,24))

fis= addmf(fis, 'input', 1, 'none', 'gaussmf', c(1.5,0))
fis= addmf(fis, 'input', 1, 'some knowledge', 'gaussmf', c(1.5,5))
fis= addmf(fis, 'input', 1, 'expert', 'gaussmf', c(1.5,10)) 

fis= addmf(fis, 'input', 2, 'easy', 'trapmf', c(0,0,1,3))
fis= addmf(fis, 'input', 2, 'more or less easy', 'trapmf', c(2, 3, 7, 8))
fis= addmf(fis, 'input', 2, 'difficult', 'trapmf', c(7,9,10,10))

fis= addmf(fis, 'input', 3, 'easy', 'gaussmf', c(1, 0))
fis= addmf(fis, 'input', 3, 'more or less', 'gaussmf', c(2, 5))
fis= addmf(fis, 'input', 3, 'difficult', 'gaussmf', c(1, 10))

fis= addmf(fis, 'output', 1, 'during it', 'gaussmf', c(1.5,0))
fis= addmf(fis, 'output', 1, 'the night before', 'gaussmf', c(1.5,12))
fis= addmf(fis, 'output', 1, 'early', 'gaussmf', c(1.5,24))

#columns:
# 1st -> first input variable
# 2nd -> second input variable
# 3rd -> thrid input variable
# 4th -> output variable
# 5th -> weigth of the rule
# 6th -> 1 for AND, 2 for OR

rules= rbind(c(1, 1, 1, 2, 1, 1),
             c(1, 1, 2, 2, 1, 1),
             c(1, 1, 3, 3, 1, 1),
             c(1, 2, 1, 2, 1, 1),
             c(1, 2, 2, 3, 1, 1),
             c(1, 2, 3, 3, 1, 1),
             c(1, 3, 1, 2, 1, 1),
             c(1, 3, 2, 3, 1, 1),
             c(1, 3, 3, 3, 1, 1),
             
             c(2, 1, 1, 3, 1, 1),
             c(2, 1, 2, 2, 1, 1),
             c(2, 1, 3, 2, 1, 1),
             c(2, 2, 1, 2, 1, 1),
             c(2, 2, 2, 2, 1, 1),
             c(2, 2, 3, 1, 1, 1),
             c(2, 3, 1, 3, 1, 1),
             c(2, 3, 2, 3, 1, 1),
             c(2, 3, 3, 3, 1, 1),
             
             c(3, 1, 1, 1, 1, 1),
             c(3, 1, 2, 1, 1, 1),
             c(3, 1, 3, 2, 1, 1),
             c(3, 2, 1, 2, 1, 1),
             c(3, 2, 2, 2, 1, 1),
             c(3, 2, 3, 3, 1, 1),
             c(3, 3, 1, 2, 1, 1),
             c(3, 3, 2, 2, 1, 1),
             c(3, 3, 3, 3, 1, 1))
fis= addrule(fis, rules)
#showfis(fis)
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
