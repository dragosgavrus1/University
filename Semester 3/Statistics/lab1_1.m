x = 0:0.01:3
plot(x,x.^5/10,"--g;x^5/10;",x,sin(x).*x,"-.r;x sinx;",x,cos(x),":b;cosx;")
title("lab 1")
