% v05.pdf, slide 12
% u^2ux + ut = 0

clear all, clc

% diskretizovati prostor
xl = -2; xd = 5; Nx = 11;
x = linspace(xl, xd, Nx);
dx = x(2)-x(1);

% diskretizovati vreme
t = 0;
tfin = 11;
dt = 0.1;

u0 = 1*(x<0) + 2 * (x>=0);
u = u0; % deklaracija niza

while (t < tfin)
  t = t + dt; % posto je uslov po vremenu
  u(1) = 1; % granicni uslov iz zadatka
  % ...:Nx)^2
  u(2:Nx) = u0(2:Nx) - dt/dx * (u0(2:Nx).^2 -  u0(2:Nx) - u0(1:Nx-1));
  u0 = u; % fiktivna naredba jer je u niz
 
  % axis([xl, xd, 0, 1]);

  % porediti analiticko & numericko
  for i=1:Nx
      if x(i) < t
          ua(i) = 1;
      elseif x(i) < 4*t+3
          ua(i) = sqrt((x(i)-3)/t); % analytical sol (inverse)
      else
          ua(i) = 2;
      end
  end
  plot(x, u, 'b', x, ua, 'r--');
  xlabel('x[m]')
  ylabel('u')
  drawnow;
end