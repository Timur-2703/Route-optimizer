import matplotlib.pyplot as plt

fig, (ax1, ax2) = plt.subplots(1, 2,  figsize=(14, 6))


def draw_on_ax(ax, route, title):
    x = [city.x for city in route]
    y = [city.y for city in route]
    names = [city.name for city in route]

    x.append(x[0])
    y.append(y[0])

    ax.plot(x, y, 'b-')
    ax.scatter(x,y,c='red', s=100)
    ax.set_title(title)

    for i, name in enumerate(names):
        plt.annotate(name, (x[i], y[i]))



