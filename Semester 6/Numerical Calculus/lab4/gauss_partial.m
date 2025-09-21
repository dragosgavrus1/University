function x = gauss_partial(A,b)
  [r,n] = size(A);
  x= zeros(size(b));
  A = [A,b];
  for i = 1 : n-1
    [m, p] = max(abs(A(i:n,i)));
    p = p + i - 1;
    if p ~= i
      A([i p],:) = A([p i], :);
    endif

    for j = i + 1 : n
      coeff = A(j,i)/A(i,i);
      A(j,i:n+1)= A(j,i:n+1) - coeff * A(i,i:n+1);
    endfor

  endfor
  x = backsub(A(:,1:n),A(:,n+1));
end
