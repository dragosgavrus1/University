#b
f=@(x)(x+1)./(3.*x.^2+2.*x+1);
nodes=linspace(-2,4,10);
f_nodes=f(nodes);
x=linspace(-2,4,500);
fi=mylagrange(nodes,f_nodes,x);
#plot(x,fi)
f1=(x+1)./(3.*x.^2+2.*x+1);
plot(x, abs(f1-fi));
max(abs(f1-fi));

#li(x)=prod(xi(j)-nodes([1:j-1,j+1:n])

f_half=(0.5+1)./(3.*0.5.^2+2.*0.5+1);
fi_half=mylagrange(nodes,f_nodes,0.5);
abs(f_half-fi_half)

