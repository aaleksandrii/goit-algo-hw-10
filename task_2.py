import random
import scipy.integrate as spi


def f(x):
    return x**2


a = 0
b = 2


def monte_carlo_integral(n=100_000, seed=42):
    if type(n) is not int or n <= 0:
        raise ValueError("Кількість точок n має бути додатним цілим числом.")

    height = f(b)
    rectangle_area = (b - a) * height

    rng = random.Random(seed)
    points_under = 0

    for _ in range(n):
        x = rng.uniform(a, b)
        y = rng.uniform(0, height)

        if y <= f(x):
            points_under += 1

    hit_fraction = points_under / n
    estimate = rectangle_area * hit_fraction
    return estimate


if __name__ == "__main__":
    n = 100_000
    mc_result = monte_carlo_integral(n=n, seed=42)

    analytical = b**3 / 3 - a**3 / 3
    quad_result, quad_error = spi.quad(f, a, b)
    absolute_error = abs(mc_result - analytical)

    relative_error_percent = absolute_error / abs(analytical) * 100

    print(f"Кількість випадкових точок: {n}")
    print(f"Монте-Карло: {mc_result:.6f}")
    print(f"Аналітично, 8/3: {analytical:.6f}")
    print(f"SciPy quad: {quad_result:.6f}")
    print(f"Оцінка абсолютної похибки самого quad: {quad_error:.2e}")
    print(f"Абсолютне відхилення Монте-Карло від 8/3: {absolute_error:.6f}")
    print(f"Відносне відхилення Монте-Карло: {relative_error_percent:.3f}%")