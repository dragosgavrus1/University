function I=trapezoid_rule(f,a,b,n)
    h=(b-a)/n;
    I=f(a)+f(b);
    ans=0;
    for i = 0 : n-1
      x = a +(i+1/2)*h;
      ans = ans + f(x);
    endfor
    I=I+ans*2;
    I=I*(h/2);
end
