syms x
f = exp(x)

p1 = taylor(f, x, 0, 'order', 2)
p2 = taylor(f, x, 0, 'order', 3)
p3 = taylor(f, x, 0, 'order', 4)
p4 = taylor(f, x, 0, 'order', 7)


clf
ezplot(f, [-3, 3])
hold on

ezplot(p1, [-3, 3])
ezplot(p2, [-3, 3])
ezplot(p3, [-3, 3])
ezplot(p4, [-3, 3])

vpa(exp(1), 7)
vpa(subs(p4, x, 1), 7)
