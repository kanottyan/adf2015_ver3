#coding:utf-8
import random as rd
import numpy as np
import matplotlib.pyplot as pl
from pylab import *

eqs = []
eqs.append(u"TwitterID:@kanottyan")
eqs.append(u"Name: KanoNoboru")
eqs.append(u"Language: Chinese, Python, PHP")
eqs.append(u"part-time: Livesense")
eqs.append(u"reserach: TextMining")
eqs.append(u"part-time: Livesense")
eqs.append(u"Favorite: Purin, HorikitaMaki")
eqs.append(u"Tool: Only Matplotlib")


eqs.append((r"$\frac{d\rho}{d t} + \rho \vec{v}\cdot\nabla\vec{v} = -\nabla p + \mu\nabla^2 \vec{v} + \rho \vec{g}$"))
eqs.append((r"$F_G = G\frac{m_1m_2}{r^2}$"))

pl.axes([0.025, 0.025, 0.95, 0.95])

for i in range(45):
    index = np.random.randint(0, len(eqs))
    eq = eqs[index]
    size = np.random.uniform(15, 40)
    x,y = np.random.uniform(0, 1, 2)
    alpha = np.random.uniform(0.25, .75)
    colors = ["#11557c","#DC143C","#87CEFA"]
    color = rd.sample(colors, 1)
    color = "".join(color)
    pl.text(x, y, eq, ha='center', va='center', color=color, alpha=alpha,
         transform=pl.gca().transAxes, fontsize=size, clip_on=True)
pl.xticks(())
pl.yticks(())
pl.show()