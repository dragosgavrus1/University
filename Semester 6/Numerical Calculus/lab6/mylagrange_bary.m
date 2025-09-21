function fi = mylagrange_bary(nodes,f_nodes,xi)
  fi=zeros(size(xi))
  n=length(nodes)
  m=length(xi)
  li=ones(size(nodes));
  w=ones(1,n);
  for i=1:n
    for j=[1:i-1, i+1:n]
      w(i)=w(i)/(nodes(i)-nodes(j));
    endfor
  endfor

  for j=1:m
    for i=1:n
      ux=prod(xi(j)-nodes);
      li(i)=w./(xi(j)-nodes)*f_nodes';
    endfor
    fi(j)=ux*li(i);
  endfor

