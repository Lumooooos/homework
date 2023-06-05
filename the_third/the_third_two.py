import random

random.seed(42)
num_points = 1000000
num_points_in_circle = 0

for i in range(num_points):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x ** 2 + y ** 2 <= 1:
        num_points_in_circle += 1

pi_estimate = 4 * num_points_in_circle / num_points

print(f"圆周率的估计值为：{pi_estimate:.2f}")
