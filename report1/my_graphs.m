clc;clear;close all;

x = [1.00000e+03, 1.00000e+04, 1.00000e+05, 1.00000e+06, 1.00000e+07, 1.00000e+08, 1.00000e+09];
y = [2.79088e-02, 1.92912e-02, 6.89116e-03, 3.98716e-03, 2.22358e-04, 1.39002e-04, 7.82624e-05];

createFit(x, y)
set(gca, 'XScale', 'log')

%%
% dane z funkcji createFit: (y = a*x^b)

a =  0.1921;
b = -0.2728
x2 = linspace(1000,10000000000, 10000000);
y2= a*x2.^b;

%% wykres

plot(x,y, 'go')
hold on
plot(x2, y2, 'b--')
set(gca, 'XScale', 'log')
legend('Dane', 'Linia trendu')
xlabel('Liczba powtórzeñ')
ylabel('B³¹d przybli¿enia')
