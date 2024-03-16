# 1.a
alpha = input("Significance level: ")
X = [7 7 4 5 9 9 ...
4 12 8 1 8 7 ...
3 13 2 1 17 7 ...
12 5 6 2 1 13 ...
14 10 2 4 9 11 ...
3 5 12 6 10 7];

n = length(X);
% the null hipothesys is h0;
% (it is thogheter with mew > 8.5 ) the efficiency standard is met
% the alternative hypothesys h1 : mew < 8.5 (the efficiency standard is not met)
% this is a left tail test for mew

% this is a left tail test for the mean when sigma is known
sigma = 5
m0 = 8.5
[h, p, ci ,zval] = ztest(X, m0, sigma, "alpha", alpha, "tail", "left");
z = norminv(alpha,0,1);
RR = [ -inf z];
% the value of h is %decimal
if h==1
  printf("the null hypothesis is rejected\n" );
  printf("the data sugests the data is not met \n");
else
  printf("the null hypothesis is not rejected \n")
  printf("the data sugests the data is met \n");
endif

printf("the rejection region is %4.4f[] \n",RR);
printf("the value of the precentage statistic is %4.4f \n", zval)
printf("the pval of the test is %4.4f \n",p)
