function a = two_rows(m)
if ndims(m) == 2
    b = size(m);
    if b(1) == 2
        a = m;
    else
      a = zeros(size(m));
      disp("Массив должен быть двумерным и иметь две строки");
    end
else
    a = zeros(size(m));
    disp("Массив должен быть двумерным и иметь две строки");
end
    