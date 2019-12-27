clc;clear;close all;

x = [1.00000e+03, 1.00000e+04, 1.00000e+05, 1.00000e+06, 1.00000e+07, 1.00000e+08, 1.00000e+09];
x = log(x);
y = [8.39E-02, 8.09E-03 , 3.61E-03 1.00E-03 , 1.02E-03, 1.08E-04, 1.04E-04];
y = log(y);

p = polyfit(y,x,1);
f1 = polyval(p,y);
figure()
plot(y,x,'o')
hold on
plot(y,f1)
legend('Dane', 'Linia trendu')
xlabel('B³¹d przybli¿enia ln(\epsilon)')
ylabel('Liczba powtórzeñ ln(N)')
p

% createFit(x, y)
% set(gca, 'XScale', 'log')
% 
% %%
% % dane z funkcji createFit: (y = a*x^b)
% 
% a =  0.1921;
% b = -0.2728
% x2 = linspace(1000,10000000000, 10000000);
% y2= a*x2.^b;
% 
% %% wykres
% 
% plot(x,y, 'go')
% hold on
% plot(x2, y2, 'b--')
% set(gca, 'XScale', 'log')
% legend('Dane', 'Linia trendu')
% xlabel('Liczba powtórzeñ')
% ylabel('B³¹d przybli¿enia')
