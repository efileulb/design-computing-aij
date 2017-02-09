import matplotlib.pyplot as plt

pos = {0: (0, 1), 1: (2, 2), 2: (2, 0), 3: (5, 2), 4: (5, 0), 5: (7, 1)}
plt.figure(facecolor="w")
plt.axis('off')
nx.draw_networkx(G, pos, node_size=2500, node_color='w')
plt.show()
