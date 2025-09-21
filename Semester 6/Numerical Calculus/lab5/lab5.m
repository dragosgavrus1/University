n=7;
A=5*eye(n) -diag(ones(n-1, 1), 1)-diag(ones(n-1, 1), -1);
b=[4;3 * ones(n-2, 1); 4];

A
b

x_0 = zeros(size(b));
err = 10 ^ -5;
maxnit = 1000;

[x, nit] = jacobi(A, b, x_0, err, maxnit)

x_0 = zeros(size(b));
err = 10 ^ -5;
maxnit = 1000;

[x, nit] = gauss(A, b, x_0, err, maxnit)
