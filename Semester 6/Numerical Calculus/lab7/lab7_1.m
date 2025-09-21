#a
nodes=[0,1/3,1/2,1]
f = @(x)cos(pi *x);
f_nodes=f(nodes)
x=linspace(0,1,50)
#c
res=lagrange_newton(nodes,f_nodes,x)
fi=f(x)
plot(x,res)
hold on;
plot(x,fi)
#d
f_d=f(1/5)
l3_d=lagrange_newton(nodes,f_nodes,[1/5])
abs(f_d-l3_d)
