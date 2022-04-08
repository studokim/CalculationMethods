# Реализовать метод решения СЛАУ, на выбор:
# LU-разложение или метод квадратного корня.
# Для матриц A, L, U вычислить числа обусловленности.
#
# Протестировать на разных матрицах:
# хорошо обусловленных, [очень] плохо обусловленных.
#
# Для нескольких плохо обусловленных матриц
# (например, для матриц Гильберта разного, больше 15, порядка)
# реализовать метод регуляризации:
#
# параметр α варьировать в пределах от 10−12 до 10−1 ;
# для каждого конкретного значения α найти числа обусловленности
# (матриц A + αE ) и норму погрешности получившегося решения;
# понять, какое значение α = α в каждом конкретном случае
# (= для каждой конкретной матрицы) кажется наилучшим.
# Наилучшее α можно находить из предположений, что точным решением является
# вектор x0 = (1,1,...,1);
# случайный вектор x0.
#
# Проверить результат на [другом] случайном векторе x 0 .

from common_lib import *
from task01_lib import build_hilbert, compute_cond_s, print_cond
from task02_lib import *


def test(A: np.array, b: np.array):
    L, U = build_LU(A)
    cond = compute_cond_s(A)
    print_cond(cond, "A:")
    print_cond(compute_cond_s(L), "L:")
    print_cond(compute_cond_s(U), "U:")
    x = solve(A, b)
    x_bib = np.linalg.solve(A, b)
    print_diff(x, x_bib)
    if (cond > k_bad_cond):
        x_ = solve_regularizing(A, b, verbosity=2)
        x0 = build_random_vector(len(A))
        print(f"Проверим результат на {x0}:")
        x_test = solve_regularizing(A, b, x0, verbosity=1)
        print_diff(x_, x_test, "решение методом регуляризации",
                   "проверочное решение")


print_task(2)

A = build_hilbert(3)
b = [1 for i in range(3)]
print_test("Гильберта 3-го порядка")
test(A, b)

A = build_hilbert(10)
b = [1 for i in range(10)]
print_test("Гильберта 10-го порядка")
test(A, b)

A = build_hilbert(20)
b = [1 for i in range(20)]
print_test("Гильберта 20-го порядка")
test(A, b)

A = np.array([[3.278164, 1.046583, -1.378574],
              [1.046583, 2.975937, 0.934251],
              [-1.378574, 0.934251, 4.836173]])
b = np.array([-0.527466, 2.526877, 5.165441])
print_test()
test(A, b)
