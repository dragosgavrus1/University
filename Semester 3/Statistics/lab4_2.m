#2
#c
N = input("N is nr of simulations ");
p = input("p is between 0 and 1 ");

X = zeros(N);

for( i = 1:N)
  X(i) = 0;
  while ( rand(1) > p )
    X(i) = X(i) + 1;
  endwhile;
endfor;

k = 0:20;
p_k = geopdf(k,p);
U_X = unique(X);

n_X = hist(X, length(U_X));
rel_freq = n_X/N;

plot(U_X,rel_freq,'*',k,p_k,'o');
