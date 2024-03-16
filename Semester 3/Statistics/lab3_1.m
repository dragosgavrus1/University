# 2
#a
p = input("0.05<p<0.95 ")
for(n=1:3:100)
  x=0:n;
  y=binopdf(x,n,p);
  plot(x,y)
  pause(0.5)
endfor

