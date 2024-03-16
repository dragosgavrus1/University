# 3

X = [3.26, 1.89, 2.42, 2.03, 3.07, 2.95, 1.39, 3.06, 2.46, 3.35, 1.56, 1.79, 1.76, 3.82, 2.42, 2.96]

# a
# the null hypothesis is H0: miu = 3 (it goes together with
# miu > 3, the standard is met)
# the alternative hypothesis is H1: miu < 3 (the standard is
# not met)
# sigma is the population stantard deviation
# std(X) - standard deviation
printf("\na)\n");

one_minus_alpha = 0.95;
alpha = 1 - one_minus_alpha;
n = length(X);

m1b = mean(X) - std(X) / sqrt(n) * tinv(1 - alpha / 2, n - 1);
m2b = mean(X) - std(X) / sqrt(n) * tinv(alpha / 2, n - 1);

printf("The confidence interval for the theoretical mean when sigma is unknown\n")
printf("is (%4.3f, %4.3f)\n", m1b, m2b)

#b
# ttest - check for mean against a given value when sigma unknown
printf("b)\n");

alpha = 0.01
m0 = 3;

[h, pval, ci, stats] = ttest(X, m0, 'alpha', alpha, 'tail', 'left');

# since is left tail test we compute the quantile for alpha

z_alpha_b = tinv(alpha, stats.df);
RR_b = [-Inf, z_alpha_b];

if h == 1
  printf("The nickel particles seem to be smaller than 3\n");
  printf("The data suggests that the standard is not met\n");

else
  printf("The nickel particles don't seem to be smaller than 3\n");
  printf("The data suggests that the standard is met\n");
end

printf("The rejection region is (%4.3f, %4.3f)\n", RR_b);
printf("The observed value of the test statistic is %4.3f\n", stats.tstat);
printf("The pval of the test is %4.3f\n", pval);

