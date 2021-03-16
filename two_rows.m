function a = two_rows(m)
b = size(m);
if ndims(m) == 2 && b(1) == 2
        a = m;
    else
      a = zeros(size(m));
      disp("Массив должен быть двумерным и иметь две строки");
    end
else
    a = zeros(size(m));
    disp("Массив должен быть двумерным и иметь две строки");
end
    
