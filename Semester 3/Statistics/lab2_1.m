# solving the final application
# n = 3 number of trials is 3
# p = 0.5 probability of success
n = 3
p = 0.5
#a
x = 0:1:n
px = binopdf(x, n ,p)
#b
xx = 0:0.01:n
cx = binocdf(xx, n, p)
#c
p1 = binocdf(0, 3, 0.5)
p2=1-binopdf(1,3,0.5)
printf('P(X = 0) = %16f\n', p2)
#d
p3 = binocdf(2, 3, 0.5)
p4 = binocdf(1, 3, 0.5)
#e
p5 = 1 - binocdf(0, 3, 0.5)
p6 = 1 - binocdf(1, 3, 0.5)
