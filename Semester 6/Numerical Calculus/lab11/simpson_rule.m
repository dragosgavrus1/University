function I=simpson_rule(f,a,b,m)
    h=(b-a)/(2*m);
    I1=0;
    I2=0;
    for i = 1 : m-1
      x1 = a + h*(2*i-1);
      x2 = a + h*2*i;
      I1 = I1 + f(x1);
      I2 = I2 + f(x2);
    endfor
    I1 = I1 + f(2*m-1);
    I = (h/3)*(f(a)+f(b)+4*I1+2*I2);
end
