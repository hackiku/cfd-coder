clear, clc, close all
% Nelinearni sistem jednacina

% 1.eksplicitno
N=50;
u=zeros(1,N);
u(1)=1;
x=linspace(0,1,N);
dx=x(2)-x(1);
for i=2:N
    u(i)=u(i-1)*(1-dx*u(i-1));
end
figure (1)
plot(x,u,'y','linewidth',2)
hold on
plot(x,1./(x+1),'g','linewidth',2)

% 2.Implicitno
e = ones(N,1);
ug = rand(N,1); 
eps = 0.001*e;
i = 1;
A = spdiags([-e (1+dx*ug).*e],[-1 0],N,N);
B = zeros(N,1);
B(1) = 1;
A(1,1) = 1; % korekcija, zbog granicnog uslova
u2 = A\B;
while sum(abs(ug-u2)>eps)
i = i+1;
ug = u2;
A = spdiags([-e (1+dx*ug).*e],[-1 0],N,N);
A(1,1) = 1; % korekcija, zbog granicnog uslova
u2 = A\B;
end
hold on
plot(x,ug,'--r','linewidth',2)

