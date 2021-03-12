function a = blocks(n,m)
a = zeros(2*n,2*m);
a(1:2*n,1:2*m) = 1;
a(1:n,m+1:2*m) = 0;
a(n+1:2*n, 1:m) = 0;
end