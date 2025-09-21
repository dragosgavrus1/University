f=@(x)(x+1)./(3.*x.^2+2.*x+1);
nodes=linspace(-2,4,10);
f_nodes=f(nodes);
x=linspace(-2,4,500);
fi=mylagrange(nodes,f_nodes,x);
s=spline(nodes,f_nodes,x);

hold on;
plot(x,fi, 'r--');
plot(x,s, 'b--');

