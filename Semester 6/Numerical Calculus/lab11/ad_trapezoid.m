function I=ad_trapezoid(f,a,b,error,m)
  I1=trapezoid_rule(f,a,b,m);
  I2=trapezoid_rule(f,a,b,2*m);
  if abs(I1-I2)<error
    I=I2;
  else
    I=trapezoid_rule(f,a,(a+b)/2,error,m) + trapezoid_rule(f,a,(a+b)/2,b,m);
  endif

