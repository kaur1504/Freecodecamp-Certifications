import matplotlib.pyplot as plt # type: ignore
from medical_data_visualizer import draw_cat_plot, draw_heat_map

fig1 = draw_cat_plot()
fig1.savefig('catplot.png')

fig2 = draw_heat_map()
fig2.savefig('heatmap.png')
