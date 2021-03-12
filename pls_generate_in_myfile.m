function pls_generate_in_myfile()
F = fopen('Новый текстовый документ.txt', 'w');
A = rand(3);
fprintf(F,'%.4f %.4f %.4f\n %.4f %.4f %.4f\n %.4f %.4f %.4f  ', A(1:3,1:3))