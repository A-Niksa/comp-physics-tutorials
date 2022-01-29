clear all
close all
clc

%% System Parameters
% Physical properties
omega = 5; % Hz | angular frequency
mu = 0.18; % kinetic friction coefficient
g = 9.81; % m/s^2 | gravitational acceleration
length = 0.5; % m | the length between the centers of the cylinders
L = length/2; % m | half-length between the centers of the cylinders
r = .15; % m | radius of each of the cylinders
T = 2*pi*sqrt(L/(mu*g));% s | period of oscillation

% Function properties
n = 200; % number of samples | the higher this number is, the more accurate the results would seemingly be.
t_end = 10; % s | the time at which the simulation ends
t = linspace(0,t_end,n); % s | the time span for the simulation

%% Generating x(t)
x = sqrt(omega^2*r^2*L/(g*mu)).*sin(sqrt(mu*g/L).*t);

%% Visualization
figure
plot(t,x,'Color',[0 0 .6],'LineWidth',1.05)
legend(sprintf('T = %f',T),'FontSize',9.75,'FontName','Times New Roman');
ylabel('x (m)','FontName','Times New Roman','FontSize',14,'FontWeight','bold')
xlabel('t (s)','FontName','Times New Roman','FontSize',14,'FontWeight','bold')
grid on
