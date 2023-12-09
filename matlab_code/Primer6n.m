clear all, clc
N=50;
x=linspace(0,1,N);
dx=x(2)-x(1);
u=zeros (1,N);
u(1)=1;
for i= 2:N
    u(i)=u(i-1)*(1-dx);
end
figure
plot (x,u,'r',x,exp(-x),'b','linewidth',2);

% 2. reda tacnosti
us=zeros(1,N);
%granicni uslovi
us(1)=1;
us(2)=exp(-x(2));
% us(2)=us(1)*(1-dx);
for i = 3:N
    us(i)=us(i-2) - 2*dx*us(i-1);
end
hold on
plot (x,us,'g','linewidth', 2)

%implicitno
%matrica koeficijenta A
e=ones(N,1);
A=spdiags([-e (1+dx)*e],[-1 0],N,N);
% korekcija zbog granicnih uslova
A(1,1)=1;
% rezultujuca matrica B
B = zeros(N,1); B(1) = 1;
u2 = A\B;
hold on
plot(x,u2,'y','linewidth',2);
xlabel('x')
ylabel('y')
axis([0 1 0 1])

    
