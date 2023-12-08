clear all, clc

% diskretizovati prostor
xl = -2; xd = 5; Nx = 11;
x = linspace(xl, xd, Nx);
dx = x(2)-x(1);

% diskretizovati vreme
t = 0;
tfin = 11;
dt = 0.01;

% boundary conditions
u0 = 1*(x<0) + 2 * (x>=0); % why? refresh taylor
u = u0; % deklaracija niza

% u0(j)*dt/dx % courant number

while (t < tfin)
  t = t + dt; % increment time
  u(1) = 1; % granicni uslov iz zadatka
  
  % u(2:Nx) = u0(2:Nx) - dt/dx * (u0(2:Nx) -  u0(2:Nx) - u0(1:Nx-1));

  % upwind scheme
  for j = 2:Nx
      u(j) = u0(j) - ( u0(j)*dt/dx ) * (u0(j) - u0(j-1));
  end

  u0 = u; % update solution for next time step

  % analytical solution
  for i=1:Nx
      if x(i) < t
        ua(i) = 1;
      elseif x(i) < 2*t
              % ua(i) = x(i)/t; 
              ua(i) = 1.5;
      else
          ua(i) = 2;
      end
  end
  plot(x, u, 'b-', x, ua, 'r--', 'LineWidth', 2);
  legend('Numerical', 'Analytical');
  xlabel('x [m]'); ylabel('u');
  title('Numerical vs Analytical Solution');
  drawnow; % Real-time update

end