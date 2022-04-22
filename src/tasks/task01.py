# Для СЛАУ с некоторой матрицей A:
# вычислить числа обусловленности;
# поварьировав матрицу и правую часть (например, на 10−2..10−10 ),
# вычислить |x − x̃|;
# посмотреть, есть ли корреляция между
# величинами чисел обусловленности и погрешностью решения.

# Для тестов можно брать:
# матрицы Гильберта разного порядка (например, от 3 до 10);
# системы из методички А.Н.Пакулиной, часть 1;
# какие-нибудь хорошие матрицы
# (например, трехдиагональные с диагональным преобладанием).
#
# Статья, в которой предлагается метод подсчёта углового числа обусловленности
# https://www.elibrary.ru/download/elibrary_15524850_60661752.pdf

from .common_data import SOLE
from .common_lib import print_task, print_test
from .task01_lib import *


def test(A: np.array, b: np.array):
    print_cond(compute_cond_s(A), "spectre")
    print_cond(compute_cond_v(A), "volume")
    print_cond(compute_cond_a(A), "angle")
    X = np.linalg.solve(A, b)
    delta = 10**(-4)
    A_ = build_variated(A, delta)
    X_ = np.linalg.solve(A_, b)
    print_diff(X, X_, delta)


print_task(1)

print_test("Гильберта 3-го порядка")
A, b = SOLE.hilbert(3)
test(A, b)

print_test("Гильберта 6-го порядка")
A, b = SOLE.hilbert(6)
test(A, b)

print_test("Гильберта 10-го порядка")
A, b = SOLE.hilbert(10)
test(A, b)

# матрица из Пакулиной, стр. 90, вар. 1
print_test()
A, b = SOLE.pakulina_2()
test(A, b)

# матрица из Пакулиной, стр. 94, вар. 1
print_test()
A, b = SOLE.pakulina_3()
test(A, b)

print_test("Трёхдиагональная")
A, b = SOLE.tridiag_5()
test(A, b)

print_test("Трёхдиагональная")
A, b = SOLE.tridiag_5()
test(A, b)
