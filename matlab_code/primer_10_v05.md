```matlab
% v05, primer 10, sl.23
% ekspanzioni talas u_ux + u_t = 0
clear all, clc

% Discretize space
xl = -1; xd = 10; Nx = 20; % Define spatial domain and number of points
x = linspace(xl, xd, Nx); % Create linearly spaced vector for spatial domain
dx = x(2)-x(1); % Calculate spatial step size

% Discretize time
t = 0; % Starting time
tfin = 5; % End time for the simulation
dt = 0.01; % Time step size

% Initial condition based on x position
u0 = 2*(x<0) + 1*(x>=0); % Step function: 2 for x < 0 and 1 for x >= 0
u = u0; % Initialize solution array with initial condition

% Time-stepping loop
while (t < tfin)
  t = t + dt; % Increment time
  u(1) = 2; % Set boundary condition at the start of the domain

  % Numerical scheme for solving the PDE
  u(2:Nx) = u0(2:Nx) - dt/dx * u0(2:Nx).*(u0(2:Nx) - u0(1:Nx-1));

  u0 = u; % Update solution for the next time step

  % Calculate analytical solution
  ua = zeros(1, Nx); % Initialize analytical solution array
  for i=1:Nx
      if x(i) < 3/2*t
          ua(i) = 2; % For x < 3/2*t, ua is 2
      else
          ua(i) = 1; % Elsewhere, ua is 1
      end
  end

  % Set plot axis limits and plot numerical and analytical solutions
  axis([xl, xd, 0, 1]); % Set axis limits
  plot(x, u, 'b', x, ua, 'r--'); % Plot numerical solution (u) in blue and analytical solution (ua) in red dashed line
  xlabel('x[m]'); % Label for x-axis
  ylabel('u'); % Label for y-axis
  drawnow; % Real-time update of the plot
end

```