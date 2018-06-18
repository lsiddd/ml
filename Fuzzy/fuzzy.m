fis = newfis("Study");

fis = addvar(fis, 'input', 'conhecimento previo', [0 25]);
fis = addvar(fis, 'input', 'dificuldade', [0 25]);
fis = addvar(fis, 'input', 'dificuldade para colar', [0 25]);
fis = addvar(fis, 'output', 'horas de antecedencia para estudar', [0 25]);

fis = addmf(fis, 'input', 1,'zerado', 'gaussmf', [3 3]);
fis = addmf(fis, 'input', 1,'mais ou menos', 'gaussmf', [3 13]);
fis = addmf(fis, 'input', 1,'expert', 'gaussmf', [3 19]);

fis = addmf(fis, 'input', 2,'facil', 'trapmf', [0 0 4 7]);
fis = addmf(fis, 'input', 2,'mais ou menos', 'trapmf', [5 7 11 15]);
fis = addmf(fis, 'input', 2,'dificil', 'trapmf', [10 16 21 25]);

fis = addmf(fis, 'input', 3,'facil', 'trimf', [0 6 9]);
fis = addmf(fis, 'input', 3,'mais ou menos', 'trimf', [8 13 18]);
fis = addmf(fis, 'input', 3,'dificil', 'trimf', [17 20 25]);

fis = addmf(fis, 'output', 1,'durante a prova', 'trapmf', [0 0 6 12]);
fis = addmf(fis, 'output', 1,'noite anterior', 'gaussmf', [3 12]);
fis = addmf(fis, 'output', 1,'cedo', 'trimf', [15 20 25]);

% 1 - conhecimento previo [0 1 2 3]
% 2 - dificuldade [0 1 2 3]
% 3 - dificuldade para colar [0 1 2 3]
% 4 - saida [1 2 3]
% 5 - Peso da Regras
% 6 - 1 para AND e 2 para OR

ruleList=[
    3 1 0 1 1 1 %1
    3 2 0 2 1 1 %2
    3 3 0 2 1 1 %3
    0 1 1 1 1 1 %4
    0 2 1 1 1 1 %5
    0 1 1 1 1 1 %6
    1 3 0 3 1 1 %7
    2 3 0 3 1 1 %8
    0 1 3 2 1 1 %9
    0 3 2 3 1 1 %10
    0 2 2 3 1 1 %11
    0 1 2 2 1 1 %12
    0 3 1 2 1 1 %13
    0 2 1 2 1 1 %14
]

fis = addrule(fis, ruleList)

showrule(fis)

figure(1)
plotmf(fis, 'input', 1);grid  on;
figure(2)
plotmf(fis, 'input', 2);grid  on;
figure(3)
plotmf(fis, 'input', 3);grid  on;
figure(4)
plotmf(fis, 'output', 1);grid  on;

writefis(fis,'sample');

figure(5)
[output,fuzzifiedInputs,ruleOutputs,aggregatedOutput] = evalfis([12 18 16],fis);
outputRange = linspace(fis.output.range(1),fis.output.range(2),length(aggregatedOutput))'; 
plot(outputRange,aggregatedOutput,[output output],[0 1])
xlabel('Horas de antecedência')
ylabel('Output Membership')
legend('Aggregated output fuzzy set','Defuzzified output')