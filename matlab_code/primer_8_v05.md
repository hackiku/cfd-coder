```matlab
clear all, clc

% Discretize space
xl = -2; xd = 5; Nx = 11;
x = linspace(xl, xd, Nx);
dx = x(2)-x(1);

% Discretize time
t = 0;
tfin = 11;
dt = 0.01;

% Boundary conditions
u0 = 1*(x<0) + 2 * (x>=0); % Step function for initial condition
u = u0; % Initialize solution array

% Iterative time loop
while (t < tfin)
  t = t + dt; % Increment time
  u(1) = 1; % Boundary condition at the start of the domain

  % Upwind scheme for numerical solution
  for j = 2:Nx
      u(j) = u0(j) - ( u0(j)*dt/dx ) * (u0(j) - u0(j-1));
  end

  u0 = u; % Update solution for the next time step

  % Construct analytical solution
  ua = zeros(1, Nx); % Initialize analytical solution array
  for i=1:Nx
      if x(i) < t
        ua(i) = 1;
      elseif x(i) < 2*t
              ua(i) = 1.5; % Simplified assumption, verify with theory
      else
          ua(i) = 2;
      end
  end

  % Plot numerical and analytical solutions
  plot(x, u, 'b-', x, ua, 'r--', 'LineWidth', 2);
  legend('Numerical', 'Analytical');
  xlabel('x [m]'); ylabel('u');
  title('Numerical vs Analytical Solution');
  drawnow; % Real-time update of the plot
end
```