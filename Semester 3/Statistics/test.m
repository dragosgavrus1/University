# 9

X1 = [4.6, 0.7, 4.2, 1.9, 4.8, 6.1, 4.7, 5.5, 5.4];
X2 = [2.5, 1.3, 2.0, 1.8, 2.7, 3.2, 3.0, 3.5, 3.4];

# vartest2 - check for comparing variances of two populations
# h0 : variances are the same
# h1 : variances differ

# both tail test

# a

printf("\na)\n");

n1 = length(X1);
n2 = length(X2);
alpha = 0.05;

[h, pval, ci, stats] = vartest2(X1, X2, 'alpha', alpha, 'tail', 'both');

# because we use both tail test quantile is calculated with alpha/2

q1 = finv(alpha/2, stats.df1, stats.df2);
q2 = finv(1 - alpha/2, stats.df1, stats.df2);

if h == 1
  printf("The null hypothesis is rejected, ie. variances do differ!\n");
  printf("The data suggests that the standard is not met\n");

else
  printf("The null hypothesis is not rejected\n");
  printf("The data suggests that the standard is met\n");
end

printf("The rejection region is (-inf, %4.3f) U (%4.3f, +inf)\n", q1, q2);
printf("The observed value of the test statistic is %4.3f\n", stats.fstat);
printf("The pval of the test is %4.3f\n", pval);

# b

# 95% significance => 1 - alpha = 0.95 => alpha = 0.05 stays the same

# the variances do differ  from point a
# sigma ^ 2 = population variance (theoretical variance)

printf("\nb)\n");
printf("Because variances differ resulting from point a we know the sigmas are not equal\n");

# The confidence interval for the difference of means when sigma1 != sigma2

c = (var(X1)/n1)/(var(X1)/n1 + var(X2)/n2)
n = (c*c/(n1-1))+((1-c)*(1-c)/(n2-1))

q = tinv(1-alpha/2,1/n)

left = mean(X1) - mean(X2) - q * sqrt(var(X1)/n1 + var(X2)/n2)
right = mean(X1) - mean(X2) + q * sqrt(var(X1)/n1 + var(X2)/n2)

printf("The confidence interval for the difference of means ie. average heat loss when sigma1 != sigma2\n");
printf("unknown is (%4.3f, %4.3f)\n", left, right);
