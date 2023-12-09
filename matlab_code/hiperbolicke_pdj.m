%% Ulazni podaci mreze
Nx=301;
x=linspace(0,300,Nx);
a=300;
dx=x(2)-x(1);
dt=1e-3;
c=a*dt/dx; % MORA BITI < 1 inace div
tfinal=1;
t=0;

%% Pocetni uslovi
U00=zeros(1,Nx);

%% Proracun
for i=1:Nx
    if (x(i)>=100 && x(i)<=220)
        U00(i) = 100*sin(pi*(x(i)-100)/120);
    end
end
U0=zeros(1,Nx);
U0(2:Nx-1)=U00(2:Nx-1)+c^2/2 * (U00(3:Nx)-2*U00(2:Nx-1)+U00(1:Nx-2));
U=U0;

while (t<tfinal)
    %t=0;
    U(1)=0;
    U(Nx)=0;
    U(2:Nx-1)=2*U0(2:Nx-1)-U00(2:Nx-1)+c^2*(U0(3:Nx)-2*U0(2:Nx-1)+U0(1:Nx-2));
    t=t+dt;
    U00=U0;
    U0=U;
    figure(3)
    plot(x,U)
    drawnow
end

figure(1)
plot(x,U0);
figure(2)
plot(x,U00);