n=7;
A = 5*eye(n) - diag(ones(n-1,1),1) - diag(ones(n-1,1),-1);
b = [ 4, 3* ones(1,n-2),4]';

[ L, U, P] = lu(A);

y = forsub(L,b)
x = backsub(U, y)
