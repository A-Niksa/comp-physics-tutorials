clear all
close all
clc

%% Importing Experimental Data
filename = 'Data.xlsx';
sheet = 1;

exp_t = xlsread(filename,sheet,'A3:A2972');
exp_x = xlsread(filename,sheet,'B3:B2972');
exp_y = zeros(length(exp_x),1);

%% Definition of Parameters
% parameters
g = 9.81; % m/s^2 | gravitational acceleration of the Earth
mu = 0.6; % kinetic friction coefficient
d = 0.2; % m | distance between the centers of the cylinders
f = sqrt(g*mu/(2*d))/pi; % Hz | frequency
x0 = 0; % m | the coordinate center | x0 is not the same as x(0)
v0 = 0; % m | initial velocity | v(0)
t_start = 0; % s | the time at which the simulation starts | phi
t_end = 10; % s | the time at which the simulation ends
n = floor(length(exp_t)/15); % number of samples (the bigger this value is, the seemingly better the results will be.)
t = linspace(t_start,t_end,n);

%% Calculation of x(t)
x(1) = 0.1; % m | initial position | x(0)
x = x0+sqrt((x(1)-x0)^2+(v0/(2*pi*f))^2).*cos(2*pi*f.*t+t_start); % m | x as a function of time
y = zeros(1,length(x)); % m | y as a function of time

%% Visualisation
% Figure 1
fig1 = figure('PaperUnits','normalized','PaperPosition',[0 0 0.6 0.28],'Visible','off');
subplot(2,1,1)
plot(exp_t,exp_x+0.4,'Color',[0 .4 .6],'LineWidth',.95)
xlabel('t (s)','FontName','Helvetica','FontSize',9,'FontWeight','bold')
ylabel('x (m)','FontName','Helvetica','FontSize',9,'FontWeight','bold')
% legend('Experiments','FontName','Helvetica','FontSize',9)
title('Experiments','FontName','Helvetica','FontSize',9)
grid on

subplot(2,1,2)
plot(t,x,'Color',[0 .6 .6],'LineWidth',.95)
xlabel('t (s)','FontName','Helvetica','FontSize',9,'FontWeight','bold')
ylabel('x (m)','FontName','Helvetica','FontSize',9,'FontWeight','bold')
% legend('Simulation','FontName','Helvetica','FontSize',9)
title('Simulation','FontName','Helvetica','FontSize',9)
grid on

print('Fig1.png','-dpng','-r500',fig1);


% Figure 2
fig2 = figure('PaperUnits','normalized','PaperPosition',[0 0 0.6 0.1],'Visible','off');
plot(exp_t,exp_x+0.4,'Color',[0 .4 .6],'LineWidth',.95)
hold on
plot(t,x,'Color',[0 .6 .6],'LineWidth',.95)
xlabel('t (s)','FontName','Helvetica','FontSize',9,'FontWeight','bold')
ylabel('x (m)','FontName','Helvetica','FontSize',9,'FontWeight','bold')
legend('Experiments','Simulation','Fontname','Helvetica','FontSize',9)
grid on

print('Fig2.png','-dpng','-r500',fig2);

% Animation 1
outerlength = 0.19; % m | the length of the rod outside each of the centers of the cylinders
r = 0.05; % m | radius of the cylinders

figure('Visible','off');
subplot(2,1,1)
plot(t,x,'Color',[0 0 .6],'LineWidth',.95)
pointer = line(t(1),x(1),'Marker','.','MarkerSize',30,'Color',[0 .4 .6]);
xlabel('t (s)','FontName','Helvetica','FontSize',12,'FontWeight','bold')
ylabel('x (m)','FontName','Helvetica','FontSize',12,'FontWeight','bold')
grid on


subplot(2,1,2)
rod = plot([x(1)-d/2-outerlength x(1)+d/2+outerlength],[y(1) y(1)],...
    'LineWidth',1.5,'Color',[0 0 .6]);
hold on
rectangle('Position',[-d/2-r -r r r],'Curvature',[1 1],'FaceColor',[0 .6 .6],'EdgeColor',[0 .6 .6])
rectangle('Position',[d/2+r -r r r],'Curvature',[1 1],'FaceColor',[0 .6 .6],'EdgeColor',[0 .6 .6])
xlabel('x (m)','FontName','Helvetica','FontSize',9,'FontWeight','bold')
ylabel('y (m)','FontName','Helvetica','FontSize',9,'FontWeight','bold')
axis equal
title1 = title(sprintf('Time: %0.2f s',t(1)),'FontName','Helvetica','FontSize',9);
axis([2*(min(x)-outerlength) 2*(max(x)+outerlength) min(x) max(x)]);
grid on

mov1(1,length(t)) = struct('cdata',[],'colormap',[]);

for i = 1:length(t)
    set(pointer,'XData',t(i),'YData',x(i));
    set(rod,'XData',[x(i)-d/2-outerlength,x(i)+d/2+outerlength],'YData',[y(i),y(i)]);
    set(title1,'String',sprintf('Time: %0.2f s',t(i)));
    pause(0.5);
    mov1(i) = getframe(gcf);
end

anim1 = VideoWriter('Anim1.avi');
open(anim1)
writeVideo(anim1,mov1)
close(anim1)
