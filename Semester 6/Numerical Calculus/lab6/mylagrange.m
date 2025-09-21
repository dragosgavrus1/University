function fi = mylagrange(nodes,f_nodes,xi)
  fi=zeros(size(xi))
  n=length(nodes)
  m=length(xi)
  li=ones(size(nodes));
  for j=1:m
    for i=1:n
      li(i)=prod(xi(j)-nodes([1:i-1,i+1:n]))./prod(nodes(i)-nodes([1:i-1,i+1:n]));
    endfor
    fi(j)=li*f_nodes';
  endfor

