#simulating 3 coin tosses
N = 3 # nr of simulations
U = rand(3, N)
Y = (U < 0.5)
X = sum(Y)
clf
hist(X)
