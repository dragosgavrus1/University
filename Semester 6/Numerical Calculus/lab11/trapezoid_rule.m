function I = trapezoid_rule(f, a, b, n)
  h = (b - a) / n;
  sum = 0;
  for i=1:n
    x_prev = a + (h .* (i - 1));
    x_curr = a + (h .* i);
    sum = sum + ((f(x_prev) + f(x_curr)) / 2);
  endfor
  I = sum .* h;
end
