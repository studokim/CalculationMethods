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

from .common_lib import *
from .common_data import SOLE
from .task01_lib import compute_cond_s, print_cond
from .task02_lib import *


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

print_test("Гильберта 3-го порядка")
A, b = SOLE.hilbert(3)
test(A, b)

print_test("Гильберта 10-го порядка")
A, b = SOLE.hilbert(10)
test(A, b)

print_test("Гильберта 20-го порядка")
A, b = SOLE.hilbert(20)
test(A, b)

print_test()
A, b = SOLE.pakulina_3()
test(A, b)
