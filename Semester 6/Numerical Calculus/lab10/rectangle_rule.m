function I=rectangle_rule(f,a,b,n)
    h=(b-a)/n;
    I=0;
    for i = 0 : n-1
      x = a +(i+1/2)*h;
      I=I+f(x);
    endfor
    I=h*I;
end
