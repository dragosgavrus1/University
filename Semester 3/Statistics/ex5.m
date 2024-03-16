% 5

A = [46,37,39,48,47,44,35,31,44,37];
B = [35,33,31,35,34,30,27,32,31,31];

%a
% alpha = input("Please enter the significance level: ");
alpha = 0.05

printf("\na)\n");
# vartest2 - check for comparing variances of two populations
# H0: var(A) = var(B)
# H1: var(A) != var(B)
# both tail test because we check if they differ

n1 = length(A)
n2 = length(B)

[h, pval, ci, stats] = vartest2(A, B, 'alpha', alpha, 'tail', 'both');

# compute the quantiles for the rejection region
q1 = finv(alpha/2, stats.df1, stats.df2);
q2 = finv(1 - alpha/2, stats.df1, stats.df2);

if h == 1
  printf("The null hypothesis is rejected, ie. variances do differ!\n");
  printf("The data suggests that the standard is not met\n");

else
  printf("The null hypothesis is not rejected, ie. variances do not differ!\n");
  printf("The data suggests that the standard is met\n");
end

printf("The rejection region is (-inf, %4.3f) U (%4.3f, +inf)\n", q1, q2);
printf("The observed value of the test statistic is %4.3f\n", stats.fstat);
printf("The pval of the test is %4.3f\n\n\n", pval);

% b

printf("\nb.\n");
# The confidence interval for the difference of the average (means)
# The null hypothesis H0: mu1 = mu2
# The alternative hypothesis H1: mu1 != mu2
# To compare the means we have to perform a ttetst2
# Two tailed test
# We set vartype to equal because our variances are equal
#[H, PVAL, CI, STATS] = ttest2(A, B, 'alpha', alpha, 'vartype', 'unequal');

#printf("The confidence interval [%4.3f, %4.3f]\n", CI(1), CI(2));
#printf('The rejection region is (-inf, %4.3f) U (%4.3f, inf)\n', -STATS.tstat, STATS.tstat);

# s ^ 2 = var(X) in octave

# we get from point a that the variances differ so the sigmas differ
# we calculate the quantiles
c = (var(A)/n1)/(var(A)/n1 + var(B)/n2)
n = (c*c/(n1-1))+((1-c)*(1-c)/(n2-1))

q = tinv(1-alpha/2,1/n)

left = mean(A) - mean(B) - q * sqrt(var(A)/n1 + var(B)/n2)
right = mean(A) - mean(B) + q * sqrt(var(A)/n1 + var(B)/n2)

printf("The confidence interval for the difference of means when sigma1 != sigma2\n")
printf("unknown is (%4.3f, %4.3f)\n", left, right)
