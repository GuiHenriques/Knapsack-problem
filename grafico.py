
# importing package
import matplotlib.pyplot as plt
import numpy as np
from main import *

  
# create data
w = len(mochila.get_itens())
x = np.arange(w)
y1 = [i.get_peso_item() for i in(mochila.get_itens())]
y2 = [i.get_preco_item() for i in(mochila.get_itens())]
width = 0.40
  
# plot data in grouped manner of bar type
plt.bar(x-0.2, y1, width)
plt.bar(x+0.2, y2, width)
plt.xticks(x, [i.get_etiqueta() for i in(mochila.get_itens())])
plt.legend(["Peso do item", "Valor do item"])

plt.show()