import numpy as np
import matplotlib.pyplot as plt

# 设置幂律分布的参数
alpha = 2.5  # 幂律指数
size = 1000   # 生成随机数的数量
low = 0.01    # 下界
high = 1.0    # 上界

# 生成符合幂律分布的随机数
random_numbers = (np.random.uniform(low, high, size) ** (-1/(alpha-1)))
random_numbers = random_numbers / sum(random_numbers)
# 可选：查看生成的随机数的直方图
plt.hist(random_numbers, bins=50, density=True)
plt.title("Power Law Distribution")
plt.xlabel("Value")
plt.ylabel("Density")
plt.show()

# 输出生成的随机数
print(random_numbers[:10])  # 查看前十个生成的数
