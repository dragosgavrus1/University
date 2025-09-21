syms x
f = log(1 + x)

p1 = taylor(f, x, 0, 'order', 3);
p2 = taylor(f, x, 0, 'order', 6);

clf
ezplot(f, [-0.9, 1]);
hold on

ezplot(p1, [-0.9, 1]);
ezplot(p2, [-0.9, 1])

# b
# p_b = taylor(f, x, 0, 'order', 1000);
# vpa(log(2), 5)
# vpa(subs(p_c, x, 1), 5)

# c
p1_c = subs(p1, x, -x)
p2_c = subs(p2, x, -x)

# d | ln(a/b) = ln(a) - ln(b)
p1_d = p1 - p1_c
p2_d = p2 - p2_c

# e
# 1 + x / 1 - x = 2 => 1 + x = 2 - 2x => 3x = 1 => x = 1/3
