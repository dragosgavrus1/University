function A = lagrange_atiken(x0,f0,x)
  p=zeros(length(x0));
  p(:,1)=f0';
  n=length(x0);

  for i = 2:n;
    for j = 2:i;
      matrix=[x-x0(i-j+1), p(i-1, j-1); x-x0(i), p(i, j-1)]
      p(i,j)=det(matrix)/(x0(i)-x0(i-j+1));
    endfor
  endfor
  A=p(n,n);

