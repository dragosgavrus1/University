x0=linspace(-4,4,9)
f=@(x)(pow2(x))
f0=f(x0)
res=lagrange_atiken(x0,f0,1/2)
