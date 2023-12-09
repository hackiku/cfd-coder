```matlab
% Initializing grid and simulation parameters
Nx = 301; % Number of grid points
x = linspace(0, 300, Nx); % Spatial domain from 0 to 300
a = 300; % Speed of wave propagation (could be sound speed, for example)
dx = x(2) - x(1); % Spatial step size
dt = 1e-3; % Time step size
c = a * dt / dx; % Courant number for stability analysis, must be < 1
tfinal = 1; % Final time for simulation
t = 0; % Initializing time variable

% Setting initial conditions for the simulation
U00 = zeros(1, Nx); % Initialize solution array with zeros

% Applying initial condition using a sinusoidal function between x=100 and x=220
for i = 1:Nx
    if (x(i) >= 100 && x(i) <= 220)
        U00(i) = 100 * sin(pi * (x(i) - 100) / 120); % Sinusoidal initial condition
    end
end

% Preparing for the first time step based on initial conditions
U0 = zeros(1, Nx); % Initialize next time step array with zeros
U0(2:Nx-1) = U00(2:Nx-1) + c^2 / 2 * (U00(3:Nx) - 2 * U00(2:Nx-1) + U00(1:Nx-2)); % Applying finite difference scheme
U = U0; % Updating solution to the next time step

% Starting the time-stepping loop to advance the solution in time
while (t < tfinal)
    U(1) = 0; % Applying boundary condition at the start of the domain
    U(Nx) = 0; % Applying boundary condition at the end of the domain
    % Calculating the solution at the next time step using the finite difference method
    U(2:Nx-1) = 2 * U0(2:Nx-1) - U00(2:Nx-1) + c^2 * (U0(3:Nx) - 2 * U0(2:Nx-1) + U0(1:Nx-2));
    t = t + dt; % Advancing time
    U00 = U0; % Updating the previous time step solution
    U0 = U; % Updating the current solution
    figure(3)
    plot(x, U) % Plotting the current state of the solution
    drawnow % Updating the plot in real time
end

% Plotting the initial and final states of the solution for comparison
figure(1)
plot(x, U0); % Final state
figure(2)
plot(x, U00); % Initial state
```