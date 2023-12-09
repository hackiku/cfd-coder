```matlab
clear all, clc

% Discretize space: Define the spatial domain from xl to xd, with Nx points
xl = -2; xd = 5; Nx = 11;
x = linspace(xl, xd, Nx); % Creates a vector of Nx linearly spaced points between xl and xd
dx = x(2)-x(1); % Calculate the spatial step size by subtracting adjacent points

% Discretize time: Define the time domain from 0 to tfin, with steps of size dt
t = 0; % Starting time
tfin = 11; % Final time for the simulation
dt = 0.1; % Time step size

% Define initial condition: 1 for x < 0 and 2 for x >= 0
u0 = 1*(x<0) + 2 * (x>=0); % Using conditional statements to create a step function
u = u0; % Initialize the solution array with initial condition

% Time-stepping loop: Continues until the current time t reaches tfin
while (t < tfin)
  t = t + dt; % Increment time by dt
  u(1) = 1; % Set boundary condition at the first point in space

  % Numerical scheme for solving the PDE
  % This updates the solution u for each spatial point based on the previous time step
  u(2:Nx) = u0(2:Nx) - dt/dx * (u0(2:Nx).^2 -  u0(2:Nx) - u0(1:Nx-1));

  u0 = u; % Update the solution for the next time step

  % Calculate analytical solution for each spatial point
  ua = zeros(1, Nx); % Initialize analytical solution array with zeros
  for i=1:Nx
      if x(i) < t
          ua(i) = 1; % For positions where x is less than current time, ua is 1
      elseif x(i) < 4*t+3
          ua(i) = sqrt((x(i)-3)/t); % For positions where x is less than 4*t+3, calculate ua using the given formula
      else
          ua(i) = 2; % Elsewhere, set ua to 2
      end
  end

  % Plot numerical and analytical solutions
  plot(x, u, 'b', x, ua, 'r--'); % Plot u in blue and ua in red dashed line
  xlabel('x[m]'); % Label for x-axis
  ylabel('u'); % Label for y-axis
  drawnow; % Real-time update of the plot for each iteration
end
```