```matlab
clear, clc, close all
% Solving a nonlinear system of equations

% Explicit method
N = 50; % Number of points
u = zeros(1, N); % Initialize solution array
u(1) = 1; % Initial condition
x = linspace(0, 1, N); % Linearly spaced vector from 0 to 1
dx = x(2) - x(1); % Spatial step size

% Iteratively update u using the explicit scheme
for i = 2:N
    u(i) = u(i-1) * (1 - dx * u(i-1)); % Update based on previous point
end

% Plot explicit solution
figure(1)
plot(x, u, 'y', 'linewidth', 2)
hold on
plot(x, 1./(x+1), 'g', 'linewidth', 2) % Plot analytical solution for comparison

% Implicit method
e = ones(N, 1); % Vector of ones for matrix construction
ug = rand(N, 1); % Initial guess
eps = 0.001 * e; % Convergence criterion
i = 1; % Iteration counter
A = spdiags([-e (1 + dx * ug) .* e], [-1 0], N, N); % Construct sparse matrix
B = zeros(N, 1); % Initialize B
B(1) = 1; % Boundary condition
A(1, 1) = 1; % Boundary condition correction
u2 = A\B; % Solve using backslash operator

% Iteratively solve until convergence
while sum(abs(ug - u2) > eps)
    i = i + 1;
    ug = u2;
    A = spdiags([-e (1 + dx * ug) .* e], [-1 0], N, N); % Update matrix A
    A(1, 1) = 1; % Boundary condition correction
    u2 = A\B; % Solve again
end

% Plot implicit solution
hold on
plot(x, ug, '--r', 'linewidth', 2)
```