import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

Df = pd.read_csv('E:\python_exercise\mangguoTV\cov.csv',encoding='utf')
df = Df.fillna(0)
plt.subplots(figsize=(34, 34))
cov_sisiter = df.corr()
cov_sisiter_0 = round(cov_sisiter,3)
sns.set(font='simhei',font_scale=3)
camp = sns.cubehelix_palette(start = 1.5, rot = 3, gamma=0.8, as_cmap = True)
sns.heatmap(cov_sisiter_0,linewidths=0.05, annot=True, vmax=1, square=True, cmap=camp)
# ax.set_title('图X 特征变量的相关系数')
plt.show()

