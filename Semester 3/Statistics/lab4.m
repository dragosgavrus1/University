# 2
# a
N = input("N is between 0 and 1 ");
p = input("p is between 0 and 1 ");

U = rand(1,N);
X = (U<p);

U_X = [0 1]
n_X = hist(X, length(U_X));
rel_freq = n_X/N
