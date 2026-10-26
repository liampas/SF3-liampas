import matplotlib.pyplot as plt

mes_x = [x for x in range(250)]
mes_x_carres = [x**2 for x in range(250)]

ma_figure = plt.figure()
plt.plot(mes_x, mes_x_carres, marker="*", linestyle=":", color="r")
plt.plot([0, 100, 150, 250], [5000, 3000, 40000, 60000], "^y--")
plt.title("Exemples de graphiques")
plt.xlabel("Axe des y")
plt.ylabel("Y")
plt.legend(["y = x**2", "Autres points"])

plt.show()








