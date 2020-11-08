import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

prob_20 = [np.random.normal(0, 1) for i in range(20)]
prob_100 = [np.random.normal(0, 1) for i in range(100)]


def statistics(list):
    df = pd.DataFrame(data=list)

    stat_tab = {'mean': df.mean(), 'median': df.median(), 'std': df.std(), 'var': df.var(),
                'skew': df.skew(), 'kurtosis': df.kurtosis(), 'max': df.max()}

    return stat_tab

print('Prob 20' , statistics(prob_20))
print('Prob 100', statistics(prob_100))

fig, ax = plt.subplots(1,2, figsize=(10,5))
ax[0].hist(prob_20, 10, facecolor='green')
ax[0].title.set_text("Prob 20")
ax[0].axis([-3, 3, 0, 5])
ax[0].grid(True)
ax[1].hist(prob_100, 12, facecolor='green')
ax[1].title.set_text("Prob 100")
ax[1].axis([-3, 3, 0, 25])
ax[1].grid(True)
plt.show()

sns.distplot(prob_100, label='Prob 100')
sns.distplot(prob_20, label='Prob 20')
plt.legend()

