function fi = lagrange_newton(nodes,f_nodes,xi)
  fi=zeros(size(xi));
  n=length(nodes);
  m=length(xi);
  li=ones(size(nodes));
  dd=divdiff(nodes,f_nodes);

  for j = 1:m
    fi(j)=dd(1,1);
    for i = 2:n
      fi(j)=fi(j)+dd(1,i)*prod(xi(j)-nodes([1:i-1]));
    endfor
  endfor

