# we are solving excercise nr 2
# we aim to plot the pdf and the cdf
# of a variable X
n = input("Give mb if trials n=")
p = input("Give the probability of succes p=")
x = 0:1:n
px = binopdf(x, n, p)
plot(x, px, '*r')
hold on
xx = 0:0.01:n
cx = binocdf(xx, n, p)
plot(xx, cx, 'g')
# homework put a legend on the graph

