syms x
f = sin(x)

p1 = taylor(f, x, 0, 'order', 4)
p2 = taylor(f, x, 0, 'order', 6)

clf
ezplot(f, [-pi, pi])
hold on

ezplot(p1, [-pi, pi])
ezplot(p2, [-pi, pi])

vpa(sin(pi / 5), 6)
vpa(subs(p2, x, pi / 5), 6)
