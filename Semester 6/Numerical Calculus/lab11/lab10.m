f=@(x)e.^(-x.^2);
a=zeros(1,10);
b=[0.1:0.1:1];

(2/sqrt(pi))*ad_trapezoid(f,a,b,0.1,10)
erf(b)
