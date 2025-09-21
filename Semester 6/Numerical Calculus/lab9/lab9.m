x = [0.5, 1.5, 2, 3, 3.5, 4.5, 5, 6, 7, 8];
f = [5, 5.8, 5.8, 6.8, 6.9, 7.6, 7.8, 8.2, 9.2, 9.9];

# a
scatter(x,f)
p=polyfit(x,f,1)
polyval(p,x)

# c
polyval(p,4)

# b
diff = norm(f - polyval(p, x))

# d
plot(x,f,'o');
hold on;
plot(x, polyval(p,x))


