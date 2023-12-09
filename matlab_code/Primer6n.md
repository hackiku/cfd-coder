```matlab
clear all, clc

N = 50; % Number of points
x = linspace(0, 1, N); % Linearly spaced vector from 0 to 1
dx = x(2) - x(1); % Spatial step size

% Explicit First-Order Method
u = zeros(1, N); % Initialize solution array
u(1) = 1; % Initial condition
% Iteratively update u
for i = 2:N
    u(i) = u(i-1) * (1 - dx); % First-order update formula
end
% Plot explicit first-order solution
figure
plot(x, u, 'r', x, exp(-x), 'b', 'linewidth', 2);

% Explicit Second-Order Method
us = zeros(1, N); % Initialize solution array for second-order method
% Boundary conditions
us(1) = 1; % First boundary condition
us(2) = exp(-x(2)); % Second boundary condition, based on analytical solution
% Iteratively update us
for i = 3:N
    us(i) = us(i-2) - 2 * dx * us(i-1); % Second-order update formula
end
% Plot explicit second-order solution
hold on
plot(x, us, 'g', 'linewidth', 2)

% Implicit Method
e = ones(N, 1); % Vector of ones for matrix construction
% Construct matrix A for implicit method
A = spdiags([-e (1 + dx) * e], [-1 0], N, N);
% Boundary condition correction
A(1, 1) = 1;
% Resulting matrix B
B = zeros(N, 1); B(1) = 1;
% Solve using implicit method
u2 = A\B;
% Plot implicit solution
hold on
plot(x, u2, 'y', 'linewidth', 2);
xlabel('x')
ylabel('y')
axis([0 1 0 1])
```