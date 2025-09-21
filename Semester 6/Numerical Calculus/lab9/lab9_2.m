f=@(x)(x.*sin(pi*x));
nodes=[-1,-1/2,0,1/2,1,3/2];
f_nodes=f(nodes);
x=linspace(-1,3/2,100);
s=spline(nodes,f_nodes,x);
p=pchip(nodes,f_nodes,x);
f_div_nodes=[pi,f_nodes, -1]
c=spline(nodes,f_div_nodes,x)

hold on;
plot(nodes, f_nodes, 'k--');
plot(x, s, 'b--');
plot(x, p, 'r--');
plot(x, c, 'g--');
