% v05, primer 10, sl.23
% ekspanzioni talas u_ux + u_t = 0
clear all, clc

% diskretizovati prostor
xl = -1; xd = 10; Nx = 20;
x = linspace(xl, xd, Nx);
dx = x(2)-x(1);

% diskretizovati vreme
t = 0;
tfin = 5;
dt = 0.01;

u0 = 2*(x<0) + 1*(x>=0);
u = u0; % deklaracija niza

while (t < tfin)
  t = t + dt; % posto je uslov po vremenu
  u(1) = 2; % granicni uslov iz zadatka
  u(2:Nx) = u0(2:Nx) - dt/dx * u0(2:Nx).*(u0(2:Nx) - u0(1:Nx-1));
  u0 = u; % fiktivna naredba jer je u niz

  % porediti analiticko & numericko
  for i=1:Nx
      if x(i) < 3/2*t
          ua(i) = 2;
      else
          ua(i) = 1;
      end
  end
  axis([xl, xd, 0, 1]);
  plot(x, u, 'b', x, ua, 'r--');
  xlabel('x[m]')
  ylabel('u')
  drawnow;
end