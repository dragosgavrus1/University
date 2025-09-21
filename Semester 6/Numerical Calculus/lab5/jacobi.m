function [x,nit] = jacobi(A,b,x_0,err,maxnit)
  n = length(b)
  M = diag(diag(A));
  N = M - A;
  c = inv(M) * b;
  T = inv(M) * N;
  x = x_0
  a = (1-norm(T,inf)) / norm(T,inf) * err;
  for k=1:maxnit
    x = T*x + c;

    if norm(x-x_0, inf) <= a
      nit = k;
      return
    endif
    x_0 = x;
  endfor

  error("Too dificult")

