import matplotlib.pyplot as plt
from matplotlib import rc
import numpy as np

rc('text', usetex=True)

fig, ax = plt.subplots(1, 1, figsize=(5,3))

w1 = np.linspace(0, 0.6, 100)
w2 = np.linspace(0.6, 1, 100)
y1 = (5/3) * w1
y2 = -6.25 * (w2 ** 2) + 7.5 * w2 - 1.25

ax.plot(w1, y1, label=r"$p(w) = \frac{5}{3}w$", color="#475f91", linewidth=2)
ax.plot(w2, y2, label=r"$p(w) = -\frac{25}{4}w^2 + \frac{15}{2}w - \frac{5}{4}$", color="#b85758", linewidth=2)
ax.plot([0.6], [1], "ok")

ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')
# ax.axvline(x=0.6, ymin=0.06, linestyle='dotted', color='k')
ax.axhline(y=0.75, xmin=0.06, linestyle='dotted', color='k')
# ax.tick_params(
#     top=False,
#     right=False,
#     labelleft=False,
# )
ax.set_yticks([0.75, 1])
ax.set_xticks([0.6, 1])
ax.set_xlabel("$w$")
ax.set_ylabel("$p(w)$")
plt.legend(loc=(0.3, 0.1))

# plt.show()
plt.savefig("./zelda_experiments/final_plots/performance_function.jpg", dpi=150)